"""Regression checks for evidence-backed link resolution, without touching vault pages."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("wiki_maintenance", Path(__file__).with_name("wiki-maintenance.py"))
wiki = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wiki)


class EvidenceResolutionTests(unittest.TestCase):
    def test_recovered_target_requires_source_target_and_matching_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "wiki/log.md"
            recovered = root / "research/evidence.md"
            recovered.parent.mkdir()
            recovered.write_bytes(b"dated original")
            manifest = root / "links.json"
            manifest.write_text(json.dumps([{
                "page": "wiki/log.md", "target": "../../retired/evidence.md",
                "recovered": "research/evidence.md",
                "sha256": hashlib.sha256(recovered.read_bytes()).hexdigest(),
            }]), encoding="utf8")
            with patch.object(wiki, "ROOT", root), patch.object(wiki, "RECOVERED", manifest):
                self.assertEqual(wiki.resolve(source, "../../retired/evidence.md", {}), (True, recovered.resolve()))
                self.assertEqual(wiki.resolve(source, "../../other/evidence.md", {}), (False, None))
                recovered.write_bytes(b"changed")
                self.assertEqual(wiki.resolve(source, "../../retired/evidence.md", {}), (False, None))

    def test_native_memory_requires_actual_matching_project_file(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            root = home / "vault"
            project_key = str(root.resolve()).replace(":", "-").replace("\\", "-").replace("/", "-")
            memory = home / ".claude/projects" / project_key / "memory/fact.md"
            memory.parent.mkdir(parents=True)
            memory.write_text("actual memory", encoding="utf8")
            with patch.object(wiki, "ROOT", root), patch.object(wiki, "RECOVERED", home / "missing.json"), patch.object(Path, "home", return_value=home):
                self.assertEqual(wiki.resolve(root / "wiki/log.md", "fact", {}), (True, memory.resolve()))
                self.assertEqual(wiki.resolve(root / "wiki/log.md", "absent", {}), (False, None))

    def test_inline_examples_are_not_links_but_real_missing_link_survives(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "wiki/log.md"
            page.parent.mkdir()
            page.write_text("`[[Example/X]]` and `[[X]]`\n[[missing]]\n", encoding="utf8")
            with patch.object(wiki, "ROOT", root), patch.object(wiki, "RECOVERED", root / "missing.json"):
                wiki.lint([page])
            report = (root / "system/generated/wiki-lint.generated.tsv").read_text(encoding="utf8")
            self.assertIn("\tmissing\n", report)
            self.assertNotIn("Example", report)
            self.assertNotIn("\tX\n", report)

    def test_top_level_system_record_is_a_real_basename_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "wiki/log.md"
            page.parent.mkdir()
            page.write_text("[[windows-machine-profile]]", encoding="utf8")
            profile = root / "system/windows-machine-profile.md"
            profile.parent.mkdir()
            profile.write_text("existing profile", encoding="utf8")
            with patch.object(wiki, "ROOT", root), patch.object(wiki, "RECOVERED", root / "missing.json"):
                wiki.lint([page])
            self.assertEqual((root / "system/generated/wiki-lint.generated.tsv").read_text(encoding="utf8"), "kind\tpage\tdetail\n")


if __name__ == "__main__":
    unittest.main()
