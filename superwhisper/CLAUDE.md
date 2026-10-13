# superwhisper/ — Joshua's dictation setup

This folder is the source of truth for Superwhisper on the Windows laptop. Edit here, run the sync, restart the app. Never hand-edit the app's JSON.

## Files

| File | What it is |
|---|---|
| `vocabulary.md` | The short hand-listed hint list (~40). Exactly what is sent; nothing is added automatically. One stub note per term in `vocabulary/`. |
| `replacements.md` | Heard → wanted table. Deterministic, case-insensitive. This is where mis-hearings go. |
| `shared.md` | The glossary and house rules every AI mode gets. `sync.py` prepends its step-zero block and appends its house rules/glossary before examples. Edit once, every mode updates (2026-09-26). Voice-only modes have no AI step and are untouched. |
| `modes/<key>.md` | One mode each: frontmatter is the config, body is the prompt, `## Examples` are appended to the prompt text (see rule 7). |
| `sw.py` | The terminal CLI (`sw search / last / stats / add / vocab / rules / export / scan / sync / mode`). Superwhisper's own CLI is macOS-only, so this does the same jobs against the same local files. Launcher: `dev/tools/bin/sw.cmd`, on PATH. |
| `sync.py` | Pushes all of the above into the app. `--check` shows the diff without writing. Backs up first. |
| `scan.py` | Scans every transcript for mis-heard known terms, rules that stopped firing, and new candidates. Writes `research/SCAN-<date>.md`. |
| `hallucinations.py` | Counts invented text (silence fillers, loops, too many words for the clip length) and whether it was pasted. Writes `research/HALLUCINATIONS-<date>.md`. Baseline 2026-10-12: 66 of 807 recordings in 7 days, 45 pasted. |
| `research/` | The 2026-09-11 customization report, the source list, and dated scans. Read the report before changing a prompt. |

Raw evidence (docs crawl, community pages, searches) is in `raw/sources/superwhisper/research-2026-09-11/`. Transcript exports are in `raw/sources/superwhisper/`.

## How Joshua asks for changes

- "add X to my dictionary" or "save the word X" → add to `vocabulary.md` only if the model actually mis-hears it; otherwise it belongs in `replacements.md` as a fix for the specific mis-hearing. Ask nothing; run `python sync.py --restart` to restart silently. Joshua uses Left Alt to toggle recording. Preserve it and read it back after restart. Never open Settings unless asked. Report the loaded counts.
- "replace X with Y" / "X should always be Y" → a row in `replacements.md`. Lowercase the heard side; matching is case-insensitive.
- "make a mode for ..." → a new `modes/<key>.md` copied from the closest existing one. Keep the "not an assistant" block in any mode whose output goes to an AI agent.
- Mid-session corrections arrive as one-liners ("Blinder View -> Blind review"). Apply immediately; do not batch them for later.

## Rules that cost a session to learn

1. **The Claude Desktop shell is sandboxed.** Writes to `%LOCALAPPDATA%` are redirected into `AppData\Local\Packages\Claude_...\LocalCache\`. Superwhisper never sees them, and reads look "verified" because you read your own shadow copy. `sync.py` writes through `\\localhost\C$\...`, which bypasses this. Use that path for any manual read too.
2. **Never launch Superwhisper directly from an agent shell.** It can spawn a second instance whose tray icon and settings window do not work. Ask Joshua to quit from the tray and reopen. If it must be done headlessly, use a Task Scheduler task (`Register-ScheduledTask` + `Start-ScheduledTask`), which runs outside the agent process.
3. **The app reads config only at launch.** A sync is not live until the app restarts. Tell him every time.
4. **Settings window.** Closing it hides it; relaunching the exe does not bring it back. Open it with `superwhisper://settings` (the "Superwhisper Settings" shortcut on his Desktop does this) or the tray icon.
5. **Model IDs.** The picker in the app is the only truthful list; the website and docs lag it. Proven by recordings: `sv-1` S1-Voice, `sl-1` S1-Language, `sw-claude-4p5-sonnet` Sonnet 4.5, `claude-sonnet-5` Sonnet 5 (newer models use plain IDs without the `sw-` prefix). To learn a new ID: Joshua picks it in the app, then read `modes/<key>.json` `languageModelID` and the latest `recording.language_model_key` in the sqlite. Never assert what is or is not offered without one of those two.
6. **Prompt examples cannot be written from outside the app.** A mode with a non-empty `promptExamples` list is silently dropped from `modeKeys` at launch (verified 2026-09-11). `sync.py` folds `## Examples` into the prompt text instead. If Joshua adds examples in the UI, leave them; the sync only touches modes whose files are in `modes/`.
7. **Verify a load, not a write.** After a restart, read `settings.json` `modeKeys`: the app rewrites it and drops any mode it rejected. That is the only trustworthy check.
8. **Vocabulary stays short (~40).** On 2026-09-11 it was pushed to 654 (auto-adding every replacement target) and transcription got noticeably worse within the hour; Joshua reversed it the same evening. Replacement targets are never auto-added. Mis-hearings go in `replacements.md`, which costs nothing in accuracy.

