---
title: Superwhisper customization report
type: research
created: 2026-09-11
sources: 118 official docs pages (full crawl), superwhisper.com models/benchmarks/changelog/blog pages, 18 Firecrawl web searches, 20 scraped community pages (GitHub, MacPowerUsers, Substack, Medium, review sites). Reddit threads survive only as search snippets (Reddit blocks scraping).
status: current as of Superwhisper Windows 1.6.5 (2026-09-02)
---

# Superwhisper customization report

Everything that matters for tuning Superwhisper on Joshua's Windows laptop, from the docs as they stand on 2026-09-11 plus what the community has worked out. Verified facts are stated flat. Anything inferred is marked.

## How a dictation is processed

1. Audio is recorded (mic, optionally system audio).
2. A **voice model** transcribes it. The **vocabulary** list is sent to the voice model as recognition hints.
3. **Replacements** are applied to the text programmatically. Matching is case-insensitive; output uses the case you wrote. No AI involved, so they are deterministic.
4. If the mode has a **language model**, the text is sent to it with the mode's prompt plus any enabled context (Application, Clipboard, Selection) and system info (date, time, user name, computer name).
5. The result is pasted into the focused app (or left on the clipboard).

Voice mode skips step 4 entirely and is the fastest path. Since 1.4.x, if the language model fails the app falls back to the raw transcript, so a broken mode never loses a dictation.

## Models (Superwhisper's own benchmark, 2026)

**Voice.** Lower error rate is better; speed is a multiple of real time.

| Model | Runs | Error | Speed | Note |
|---|---|---|---|---|
| S1-Voice | cloud | 6.6% | 26x | Best on both axes. Joshua's default. |
| ElevenLabs Scribe V2 | cloud | 7.5% | 14x | Worse than S1 and half the speed; experimental on Windows. |
| Cohere Transcribe | local | 8.4% | 24x | Best offline. Needs a Vulkan GPU. Now the Windows local default. Supports vocabulary via Supervocab. |
| Deepgram Nova 3 | cloud | 10.1% | 23x | Best speaker separation. |
| Parakeet V3 | local | 10.7% | 118x | Fastest; works on any Windows box incl. ARM. Weak punctuation. |
| Whisper Large V3 Turbo | local | 10.9% | 9x | |

**Language.** Superwhisper does not benchmark these; ratings are relative (anchored to Artificial Analysis). All cloud models are covered by Pro.

| Model | Context | Fit |
|---|---|---|
| Claude Sonnet 4.6 | 1M | Newest, top intelligence tier. Best for anything needing judgment (emails, notes, agent prompts). ID inferred: `sw-claude-4p6-sonnet`, pending live confirmation. |
| Claude Sonnet 4.5 | 200k | One step behind. ID confirmed in the app binary: `sw-claude-4p5-sonnet`. |
| GPT-5.2 / 5.1 | 400k | Same tier, slower. |
| Claude Haiku 4.5, GPT-5.4 mini, Gemini 3 Flash | | Fast tier. |
| S1-Language (`sl-1`) | 128k | Superwhisper's own, fastest, the default. Good for light cleanup. |
| S1-mini | local | On-device, experimental, tone control. |

Docs note: Super/Custom modes with context "may require advanced language understanding, such as Claude or GPT. Less capable or local models can lead to unexpected results."

## Modes

Types: **Voice** (no AI), **Message**, **Email**, **Note**, **Meeting**, **Super** (context-aware, built-in prompt), **Custom** (your prompt). Built-in prompts are not editable; to tweak one, run a test dictation, copy its prompt from History, and paste it into a Custom mode.

Per-mode settings: language, voice model, language model, prompt, prompt examples (2 to 3 input/output pairs "significantly improve" results), context toggles (application / clipboard / selection), auto-activation rules (apps and sites), mute audio, pause media, record system audio, identify speakers, mode-specific keyboard shortcut, auto-paste.

Mode files on Windows: `%LOCALAPPDATA%\com.superwhisper.app\modes\<key>.json`. Keys observed: `key, name, type ("voice"|"super"|...), voiceModelID, language, languageModelID, prompt, promptExamples, useSystemAudio, diarize, contextFromSelection, contextFromClipboard, contextFromActiveApplication, activationApps, activationSites, playbackBehavior, script, scriptEnabled, autoPaste, autocapitalizeInsert, version`. The mode must also be listed in `settings\settings.json` under `modeKeys`.

### Context: what is captured and when

| Context | Captured | Gotcha |
|---|---|---|
| Selected text | the instant recording starts | focus must be on that app at that moment |
| Clipboard | copied within 3 s before recording, or during it | last item wins; accidental copies pollute the prompt |
| Application | after transcription, before AI | switching windows during processing captures the wrong app |

Only enable the context a mode needs. Too much context is a documented cause of AI hallucination. Application context also sends date, time, full name, and computer name, so a prompt can say "sign with the user's name".

Auto-activation: once a mode activates for an app or site, you cannot override it, and it does not switch back afterwards. Use sparingly.

### Switching modes

