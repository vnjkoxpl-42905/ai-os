import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('session_builder', Path(__file__).with_name('build_session_manual.py'))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class StudentCopyRules(unittest.TestCase):
    def lint(self, page):
        with contextlib.redirect_stdout(io.StringIO()):
            builder.lint('fixture.html', page)

    def test_each_scoped_rejected_phrase_is_caught(self):
        for phrase in builder.COPY_EXCLUSIONS:
            with self.subTest(phrase=phrase), self.assertRaises(ValueError):
                self.lint('<p>' + phrase.upper() + '</p>')

    def test_title_labels_and_hidden_answers_are_checked(self):
        for page in ('<title>Topic · Manual</title>', '<details><summary>Check</summary><p>Candidate assumption</p></details>', '<button aria-label="Recognition drill">Open</button>', '<div hidden>Grammatical shape</div>'):
            with self.subTest(page=page), self.assertRaises(ValueError):
                self.lint(page)

    def test_phrases_allow_inline_markup_and_whitespace(self):
        with self.assertRaises(ValueError):
            self.lint('<p>Two <strong>complete</strong>\n conditions</p>')

    def test_ordinary_copy_and_private_evidence_remain_valid(self):
        self.lint('<title>Find the conclusion · Reference</title><p>Explain the rule. Test an answer you are considering. A manualist is a different word.</p><!-- PRIVATE HISTORY: candidate assumption; manual --><style>.manual {color:red}</style><script>const example="recognition drill";</script>')

    def test_browser_title_derives_from_note_role(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'note.md'
            path.write_text('# Find the conclusion\n\nRead the argument.\n', encoding='utf-8')
            for kicker, suffix in [('Before you start · Practice', 'Before you start'), ('Reference · Keep it open', 'Reference'), ('Session recap', 'Session recap'), ('Other note', 'Session notes')]:
                with self.subTest(kicker=kicker):
                    page = builder.from_md(str(path), kicker, 'fixture-note')
                    self.assertIn('<title>Find the conclusion · ' + suffix + '</title>', page)
                    self.lint(page)

    def test_previous_warning_only_exclusions_now_stop_build(self):
        for phrase in ('—', '–', '~', 'concept lesson', 'establish'):
            with self.subTest(phrase=phrase), self.assertRaises(ValueError):
                self.lint('<p>Read ' + phrase + ' this.</p>')

    def test_recap_does_not_silently_rewrite_rejected_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'recap.src.html'
            source.write_text('<title>Session Manual</title><style>/*CSS*/</style><p>Read the argument.</p>', encoding='utf-8')
            page = builder.recap(directory)
            self.assertIn('<title>Session Manual</title>', page)
            with self.assertRaises(ValueError):
                self.lint(page)


if __name__ == '__main__':
    unittest.main()
