# Shared Windows command line tools

Last verified: 2026-10-08 on Joshua's Windows laptop. This guide is the shared machine reference for Codex, Claude Code, and Antigravity. The tools are installed once for the Windows user and are not duplicated inside each AI runtime.

## Installed tools and locations

WinGet package directories are versioned/managed by WinGet. Prefer calling the command by name through PATH. These paths confirm where the current packages live; a later package update may change a folder name.

| Command | Current version | Current executable |
|---|---|---|
| `uv` | 0.12.23 | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\astral-sh.uv_Microsoft.Winget.Source_8wekyb3d8bbwe\uv.exe` |
| `yt-dlp` | 2026.08.19 | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe` |
| `ffmpeg`, `ffprobe`, `ffplay` | N-126374-g089a48eb36-20260831 | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-N-126374-g089a48eb36-win64-gpl\bin\` |
| `deno` | 2.9.7 | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\DenoLand.Deno_Microsoft.Winget.Source_8wekyb3d8bbwe\deno.exe` |

### Python (added 2026-10-12)

| Command | Version | Notes |
|---|---|---|
| `py` | launcher 3.15.0, default `3.15` | Newest. Python 3.15.0 (released 2026-10-09) from python.org, installer signature checked (Python Software Foundation), per-user at `%LOCALAPPDATA%\Programs\Python\Python315`. Has `requests` and `youtube-transcript-api` for the vault scripts. `py -3.12` still works. |
| `python`, `pip` | 3.15.0 | Moved to 3.15 on 2026-10-12 at Joshua's request: `Python315` and `Python315\Scripts` are first among the Python entries on the user PATH. All 50 packages 3.12 had were installed on 3.15 (19 key ones import, `pip check` clean), and the `accommodations-email` send script passed a dry run as plain `python`. Python 3.12.10 stays installed and is reachable as `py -3.12`. |
| `python3` | Microsoft Store stub | Prints an install hint and does nothing. `check-skills.sh` already skips it. |

The saved Windows user PATH already contains these package directories. All four commands were verified by name after reloading PATH. The original failure was a stale PATH inherited by already-running Codex, not a missing install. Restarting an AI application gives its new terminals the refreshed environment.

## Check access in any runtime

Run in that runtime's PowerShell terminal:

```powershell
Get-Command uv, yt-dlp, ffmpeg, ffprobe, ffplay, deno -ErrorAction SilentlyContinue |
  Select-Object Name, Source
uv --version
yt-dlp --version
ffmpeg -version | Select-Object -First 1
ffprobe -version | Select-Object -First 1
deno --version | Select-Object -First 1
```

If the commands are installed but are not found, first refresh only the current PowerShell process from the saved Windows PATH:

```powershell
$machinePath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$env:Path = "$userPath;$machinePath"
Get-Command uv, yt-dlp, ffmpeg, ffprobe, ffplay, deno
```

If that works, restart the affected AI application so its future terminals inherit the environment. Do not reinstall the tools or change persistent PATH just because one already-open shell cannot see them. If the refreshed shell still cannot find a command, inspect `winget list --id <package-id> --exact` and the executable at the table's current package path before making changes.

## What each tool is for

- `uv` creates and manages isolated Python project environments and dependencies. Use `uv add package-name` from the intended code project when that project should depend on a library; do not install every library globally. Use `uv run ...` to run a command in that project environment.
- `yt-dlp` retrieves available video metadata and captions, and can retrieve media when specifically needed. For a first caption check, use `yt-dlp --list-subs <URL>`; use `--skip-download` when retrieving subtitles only. Do not assume a website exposes captions or that a successful install grants account access.
- `ffmpeg` converts, trims, extracts and processes audio/video. `ffprobe` inspects media metadata. `ffplay` plays media for inspection.
- `deno` is a JavaScript/TypeScript runtime. yt-dlp detects it as its JavaScript challenge runtime for supported YouTube extraction; ordinary tasks do not need to invoke it directly.

## Python library scope

Python packages installed in one interpreter are not automatically shared with the others. Codex's managed Python bundle includes `pypdf`, `pdfplumber`, `Pillow`, and `lxml`; the regular user Python 3.12 includes `requests`. Claude Code and Antigravity projects should check their own interpreter and project lockfile. Add only required missing packages to that project's isolated environment with uv. Do not modify Codex's managed runtime or put virtual environments in the Obsidian vault.

## Instructions for the three AI tools

- **Codex:** repository rules are in `AGENTS.md`. Use the shared CLI paths and PATH recovery above; restart Codex when its inherited PATH is stale.
- **Claude Code:** repository rules are in `CLAUDE.md`. Use the same user-installed executables; project Python dependencies belong in that project's environment.
- **Antigravity:** workspace rules are in `GEMINI.md` and `AGENTS.md`. Use the same user-installed executables; if it cannot see them, refresh/restart its terminal/application before considering an install.

These tools are shared at the Windows user level. Do not create copies in `.agents/`, `.claude/`, `.gemini/`, or inside the vault. Per-project Python packages remain isolated in each project's environment.
