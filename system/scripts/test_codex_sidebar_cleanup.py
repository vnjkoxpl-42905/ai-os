import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("cleanup", Path(__file__).with_name("codex-sidebar-cleanup.py"))
cleanup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cleanup)


class CleanupTests(unittest.TestCase):
    def row(self, **extra):
        return dict({"id": "review", "name": cleanup.PREFIX, "status": {"type": "notLoaded"}, "updatedAt": 1}, **extra)

    def test_protects_active_excluded_recent_and_renamed_chats(self):
        row = self.row()
        self.assertTrue(cleanup.eligible(row, set(), 100))
        self.assertFalse(cleanup.eligible(row, {"review"}, 100))
        for field, value in [("status", {"type": "active"}), ("updatedAt", 101), ("name", "My real conversation")]:
            candidate = dict(row)
            candidate[field] = value
            self.assertFalse(cleanup.eligible(candidate, set(), 100))

    def test_running_import_is_not_completed(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "session.jsonl"
            def write(kinds):
                path.write_text("\n".join(json.dumps({"type": "event_msg", "payload": {"type": kind, "turn_id": "external-import-turn-1"}}) for kind in kinds), encoding="utf-8")
            write(["task_started", "task_complete"])
            self.assertTrue(cleanup.completed_import({"path": str(path)}))
            write(["task_started", "task_complete", "task_started"])
            self.assertFalse(cleanup.completed_import({"path": str(path)}))
            self.assertFalse(cleanup.completed_import({"path": str(path.with_suffix('.missing'))}))

    def test_legacy_cleanup_backs_up_preserves_files_and_unassigns_dict_membership(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            existing = root / "real-project"
            existing.mkdir()
            state = {"local-projects": {
                "stale": {"name": "stale", "rootPaths": [str(root / "missing")]},
                "keep": {"name": "keep", "rootPaths": [str(existing)]}},
                "project-order": ["stale", "keep"], "selected-project": {"type": "local", "projectId": "stale"},
                "thread-project-assignments": {"chat": {"projectKind": "local", "projectId": "stale"}},
                "unrelated": {"preserve": True}}
            path = root / ".codex-global-state.json"
            before = json.dumps(state).encode()
            path.write_bytes(before)
            with patch.dict(os.environ, {"CODEX_HOME": str(root)}), contextlib.redirect_stdout(io.StringIO()):
                cleanup.clean_legacy_projects(root / "logs", False)
                self.assertEqual(path.read_bytes(), before)
                cleanup.clean_legacy_projects(root / "logs", True)
            after = json.loads(path.read_bytes())
            self.assertEqual(list(after["local-projects"]), ["keep"])
            self.assertEqual(after["thread-project-assignments"], {})
            self.assertIsNone(after["selected-project"])
            self.assertEqual(after["unrelated"], state["unrelated"])
            self.assertTrue(existing.is_dir())
            self.assertEqual(next((root / "logs").glob("*.json")).read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
