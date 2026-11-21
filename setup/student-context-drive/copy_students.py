"""Private, resumable, copy-only student context transfer through authenticated gws."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
import threading
from concurrent.futures import ThreadPoolExecutor

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'students'
STATE = HERE / 'copy-state.generated.json'
ROOT_NAME = 'LSAT U - Student Context'
ACCOUNT = 'contact@aspiringattorneys.com'
LOCK = threading.RLock()
STUDENTS = 'adriana-varea amanda asia avneet-natt celia-cutler charles-moore dakota david-salgado ethan favour fernande-charleus gianna ivory-johnson nicole ore sandra sofia steven-morris venusa-laveaux vinay-kalva whit-wilson yahunatan-zetvy zeina-borji'.split()
FIELDS = 'id,name,mimeType,size,md5Checksum,parents,appProperties,webViewLink,trashed'
MARKERS = [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'\bAIza[0-9A-Za-z_-]{35}\b', rb'\bsk_(?:live|test)_[A-Za-z0-9]{16,}\b', rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b', rb'(?im)^\s*(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\x22\x27]?[A-Za-z0-9_+/=-]{16,}']
MARKERS += [rb'\beyJ[A-Za-z0-9_-]{10,}\.eyJ', rb'\bsk-[A-Za-z0-9_-]{20,}', rb'\bAKIA[0-9A-Z]{16}\b', rb'\b1//[0-9A-Za-z_-]{30,}', rb'\bxox[baprs]-[A-Za-z0-9-]{10,}']

def gws_executable():
    executable = shutil.which('gws.exe' if os.name == 'nt' else 'gws')
    if not executable or (os.name == 'nt' and Path(executable).suffix.lower() != '.exe'):
        raise RuntimeError('A native gws.exe is required on Windows; command shims are not supported')
    return executable

def gws(parts, params=None, body=None, upload=None, output=None):
    cmd = [gws_executable(), 'drive', *parts]
    if params is not None: cmd += ['--params', json.dumps(params)]
    if body is not None: cmd += ['--json', json.dumps(body)]
    if upload is not None: cmd += ['--upload', upload.name]
    if output is not None: cmd += ['--output', output.name]
    for attempt in range(3 if parts[-1] in {'get', 'list'} else 1):
        result = subprocess.run(cmd, cwd=upload.parent if upload else output.parent if output else HERE, capture_output=True, text=True, timeout=180)
        if not result.returncode: break
        if attempt < 2 and parts[-1] in {'get', 'list'}: time.sleep(2 ** attempt)
    if result.returncode: raise RuntimeError('gws operation failed: ' + ' '.join(parts) + ' ' + result.stderr[-500:])
    if output is not None: return None
    return json.loads(result.stdout)

def save(state):
    with LOCK:
        temp = STATE.with_suffix('.tmp')
        temp.write_text(json.dumps(state, indent=2), encoding='utf-8')
        for attempt in range(8):
            try:
                os.replace(temp, STATE)
                break
            except PermissionError:
                if attempt == 7: raise
                time.sleep(min(0.1 * 2 ** attempt, 2))

def in_source(path, source):
    for candidate in [path, *path.parents]:
        if candidate.is_symlink() or (hasattr(candidate, 'is_junction') and candidate.is_junction()):
            raise RuntimeError('Linked source path excluded: ' + str(candidate))
        if candidate == source: break
    if not path.resolve().is_relative_to(source.resolve()):
        raise RuntimeError('Source path escapes student root: ' + str(path))

def inventory(source=SOURCE):
    in_source(source, source)
    rows = []
    for student in STUDENTS:
        folder = source / student
        in_source(folder, source)
        if not folder.is_dir(): raise RuntimeError('Missing student folder: ' + student)
        for path in sorted(folder.rglob('*')):
            in_source(path, source)
            if not path.is_file(): continue
            if path.name.startswith('.env') or path.suffix.lower() in {'.pem', '.key', '.p12', '.pfx'}:
                raise RuntimeError('Potential secret file: ' + str(path))
            data = path.read_bytes()
            if any(re.search(pattern, data) for pattern in MARKERS):
                raise RuntimeError('Potential credential marker: ' + str(path))
            rows.append({'path': path.relative_to(source).as_posix(), 'size': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'md5': hashlib.md5(data).hexdigest()})
    return rows

def listing(query):
    rows, token = [], None
    while True:
        params = {'q': query, 'pageSize': 1000, 'fields': 'nextPageToken,files(' + FIELDS + ')'}
        if token: params['pageToken'] = token
        page = gws(['files', 'list'], params)
        rows += page.get('files', [])
        token = page.get('nextPageToken')
        if not token: return rows

def private(file_id):
    perms = gws(['permissions', 'list'], {'fileId': file_id, 'fields': 'permissions(id,type,role,emailAddress,domain)', 'pageSize':100}).get('permissions', [])
    if not perms or any(p.get('type') != 'user' or p.get('emailAddress', '').lower() != ACCOUNT for p in perms):
        raise RuntimeError('Folder is not restricted to the expected account: ' + file_id)

def escaped(value): return value.replace('\\', '\\\\').replace("'", "\\'")

def path_marker(relative):
    # Drive limits each property key plus value to 124 UTF-8 bytes.
    if len(('lsatuContextPath' + relative).encode('utf-8')) <= 124: return relative
    return 'sha256:' + hashlib.sha256(relative.encode('utf-8')).hexdigest()

def folder(name, parent, relative, state):
    existing = listing("trashed = false and '" + escaped(parent) + "' in parents and name = '" + escaped(name) + "'")
    if len(existing) > 1: raise RuntimeError('Ambiguous destination folder: ' + relative)
    if existing:
        item = existing[0]
        if item.get('mimeType') != 'application/vnd.google-apps.folder': raise RuntimeError('Destination conflicts: ' + relative)
        if item.get('appProperties', {}).get('lsatuContextPath') != path_marker(relative): raise RuntimeError('Unmanaged folder conflict: ' + relative)
    else:
        if relative in state['folders']: raise RuntimeError('Stored folder moved or renamed, preserved: ' + relative)
        item = gws(['files', 'create'], {'fields': FIELDS}, {'name': name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [parent], 'appProperties': {'lsatuContextPath':path_marker(relative)}})
    if relative in state['folders'] and state['folders'][relative] != item['id']:
        raise RuntimeError('Stored folder ID changed, preserved: ' + relative)
    private(item['id'])
    with LOCK:
        if state['folders'].get(relative) != item['id']:
            state['folders'][relative] = item['id']; save(state)
    return item['id']

def matching(remote, row):
    return not remote.get('trashed', False) and remote.get('md5Checksum') == row['md5'] and int(remote.get('size', -1)) == row['size']

def validate_state(state):
    if not isinstance(state, dict) or state.get('status') not in {'running', 'complete'}:
        raise RuntimeError('Copy state is missing a valid status; run --apply first')
    root = state.get('root_id')
    if not isinstance(root, str) or not root.strip():
        raise RuntimeError('Copy state is missing a valid root_id; run --apply first')
    if not isinstance(state.get('folders'), dict) or state['folders'].get('student-context-root-v1') != root:
        raise RuntimeError('Copy state root_id does not match the managed root folder')
    if not isinstance(state.get('files'), dict):
        raise RuntimeError('Copy state is missing the verified file inventory')

def finish(rows, state):
    validate_state(state)
    for row in rows:
        stored = state['files'].get(row['path'], {})
        if not stored.get('verified') or any(stored.get(key) != row[key] for key in ['sha256','md5','size']):
            raise RuntimeError('Incomplete verified copy: ' + row['path'])
    sample = rows[0]
    private(state['root_id'])
    private(state['files'][sample['path']]['id'])
    with tempfile.TemporaryDirectory(prefix='lsatu-context-restore-') as tmp:
        restored = Path(tmp) / 'sample.bin'
        gws(['files','get'], {'fileId':state['files'][sample['path']]['id'], 'alt':'media'}, output=restored)
        if hashlib.sha256(restored.read_bytes()).hexdigest() != sample['sha256']: raise RuntimeError('Restore sample hash mismatch')
    state['restore_sample'] = {'path':sample['path'], 'sha256':sample['sha256'], 'verified':True, 'permissions_verified':True}
    if inventory() != rows: raise RuntimeError('Local source changed during copy; originals preserved, rerun requires conflict review')
    private(state['root_id'])
    state['status'] = 'complete'
    state['completed_at_unix'] = int(time.time()); save(state)
    print(json.dumps({'root':state['root_url'], 'verified_files':len(rows), 'restore_sample':True}), flush=True)

def transfer(row, state, remote_children, source=SOURCE, api=None):
    api = api or gws
    parts = Path(row['path']).parts
    directory = Path(row['path']).parent.as_posix()
    parent = state['folders'][directory]
    candidates = [item for item in remote_children[directory] if item['name'] == parts[-1]]
    if len(candidates) > 1: raise RuntimeError('Ambiguous destination file: ' + row['path'])
    remote = candidates[0] if candidates else None
    cached = state['files'].get(row['path'])
    if cached and (not remote or remote['id'] != cached['id']):
        raise RuntimeError('Stored file moved or renamed, preserved: ' + row['path'])
    if remote and remote.get('appProperties', {}).get('lsatuContextPath') != path_marker(row['path']):
        raise RuntimeError('Unmanaged file conflict, preserved: ' + row['path'])
    if remote and not matching(remote, row): raise RuntimeError('Remote content conflict, preserved: ' + row['path'])
    if not remote:
        path = source / row['path']
        in_source(path, source)
        if hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']: raise RuntimeError('Source changed: ' + row['path'])
        remote = api(['files', 'create'], {'fields':FIELDS}, {'name':parts[-1], 'parents':[parent], 'appProperties':{'lsatuContextPath':path_marker(row['path']), 'sourceSha256':row['sha256']}}, upload=path)
        if not matching(remote, row): raise RuntimeError('Upload verification failed: ' + row['path'])
    with LOCK:
        state['files'][row['path']] = {**row, 'id':remote['id'], 'verified':True}; save(state)
        if len(state['files']) % 25 == 0: print('Verified files: ' + str(len(state['files'])), flush=True)

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--apply', action='store_true'); parser.add_argument('--verify-existing', action='store_true'); args = parser.parse_args()
    rows = inventory()
    (HERE / 'inventory.generated.json').write_text(json.dumps({'source':str(SOURCE), 'students':STUDENTS, 'files':rows}, indent=2), encoding='utf-8')
    print(json.dumps({'students':len(STUDENTS), 'files':len(rows), 'bytes':sum(r['size'] for r in rows), 'mode':'verify-existing' if args.verify_existing else 'apply' if args.apply else 'dry-run'}), flush=True)
    if not args.apply and not args.verify_existing: return
    state = json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {'folders':{}, 'files':{}}
    if args.verify_existing: validate_state(state)
    about = gws(['about', 'get'], {'fields':'user(emailAddress)'})
    if about.get('user', {}).get('emailAddress', '').lower() != ACCOUNT: raise RuntimeError('Unexpected Drive account')
    if args.verify_existing:
        finish(rows, state)
        return
    state['status'] = 'running'
    state['inventory_sha256'] = hashlib.sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest()
    save(state)
    root = folder(ROOT_NAME, 'root', 'student-context-root-v1', state)
    state['root_id'] = root; state['root_url'] = 'https://drive.google.com/drive/folders/' + root; save(state)
    directories = set(STUDENTS)
    for row in rows:
        directory = Path(row['path']).parent
        directories.update(p.as_posix() for p in [directory, *directory.parents] if p.as_posix() != '.')
    def ensure(relative):
        path = Path(relative); parent_path = path.parent.as_posix()
        return folder(path.name, root if parent_path == '.' else state['folders'][parent_path], relative, state)
    with ThreadPoolExecutor(max_workers=4) as pool:
        for depth in range(1, max(len(Path(d).parts) for d in directories) + 1):
            list(pool.map(ensure, sorted(d for d in directories if len(Path(d).parts) == depth)))
    mapping = {student:{'folder_id':state['folders'][student], 'folder_url':'https://drive.google.com/drive/folders/' + state['folders'][student]} for student in STUDENTS}
    (HERE / 'student-folders.generated.json').write_text(json.dumps({'root_id':root, 'students':mapping}, indent=2), encoding='utf-8')
    print('Private student folder mapping ready: 23 students', flush=True)
    def children(relative):
        file_id = state['folders'][relative]
        return relative, listing("trashed = false and '" + escaped(file_id) + "' in parents")
    with ThreadPoolExecutor(max_workers=4) as pool:
        remote_children = dict(pool.map(children, sorted(directories)))
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda row: transfer(row, state, remote_children), rows))
    finish(rows, state)

if __name__ == '__main__': main()
