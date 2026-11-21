import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('manifest_runner', Path(__file__).with_name('runner.py'))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class InspectionManifest(unittest.TestCase):
    def test_large_complete_manifest_is_externalized_with_verified_digest(self):
        # Realistic deep paths create a manifest larger than Claude's 10 MB stdin cap.
        files = [{'path': f'preserved/{i}/' + ('nested/' * 70) + 'source.py',
                  'kind': 'file', 'sha256': runner.digest(str(i).encode())}
                 for i in range(20000)]
        manifest = {'base': 'base-commit', 'files': files, 'diff_sha256': 'diff-digest'}
        manifest['sha256'] = runner.digest(json.dumps(manifest, sort_keys=True).encode())
        self.assertGreater(len(json.dumps(manifest).encode()), 10_000_000)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prompt = runner.inspection_manifest_prompt(manifest, root)
            self.assertLess(len(prompt.encode()), 4096)
            artifact = root / 'change-manifest.json'
            self.assertEqual(json.loads(artifact.read_text(encoding='utf-8')), manifest)
            self.assertIn(str(artifact), prompt)
            self.assertIn(runner.digest(artifact.read_bytes()), prompt)
            self.assertIn(manifest['sha256'], prompt)
            self.assertIn('20000', prompt)
            self.assertIn('Report any coverage limits', prompt)
            self.assertEqual(manifest['files'], files)

    def test_small_manifest_keeps_existing_inline_contract(self):
        manifest = {'base': 'base', 'files': [{'path': 'changed.py', 'kind': 'file', 'sha256': 'hash'}], 'sha256': 'snapshot'}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prompt = runner.inspection_manifest_prompt(manifest, root)
            self.assertIn(json.dumps(manifest, ensure_ascii=False), prompt)
            self.assertFalse((root / 'change-manifest.json').exists())


if __name__ == '__main__':
    unittest.main()
