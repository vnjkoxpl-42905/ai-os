"""Evict only byte-proven cloud backup payloads, retaining restore metadata."""
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import uuid
import zipfile

ACCOUNT = 'contact@aspiringattorneys.com'
STAGE = Path.home() / 'LaptopBackups' / '2026-10-07'
METADATA = ['manifest.json', 'parts-manifest.json', 'SHA256SUMS.txt',
            'new-machine-backup.py', 'new-machine-restore.py',
            'new-machine-cloud.py', 'new-machine-README.md']
CHUNK = 128 * 1024 * 1024


def safe_path(path):
    path = Path(path).absolute()
    for item in [path, *path.parents]:
        if os.path.lexists(item):
            st = item.lstat()
            if item.is_symlink() or getattr(st, 'st_file_attributes', 0) & 1024:
                raise ValueError('Reparse or symlink path refused: ' + str(item))
    return path


def digest(path):
    sha, md5, size = hashlib.sha256(), hashlib.md5(), 0
    with safe_path(path).open('rb') as source:
        while block := source.read(1024 * 1024):
            sha.update(block); md5.update(block); size += len(block)
    return sha.hexdigest(), md5.hexdigest(), size


@contextmanager
def scheduled_lock(stage):
    import msvcrt
    with safe_path(stage / 'scheduled.lock').open('a+b') as lock:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        try:
            yield
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


