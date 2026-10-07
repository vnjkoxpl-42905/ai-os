# Current local work available in Claude and Codex

This sync covers `ai-os` and each checkout under the sibling `ai-os-projects` directory. Every checkout gets its own private GitHub snapshot branch:

```text
codex/local-sync/<machine>/<checkout>
```

Snapshots capture unfinished files without changing the active Git index, checkout, branch, or production `main`. Separate worktrees stay separate. Existing cloud changes on a sync branch are a conflict; the uploader must stop rather than overwrite them. Make cloud edits on a new work branch and integrate them through the normal project workflow.

The Windows task `AI OS - Private GitHub Sync` checks every two minutes while signed in, and after logon. It publishes GitHub snapshots, then mirrors those exact commits to Google Drive. Changes arrive after that check and upload finish. Offline or sleeping laptops sync when execution and network access resume. A running cloud session retains its clone until it fetches current work.

## What is included

- Current project source, notes, skills, references, plans, and ordinary working data.
- Each LSAT U worktree on its own branch of the app repository.
- Readable Claude Code and Codex conversation exports for the covered roots, under `.cloud-sync/conversations/` in the AI OS snapshot.
- Generated workspace metadata and a freshness/status record.

Conversation exports preserve user and assistant prose, compaction context, and useful tool calls/results, with credential redaction. They exclude hidden reasoning and binary attachments. They are files Claude/Codex can read, not native chat sessions in either product's sidebar. Source JSONL disappearance removes the generated current-view export. UI archive/delete can leave the source file behind, so UI deletion is not guaranteed to remove an export. Previous Git commits retain history; permanent history erasure is not performed automatically.

Credentials, `.env`, raw archives, native browser/auth sessions, private keys, dependency/build/cache/runtime directories, nested Git metadata, and reparse links are excluded. Files above the configured GitHub size limit are reported. Gitleaks screens the actual upload snapshot and excluded files are recorded without printing secret values. It does not upload the entire laptop or bypass existing private backup rules. Private Drive backups continue independently.

## Google Drive mirror

The private folder `AI OS - Live Workspace Sync` contains machine and checkout folders. Each checkout has `latest.zip` and `manifest.json`; the archive contains the same filtered project and conversation snapshot as GitHub. Uploads replace the same Drive file and verify its checksum and size. Source deletions disappear from the latest archive. Prior Drive revisions and Git history can retain older content. Existing laptop backups stay separate. No Drive files are deleted or shared by this sync.

## Start cloud work from the latest snapshot

Attach `vnjkoxpl-42905/ai-os` and `vnjkoxpl-42905/lsatu-684d89db`. Select the sync branch for AI OS and the desired app checkout. Read the generated workspace metadata, the conversation index, and the current handoff. Confirm the latest snapshot against local sync status before resuming a paused task. Cloud live-system connections must be verified separately; repository access does not supply credentials.

```text
You are continuing work from private local-sync snapshots. Read setup/github-sync/README.md, .cloud-sync/workspace.json, and the relevant .cloud-sync/conversations/index.json and handoff. Resolve paths against your actual cloned repositories. Never assume a local Windows path exists here. Work on a new task branch; do not push edits to a local-sync branch. Fetch the latest sync branches before starting and check recorded source/freshness metadata. Report missing dependencies and test actual live tool access before production changes.
```

## Operations

```powershell
python setup/github-sync/sync.py --once --dry-run --config setup/github-sync/config.json
python setup/github-sync/run_sync.py --once --config setup/github-sync/config.json
powershell -NoProfile -ExecutionPolicy Bypass -File setup/github-sync/install.ps1
```

Generated state is machine-only in `setup/github-sync/state/`. `status.json` records GitHub results; `drive-status.json` records verified Drive uploads; `runner-status.json` records the combined run. Inspect these for conflicts, excluded files, failed credential checks, or upload errors. New project folders are discovered automatically. Folders without a remote receive a new private `local-<folder>` repository under the configured owner; existing name collisions and public or foreign repositories block publication for review.

Gitleaks 8.30.1 was obtained from its official GitHub release. The Windows archive SHA-256 matched the published checksum: `d29144deff3a68aa93ced33dddf84b7fdc26070add4aa0f4513094c8332afc4e`.
