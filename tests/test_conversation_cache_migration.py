import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SYNC_ROOT = Path(__file__).resolve().parents[1] / 'setup/github-sync'
sys.path.insert(0, str(SYNC_ROOT))
spec = importlib.util.spec_from_file_location(
    'cache_migration', SYNC_ROOT / 'migrate_conversation_cache.py')
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)


class ConversationCacheMigrationTests(unittest.TestCase):
    def cache(self, root):
        old = root / 'conversations'
        (old / 'codex').mkdir(parents=True)
        (old / 'codex/sample.md').write_text('# Sample\nContent\n', encoding='utf-8')
        (old / 'index.json').write_text('{"sessions": []}', encoding='utf-8')
        return old

    def test_preserves_files_and_cloud_copy_paths(self):
        from sync import copy_filtered
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            before = migration.manifest(self.cache(state))
            result = migration.migrate(state)
            self.assertEqual(result['status'], 'verified')
            self.assertEqual(before, migration.manifest(state / '.conversations'))
            cloud = state / 'snapshot/.cloud-sync/conversations'
            copy_filtered(state / '.conversations', cloud)
            self.assertEqual(before, migration.manifest(cloud))
            self.assertEqual(migration.migrate(state)['status'], 'already-migrated')

    def test_refuses_conflicting_locations(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            self.cache(state)
            (state / '.conversations').mkdir()
            with self.assertRaisesRegex(RuntimeError, 'Both cache'):
                migration.migrate(state)
            self.assertTrue((state / 'conversations/codex/sample.md').exists())

    def test_rolls_back_when_verification_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            old = self.cache(state)
            before = migration.manifest(old)
            with patch.object(migration, 'manifest', side_effect=[before, {}]):
                with self.assertRaisesRegex(RuntimeError, 'hashes differ'):
                    migration.migrate(state)
            self.assertEqual(migration.manifest(old), before)
            self.assertFalse((state / '.conversations').exists())

    def test_directory_read_failure_aborts_before_rename(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            old = self.cache(state)

            def unreadable(*args, **kwargs):
                kwargs['onerror'](PermissionError('Directory unavailable'))

            with patch.object(migration.os, 'walk', side_effect=unreadable):
                with self.assertRaisesRegex(PermissionError, 'unavailable'):
                    migration.migrate(state)
            self.assertTrue(old.exists())
            self.assertFalse((state / '.conversations').exists())


if __name__ == '__main__':
    unittest.main()
