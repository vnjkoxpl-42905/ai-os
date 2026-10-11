"""Isolated regressions for Gemini coverage and bounded provider sanity."""
import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'system/scripts'))
spec = importlib.util.spec_from_file_location('skill_checks', ROOT / 'system/scripts/check-skills.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class ValidatorTests(unittest.TestCase):
    def test_generator_includes_gemini_and_preserves_concurrent_index_edit(self):
        spec = importlib.util.spec_from_file_location('skill_index', ROOT / 'system/scripts/gen-skill-index.py')
        generator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(generator)
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'skills'
            for runtime in ('claude', 'codex', 'gemini'):
                p = db / runtime / 'gws-fixture' / 'SKILL.md'
                p.parent.mkdir(parents=True)
                p.write_text('---\nname: gws-fixture\ndescription: Fixture operation\n---\n', encoding='utf-8')
            output = db / 'INDEX.md'
            output.write_text('original', encoding='utf-8')
            with patch.object(generator, 'DB', str(db)), contextlib.redirect_stdout(io.StringIO()):
                generator.main()
                text = output.read_text(encoding='utf-8')
                self.assertIn('## gemini/', text)
                self.assertIn('`.gemini/skills/`', text)
                fixture = db / 'gemini/gws-fixture/SKILL.md'
                fixture.write_text(fixture.read_text(encoding='utf-8').replace('Fixture operation', 'Updated operation'), encoding='utf-8')
                original_scan = generator.scan
                def concurrent_scan(runtime):
                    result = original_scan(runtime)
                    if runtime == 'claude':
                        output.write_text('concurrent update', encoding='utf-8')
                    return result
                with patch.object(generator, 'scan', side_effect=concurrent_scan), self.assertRaises(RuntimeError):
                    generator.main()
                self.assertEqual(output.read_text(encoding='utf-8'), 'concurrent update')

    def test_matching_relocated_support_link_and_real_content_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, active = root / 'source', root / 'active'
            source.mkdir()
            active.mkdir()
            target = source / 'ref.md'
            target.write_text('reference', encoding='utf-8')
            a, b = source / 'SKILL.md', active / 'SKILL.md'
            a.write_text('Read [ref](ref.md).', encoding='utf-8')
            b.write_text('Read [ref](../source/ref.md).', encoding='utf-8')
            self.assertTrue(checks.entrypoints_match(a, b))
            b.write_text('Replace [ref](../source/ref.md).', encoding='utf-8')
            self.assertFalse(checks.entrypoints_match(a, b))

    def test_corrupted_provider_reference_is_rejected_and_correct_identity_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            api = root / 'claude-api' / 'SKILL.md'
            academy = root / 'academy-guide' / 'SKILL.md'
            api.parent.mkdir()
            academy.parent.mkdir()
            api.write_text('---\nname: Codex-api\n---\nCodex API / Anthropic SDK', encoding='utf-8')
            academy.write_text('https://academy.Codex.com', encoding='utf-8')
            self.assertEqual(len(checks.owned_provider_errors([root])), 3)
            api.write_text('---\nname: claude-api\n---\nAnthropic SDK for Claude', encoding='utf-8')
            academy.write_text('https://anthropic.skilljar.com', encoding='utf-8')
            self.assertEqual(checks.owned_provider_errors([root]), [])

    def test_gemini_activation_drift_fails_then_matching_copy_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = '---\nname: fixture\ndescription: A fixture\n---\nRead source.\n'
            for runtime in ('claude', 'codex', 'gemini'):
                p = root / 'skills' / runtime / 'fixture' / 'SKILL.md'
                p.parent.mkdir(parents=True)
                p.write_text(skill, encoding='utf-8')
            (root / 'skills/INDEX.md').write_text('- **fixture** description', encoding='utf-8')
            (root / 'skills/PARITY.md').write_text('No asymmetric skills.', encoding='utf-8')
            for manual in ('AGENTS.md', 'CLAUDE.md'):
                (root / manual).write_text('Fixture instructions.', encoding='utf-8')
            active = root / '.gemini/skills/fixture/SKILL.md'
            active.parent.mkdir(parents=True)
            active.write_text(skill.replace('Read source.', 'Wrong source.'), encoding='utf-8')
            with patch.multiple(checks, BRAIN=str(root), DB=str(root / 'skills'), HOME=str(root / 'home'),
                                PROJECT_ACTIVE_ROOTS=[str(root / '.gemini/skills')],
                                RUNTIME_ACTIVE_ROOTS={'claude': [], 'codex': []}), \
                    patch.object(checks.subprocess, 'run', return_value=type('R', (), {'stdout': ''})()):
                out = io.StringIO()
                with contextlib.redirect_stderr(out), self.assertRaises(SystemExit):
                    checks.main()
                self.assertIn('stale activation copy', out.getvalue())
                active.write_text(skill, encoding='utf-8')
                with contextlib.redirect_stdout(io.StringIO()):
                    checks.main()


if __name__ == '__main__':
    unittest.main(verbosity=2)
