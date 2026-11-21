# New laptop checklist, 2026-11-11

Restored from the 2026-11-01 backup. Each item says whether it was checked or assumed.

## Done and checked

- **Vault** (`C:\Users\Joshu\dev\ai-os`): `wiki/` has 47 files, including `hot.md`, `index.md`, `log.md` and `tasks.md`. `raw/` is present.
- **Git:** GitHub, this laptop and the backup are all at commit `7e3a37c4`. No commits were lost. Nothing was committed or pushed during the restore.
- **App projects:** 85 folders in `C:\Users\Joshu\dev\ai-os-projects`, including `lsatu`.
- **Claude Code:** 73 memory files and 1.5 GB of chat history, across 51 projects. Settings and hooks are restored.
- **Codex:** signed in with ChatGPT. Config, memories and sessions are restored.
- **Logins:** GitHub (`gh`) and Google Workspace (`gws`) both work. Gmail answered a test call.
- **Superwhisper:** data restored, and the app starts.
- **Personal folders:** Desktop, Documents, Downloads and Pictures are merged in.
- **Apps:** every app from the old laptop's list is installed. The only failure was Windows App Runtime 1.5, an old helper library that newer versions replace.
- **Obsidian:** opens `C:\Users\Joshu\dev\ai-os` as its vault.
- **Backup:** the "Claude Code Backup" task is enabled and works. On 2026-11-12 the scheduled run finished with result 0, and every copy step returned a success code. Drive's `current\` copy is repaired, and its `wiki` has 47 files again. The first two runs, on 2026-11-11, quit after a few seconds. A full manual run that night completed, and the task has worked since.
- **Broken nested repo:** `ai-os\skill-audit\.git` is not a valid git repository, so git prints an error during the backup's commit step. This does not affect the backup. Fix it in a later session.

## For you to do (about 5 minutes)

1. **Sign in to Superwhisper** if it asks. Then check that your custom vocabulary is there.
2. **Sign in to the Claude desktop app, Proton Mail, Proton Pass and Proton Drive** the first time you open each one.
3. **Run this once in a terminal.** The command is blocked for the agent.
   ```bash
   git config --global core.autocrlf input
   ```
4. **Free up disk space (optional).** Google Drive for desktop cached about 290 GB during the download. In Drive's settings, open Preferences, then the gear icon, then clear the cache. Your files stay safe on Drive.

## Not done, on purpose

- **The `C:\Backups` folder (about 300 GB) was kept.** It holds the downloaded backup, the restored copy and a snapshot of the laptop from before the merge (`live-pre-merge-20261111`). Delete it only when you are happy with the laptop. It is the way back if anything looks wrong.
- **Duplicate projects folder.** App projects also exist in `ai-os\projects\` from the 2026-11-10 restore. CLAUDE.md says they belong in `..\ai-os-projects`, which is now complete. Nothing was deleted. Remove `ai-os\projects\` when you are ready.
- **Skill catalog index.** `check-skills.py` reports 45 problems: index entries and Claude-versus-Codex activation differences that came back with the old laptop's skills. All skills work. This is catalog upkeep for a later session.
- **Antigravity app data** was restored to `C:\Backups\RestoredCore\antigravity-*` but was not copied into place.

## If something looks wrong

- An older file showing up somewhere: the version from before the merge is in `C:\Backups\live-pre-merge-20261111`.
- A file missing: the full verified restore is in `C:\Backups\RestoredCore` and `C:\Backups\RestoredPersonal`.
- Logs: `C:\Backups\merge-log-20261111.txt` and `C:\Backups\undo-recent-log.txt`.
