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
        path.write_text("import sys,json\nif sys.argv[-2:]==['features','list']:\n print('\\n'.join(n+' stable false' for n in ('apps', 'computer_use', 'browser_use', 'browser_use_external', 'browser_use_full_cdp_access', 'in_app_browser', 'plugins', 'remote_plugin', 'code_mode_host')))\n sys.exit(0)\nif sys.argv[-3:]==['mcp','list','--json']:\n print(" + repr(inventory) + ")\n sys.exit(" + str(exit_code) + ")\nprint(json.dumps(sys.argv[1:]))\n", encoding="utf-8")
        return [sys.executable, str(path)]

    def test_all_servers_disabled_for_fresh_and_resumed_reviews(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prefix = self.fake(root, json.dumps([{ "name": "cua_repl", "enabled": True, "secret": "do-not-log" }, { "name": "lsat-u-lessons", "enabled": True }, { "name": "already-disabled", "enabled": False }, { "name": "node_repl", "enabled": True }]))
            names = runner.codex_review_mcp_servers(prefix, root)
            self.assertEqual(names, ["already-disabled", "cua_repl", "lsat-u-lessons", "node_repl"])
            for session in (None, "prior-session"):
                argv = runner.command("codex", "review", root, session=session, mcp_overrides=sum((["-c", f'mcp_servers.{n}={{enabled=false,command="review-disabled"}}'] for n in names), []))
                actual = subprocess.run(prefix + argv, input="review", text=True, capture_output=True, check=True)
                recorded = json.loads(actual.stdout)
                for name in names:
                    self.assertIn(f'mcp_servers.{name}={{enabled=false,command="review-disabled"}}', recorded)
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

    def test_verification_rejects_enabled_or_changed_inventory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for rows in ([{"name": "enabled", "enabled": True}], [{"name": "disabled"}]):
                prefix = self.fake(root, json.dumps(rows))
                with self.assertRaises(runner.RunError):
                    runner.codex_review_mcp_overrides(prefix, root)
            path = root / "changing.py"
            path.write_text('import sys,json\nif sys.argv[-2:]==["features","list"]:\n print("\\n".join(n+" stable false" for n in '+repr(runner.REVIEW_DISABLED_FEATURES)+'))\n sys.exit(0)\nprint(json.dumps([{ "name": "new", "enabled": False }] if "-c" in sys.argv else [{ "name": "old", "enabled": True }]))\n', encoding="utf-8")
            with self.assertRaises(runner.RunError):
                runner.codex_review_mcp_overrides([sys.executable, str(path)], root)

    def test_verified_overrides_are_exact_execution_overrides(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "verified.py"
            path.write_text('import sys,json\nif sys.argv[-2:]==["features","list"]:\n print("\\n".join(n+" stable false" for n in '+repr(runner.REVIEW_DISABLED_FEATURES)+'))\n sys.exit(0)\nif sys.argv[-3:]==["mcp","list","--json"]:\n print(json.dumps([{ "name": "cua_repl", "enabled": "-c" not in sys.argv }]))\nelse: print(json.dumps(sys.argv[1:]))\n', encoding="utf-8")
            prefix = [sys.executable, str(path)]
            names, overrides = runner.codex_review_mcp_overrides(prefix, root)
            self.assertEqual(names, ["cua_repl"])
            argv = runner.command("codex", "inspect", root, mcp_overrides=overrides)
            self.assertIn('mcp_servers.cua_repl={enabled=false,command="review-disabled"}', argv)

    def test_enabled_or_unrecognized_feature_inventory_blocks_review(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "unsafe_features.py"
            for output in ("apps stable true", "private-secret malformed", ""):
                path.write_text("print(" + repr(output) + ")", encoding="utf-8")
                with self.assertRaises(runner.RunError) as caught:
                    runner.codex_review_features([sys.executable, str(path)], root, [])
                self.assertNotIn("private-secret", str(caught.exception))

    def test_missing_discovery_cannot_construct_codex_review(self):
        with self.assertRaises(runner.RunError):
            runner.command("codex", "inspect", Path("."))

    def test_empty_inventory_allowed_and_build_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(runner.codex_review_mcp_servers(self.fake(root, "[]"), root), [])
            self.assertIn("read-only", runner.command("codex", "inspect", root, mcp_overrides=[]))
            build = runner.command("codex", "build", root)
            self.assertIn("workspace-write", build)
            self.assertFalse(any("mcp_servers" in flag for flag in build))

if __name__ == "__main__":
    unittest.main()
