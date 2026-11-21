"""Prepare verified student-folder links; import only after the Home backend is deployed."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
DRIVE_ID = re.compile(r"^[A-Za-z0-9_-]{10,200}$")


def read_env(path: Path) -> dict[str, str]:
    result = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def primary_email(text: str) -> str | None:
    """Use the authored identity field; never guess from names or prose."""
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not front:
        return None
    matches = re.findall(r"^email:\s*([^\r\n]+)", front[1], re.M)
    if len(matches) != 1:
        return None
    value = matches[0].strip().strip("\"'").lower()
    return value if EMAIL.fullmatch(value) else None


def match_folders(mapping: dict, students_root: Path, roster: list[dict]) -> tuple[list, list]:
    candidates, unresolved = [], []
    root = students_root.resolve()
    for slug, folder in sorted(mapping["students"].items()):
        profile = students_root / slug / f"{slug}.md"
        if (not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug)
                or profile.is_symlink() or not profile.resolve().is_relative_to(root)
                or not profile.is_file() or not DRIVE_ID.fullmatch(folder.get("folder_id", ""))):
            unresolved.append({"slug": slug, "reason": "invalid_or_missing_source"})
            continue
        raw = profile.read_bytes()
        email = primary_email(raw.decode("utf-8-sig"))
        if not email:
            unresolved.append({"slug": slug, "reason": "missing_primary_email"})
            continue
        candidates.append({"slug": slug, "email": email, "folder_id": folder["folder_id"],
                           "profile_sha256": hashlib.sha256(raw).hexdigest()})
    counts = Counter(row["email"] for row in candidates)
    links = []
    for row in candidates:
        if counts[row["email"]] != 1:
            unresolved.append({"slug": row["slug"], "reason": "duplicate_local_email"})
            continue
        hits = [user for user in roster if str(user.get("email", "")).strip().lower() == row["email"]]
        if len(hits) != 1:
            unresolved.append({"slug": row["slug"], "reason": "no_exact_account" if not hits else "ambiguous_account"})
            continue
        user = hits[0]
        if user.get("role") == "admin" or user.get("archived_at") or user.get("is_archived") or not user.get("class_id"):
            unresolved.append({"slug": row["slug"], "reason": "ineligible_account"})
            continue
        links.append({**row, "student_id": user["class_id"], "emails": [row["email"]]})
    return links, unresolved


def request_json(url: str, headers: dict, body=None):
    request = urllib.request.Request(url, headers=headers, data=None if body is None else json.dumps(body).encode())
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # Provider bodies may contain operational details. Keep credentials and bodies out of output.
        raise RuntimeError(f"Request failed with HTTP {error.code}: {url.split('/functions/v1/')[-1].split('?')[0]}") from None


def validate_copy(mapping: dict, state: dict) -> None:
    if state.get("status") != "complete" or state.get("root_id") != mapping.get("root_id"):
        raise RuntimeError("The private Drive copy is not complete for this root")
    for slug, folder in mapping.get("students", {}).items():
        if state.get("folders", {}).get(slug) != folder.get("folder_id"):
            raise RuntimeError(f"Drive folder mapping does not match the verified copy: {slug}")
    if not state.get("restore_sample", {}).get("verified"):
        raise RuntimeError("The Drive restore check is missing")


def verify_readback(payload: dict, readback: dict) -> None:
    if not isinstance(readback, dict) or readback.get("ok") is not True or not isinstance(readback.get("folders"), list):
        raise RuntimeError("Invalid folder readback response")
    if readback.get("drive_root_id") != payload["drive_root_id"]:
        raise RuntimeError("Stored Drive root does not match")
    fields = ("student_id", "slug", "folder_id")
    if any(not isinstance(row, dict) or any(not isinstance(row.get(field), str) or not row[field] for field in fields)
           for row in readback["folders"]):
        raise RuntimeError("Invalid folder readback row")
    expected = {tuple(row.get(field) for field in fields) for row in payload["folders"]}
    actual = [tuple(row.get(field) for field in fields) for row in readback["folders"]]
    if set(actual) != expected or len(actual) != len(expected):
        raise RuntimeError("Stored student-folder links do not exactly match the import")


def verify_private_copy(mapping: dict) -> None:
    # Reuse the copy tool's provider-side checks just before importing any links.
    from copy_students import ACCOUNT, gws, private
    account = gws(["about", "get"], {"fields": "user(emailAddress)"})
    if account.get("user", {}).get("emailAddress", "").lower() != ACCOUNT:
        raise RuntimeError("Unexpected Drive account")
    private(mapping["root_id"])
    for slug, folder in mapping["students"].items():
        private(folder["folder_id"])
        remote = gws(["files", "get"], {"fileId": folder["folder_id"], "fields": "parents,mimeType,appProperties,trashed"})
        if (remote.get("trashed") or remote.get("mimeType") != "application/vnd.google-apps.folder"
                or remote.get("parents") != [mapping["root_id"]]
                or remote.get("appProperties", {}).get("lsatuContextPath") != slug):
            raise RuntimeError(f"Drive student folder is no longer the verified copy: {slug}")


def apply_import(mapping: dict, payload: dict, output: dict, destination: Path, base: str, headers: dict) -> None:
    """Persist a safe audit even when a write succeeds but its readback fails."""
    stage = "private_copy_check"
    output["status"] = "applying"
    try:
        verify_private_copy(mapping)
        stage = "import_request"
        result = request_json(base + "/functions/v1/teacher-post-session-sync", headers, payload)
        if not isinstance(result, dict) or result.get("ok") is not True:
            raise RuntimeError("Backend did not confirm the folder import")
        output["import_confirmed"] = True
        stage = "readback"
        readback = request_json(base + "/functions/v1/teacher-post-session-sync", headers, {"action": "folder_links"})
        verify_readback(payload, readback)
        output["readback_verified"] = True
        output["status"] = "verified"
    except Exception:
        # Never serialize provider bodies, exception text, credentials or headers.
        output.update(status="failed", failed_stage=stage, readback_verified=False)
        raise RuntimeError(f"Folder connection failed during {stage}; inspect the saved audit before retrying") from None
    finally:
        destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", type=Path, required=True, help="Local LSAT U checkout")
    parser.add_argument("--apply", action="store_true", help="Import links into the deployed admin-only backend")
    args = parser.parse_args()
    env = {**read_env(args.app / ".env"), **read_env(ROOT / ".env")}
    base = env.get("VITE_SUPABASE_URL", "").rstrip("/")
    if base != "https://atrcqxpmqrynmtvvyjju.supabase.co":
        raise RuntimeError("Refusing an unexpected LSAT U backend")
    key = env.get("VITE_SUPABASE_PUBLISHABLE_KEY") or env.get("VITE_SUPABASE_ANON_KEY")
    if not key or not env.get("LSATPREP_ADMIN_EMAIL") or not env.get("LSATPREP_ADMIN_PASSWORD"):
        raise RuntimeError("Required existing credentials are unavailable")
    token = request_json(base + "/auth/v1/token?grant_type=password", {"apikey": key, "Content-Type": "application/json"},
                         {"email": env["LSATPREP_ADMIN_EMAIL"], "password": env["LSATPREP_ADMIN_PASSWORD"]})
    if not token.get("access_token") or not token.get("user", {}).get("id"):
        raise RuntimeError("Admin sign-in did not return a valid identity")
    headers = {"apikey": key, "Authorization": "Bearer " + token["access_token"], "Content-Type": "application/json"}
    roster = request_json(base + "/functions/v1/admin-manage-users", headers)
    if not isinstance(roster, list):
        raise RuntimeError("Unexpected roster response")
    owner_id = token["user"]["id"]
    if not any(user.get("class_id") == owner_id and user.get("role") == "admin" for user in roster):
        raise RuntimeError("Signed-in identity is not a verified roster admin")
    mapping = json.loads((Path(__file__).parent / "student-folders.generated.json").read_text(encoding="utf-8-sig"))
    if not DRIVE_ID.fullmatch(mapping.get("root_id", "")):
        raise RuntimeError("Invalid private Drive root")
    state = json.loads((Path(__file__).parent / "copy-state.generated.json").read_text(encoding="utf-8-sig"))
    validate_copy(mapping, state)
    links, unresolved = match_folders(mapping, ROOT / "students", roster)
    payload = {"action": "import_folders", "drive_root_id": mapping["root_id"], "folders": links}
    output = {"generated_at": datetime.now(timezone.utc).isoformat(), "mode": "applied" if args.apply else "dry_run",
              "owner_id": owner_id, "matched_count": len(links), "unresolved": unresolved, "payload": payload}
    destination = Path(__file__).parent / "home-import.generated.json"
    if args.apply:
        apply_import(mapping, payload, output, destination, base, headers)
        # Import does not activate the schedule or move its start cutoff.
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"mode": output["mode"], "matched": len(links), "unresolved": unresolved,
                      "output": str(destination), "owner_id": owner_id}))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, OSError) as error:
        raise SystemExit(str(error)) from None
