"""Conditional failed-history removal. Dry-run by default; exact plan confirmation required.

Only historical payload.zip files are targets. Metadata and snapshots are preserved.
"""
import argparse
from contextlib import ExitStack
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import uuid

from new_machine_offload import safe_path, scheduled_lock

STAGE = Path.home() / 'LaptopBackups' / '2026-10-07'
ROOT_ID = '1vQ_Xm9GqDd7SlahE4sp6znQKiYkW8xOe'
ACCOUNT = 'contact@aspiringattorneys.com'
TARGET_GENERATIONS = frozenset({
    '20261014-200506', '20261015-223301', '20261016-164840',
    '20261016-190001', '20261017-190011', '20261018-190002',
    '20261019-201032', '20261020-190002', '20261021-190002',
    '20261023-032455',
})


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def file_sha256(path):
    value = hashlib.sha256()
    with safe_path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            value.update(chunk)
    return value.hexdigest()


def read_json(path):
    return json.loads(safe_path(path).read_bytes())


def load_cloud_module():
    path = Path(__file__).with_name('new-machine-cloud.py')
    spec = importlib.util.spec_from_file_location('history_cleanup_cloud', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def checked_plan(plan_path, confirmed_sha=None):
    raw = safe_path(plan_path).read_bytes()
    digest = sha256_bytes(raw)
    if confirmed_sha is not None and digest != confirmed_sha:
        raise ValueError('Plan SHA256 differs from explicit confirmation')
    plan = json.loads(raw)
    entries = plan['conditional_discard_failed_core_payloads']
    names = [entry['generation'] for entry in entries]
    if len(entries) != 10 or set(names) != TARGET_GENERATIONS:
        raise ValueError('Plan must contain the exact ten reviewed generations once')
    for entry in entries:
        expected = STAGE / entry['generation'] / 'payload.zip'
        target = safe_path(entry['delete_file_if_approved'])
        if target != expected.absolute():
            raise ValueError('Plan target is outside the exact reviewed payload path')
        if len(entry.get('archive_sha256', '')) != 64 or len(entry.get('manifest_sha256', '')) != 64:
            raise ValueError('Plan lacks payload and manifest SHA256 bindings')
    return plan, digest, raw


def latest_scope_closure():
    selected, manifests = {}, {}
    for path in sorted(STAGE.glob('*/manifest.json'), reverse=True):
        safe_path(path)
        manifest = read_json(path)
        if manifest.get('generation') != path.parent.name:
            raise ValueError('Manifest generation identity differs')
        manifests[path.parent.name] = manifest
        scope = manifest.get('scope')
        if manifest.get('complete') is True and scope in {'core', 'personal'}:
            selected.setdefault(scope, path.parent.name)
    if set(selected) != {'core', 'personal'}:
        raise ValueError('Latest complete core and personal are both required')
    protected, pending = set(), list(selected.values())
    while pending:
        generation = pending.pop()
        if generation in protected:
            continue
        if not generation or Path(generation).name != generation or '/' in generation or '\\' in generation:
            raise ValueError('Unsafe dependency identity')
        if generation not in manifests:
            raise ValueError('Missing dependency manifest: ' + generation)
        protected.add(generation)
        pending.extend({record['generation'] for record in manifests[generation]['files'].values()} - protected)
    return selected, protected, manifests


def validate_target(entry):
    generation = STAGE / entry['generation']
    target = safe_path(generation / 'payload.zip')
    manifest_path = safe_path(generation / 'manifest.json')
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw)
    if sha256_bytes(raw) != entry['manifest_sha256']:
        raise ValueError('Reviewed historical manifest changed')
    if (manifest.get('generation') != generation.name or manifest.get('scope') != 'core'
            or manifest.get('complete') is not False or manifest.get('opaque_payload')):
        raise ValueError('Target is not a reviewed incomplete core capture')
    if (generation / 'CLOUD-VERIFIED.json').exists():
        raise ValueError('Target now has a cloud receipt; use preservation offloader instead')
    if manifest['archive_sha256'] != entry['archive_sha256'] or int(manifest['archive_bytes']) != int(entry['bytes']):
        raise ValueError('Reviewed archive identity differs')
    state = target.stat()
    import stat
    if not stat.S_ISREG(state.st_mode) or state.st_size != int(entry['bytes']):
        raise ValueError('Target size/type differs')
    return target, raw, (state.st_dev, state.st_ino, state.st_size, state.st_mtime_ns)


def pending_targets(entries):
    """Never delete targets already preserved elsewhere or already absent."""
    pending, skipped = [], []
    for entry in entries:
        directory = STAGE / entry['generation']
        target = safe_path(directory / 'payload.zip')
        if safe_path(directory / 'CLOUD-VERIFIED.json').exists():
            skipped.append({'generation': entry['generation'], 'reason': 'cloud receipt exists; preservation offloader owns this target'})
        elif not target.exists():
            skipped.append({'generation': entry['generation'], 'reason': 'payload already absent'})
        else:
            pending.append(entry)
    return pending, skipped


