# CLAUDE CODE BACKUP: START HERE

**This folder is the one to use.** It is an automatic copy of Joshua's full Claude Code setup,
refreshed every 10 minutes from the current laptop. Check `LAST-BACKUP.txt` for the time of the
last copy. The older `_OLD AI-OS ...` folder on this Drive is out of date; do not use it.

## Setting up a new laptop (about 20 minutes, most of it downloading)

1. Sign in to **Google Drive for Desktop** with contact@aspiringattorneys.com and wait until this
   folder shows a green check (fully synced).
2. Install **Git**, **Node.js (LTS)**, then run `npm install -g @anthropic-ai/claude-code`.
   Also install the Claude desktop app, Obsidian, and Superwhisper if you use them.
3. Run the restore script:
   - **Windows:** right-click `restore.ps1` > Run with PowerShell
     (or: `powershell -ExecutionPolicy Bypass -File "G:\My Drive\CLAUDE-CODE-BACKUP - START HERE\restore.ps1"`)
   - **Mac:** open Terminal, `bash "<this folder>/restore.sh"`
4. Open Claude Code in `~/dev/ai-os` and run `claude --resume`. Your chats, skills, memory,
   settings, and vault are all there. Sign in once if `claude`, `gh`, or `gws` ask.
5. On Windows the restore also re-registers the 10-minute backup, so the new laptop keeps this
   folder current from then on. On Mac see `ai-os/setup/backup/README.md`.

## What is in here
- `current\` : the live mirror (chats, skills, plugins, config, Codex, Superwhisper, vault)
- `snapshots\` : one zip per day, last 30 days, in case you need an older state
- `logs\` : one log per day from the backup task
- `restore.ps1` / `restore.sh` : the scripts from step 3
- `LAST-BACKUP.txt` : when the last copy ran

The vault also lives in the private GitHub repo `vnjkoxpl-42905/ai-os` for history.
