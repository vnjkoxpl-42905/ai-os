import contextlib
from datetime import datetime, timezone
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

doctor = load('workspace_doctor', 'workspace-doctor.py')
validator = load('check_skills_fixture', 'check-skills.py')
NOW = datetime(2026, 11, 14, 12, tzinfo=timezone.utc)

class DoctorChecks(unittest.TestCase):
    def test_missing_hook_target_detected(self):
        result = doctor.hook_targets([r'C:\missing\agent-hook.cmd'], lambda p: False)
        self.assertEqual(result.state, 'failed')

    def test_absolute_interpreter_and_relative_script_is_unknown(self):
        command = r'C:\Python\python.exe missing.py'
        result = doctor.hook_targets([command], lambda path: True)
        self.assertEqual(result.state, 'unknown')

    def test_unresolved_hook_is_unknown(self):
        result = doctor.hook_targets(['some-command --dynamic'], lambda p: True)
        self.assertEqual(result.state, 'unknown')

    def test_stale_success_receipt_is_warning(self):
        result = doctor.receipt_finding({'last_success': '2026-11-10T12:00:00+00:00'}, NOW)
        self.assertEqual(result.state, 'warning')

    def test_recent_receipt_does_not_prove_restore(self):
        result = doctor.receipt_finding({'last_success': '2026-11-14T11:00:00+00:00'}, NOW)
        self.assertEqual(result.state, 'healthy')
        self.assertIn('restore', result.action)

    def test_date_only_checkpoint_is_unknown(self):
        result = doctor.checkpoint_finding('- **Checkpoint time:** 2026-11-14, America/Toronto.', NOW)
        self.assertEqual(result.state, 'unknown')

    def test_old_checkpoint_is_warning(self):
        result = doctor.checkpoint_finding('- **Checkpoint time:** 2026-10-01T10:00:00+00:00', NOW)
        self.assertEqual(result.state, 'warning')

    def test_shared_section_drift_detected(self):
        first = '## Routing map\nA\n## Guardrails\nB\n'
        self.assertEqual(doctor.policy_finding(first, first.replace('B', 'C')).state, 'warning')

    def test_compare_and_swap_refuses_intervening_change(self):
        # New isolated fixtures are deliberately retained.
        base = Path(tempfile.mkdtemp(prefix='workspace-doctor-test-'))
        target = base / 'health.md'
        target.write_text(doctor.MARKER + '\nold', encoding='utf-8')
        expected = doctor.digest(target.read_bytes())
        target.write_text(doctor.MARKER + '\nchanged', encoding='utf-8')
        with self.assertRaises(RuntimeError):
            doctor.write_report(target, expected, doctor.MARKER + '\nnew', base / 'test.lock')
        self.assertIn('changed', target.read_text(encoding='utf-8'))

    def test_project_codex_invalid_toml_is_failed(self):
        root = Path(tempfile.mkdtemp(prefix='workspace-doctor-settings-'))
        home = root / 'home'
        for path in [home/'.codex/hooks.json', home/'.claude/settings.json', root/'.codex/hooks.json', root/'.claude/settings.json']:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('{}', encoding='utf-8')
        (home/'.codex/config.toml').write_text('enabled = true', encoding='utf-8')
        (root/'.codex/config.toml').write_text('[broken', encoding='utf-8')
        self.assertEqual(doctor.settings_findings(root, home)[0].state, 'failed')

    def test_old_combined_success_warns(self):
        finding = doctor.runner_finding({'outcome': 'succeeded', 'completed_utc': '2026-10-01T10:00:00+00:00'}, NOW)
        self.assertEqual(finding.state, 'warning')

    def test_success_without_completion_time_is_unknown(self):
        self.assertEqual(doctor.runner_finding({'outcome': 'succeeded'}, NOW).state, 'unknown')

    def test_recent_combined_success_is_healthy(self):
        finding = doctor.runner_finding({'outcome': 'succeeded', 'completed_utc': '2026-11-14T11:00:00+00:00'}, NOW)
        self.assertEqual(finding.state, 'healthy')

    def test_existing_validator_accepts_declared_runtime_difference(self):
        root = Path(tempfile.mkdtemp(prefix='workspace-skill-parity-test-'))
        db = root / 'skills'
        (db / 'claude' / 'only-claude').mkdir(parents=True)
        (db / 'codex').mkdir()
        (db / 'claude' / 'only-claude' / 'SKILL.md').write_text('---\nname: only-claude\n---\n', encoding='utf-8')
        (db / 'INDEX.md').write_text('- **only-claude**\n', encoding='utf-8')
        (db / 'PARITY.md').write_text(chr(96) + 'only-claude' + chr(96) + ' is deliberately Claude-only.\n', encoding='utf-8')
        (root / 'AGENTS.md').write_text('# policy\n', encoding='utf-8')
        (root / 'CLAUDE.md').write_text('# policy\n', encoding='utf-8')
        overrides = {'BRAIN': str(root), 'DB': str(db), 'PROJECT_ACTIVE_ROOTS': [],
                     'RUNTIME_ACTIVE_ROOTS': {'claude': [], 'codex': []}}
        with patch.multiple(validator, **overrides), patch.object(validator.subprocess, 'run', return_value=types.SimpleNamespace(stdout='')), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertIsNone(validator.main())

if __name__ == '__main__':
    unittest.main()