def gws(*args):
    binary = os.environ.get('GWS_EXECUTABLE') or shutil.which('gws')
    if not binary:
        raise RuntimeError('gws executable missing')
    arguments = list(args)
    cwd = None
    if '--output' in arguments:
        index = arguments.index('--output') + 1
        output = safe_path(arguments[index])
        if output.exists():
            raise ValueError('Download output already exists')
        cwd = str(output.parent)
        arguments[index] = output.name
    result = subprocess.run([binary, *arguments], capture_output=True, text=True, cwd=cwd,
                            timeout=300, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    if result.returncode:
        raise RuntimeError('Drive request failed; no payload eviction')
    if '--output' in args:
        return {}
    return json.loads(result.stdout) if result.stdout.strip() else {}


def verify_generation(stage, generation, call=gws):
    stage, generation = safe_path(stage), safe_path(generation)
    if stage != STAGE.absolute() or generation.parent != stage or not re.fullmatch(r'\d{8}-\d{6}', generation.name):
        raise ValueError('Only exact backup stage generation paths are allowed')
    import datetime
    datetime.datetime.strptime(generation.name, '%Y%m%d-%H%M%S')
    documents = {name: safe_path(generation / name).read_bytes()
                 for name in ['manifest.json', 'parts-manifest.json', 'CLOUD-VERIFIED.json']}
    manifest, parts, receipt = (json.loads(documents[name]) for name in documents)
    if receipt.get('complete') is not True or receipt.get('generation') != generation.name or receipt.get('account') != ACCOUNT:
        raise ValueError('Unverified cloud receipt')
    if call('drive', 'about', 'get', '--params', json.dumps({'fields': 'user(emailAddress)'}))['user']['emailAddress'].lower() != ACCOUNT:
        raise ValueError('Wrong live Drive account')
    if manifest['archive_sha256'] != parts['archive_sha256'] or not parts['parts']:
        raise ValueError('Archive hash or parts missing')
    records = receipt['files']
    names = [r['name'] for r in records]
    expected = METADATA + [r['name'] for r in parts['parts']]
    if len(set(names)) != len(names) or set(names) != set(expected) or len(set(expected)) != len(expected):
        raise ValueError('Receipt names are not the exact expected set')
    by_name = {r['name']: r for r in records}
    for index, part in enumerate(parts['parts'], 1):
        if part['name'] != 'payload.zip.part%04d' % index or not 0 < part['bytes'] <= CHUNK:
            raise ValueError('Unsafe or unordered part record')
        if index < len(parts['parts']) and part['bytes'] != CHUNK:
            raise ValueError('Short nonfinal chunk')
    folder = receipt['folder_id']
    cloud_files = []
    token = None
    while True:
        params = {'q': "trashed=false and '%s' in parents" % folder,
                  'fields': 'nextPageToken,files(id,name,size,md5Checksum,parents,trashed)', 'pageSize': 1000}
        if token:
            params['pageToken'] = token
        page = call('drive', 'files', 'list', '--params', json.dumps(params))
        cloud_files.extend(page['files'])
        next_token = page.get('nextPageToken')
        if not next_token:
            break
        if next_token == token:
            raise ValueError('Drive pagination did not advance')
        token = next_token
    def remote(record):
        matches = [item for item in cloud_files if item.get('name') == record['name']]
        if len(matches) != 1:
            raise ValueError('Missing or duplicate cloud filename')
        value = matches[0]
        if (value.get('id') != record['id'] or value.get('name') != record['name']
                or value.get('md5Checksum') != record['md5Checksum']
                or int(value.get('size', -1)) != int(record['size'])
                or value.get('trashed') is not False or folder not in value.get('parents', [])):
            raise ValueError('Live Drive checksum, identity or parent mismatch')
    folder_info = call('drive', 'files', 'get', '--params', json.dumps({'fileId': folder, 'fields': 'id,name,parents,trashed,mimeType'}))
    if (folder_info.get('id') != folder or folder_info.get('name') != generation.name
            or folder_info.get('trashed') is not False or receipt['root_id'] not in folder_info.get('parents', [])
            or folder_info.get('mimeType') != 'application/vnd.google-apps.folder'):
        raise ValueError('Live generation folder mismatch')
    root = call('drive', 'files', 'get', '--params', json.dumps({'fileId': receipt['root_id'], 'fields': 'id,name,trashed,mimeType'}))
    if root.get('id') != receipt['root_id'] or root.get('trashed') is not False or root.get('mimeType') != 'application/vnd.google-apps.folder':
        raise ValueError('Live backup root mismatch')
    for name in METADATA:
        _, md5, size = digest(generation / name)
        if md5 != by_name[name]['md5Checksum'] or size != int(by_name[name]['size']):
            raise ValueError('Local metadata differs from uploaded metadata')
    for record in records:
        remote(record)
    payload = safe_path(generation / 'payload.zip')
    candidates = []
    full = hashlib.sha256()
    if payload.exists():
        with payload.open('rb') as source:
            for part in parts['parts']:
                chunk = source.read(part['bytes'])
                full.update(chunk)
                if len(chunk) != part['bytes'] or hashlib.sha256(chunk).hexdigest() != part['sha256'] or hashlib.md5(chunk).hexdigest() != part['md5']:
                    raise ValueError('Local archive chunk mismatch')
            if source.read(1) or full.hexdigest() != manifest['archive_sha256']:
                raise ValueError('Whole payload mismatch')
        candidates.append(payload)
    for part in parts['parts']:
        record = by_name[part['name']]
        if int(record['size']) != part['bytes'] or record['md5Checksum'] != part['md5']:
            raise ValueError('Part receipt differs from archive chunk')
        target = safe_path(generation / 'cloud-parts' / part['name'])
        if target.exists():
            if digest(target) != (part['sha256'], part['md5'], part['bytes']):
                raise ValueError('Local part mismatch')
            candidates.append(target)
    return generation, documents, parts, by_name, candidates


def snapshot_candidates(generation):
    """Return only exact checksum-recorded SQLite working copies; preserve the rest."""
    manifest = json.loads((generation / 'manifest.json').read_text())
    root = safe_path(generation / 'sqlite-snapshots')
    selected, pending = [], []
    if not root.exists():
        return selected, pending
    payload = safe_path(generation / 'payload.zip')
    archive = zipfile.ZipFile(payload) if payload.exists() else None
    prior_eviction_proven = False
    if archive is None:
        audit_path = safe_path(generation / 'OFFLOADED.json')
        evidence = json.loads(audit_path.read_text()) if audit_path.exists() else {}
        parts = json.loads((generation / 'parts-manifest.json').read_text())
        receipt = json.loads((generation / 'CLOUD-VERIFIED.json').read_text())
        first = parts['parts'][0]
        cloud_part = next((r for r in receipt['files'] if r['name'] == first['name']), {})
        expected_sample = {'cloud_id': cloud_part.get('id'), 'sha256': first['sha256'],
                           'md5': first['md5'], 'bytes': first['bytes'], 'verified': True}
        metadata_hashes = {name: digest(generation / name)[0] for name in METADATA}
        prior_eviction_proven = (evidence.get('status') == 'evicted'
            and evidence.get('generation') == generation.name
            and evidence.get('archive_sha256') == manifest['archive_sha256']
            and evidence.get('archive_bytes') == sum(p['bytes'] for p in parts['parts'])
            and evidence.get('metadata_sha256') == metadata_hashes
            and evidence.get('restore_sample') == expected_sample)
    try:
        for parent, directories, names in os.walk(root, followlinks=False):
            for name in directories:
                safe_path(Path(parent) / name)
            for name in names:
                path = safe_path(Path(parent) / name)
                key = path.relative_to(root).as_posix()
                record = manifest.get('files', {}).get(key)
                if not record or record.get('generation') != generation.name or path.suffix not in ('.sqlite', '.db'):
                    pending.append({'path': str(path), 'bytes': path.stat().st_size, 'reason': 'not recorded in this generation'})
                    continue
                sha, _, size = digest(path)
                if sha != record['sha256'] or size != record['size']:
                    pending.append({'path': str(path), 'bytes': size, 'reason': 'snapshot differs from recorded archive member'})
                    continue
                if archive is None and not prior_eviction_proven:
                    pending.append({'path': str(path), 'bytes': size, 'reason': 'legacy-proof-not-bound'})
                    continue
                if archive is not None:
                    matching = [info for info in archive.infolist() if info.filename == key]
                    if len(matching) != 1 or matching[0].file_size != size:
                        raise ValueError('Snapshot archive mapping missing or duplicated')
                    hashed = hashlib.sha256()
                    with archive.open(matching[0]) as source:
                        while chunk := source.read(1024 * 1024):
                            hashed.update(chunk)
                    if hashed.hexdigest() != sha:
                        raise ValueError('Archived SQLite member checksum mismatch')
                selected.append(path)
    finally:
        if archive is not None:
            archive.close()
    return selected, pending


def offload_generation(stage, generation, apply=False, lock_held=False, call=gws, include_sqlite_snapshots=True):
    """lock_held is for the coordinator already holding scheduled.lock only."""
    if safe_path(stage) != STAGE.absolute():
        raise ValueError('Only the fixed backup stage is allowed')
    if not lock_held:
        with scheduled_lock(safe_path(stage)):
            return offload_generation(stage, generation, apply, True, call, include_sqlite_snapshots)
    generation, documents, parts, records, candidates = verify_generation(stage, generation, call)
    snapshots, pending = snapshot_candidates(generation) if include_sqlite_snapshots else ([], [])
    candidates += snapshots
    result = {'generation': generation.name, 'apply': apply,
              'payload_files': [str(p) for p in candidates], 'bytes': sum(p.stat().st_size for p in candidates),
              'sqlite_snapshot_files': len(snapshots), 'pending_snapshots': pending,
              'archive_sha256': json.loads(documents['manifest.json'])['archive_sha256'],
              'archive_bytes': sum(p['bytes'] for p in parts['parts']),
              'metadata_sha256': {name: digest(generation / name)[0] for name in METADATA}}
    prior_audit_path = safe_path(generation / 'OFFLOADED.json')
    prior_audit = json.loads(prior_audit_path.read_text()) if prior_audit_path.exists() else {}
    prior_bytes = prior_audit.get('cumulative_bytes_evicted', prior_audit.get('bytes', 0)) if prior_audit.get('status') == 'evicted' else prior_audit.get('cumulative_bytes_evicted', 0)
    result['cumulative_bytes_evicted'] = int(prior_bytes)
    if not apply or not candidates:
        return result
    first = parts['parts'][0]
    # Download a real cloud chunk to a new isolated directory before any removal.
    sample_dir = Path(tempfile.mkdtemp(prefix='backup-offload-restore-check-'))
    sample = sample_dir / first['name']
    call('drive', 'files', 'get', '--params', json.dumps({'fileId': records[first['name']]['id'], 'alt': 'media'}), '--output', str(sample))
    if digest(sample) != (first['sha256'], first['md5'], first['bytes']):
        raise ValueError('Downloaded restore sample mismatch; no eviction')
    result['restore_sample'] = {'cloud_id': records[first['name']]['id'], 'sha256': first['sha256'],
                              'md5': first['md5'], 'bytes': first['bytes'], 'verified': True}
    # Recheck local evidence and full live chain after sample download.
    _, latest_documents, _, _, latest_candidates = verify_generation(stage, generation, call)
    if include_sqlite_snapshots:
        latest_snapshots, _ = snapshot_candidates(generation)
        latest_candidates += latest_snapshots
    if documents != latest_documents or candidates != latest_candidates:
        raise ValueError('Generation changed concurrently; eviction refused')
    audit = generation / 'OFFLOADED.json'
    audit_before = safe_path(audit).read_bytes() if audit.exists() else None
    def save_audit(status):
        nonlocal audit_before
        data = json.dumps(dict(result, status=status), indent=2).encode()
        temporary = generation / ('OFFLOADED-' + uuid.uuid4().hex + '.tmp')
        temporary.write_bytes(data)
        if (audit.read_bytes() if audit.exists() else None) != audit_before:
            raise ValueError('Offload audit changed concurrently')
        os.replace(temporary, audit)
        audit_before = data
    save_audit('verified-before-eviction')
    for candidate in candidates:
        safe_path(candidate).unlink()
    result['evicted'] = True
    result['cumulative_bytes_evicted'] += result['bytes']
    save_audit('evicted')
    safe_path(sample).unlink()
    sample_dir.rmdir()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage', default=str(STAGE))
    parser.add_argument('--generation', required=True)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--include-sqlite-snapshots', action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()
    print(json.dumps(offload_generation(args.stage, args.generation, args.apply,
                                      include_sqlite_snapshots=args.include_sqlite_snapshots), indent=2))


if __name__ == '__main__':
    main()
