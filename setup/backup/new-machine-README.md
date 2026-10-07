# Replacement laptop backup and restore

This workflow preserves dated generations and never deletes files, mirrors directories,
commits to Git, or changes live Codex databases. The older `backup.ps1` is not part of it.

## What is included

Core: the entire ai-os vault including `.env` and `raw`, sibling app repositories when
present, Codex/Claude chats and skills, global agents, CLI settings, Superwhisper recordings
and modes, Obsidian and editor user settings. SQLite uses a consistent read-only backup.
Personal scope (`--scope all`) additionally captures Documents, Downloads, Desktop and
Pictures. Apps themselves and downloaded models must be reinstalled. Account credentials
may be machine-bound, so reconnecting accounts can still be required.

Caches, dependency directories, browser profiles, lock/WAL temporary files, model downloads,
and the old `Documents/Codex/2026-10-06/in-x20/work` recovery staging are excluded. Original
cloud backup archives are unchanged. Symlinks/junctions are not followed. Missing roots
and capture failures are recorded in the manifest. A failure prevents `complete=true`.

## Capture

```powershell
python C:\Users\Joshu\dev\ai-os\setup\backup\new-machine-backup.py --stage C:\Users\Joshu\LaptopBackups\2026-10-07 --scope core
```

Use `--scope personal` for a separate personal-file generation or `--scope all` for both.
Repeated captures of the same scope store only
new or changed files. Keep ALL generation folders: the manifest points to the generation
that contains each unchanged file. Never upload only the most recent incremental folder.
The script validates archive CRCs and writes SHA256SUMS, full file checksums, explicit
errors and the source-to-restore mapping. Active files changed during capture are errors
and should be recaptured; backups do not require closing Codex.

## Private Google Drive

Cloud uploader splits archives into numbered 128 MiB parts. The restore script reassembles
them, verifies each part and the complete archive, then verifies extracted files. Download
every cloud generation folder into one parent directory, keeping generation folder names.

Upload every generation folder and these scripts to a private Drive folder using the
verified account. Never use GitHub for these archives because they include secrets and
personal files. A local completed archive is NOT proof of cloud backup. Record each
uploaded file ID, size and Drive MD5 checksum, and compare it with the local file.
No automatic scheduled task is enabled until a successful cloud upload is verified.

## Restore onto another Windows computer

1. Download all generations and install Python 3.12 or newer. Keep the timestamp folder
   names inside one parent directory. Inspect each `manifest.json` for `scope` and
   `complete`. Choose the newest complete **core** generation and the newest complete
   **personal** generation. They are separate scopes; restoring only personal does not
   restore the second brain. Keep their older dependency generations too.
2. Materialize the selected core generation into one NEW folder, then materialize the
   selected personal generation into another NEW folder:

```powershell
python new-machine-restore.py --generation C:\Backups\CORE_TIMESTAMP --output C:\RestoredCore
python new-machine-restore.py --generation C:\Backups\PERSONAL_TIMESTAMP --output C:\RestoredPersonal
```

3. The restore verifies every extracted file's SHA256. Copy `RestoredCore/ai-os` to your new user's
   `dev/ai-os`. Use manifest `roots` to map the other folders to the equivalent paths
   under your new Windows user. Preserve current data before merging or replacement.
4. Close the corresponding app before applying its database files. Reinstall apps and
   reconnect accounts. Different usernames require reviewing saved absolute paths.

`system/machine-info.json` preserves the user's Windows environment registry values,
including `CLAUDE_CODE_GIT_BASH_PATH`. Review paths before restoring environment values
on another computer. Install Git for Windows first and point that variable at its
`bin/bash.exe` if Claude Code requires it. Avoid replacing the new computer's entire PATH.

The replacement backup runs daily at 19:00 local and at logon once cloud verification
has succeeded and `new-machine-install-task.ps1` has registered it. It captures core and
personal changes, uploads every complete pending generation and verifies Drive MD5/size.
Failures leave a dated local log and no success marker. Check Windows Task Scheduler's
`Private Laptop Backup - Replacement` result and local `LATEST-CLOUD-SUCCESS.txt`.

This is a portable data backup, not a bootable Windows disk image. Apps, Windows licenses,
Personal Vault files never captured on the old machine and unreadable cloud files cannot
be recreated from it.
