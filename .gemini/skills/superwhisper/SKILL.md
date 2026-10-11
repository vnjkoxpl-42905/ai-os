---
name: superwhisper
description: "Use whenever Joshua wants anything changed in Superwhisper, his dictation app on the Windows laptop. Triggers on \"save X in my vocabulary\", \"add X to my dictionary\", \"X --> Y\", \"X should always be Y\", \"replace X with Y\", a bare mis-heard word with an arrow, \"make a mode for ...\", \"scan my transcripts\", \"what keeps getting messed up\", \"what should I add to Superwhisper\", \"restart Superwhisper\", and any mention of Superwhisper, Super Whisper, or \"the dictation\" in the same breath as a word, a spelling, or a mode. Also use it when a dictated message from Joshua arrives with an obvious mis-hearing of a known term, even if he does not ask: note it and offer the fix. Covers the whole loop: edit the vault files, think through the likely mis-hearing variants, sync into the app, restart it silently, verify the load, and scan the transcript history for the next improvements."
---

## Gemini host boundary

Use the current shared runner/CLI contract. Claude-native browser, task and hook tools named in the reference are available only when actually exposed; otherwise use the supported host route and report unavailable operations. Keep project paths relative to this registered root.


# Superwhisper

Joshua dictates almost everything he sends you. Superwhisper is the app that does it, and the
`dev/ai-os/superwhisper/` folder is its source of truth. Your job is to keep that folder right
and get it into the app without him having to touch anything. He uses Left Alt to toggle recording; preserve it and verify it after restart.

Read `dev/ai-os/superwhisper/CLAUDE.md` first if this is a new session. It holds the rules
that cost a whole session to learn (the Claude Desktop sandbox redirects writes, the app
reads config only at launch, prompt examples cannot be written from outside the app). This
skill assumes those rules; it does not repeat them.

## The three requests

### 1. A word or a correction ("Firecrow --> Firecrawl", "save Pre-workout")

Decide which of two files it belongs in. They do different jobs:

- `replacements.md` fixes a specific mis-hearing. Deterministic, case-insensitive, applied
  after transcription. This is where almost everything goes.
- `vocabulary.md` is a hint list sent to the voice model. Keep it around 40 entries: names and
  terms the model cannot know. On 2026-09-11 it was pushed to 654 (every replacement target
  auto-added) and transcription got noticeably worse within the hour, so that rule is gone;
  the sync sends exactly the listed terms. Add a vocabulary line only for a term the model
  keeps getting wrong.

A correction with an arrow is a replacement row only. "Save the word X" means a vocabulary
line (if the model really cannot know it) plus replacement rows for how it gets mangled.

**Think through the variants before writing.** One row per spelling he sends is not enough;
he sends the next mis-hearing ten minutes later. For each term, write rows for:

- the exact form he sent, lowercase on the heard side
- the same with a trailing period (`firecrow.`), because a one-word dictation gets
  auto-punctuated and the rule will not match with the period attached
- phonetic neighbours: swapped vowels (fisseha → faseya, fuseya, fasaya, fesaya), doubled
  or dropped letters (firecrawll, firecraw), split or joined words (pre workout, preworkout,
  cloudcode)
- spoken forms of anything with punctuation: "at ... dot com", "dot study"
- a casing pin when the wanted form has specific casing (`pre-workout` → `Pre-workout`,
  `lsatprep.study` lowercase, `LSATU` → `LSAT U`)
- the bare surname or bare product name, not only the full email or phrase

Do not add a row whose heard side is an ordinary English word or number ("seven" → Steven,
"white" → Whit, "care" → Charles, "and review" → blind review). It would fire inside normal
sentences. When a scan suggests one of those, say so and leave it out.

Note the trade-off on trailing-period rows: a sentence that genuinely ends with the word
loses its full stop. Say this once when you add the first such row; do not repeat it.

Then run the loop (below). The whole thing is one turn: he sends the word, you reply with
what you added and the loaded counts. No questions unless the target spelling is ambiguous.

### 2. A mode ("make a mode for ...")

Copy the closest file in `modes/` to a new `modes/<key>.md`. Frontmatter is the config
(key, name, type, voice_model `sv-1`, language_model, the three context flags, auto_paste);
the body is the prompt; `## Examples` with `### Input` / `### Output` pairs are appended to
the prompt text by the sync (the app rejects examples written any other way).

