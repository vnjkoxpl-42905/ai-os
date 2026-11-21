import importlib.util
import tempfile
import unittest
import subprocess
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('credential_bundle', Path(__file__).parents[1] / 'setup/github-sync/credential_bundle.py')
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

class CredentialTests(unittest.TestCase):
    def test_multipart_reassembles_original_and_detects_corrupt_chunk(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = b'Useful context and original credential 123456\n' * 20
            with patch.object(module, 'MAX_CHUNK_BYTES', 32):
                metadata = module.bundle([], root / 'state', root / 'snapshot', 'redacted-context', {'lesson.md': original})
                self.assertGreater(len(metadata['ciphertext_parts']), 1)
                for part in metadata['ciphertext_parts']:
                    self.assertLessEqual((root / 'snapshot' / part['file']).stat().st_size, 32)
                key = (root / 'state/secrets.key').read_bytes()
                package = root / 'snapshot/redacted-context.enc'
                module.decrypt(package, root / 'restored', key)
                self.assertEqual((root / 'restored/lesson.md').read_bytes(), original)
                first = root / 'snapshot' / metadata['ciphertext_parts'][0]['file']
                first.write_bytes(b'corrupt')
                with self.assertRaisesRegex(ValueError, 'integrity'):
                    module.decrypt(package, root / 'corrupt', key)

    def test_compressed_original_context_same_key_cache_isolation_and_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / '.env'; source.write_text('PRIVATE=original')
            module.bundle([{'path': str(source), 'label': 'env'}], root / 'state', root / 'snapshot')
            primary = (root / 'snapshot/credentials.enc').read_bytes()
            original = b'Safe lesson\npassword=the-original-credential\nUseful lesson\n'
            arguments = ([], root / 'context-cache', root / 'snapshot', 'redacted-context', {'project/lesson.md': original})
            module.bundle(*arguments, key_state=root / 'state')
            context = root / 'snapshot/redacted-context.enc'
            encrypted = context.read_bytes()
            module.bundle(*arguments, key_state=root / 'state')
            self.assertEqual(encrypted, context.read_bytes())
            self.assertEqual(primary, (root / 'snapshot/credentials.enc').read_bytes())
            key = (root / 'state/secrets.key').read_bytes()
            module.decrypt(context, root / 'recovered', key)
            self.assertEqual((root / 'recovered/project/lesson.md').read_bytes(), original)
            context.write_bytes(encrypted[:-1] + bytes([encrypted[-1] ^ 1]))
            with self.assertRaisesRegex(ValueError, 'authentication'):
                module.decrypt(context, root / 'tampered', key)
            with self.assertRaisesRegex(ValueError, 'JSONL'):
                module.bundle([], root / 'state', root / 'snapshot', 'redacted-context', {'session.jsonl': b'raw'})

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
