"""Isolated watch tests: no network, real modified Python control flow."""
import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path.home()/'.agents/skills/watch/scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('watch_fixture', SCRIPTS/'watch.py')
watch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(watch)
import frames
import whisper

class WatchBoundaries(unittest.TestCase):
    def test_no_implicit_upload_even_with_configured_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)/'fresh'
            with patch.object(sys, 'argv', ['watch', 'fixture.mp4', '--out-dir', str(work)]), \
                 patch.object(watch, 'download', return_value={'video_path':'fixture.mp4'}), \
                 patch.object(watch, 'get_metadata', return_value={'duration_seconds':10}), \
                 patch.object(watch, 'extract', return_value=[]), \
                 patch.object(watch, 'load_api_key', return_value=('groq','test-only')) as key, \
                 patch.object(watch, 'transcribe_video') as upload, \
                 contextlib.redirect_stdout(io.StringIO()) as output, contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(watch.main(), 0)
                key.assert_not_called()
                upload.assert_not_called()
                self.assertIn('No transcript available', output.getvalue())
                self.assertNotIn('delete when done', output.getvalue())

    def test_explicit_provider_keeps_optional_capability(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)/'fresh'
            with patch.object(sys, 'argv', ['watch', 'fixture.mp4', '--out-dir', str(work), '--whisper','openai']), \
                 patch.object(watch, 'download', return_value={'video_path':'fixture.mp4'}), \
                 patch.object(watch, 'get_metadata', return_value={'duration_seconds':10}), \
                 patch.object(watch, 'extract', return_value=[]), \
                 patch.object(watch, 'load_api_key', return_value=('openai','test-only')) as key, \
                 patch.object(watch, 'transcribe_video', return_value=([{'start':0,'end':1,'text':'test'}], 'openai')) as upload, \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(watch.main(), 0)
                key.assert_called_once_with('openai')
                upload.assert_called_once()

    def test_nonempty_work_directory_preserved_before_download(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp)/'keep.md'
            original.write_text('existing evidence')
            with patch.object(sys, 'argv', ['watch','fixture.mp4','--out-dir',tmp]), patch.object(watch,'download') as download:
                with self.assertRaisesRegex(SystemExit, 'not empty'):
                    watch.main()
                download.assert_not_called()
            self.assertEqual(original.read_text(), 'existing evidence')

    def test_frames_preserve_previous_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp)/'frame_0001.jpg'
            original.write_bytes(b'old frame')
            with patch.object(frames.shutil,'which',return_value='ffmpeg'), patch.object(frames.subprocess,'run') as run:
                with self.assertRaisesRegex(SystemExit,'not empty'):
                    frames.extract('fixture.mp4',Path(tmp),1)
                run.assert_not_called()
            self.assertEqual(original.read_bytes(), b'old frame')
            # The old unlink loop would have removed the fixture before running ffmpeg.
            self.assertEqual(len(list(Path(tmp).glob('frame_*.jpg'))),1)

    def test_new_frames_use_no_overwrite_flag(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(frames.shutil,'which',return_value='ffmpeg'), patch.object(frames.subprocess,'run') as run:
                run.return_value.returncode=0
                frames.extract('fixture.mp4',Path(tmp)/'frames',1)
                args = run.call_args.args[0]
                self.assertIn('-n',args)
                self.assertNotIn('-y',args)

    def test_no_legacy_secret_store(self):
        self.assertNotIn('Path.home() / ".config"', (SCRIPTS/'whisper.py').read_text())
        with patch.dict(whisper.os.environ, {'OPENAI_API_KEY':'fake-test-key'}, clear=True):
            self.assertEqual(whisper.load_api_key('openai'), ('openai','fake-test-key'))

    def test_provider_required_before_audio_or_key_detection(self):
        with patch.object(whisper,'load_api_key') as key, patch.object(whisper,'extract_audio') as audio:
            with self.assertRaisesRegex(SystemExit,'Select groq or openai explicitly'):
                whisper.transcribe_video('fixture.mp4',Path('fixture.mp3'))
            key.assert_not_called()
            audio.assert_not_called()

    def test_existing_audio_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            audio=Path(tmp)/'audio.mp3'
            audio.write_bytes(b'original audio')
            with patch.object(whisper.shutil,'which',return_value='ffmpeg'), patch.object(whisper.subprocess,'run') as run:
                with self.assertRaisesRegex(SystemExit,'already exists'):
                    whisper.extract_audio('fixture.mp4',audio)
                run.assert_not_called()
            self.assertEqual(audio.read_bytes(),b'original audio')

    def test_missing_provider_key_has_no_legacy_wizard_instruction(self):
        with patch.object(whisper,'load_api_key',return_value=(None,None)):
            with self.assertRaises(SystemExit) as error:
                whisper.transcribe_video('fixture.mp4',Path('fixture.mp3'),backend='openai')
            self.assertNotIn('setup.py',str(error.exception))
            self.assertNotIn('~/.config',str(error.exception))

if __name__ == '__main__':
    unittest.main()
