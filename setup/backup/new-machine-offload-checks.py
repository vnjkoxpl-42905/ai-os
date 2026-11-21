"""Focused isolated offload safety checks; no real cloud access or backup writes."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from types import SimpleNamespace
from unittest.mock import patch

import new_machine_offload as module


class OffloadTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.stage = Path(self.temp.name)
        self.generation = self.stage / '20261023-120000'
        self.generation.mkdir()
        self.data = b'archive-test-data'
        sha = hashlib.sha256(self.data).hexdigest()
        md5 = hashlib.md5(self.data).hexdigest()
        self.part = {'name': 'payload.zip.part0001', 'bytes': len(self.data), 'md5': md5, 'sha256': sha}
        (self.generation / 'payload.zip').write_bytes(self.data)
        (self.generation / 'cloud-parts').mkdir()
        (self.generation / 'cloud-parts' / self.part['name']).write_bytes(self.data)
        (self.generation / 'manifest.json').write_text(json.dumps({'archive_sha256': sha, 'complete': False}))
        (self.generation / 'parts-manifest.json').write_text(json.dumps({'archive_sha256': sha, 'parts': [self.part]}))
        for name in module.METADATA[2:]:
            (self.generation / name).write_text('preserve')
        records = []
        for name in module.METADATA:
            _, checksum, size = module.digest(self.generation / name)
            records.append({'id': name, 'name': name, 'size': str(size), 'md5Checksum': checksum})
        records.append({'id': 'part', 'name': self.part['name'], 'size': str(len(self.data)), 'md5Checksum': md5})
        self.receipt = {'complete': True, 'account': module.ACCOUNT, 'generation': self.generation.name,
                        'root_id': 'root', 'folder_id': 'folder', 'files': records}
        self.save_receipt()
        self.wrong_live = False
        self.bad_download = False
        self.stage_patch = patch.object(module, 'STAGE', self.stage)
        self.stage_patch.start()

    def save_receipt(self):
        (self.generation / 'CLOUD-VERIFIED.json').write_text(json.dumps(self.receipt))

    def tearDown(self):
        self.stage_patch.stop()
        self.temp.cleanup()

    def call(self, *args):
        params = json.loads(args[args.index('--params') + 1])
        if args[:3] == ('drive', 'about', 'get'):
            return {'user': {'emailAddress': module.ACCOUNT}}
        if '--output' in args:
            Path(args[args.index('--output') + 1]).write_bytes(b'wrong' if self.bad_download else self.data)
            return {}
        if args[:3] == ('drive', 'files', 'list'):
            return {'files': [dict(r, parents=['wrong' if self.wrong_live else 'folder'], trashed=False)
                              for r in self.receipt['files']]}
        identity = params['fileId']
        if identity in ['folder', 'root']:
            return {'id': identity, 'name': self.generation.name if identity == 'folder' else 'Replacement Laptop Backups',
                    'parents': ['root'], 'trashed': False, 'mimeType': 'application/vnd.google-apps.folder'}
        record = next(r for r in self.receipt['files'] if r['id'] == identity)
        return dict(record, parents=['wrong' if self.wrong_live else 'folder'], trashed=False)

    def run_offload(self, apply=False):
        return module.offload_generation(self.stage, self.generation, apply, lock_held=True, call=self.call)

    def sample_directory(self, **kwargs):
        directory = self.stage / 'sample-download'
        directory.mkdir()
        return str(directory)

    def test_dry_run_keeps_payload(self):
        self.assertEqual(len(self.run_offload()['payload_files']), 2)
        self.assertTrue((self.generation / 'payload.zip').exists())

    def test_cloud_parent_mismatch_blocks(self):
        self.wrong_live = True
        with self.assertRaises(ValueError): self.run_offload(True)
        self.assertTrue((self.generation / 'payload.zip').exists())

    def test_corrupted_payload_blocks(self):
        (self.generation / 'payload.zip').write_bytes(b'corrupt')
        with self.assertRaises(ValueError): self.run_offload(True)

    def test_missing_receipt_part_blocks(self):
        self.receipt['files'].pop(); self.save_receipt()
        with self.assertRaises(ValueError): self.run_offload(True)

    def test_repeated_apply_is_idempotent(self):
        with patch.object(module.tempfile, 'mkdtemp', side_effect=self.sample_directory):
            self.run_offload(True)
            self.assertEqual(self.run_offload(True)['bytes'], 0)

    def test_invalid_stage_rejected_before_lock_creation(self):
        with self.assertRaises(ValueError):
            module.offload_generation(self.stage / 'wrong', self.generation, call=self.call)
        self.assertFalse((self.stage / 'wrong').exists())

    def test_download_adapter_uses_output_parent_as_cwd(self):
        target = self.stage / 'sample.bin'
        with patch.dict(module.os.environ, {'GWS_EXECUTABLE': 'test-gws'}):
            with patch.object(module.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='binary saved')) as run:
                module.gws('drive', 'files', 'get', '--output', str(target))
                self.assertEqual(run.call_args.kwargs['cwd'], str(self.stage))
                self.assertEqual(run.call_args.args[0][-1], target.name)

    def prepare_snapshots(self):
        root = self.generation / 'sqlite-snapshots' / 'codex'
        root.mkdir(parents=True)
        recorded = root / 'threads.sqlite'; recorded.write_bytes(b'database snapshot')
        unrecorded = root / 'interrupted.sqlite'; unrecorded.write_bytes(b'incomplete')
        manifest = {'archive_sha256': 'bound-test-archive', 'files': {'codex/threads.sqlite': {'generation': self.generation.name,
                    'sha256': hashlib.sha256(recorded.read_bytes()).hexdigest(), 'size': recorded.stat().st_size}}}
        (self.generation / 'manifest.json').write_text(json.dumps(manifest))
        with zipfile.ZipFile(self.generation / 'payload.zip', 'w') as archive:
            archive.writestr('codex/threads.sqlite', recorded.read_bytes())
        return recorded, unrecorded

    def test_snapshot_selection_preserves_unrecorded_and_mismatched(self):
        recorded, unrecorded = self.prepare_snapshots()
        selected, pending = module.snapshot_candidates(self.generation)
        self.assertEqual(selected, [recorded]); self.assertEqual(len(pending), 1)
        self.assertTrue(unrecorded.exists())
        recorded.write_bytes(b'changed')
        selected, pending = module.snapshot_candidates(self.generation)
        self.assertEqual(selected, []); self.assertEqual(len(pending), 2)

    def test_snapshot_archive_member_mismatch_blocks(self):
        self.prepare_snapshots()
        with zipfile.ZipFile(self.generation / 'payload.zip', 'w') as archive:
            archive.writestr('codex/threads.sqlite', b'bad')
        with self.assertRaises(ValueError): module.snapshot_candidates(self.generation)

    def test_snapshot_only_requires_previous_eviction_proof(self):
        recorded, _ = self.prepare_snapshots()
        (self.generation / 'payload.zip').unlink()
        selected, pending = module.snapshot_candidates(self.generation)
        self.assertEqual(selected, []); self.assertEqual(pending[-1]['reason'], 'legacy-proof-not-bound')
        (self.generation / 'OFFLOADED.json').write_text(json.dumps({'status': 'evicted', 'restore_sample': {'verified': True}}))
        self.assertEqual(module.snapshot_candidates(self.generation)[0], [])
        evidence = {'status': 'evicted', 'generation': self.generation.name,
                    'archive_sha256': 'bound-test-archive', 'archive_bytes': len(self.data),
                    'metadata_sha256': {n: module.digest(self.generation / n)[0] for n in module.METADATA},
                    'restore_sample': {'cloud_id': 'part', 'sha256': self.part['sha256'],
                                       'md5': self.part['md5'], 'bytes': len(self.data), 'verified': True}}
        proof = self.generation / 'OFFLOADED.json'
        proof.write_text(json.dumps(evidence))
        self.assertEqual(module.snapshot_candidates(self.generation)[0], [recorded])
        evidence['archive_sha256'] = 'wrong'
        proof.write_text(json.dumps(evidence))
        self.assertEqual(module.snapshot_candidates(self.generation)[0], [])
        evidence['archive_sha256'] = 'bound-test-archive'
        evidence['restore_sample']['cloud_id'] = 'wrong'
        proof.write_text(json.dumps(evidence))
        self.assertEqual(module.snapshot_candidates(self.generation)[0], [])

    def test_bad_restore_sample_blocks(self):
        self.bad_download = True
        with patch.object(module.tempfile, 'mkdtemp', side_effect=self.sample_directory):
            with self.assertRaises(ValueError): self.run_offload(True)
        self.assertTrue((self.generation / 'payload.zip').exists())

    def test_apply_preserves_metadata_snapshots_and_extra_parts(self):
        (self.generation / 'sqlite-snapshot.db').write_text('preserve')
        extra = self.generation / 'cloud-parts' / 'unlisted'; extra.write_text('preserve')
        with patch.object(module.tempfile, 'mkdtemp', side_effect=self.sample_directory):
            self.assertTrue(self.run_offload(True)['evicted'])
        self.assertFalse((self.generation / 'payload.zip').exists())
        for name in module.METADATA + ['CLOUD-VERIFIED.json', 'sqlite-snapshot.db']:
            self.assertTrue((self.generation / name).exists())
        self.assertTrue(extra.exists())


if __name__ == '__main__':
    unittest.main()
