---
type: system
subject: Windows machine profile — Dell 15 DC15250
updated: 2026-09-07
aliases: [dell, this-machine, windows-box]
---

# Windows machine profile

Replaces the MacBook (`/Users/joshuaf/...`). Written 2026-09-07 during the Dell rebuild.
Supersedes the brew-based assumptions in [[tooling]], which describes the dead Mac.

## Hardware

| | |
|---|---|
| Model | Dell 15 DC15250 (laptop) |
| Service Tag | 9XS1FK4 |
| BIOS | 1.5.1 |
| CPU | Intel Core i5-1334U — 13th gen, 10 cores (2 performance + 8 efficiency), 12 threads |
| RAM | 15.7 GB |
| GPU | Intel UHD Graphics (integrated only — no discrete GPU) |
| Disk | Samsung 512 GB NVMe — 453 GB usable, 337 GB free |
| OS | Windows 11 Home, build 26200 |

The `U` in i5-1334U means low-power (~15 W). This is a thin-and-light office laptop, not a
workstation. Fine for editing, browsing, Node builds. Slow for anything sustained.

## How this differs from the MacBook

Ranked by how much it actually changes daily work.

### 1. No Apple Silicon — local AI is effectively gone
The Mac had unified memory and a Neural Engine. This has integrated Intel UHD graphics, no
CUDA, no Metal. Local Whisper transcription, local LLMs, on-device ML: all either impossible
or so slow they are not worth attempting. **Anything that used to run locally must move to a
cloud API.** `ffmpeg` still works for audio *manipulation*; it is the *transcription* that lost
its accelerator.

### 2. No Homebrew
`brew install X` is now `winget install X`. There is no `/usr/local/bin`. Binaries scatter:

| Installed by | Lands in |
|---|---|
| winget | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\` |
| MSI / .exe installers | `C:\Program Files\` |
| `npm i -g` | `%APPDATA%\npm` |

### 3. PATH is manual and fragile — this is the big one
On the Mac, brew symlinked everything into a directory already on PATH. On Windows every
installer decides for itself, and some do not touch PATH at all. **This is what made the laptop
look broken on 2026-09-06:** Node and `gh` were installed the whole time, just invisible.
When a tool "is not installed", check PATH before reinstalling. Backup at `~/dev/PATH-backup.txt`.

### 4. No native Unix userland
Git Bash is an emulation layer, not a real system. No `launchd`, no `cron`, no `/usr/local`.
Scheduled jobs use Task Scheduler. Old vault paths beginning `/Users/joshuaf/` are dead.

### 5. Line endings — CRLF vs LF
Windows checks out CRLF; the repo stores LF. Already produced a warning on
`SectionLibraryLaunch.test.tsx`. Left unset this creates phantom whole-file diffs.
**Unresolved — needs `git config --global core.autocrlf input`.** Blocked by the
`Bash(git config --global*)` deny rule, so Joshua must run it himself.

### 6. Symlinks need permission
Developer Mode or admin. Some Node tooling assumes them silently.

### 7. Credentials
Keychain → Windows Credential Manager. `gh` and `gws` store tokens differently than on the Mac;
Mac credential exports do not transfer.

### 8. Automation
No AppleScript, Automator, or Shortcuts. Power Automate is installed as the rough equivalent.

## WSL — recommended, currently blocked

WSL2 would restore most Mac terminal muscle memory (real Linux, real `/usr/local/bin`, apt).

**It cannot be installed right now: virtualization is disabled in firmware.**
Fix: reboot → tap `F2` at the Dell logo → enable Virtualization / VT-x (and VT-d) → save →
then run `wsl --install`.

## Installed software

**Dev:** Node 24.19.0, npm 11.17.0, pnpm 12.3.4, Python 3.12.10, uv 0.12.10, Deno 2.9.6,
Git 2.55.0.5, GitHub CLI 2.100.0, jq 1.8.2, SQLite 3.53.4, ffmpeg 9.0.1, yt-dlp 2026.07.04,
Windows Terminal 1.24, Playwright (chromium + firefox)

**Agents:** Claude Desktop 1.46388.4.0, Claude Code CLI 2.1.263, Codex CLI 0.153.4,
ChatGPT desktop 26.901, Microsoft Copilot

**Work:** Microsoft 365 (en-us, es-es, fr-fr, pt-br), Outlook, Teams, OneNote, OneDrive,
Obsidian 1.13.7, Power Automate

**Browsers:** Chrome 152, Edge 152

**Dell OEM:** SupportAssist, Optimizer, Core Services, Connected Service Delivery

## Gaps and flags

- **No code editor installed.** No VS Code, no Cursor. `~/dev/cli` contains a `.vscode/` folder
  expecting one.
- **McAfee + WebAdvisor are installed.** Real-time scanning slows `npm install` noticeably and
  can quarantine scripts. Consider removing in favour of Windows Defender.
- **Two installers downloaded but never run:** `superwhisper_1.6.5_x64-setup.exe` (dictation —
  likely wanted, given how much is dictated) and `Antigravity-x64.exe`.
- **`gws` has no auth** — `auth_method: none`, no `client_secret.json`. 1,127 skill references
  depend on it. Nothing in the backup restores this; it must be rebuilt in Google Cloud Console.
- **`lsatu` is a shallow clone** (depth 1). Needs `git fetch --unshallow` after `gh auth login`.
- **`opencli` deliberately not installed** — write access to real social accounts. See [[tooling]].
