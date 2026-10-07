# Current replacement-laptop workflow (2026-10-07)

Use [new-machine-README.md](new-machine-README.md) for this Windows laptop. The new workflow creates preserved generations, checks files and archive dependencies, and uploads through gws to the private [Replacement Laptop Backups](https://drive.google.com/drive/folders/1vQ_Xm9GqDd7SlahE4sp6znQKiYkW8xOe) folder. Latest core 20261007-153457 and personal 20261007-153621 and all their archive dependencies are cloud verified. Private Laptop Backup - Replacement passed its actual scheduled run with exit code 0; it runs daily at 19:00 Toronto and at logon. Follow the published [restore guide](https://drive.google.com/file/d/1SNwtDER_GybOqU5Yi7YHOo914jyYhZ5z/view) and its index; newest timestamp alone does not identify both required scopes.

Claude Code is authenticated and tested. Its easy launcher is `C:\Users\Joshu\Documents\Claude\Start Claude Second Brain.cmd`; the vault is `C:\Users\Joshu\dev\ai-os`. Joshua uses Claude Code only, so desktop sign-in is not required. GitHub and Google Drive CLI authentication are verified. Codex remains open; the stuck all-or-nothing recovery task is disabled. Do not run `Finish-Restore.cmd` or the old mirror workflow below as part of this recovery.

The following section describes the former laptop's legacy setup, not verified behavior on this replacement laptop. It is retained as historical documentation. The legacy scripts mirror/prune data and are not the active recovery workflow.

# Legacy Claude Code backup: how it worked

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
| `ai-os\` | `~\dev\ai-os` | the whole vault, including code repos (minus `node_modules` and `.venv`) |
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
