import importlib.util
import tempfile
import unittest
import json
import sys
from types import SimpleNamespace
from unittest.mock import Mock, patch
from pathlib import Path

spec = importlib.util.spec_from_file_location("connect_home", Path(__file__).with_name("connect_home.py"))
home = importlib.util.module_from_spec(spec)
spec.loader.exec_module(home)


class HomeMappingTests(unittest.TestCase):
    def test_incomplete_or_stale_copy_cannot_be_connected(self):
        mapping = {"root_id": "root", "students": {"one": {"folder_id": "folder"}}}
        complete = {"status": "complete", "root_id": "root", "folders": {"one": "folder"}, "restore_sample": {"verified": True}}
        home.validate_copy(mapping, complete)
        for replacement in ({"status": "running"}, {"root_id": "other"}, {"folders": {"one": "other"}}, {"restore_sample": {}}):
            with self.assertRaises(RuntimeError):
                home.validate_copy(mapping, {**complete, **replacement})

    def test_readback_must_match_every_identity_and_folder_exactly(self):
        payload = {"drive_root_id": "root", "folders": [{"student_id": "student", "slug": "one", "folder_id": "folder"}]}
        readback = {"ok": True, **payload}
        home.verify_readback(payload, readback)
        for change in ({"drive_root_id": "other"}, {"folders": []}, {"folders": payload["folders"] * 2}, {"ok": False}):
            with self.assertRaises(RuntimeError):
                home.verify_readback(payload, {**readback, **change})
        for row in (None, "folder", [], {}, {"student_id": [], "slug": "one", "folder_id": "folder"}):
            with self.subTest(row=row), self.assertRaises(RuntimeError):
                home.verify_readback(payload, {**readback, "folders": [row]})

    def test_private_copy_rechecks_account_and_folder_integrity(self):
        mapping = {"root_id": "root", "students": {"one": {"folder_id": "folder"}}}
        remote = {"parents": ["root"], "mimeType": "application/vnd.google-apps.folder", "appProperties": {"lsatuContextPath": "one"}, "trashed": False}
        for change in (None, {"trashed": True}, {"parents": ["other"]}, {"appProperties": {}}, {"mimeType": "text/plain"}):
            fake = SimpleNamespace(ACCOUNT="owner@example.com", private=Mock(), gws=Mock(side_effect=[{"user": {"emailAddress": "owner@example.com"}}, {**remote, **(change or {})}]))
            with self.subTest(change=change), patch.dict(sys.modules, {"copy_students": fake}):
                if change is None:
                    home.verify_private_copy(mapping)
                    self.assertEqual(fake.private.call_count, 2)
                else:
                    with self.assertRaises(RuntimeError):
                        home.verify_private_copy(mapping)
        fake.gws = Mock(return_value={"user": {"emailAddress": "wrong@example.com"}})
        fake.private.reset_mock()
        with patch.dict(sys.modules, {"copy_students": fake}), self.assertRaises(RuntimeError):
            home.verify_private_copy(mapping)
        fake.private.assert_not_called()

    def test_apply_failures_leave_safe_audit_and_raise(self):
        payload = {"drive_root_id": "root", "folders": []}
        for stage in ("private_copy_check", "import_request", "readback"):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as temporary:
                destination = Path(temporary) / "audit.json"
                output = {"mode": "applied", "payload": payload}
                responses = [RuntimeError("secret-token")] if stage == "import_request" else [{"ok": True}, {"ok": True, "drive_root_id": "wrong", "folders": []}]
                with patch.object(home, "verify_private_copy", side_effect=RuntimeError("secret-token") if stage == "private_copy_check" else None), patch.object(home, "request_json", side_effect=responses), self.assertRaises(RuntimeError):
                    home.apply_import({}, payload, output, destination, "https://example.com", {"Authorization": "secret-token"})
                saved = destination.read_text()
                audit = json.loads(saved)
                self.assertEqual(audit["status"], "failed")
                self.assertEqual(audit["failed_stage"], stage)
                self.assertFalse(audit["readback_verified"])
                self.assertNotIn("secret-token", saved)

    def test_apply_success_requires_exact_readback(self):
        payload = {"drive_root_id": "root", "folders": [{"student_id": "student", "slug": "one", "folder_id": "folder"}]}
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "audit.json"
            output = {"mode": "applied", "payload": payload}
            with patch.object(home, "verify_private_copy"), patch.object(home, "request_json", side_effect=[{"ok": True, "ignored_provider_detail": "not-saved"}, {"ok": True, **payload}]) as request:
                home.apply_import({}, payload, output, destination, "https://example.com", {})
            saved = json.loads(destination.read_text())
            self.assertEqual(saved["status"], "verified")
            self.assertTrue(saved["import_confirmed"])
            self.assertTrue(saved["readback_verified"])
            self.assertEqual(request.call_count, 2)
            self.assertNotIn("ignored_provider_detail", saved)

    def test_source_and_account_edge_cases_are_not_matched(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for slug, content in (("valid", "---\nemail: person@example.com\n---\n"), ("missing", "No identity")):
                (root / slug).mkdir()
                (root / slug / f"{slug}.md").write_text(content, encoding="utf-8")
            roster = [{"email": "person@example.com", "class_id": "id", "role": "admin"}]
            for slug, folder_id, reason in (("../bad", "valid_drive_identifier", "invalid_or_missing_source"), ("valid", "bad!", "invalid_or_missing_source"), ("missing", "valid_drive_identifier", "missing_primary_email"), ("valid", "valid_drive_identifier", "ineligible_account")):
                links, unresolved = home.match_folders({"students": {slug: {"folder_id": folder_id}}}, root, roster)
                self.assertEqual(links, [])
                self.assertEqual(unresolved[0]["reason"], reason)
            profile = root / "valid" / "valid.md"
            original = Path.is_symlink
            with patch.object(Path, "is_symlink", lambda path: path == profile or original(path)):
                links, unresolved = home.match_folders({"students": {"valid": {"folder_id": "valid_drive_identifier"}}}, root, roster)
            self.assertEqual(links, [])
            self.assertEqual(unresolved[0]["reason"], "invalid_or_missing_source")

    def test_identity_uses_only_the_authored_primary_field(self):
        self.assertEqual(home.primary_email('---\nemail: Student@Example.com\n---\n'), "student@example.com")
        self.assertIsNone(home.primary_email("Contact student@example.com"))
        self.assertIsNone(home.primary_email('---\nemail: one@example.com\nemail: two@example.com\n---\n'))

    def test_exact_matches_reject_archived_and_duplicate_local_identity(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mapping = {"students": {}}
            for slug, email in [("one", "one@example.com"), ("copy", "one@example.com"), ("old", "old@example.com"), ("valid", "valid@example.com")]:
                (root / slug).mkdir()
                (root / slug / f"{slug}.md").write_text(f"---\nemail: {email}\n---\n", encoding="utf-8")
                mapping["students"][slug] = {"folder_id": "valid_drive_identifier"}
            roster = [{"class_id": "one", "email": "one@example.com", "role": "student"},
                      {"class_id": "old", "email": "old@example.com", "archived_at": "2026-01-01", "role": "student"},
                      {"class_id": "valid", "email": "valid@example.com", "role": "student"}]
            links, unresolved = home.match_folders(mapping, root, roster)
            self.assertEqual([row["slug"] for row in links], ["valid"])
            self.assertEqual(sorted(row["reason"] for row in unresolved), ["duplicate_local_email", "duplicate_local_email", "ineligible_account"])

    def test_ambiguous_remote_identity_is_not_guessed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "student").mkdir()
            (root / "student" / "student.md").write_text("---\nemail: person@example.com\n---\n", encoding="utf-8")
            mapping = {"students": {"student": {"folder_id": "valid_drive_identifier"}}}
            links, unresolved = home.match_folders(mapping, root, [{"class_id": "a", "email": "person@example.com"}, {"class_id": "b", "email": "person@example.com"}])
            self.assertEqual(links, [])
            self.assertEqual(unresolved[0]["reason"], "ambiguous_account")


if __name__ == "__main__":
    unittest.main()
