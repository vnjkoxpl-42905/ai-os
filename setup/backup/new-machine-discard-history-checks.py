"""Isolated failed-history cleanup tests. Never touches real backups or Drive."""
from contextlib import nullcontext
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import new_machine_discard_failed_history as cleanup


class CleanupTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.stage = Path(self.temporary.name)
        self.addCleanup(patch.stopall)
        patch.object(cleanup, 'STAGE', self.stage).start()
        patch.object(cleanup, 'scheduled_lock', return_value=nullcontext()).start()
        self.verify = patch.object(cleanup, 'verify_cloud_closure').start()
        self.cloud = SimpleNamespace(upload_lock=lambda directory: nullcontext())
        self.plan_path = self.stage / 'plan.json'
        self.entries = []
        for number, name in enumerate(sorted(cleanup.TARGET_GENERATIONS)):
            directory = self.stage / name
            directory.mkdir()
            content = ('historical-' + str(number)).encode()
            (directory / 'payload.zip').write_bytes(content)
            manifest = {'generation': name, 'scope': 'core', 'complete': False,
                        'archive_bytes': len(content), 'archive_sha256': hashlib.sha256(content).hexdigest(), 'files': {}}
            raw = json.dumps(manifest).encode()
            (directory / 'manifest.json').write_bytes(raw)
            (directory / 'metadata-preserve.txt').write_text('keep')
            (directory / 'sqlite-snapshots').mkdir()
            (directory / 'sqlite-snapshots' / 'keep.db').write_bytes(b'keep')
            self.entries.append({'generation': name, 'delete_file_if_approved': str(directory / 'payload.zip'),
                                 'bytes': len(content), 'archive_sha256': manifest['archive_sha256'],
                                 'manifest_sha256': hashlib.sha256(raw).hexdigest()})
        for scope, name in [('core', '20261024-211629'), ('personal', '20261024-213612')]:
            directory = self.stage / name
            directory.mkdir()
            (directory / 'manifest.json').write_text(json.dumps({'generation': name, 'scope': scope, 'complete': True, 'files': {}}))
        self.write_plan()

    def write_plan(self):
        self.plan_path.write_text(json.dumps({'conditional_discard_failed_core_payloads': self.entries}))
        self.confirmation = cleanup.file_sha256(self.plan_path)

    def apply(self, **kwargs):
        return cleanup.run(self.plan_path, True, self.confirmation, cloud=self.cloud, call=lambda *args: {}, **kwargs)

    def assert_all_present(self):
        self.assertTrue(all(Path(entry['delete_file_if_approved']).exists() for entry in self.entries))

    def test_default_dry_run_never_deletes_or_calls_cloud(self):
        result = cleanup.run(self.plan_path)
        self.assertEqual(result['mode'], 'dry-run')
        self.assert_all_present()
        self.verify.assert_not_called()

    def test_apply_exact_ten_preserves_metadata_snapshots(self):
        result = self.apply()
        self.assertEqual(len(result['deleted']), 10)
        self.assertEqual(json.loads(Path(result['audit']).read_text())['status'], 'deleted')
        self.verify.assert_called_once()
        for entry in self.entries:
            directory = self.stage / entry['generation']
            self.assertFalse((directory / 'payload.zip').exists())
            self.assertTrue((directory / 'manifest.json').exists())
            self.assertEqual((directory / 'sqlite-snapshots' / 'keep.db').read_bytes(), b'keep')

    def test_requires_explicit_exact_plan_sha(self):
        for confirmation in [None, '0' * 64]:
            with self.assertRaises(ValueError):
                cleanup.run(self.plan_path, True, confirmation)
        self.assert_all_present()

    def test_wrong_target_or_target_count_refused(self):
        self.entries[0]['delete_file_if_approved'] = str(self.stage / 'other' / 'payload.zip')
        self.write_plan()
        with self.assertRaises(ValueError):
            cleanup.run(self.plan_path)
        self.entries = self.entries[:-1]
        self.write_plan()
        with self.assertRaises(ValueError):
            cleanup.run(self.plan_path)

    def test_current_dependency_blocks_history_deletion(self):
        path = self.stage / '20261024-211629' / 'manifest.json'
        value = json.loads(path.read_text())
        value['files'] = {'x': {'generation': self.entries[0]['generation']}}
        path.write_text(json.dumps(value))
        with self.assertRaises(ValueError):
            self.apply()
        self.assert_all_present()

    def test_busy_uploader_refuses_all_deletion(self):
        def busy(directory):
            raise OSError('upload is active')
        self.cloud.upload_lock = busy
        with self.assertRaises(OSError):
            self.apply()
        self.assert_all_present()

    def test_cloud_failure_preserves_all_targets(self):
        self.verify.side_effect = RuntimeError('cloud checksum failed')
        with self.assertRaises(RuntimeError):
            self.apply()
        self.assert_all_present()

    def test_corrupt_same_size_target_blocks_all_deletions(self):
        target = Path(self.entries[-1]['delete_file_if_approved'])
        target.write_bytes(b'x' * target.stat().st_size)
        with self.assertRaises(ValueError):
            self.apply()
        self.assert_all_present()

    def test_new_receipt_target_skipped_without_broadening_scope(self):
        directory = self.stage / self.entries[0]['generation']
        (directory / 'CLOUD-VERIFIED.json').write_text('{}')
        result = self.apply()
        self.assertEqual(len(result['deleted']), 9)
        self.assertEqual(len(result['skipped_targets']), 1)
        self.assertTrue((directory / 'payload.zip').exists())

    def test_missing_target_skipped_for_safe_resume(self):
        Path(self.entries[0]['delete_file_if_approved']).unlink()
        result = self.apply()
        self.assertEqual(len(result['deleted']), 9)
        self.assertEqual(len(result['skipped_targets']), 1)


if __name__ == '__main__':
    unittest.main()
