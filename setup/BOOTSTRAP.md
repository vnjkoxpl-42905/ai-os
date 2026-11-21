# Bootstrap a new machine (Claude Code, Codex, Antigravity)

Any agent that opens this folder on a machine that does not look set up reads this file
first and walks Joshua through it. Written 2026-11-01 from the laptop being returned.
The backup is a one-time upload to Drive, not a schedule. Detail and tooling:
`setup/backup/new-machine-README.md`.

## Is this machine already set up?

Set up means all of these exist: `~/.claude/projects/`, `~/.codex/`, `~/.gemini/`, and
`.env` in this folder. If any is missing, follow the steps. If all exist, stop.

## Exact setup being reproduced (captured 2026-11-01)

| Tool | Version | Where it lives |
|---|---|---|
| Claude Code | 2.1.309 | `~/.local/bin/claude` (native install) |
| Codex CLI | 0.162.1 | `~/dev/tools/node` (installed with `npm install --prefix`; first on user PATH) and `@openai/codex@0.162.1` global |
| Antigravity IDE | installed app | `~/AppData/Local/Programs/Antigravity IDE`, CLI `agy` in `~/AppData/Local/agy/bin` |
| Node | 26.8.1 | system |
| Python | 3.12 (task runner) and 3.15 | `~/AppData/Local/Programs/Python/` |
| Git for Windows | 2.55.0 | `CLAUDE_CODE_GIT_BASH_PATH` must point at its `bin/bash.exe` |
| GitHub CLI | 2.102.0 | account `vnjkoxpl-42905` |
| Google Workspace CLI | `@googleworkspace/cli@0.22.5` | GCP project `ai-os-joshua`, account contact@aspiringattorneys.com |
| Other npm globals | `firecrawl-cli@1.26.3`, `@klingai/cli-global@0.2.1` | `~/AppData/Roaming/npm` |
| Also on PATH | uv, yt-dlp, ffmpeg, deno, jq, Stripe CLI, Go, Cargo | see `references/ai-workspace/windows-cli-toolchain.md` |

User environment variables to recreate: `CLAUDE_CODE_GIT_BASH_PATH`, `GHIDRA_INSTALL_DIR`,
`GOPATH`, `API_KEY_21ST`. Values are in the backup's `system/machine-info.json`; review the
paths, do not replace the new PATH wholesale.

The Store build of PowerShell cannot see `AppData\Roaming\npm`, so install npm CLIs with
`npm install --prefix %USERPROFILE%\dev\tools\node <pkg>@<version>` and keep that folder
first on the user PATH.

## Steps

1. **Install base tools:** Git for Windows, Python 3.12, Node, `gh`. Run `gh auth login`.
2. **Vault from GitHub:** `gh repo clone vnjkoxpl-42905/ai-os ~/dev/ai-os`. GitHub does not
   hold `.env`, `raw/`, `projects/` or credentials. They come from Drive in step 4.
3. **Install `gws` and sign in** as contact@aspiringattorneys.com, so Drive can be read.
4. **Pull the backup from Drive.** Folder "Replacement Laptop Backups"
   (id `1vQ_Xm9GqDd7SlahE4sp6znQKiYkW8xOe`). Read the newest `Restore-Guide-*.md` and
   `Restore-Index-*.json` in it: they name the exact core and personal generations and
   every dependency generation to download. Keep generation folder names together in one
   parent folder. Restore each into a NEW folder:
   `python new-machine-restore.py --generation <gen> --output <new folder>`.
5. **Place files** from the restored folders (table below). Close the app first. Move any
   existing folder aside, never delete it.
6. **Install apps and CLIs** at the versions above: Claude Code, Codex, Antigravity IDE,
   Claude desktop app, Codex app, Obsidian, Superwhisper, Chrome.
7. **Sign in again** to Claude Code, Codex, Antigravity, `gh`, `gws`. Some logins are
   machine-bound and may not carry over.
8. **Resume.** Open `~/dev/ai-os` in the tool. Claude Code: `claude --resume`. Codex: resume
   from the app sidebar. Skills, memory, settings and chats are restored by step 5.
9. **Check:** `claude --version`, `codex --version`, `gh auth status`, `gws` login, then
   open one old chat in each tool.

## Where restored folders go

| Backup label | Destination |
|---|---|
| `ai-os` | `~/dev/ai-os` |
| `projects` | `~/dev/ai-os-projects` |
| `claude`, `codex`, `agents`, `gemini`, `antigravity-ide` | `~/.claude`, `~/.codex`, `~/.agents`, `~/.gemini`, `~/.antigravity-ide` |
| `config` | `~/.config` |
| `dotfiles/*` | `~/` (`.claude.json`, `.gitconfig`, `.npmrc`, `.bashrc`) |
| `codex-app`, `obsidian`, `vscode-user`, `gh`, `gws`, `antigravity-app`, `antigravity-ide-app`, `claude-desktop` | `~/AppData/Roaming/` as `Codex`, `obsidian`, `Code/User`, `gh`, `gws`, `Antigravity`, `Antigravity IDE`, `Claude` |
| `superwhisper` | `~/AppData/Local/com.superwhisper.app` |
| Documents, Downloads, Desktop, Pictures (personal scope) | same folders under `~/` |

A different Windows username means saved absolute paths need review.

## Known limits

A data backup, not a disk image. Apps, licences and machine-bound sessions are not
restorable. The restore index, not the newest timestamp, says which generations are
complete. Caches, `node_modules`, browser profiles and model downloads are excluded and
rebuild themselves.