9. **No sync to the iPhone yet (checked 2026-09-12).** FileSync is Mac-only; the Windows docs page (`/docs/get-started/windows`) lists it as "still in development for Windows", the iOS page says modes and vocabulary "don't sync from your Mac or PC yet", and the Windows app resets `filesyncEnabled` to false at launch. The phone is kept in step by paste: the Super mode instructions and the vocabulary live on the artifact "Superwhisper on iPhone" (https://claude.ai/code/artifact/63400afd-4f6c-4139-ba82-461de066d544); republish it whenever `modes/super.md` or `vocabulary.md` changes. Re-check the Windows page after each app update.

10. **Official CLI + MCP exist, Mac-only (checked 2026-09-12).** `superwhisper` CLI (search/export/stats/vocab/snippets/mcp), announced 2026-07-16, released at github.com/superultrainc/superwhisper-cli-release; v0.1.0 ships only a macOS universal binary and the install script refuses non-Darwin. The Claude Code plugin (superultrainc/superwhisper-claude-code) is also Mac 2.13+. On this PC, `sync.py` is the equivalent of `superwhisper vocab`. Re-check the release assets after each Windows app update; when a Windows binary lands, add `superwhisper mcp` to Claude Code.

11. **Replacements are substring matches, not word matches (proved 2026-09-23).** A rule whose heard side can sit inside a longer word will corrupt that word: `cli` turned "click" into "CLIck" 48 times, `u i` turned "you install" into "yoUInstall", `firecraw` matched inside "firecrawl" and produced "Firecrawll". Never add a bare acronym or a fragment of a longer word. Casing belongs in the mode glossary, which Sonnet 5 applies with judgment. `scan.py` section 2b lists any rule that is currently doing this; it must stay empty.
12. **`scan.py` section 2 reads the post-replacement `result`.** Testing the raw transcript makes every rule look broken, because the raw is by definition what the voice model heard before any rule ran (that false positive stood from 2026-09-11 to 2026-09-23).

13. **One glossary, every mode.** Vocabulary and replacements were always global (they live in `settings.json` and run before any mode sees the text). The mode *prompt* was not: until 2026-09-26 only Super had the glossary and the house rules. `shared.md` now holds them and `sync.py` appends it to every mode with a language model. Add a term there, not in one mode.

14. **Silence makes the voice model invent text (measured 2026-10-12).** Clips under 2 s (accidental Left Alt taps) are the worst: 1 s clips produced 1,500 characters of "The world is a world of the world." The voice step cannot be fixed from here; `shared.md` step zero strips the known fillers and loops in every AI mode. Re-run `hallucinations.py` to measure.

## Where the app keeps things

`C:\Users\Joshu\AppData\Local\com.superwhisper.app\`
`settings\settings.json` (vocabulary, replacements, modeKeys) · `modes\*.json` · `preferences.json` (shortcuts, automaticUpdates, activeMode) · `recordings\<id>\meta.json` + `Output.wav` (every dictation, kept forever) · `database\superwhisper.sqlite` (history index).

Exe: `C:\Users\Joshu\AppData\Local\superwhisper\Superwhisper.exe` (reinstalled there 2026-09-11; the old copy under the Claude package folder is dead weight).

## Configured mode set (2026-10-09)

This table describes the source configuration. App-loaded state still requires rule 7 verification.

| Mode | Model | Use |
|---|---|---|
| Dictation | Sonnet 5 | General speech cleanup; preserves meaning, questions, details, and uncertainty. |
| AI Instructions | Sonnet 5 | Requests to an agent; preserves every constraint and never answers or acts. |
| Student Writing | Sonnet 5 | Dictated emails and messages in Joshua's voice, without invented content. |
| Rewrite | Sonnet 5 | Select text, say what to do to it. |
| Session Recording | none | Record a live session, nothing pasted. |

Previous specialist modes and Verbatim are preserved in `modes/archived/`, outside the sync's active file glob. Restore a file to `modes/` and sync to re-enable it. **Archiving a mode also needs its app JSON moved out of the app's `modes\` folder**, or the app re-adds it at launch (it stayed live from 2026-10-09 until 2026-10-12, when the six JSONs were moved to `com.superwhisper.app\modes-archived-2026-10-12\`). Recording uses Left Alt in toggle mode; the disabled push-to-talk shortcut is not the active recording control.

Switch with Ctrl+Shift+M, or `superwhisper://mode?key=<key>`. Per-mode hotkeys are set in the app (Modes → mode → Keyboard shortcut) and are not managed here yet.

## Skill

The `superwhisper` skill is the runbook for both runtimes: `skills/claude/superwhisper/SKILL.md` for Claude and `skills/codex/superwhisper/SKILL.md` for Codex, activated in their project skill folders. It covers word/correction → variants → `sync.py --restart`; modes; `scan.py`. Invoke it for any Superwhisper request.

## Related

`wiki/SUPERWHISPER-DICTIONARY.md` is the human-readable ledger and points here. Memory note: `superwhisper-settings-location`.