What makes his prompts work, from the docs and the community collections in
`superwhisper/research/`:

- Name the inputs exactly: User Message, Application Context, Selected Text, Clipboard
  Context. Say the User Message is dictated speech.
- Any mode whose output goes to an AI agent needs the "you are not an assistant" block with
  WRONG/CORRECT pairs, or the model answers the dictation instead of cleaning it. Copy it
  from `modes/claude-code.md`.
- Anything student-facing routes through `wiki/teaching-voice.md`: no em dashes, no hype
  words, short lines, "Hi [Name]," / "Best, Joshua".
- Turn on only the context the mode needs. Selection is captured at record start, clipboard
  within 3 s before or during, application after transcription.
- Language model: Joshua chose S1-Language (`sl-1`) for all modes on 2026-09-11 for speed.
  Keep that unless he asks; `sw-claude-4p5-sonnet` is the confirmed upgrade if a mode needs
  judgment.

Then run the loop. Add the mode to the table in `superwhisper/CLAUDE.md`.

### 3. A scan ("what keeps going wrong", "scan my transcripts", or every week or so unprompted)

```bash
python C:/Users/Joshu/dev/ai-os/superwhisper/scan.py            # all history
python C:/Users/Joshu/dev/ai-os/superwhisper/scan.py --since 7  # last week
```

It reads every recording's raw transcript and writes `research/SCAN-<date>.md` with four
sections: near-misses of known terms (these become replacement rows), replacement rules
that did not fire after their date (means the app was not restarted, or the spelling
differs), candidate terms seen often with varying spellings (worth adding), and the most
used domain words.

Turn the report into a short offer, not a dump: the rows you would add (and why), the ones
you are deliberately skipping (and why), and any mode-level improvement the transcripts
suggest (for example, if most of the week's dictations were instructions to an agent and
the Claude Code mode is not the active one, say so). Apply the safe rows in the same turn,
run the loop, and leave the judgment calls to him.

## The loop

Every change ends the same way. `sync.py --restart` does all of it:

```bash
python C:/Users/Joshu/dev/ai-os/superwhisper/sync.py --restart
```

1. Reads `vocabulary.md`, `replacements.md`, `modes/*.md`.
2. Backs up the app's `settings.json`, then writes vocabulary, replacements, modeKeys, and
   every mode file through the `\\localhost\C$` path (the sandbox bypass).
3. Quits Superwhisper and relaunches it through Task Scheduler so it runs outside the
   sandbox, silently, in the background. Nothing appears on his screen; he keeps using
   Left Alt.
4. Reads `modeKeys` back. The app rewrites that list at launch and drops any mode it
   rejected, so this is the only proof that a change loaded. A write is not a load.

Report the last line it prints (replacements / vocabulary / modes loaded). If the mode
count is lower than the number of files in `modes/`, a mode was rejected: diff the loaded
list against the files and fix before saying done.

`python sync.py --check` shows the diff without writing, for when you want to confirm
before touching anything.

## Things not to do

- Do not open the Settings window, the app, or anything visible after a restart. He asked
  for this explicitly on 2026-09-11. If he needs Settings, `superwhisper://settings` or the
  "Superwhisper Settings" shortcut on his Desktop opens it.
- Do not launch `Superwhisper.exe` with Start-Process from this shell. It starts a
  sandboxed second copy whose tray icon does not work. Only the scheduler route in
  `sync.py`.
- Do not edit the app's JSON by hand. Edit the vault files; the sync owns the JSON.
- Do not pad the vocabulary. When in doubt, it is a replacement.
- Do not batch his corrections for later. Each one lands, syncs, restarts, and is reported in
  the turn it arrives, even mid-task.

## Files

| Path | Role |
|---|---|
| `dev/ai-os/superwhisper/CLAUDE.md` | The rules. Read first. |
| `dev/ai-os/superwhisper/vocabulary.md`, `replacements.md` | The lists. Edit these. |
| `dev/ai-os/superwhisper/modes/*.md` | One file per mode. |
| `dev/ai-os/superwhisper/sync.py` | Push + restart + verify. |
| `dev/ai-os/superwhisper/scan.py` | Transcript scan → `research/SCAN-<date>.md`. |
| `dev/ai-os/superwhisper/research/` | The 2026-09-11 customization report, sources, scans. |
| `wiki/SUPERWHISPER-DICTIONARY.md` | Dated history ledger; append a line when something notable changes. |
