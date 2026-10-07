import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("chat_export", Path(__file__).resolve().parents[1] / "system/scripts/github-sync/chat_export.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ConversationExportTests(unittest.TestCase):
    def test_redaction(self):
        text = 'api_key="sensitive" password=hello https://example.com/?token=xyz Bearer abc.def sk-abcdefghijklmnop'
        clean = module.redact(text)
        for secret in ("sensitive", "hello", "xyz", "abc.def", "sk-abcdefghijklmnop"):
            self.assertNotIn(secret, clean)
        self.assertFalse(module.secret_checks(clean))

    def test_nested_serialized_credentials_converge(self):
        samples = [r'{"password": "api_key=hidden"}', 'authorization=Bearer hidden', 'password="token=hidden"', 'key=https://example.com/?token=password=hidden']
        for sample in samples:
            clean = module.redact(sample)
            self.assertEqual(clean, module.redact(clean))
            self.assertNotIn("hidden", clean)

    def test_export_filter_preserve_corrupt_and_remove_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            project = home / "project"
            source = home / ".claude/projects/p"
            source.mkdir(parents=True)
            session = source / "one.jsonl"
            rows = [{"type": "user", "cwd": str(project), "sessionId": "one", "message": {"role": "user", "content": "Do work"}}, {"type": "assistant", "message": {"content": [{"type": "thinking", "thinking": "private reasoning"}, {"type": "text", "text": "Done password=secret"}]}}]
            session.write_text("\n".join(json.dumps(row) for row in rows))
            unrelated = source / "other.jsonl"
            unrelated.write_text(json.dumps({"type": "user", "cwd": str(home / "elsewhere"), "message": {"content": "Unrelated"}}))
            dest = home / "exports"
            with patch.object(Path, "home", return_value=home):
                result = module.export_conversations(dest, [project])
                self.assertEqual(len(result["sessions"]), 1)
                output = dest / "claude/one.md"
                self.assertNotIn("private reasoning", output.read_text())
                self.assertNotIn("secret", output.read_text())
                stamp = output.stat().st_mtime_ns
                # Unrelated records can be parsed; the cached project source cannot.
                real_parse = module._parse
                def cached_parse(path, platform, roots):
                    if path == session:
                        raise AssertionError("cached session was parsed again")
                    return real_parse(path, platform, roots)
                with patch.object(module, "_parse", side_effect=cached_parse):
                    module.export_conversations(dest, [project])
                self.assertEqual(stamp, output.stat().st_mtime_ns)
                session.write_text("{broken")
                self.assertTrue(module.export_conversations(dest, [project])["errors"])
                self.assertTrue(output.exists())
                session.unlink()
                module.export_conversations(dest, [project])
                self.assertFalse(output.exists())

    def test_codex_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            source = home / ".codex/sessions"
            source.mkdir(parents=True)
            rows = [{"type": "session_meta", "payload": {"id": "thread-1", "cwd": str(home / "project")}}, {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "Request"}]}}, {"type": "response_item", "payload": {"type": "function_call_output", "output": "password=abc"}}, {"type": "compacted", "payload": {"message": "Resume here"}}]
            (source / "session.jsonl").write_text("\n".join(json.dumps(row) for row in rows))
            with patch.object(Path, "home", return_value=home):
                module.export_conversations(home / "exports", [home / "project"])
            text = next((home / "exports/codex").glob("thread-1-*.md")).read_text()
            self.assertIn("Resume here", text)
            self.assertNotIn("abc", text)

    def test_subagent_collision_and_analysis(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            main = root / "main.jsonl"
            child = root / "subagents/agent-one.jsonl"
            child.parent.mkdir()
            record = {"type": "user", "sessionId": "same", "cwd": str(root), "message": {"content": "hello"}}
            main.write_text(json.dumps(record))
            child.write_text(json.dumps(record))
            self.assertNotEqual(module._parse(main, "claude", [root])[0], module._parse(child, "claude", [root])[0])
            codex = root / "codex.jsonl"
            records = [{"type": "session_meta", "payload": {"cwd": str(root), "id": "one"}}, {"type": "response_item", "payload": {"type": "message", "role": "assistant", "channel": "analysis", "content": "Hidden reasoning"}}, {"type": "response_item", "payload": {"type": "message", "role": "assistant", "channel": "final", "content": "Visible answer"}}]
            codex.write_text("\n".join(json.dumps(row) for row in records))
            body = module._parse(codex, "codex", [root])[1]
            self.assertNotIn("Hidden reasoning", body)
            self.assertIn("Visible answer", body)

    def test_archived_and_unavailable_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            active = home / ".codex/sessions"
            archive = home / ".codex/archived_sessions"
            active.mkdir(parents=True)
            archive.mkdir()
            rows = [{"type": "session_meta", "payload": {"id": "archived", "cwd": str(home / "project")}}, {"type": "event_msg", "payload": {"type": "user_message", "message": "Archived request"}}]
            (archive / "chat.jsonl").write_text("\n".join(json.dumps(row) for row in rows))
            dest = home / "exports"
            with patch.object(Path, "home", return_value=home):
                first = module.export_conversations(dest, [home / "project"])
                self.assertEqual(len(first["sessions"]), 1)
                self.assertIn("Archived request", (dest / "README.md").read_text())
                archive.rename(home / "unavailable")
                second = module.export_conversations(dest, [home / "project"])
                self.assertEqual(len(second["sessions"]), 1)
                self.assertTrue(second["errors"])

    def test_truncated_last_record_and_corrupt_middle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "session.jsonl"
            good = json.dumps({"type": "user", "sessionId": "one", "cwd": str(root), "message": {"content": "Valid request"}})
            path.write_text(good + '\n{"type":')
            parsed = module._parse(path, "claude", [root])
            self.assertIn("Valid request", parsed[1])
            self.assertTrue(parsed[2]["warnings"])
            path.write_text(good + '\n{"broken":\n' + good)
            with self.assertRaises(json.JSONDecodeError):
                module._parse(path, "claude", [root])


if __name__ == "__main__":
    unittest.main()
