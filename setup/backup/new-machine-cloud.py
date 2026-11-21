"""Upload immutable backup archives with bounded staging and live Drive readback."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import time
import uuid
import zipfile

ACCOUNT = 'contact@aspiringattorneys.com'
DEFAULT_PARENT = '1UtlkMAzoo4dMMWgj2kTw9U4QR9p-sAUf'
PART_BYTES = 128 * 1024 * 1024
HELPERS = ['new-machine-backup.py', 'new-machine-restore.py',
           'new-machine-cloud.py', 'new-machine-README.md']
METADATA = ['manifest.json', 'parts-manifest.json', 'SHA256SUMS.txt'] + HELPERS
FIELDS = 'id,name,size,md5Checksum,parents,trashed'
RETRY_DELAYS = (2, 8)
SAFE_REASONS = {
    'notFound', 'authError', 'invalidCredentials', 'insufficientPermissions',
    'forbidden', 'badRequest', 'validationError', 'discoveryError',
    'internalError', 'backendError', 'rateLimitExceeded',
    'userRateLimitExceeded', 'sharingRateLimitExceeded', 'storageQuotaExceeded',
    'dailyLimitExceeded', 'downloadQuotaExceeded', 'accessNotConfigured',
    'quotaExceeded', 'invalid', 'required', 'conditionNotMet', 'conflict',
}


class CloudRequestError(RuntimeError):
    """Keep machine diagnostics without retaining provider text or credentials."""
    def __init__(self, operation, category, exit_code=None, http_status=None,
                 reason='unclassified', retryable=False, reported_code=None):
        self.operation = operation
        self.category = category
        self.exit_code = exit_code
        self.http_status = http_status
        self.reason = reason
        self.retryable = retryable
        self.reported_code = reported_code
        self.retries_exhausted = False
        super().__init__('Drive request failed: ' + json.dumps(self.diagnostic(), sort_keys=True))

    def diagnostic(self):
        return {'operation': self.operation, 'category': self.category,
                'exit_code': self.exit_code, 'http_status': self.http_status,
                'reason': self.reason, 'retryable': self.retryable,
                'reported_code': self.reported_code}


def request_error(result, operation):
    """gws reports structured errors on stdout; stderr includes a keyring banner."""
    detail = {}
    for output in (result.stdout, result.stderr):
        try:
            parsed = json.loads(output)
            candidate = parsed.get('error', {}) if isinstance(parsed, dict) else {}
            if isinstance(candidate, dict) and candidate:
                detail = candidate
                break
        except (ValueError, TypeError):
            pass
    code = detail.get('code')
    code = code if isinstance(code, int) and not isinstance(code, bool) and 100 <= code <= 599 else None
    # Auth/validation/internal codes in gws JSON are synthetic, not HTTP evidence.
    status = code if result.returncode == 1 else None
    reason = detail.get('reason')
    reason = reason if isinstance(reason, str) and reason in SAFE_REASONS else 'unclassified'
    category = {1: 'api', 2: 'auth', 3: 'validation', 4: 'discovery', 5: 'internal'}.get(
        result.returncode, 'cli')
    text = (str(detail.get('message', '')) + ' ' + (result.stderr or '')).lower()
    if result.returncode not in (1, 2, 3):
        if any(marker in text for marker in ('timed out', 'timeout', 'deadline has elapsed')):
            category = 'transport_timeout'
        elif any(marker in text for marker in ('dns error', 'dns lookup', 'failed to lookup', 'name resolution')):
            category = 'transport_dns'
        elif any(marker in text for marker in ('certificate', 'tls handshake', 'ssl error')):
            category = 'transport_tls'
        elif any(marker in text for marker in ('connection reset', 'connection refused', 'connection closed', 'error sending request')):
            category = 'transport_connection'
        elif 'http request failed' in text:
            category = 'transport_unspecified'
    retryable = (status in (408, 429, 500, 502, 503, 504)
                 or status == 403 and reason in {'rateLimitExceeded', 'userRateLimitExceeded', 'sharingRateLimitExceeded'}
                 or category in {'transport_timeout', 'transport_dns', 'transport_connection', 'transport_unspecified'})
    return CloudRequestError(operation, category, result.returncode, status,
                             reason, retryable, code)


def retry_pause(error, attempt):
    delay = RETRY_DELAYS[attempt]
    print(json.dumps(dict(event='cloud-request-retry', attempt=attempt + 1,
                          delay_seconds=delay, **error.diagnostic())), flush=True)
    time.sleep(delay)


def digest_file(path, algorithm='sha256'):
    digest = hashlib.new(algorithm)
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    os.replace(temporary, path)


def check_generation(path):
    path = Path(path).resolve()
    manifest = read_json(path / 'manifest.json')
    if manifest.get('generation') != path.name:
        raise RuntimeError('Generation directory and manifest identity differ')
    if manifest.get('opaque_payload') and manifest.get('complete'):
        raise RuntimeError('An opaque unindexed payload cannot be a complete restore point')
    for record in manifest['files'].values():
        name = record['generation']
        if not name or Path(name).name != name or name in {'.', '..'} or '/' in name or '\\' in name:
            raise RuntimeError('Unsafe dependency generation')
    return path, manifest


def create_unindexed_manifest(generation):
    """Describe original unindexed bytes once; never repair or repack the payload."""
    generation = Path(generation).absolute()
    payload = generation / 'payload.zip'
    manifest_path = generation / 'manifest.json'
    if os.path.lexists(manifest_path):
        raise RuntimeError('Existing manifest must not be overwritten by unindexed preservation')
    for path in (generation, *generation.parents, payload):
        value = path.lstat()
        if path.is_symlink() or getattr(value, 'st_file_attributes', 0) & 0x400:
            raise RuntimeError('Unindexed preservation refuses reparse or symlink paths')
    before = payload.stat()
    if not stat.S_ISREG(before.st_mode):
        raise RuntimeError('Unindexed payload must be a regular file')
    archive_sha256 = digest_file(payload)
    after = payload.stat()
    if before.st_size != after.st_size or before.st_mtime_ns != after.st_mtime_ns:
        raise RuntimeError('Unindexed payload changed during hashing')
    manifest = {'format': 1, 'generation': generation.name, 'scope': 'unindexed',
                'complete': False, 'opaque_payload': True, 'files': {}, 'roots': {},
                'errors': [{'error': 'original capture manifest missing; opaque bytes only, not a restore point'}],
                'archive_sha256': archive_sha256, 'archive_bytes': after.st_size}
    checksum = archive_sha256 + '  payload.zip\n'
    checksum_path = generation / 'SHA256SUMS.txt'
    if os.path.lexists(checksum_path):
        value = checksum_path.lstat()
        if checksum_path.is_symlink() or getattr(value, 'st_file_attributes', 0) & 0x400:
            raise RuntimeError('Checksum metadata is a reparse or symlink path')
        if checksum_path.read_text(encoding='utf-8') != checksum:
            raise RuntimeError('Existing checksum differs; preservation metadata refused')
    else:
        with checksum_path.open('x', encoding='utf-8', newline='\n') as stream:
            stream.write(checksum)
    with manifest_path.open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(manifest, indent=2) + '\n')
    return manifest


def make_gws(generation):
    executable = os.environ.get('GWS_EXECUTABLE') or shutil.which('gws')
    if not executable:
        raise RuntimeError('gws executable is missing; reconnect the CLI first')

    def call(*args):
        # gws confines local file access to its working directory. Recursive
        # dependency uploads can live in a sibling generation, so use the
        # particular upload file's own directory rather than the initial one.
        working_directory = generation
        if '--upload' in args:
            upload_file = Path(args[args.index('--upload') + 1])
            if not upload_file.is_absolute():
                upload_file = generation / upload_file
            working_directory = upload_file.resolve(strict=True).parent
        operation = '.'.join(args[:3]) if tuple(args[:3]) in {
            ('drive', 'about', 'get'), ('drive', 'files', 'list'),
            ('drive', 'files', 'get'), ('drive', 'files', 'create')} else 'drive.other'
        read_only = operation in {'drive.about.get', 'drive.files.list', 'drive.files.get'}
        attempts = len(RETRY_DELAYS) + 1 if read_only else 1
        for attempt in range(attempts):
            try:
                result = subprocess.run([executable, *args], capture_output=True, text=True,
                                        timeout=300, cwd=working_directory,
                                        creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
            except subprocess.TimeoutExpired:
                error = CloudRequestError(operation, 'transport_timeout', retryable=True)
            else:
                if result.returncode:
                    error = request_error(result, operation)
                else:
                    try:
                        return json.loads(result.stdout)
                    except ValueError:
                        error = CloudRequestError(operation, 'response_protocol', retryable=True)
            if not error.retryable or attempt == attempts - 1:
                error.retries_exhausted = read_only and error.retryable
                # Never attach raw subprocess exceptions, stdout or stderr to the traceback.
                raise error from None
            retry_pause(error, attempt)
    return call


def account_quota(call):
    about = call('drive', 'about', 'get', '--params', json.dumps({
        'fields': 'user(emailAddress),storageQuota(limit,usage)'}))
    if about.get('user', {}).get('emailAddress', '').lower() != ACCOUNT:
        raise RuntimeError('Wrong Google account; upload refused')
    return about.get('storageQuota', {})


def require_quota(quota, required):
    if quota.get('limit') is not None:
        available = int(quota['limit']) - int(quota.get('usage', 0))
        if required > available:
            raise RuntimeError('Google Drive capacity is insufficient for missing backup bytes')


def quoted(value):
    return str(value).replace('\\', '\\\\').replace("'", "\\'")


def list_named(call, parent, name, folders=False):
    query = "trashed=false and '%s' in parents and name='%s'" % (quoted(parent), quoted(name))
    if folders:
        query += " and mimeType='application/vnd.google-apps.folder'"
    result, token = [], None
    while True:
        params = {'q': query, 'fields': 'nextPageToken,files(' + FIELDS + ')', 'pageSize': 100}
        if token:
            params['pageToken'] = token
        response = call('drive', 'files', 'list', '--params', json.dumps(params))
        result.extend(response.get('files', []))
        token = response.get('nextPageToken')
        if not token:
            break
    if len(result) > 1:
        raise RuntimeError('Duplicate destination name: ' + name)
    return result


def folder(call, name, parent):
    found = list_named(call, parent, name, folders=True)
    if found:
        return found[0]['id']
    return call('drive', 'files', 'create', '--json', json.dumps({
        'name': name, 'parents': [parent], 'mimeType': 'application/vnd.google-apps.folder'}),
        '--params', json.dumps({'fields': 'id'}))['id']


def verify_remote(call, record, destination):
    actual = call('drive', 'files', 'get', '--params', json.dumps({
        'fileId': record['id'], 'fields': FIELDS}))
    if (actual.get('id') != record['id'] or actual.get('name') != record['name']
            or actual.get('md5Checksum') != record['md5Checksum']
            or int(actual.get('size', -1)) != int(record['size'])
            or actual.get('trashed') is not False
            or destination not in actual.get('parents', [])):
        raise RuntimeError('Cloud identity, checksum, location or size failed: ' + record['name'])
    return actual


def expected_records(generation, manifest, parts):
    if parts.get('archive_sha256') != manifest['archive_sha256']:
        raise RuntimeError('Parts manifest archive identity differs')
    expected = {}
    total = 0
    for number, part in enumerate(parts['parts'], 1):
        name = 'payload.zip.part%04d' % number
        if part['name'] != name or not re.fullmatch('[0-9a-f]{32}', part.get('md5', '')):
            raise RuntimeError('Invalid ordered archive part metadata')
        if not re.fullmatch('[0-9a-f]{64}', part.get('sha256', '')):
            raise RuntimeError('Invalid part SHA256')
        size = int(part['bytes'])
        if size <= 0 or size > PART_BYTES:
            raise RuntimeError('Invalid archive part size')
        total += size
        expected[name] = {'name': name, 'size': size, 'md5Checksum': part['md5']}
    if total != int(manifest['archive_bytes']):
        raise RuntimeError('Archive part sizes do not cover the declared archive')
    for name in METADATA:
        path = generation / name
        expected[name] = {'name': name, 'size': path.stat().st_size,
                          'md5Checksum': digest_file(path, 'md5')}
    return expected


def verify_generation_cloud(generation, call):
    """Live verification works after payload eviction; local metadata must remain."""
    generation, manifest = check_generation(generation)
    receipt = read_json(generation / 'CLOUD-VERIFIED.json')
    expected = expected_records(generation, manifest, read_json(generation / 'parts-manifest.json'))
    if (receipt.get('complete') is not True or receipt.get('generation') != generation.name
            or receipt.get('account') != ACCOUNT or not receipt.get('folder_id')):
        raise RuntimeError('Cloud receipt identity is invalid')
    if receipt.get('archive_sha256', manifest['archive_sha256']) != manifest['archive_sha256']:
        raise RuntimeError('Receipt archive identity differs')
    if int(receipt.get('archive_bytes', manifest['archive_bytes'])) != int(manifest['archive_bytes']):
        raise RuntimeError('Receipt archive size differs')
    records = receipt.get('files', [])
    names = [record.get('name') for record in records]
    if len(names) != len(set(names)) or set(names) != set(expected):
        raise RuntimeError('Cloud receipt does not cover the exact expected file set')
    actual = []
    for record in records:
        wanted = expected[record['name']]
        if (not record.get('id') or int(record.get('size', -1)) != wanted['size']
                or record.get('md5Checksum') != wanted['md5Checksum']):
            raise RuntimeError('Cloud receipt differs from local archive metadata')
        actual.append(verify_remote(call, record, receipt['folder_id']))
    return dict(receipt, files=actual)


def validate_dependency(manifest, dependency, previous):
    required = {key: value for key, value in manifest['files'].items()
                if value['generation'] == dependency}
    if any(previous['files'].get(key) != value for key, value in required.items()):
        raise RuntimeError('Dependency records mismatch')


def validate_payload(generation, manifest, preserve_opaque=False):
    payload = generation / 'payload.zip'
    if payload.stat().st_size != int(manifest['archive_bytes']):
        raise RuntimeError('Local archive size differs from manifest')
    if digest_file(payload) != manifest['archive_sha256']:
        raise RuntimeError('Local archive SHA256 differs from manifest')
    if manifest.get('opaque_payload'):
        if manifest.get('complete') or not preserve_opaque:
            raise RuntimeError('Opaque payload requires explicit incomplete preservation')
        return payload
    with zipfile.ZipFile(payload) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError('Duplicate ZIP entries')
        for key, record in manifest['files'].items():
            if record['generation'] == generation.name:
                info = archive.getinfo(key)
                if info.file_size != record['size']:
                    raise RuntimeError('Recorded ZIP entry size differs: ' + key)
    return payload


def matching_remote(call, destination, name, size, md5):
    found = list_named(call, destination, name)
    if not found:
        return None
    item = found[0]
    if int(item.get('size', -1)) != size or item.get('md5Checksum') != md5:
        raise RuntimeError('Same-name cloud file differs: ' + name)
    return verify_remote(call, item, destination)


def upload_path(call, destination, path, name, size, md5):
    failure = None
    for attempt in range(3):
        try:
            found = matching_remote(call, destination, name, size, md5)
            if found:
                return found
            result = call('drive', 'files', 'create', '--json', json.dumps({
                'name': name, 'parents': [destination]}), '--upload', str(path),
                '--params', json.dumps({'fields': FIELDS}))
            wanted = {'id': result['id'], 'name': name, 'size': size, 'md5Checksum': md5}
            return verify_remote(call, wanted, destination)
        except subprocess.TimeoutExpired:
            error = CloudRequestError('drive.files.create', 'transport_timeout', retryable=True)
            failure = error
        except CloudRequestError as error:
            if not error.retryable or error.retries_exhausted:
                raise
            failure = error
        # Integrity/conflict RuntimeErrors intentionally abort without retry.
        if attempt < len(RETRY_DELAYS):
            retry_pause(failure, attempt)
    raise RuntimeError('Three upload attempts failed: ' + name) from failure


def upload_generation(generation, call, parent=DEFAULT_PARENT, dependency_of=None,
                      preserve_incomplete=False, part_bytes=PART_BYTES, active=None):
    generation, manifest = check_generation(generation)
    receipt_path = generation / 'CLOUD-VERIFIED.json'
    receipt_before = receipt_path.read_bytes() if receipt_path.exists() else None
    active = set() if active is None else active
    if generation.name in active:
        raise RuntimeError('Cyclic backup dependency')
    active = active | {generation.name}
    if not manifest['complete'] and not preserve_incomplete:
        if not dependency_of:
            raise RuntimeError('Incomplete capture; upload refused without preservation authorization')
        final = read_json(dependency_of)
        if not final['complete'] or not any(r['generation'] == generation.name for r in final['files'].values()):
            raise RuntimeError('No complete dependent manifest')
        validate_dependency(final, generation.name, manifest)
    dependencies = sorted({r['generation'] for r in manifest['files'].values()} - {generation.name})
    if manifest['complete']:
        for dependency in dependencies:
            previous, previous_manifest = check_generation(generation.parent / dependency)
            validate_dependency(manifest, dependency, previous_manifest)
            if not (previous / 'CLOUD-VERIFIED.json').exists():
                with upload_lock(previous):
                    upload_generation(previous, call, parent, generation / 'manifest.json', active=active)
            verify_generation_cloud(previous, call)
    if not (generation / 'payload.zip').exists():
        return verify_generation_cloud(generation, call)
    payload = validate_payload(generation, manifest, preserve_opaque=preserve_incomplete)
    quota = account_quota(call)
    root = folder(call, 'Replacement Laptop Backups', parent)
    destination = folder(call, generation.name, root)
    before = payload.stat()
    records, existing, required = [], {}, 0
    with payload.open('rb') as stream:
        while chunk := stream.read(part_bytes):
            number = len(records) + 1
            record = {'name': 'payload.zip.part%04d' % number, 'bytes': len(chunk),
                      'md5': hashlib.md5(chunk).hexdigest(), 'sha256': hashlib.sha256(chunk).hexdigest()}
            records.append(record)
            remote = matching_remote(call, destination, record['name'], len(chunk), record['md5'])
            if remote:
                existing[record['name']] = remote
            else:
                required += len(chunk)
    parts = {'archive_sha256': manifest['archive_sha256'], 'parts': records}
    for name in HELPERS:
        if not (generation / name).exists():
            shutil.copyfile(Path(__file__).parent / name, generation / name)
    parts_path = generation / 'parts-manifest.json'
    if parts_path.exists():
        if read_json(parts_path) != parts:
            raise RuntimeError('Existing parts manifest differs; refusing replacement')
    else:
        write_json(parts_path, parts)
    expected = expected_records(generation, manifest, parts)
    for name in METADATA:
        wanted = expected[name]
        remote = matching_remote(call, destination, name, wanted['size'], wanted['md5Checksum'])
        if remote:
            existing[name] = remote
        else:
            required += wanted['size']
    require_quota(quota, required)
    verified = []
    print(json.dumps({'event': 'cloud-upload-plan', 'generation': generation.name,
                      'parts': len(records), 'missing_bytes': required}), flush=True)
    # Only one absent archive chunk is staged; matching cloud chunks use no local copy.
    with tempfile.TemporaryDirectory(prefix='.upload-staging-', dir=generation) as temporary:
        with payload.open('rb') as stream:
            for record in records:
                chunk = stream.read(record['bytes'])
                if hashlib.sha256(chunk).hexdigest() != record['sha256']:
                    raise RuntimeError('Archive changed while uploading')
                name = record['name']
                if name in existing:
                    verified.append(existing[name])
                    print(json.dumps({'event': 'cloud-part-verified', 'generation': generation.name,
                                      'part': name, 'bytes': record['bytes'], 'reused': True}), flush=True)
                    continue
                if shutil.disk_usage(generation).free < len(chunk) + 64 * 1024 * 1024:
                    raise RuntimeError('Insufficient local staging headroom')
                target = Path(temporary) / name
                target.write_bytes(chunk)
                verified.append(upload_path(call, destination, target, name, len(chunk), record['md5']))
                target.unlink()  # This process created this temporary part only.
                print(json.dumps({'event': 'cloud-part-verified', 'generation': generation.name,
                                  'part': name, 'bytes': record['bytes'], 'reused': False}), flush=True)
    for name in METADATA:
        wanted = expected[name]
        verified.append(existing[name] if name in existing else upload_path(
            call, destination, generation / name, name, wanted['size'], wanted['md5Checksum']))
    after = payload.stat()
    if before.st_size != after.st_size or before.st_mtime_ns != after.st_mtime_ns:
        raise RuntimeError('Archive changed during upload')
    if expected_records(generation, manifest, read_json(parts_path)) != expected:
        raise RuntimeError('Local backup metadata changed during upload')
    # Recheck every record immediately before writing the success receipt.
    verified = [verify_remote(call, record, destination) for record in verified]
    receipt = {'complete': True, 'capture_complete': manifest['complete'],
               'preservation_only': not manifest['complete'] and preserve_incomplete,
               'dependency_of': str(dependency_of) if dependency_of else None,
               'account': ACCOUNT, 'root_id': root, 'folder_id': destination,
               'generation': generation.name, 'files': verified,
               'archive_sha256': manifest['archive_sha256'],
               'archive_bytes': manifest['archive_bytes'],
               'dependency_generations': dependencies,
               'verified_at': datetime.now(timezone.utc).isoformat()}
    if (receipt_path.read_bytes() if receipt_path.exists() else None) != receipt_before:
        raise RuntimeError('Cloud receipt changed concurrently; compare-and-swap refused')
    write_json(receipt_path, receipt)
    print(json.dumps({'complete': True, 'generation': generation.name,
                      'folder_id': destination, 'files': len(verified),
                      'preservation_only': receipt['preservation_only']}), flush=True)
    return receipt


@contextmanager
def upload_lock(generation):
    path = Path(generation) / '.cloud-upload.lock'
    with path.open('a+b') as handle:
        if handle.tell() == 0:
            handle.write(b'0')
            handle.flush()
        handle.seek(0)
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == 'nt':
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generation', required=True)
    parser.add_argument('--parent', default=DEFAULT_PARENT)
    parser.add_argument('--dependency-of')
    parser.add_argument('--preserve-incomplete', action='store_true',
                        help='Preserve a failed archive unchanged; does not make it a restore point')
    parser.add_argument('--preserve-unindexed', action='store_true',
                        help='Create opaque preservation metadata only when the original manifest is absent')
    parser.add_argument('--verify-only', action='store_true', help='Live-read receipt without uploading; payload may be evicted')
    args = parser.parse_args()
    generation = Path(args.generation).resolve()
    call = make_gws(generation)
    account_quota(call)
    if args.verify_only:
        receipt = verify_generation_cloud(generation, call)
        print(json.dumps({'complete': True, 'generation': generation.name, 'files': len(receipt['files'])}))
        return
    with upload_lock(generation):
        if args.preserve_unindexed:
            create_unindexed_manifest(generation)
        upload_generation(generation, call, args.parent, args.dependency_of,
                          args.preserve_incomplete or args.preserve_unindexed)


if __name__ == '__main__':
    main()
