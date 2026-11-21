import copy
from contextlib import redirect_stdout
import hashlib
import importlib.util
import json
import io
from pathlib import Path
import re
import tempfile
import unittest
import zipfile
import subprocess
from unittest.mock import patch
from types import SimpleNamespace

MODULE = Path(__file__).resolve().parents[1] / 'setup/backup/new-machine-cloud.py'
spec = importlib.util.spec_from_file_location('new_machine_cloud', MODULE)
cloud = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cloud)


class FakeDrive:
    def __init__(self, root):
        self.root = root
        self.files = {}
        self.upload_count = 0
        self.peak_staged_bytes = 0
        self.available = 10**12
        self.timeout_after_create = False

    def __call__(self, *args):
        command = args[:3]
        params = json.loads(args[args.index('--params') + 1]) if '--params' in args else {}
        if command == ('drive', 'about', 'get'):
            return {'user': {'emailAddress': cloud.ACCOUNT},
                    'storageQuota': {'limit': str(self.available), 'usage': '0'}}
        if command == ('drive', 'files', 'list'):
            query = params['q']
            name = re.search(r"name\s*=\s*'([^']*)'", query).group(1)
            parent = re.search(r"'([^']*)' in parents", query).group(1)
            folders = "mimeType='application/vnd.google-apps.folder'" in query
            return {'files': [copy.deepcopy(record) for record in self.files.values()
                              if record['name'] == name and parent in record['parents']
                              and not record['trashed']
                              and (not folders or record.get('mimeType') == 'application/vnd.google-apps.folder')]}
        if command == ('drive', 'files', 'create'):
            body = json.loads(args[args.index('--json') + 1])
            record = dict(body, id=str(len(self.files) + 1), trashed=False)
            if '--upload' in args:
                path = Path(args[args.index('--upload') + 1])
                data = path.read_bytes()
                self.upload_count += 1
                staged = sum(p.stat().st_size for p in self.root.glob('*/.upload-staging-*/payload.zip.part*'))
                self.peak_staged_bytes = max(self.peak_staged_bytes, staged)
                record.update(size=str(len(data)), md5Checksum=hashlib.md5(data).hexdigest())
            self.files[record['id']] = record
            if '--upload' in args and self.timeout_after_create:
                self.timeout_after_create = False
                raise subprocess.TimeoutExpired('gws', 300)
            return copy.deepcopy(record)
        if command == ('drive', 'files', 'get'):
            return copy.deepcopy(self.files[params['fileId']])
        raise AssertionError(args)


