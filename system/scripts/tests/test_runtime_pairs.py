"""Host-specific skill pairing regressions; no real catalog mutations."""
import importlib.util
from pathlib import Path
import sys
import tomllib
import unittest
from unittest.mock import patch
import tempfile

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("runtime_pair_validation", SCRIPTS / "check-skills.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class RuntimePairChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = tomllib.loads((Path(validation.DB) / "runtime-pairs.toml").read_text(encoding="utf-8"))
        cls.groups = [
            ("claude", "codex", config["pairs"]),
            ("codex", "gemini", config["codex_gemini_pairs"]),
        ]
        cls.catalogs = {runtime: validation.db_names(runtime)
                        for runtime in ("claude", "codex", "gemini")}
        cls.active = {
            runtime: {p.name for root in roots if Path(root).is_dir()
                      for p in Path(root).iterdir() if (p / "SKILL.md").is_file()}
            for runtime, roots in validation.RUNTIME_ACTIVE_ROOTS.items()
        }

    def test_real_configuration_uses_correct_hosts(self):
        self.assertEqual(self.groups[1][2]["gemini-review"], "codex-review")
        self.assertNotIn("gemini-review", self.groups[0][2])
        self.assertEqual(validation.runtime_pair_errors(self.groups, self.catalogs), [])
        self.assertEqual(validation.runtime_pair_errors(self.groups, self.active, activation=True), [])

    def test_missing_gemini_catalog_is_rejected(self):
        missing = {runtime: set(names) for runtime, names in self.catalogs.items()}
        missing["gemini"].remove("codex-review")
        errors = validation.runtime_pair_errors(self.groups, missing)
        self.assertEqual(len(errors), 1)
        self.assertIn("codex/gemini-review -> gemini/codex-review", errors[0])

    def test_missing_gemini_activation_is_rejected(self):
        missing = {runtime: set(names) for runtime, names in self.active.items()}
        missing["gemini"].remove("codex-review")
        errors = validation.runtime_pair_errors(self.groups, missing, activation=True)
        self.assertEqual(len(errors), 1)
        self.assertIn("codex gemini-review / gemini codex-review", errors[0])

    def test_missing_codex_catalog_keeps_existing_pair_check(self):
        missing = {runtime: set(names) for runtime, names in self.catalogs.items()}
        missing["codex"].remove("claude-review")
        errors = validation.runtime_pair_errors(self.groups, missing)
        self.assertEqual(len(errors), 1)
        self.assertIn("claude/codex-review -> codex/claude-review", errors[0])

    def test_same_names_on_wrong_hosts_do_not_satisfy_pair(self):
        wrong = {"claude": {"gemini-review"}, "codex": {"codex-review"}, "gemini": set()}
        groups = [("codex", "gemini", {"gemini-review": "codex-review"})]
        self.assertEqual(len(validation.runtime_pair_errors(groups, wrong)), 1)

    def test_instruction_walk_skips_junctions_but_keeps_regular_scopes(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root)
            (root / "ordinary").mkdir()
            (root / "junction").mkdir()
            (root / "node_modules").mkdir()
            is_junction = lambda path: Path(path).name == "junction"
            with patch.object(validation.os.path, "isjunction", is_junction, create=True):
                visited = {Path(current).name for current, _ in validation.instruction_scopes(root)}
            self.assertIn("ordinary", visited)
            self.assertNotIn("junction", visited)
            self.assertNotIn("node_modules", visited)


if __name__ == "__main__":
    unittest.main()
