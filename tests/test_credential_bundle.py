import importlib.util
import tempfile
import unittest
import subprocess
from pathlib import Path

spec = importlib.util.spec_from_file_location('credential_bundle', Path(__file__).parents[1] / 'setup/github-sync/credential_bundle.py')
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

class CredentialTests(unittest.TestCase):
    def test_linked_destination_and_source_ancestor_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            real = root / 'real'; real.mkdir()
            secret = real / '.env'; secret.write_text('secret')
            link = root / 'linked'
            try:
                link.symlink_to(real, target_is_directory=True)
            except OSError:
                if __import__('os').name != 'nt': raise
                result = subprocess.run(['cmd', '/c', 'mklink', '/J', str(link), str(real)], capture_output=True)
                if result.returncode: self.skipTest('No junction capability')
            with self.assertRaisesRegex(ValueError, 'link'):
                module.collect([{'path': str(link / '.env'), 'label': 'env'}])
            sources = [{'path': str(secret), 'label': 'env'}]
            module.bundle(sources, root / 'state', root / 'snapshot')
            key = (root / 'state/secrets.key').read_bytes()
            with self.assertRaisesRegex(ValueError, 'link'):
                module.decrypt(root / 'snapshot/credentials.enc', link / 'output', key)
            self.assertFalse((real / 'output').exists())

    def test_env_discovery_includes_future_projects_and_prunes_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory) / 'vault'; vault.mkdir()
            product = Path(directory) / 'new-product'; product.mkdir()
            (vault / '.env').write_text('secret')
            (product / '.env.local').write_text('secret')
            (product / '.env.example').write_text('placeholder')
            (product / 'node_modules').mkdir()
            (product / 'node_modules/.env').write_text('dependency')
            result = module.discover_env_sources({'ai_os': str(vault), '_allowed_roots': [str(vault), str(product)]})
            self.assertEqual(sorted(item['label'] for item in result), ['ai-os/.env', 'projects/new-product/.env.local'])

    def test_round_trip_cache_and_authentication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / '.env'; source.write_text('PRIVATE_SECRET=never-publish-cleartext')
            sources = [{'path': str(source), 'label': 'ai-os/.env'}]
            module.bundle(sources, root / 'state', root / 'snapshot')
            package = root / 'snapshot/credentials.enc'
            original = package.read_bytes()
            self.assertNotIn(b'never-publish-cleartext', original)
            module.bundle(sources, root / 'state', root / 'snapshot')
            self.assertEqual(package.read_bytes(), original)
            key = (root / 'state/secrets.key').read_bytes()
            with self.assertRaisesRegex(ValueError, 'authentication'):
                module.decrypt(package, root / 'wrong', b'X' * 32)
            module.decrypt(package, root / 'restored', key)
            self.assertEqual((root / 'restored/ai-os/.env').read_bytes(), source.read_bytes())
            with self.assertRaisesRegex(ValueError, 'overwrite'):
                module.decrypt(package, root / 'restored', key)

    def test_traversal_and_native_auth_rejected(self):
        with self.assertRaises(ValueError): module._safe_name('../secret')
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'Cookies'; source.write_text('native cookie data')
            with self.assertRaisesRegex(RuntimeError, 'not portable'):
                module.collect([{'path': str(source), 'label': 'browser/Cookies'}])

if __name__ == '__main__': unittest.main()
