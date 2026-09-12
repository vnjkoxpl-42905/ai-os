# Machine setup — Dell 15 DC15250

**Date:** 2026-09-07
**Box:** Dell 15 DC15250 · Intel Core i5-1334U · 16 GB RAM · 512 GB NVMe (340 GB free)
**OS:** Windows 11 Home 26200 · installed 2026-09-05
**Replaces:** 2020 Intel MacBook Pro (dead)

---

## What was already here

The box was not bare. A prior session had installed: Git 2.55, Node 24.19 LTS,
npm 11.17, pnpm 12.3.4, Python 3.12.10, uv, Deno 2.9.6, Rust 1.98.1, gh 2.100,
ffmpeg 9.0.1, yt-dlp, jq, SQLite, Google Cloud SDK, Obsidian 1.13.7, Windows
Terminal, Claude Code 2.1.263, Codex 0.153.4, firecrawl-cli 1.23.3, and `gws`.

The vault at `C:\Users\Joshu\dev\ai-os` was intact — 10,941 files, 2.5 GB, with
the full skill catalog present (179 Claude + 154 Codex, matching [[CLAUDE]]).

## What was missing or broken

Three things mattered more than the missing packages.

**Git had no global config at all.** No `user.name`, no `user.email`, no
`init.defaultBranch`. Every commit on this machine would have been authored by
nobody.

**Obsidian was pointed at the wrong vault.** `obsidian.json` registered
`C:\Users\Joshu\OneDrive\Desktop\OS` — a 45-file, 202 KB scaffold. The real
10,941-file vault was never registered. This is exactly the failure the
`ai-os-vault-location` memory warns about. The `obsidian` CLI (`search`,
`backlinks`, `read`) would have been reading the scaffold.

**No editor.** No VS Code, no Cursor, nothing.

## What got installed

| Category | Tools |
|---|---|
| Shell | PowerShell 7.6.5 (MSI — see the trap below), Oh My Posh 31.2 |
| Editor | VS Code 1.136.1 + 18 extensions |
| Search / files | ripgrep 15.2, fd 10.5, bat 0.26, fzf 0.74, eza 0.23, zoxide 0.10 |
| Git | delta 0.19.2 (side-by-side diffs) |
| Runtimes | Go 1.27.0, Bun 1.4.2 |
| Utility | 7-Zip 26.02, PowerToys 0.101, JetBrainsMono Nerd Font |
| PS modules | Terminal-Icons, PSFzf, PSReadLine 2.4.5 |

Runtime upgrades: VCRedist x64/x86, .NET Desktop Runtime 8, ASP.NET Core 8.
`WindowsAppRuntime.1.5` (1.5.8 → 1.5.9) failed with "package in use" — a point
release, not worth chasing.

## The PowerShell MSIX trap — worth remembering

Installing PowerShell 7 with `winget install Microsoft.PowerShell --scope user`
gets you the **MSIX/Store** build, which runs with AppData virtualization and
**cannot see `AppData\Roaming\npm`**. In that shell, `claude`, `codex`,
`firecrawl`, and `pnpm` all silently fail to resolve — the entire CLI workflow,
gone, in the shell being set up as the default.

Confirmed by contrast: unpackaged Windows PowerShell 5.1 resolved
`claude → AppData\Roaming\npm\claude.ps1` fine; MSIX pwsh returned
`Test-Path` **False** on the same directory.

Fix: uninstall the MSIX build, install the MSI from GitHub releases
(`PowerShell-7.6.5-win-x64.msi`) so it lands in `C:\Program Files\PowerShell\7`.
Requires elevation. See [[POWERSHELL-MSIX-BREAKS-NPM-CLIS]].

## Files written

| File | Purpose |
|---|---|
| `~/.gitconfig` | Identity, delta pager, rebase-pull, autoSetupRemote, `gh` credential helper, 9 aliases |
| `~/OneDrive/Documents/PowerShell/profile.ps1` | Prompt, history prediction, fzf/zoxide, eza+bat aliases, git shortcuts, `aios`/`lsatu`/`wiki` jumps |
| Windows Terminal `settings.json` | pwsh default, Catppuccin Mocha, Nerd Font, pane keybinds |
| VS Code `settings.json` | 95 keys — format-on-save, per-language formatters, pwsh terminal |
| `ai-os/.obsidian/app.json` | **Excludes `raw/`, `projects/`, `graph-imports/`, `tmp/`, `archive/` from indexing** — without this Obsidian crawls 2.5 GB |

## Still needs your hand

Two scripts in this folder need elevation, and both remove or relax something,
so neither was run unattended:

- `01-defender-exclusions.ps1` — the single largest speed win available on this
  box. Defender scanning every file in a `node_modules` tree is the main reason
  installs and Vite builds drag.
- `02-remove-bloatware.ps1` — McAfee and the Dell agents were holding ~800 MB
  while the machine had only 2.7 GB of 16 GB free. Read the header; it explains
  what each component is and why Waves MaxxAudio was deliberately left alone.

Also open:

- **WSL is not installed.** `wsl --install` (admin + reboot). Nothing in the
  current stack needs it — Node, Vite, Supabase, and Deno all run native.
- **The vault is not under version control.** 10,941 files of second brain with
  no history. Worth doing, but needs a `.gitignore` that excludes `raw/` (1.2 GB),
  `projects/` (own repos), and the root `.env` before a first commit.
- **`OneDrive\Desktop\OS`** — the 45-file scaffold. Deregistered from Obsidian,
  not deleted.

Related: [[CLAUDE]] · [[tasks]] · [[hot]]
