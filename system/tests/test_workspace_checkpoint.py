import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'check-workspace-checkpoint.py'
spec = importlib.util.spec_from_file_location('checkpoint_verifier', SCRIPT)
verifier = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = verifier
spec.loader.exec_module(verifier)

class CheckpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Real Git fixture deliberately persists; it never touches an existing checkout.
        cls.base = Path(tempfile.mkdtemp(prefix='workspace-checkpoint-fixture-'))
        cls.repo = cls.base / 'checkout'
        cls.repo.mkdir()
        cls.run_git('init', '-b', 'checkpoint-fixture')
        (cls.repo / 'fixture.txt').write_text('one\n', encoding='utf-8')
        cls.run_git('add', 'fixture.txt')
        cls.run_git('-c', 'user.name=Checkpoint Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-m', 'fixture one')
        cls.first = cls.run_git('rev-parse', 'HEAD').stdout.strip()
        cls.record = cls.base / 'checkpoint.md'

    @classmethod
    def run_git(cls, *args):
        env = dict(os.environ)
        env.update({'GIT_TERMINAL_PROMPT': '0', 'GIT_OPTIONAL_LOCKS': '0'})
        return subprocess.run(['git', '-C', str(cls.repo), *args], env=env, capture_output=True, text=True, check=True)

    def checkpoint(self, *, path=None, branch='checkpoint-fixture', head=None, writer='Yielded'):
        self.record.write_text('\n'.join([
            '- **Canonical repository and actual checkout:** ' + str(path or self.repo),
            '- **Branch and observed HEAD:** ' + branch + ', ' + (head or self.first) + ', observed for test',
            '- **Active writer:** ' + writer, ''
        ]), encoding='utf-8')
        return verifier.verify(self.record)

    def test_valid_then_real_stale_head(self):
        findings = self.checkpoint()
        self.assertTrue(all(f.state == 'pass' for f in findings), findings)
        (self.repo / 'second.txt').write_text('two\n', encoding='utf-8')
        self.run_git('add', 'second.txt')
        self.run_git('-c', 'user.name=Checkpoint Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-m', 'fixture two')
        findings = self.checkpoint()
        self.assertEqual(next(f.state for f in findings if f.check == 'HEAD'), 'failed')

    def test_missing_record_is_failed(self):
        self.assertEqual(verifier.verify(self.base / 'absent.md')[0].state, 'failed')

    def test_invalid_record_is_failed(self):
        self.record.write_text('No fields', encoding='utf-8')
        self.assertEqual(verifier.verify(self.record)[0].state, 'failed')

    def test_unyielded_and_missing_checkout_detected(self):
        findings = self.checkpoint(path=self.base/'missing', writer='Codex, still working')
        self.assertEqual(next(f.state for f in findings if f.check == 'Ownership'), 'failed')
        self.assertEqual(next(f.state for f in findings if f.check == 'Checkout'), 'failed')

    def test_branch_discrepancy(self):
        findings = self.checkpoint(branch='different-branch')
        self.assertEqual(next(f.state for f in findings if f.check == 'Branch'), 'failed')

    def test_short_head_rejected(self):
        findings = self.checkpoint(head='abc123')
        self.assertEqual(findings[0].check, 'Checkpoint')
        self.assertEqual(findings[0].state, 'failed')

if __name__ == '__main__':
    unittest.main()
