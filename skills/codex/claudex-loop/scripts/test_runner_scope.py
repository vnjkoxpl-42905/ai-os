import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('scope_runner', Path(__file__).with_name('runner.py'))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class InspectionScope(unittest.TestCase):
    def git(self, root, *args):
        return subprocess.run(['git', *args], cwd=root, capture_output=True, check=True).stdout

    def test_scope_preserves_all_local_change_types_and_ignores_external_activity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, 'init', '-q')
            (root / 'work').mkdir()
            for name in ('edited', 'deleted', 'staged'):
                (root / 'work' / name).write_text('original')
            (root / 'unrelated').write_text('original')
            self.git(root, 'add', '.')
            self.git(root, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.com', 'commit', '-qm', 'fixture')
            base = self.git(root, 'rev-parse', 'HEAD').decode().strip()
            (root / 'work' / 'edited').write_text('modified')
            (root / 'work' / 'deleted').unlink()
            (root / 'work' / 'staged').write_text('staged change')
            self.git(root, 'add', 'work/staged')
            (root / 'work' / 'untracked').write_text('new')
            scoped = runner.snapshot(root, base, ['work'])
            self.assertEqual(scoped['scope'], ['work'])
            self.assertEqual({row['path'] for row in scoped['files']}, {'work/edited', 'work/deleted', 'work/staged', 'work/untracked'})
            self.assertEqual(next(row['kind'] for row in scoped['files'] if row['path'] == 'work/deleted'), 'deleted')
            full_before = runner.snapshot(root, base)
            self.assertNotIn('scope', full_before)
            (root / 'unrelated').write_text('changed independently')
            self.assertEqual(runner.snapshot(root, base, ['work']), scoped)
            self.assertNotEqual(runner.snapshot(root, base)['sha256'], full_before['sha256'])
            (root / 'work' / 'untracked').write_text('changed inside scope')
            self.assertNotEqual(runner.snapshot(root, base, ['work'])['sha256'], scoped['sha256'])
            self.assertNotEqual(runner.snapshot(root, base, ['work/edited'])['sha256'], scoped['sha256'])

    def test_scope_rejects_traversal_absolute_and_git_magic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for value in ('../outside', 'work/../outside', '/absolute', 'C:/absolute', ':!excluded', ':(glob)**', 'work\\outside', '', 'work//file', './work'):
                with self.subTest(value=value), self.assertRaises(runner.RunError):
                    runner.inspection_scope(root, [value])
            self.assertEqual(runner.inspection_scope(root, ['work', 'work/file.py', 'work']), ['work', 'work/file.py'])


if __name__ == '__main__':
    unittest.main()
