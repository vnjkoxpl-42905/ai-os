import hashlib
import importlib.util
import tempfile
import unittest
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