class CloudBackupTests(unittest.TestCase):
    def setUp(self):
        self.enterContext(redirect_stdout(io.StringIO()))
        self.sleep = self.enterContext(patch.object(cloud.time, 'sleep'))
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.drive = FakeDrive(self.root)

    def generation(self, name='20261023-010101', complete=True, dependency=None):
        directory = self.root / name
        directory.mkdir()
        content = bytes(range(256)) * 4
        own_name = 'current.bin' if dependency and 'sample.bin' in dependency else 'sample.bin'
        with zipfile.ZipFile(directory / 'payload.zip', 'w') as archive:
            archive.writestr(own_name, content)
        payload = directory / 'payload.zip'
        manifest = {'generation': name, 'complete': complete, 'scope': 'core',
                    'files': {own_name: {'generation': name, 'size': len(content),
                                             'sha256': hashlib.sha256(content).hexdigest()}},
                    'archive_bytes': payload.stat().st_size,
                    'archive_sha256': cloud.digest_file(payload)}
        if dependency:
            manifest['files'].update(dependency)
        cloud.write_json(directory / 'manifest.json', manifest)
        (directory / 'SHA256SUMS.txt').write_text(manifest['archive_sha256'] + '  payload.zip\n')
        for helper in cloud.HELPERS:
            (directory / helper).write_text('helper fixture\n')
        return directory

    def test_bounded_staging_resume_and_evicted_legacy_receipt(self):
        directory = self.generation()
        before = (directory / 'payload.zip').read_bytes()
        receipt = cloud.upload_generation(directory, self.drive, part_bytes=256)
        self.assertLessEqual(self.drive.peak_staged_bytes, 256)
        self.assertFalse((directory / 'cloud-parts').exists())
        self.assertFalse(list(directory.glob('.upload-staging-*')))
        self.assertEqual((directory / 'payload.zip').read_bytes(), before)
        count = self.drive.upload_count
        parts_before = (directory / 'parts-manifest.json').read_bytes()
        cloud.upload_generation(directory, self.drive, part_bytes=256)
        self.assertEqual(self.drive.upload_count, count)
        self.assertEqual((directory / 'parts-manifest.json').read_bytes(), parts_before)
        (directory / 'payload.zip').unlink()  # Test fixture only: simulate an offloaded archive.
        receipt.pop('archive_sha256')
        receipt.pop('archive_bytes')
        cloud.write_json(directory / 'CLOUD-VERIFIED.json', receipt)
        self.assertTrue(cloud.verify_generation_cloud(directory, self.drive)['complete'])

    def test_wrong_archive_refused_before_remote_mutation(self):
        directory = self.generation()
        with (directory / 'payload.zip').open('ab') as stream:
            stream.write(b'changed')
        with self.assertRaisesRegex(RuntimeError, 'archive size'):
            cloud.upload_generation(directory, self.drive)
        self.assertFalse(self.drive.files)

    def test_failed_capture_preserved_without_changing_manifest(self):
        directory = self.generation(complete=False)
        before = (directory / 'manifest.json').read_bytes()
        with self.assertRaisesRegex(RuntimeError, 'Incomplete capture'):
            cloud.upload_generation(directory, self.drive)
        receipt = cloud.upload_generation(directory, self.drive, preserve_incomplete=True, part_bytes=256)
        self.assertTrue(receipt['preservation_only'])
        self.assertFalse(receipt['capture_complete'])
        self.assertEqual((directory / 'manifest.json').read_bytes(), before)

    def test_live_receipt_rejects_moved_or_trashed_files(self):
        directory = self.generation()
        receipt = cloud.upload_generation(directory, self.drive, part_bytes=256)
        remote = self.drive.files[receipt['files'][0]['id']]
        remote['trashed'] = True
        with self.assertRaisesRegex(RuntimeError, 'Cloud identity'):
            cloud.verify_generation_cloud(directory, self.drive)
        remote['trashed'] = False
        remote['parents'] = ['somewhere-else']
        with self.assertRaisesRegex(RuntimeError, 'Cloud identity'):
            cloud.verify_generation_cloud(directory, self.drive)

    def test_quota_refuses_missing_bytes_without_uploading_payload(self):
        directory = self.generation()
        self.drive.available = 1
        with self.assertRaisesRegex(RuntimeError, 'capacity'):
            cloud.upload_generation(directory, self.drive, part_bytes=256)
        self.assertEqual(self.drive.upload_count, 0)
        self.assertTrue((directory / 'payload.zip').exists())

    def test_duplicate_cloud_names_refused(self):
        directory = self.generation()
        receipt = cloud.upload_generation(directory, self.drive, part_bytes=256)
        duplicate = dict(self.drive.files[receipt['files'][0]['id']], id='duplicate')
        self.drive.files['duplicate'] = duplicate
        with self.assertRaisesRegex(RuntimeError, 'Duplicate destination'):
            cloud.upload_generation(directory, self.drive, part_bytes=256)

    def test_unknown_upload_outcome_resumes_without_duplicate(self):
        directory = self.generation()
        self.drive.timeout_after_create = True
        receipt = cloud.upload_generation(directory, self.drive, part_bytes=256)
        self.assertEqual(self.drive.upload_count, len(receipt['files']))

    def test_dependency_can_be_live_verified_after_payload_eviction(self):
        previous = self.generation(name='20261023-010101')
        cloud.upload_generation(previous, self.drive, part_bytes=256)
        dependency = cloud.read_json(previous / 'manifest.json')['files']
        (previous / 'payload.zip').unlink()  # Test fixture only.
        current = self.generation(name='20261023-020202', dependency=dependency)
        receipt = cloud.upload_generation(current, self.drive, part_bytes=256)
        self.assertEqual(receipt['dependency_generations'], [previous.name])

    def test_old_parts_manifest_serialization_is_preserved(self):
        directory = self.generation()
        payload = (directory / 'payload.zip').read_bytes()
        record = {'name': 'payload.zip.part0001', 'bytes': len(payload),
                  'md5': hashlib.md5(payload).hexdigest(), 'sha256': hashlib.sha256(payload).hexdigest()}
        document = {'archive_sha256': hashlib.sha256(payload).hexdigest(), 'parts': [record]}
        old_bytes = json.dumps(document, indent=2).encode()  # Old uploader writes no trailing newline.
        (directory / 'parts-manifest.json').write_bytes(old_bytes)
        cloud.upload_generation(directory, self.drive)
        self.assertEqual((directory / 'parts-manifest.json').read_bytes(), old_bytes)

    def test_gws_upload_cwd_contains_sibling_dependency_file(self):
        current = self.generation(name='20261023-020202')
        previous = self.generation(name='20261023-010101')
        target = previous / 'manifest.json'
        with patch.dict(cloud.os.environ, {'GWS_EXECUTABLE': 'fake-gws'}):
            call = cloud.make_gws(current)
        with patch.object(cloud.subprocess, 'run', return_value=SimpleNamespace(
                returncode=0, stdout='{}', stderr='')) as run:
            call('drive', 'files', 'create', '--upload', str(target))
        self.assertEqual(run.call_args.kwargs['cwd'], target.parent)

    def test_unindexed_interrupted_zip_preserved_as_original_opaque_bytes(self):
        directory = self.root / '20261023-030303'
        directory.mkdir()
        payload = directory / 'payload.zip'
        original = b'PK\x03\x04interrupted archive without central directory' * 20
        payload.write_bytes(original)
        manifest = cloud.create_unindexed_manifest(directory)
        self.assertEqual(manifest['scope'], 'unindexed')
        self.assertFalse(manifest['complete'])
        self.assertEqual(manifest['files'], {})
        with self.assertRaisesRegex(RuntimeError, 'Opaque payload requires'):
            cloud.validate_payload(directory, manifest)
        receipt = cloud.upload_generation(directory, self.drive, preserve_incomplete=True, part_bytes=256)
        self.assertTrue(receipt['preservation_only'])
        self.assertFalse(receipt['capture_complete'])
        self.assertEqual(payload.read_bytes(), original)
        self.assertEqual(cloud.read_json(directory / 'manifest.json'), manifest)

    def test_opaque_payload_cannot_claim_complete(self):
        directory = self.generation()
        manifest = cloud.read_json(directory / 'manifest.json')
        manifest['opaque_payload'] = True
        cloud.write_json(directory / 'manifest.json', manifest)
        with self.assertRaisesRegex(RuntimeError, 'opaque unindexed payload cannot'):
            cloud.upload_generation(directory, self.drive, preserve_incomplete=True)
        self.assertFalse(self.drive.files)

    def test_unindexed_preservation_never_overwrites_existing_manifest(self):
        directory = self.generation()
        before = (directory / 'manifest.json').read_bytes()
        with self.assertRaisesRegex(RuntimeError, 'must not be overwritten'):
            cloud.create_unindexed_manifest(directory)
        self.assertEqual((directory / 'manifest.json').read_bytes(), before)

    def test_unindexed_preservation_refuses_reparse_payload(self):
        directory = self.root / '20261023-030303'
        directory.mkdir()
        payload = directory / 'payload.zip'
        payload.write_bytes(b'opaque')
        original_lstat = Path.lstat

        def tagged(path, *args, **kwargs):
            value = original_lstat(path, *args, **kwargs)
            if path == payload:
                return SimpleNamespace(st_file_attributes=0x400, st_mode=value.st_mode)
            return value

        with patch.object(Path, 'lstat', tagged):
            with self.assertRaisesRegex(RuntimeError, 'reparse or symlink'):
                cloud.create_unindexed_manifest(directory)
        self.assertFalse((directory / 'manifest.json').exists())

    def gws_call(self, directory):
        with patch.dict(cloud.os.environ, {'GWS_EXECUTABLE': 'fake-gws'}):
            return cloud.make_gws(directory)

    def test_structured_stdout_status_is_preserved_without_provider_text(self):
        call = self.gws_call(self.root)
        failure = SimpleNamespace(returncode=1, stdout=json.dumps({'error': {
            'code': 404, 'reason': 'notFound', 'message': 'secret-token-MUST-NOT-LOG'}}),
            stderr='Using keyring backend: keyring\nerror[api]: secret-token-MUST-NOT-LOG')
        with patch.object(cloud.subprocess, 'run', return_value=failure) as run:
            with self.assertRaises(cloud.CloudRequestError) as caught:
                call('drive', 'files', 'get', '--params', '{}')
        error = caught.exception
        self.assertEqual(error.http_status, 404)
        self.assertEqual(error.reason, 'notFound')
        self.assertNotIn('secret-token', str(error))
        self.assertEqual(run.call_count, 1)
        self.sleep.assert_not_called()

    def test_read_transient_failure_uses_bounded_backoff(self):
        call = self.gws_call(self.root)
        failure = SimpleNamespace(returncode=1, stdout=json.dumps({'error': {
            'code': 503, 'reason': 'backendError', 'message': 'private URL'}}), stderr='keyring banner')
        success = SimpleNamespace(returncode=0, stdout='{"files": []}', stderr='')
        with patch.object(cloud.subprocess, 'run', side_effect=[failure, failure, success]) as run:
            self.assertEqual(call('drive', 'files', 'list', '--params', '{}'), {'files': []})
        self.assertEqual(run.call_count, 3)
        self.assertEqual([item.args[0] for item in self.sleep.call_args_list], [2, 8])

    def test_transport_failure_does_not_claim_synthetic_code_is_http_status(self):
        failure = SimpleNamespace(returncode=5, stdout=json.dumps({'error': {
            'code': 500, 'reason': 'internalError',
            'message': 'HTTP request failed: error sending request for url https://secret.invalid/token'}}),
            stderr='Using keyring backend: keyring\nerror: HTTP request failed')
        error = cloud.request_error(failure, 'drive.files.create')
        self.assertEqual(error.category, 'transport_connection')
        self.assertIsNone(error.http_status)
        self.assertEqual(error.reported_code, 500)
        self.assertTrue(error.retryable)
        self.assertNotIn('secret.invalid', str(error))

    def test_upload_permanent_quota_error_is_not_retried(self):
        directory = self.generation()
        attempts = []

        def permanent(*args):
            if args[:3] == ('drive', 'files', 'create'):
                attempts.append(args)
                raise cloud.CloudRequestError('drive.files.create', 'api', exit_code=1,
                                              http_status=403, reason='storageQuotaExceeded')
            return self.drive(*args)

        with self.assertRaises(cloud.CloudRequestError):
            cloud.upload_path(permanent, 'destination', directory / 'payload.zip',
                              'payload.zip.part0001', 10, 'md5')
        self.assertEqual(len(attempts), 1)
        self.sleep.assert_not_called()

    def test_exhausted_read_retry_is_not_multiplied_by_upload_retry(self):
        directory = self.generation()
        call = self.gws_call(directory)
        failure = SimpleNamespace(returncode=1, stdout=json.dumps({'error': {
            'code': 429, 'reason': 'rateLimitExceeded', 'message': 'private'}}), stderr='')
        with patch.object(cloud.subprocess, 'run', return_value=failure) as run:
            with self.assertRaises(cloud.CloudRequestError) as caught:
                cloud.upload_path(call, 'destination', directory / 'payload.zip',
                                  'payload.zip.part0001', 10, 'md5')
        self.assertEqual(run.call_count, 3)
        self.assertTrue(caught.exception.retries_exhausted)
        self.assertEqual([item.args[0] for item in self.sleep.call_args_list], [2, 8])



if __name__ == '__main__':
    unittest.main()