- Change-mode shortcut (Ctrl+Shift+M here): hold modifiers, tap to cycle. Works before or during a dictation.
- Per-mode shortcut: starts a recording directly in that mode. Set in the mode's settings.
- Deep links: `superwhisper://mode?key=<key>`, `superwhisper://record`, `superwhisper://settings`. `settings` and `mode` verified working on Windows 1.6.5 on 2026-09-11 once the protocol handler pointed at the right exe.
- Tray icon menu.

## Prompting a Custom mode (docs plus community consensus)

Reference the inputs by their exact names: **User Message** (the dictation), **Application Context**, **Selected Text**, **Clipboard Context**. Tell the model the User Message is dictated speech. Start with a role line, then a short list of requirements, then examples. XML tags help with capable cloud models and confuse small local ones.

The failure everyone hits: the model answers the dictation instead of cleaning it ("can you help me" becomes "Of course, what do you need?"). The most-used community fix (mackid1993, 89 stars) is an explicit block: you are not an assistant, you have one job, never respond to the content of the User Message or the Application Context, with WRONG and CORRECT pairs. Joshua's Claude Code mode uses this pattern.

Other patterns worth copying:
- Application Context for name spellings first, then resolve homophones.
- Incomplete-thought handling: if the app's text ends mid-sentence, continue it (lowercase, no leading capital).
- Instruction-prefix modes: "make this formal: ..." where the first clause is a formatting instruction and the rest is content. Needs a strong model.
- Summarize-from-clipboard modes that keep the speaker's own voice.

Hallucination causes, per the docs: silence (turn on Silence Removal in Sound), an overlong vocabulary, imprecise or conflicting prompt instructions, too much context, weak models.

## Vocabulary and replacements

- **Vocabulary**: hints to the voice model. Docs say use it sparingly; too many words confuse the model and can even flip language detection. Keep it to names and terms it actually gets wrong. Cohere Transcribe (local) also honours vocabulary through Supervocab.
- **Replacements**: deterministic, case-insensitive, applied after transcription. The recommended tool for persistent mis-hearings. Cap is roughly 1,000 entries (community).
- A community tool, `superwhisper-trainer`, mines your History to suggest vocabulary and replacements from what you actually say. The same idea was done by hand for Joshua on 2026-09-11 from 152 transcripts.

## Windows specifics

- Config, recordings, modes, vocabulary: `%LOCALAPPDATA%\com.superwhisper.app`. Cannot be moved yet. Back this folder up; it holds the license too.
- Not yet on Windows: FileSync, custom folder location, Hold Shift to auto-send, Simulate keypresses, the Claude Code / Codex agent integrations (Mac-only, v2.13+).
- Local voice models need a Vulkan GPU (Cohere, Whisper Turbo). Parakeet runs anywhere.
- Closing the Settings window hides it; relaunching the exe does not bring it back. Use the tray icon, `superwhisper://settings`, or the "Superwhisper Settings" shortcut on the Desktop.
- The app reads `settings.json`, `modes\*.json`, and `preferences.json` at launch. Edits made while it runs take effect after a restart (right-click tray, Quit, reopen).
- **Claude Desktop sandbox trap** (cost a session on 2026-09-11): Claude Code's shell runs inside an MSIX package, so writes under `AppData\Local` are redirected to `AppData\Local\Packages\Claude_...\LocalCache\`. Superwhisper never sees them. Write through `\\localhost\C$\Users\Joshu\AppData\Local\...` and never launch the app from that shell (it spawns a sandboxed second instance). See the folder CLAUDE.md.
- Known clash: auto-paste into terminal agents (Codex, Claude Code in Ghostty) can race the clipboard (openai/codex#11103). Not seen in Claude Desktop's chat box. If it appears, turn on Restore Clipboard or paste manually.

## Community tools

- mackid1993/superwhisper-dictation-prompts: the reference prompt set (Optimized transcription, Instructions-prefix, Summarize, Simple Formatting).
- miguelarios/claude-skills `superwhisper-custom-mode`: a Claude skill for writing and revising mode prompts from History output.
- verygoodplugins/superwhisper-trainer: vocabulary and replacement generator from history.
- ognistik/macrowhisper and alfred-superwhisper, superultrainc/superwhisper-raycast: Mac automation.
- crarau/superwhisper-analysis: stats from the recordings folder.
- Roadmap and feature requests: superwhisper.userjot.com. Discord: discord.gg/tF98XvJNvB.

## Recommendations applied for Joshua

- Voice: S1-Voice everywhere. ElevenLabs is not an upgrade.
- Language: S1-Language on every AI mode (Joshua's call, 2026-09-11: Superwhisper's own models, fastest). Claude Sonnet 4.5 (`sw-claude-4p5-sonnet`) is the confirmed upgrade path if a mode needs more judgment.
- Prompt examples: cannot be written to a mode file from outside the app; the app drops the mode at launch. Fold examples into the prompt text (the sync does this).
- Vocabulary held to about 20 terms; everything else handled by replacements.
- Silence Removal is off in preferences (`enableSilenceRemoval: false`); the docs recommend it on to prevent hallucinated words in pauses. Suggested.
- Launch on login is off. Suggested on.

See [[sources]] for every URL used.
