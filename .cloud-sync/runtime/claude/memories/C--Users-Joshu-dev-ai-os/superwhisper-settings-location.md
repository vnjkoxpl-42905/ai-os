---
name: superwhisper-settings-location
description: Superwhisper (Windows) config lives in AppData\Local\com.superwhisper.app, but Claude Desktop's MSIX sandbox redirects writes there; use the UNC bypass path and never launch the app from the shell.
metadata:
  type: reference
---

Superwhisper on Windows (Tauri app). Real config: `C:\Users\Joshu\AppData\Local\com.superwhisper.app\`
- `settings\settings.json`: `replacements: [{id, original, with}]` (case-insensitive match), `vocabulary: [str]` (keep ~40; on 2026-09-11 a 654-entry list made transcription noticeably worse within the hour and Joshua reversed it; never auto-add replacement targets), `modeKeys`
- `modes\<key>.json` (prompt, voiceModelID `sv-1`, languageModelID e.g. `sl-1`, `sw-claude-4p5-sonnet`)
- `preferences.json` (shortcuts, automaticUpdates)

**Trap (cost a full session on 2026-09-11):** Claude Desktop is an MSIX package, so from its shell any write under `AppData\Local` is redirected to `AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Local\...`. The real app never sees it, and reads look "verified" because you read your own shadow copy.
- Write/read via `//localhost/C$/Users/Joshu/AppData/Local/com.superwhisper.app/...` (UNC bypasses virtualization).
- Never `Start-Process Superwhisper.exe` from the shell: it spawns a sandboxed second instance whose tray icon/settings window won't work. Ask Joshua to quit and reopen the app (right-click tray → Quit) after a config change; the app only reads config at launch.

Source of truth: `dev/ai-os/superwhisper/` (CLAUDE.md, vocabulary.md, replacements.md, modes/*.md, sync.py). Ledger: `wiki/SUPERWHISPER-DICTIONARY.md`.

**2026-09-11 additions.** (1) A mode file with a non-empty `promptExamples` list is silently dropped from `modeKeys` at launch; fold examples into the prompt text. (2) The only trustworthy check is reading `modeKeys` after a restart: the app rewrites it. (3) Restart headlessly with a Task Scheduler task, never Start-Process. (4) Joshua chose S1-Language for all modes over Claude/GPT.
