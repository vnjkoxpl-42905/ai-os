import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("loop_runner", Path(__file__).with_name("runner.py"))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class ReviewMcpBoundary(unittest.TestCase):
    def fake(self, root, inventory, exit_code=0):
        path = root / "fake_cli.py"
        path.write_text("import sys,json\nif sys.argv[1:]==['mcp','list','--json']:\n print(" + repr(inventory) + ")\n sys.exit(" + str(exit_code) + ")\nprint(json.dumps(sys.argv[1:]))\n", encoding="utf-8")
        return [sys.executable, str(path)]

    def test_all_servers_disabled_for_fresh_and_resumed_reviews(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prefix = self.fake(root, json.dumps([{ "name": "cua_repl", "enabled": True, "secret": "do-not-log" }, { "name": "lsat-u-lessons", "enabled": True }, { "name": "already-disabled", "enabled": False }, { "name": "odd.name", "enabled": True }]))
            names = runner.codex_review_mcp_servers(prefix, root)
            self.assertEqual(names, ["already-disabled", "cua_repl", "lsat-u-lessons", "odd.name"])
            for session in (None, "prior-session"):
                argv = runner.command("codex", "review", root, session=session, mcp_servers=names)
                actual = subprocess.run(prefix + argv, input="review", text=True, capture_output=True, check=True)
                recorded = json.loads(actual.stdout)
                for name in names:
                    self.assertIn(f'mcp_servers.{json.dumps(name)}.enabled=false', recorded)
                self.assertNotIn("do-not-log", json.dumps(recorded))

    def test_discovery_failures_do_not_expose_private_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for output, code in [("PRIVATE-SECRET", 1), ("PRIVATE-SECRET", 0), ("{}", 0), ('[{"name":"x"},{"name":"x"}]', 0), ('[{"name":""}]', 0), ('[{}]', 0)]:
                prefix = self.fake(root, output, code)
                with self.assertRaises(runner.RunError) as caught:
                    runner.codex_review_mcp_servers(prefix, root)
                self.assertNotIn("PRIVATE-SECRET", str(caught.exception))
                self.assertIn("review was not launched", str(caught.exception))

    def test_missing_discovery_cannot_construct_codex_review(self):
        with self.assertRaises(runner.RunError):
            runner.command("codex", "inspect", Path("."))

    def test_empty_inventory_allowed_and_build_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(runner.codex_review_mcp_servers(self.fake(root, "[]"), root), [])
            self.assertIn("read-only", runner.command("codex", "inspect", root, mcp_servers=[]))
            build = runner.command("codex", "build", root)
            self.assertIn("workspace-write", build)
            self.assertFalse(any("mcp_servers" in flag for flag in build))

if __name__ == "__main__":
    unittest.main()
