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
- Separate global Claude, Codex and shared skill catalogs, global instructions, covered Claude native memories and a consistent readable Codex memory export under `.cloud-sync/runtime/`.
- Joshua-authorized credentials and runtime configuration in an authenticated encrypted package under `.cloud-sync/private/`. Plaintext credentials remain excluded from ordinary files and conversation exports.

Conversation exports preserve user and assistant prose, compaction context, and useful tool calls/results, with credential redaction. They exclude hidden reasoning and binary attachments. They are files Claude/Codex can read, not native chat sessions in either product's sidebar. Source JSONL disappearance removes the generated current-view export. UI archive/delete can leave the source file behind, so UI deletion is not guaranteed to remove an export. Previous Git commits retain history; permanent history erasure is not performed automatically.

Plaintext credentials, `.env`, raw archives, native browser sessions, OS keyrings, dependency/build/cache/runtime directories, nested Git metadata, and reparse links are excluded from the readable snapshot. Configured credential files and discovered project `.env` files are included only inside the encrypted package. Files above the configured GitHub size limit are reported. Gitleaks screens the upload snapshot and records exclusions without printing secret values. Private Drive laptop backups continue independently.

## Credential access in cloud

The encrypted package uses AES-GCM with a random 256-bit key. Its key stays in the ignored, access-restricted `setup/github-sync/state/private/` directory, outside GitHub and Drive. `cloud-key.env` provides the one-time cloud key configuration; never paste its contents into a chat, commit or handoff. Any cloud environment given this key can decrypt all included credentials. Environment variables in Claude's settings are visible to users of that environment; account-level access and environment selection matter.

After privately provisioning `AI_OS_SYNC_KEY`, run these commands from the AI OS cloud checkout:

```bash
python -m pip install -r setup/github-sync/requirements.txt
python setup/github-sync/credential_bundle.py --decrypt .cloud-sync/private/credentials.enc --destination .cloud-private/credentials
```

Do not print decrypted files, enable shell tracing, commit them, or overwrite native cloud authentication with local auth files. Use the central `.env` and relevant project credentials for the specific tool that needs them. GWS keyring data, expiring login tokens and Windows paths can require cloud authentication or path adaptation; encrypted transport does not prove the service will accept them. Decryption refuses existing destination files, so use a fresh protected directory for a refreshed package.

Each repository also carries `.cloud-sync/private/redacted-context.enc` when readable files required redaction. This compressed encrypted package preserves those original visible text files with the same unlock key. Its manifest identifies their logical paths. Large encrypted packages use a small .enc descriptor plus .enc.partNNNN files, each below GitHub’s file-size limit. Keep all parts together; the decryption helper verifies and reassembles them automatically. Decrypt into a fresh ignored private directory and read the original when an explanation, skill or code line was redacted. Keep plaintext credentials out of work branches and PRs. Source session JSONL and hidden reasoning are never added to this package.

```bash
python setup/github-sync/credential_bundle.py --decrypt .cloud-sync/private/redacted-context.enc --destination .cloud-private/original-context
```

Use the AI OS copy of `credential_bundle.py` for packages belonging to an app checkout, resolving the package and destination paths explicitly. Git commit time is the snapshot freshness authority; generated metadata stays stable on unchanged files to avoid uploading identical archives every check.

## The web and local runtimes differ

Cloud sessions run on separate machines and cannot become identical to the local Windows process. Exported context is readable; native chat state, plugin installations, machine-bound credentials and connected browser sessions are separate. Cloud work returns through a reviewed task branch/PR and normal local integration; this uploader does not silently pull cloud edits over local unfinished work. Native cloud-only conversations are not automatically downloaded by this local exporter.

For the actual same local session from a browser, [Claude Remote Control](https://code.claude.com/docs/en/remote-control) keeps local tools, files and the conversation available remotely. The local computer and Claude process must keep running.

## Google Drive mirror

The private folder [AI OS - Live Workspace Sync](https://drive.google.com/drive/folders/1z3oXAoKOWNqKjAPO-Txtkm0uEgz88sgY) contains machine and checkout folders. Each checkout has `latest.zip` and `manifest.json`; the archive contains the same filtered project and conversation snapshot as GitHub. Uploads replace the same Drive file and verify its checksum and size. Source deletions disappear from the latest archive. Prior Drive revisions and Git history can retain older content. Existing laptop backups stay separate. No Drive files are deleted or shared by this sync.

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
