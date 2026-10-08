"""Mirror already published, filtered Git snapshots into private Drive archives."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, subprocess, tempfile, time
from datetime import datetime, timezone
from pathlib import Path

FIELDS = 'id,name,size,md5Checksum,appProperties,parents,permissions(type,role)'

def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix('.pending.json')
    temp.write_text(json.dumps(data, indent=2), encoding='utf-8')
    os.replace(temp, path)

def gws(method, params=None, body=None, upload=None):
    binary = os.environ.get('GWS_EXECUTABLE') or shutil.which('gws')
    if not binary:
        raise RuntimeError('Google Workspace CLI is unavailable')
    command = [binary, 'drive', 'files', method]
    if params: command += ['--params', json.dumps(params)]
    if body: command += ['--json', json.dumps(body)]
    if upload: command += ['--upload', str(upload)]
    error = {}
    for attempt in range(4):
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=900,
                                    cwd=str(Path(upload).resolve().parent) if upload else None,
                                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        except (subprocess.TimeoutExpired, ConnectionError):
            if attempt == 3: raise RuntimeError('Drive operation timed out: ' + method) from None
            time.sleep(2 ** attempt)
            continue
        if not result.returncode:
            break
        try:
            error = json.loads(result.stdout).get('error', {})
        except (ValueError, AttributeError):
            error = {}
        transient = error.get('code') in {429, 500, 502, 503, 504} or error.get('reason') in {'backendError', 'internalError', 'rateLimitExceeded', 'userRateLimitExceeded'}
        if not error.get('code'):
            transport = getattr(result, 'stderr', '').lower()
            transient = transient or any(marker in transport for marker in ('connection reset', 'connection refused', 'timed out', 'dns error', 'error sending request', 'transport error'))
        if not transient or attempt == 3:
            break
        # Create requests use pre-reserved IDs; retrying cannot create another
        # object. A duplicate-ID response is recovered by ensure().
        time.sleep(2 ** attempt)
    if result.returncode:
        detail = f'exit {result.returncode}'
        try:
            error = json.loads(result.stdout).get('error', {})
            code, reason = error.get('code'), error.get('reason')
            if code is not None: detail += f', API code {code}'
            if isinstance(reason, str) and reason.replace('_', '').isalnum(): detail += ', reason ' + reason
        except (ValueError, AttributeError):
            pass
        raise RuntimeError('Drive operation failed: ' + method + ' (' + detail + ')')
    return json.loads(result.stdout)

def quote(value):
    return value.replace('\\', '\\\\').replace("'", "\\'")

class Mirror:
    def __init__(self, state_path, api=gws):
        self.path, self.api = Path(state_path), api
        self.state = json.loads(self.path.read_text()) if self.path.exists() else {'ids': {}, 'checkouts': {}}

    def save(self):
        # Preserve receipts from earlier/manual invocations during recovery.
        if self.path.exists():
            disk = json.loads(self.path.read_text())
            self.state['ids'] = dict(disk.get('ids', {}), **self.state['ids'])
            current = disk.get('checkouts', {})
            for checkout, record in self.state['checkouts'].items():
                if record.get('updated_utc', '') >= current.get(checkout, {}).get('updated_utc', ''):
                    current[checkout] = record
            self.state['checkouts'] = current
        atomic_json(self.path, self.state)

    def find(self, parent, name, key):
        query = f"trashed=false and '{quote(parent)}' in parents and (name='{quote(name)}' or appProperties has {{ key='syncKey' and value='{quote(key)}' }})"
        files, token = [], None
        while True:
            params = {'q': query, 'fields': f'nextPageToken,files({FIELDS})', 'pageSize': 100}
            if token: params['pageToken'] = token
            response = self.api('list', params)
            files += response.get('files', [])
            token = response.get('nextPageToken')
            if not token: break
        if len(files) > 1: raise RuntimeError('Ambiguous Drive destination: ' + name)
        if files and files[0].get('appProperties', {}).get('syncKey') != key:
            raise RuntimeError('Unmanaged Drive name collision: ' + name)
        return files[0] if files else None

    def private(self, file):
        if 'permissions' not in file:
            raise RuntimeError('Drive destination privacy could not be verified')
        if any(p.get('type') in {'anyone', 'domain'} or p.get('role') != 'owner' for p in file.get('permissions', [])):
            raise RuntimeError('Drive sync destination has unexpected sharing')

    def ensure(self, parent, name, key, mime, upload=None):
        found = self.find(parent, name, key)
        if found:
            self.private(found)
            return found
        reserved = self.state['ids'].get(key)
        if not reserved:
            reserved = self.api('generateIds', {'count': 1, 'space': 'drive'})['ids'][0]
            self.state['ids'][key] = reserved
            self.save()
        body = {'id': reserved, 'name': name, 'parents': [parent], 'mimeType': mime, 'appProperties': {'syncKey': key}}
        try:
            self.api('create', {'fields': FIELDS, 'ignoreDefaultVisibility': True}, body, upload)
        except RuntimeError as create_error:
            # An uncertain upload can have succeeded. Reuse the durable ID.
            try:
                recovered = self.api('get', {'fileId': reserved, 'fields': FIELDS})
            except RuntimeError as recovery_error:
                raise RuntimeError(str(create_error) + '; recovery: ' + str(recovery_error)) from None
            if recovered.get('appProperties', {}).get('syncKey') != key or parent not in recovered.get('parents', []):
                raise RuntimeError('Drive recovery ID does not match destination')
        result = self.api('get', {'fileId': reserved, 'fields': FIELDS})
        self.private(result)
        return result

    def folder(self, parent, name, key):
        return self.ensure(parent, name, key, 'application/vnd.google-apps.folder')['id']

    def upload(self, parent, name, key, path, mime):
        digest = hashlib.md5(path.read_bytes()).hexdigest()
        size = path.stat().st_size
        file = self.ensure(parent, name, key, mime, path)
        if file.get('md5Checksum') != digest or int(file.get('size', -1)) != size:
            self.api('update', {'fileId': file['id'], 'fields': FIELDS}, {'mimeType': mime}, path)
        verified = self.api('get', {'fileId': file['id'], 'fields': FIELDS})
        self.private(verified)
        if verified.get('md5Checksum') != digest or int(verified.get('size', -1)) != size:
            raise RuntimeError('Drive checksum verification failed: ' + name)
        return verified['id'], digest

def _mirror_from_state(config_path):
    config_path = Path(config_path).resolve()
    state_dir = config_path.parent / 'state'
    snapshots = json.loads((state_dir / 'state.json').read_text())
    mirror = Mirror(state_dir / 'drive-status.json')
    root_id = mirror.folder('root', 'AI OS - Live Workspace Sync', 'ai-os-live-sync:v1')
    mirror.state['root_id'] = root_id
    results = []
    for checkout, snapshot in snapshots.items():
        commit = snapshot.get('commit')
        if not commit or snapshot.get('pending_commit'): continue
        branch, repo = snapshot['branch'], snapshot['repository']
        parts = branch.split('/')
        machine = parts[-2]
        name = Path(checkout).name
        key = hashlib.sha256((checkout + '|' + repo).encode()).hexdigest()
        old = mirror.state['checkouts'].get(checkout, {})
        if old.get('commit') == commit:
            # Verify presence and content, not just a local success marker.
            remote = mirror.api('get', {'fileId': old['archive_id'], 'fields': FIELDS})
            mirror.private(remote)
            if remote.get('md5Checksum') == old.get('md5') and int(remote.get('size', -1)) == old.get('size'):
                results.append({'checkout': checkout, 'status': 'unchanged', **old})
                continue
        machine_id = mirror.folder(root_id, machine, 'machine:' + machine)
        folder_id = mirror.folder(machine_id, name, 'checkout:' + key)
        with tempfile.TemporaryDirectory(prefix='drive-workspace-sync-') as temp:
            archive = Path(temp) / 'latest.zip'
            environment = os.environ.copy()
            environment.update(GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
            result = subprocess.run(['git', '-C', checkout, 'archive', '--format=zip', '-o', str(archive), commit], capture_output=True, env=environment, timeout=300, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
            if result.returncode: raise RuntimeError('Unable to archive published snapshot')
            archive_id, digest = mirror.upload(folder_id, 'latest.zip', 'archive:' + key, archive, 'application/zip')
            record = {'commit': commit, 'branch': branch, 'repository': repo, 'updated_utc': datetime.now(timezone.utc).isoformat(), 'archive_id': archive_id, 'md5': digest, 'size': archive.stat().st_size, 'folder_id': folder_id}
            manifest = Path(temp) / 'manifest.json'
            manifest.write_text(json.dumps(record, indent=2), encoding='utf-8')
            mirror.upload(folder_id, 'manifest.json', 'manifest:' + key, manifest, 'application/json')
            mirror.state['checkouts'][checkout] = record
            mirror.save()
            results.append({'checkout': checkout, 'status': 'uploaded', **record})
    with tempfile.TemporaryDirectory(prefix='drive-workspace-index-') as temp:
        readme = Path(temp) / 'README.md'
        lines = ['# Local workspace snapshots', '', 'Each checkout contains latest.zip and manifest.json. These archives contain the same filtered snapshot published to GitHub. Source deletions disappear from current archive contents. This sync never deletes Drive files. Drive revision retention follows Drive policy; Git snapshot history preserves prior versions.', '', 'Plaintext secrets, browser sessions, raw personal exports and dependency caches are excluded from readable files. Authorized credential files and original redacted text are included in encrypted packages whose unlock key is provisioned separately. Exported conversations are readable files, not native Claude chat history.', '']
        for checkout, record in sorted(mirror.state['checkouts'].items()):
            lines += [f"- {Path(checkout).name}: https://github.com/{record['repository']}/tree/{record['branch']} | commit {record['commit']} | {record['updated_utc']} | https://drive.google.com/drive/folders/{record['folder_id']}"]
        readme.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        mirror.upload(root_id, 'README.md', 'registry:v1', readme, 'text/markdown')
    mirror.state['last_success_utc'] = datetime.now(timezone.utc).isoformat()
    mirror.save()
    return {'root_id': root_id, 'results': results}

def mirror_from_state(config_path):
    # Shared OS lock protects scheduled and manual mirror invocations.
    import importlib.util
    spec = importlib.util.spec_from_file_location('workspace_sync_lock', Path(__file__).with_name('sync.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    state_dir = Path(config_path).resolve().parent / 'state'
    state_dir.mkdir(parents=True, exist_ok=True)
    with module.process_lock(state_dir / 'drive.lock') as acquired:
        if not acquired:
            return {'status': 'busy', 'results': []}
        return _mirror_from_state(config_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default=str(Path(__file__).with_name('config.json')))
    args = parser.parse_args()
    print(json.dumps(mirror_from_state(args.config), indent=2))
