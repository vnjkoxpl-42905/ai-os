"""Read-only worker helpers tested without processes, Drive or real backups."""
import unittest
import json
from pathlib import Path
import tempfile
from unittest.mock import patch
import new_machine_approved_cleanup_worker as worker


class WorkerTests(unittest.TestCase):
    def uploader(self, pid, generation, created='one'):
        return {'pid': pid, 'name': 'python.exe', 'command': 'python new-machine-cloud.py --generation ' + generation, 'created': created}

    def test_absent_original_uploaders_do_not_wait_on_future_pid_reuse(self):
        bound = worker.bind_processes({})
        later = {14252: self.uploader(14252, worker.CORE)}
        self.assertEqual(worker.still_running(bound, later), [])

    def test_pid_reuse_is_not_original_process(self):
        original = {14252: self.uploader(14252, worker.CORE)}
        bound = worker.bind_processes(original)
        self.assertEqual(worker.still_running(bound, original), [14252])
        self.assertEqual(worker.still_running(bound, {14252: self.uploader(14252, worker.CORE, 'new')}), [])

    def test_unexpected_initial_pid_identity_refused(self):
        wrong = self.uploader(14252, 'different-generation')
        with self.assertRaises(ValueError):
            worker.bind_processes({14252: wrong})

    def test_bound_command_identity_change_refused(self):
        original = {14252: self.uploader(14252, worker.CORE)}
        bound = worker.bind_processes(original)
        original[14252]['command'] = 'python other-script.py'
        with self.assertRaises(ValueError):
            worker.still_running(bound, original)

    def test_retry_requires_safe_structured_retryable_marker(self):
        self.assertTrue(worker.transient_log_failure('Drive failed {"retryable": true}'))
        self.assertFalse(worker.transient_log_failure('Drive failed {"retryable": false}'))
        self.assertFalse(worker.transient_log_failure('unknown error'))

    def test_import_does_not_launch_work(self):
        with patch.object(worker.subprocess, 'run') as run:
            self.assertEqual(len(worker.EXPECTED_PROCESSES), 2)
            run.assert_not_called()

    def test_download_sample_requires_full_current_metadata_binding(self):
        from new_machine_offload import METADATA
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / worker.CORE
            directory.mkdir()
            part = {'name': 'payload.zip.part0001', 'sha256': 'a' * 64, 'md5': 'b' * 32, 'bytes': 22}
            (directory / 'manifest.json').write_text(json.dumps({'archive_sha256': 'c' * 64}))
            (directory / 'parts-manifest.json').write_text(json.dumps({'parts': [part]}))
            (directory / 'CLOUD-VERIFIED.json').write_text(json.dumps({'files': [{'name': part['name'], 'id': 'cloud-id'}]}))
            for name in METADATA:
                if not (directory / name).exists():
                    (directory / name).write_text('fixture')
            sample = {'cloud_id': 'cloud-id', 'sha256': part['sha256'], 'md5': part['md5'], 'bytes': 22, 'verified': True}
            evidence = {'status': 'evicted', 'generation': directory.name, 'archive_sha256': 'c' * 64,
                        'archive_bytes': 22, 'metadata_sha256': {name: worker.discard.file_sha256(directory / name) for name in METADATA},
                        'restore_sample': sample}
            path = directory / 'OFFLOADED.json'
            path.write_text(json.dumps(evidence))
            self.assertEqual(worker.require_bound_restore_sample(directory), sample)
            evidence['restore_sample']['cloud_id'] = 'different'
            path.write_text(json.dumps(evidence))
            with self.assertRaises(ValueError):
                worker.require_bound_restore_sample(directory)
            evidence['restore_sample'] = sample.copy()
            evidence['metadata_sha256'] = {}
            path.write_text(json.dumps(evidence))
            with self.assertRaises(ValueError):
                worker.require_bound_restore_sample(directory)


if __name__ == '__main__':
    unittest.main()
