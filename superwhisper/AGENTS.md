# superwhisper/ — Joshua's dictation setup

This folder is the source of truth for Superwhisper on the Windows laptop. Edit here, run the sync, restart the app. Never hand-edit the app's JSON.

## Files

| File | What it is |
|---|---|
| `vocabulary.md` | The short hand-listed hint list (~40). Exactly what is sent; nothing is added automatically. One stub note per term in `vocabulary/`. |
| `replacements.md` | Heard → wanted table. Deterministic, case-insensitive. This is where mis-hearings go. |
| `modes/<key>.md` | One mode each: frontmatter is the config, body is the prompt, `## Examples` are appended to the prompt text (see rule 7). |
| `sync.py` | Pushes all of the above into the app. `--check` shows the diff without writing. Backs up first. |
| `scan.py` | Scans every transcript for mis-heard known terms, rules that stopped firing, and new candidates. Writes `research/SCAN-<date>.md`. |
| `research/` | The 2026-09-11 customization report, the source list, and dated scans. Read the report before changing a prompt. |

Raw evidence (docs crawl, community pages, searches) is in `raw/sources/superwhisper/research-2026-09-11/`. Transcript exports are in `raw/sources/superwhisper/`.

## How Joshua asks for changes

- "add X to my dictionary" or "save the word X" → add to `vocabulary.md` only if the model actually mis-hears it; otherwise it belongs in `replacements.md` as a fix for the specific mis-hearing. Ask nothing; run `python sync.py --restart`, which relaunches the app silently in the background (Joshua only ever presses Ctrl+Space; never open Settings for him unless asked), then report the loaded counts.
- "replace X with Y" / "X should always be Y" → a row in `replacements.md`. Lowercase the heard side; matching is case-insensitive.
- "make a mode for ..." → a new `modes/<key>.md` copied from the closest existing one. Keep the "not an assistant" block in any mode whose output goes to an AI agent.
- Mid-session corrections arrive as one-liners ("Blinder View -> Blind review"). Apply immediately; do not batch them for later.

## Rules that cost a session to learn

1. **Check the active shell boundary before writing app data.** Claude Desktop redirects writes to `%LOCALAPPDATA%` into `AppData\Local\Packages\Claude_...\LocalCache\`; Codex may not. `sync.py` already uses `\\localhost\C$\...` so both runtimes reach the real app data. Use that path for any manual read or write too.
2. **Never launch Superwhisper directly from an agent shell.** It can spawn a second instance whose tray icon and settings window do not work. Ask Joshua to quit from the tray and reopen. If it must be done headlessly, use a Task Scheduler task (`Register-ScheduledTask` + `Start-ScheduledTask`), which runs outside the agent process.
3. **The app reads config only at launch.** A sync is not live until the app restarts. Tell him every time.
4. **Settings window.** Closing it hides it; relaunching the exe does not bring it back. Open it with `superwhisper://settings` (the "Superwhisper Settings" shortcut on his Desktop does this) or the tray icon.
5. **Model IDs.** The picker in the app is the only truthful list; the website and docs lag it. Proven by recordings: `sv-1` S1-Voice, `sl-1` S1-Language, `sw-claude-4p5-sonnet` Sonnet 4.5, `claude-sonnet-5` Sonnet 5 (newer models use plain IDs without the `sw-` prefix). To learn a new ID: Joshua picks it in the app, then read `modes/<key>.json` `languageModelID` and the latest `recording.language_model_key` in the sqlite. Never assert what is or is not offered without one of those two.
6. **Prompt examples cannot be written from outside the app.** A mode with a non-empty `promptExamples` list is silently dropped from `modeKeys` at launch (verified 2026-09-11). `sync.py` folds `## Examples` into the prompt text instead. If Joshua adds examples in the UI, leave them; the sync only touches modes whose files are in `modes/`.
7. **Verify a load, not a write.** After a restart, read `settings.json` `modeKeys`: the app rewrites it and drops any mode it rejected. That is the only trustworthy check.
8. **Vocabulary stays short (~40).** On 2026-09-11 it was pushed to 654 (auto-adding every replacement target) and transcription got noticeably worse within the hour; Joshua reversed it the same evening. Replacement targets are never auto-added. Mis-hearings go in `replacements.md`, which costs nothing in accuracy.

9. **No sync to the iPhone yet (checked 2026-09-12).** FileSync is Mac-only; the Windows docs page (`/docs/get-started/windows`) lists it as "still in development for Windows", the iOS page says modes and vocabulary "don't sync from your Mac or PC yet", and the Windows app resets `filesyncEnabled` to false at launch. The phone is kept in step by paste: the Super mode instructions and the vocabulary live on the artifact "Superwhisper on iPhone" (https://claude.ai/code/artifact/63400afd-4f6c-4139-ba82-461de066d544); republish it whenever `modes/super.md` or `vocabulary.md` changes. Re-check the Windows page after each app update.

## Where the app keeps things

`C:\Users\Joshu\AppData\Local\com.superwhisper.app\`
`settings\settings.json` (vocabulary, replacements, modeKeys) · `modes\*.json` · `preferences.json` (shortcuts, automaticUpdates, activeMode) · `recordings\<id>\meta.json` + `Output.wav` (every dictation, kept forever) · `database\superwhisper.sqlite` (history index).

Exe: `C:\Users\Joshu\AppData\Local\superwhisper\Superwhisper.exe` (reinstalled there 2026-09-11; the old copy under the Claude package folder is dead weight).

## Mode set (2026-09-11)

| Mode | Model | Use |
|---|---|---|
| Claude Code | S1-Language | Instructions to an agent. Keeps every detail, never answers. |
| Student Email | S1-Language | Finished email in his voice, per `wiki/teaching-voice.md`. |
| Student Message | S1-Language | Short in-platform message or drill feedback. Coaching register. |
| Lesson Notes | S1-Language | Spoken teaching → notes with the reasoning intact. |
| Vault Note | S1-Language | Thinking out loud → Obsidian note, wiki-links, absolute dates. |
| Consult Notes | S1-Language | Post-consultation debrief → structured record + follow-ups. |
| Rewrite | S1-Language | Select text, say what to do to it. |
| Message | S1-Language | Texts and DMs, light cleanup. |
| Verbatim | none | Raw transcript. |
| Session | none | Record a live session, nothing pasted. |
| Super | S1-Language | His original generic mode, kept as fallback. |

Switch with Ctrl+Shift+M, or `superwhisper://mode?key=<key>`. Per-mode hotkeys are set in the app (Modes → mode → Keyboard shortcut) and are not managed here yet.

## Skill

The `superwhisper` skill is the runbook: word/correction → variants → `sync.py --restart`; modes; `scan.py`. Claude uses `skills/claude/superwhisper/SKILL.md`; Codex uses its activated Codex counterpart. Invoke it for any Superwhisper request.

## Related

`wiki/SUPERWHISPER-DICTIONARY.md` is the human-readable ledger and points here. Memory note: `superwhisper-settings-location`.