def verify_cloud_closure(cloud, call, protected):
    cloud.account_quota(call)  # Enforces exact live Google account.
    root = call('drive', 'files', 'get', '--params', json.dumps({
        'fileId': ROOT_ID, 'fields': 'id,name,mimeType,trashed'}))
    if root.get('id') != ROOT_ID or root.get('trashed') is not False or root.get('mimeType') != 'application/vnd.google-apps.folder':
        raise ValueError('Expected private backup root is unavailable')
    for generation in sorted(protected):
        directory = STAGE / generation
        receipt = cloud.verify_generation_cloud(directory, call)
        if receipt.get('root_id') != ROOT_ID or receipt.get('account') != ACCOUNT:
            raise ValueError('Dependency receipt root/account differs')
        folder = call('drive', 'files', 'get', '--params', json.dumps({
            'fileId': receipt['folder_id'], 'fields': 'id,name,parents,trashed,mimeType'}))
        if (folder.get('id') != receipt['folder_id'] or folder.get('name') != generation
                or folder.get('trashed') is not False or ROOT_ID not in folder.get('parents', [])
                or folder.get('mimeType') != 'application/vnd.google-apps.folder'):
            raise ValueError('Dependency cloud folder identity differs')


def atomic_audit(path, data, previous):
    path = safe_path(path)
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    raw = (json.dumps(data, indent=2) + '\n').encode()
    with temporary.open('xb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    if (path.read_bytes() if path.exists() else None) != previous:
        raise ValueError('Cleanup audit changed concurrently')
    os.replace(temporary, path)
    return raw


def run(plan_path, apply=False, confirmed_plan_sha=None, cloud=None, call=None, progress=None):
    emit = progress or (lambda phase, **fields: None)
    if apply and not confirmed_plan_sha:
        raise ValueError('Apply requires --confirmed-plan-sha after explicit approval')
    plan, digest, plan_raw = checked_plan(plan_path, confirmed_plan_sha)
    selected, protected, _ = latest_scope_closure()
    if TARGET_GENERATIONS & protected:
        raise ValueError('Reviewed history is required by the latest restore chains')
    entries, skipped = pending_targets(plan['conditional_discard_failed_core_payloads'])
    states = [validate_target(entry) for entry in entries]
    result = {'mode': 'apply' if apply else 'dry-run', 'plan_sha256': digest,
              'latest_complete_scopes': selected, 'protected_generations': sorted(protected),
              'targets': [str(state[0]) for state in states],
              'bytes': sum(int(entry['bytes']) for entry in entries), 'skipped_targets': skipped,
              'historical_versions_will_be_lost': True, 'deleted': []}
    if not apply:
        result['cloud_verified'] = False
        return result
    cloud = cloud or load_cloud_module()
    call = call or cloud.make_gws(STAGE)
    # Coordinator and every target uploader must be idle. Nonblocking locks refuse busy work.
    with ExitStack() as stack:
        stack.enter_context(scheduled_lock(STAGE))
        for entry in sorted(plan['conditional_discard_failed_core_payloads'], key=lambda item: item['generation']):
            safe_path(STAGE / entry['generation'] / '.cloud-upload.lock')
            stack.enter_context(cloud.upload_lock(STAGE / entry['generation']))
        if safe_path(plan_path).read_bytes() != plan_raw:
            raise ValueError('Plan changed while acquiring locks')
        selected_now, protected_now, _ = latest_scope_closure()
        if selected_now != selected or protected_now != protected:
            raise ValueError('Latest restore selection changed')
        protected_manifest_hashes = {generation: file_sha256(STAGE / generation / 'manifest.json')
                                     for generation in protected}
        entries, result['skipped_targets'] = pending_targets(plan['conditional_discard_failed_core_payloads'])
        states = [validate_target(entry) for entry in entries]
        result['targets'] = [str(state[0]) for state in states]
        result['bytes'] = sum(int(entry['bytes']) for entry in entries)
        emit('verifying-cloud', generations=len(protected))
        verify_cloud_closure(cloud, call, protected)
        result['cloud_verified'] = True
        # All target checksums must pass before the first deletion.
        for entry, state in zip(entries, states):
            emit('hashing', generation=entry['generation'], bytes=entry['bytes'])
            if file_sha256(state[0]) != entry['archive_sha256']:
                raise ValueError('Historical payload checksum differs')
        final_selected, final_protected, _ = latest_scope_closure()
        if final_selected != selected or final_protected != protected:
            raise ValueError('Latest restore selection changed during verification')
        if any(file_sha256(STAGE / generation / 'manifest.json') != digest
               for generation, digest in protected_manifest_hashes.items()):
            raise ValueError('Protected restore manifest changed during verification')
        audit = STAGE / ('FAILED-HISTORY-DISCARD-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex + '.json')
        result['audit'] = str(audit)
        result['status'] = 'verified-before-deletion'
        previous = atomic_audit(audit, result, None)
        try:
            for entry, (target, raw_manifest, original_state) in zip(entries, states):
                if safe_path(plan_path).read_bytes() != plan_raw:
                    raise ValueError('Confirmed plan changed during cleanup')
                current_target, current_manifest, current_state = validate_target(entry)
                if current_manifest != raw_manifest or current_state != original_state:
                    raise ValueError('Historical payload changed after checksum validation')
                emit('deleting', generation=entry['generation'], bytes=entry['bytes'])
                current_target.unlink()
                result['deleted'].append(str(target))
                result['status'] = 'partially-deleted'
                previous = atomic_audit(audit, result, previous)
            result['status'] = 'deleted'
            atomic_audit(audit, result, previous)
        except Exception as error:
            result['status'] = 'interrupted'
            result['error_type'] = type(error).__name__
            atomic_audit(audit, result, previous)
            raise
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', required=True, type=Path)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--confirmed-plan-sha')
    args = parser.parse_args()
    print(json.dumps(run(args.plan, args.apply, args.confirmed_plan_sha), indent=2))


if __name__ == '__main__':
    main()
