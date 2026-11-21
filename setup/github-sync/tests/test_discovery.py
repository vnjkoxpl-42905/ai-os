import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('workspace_sync_discovery', Path(__file__).parents[1] / 'sync.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DiscoveryTests(unittest.TestCase):
    def test_scan_uses_configured_deadline_without_skipping_scan(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            executable = root / 'scanner.exe'
            executable.write_bytes(b'fixture')
            destination = root / 'snapshot'
            destination.mkdir()
            response = type('Response', (), {'returncode': 0})()
            with patch.object(module.subprocess, 'run', return_value=response) as call:
                module.scan(destination, executable, timeout=900)
            self.assertEqual(call.call_args.kwargs['timeout'], 900)
            self.assertIn('--redact=100', call.call_args.args[0])

    def test_rescan_keeps_configured_deadline(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            executable = root / 'scanner.exe'
            executable.write_bytes(b'fixture')
            destination = root / 'snapshot'
            destination.mkdir()
            (root / 'gitleaks.json').write_text('[]')
            findings = type('Response', (), {'returncode': 1})()
            clean = type('Response', (), {'returncode': 0})()
            with patch.object(module.subprocess, 'run', side_effect=[findings, clean]) as call:
                module.scan(destination, executable, timeout=900)
            self.assertEqual([c.kwargs['timeout'] for c in call.call_args_list], [900, 900])

    def test_upstream_tooling_clone_is_skipped_without_inspecting_or_publishing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            vault, projects = root / 'ai-os', root / 'projects'
            for path in (vault, projects / 'claudex-loop', projects / 'lsatu'):
                (path / '.git').mkdir(parents=True)
            config = {'ai_os': str(vault), 'projects_root': str(projects), 'owner': 'owner'}
            with patch.object(module, 'git', side_effect=lambda path, *args: f'https://github.com/owner/{path.name}.git') as git:
                found = module.discover(config)
            self.assertEqual([path.name for path, _ in found], ['ai-os', 'lsatu'])
            self.assertEqual([call.args[0].name for call in git.call_args_list], ['ai-os', 'lsatu'])
            self.assertFalse(config.get('_discovery_errors'))
            self.assertEqual(config['_discovery_skipped'][0]['folder'], 'claudex-loop')

    def test_other_unapproved_remote_remains_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            vault, projects = root / 'ai-os', root / 'projects'
            for path in (vault, projects / 'other'):
                (path / '.git').mkdir(parents=True)
            config = {'ai_os': str(vault), 'projects_root': str(projects), 'owner': 'owner'}
            with patch.object(module, 'git', side_effect=lambda path, *args: f'https://github.com/{"owner" if path == vault else "upstream"}/{path.name}.git'):
                found = module.discover(config)
            self.assertEqual([path.name for path, _ in found], ['ai-os'])
            self.assertEqual(config['_discovery_errors'][0]['error'], 'Unapproved remote')


if __name__ == '__main__':
    unittest.main()
