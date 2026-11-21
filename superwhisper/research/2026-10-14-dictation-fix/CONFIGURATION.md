# Superwhisper configuration repair, 2026-10-14

## The saved prompt was bypassed

Recent recording metadata contained the built-in Super template, despite custom instructions in mode JSON. All four AI mode files were `type: super`. The vendor's mode schema says custom instructions require `type: custom`; the installed Windows binary also exposes distinct Super and Custom mode types. Sources: https://raw.githubusercontent.com/superultrainc/superwhisper-docs/main/skills/superwhisper-optimize/references/mode-schema.md and local recording metadata. Historical prompt equality did not prove runtime execution.

## Applied configuration

- Dictation, AI Instructions, Student Writing, and Rewrite now use Custom. Session Recording stays Voice with auto-paste disabled.
- Preserved the app-selected models: AI Instructions `claude-sonnet-5-5`; other AI modes `claude-sonnet-5`; all use existing S1-Voice.
- Disabled application, clipboard, and selection context for general dictation, AI Instructions, and Student Writing. Rewrite uses selection only.
- Simplified the shared glossary to contextual exact-name references. Removed blanket gratitude deletion and speculative ordinary-word mappings. Added faithful cleanup examples, including literal repeated slash words and ambiguous product-like wording.
- Live shortcut was Backslash at the preflight check. Restored `toggleRecordingShortcut=AltLeft`, `p2t=false` as requested.
- Preserved live vocabulary (33, including Kling) and replacements (870), using `--modes-only`. Source word-list differences remain unapplied.

## Verification and recovery

Applied with `python sync.py --modes-only --left-alt --restart`. Final restart reported two Superwhisper processes, five loaded modes, 33 vocabulary entries, 870 replacements, Left Alt toggle, and exact source/live prompt, type, model, and context agreement. The five-mode dry check was unchanged after the initial repair. The final prompt refinement was synced again and passed the same readback checks.

The sync now stops Superwhisper before writes, backs up app settings, all mode files, and preferences, and checks exact configuration after launch. It leaves unrelated settings untouched. The default generated mode type is Custom.

Original source backups: `../backups/2026-10-14-prompts/`. App backups are under `C:/Users/Joshu/AppData/Local/com.superwhisper.app/settings/bak/`, with stamps `2026-10-14-002837` (pre-repair app state) and `2026-10-14-003219` (before final prompt refinement). Restore the matching settings, modes, and preferences with the app stopped, then restart. The older backup contains the original Backslash shortcut.

## What the tests prove

See `RESULTS.md`, model receipts, compiled prompts, and `audio-signal.json` here. Saved raw-transcript cleanup tests are not audio recognition tests and do not establish intended speech. Initial replay used Opus; final replay requested and received the exact app Sonnet IDs. Batch wrappers differ from individual Superwhisper requests.

No supported external Windows audio-reprocess endpoint was found. An internal Tauri command alone is insufficient to invoke safely. No audio was uploaded or original recording modified. Fresh recording effective-prompt verification and an in-app audio replay remain unperformed. Signal measurements establish audio presence, not intelligibility or microphone quality. The 1.744-second hallucination clip is not globally near-silent.
