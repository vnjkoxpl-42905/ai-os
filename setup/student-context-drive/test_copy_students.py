import hashlib
from pathlib import Path
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch, Mock
import copy_students as copy

class CopySafetyTests(unittest.TestCase):
    def test_restore_uses_output_directory_as_cwd_for_gws(self):
        from types import SimpleNamespace
        with tempfile.TemporaryDirectory() as tmp, patch.object(copy.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout='',stderr='')) as run:
            destination = Path(tmp)/'restore.bin'
            copy.gws(['files','get'],{'fileId':'sample','alt':'media'},output=destination)
            self.assertEqual(run.call_args.kwargs['cwd'],destination.parent)
            self.assertEqual(run.call_args.args[0][-2:],['--output','restore.bin'])

    def test_finish_rejects_incomplete_manifest_before_download(self):
        with patch.object(copy,'gws') as api:
            with self.assertRaisesRegex(RuntimeError,'Incomplete verified copy'):
                copy.finish([{'path':'sandra/notes.md','size':3,'md5':'abc','sha256':'def'}],{'status':'running','root_id':'root','folders':{'student-context-root-v1':'root'},'files':{}})
            api.assert_not_called()

    def test_missing_or_invalid_status_is_clear_before_provider_call(self):
        with patch.object(copy,'gws') as api:
            for state in [{}, {'status':'unknown'}]:
                with self.assertRaisesRegex(RuntimeError,'valid status'): copy.finish([],state)
            api.assert_not_called()

    def test_missing_or_inconsistent_root_is_clear_before_provider_call(self):
        with patch.object(copy,'gws') as api:
            with self.assertRaisesRegex(RuntimeError,'valid root_id'): copy.finish([],{'status':'complete'})
            with self.assertRaisesRegex(RuntimeError,'does not match'):
                copy.finish([],{'status':'complete','root_id':'other','folders':{'student-context-root-v1':'root'},'files':{}})
            api.assert_not_called()

    def test_shared_restore_sample_is_rejected_before_download(self):
        row = {'path':'sandra/notes.md','size':3,'md5':'abc','sha256':'def'}
        state = {'status':'running','root_id':'root','folders':{'student-context-root-v1':'root'},'files':{row['path']:{**row,'id':'sample','verified':True}}}
        with patch.object(copy,'private',side_effect=[None,RuntimeError('shared sample')]) as privacy, patch.object(copy,'gws') as api:
            with self.assertRaisesRegex(RuntimeError,'shared sample'): copy.finish([row],state)
            self.assertEqual([c.args[0] for c in privacy.call_args_list],['root','sample'])
            api.assert_not_called()

    def test_long_utf8_paths_fit_drive_property_limit_deterministically(self):
        path = 'sandra/' + 'é' * 120
        marker = copy.path_marker(path)
        self.assertLessEqual(len(('lsatuContextPath'+marker).encode()),124)
        self.assertEqual(marker,copy.path_marker(path))
        self.assertNotEqual(marker,copy.path_marker(path+'x'))
        self.assertEqual(copy.path_marker('sandra/notes.md'),'sandra/notes.md')

    def test_atomic_save_retries_windows_reader_lock(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STATE',Path(tmp)/'state.json'), patch.object(copy.os,'replace',side_effect=[PermissionError('reader lock'),None]) as replace, patch.object(copy.time,'sleep'):
            copy.save({'files':{}})
            self.assertEqual(replace.call_count,2)
    def test_remote_content_must_match_both_size_and_hash(self):
        row = {'size':3, 'md5':'abc'}
        self.assertTrue(copy.matching({'size':'3', 'md5Checksum':'abc'}, row))
        self.assertFalse(copy.matching({'size':'4', 'md5Checksum':'abc'}, row))
        self.assertFalse(copy.matching({'size':'3', 'md5Checksum':'other'}, row))
        self.assertFalse(copy.matching({'size':'3', 'md5Checksum':'abc','trashed':True}, row))

    def test_concurrent_progress_writes_keep_valid_complete_manifest(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STATE',Path(tmp)/'state.json'):
            state = {'files':{}}
            def record(index):
                with copy.LOCK:
                    state['files'][str(index)] = index
                    copy.save(state)
            with ThreadPoolExecutor(max_workers=4) as pool: list(pool.map(record,range(40)))
            import json
            self.assertEqual(len(json.loads(copy.STATE.read_text())['files']),40)

    def test_private_folder_rejects_link_or_other_user(self):
        for perm in [{'type':'anyone'}, {'type':'user','emailAddress':'other@example.com'}]:
            with patch.object(copy, 'gws', return_value={'permissions':[perm]}):
                with self.assertRaisesRegex(RuntimeError, 'not restricted'): copy.private('folder')

    def test_existing_managed_folder_reused_without_create(self):
        item = {'id':'stable','mimeType':'application/vnd.google-apps.folder','appProperties':{'lsatuContextPath':'sandra'}}
        state = {'folders':{}}
        with patch.object(copy,'listing',return_value=[item]), patch.object(copy,'private'), patch.object(copy,'save'), patch.object(copy,'gws') as api:
            self.assertEqual(copy.folder('sandra','root','sandra',state), 'stable')
            api.assert_not_called()

    def test_unmanaged_same_name_folder_is_not_adopted(self):
        item = {'id':'foreign','mimeType':'application/vnd.google-apps.folder'}
        with patch.object(copy,'listing',return_value=[item]):
            with self.assertRaisesRegex(RuntimeError,'Unmanaged'): copy.folder('sandra','root','sandra',{'folders':{}})

    def test_inventory_rejects_secret_without_returning_content(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STUDENTS',['sandra']):
            folder = Path(tmp)/'sandra'; folder.mkdir()
            (folder/'notes.md').write_text('-----BEGIN PRIVATE KEY-----')
            with self.assertRaisesRegex(RuntimeError,'Potential credential marker'): copy.inventory(Path(tmp))

    def test_inventory_rejects_env_and_key_files_without_changing_bytes(self):
        for name in ['.env','.env.local','secret.pem','secret.key']:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STUDENTS',['sandra']):
                folder = Path(tmp)/'sandra'; folder.mkdir(); path = folder/name
                path.write_bytes(b'preserve these bytes')
                with self.assertRaisesRegex(RuntimeError,'Potential secret file'): copy.inventory(Path(tmp))
                self.assertEqual(path.read_bytes(),b'preserve these bytes')

    def test_inventory_rejects_extended_credential_shapes(self):
        samples = ['eyJ'+'a'*12+'.eyJabc', 'sk-'+'a'*24, 'AKIA'+'A'*16, '1//'+'a'*32, 'xoxb-'+'a'*20]
        for sample in samples:
            with self.subTest(shape=sample[:4]), tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STUDENTS',['sandra']):
                folder = Path(tmp)/'sandra'; folder.mkdir(); path=folder/'notes.md'; path.write_text(sample)
                with self.assertRaisesRegex(RuntimeError,'Potential credential marker'): copy.inventory(Path(tmp))
                self.assertEqual(path.read_text(),sample)

    def test_inventory_rejects_linked_source_student_and_file(self):
        for kind in ['source','student','file']:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STUDENTS',['sandra']):
                root=Path(tmp); source=root/'students'; source.mkdir(); outside=root/'outside'; outside.mkdir()
                (outside/'notes.md').write_bytes(b'preserve external original')
                try:
                    if kind=='source':
                        source=root/'linked-students'; source.symlink_to(outside,target_is_directory=True)
                    elif kind=='student': (source/'sandra').symlink_to(outside,target_is_directory=True)
                    else:
                        (source/'sandra').mkdir(); (source/'sandra'/'notes.md').symlink_to(outside/'notes.md')
                except OSError as error: self.skipTest('OS does not permit test symlinks: '+str(error))
                with self.assertRaisesRegex(RuntimeError,'Linked source path'): copy.inventory(source)
                self.assertEqual((outside/'notes.md').read_bytes(),b'preserve external original')

    def test_resolved_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'students'; source.mkdir(); outside=root/'outside.md'; outside.write_bytes(b'original')
            with self.assertRaisesRegex(RuntimeError,'escapes'): copy.in_source(outside,source)
            self.assertEqual(outside.read_bytes(),b'original')

    def test_link_detection_guards_all_inventory_levels_without_symlink_privilege(self):
        for kind in ['source','student','file']:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STUDENTS',['sandra']):
                source=Path(tmp); student=source/'sandra'; student.mkdir(); path=student/'notes.md'; path.write_bytes(b'original')
                target={'source':source,'student':student,'file':path}[kind]
                with patch.object(Path,'is_symlink',lambda candidate: candidate==target):
                    with self.assertRaisesRegex(RuntimeError,'Linked source path'): copy.inventory(source)
                self.assertEqual(path.read_bytes(),b'original')

    @unittest.skipUnless(copy.os.name=='nt','Windows junction test')
    def test_real_windows_student_junction_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(copy,'STUDENTS',['sandra']):
            root=Path(tmp); source=root/'students'; source.mkdir(); outside=root/'outside'; outside.mkdir()
            original=outside/'notes.md'; original.write_bytes(b'outside original')
            result=copy.subprocess.run(['cmd','/d','/c','mklink','/J',str(source/'sandra'),str(outside)],capture_output=True,text=True)
            if result.returncode: self.skipTest('Windows junction creation unavailable')
            with self.assertRaisesRegex(RuntimeError,'Linked source path'): copy.inventory(source)
            self.assertEqual(original.read_bytes(),b'outside original')

    def test_windows_cmd_shim_is_rejected(self):
        with patch.object(copy.os,'name','nt'), patch.object(copy.shutil,'which',return_value='C:/tools/gws.cmd'):
            with self.assertRaisesRegex(RuntimeError,'native gws.exe'): copy.gws_executable()

class FileTransferTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.source=Path(self.temp.name); (self.source/'sandra').mkdir()
        self.path=self.source/'sandra'/'notes.md'; self.original=b'Ordinary session notes.'; self.path.write_bytes(self.original)
        with patch.object(copy,'STUDENTS',['sandra']): self.row=copy.inventory(self.source)[0]
        self.state={'folders':{'sandra':'folder'},'files':{}}
        self.remote={'id':'remote','name':'notes.md','size':str(len(self.original)),'md5Checksum':self.row['md5'],'appProperties':{'lsatuContextPath':self.row['path']}}
        self.api=Mock(return_value=self.remote)
        self.save=patch.object(copy,'save'); self.save.start(); self.addCleanup(self.save.stop)

    def tearDown(self): self.assertEqual(self.path.read_bytes(),self.original)

    def transfer(self, children):
        copy.transfer(self.row,self.state,{'sandra':children},self.source,self.api)

    def test_lost_response_resume_adopts_matching_managed_file_without_create(self):
        self.transfer([self.remote]); self.api.assert_not_called()
        self.assertEqual(self.state['files'][self.row['path']]['id'],'remote')

    def test_remote_md5_or_size_conflict_never_creates(self):
        for change in [{'md5Checksum':'different'},{'size':'999'}]:
            with self.subTest(change=change):
                with self.assertRaisesRegex(RuntimeError,'Remote content conflict'): self.transfer([{**self.remote,**change}])
                self.api.assert_not_called(); self.assertEqual(self.state['files'],{})

    def test_cached_id_mismatch_or_missing_remote_never_creates(self):
        self.state['files'][self.row['path']]={'id':'cached'}
        for children in [[self.remote],[]]:
            with self.assertRaisesRegex(RuntimeError,'moved or renamed'): self.transfer(children)
        self.api.assert_not_called()

    def test_unmanaged_same_name_file_is_not_adopted(self):
        with self.assertRaisesRegex(RuntimeError,'Unmanaged file'): self.transfer([{**self.remote,'appProperties':{}}])
        self.api.assert_not_called()

    def test_duplicate_names_never_create(self):
        with self.assertRaisesRegex(RuntimeError,'Ambiguous'): self.transfer([self.remote,self.remote.copy()])
        self.api.assert_not_called()

    def test_upload_then_second_run_makes_zero_creates_and_preserves_source(self):
        self.transfer([]); self.assertEqual(self.api.call_count,1)
        self.assertEqual(self.api.call_args.args[0],['files','create'])
        self.assertEqual(self.api.call_args.kwargs['upload'],self.path)
        self.api.reset_mock(); self.transfer([self.remote]); self.api.assert_not_called()

    def test_bad_upload_checksum_does_not_mark_verified_or_touch_original(self):
        self.api.return_value={**self.remote,'md5Checksum':'incorrect'}
        with self.assertRaisesRegex(RuntimeError,'Upload verification failed'): self.transfer([])
        self.assertEqual(self.state['files'],{})

if __name__ == '__main__': unittest.main()
