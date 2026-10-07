import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('sync', Path(__file__).parents[1] / 'setup/github-sync/sync.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

class SnapshotTests(unittest.TestCase):
    def test_new_project_baseline_never_stages_or_pushes_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'product'; root.mkdir()
            (root / 'source.txt').write_text('untracked source')
            original_run = sync.run
            calls = []
            def fake_run(*args, **kwargs):
                if args[0] == 'gh':
                    calls.append(args)
                    return '{"private": true}' if args[1] == 'api' else ''
                return original_run(*args, **kwargs)
            with patch.object(sync, 'run', side_effect=fake_run):
                sync.initialize_private_project(root, {})
            self.assertEqual(sync.git(root, 'ls-tree', '--name-only', 'HEAD'), '')
            self.assertIn('?? source.txt', sync.git(root, 'status', '--porcelain'))
            creation = next(call for call in calls if call[1:3] == ('repo', 'create'))
            self.assertIn('--private', creation)
            self.assertNotIn('--push', creation)

    def test_long_meaningful_path_and_api_key_redaction(self):
        temporary_directory = tempfile.TemporaryDirectory()
        temporary_directory.name = str(sync.long_path(temporary_directory.name))
        with temporary_directory as directory:
            root = sync.long_path(Path(directory) / 'root'); root.mkdir()
            target = sync.long_path(Path(directory) / 'target'); target.mkdir()
            nested = root / ('a' * 100) / ('b' * 100)
            nested.mkdir(parents=True)
            source = nested / ('c' * 100 + '.txt')
            source.write_text('browserKey = "AIza' + 'A' * 35 + '"')
            report = sync.copy_filtered(root, target)
            copied = target / source.relative_to(root)
            self.assertIn('REDACTED_CREDENTIAL', copied.read_text())
            self.assertIn('AIza', source.read_text())
            self.assertIn('redacted', report[0]['reason'])
    def test_pending_push_recovers_only_exact_remote_commit(self):
        entry = {'commit': 'old', 'pending_commit': 'new', 'prior_remote': 'old'}
        self.assertEqual(sync.reconcile_pending(entry, 'new'), 'new')
        self.assertNotIn('pending_commit', entry)
        with self.assertRaisesRegex(RuntimeError, 'changed externally'):
            sync.reconcile_pending({'commit': 'old', 'pending_commit': 'new', 'prior_remote': 'old'}, 'external')

    def test_lock_released_after_exception(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'lock'
            with self.assertRaises(ValueError):
                with sync.process_lock(path) as acquired:
                    self.assertTrue(acquired)
                    raise ValueError('test')
            with sync.process_lock(path) as acquired:
                self.assertTrue(acquired)

    def test_filters_ignored_meaningful_files_and_secrets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'root'; root.mkdir()
            target = Path(directory) / 'out'; target.mkdir()
            (root / '.gitignore').write_text('notes.md\n')
            (root / 'notes.md').write_text('meaningful ignored note')
            (root / '.env').write_text('SECRET=secret')
            (root / 'leak.txt').write_text('ghp_' + 'A' * 40)
            (root / 'nested').mkdir(); (root / 'nested/.git').mkdir()
            report = sync.copy_filtered(root, target)
            self.assertTrue((target / 'notes.md').exists())
            self.assertFalse((target / '.env').exists())
            self.assertIn('REDACTED_CREDENTIAL', (target / 'leak.txt').read_text())
            self.assertFalse((target / 'nested').exists())
            self.assertEqual(len(report), 3)

    def test_snapshot_does_not_change_active_index_or_head(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'repo'; root.mkdir()
            sync.run('git', 'init', str(root))
            sync.git(root, 'config', 'user.email', 'test@localhost')
            sync.git(root, 'config', 'user.name', 'Test')
            (root / 'source.txt').write_text('original')
            sync.git(root, 'add', '.')
            sync.git(root, 'commit', '-m', 'initial')
            (root / 'source.txt').write_text('staged')
            sync.git(root, 'add', '.')
            before = sync.git(root, 'status', '--porcelain')
            head = sync.git(root, 'rev-parse', 'HEAD')
            staging = sync.long_path(Path(directory) / 'files'); staging.mkdir()
            (staging / 'snapshot.txt').write_text('snapshot')
            tree = sync.create_tree(root, staging)
            self.assertTrue(tree)
            self.assertEqual(before, sync.git(root, 'status', '--porcelain'))
            self.assertEqual(head, sync.git(root, 'rev-parse', 'HEAD'))

    def test_external_advance_blocks_publish(self):
        with patch.object(sync, 'verify_private'), patch.object(sync, 'remote_tip', return_value='new'):
            with self.assertRaisesRegex(RuntimeError, 'changed externally'):
                sync.publish(Path('repo'), 'owner/repo', {}, {'repo': {'commit': 'old'}})

    def test_scanner_required(self):
        with self.assertRaisesRegex(RuntimeError, 'unavailable'):
            sync.scan(Path('.'), 'not-present.exe')

    def test_public_repository_blocked(self):
        with patch.object(sync, 'run', return_value='{"private": false}'):
            with self.assertRaisesRegex(RuntimeError, 'private'):
                sync.verify_private('owner/repo')

if __name__ == '__main__': unittest.main()
