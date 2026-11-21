"""Preview/archive automated review chats through the running Codex app server.

Usage: python system/scripts/codex-sidebar-cleanup.py [--apply]
No database edits, file deletion, model calls, or history imports.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import queue
import shutil
import subprocess
import sys
import threading
import time

PREFIX = "You are the independent reviewer."
SOURCES = ["cli", "vscode", "exec", "appServer", "subAgent", "subAgentReview",
           "subAgentCompact", "subAgentThreadSpawn", "subAgentOther", "unknown"]


def command(standalone=False):
    transport = ["app-server", "--stdio"] if standalone else ["app-server", "proxy"]
    exe = shutil.which("codex.exe")
    if exe:
        return [exe] + transport
    shim = shutil.which("codex.cmd") or shutil.which("codex")
    if shim:
        root = Path(shim).parent
        entry = root / "node_modules/@openai/codex/bin/codex.js"
        node = root / "node.exe"
        if entry.is_file():
            return [str(node) if node.is_file() else shutil.which("node"),
                    str(entry)] + transport
    raise RuntimeError("Cannot find Codex CLI. Put codex on PATH.")


class Client:
    def __init__(self, standalone=False):
        self.standalone = standalone

    def __enter__(self):
        self.messages = queue.Queue()
        self.seq = 0
        self.proc = subprocess.Popen(command(self.standalone), stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     text=True, encoding="utf-8",
                                     creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        def reader():
            try:
                for line in self.proc.stdout:
                    self.messages.put(json.loads(line))
            except Exception as exc:
                self.messages.put(exc)
            finally:
                self.messages.put(EOFError("Codex proxy closed. Keep Codex desktop open."))
        threading.Thread(target=reader, daemon=True).start()
        # Drain diagnostics without printing potentially private server output.
        threading.Thread(target=lambda: list(self.proc.stderr), daemon=True).start()
        try:
            self.call("initialize", {"clientInfo": {"name": "sidebar_cleanup", "version": "1.0"},
                                     "capabilities": {"experimentalApi": True}})
            self.send({"method": "initialized"})
        except BaseException:
            self.__exit__(None, None, None)
            raise
        return self

    def send(self, value):
        self.proc.stdin.write(json.dumps(value) + "\n")
        self.proc.stdin.flush()

    def call(self, method, params):
        self.seq += 1
        ident = self.seq
        self.send({"id": ident, "method": method, "params": params})
        deadline = time.monotonic() + 45
        while True:
            try:
                value = self.messages.get(timeout=max(.01, deadline - time.monotonic()))
            except queue.Empty:
                raise RuntimeError(f"Timed out: {method}; no direct-database fallback.")
            if isinstance(value, Exception):
                raise value
            if value.get("id") == ident:
                if "error" in value:
                    raise RuntimeError(f"{method}: {value['error']}")
                return value["result"]
            if "id" in value and "method" in value:
                self.send({"id": value["id"], "error": {"code": -32601,
                           "message": "Cleanup client does not handle requests"}})

    def all(self, method, params):
        rows, cursor, seen = [], None, set()
        while True:
            result = self.call(method, dict(params, cursor=cursor, limit=100))
            rows.extend(result["data"])
            cursor = result.get("nextCursor")
            if not cursor:
                return rows
            if cursor in seen:
                raise RuntimeError("Repeated pagination cursor; refusing incomplete scan.")
            seen.add(cursor)

    def __exit__(self, *unused):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait()


def eligible(row, excluded, cutoff):
    status = row.get("status", {})
    status = status.get("type") if isinstance(status, dict) else status
    section = row.get("section") or {}
    pinned = section == "pinned" or (isinstance(section, dict) and section.get("id") == "pinned")
    return (row["id"] not in excluded and not pinned
            and (row.get("name") or row.get("preview", "")).startswith(PREFIX)
            and status in ("idle", "notLoaded")
            and row["updatedAt"] < cutoff)


def completed_import(row):
    """Standalone server cannot see desktop runtime; only touch completed imports."""
    path = row.get("path")
    if not path or not Path(path).is_file():
        return False
    last = None
    imported = False
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            event = json.loads(line)
            payload = event.get("payload", {})
            if event.get("type") == "event_msg" and payload.get("type") in ("task_started", "task_complete", "task_aborted"):
                last = payload.get("type")
                imported |= str(payload.get("turn_id", "")).startswith("external-import-")
    return imported and last == "task_complete"


def clean_legacy_projects(log_dir, apply):
    """Desktop keeps its own legacy project list, separate from app-server IDs."""
    path = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / ".codex-global-state.json"
    original = path.read_bytes()
    state = json.loads(original)
    projects = state.get("local-projects", {})
    stale = {key for key, value in projects.items()
             if value.get("rootPaths") and all(not Path(root).exists() for root in value["rootPaths"])}
    print(f"Desktop legacy missing-folder registrations: {len(stale)}")
    for key in sorted(stale):
        print(f"  {projects[key]['name']}")
    if not apply or not stale:
        return
    # Back up the entire state before changing only project registrations/references.
    log_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    backup = log_dir / f"desktop-state-before-{stamp}.json"
    backup.write_bytes(original)
    for key in stale:
        projects.pop(key)
    for key in ("project-order", "pinned-project-ids"):
        if isinstance(state.get(key), list):
            state[key] = [item for item in state[key] if item not in stale]
    for key in ("sidebar-project-thread-orders",):
        for project in stale:
            state.get(key, {}).pop(project, None)
    # Preserve conversations by unassigning stale project membership.
    assignments = state.get("thread-project-assignments", {})
    for thread, project in list(assignments.items()):
        project_id = project.get("projectId") if isinstance(project, dict) else project
        if isinstance(project_id, str) and project_id in stale:
            del assignments[thread]
    for mapping in state.get("app-server-project-id-by-legacy-project-id-by-host", {}).values():
        for project in stale:
            mapping.pop(project, None)
    selected = state.get("selected-project")
    selected_id = selected.get("projectId") if isinstance(selected, dict) else selected
    if isinstance(selected_id, str) and selected_id in stale:
        state["selected-project"] = None
    # Read once more immediately before replacing to avoid clobbering app writes.
    if path.read_bytes() != original:
        raise RuntimeError("Desktop state changed concurrently; backup saved, no state written. Retry.")
    temp = path.with_name(f".cleanup-{stamp}.tmp")
    with temp.open("xb") as stream:
        stream.write(json.dumps(state, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
        stream.flush()
        os.fsync(stream.fileno())
    if path.read_bytes() != original:
        raise RuntimeError(f"Concurrent desktop write; refusing replace. Unused temp: {temp}")
    os.replace(temp, path)
    verify = json.loads(path.read_bytes())
    if any(key in verify.get("local-projects", {}) for key in stale):
        raise RuntimeError("Desktop state readback failed")
    print(f"Removed {len(stale)} legacy registrations. Backup: {backup}")
    print("Desktop may require restart to drop already-rendered entries; no restart is forced.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Archive matches; default is preview")
    parser.add_argument("--standalone", action="store_true", help="When desktop proxy is unavailable, scan completed external imports only")
    parser.add_argument("--remove-stale-projects", action="store_true", help="With --apply, remove missing-folder project registrations (never filesystem folders)")
    parser.add_argument("--stop-imports", action="store_true", help="With --apply, disable automatic external-agent imports in Codex desktop config")
    parser.add_argument("--clean-legacy-projects", action="store_true", help="Back up and remove missing-folder entries from desktop's legacy project list")
    parser.add_argument("--exclude", action="append", default=[], help="Protect a thread ID (repeatable)")
    parser.add_argument("--min-age-hours", type=float, default=1)
    parser.add_argument("--log-dir", type=Path, default=Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "CodexCleanup")
    args = parser.parse_args()
    if args.min_age_hours < 0:
        parser.error("Minimum age must be nonnegative")
    excluded = set(args.exclude)
    if os.environ.get("CODEX_THREAD_ID"):
        excluded.add(os.environ["CODEX_THREAD_ID"])
    cutoff = time.time() - args.min_age_hours * 3600
    with Client(args.standalone) as client:
        if args.stop_imports:
            if args.apply:
                config_path = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "config.toml"
                args.log_dir.mkdir(parents=True, exist_ok=True)
                backup = args.log_dir / ("config-before-" + dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".toml")
                backup.write_bytes(config_path.read_bytes())
                client.call("config/value/write", {"keyPath": "desktop.external-agent-import-sync-enabled",
                            "value": False, "mergeStrategy": "upsert"})
                config = client.call("config/read", {"includeLayers": False})["config"]
                if config.get("desktop", {}).get("external-agent-import-sync-enabled") is not False:
                    raise RuntimeError("Automatic import disable readback failed")
                print("Verified: desktop automatic external-agent imports disabled.")
            else:
                print("PREVIEW: would disable desktop automatic external-agent imports.")
        rows = client.all("thread/list", {"archived": False, "sourceKinds": SOURCES, "useStateDbOnly": True,
                                         "sortKey": "created_at"})
        matches = [r for r in rows if eligible(r, excluded, cutoff)]
        if args.standalone:
            matches = [r for r in matches if completed_import(r)]
        projects = client.all("project/list", {})
        stale = [p for p in projects if p.get("roots") and all(not Path(r["path"]).exists() for r in p["roots"])]
        print(f"{'APPLY' if args.apply else 'PREVIEW'}: {len(matches)} review chats; {len(stale)} missing-folder projects.")
        for r in matches:
            print(f"  Archive {r['id']}  {r.get('cwd', '')}")
        for p in stale:
            print(f"  Stale project ({'remove registration' if args.remove_stale_projects else 'report only'}): {p['name']} [{p['id']}]")
        if not args.apply:
            if args.clean_legacy_projects:
                clean_legacy_projects(args.log_dir, False)
            return
        args.log_dir.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        log_path = args.log_dir / f"cleanup-{stamp}.jsonl"
        count = 0
        with log_path.open("x", encoding="utf-8") as log:
            def record(value):
                log.write(json.dumps(value) + "\n")
                log.flush()
                os.fsync(log.fileno())
            for row in matches:
                fresh = client.call("thread/read", {"threadId": row["id"], "includeTurns": False})["thread"]
                if not eligible(fresh, excluded, cutoff):
                    continue
                if args.standalone and not completed_import(fresh):
                    continue
                record({"action": "archive_requested", "threadId": row["id"],
                        "name": fresh.get("name"), "cwd": fresh.get("cwd")})
                client.call("thread/archive", {"threadId": row["id"]})
                record({"action": "archived", "threadId": row["id"]})
                count += 1
            if args.remove_stale_projects:
                for project in stale:
                    fresh = client.call("project/read", {"projectId": project["id"]})["project"]
                    if fresh != project or any(Path(r["path"]).exists() for r in fresh["roots"]):
                        raise RuntimeError("Project changed since preview; refusing removal.")
                    members = client.all("thread/list", {"projectId": project["id"], "archived": False,
                                                         "sourceKinds": SOURCES, "useStateDbOnly": True})
                    if members:
                        print(f"Preserving {project['name']}: has unarchived conversations.")
                        continue
                    record({"action": "project_remove_requested", "project": fresh})
                    client.call("project/delete", {"projectId": project["id"]})
                    if any(p["id"] == project["id"] for p in client.all("project/list", {})):
                        raise RuntimeError("Project removal verification failed.")
                    record({"action": "project_removed", "projectId": project["id"]})
                    print(f"Removed stale registration: {project['name']}")
        remaining = {r["id"] for r in client.all("thread/list", {"archived": False, "sourceKinds": SOURCES, "useStateDbOnly": True})}
        if any(r["id"] in remaining for r in matches):
            print("Some candidates remain (changed status or were not archived).")
        print(f"Archived {count}. Recovery log: {log_path}")
        print("Recovery API: thread/unarchive with the logged threadId. No filesystem folders deleted.")
    if args.clean_legacy_projects:
        clean_legacy_projects(args.log_dir, True)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, EOFError) as exc:
        print(f"Cleanup stopped: {exc}", file=sys.stderr)
        sys.exit(1)
