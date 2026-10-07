---
name: claude-code-backup-to-drive
description: Full Claude Code + vault backup runs every 10 min to G:\My Drive\CLAUDE-CODE-BACKUP - START HERE; restore scripts + private GitHub mirror of the vault.
metadata:
  type: project
---

Since 2026-09-12 a scheduled task "Claude Code Backup" mirrors ~/.claude, ~/.claude.json, ~/.codex, Superwhisper, and the whole vault (minus node_modules/.venv) into `G:\My Drive\CLAUDE-CODE-BACKUP - START HERE\current\` every 10 minutes, keeps 30 daily zips, and auto-commits the vault to private GitHub `vnjkoxpl-42905/ai-os` (projects/, raw/, .env ignored). Scripts live in `setup/backup/`. Secrets are included on Drive by Joshua's explicit decision.

**Why:** he lost ~6 weeks of work when the previous laptop died and wants a one-script restore on a new machine.

**How to apply:** never delete or rename that Drive folder; when adding a new dotfile or app config that matters, add it to `backup.ps1`. `restore.sh` (Mac) has never been run. The vault is now a git repo: commits happen automatically, so don't commit by hand unless asked. See [[branch-per-session-in-lsatu]].
