# Clean automated reviews out of the Codex sidebar

From `C:/Users/Joshu/dev/ai-os`:

```powershell
# Preview completed imported reviews and missing-folder projects.
python system/scripts/codex-sidebar-cleanup.py --standalone

# Archive reviews and remove empty missing-folder project registrations.
python system/scripts/codex-sidebar-cleanup.py --standalone --apply --remove-stale-projects

# Prevent automatic Claude chat/project imports; also clean legacy desktop entries.
python system/scripts/codex-sidebar-cleanup.py --standalone --apply --stop-imports --clean-legacy-projects
```

Without `--standalone`, the script uses the running app-server proxy. This installation
did not expose that proxy during verification on 2026-10-28. Standalone mode starts a
temporary local app-server and requires saved external-import history ending in a
completed task. It never launches a model turn.

Only titles starting with `You are the independent reviewer.` qualify. The default
minimum age is one hour. Pinned, active, unknown-status and explicitly excluded chats
are skipped. `CODEX_THREAD_ID` is excluded when available; add `--exclude THREAD_ID`
for any other conversation to protect. Standalone runtime status cannot see activity
in other processes, so it also checks the saved completion marker immediately before
archiving. Avoid reopening matching reviews while cleanup runs.

Projects are report-only unless `--remove-stale-projects` and `--apply` are both
present. Removal requires all roots to be missing and no unarchived member threads.
Files and repositories are never deleted. An inaccessible drive can look missing;
check the preview before applying project removal when external drives are involved.

Actions are flushed to `%LOCALAPPDATA%/CodexCleanup/cleanup-*.jsonl` before and after
each mutation. Archived chats can be restored in Codex Settings or with the supported
`thread/unarchive` API and a logged ID. Removed project metadata is retained in the
log; recreating a registration can assign a new ID.

`--stop-imports` uses `config/value/write` to set
`desktop.external-agent-import-sync-enabled = false`, backs up config.toml, and
verifies the effective value through `config/read`. It stops automatic external-agent
imports, including automatic chat/project imports. Manual imports can still bring
items back. Existing review workflows and source transcripts are preserved.

`--clean-legacy-projects` also backs up `.codex-global-state.json` and removes only
missing-root project entries and their stale references. It checks for concurrent
file changes before replacing the state. The running desktop can rewrite its cached
state afterward: for durable legacy cleanup, close Codex first and run from an
independent PowerShell window. No process is forcibly closed by this script.

Verified: preview, live archival, second preview returning zero eligible chats,
backend project removal/readback, automatic-import setting readback, and desktop
sidebar grouping through the Codex app tools. Running-desktop legacy state can still
restore stale registrations; do not call that part complete from a file read alone.

Safety regression checks:

```powershell
python system/scripts/test_codex_sidebar_cleanup.py
```
