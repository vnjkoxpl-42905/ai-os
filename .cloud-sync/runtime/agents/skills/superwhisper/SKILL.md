---
name: superwhisper
description: Maintain Joshua's Superwhisper dictation setup on this Windows laptop. Use for vocabulary requests, spoken correction mappings, custom modes, transcript-error scans, configuration checks, or restarting Superwhisper.
---

# Superwhisper

The source of truth is `C:/Users/Joshu/dev/ai-os/superwhisper/`. Read
`superwhisper/CLAUDE.md` before changing anything; despite its name, it contains the
app-specific operating rules for both runtimes.

Joshua uses Left Alt to toggle recording. Preserve it and verify it after restart. Complete configuration changes, sync them, restart
the app silently, and verify what loaded without opening Superwhisper or Settings.

## Correction or vocabulary request

- `X --> Y`, "replace X with Y", and "X should always be Y" add rows to
  `superwhisper/replacements.md`. Matching is case-insensitive.
- "Save X in my vocabulary" adds X to `superwhisper/vocabulary.md` only when X is an
  unusual name or domain term the voice model needs help recognizing.
- Do not automatically add replacement targets to vocabulary. That experiment expanded
  the list to 654 entries on 2026-09-11 and immediately worsened transcription. Keep the
  vocabulary around 40 terms.

For a replacement, add useful variants in the same pass: the exact error, a trailing-period
form for one-word dictation, plausible phonetic spellings, joined or split words, and spoken
punctuation such as "dot" or "at". Add only variants that plausibly identify the intended
term. Never replace an ordinary word such as `seven`, `white`, or `care` merely because it
resembles a name; that would corrupt normal sentences.

Use `apply_patch` for vault edits. Preserve the Markdown table format:

```markdown
| heard form | Wanted form | YYYY-MM-DD | reason |
```

After editing, run from `C:/Users/Joshu/dev/ai-os/superwhisper/`:

```powershell
python sync.py --restart
```

Report the final loaded counts. If the loaded mode count is below the number of mode files,
fix the rejected mode before reporting success.

## Custom mode

Read the relevant existing file in `superwhisper/modes/` and copy its structure into a new
`modes/<key>.md` file. Frontmatter controls the model and context; the body is the prompt.

- Use S1-Voice (`sv-1`) unless Joshua chooses another voice model.
- The app picker and the app's mode JSON are the authority for available language models.
  Website documentation can lag. Never infer a model ID.
- Agent-output modes need an explicit "you are not an assistant" instruction so the model
  cleans the dictated request rather than answering it.
- Student-facing modes must follow `wiki/teaching-voice.md`.
- Enable only the context the mode needs.
- Put worked examples under `## Examples`; `sync.py` folds them into prompt text because
  externally written `promptExamples` cause the app to reject a mode.

After adding a mode, update the mode table in `superwhisper/CLAUDE.md`, then sync, restart,
and verify the loaded `modeKeys`.

## Transcript scan

Run one of:

```powershell
python C:/Users/Joshu/dev/ai-os/superwhisper/scan.py
python C:/Users/Joshu/dev/ai-os/superwhisper/scan.py --since 7
```

The report is written to `superwhisper/research/SCAN-<date>.md`. Apply safe, specific
mis-hearing fixes. Report risky suggestions separately and leave them unapplied. A common
English word is always a risky replacement target.

## Operational constraints

- Edit the vault files, not the app JSON. `sync.py` owns the generated JSON.
- The real app data is under
  `C:/Users/Joshu/AppData/Local/com.superwhisper.app/`; `sync.py` already uses the tested
  path and restart procedure.
- Do not launch the executable directly and do not open visible app windows. Use
  `sync.py --restart`.
- The app reads configuration only at launch. A successful write is not proof; the final
  `modeKeys` readback after restart is proof.
- Apply individual corrections immediately rather than batching them for later.
- Append a short entry to `wiki/SUPERWHISPER-DICTIONARY.md` only for notable policy,
  mode, migration, or bulk-scan changes. Routine one-word replacements do not need a ledger
  entry.
