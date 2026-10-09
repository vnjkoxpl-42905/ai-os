import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('sync_runtime_lock_probe', Path(__file__).parents[1] / 'sync.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RuntimeLockTests(unittest.TestCase):
    def test_active_runtime_lock_skipped_dependency_lock_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            source, destination = Path(temp) / 'source', Path(temp) / 'copy'
            locks = source / 'runtime/codex-hooks'
            locks.mkdir(parents=True)
            process_lock = locks / 'session.lock'
            process_lock.write_bytes(b'0')
            (source / 'uv.lock').write_text('version = 1\n')
            (source / 'runtime/uv.lock').write_text('version = 1\n')
            (source / 'package-lock.json').write_text('{"lockfileVersion":3}')
            handle = process_lock.open('r+b')
            try:
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                report = module.copy_filtered(source, destination)
                self.assertFalse((destination / 'runtime/codex-hooks/session.lock').exists())
                self.assertTrue((destination / 'uv.lock').exists())
                self.assertTrue((destination / 'runtime/uv.lock').exists())
                self.assertTrue((destination / 'package-lock.json').exists())
                self.assertIn({'path': 'runtime/codex-hooks/session.lock', 'reason': 'runtime process lock'}, report)
            finally:
                if os.name == 'nt':
                    handle.seek(0)
                    msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
                handle.close()

if __name__ == '__main__': unittest.main()
