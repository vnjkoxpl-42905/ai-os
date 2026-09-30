"""Regression checks for accepting relocation without hiding content drift."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("skill_validation", SCRIPTS / "check-skills.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class RelocationChecks(unittest.TestCase):
    def test_valid_relocation_and_changed_instructions(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "active").mkdir()
            (root / "catalog").mkdir()
            (root / "helper.md").write_text("helper", encoding="utf-8")
            active, catalog = root / "active/SKILL.md", root / "catalog/SKILL.md"
            active.write_text("Read [helper](../helper.md).", encoding="utf-8")
            catalog.write_text("Read [helper](../active/../helper.md).", encoding="utf-8")
            self.assertTrue(validation.entrypoints_match(active, catalog))
            catalog.write_text("Delete [helper](../helper.md).", encoding="utf-8")
            self.assertFalse(validation.entrypoints_match(active, catalog))

    def test_missing_destination_is_not_accepted_as_relocation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            a, b = root / "a.md", root / "b.md"
            a.write_text("[helper](missing.md)", encoding="utf-8")
            b.write_text("[helper](./missing.md)", encoding="utf-8")
            self.assertFalse(validation.entrypoints_match(a, b))

    def test_distinct_resources_and_remote_urls_are_not_equivalent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("first.md", "second.md"):
                (root / name).write_text("same content", encoding="utf-8")
            a, b = root / "a.md", root / "b.md"
            a.write_text("[helper](first.md)", encoding="utf-8")
            b.write_text("[helper](second.md)", encoding="utf-8")
            self.assertFalse(validation.entrypoints_match(a, b))
            a.write_text("[helper](https://example.com/a)", encoding="utf-8")
            b.write_text("[helper](https://example.com/b)", encoding="utf-8")
            self.assertFalse(validation.entrypoints_match(a, b))


if __name__ == "__main__":
    unittest.main()
