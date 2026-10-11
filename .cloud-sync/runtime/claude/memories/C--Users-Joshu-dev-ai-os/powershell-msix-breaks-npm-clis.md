---
name: powershell-msix-breaks-npm-clis
description: "The MSIX/Store build of PowerShell 7 cannot see AppData\\Roaming\\npm, silently breaking claude/codex/firecrawl/pnpm — install the MSI build instead."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0b4c747a-84ce-4095-8c2c-9bb1b7ec4ec8
  modified: 2026-10-11T01:47:48.578Z
---

On Windows, `winget install Microsoft.PowerShell --scope user` installs the
**MSIX/Store** build (lands in `C:\Program Files\WindowsApps\...`). That build
runs with AppData virtualization and **cannot see `C:\Users\<user>\AppData\Roaming\npm`**.

Consequence: `claude`, `codex`, `firecrawl`, and `pnpm` — every npm-global CLI —
fail to resolve in that shell, with no error explaining why. `Test-Path` on the
npm global dir returns `False` from MSIX pwsh and `True` from unpackaged
Windows PowerShell 5.1. That contrast is the fastest way to confirm the diagnosis.

**Fix:** uninstall the MSIX package, then install the MSI from GitHub releases
(`PowerShell-<ver>-win-x64.msi`) via elevated `msiexec /i ... /qn /norestart`.
It installs to `C:\Program Files\PowerShell\7`, which is also the path Windows
Terminal's well-known PowerShell profile GUID
`{574e775e-4f2a-5b96-ac1e-a2962a402336}` expects.

`winget --scope machine` refuses without admin, and `winget show` reports the
installer type as `msix` — so there is no winget-only path to the MSI.

Verified 2026-09-07 on the Dell 15 DC15250 during [[ai-os-vault-location]] setup.

**Same trap, Windows Terminal and Herdr (verified 2026-10-10 on LAPTOP-LE9A083P).**
Windows Terminal is also a Store app. A Herdr server started under it
(`WindowsTerminal.exe` is its ancestor), and every pane, sees
`AppData\Roaming\npm` as empty even though the PATH entry is present and the
files exist on disk. `codex`, `firecrawl` and `kling` vanished inside Herdr;
`claude` (`.local\bin`) and `gws` (recovery-toolchain) survived because they
live outside AppData. The fix is not an MSI this time. Install npm CLIs with
`npm install -g --prefix C:\Users\Joshu\dev\tools\node <pkg>` and keep that
folder first on the user PATH. The Herdr desktop shortcut launcher
(`C:\Users\Joshu\.herdr\launch-herdr.ps1`) rebuilds PATH from the registry.
Check the first step of any "tool missing in Herdr" report with `Test-Path` on
the npm shim from inside a pane.
