# Claude Code backup: how it works

Every 10 minutes (and at logon) a Windows Scheduled Task named **Claude Code Backup** runs
`backup.ps1`, which mirrors this laptop's whole Claude Code setup into
`G:\My Drive\CLAUDE-CODE-BACKUP - START HERE\`. Google Drive uploads it from there.

What gets copied (Drive folder `current\`):

| Drive folder | From | Holds |
|---|---|---|
| `claude\` | `~\.claude` | every chat transcript, skill, plugin, settings, memory |
| `claude.json` | `~\.claude.json` | MCP servers, OAuth |
| `codex\` | `~\.codex` | Codex CLI config + auth |
| `superwhisper\` | `%LOCALAPPDATA%\Superwhisper` | modes, vocabulary, settings |
| `ai-os\` | `~\dev\ai-os` | the whole vault, including code repos (minus `node_modules`) |
| `dotfiles\` | `.gitconfig`, `gh`, `gws`, `.config` | CLI logins and config |
| `machine-info.json` | | which machine, when, which paths (restore uses this) |

Secrets are included on purpose (decision 2026-09-11): the Drive is private and the goal is a
zero-effort restore.

Also: the vault auto-commits and pushes to the private GitHub repo `vnjkoxpl-42905/ai-os`
(history; `projects/`, `raw/`, `.env` stay out of GitHub, they are on Drive). And once a day a
zip lands in `snapshots\`, 30 kept, so one bad sync can never overwrite the only good copy.

## Restore on a new laptop
See `README - START HERE.md` in the Drive folder. Short version: sign in to Google Drive,
install Git + Node + Claude Code, run `restore.ps1` (Windows) or `restore.sh` (Mac).

## Check it is running
`LAST-BACKUP.txt` in the Drive folder shows the time of the last successful run.
Logs: `logs\backup-YYYY-MM-DD.log`. Run by hand: `powershell -ExecutionPolicy Bypass -File backup.ps1`.
Re-register the task: `install-task.ps1`.
