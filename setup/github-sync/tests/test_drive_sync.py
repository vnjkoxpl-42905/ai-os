import hashlib
import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch, Mock
from pathlib import Path

spec = importlib.util.spec_from_file_location('drive_sync', Path(__file__).parents[1] / 'drive_sync.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class FakeDrive:
    def __init__(self):
        self.files, self.calls, self.next_id = {}, [], 0
        self.corrupt = False

    def __call__(self, method, params=None, body=None, upload=None):
        self.calls.append(method)
        if method == 'generateIds':
            self.next_id += 1
            return {'ids': [str(self.next_id)]}
        if method == 'list':
            key = params['q'].split("value='")[1].split("'")[0]
            return {'files': [f for f in self.files.values() if f.get('appProperties', {}).get('syncKey') == key]}
        if method == 'create':
            self.files[body['id']] = dict(body, permissions=[{'type': 'user', 'role': 'owner'}])
            file = self.files[body['id']]
        elif method in {'get', 'update'}:
            file = self.files[params['fileId']]
        else:
            raise AssertionError(method)
        if upload:
            data = upload.read_bytes()
            file.update(md5Checksum='bad' if self.corrupt else hashlib.md5(data).hexdigest(), size=str(len(data)))
        return file.copy()

class DriveTests(unittest.TestCase):
    def test_configured_cli_works_without_inherited_path(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            cli = root / 'gws.exe'
            cli.write_bytes(b'fixture')
            config = root / 'config.json'
            config.write_text(json.dumps({'gws_executable': str(cli)}))
            with patch.dict(module.os.environ, {}, clear=True), patch.object(module.shutil, 'which', return_value=None):
                module.configure_cli(config)
                self.assertEqual(module.os.environ['GWS_EXECUTABLE'], str(cli))

    def test_checkout_failure_does_not_block_healthy_mirror(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            state = root / 'state'
            state.mkdir()
            snapshots = {name: {'commit': 'current', 'branch': 'codex/local-sync/machine/' + name,
                                'repository': 'owner/repo'} for name in ['broken', 'healthy']}
            (state / 'state.json').write_text(json.dumps(snapshots))
            mirror = Mock()
            mirror.state = {'checkouts': {name: {'commit': 'current', 'archive_id': name,
                                               'md5': 'digest', 'size': 10, 'folder_id': name,
                                               'repository': 'owner/repo', 'branch': 'branch',
                                               'updated_utc': 'previous'} for name in snapshots}}
            mirror.folder.return_value = 'root'
            mirror.api.side_effect = [module.DriveOperationError('api', 'get', 1, 404),
                                      {'md5Checksum': 'digest', 'size': '10'}]
            with patch.object(module, 'Mirror', return_value=mirror):
                result = module._mirror_from_state(root / 'config.json')
            self.assertEqual([r['status'] for r in result['results']], ['failed', 'unchanged'])
            self.assertNotIn('last_success_utc', mirror.state)

    def test_safe_diagnostics_do_not_expose_arbitrary_error_text(self):
        detail = module.safe_error(RuntimeError('SECRET_SENTINEL'))
        self.assertNotIn('SECRET_SENTINEL', str(detail))
        self.assertEqual(detail['category'], 'unexpected_error')

    def test_api_diagnostics_preserve_code_but_not_untrusted_reason(self):
        error = module.DriveOperationError('api', 'update', 1, 403, 'SECRET_SENTINEL')
        self.assertEqual(module.safe_error(error)['api_code'], 403)
        self.assertNotIn('SECRET_SENTINEL', str(error))

    def test_transient_retry_preserves_command_and_id(self):
        error = type('Response', (), {'returncode': 1, 'stdout': '{"error":{"code":500,"reason":"internalError"}}'})()
        success = type('Response', (), {'returncode': 0, 'stdout': '{"id":"one"}'})()
        with patch.object(module.shutil, 'which', return_value='gws'), patch.object(module.subprocess, 'run', side_effect=[error, success]) as call, patch.object(module.time, 'sleep') as pause:
            result = module.gws('update', {'fileId': 'one'}, {'name': 'latest.zip'})
        self.assertEqual(result['id'], 'one')
        self.assertEqual(call.call_count, 2)
        self.assertEqual(call.call_args_list[0].args, call.call_args_list[1].args)
        pause.assert_called_once_with(1)

    def test_auth_failure_is_not_retried(self):
        error = type('Response', (), {'returncode': 1, 'stdout': '{"error":{"code":403,"reason":"forbidden"}}'})()
        with patch.object(module.shutil, 'which', return_value='gws'), patch.object(module.subprocess, 'run', return_value=error) as call, patch.object(module.time, 'sleep') as pause:
            with self.assertRaisesRegex(RuntimeError, '403'):
                module.gws('get', {'fileId': 'one'})
        self.assertEqual(call.call_count, 1)
        pause.assert_not_called()

    def test_save_preserves_newer_receipts(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'state.json'
            stale = module.Mirror(path, FakeDrive())
            fresh = module.Mirror(path, FakeDrive())
            fresh.state['checkouts']['one'] = {'updated_utc': '2026-10-07T23:00:00Z', 'commit': 'fresh'}
            fresh.save()
            stale.state['checkouts']['two'] = {'updated_utc': '2026-10-07T22:00:00Z', 'commit': 'other'}
            stale.save()
            self.assertEqual(stale.state['checkouts']['one']['commit'], 'fresh')

    def test_cli_upload_cwd_contains_file(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'latest.zip'
            source.write_bytes(b'archive')
            response = type('Response', (), {'returncode': 0, 'stdout': '{"id":"one"}'})()
            with patch.object(module.shutil, 'which', return_value='gws'), patch.object(module.subprocess, 'run', return_value=response) as call:
                module.gws('create', {'fields': 'id'}, {'name': 'latest.zip'}, source)
            self.assertEqual(call.call_args.kwargs['cwd'], str(source.resolve().parent))

    def test_upload_is_idempotent_and_updates_same_id(self):
        with tempfile.TemporaryDirectory() as temp:
            api = FakeDrive()
            mirror = module.Mirror(Path(temp) / 'state.json', api)
            source = Path(temp) / 'latest.zip'
            source.write_bytes(b'first')
            first, _ = mirror.upload('parent', 'latest.zip', 'key', source, 'application/zip')
            second, _ = mirror.upload('parent', 'latest.zip', 'key', source, 'application/zip')
            self.assertEqual(first, second)
            self.assertEqual(api.calls.count('create'), 1)
            self.assertEqual(api.calls.count('update'), 0)
            source.write_bytes(b'second')
            third, _ = mirror.upload('parent', 'latest.zip', 'key', source, 'application/zip')
            self.assertEqual(first, third)
            self.assertEqual(api.calls.count('update'), 1)
            self.assertNotIn('delete', api.calls)

    def test_checksum_failure_does_not_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            api = FakeDrive()
            api.corrupt = True
            mirror = module.Mirror(Path(temp) / 'state.json', api)
            source = Path(temp) / 'latest.zip'
            source.write_bytes(b'data')
            with self.assertRaisesRegex(RuntimeError, 'checksum'):
                mirror.upload('parent', 'latest.zip', 'key', source, 'application/zip')

    def test_duplicate_destination_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            api = FakeDrive()
            api.files = {'one': {'appProperties': {'syncKey': 'key'}}, 'two': {'appProperties': {'syncKey': 'key'}}}
            mirror = module.Mirror(Path(temp) / 'state.json', api)
            with self.assertRaisesRegex(RuntimeError, 'Ambiguous'):
                mirror.folder('parent', 'folder', 'key')

    def test_shared_destination_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            api = FakeDrive()
            api.files = {'one': {'id': 'one', 'appProperties': {'syncKey': 'key'}, 'permissions': [{'type': 'anyone', 'role': 'reader'}]}}
            mirror = module.Mirror(Path(temp) / 'state.json', api)
            with self.assertRaisesRegex(RuntimeError, 'sharing'):
                mirror.folder('parent', 'folder', 'key')

    def test_uncertain_create_recovers_reserved_id(self):
        with tempfile.TemporaryDirectory() as temp:
            api = FakeDrive()
            def uncertain(method, params=None, body=None, upload=None):
                result = api(method, params, body, upload)
                if method == 'create':
                    raise RuntimeError('connection ended after upload')
                return result
            mirror = module.Mirror(Path(temp) / 'state.json', uncertain)
            folder = mirror.folder('parent', 'folder', 'key')
            self.assertEqual(folder, '1')
            self.assertEqual(api.calls.count('create'), 1)
            self.assertEqual(mirror.state['ids']['key'], '1')

if __name__ == '__main__':
    unittest.main()
