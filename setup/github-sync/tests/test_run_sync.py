import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location('run_sync', ROOT / 'run_sync.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sys.path.pop(0)


class RunnerTests(unittest.TestCase):
    def run_fixture(self, state, github=0, drive=None, error=None):
        response = type('Response', (), {'returncode': github})()
        with patch.object(module.subprocess, 'run', return_value=response), patch.object(
                module, 'mirror_from_state', return_value=drive or {'results': []}, side_effect=error):
            return module.run_once(state.parent / 'config.json', state)

    def test_distinct_runs_preserve_history_and_latest_status(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            first, _ = self.run_fixture(state)
            second, failed = self.run_fixture(state)
            events = json.loads((state / 'runner-history.json').read_text())['events']
            self.assertFalse(failed)
            self.assertNotEqual(first['run_id'], second['run_id'])
            self.assertEqual([e['event'] for e in events], ['started', 'succeeded', 'started', 'succeeded'])
            self.assertEqual(json.loads((state / 'runner-status.json').read_text())['run_id'], second['run_id'])

    def test_failure_is_durable_and_does_not_leak_exception_text(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            receipt, failed = self.run_fixture(state, error=RuntimeError('SECRET_SENTINEL'))
            self.assertTrue(failed)
            self.assertEqual(receipt['drive_error'], 'RuntimeError')
            self.assertEqual(receipt['outcome'], 'failed')
            self.assertNotIn('SECRET_SENTINEL', ''.join(p.read_text() for p in state.glob('*.json')))

    def test_github_launch_failure_is_recorded(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            with patch.object(module.subprocess, 'run', side_effect=OSError('SECRET_SENTINEL')), patch.object(
                    module, 'mirror_from_state', return_value={'results': []}):
                receipt, failed = module.run_once(state.parent / 'config.json', state)
            self.assertTrue(failed)
            self.assertEqual(receipt['github_error'], 'OSError')

    def test_failed_drive_result_is_not_reported_as_success(self):
        with tempfile.TemporaryDirectory() as temp:
            receipt, failed = self.run_fixture(Path(temp), drive={'results': [
                {'checkout': 'broken', 'status': 'failed', 'error': {'category': 'api'}},
                {'checkout': 'healthy', 'status': 'unchanged'}]})
            self.assertTrue(failed)
            self.assertEqual(receipt['outcome'], 'failed')

    def test_drive_busy_is_deferred_not_success(self):
        with tempfile.TemporaryDirectory() as temp:
            receipt, failed = self.run_fixture(Path(temp), drive={'status': 'busy', 'results': []})
            self.assertFalse(failed)
            self.assertEqual(receipt['outcome'], 'deferred')

    def test_child_lock_collision_defers_without_mirroring_stale_state(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            response = type('Response', (), {'returncode': 0, 'stdout': '{"status": "busy"}'})()
            with patch.object(module.subprocess, 'run', return_value=response), patch.object(
                    module, 'mirror_from_state') as mirror:
                receipt, failed = module.run_once(state.parent / 'config.json', state)
            mirror.assert_not_called()
            self.assertFalse(failed)
            self.assertEqual(receipt['outcome'], 'deferred')
            self.assertEqual(receipt['github_status'], 'busy')
            events = json.loads((state / 'runner-history.json').read_text())['events']
            self.assertEqual(events[-1]['event'], 'deferred')

    def test_history_has_a_bounded_window(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            with patch.object(module, 'HISTORY_LIMIT', 3):
                for i in range(5):
                    module.record_event(state, str(i), 'started')
            events = json.loads((state / 'runner-history.json').read_text())['events']
            self.assertEqual([e['run_id'] for e in events], ['2', '3', '4'])


if __name__ == '__main__':
    unittest.main()
