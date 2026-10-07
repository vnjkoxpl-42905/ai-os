---
name: ingest
description: >
  Front door for getting anything into the brain — web clips, session
  transcripts, exports, dropped files. Use when Joshua says "ingest this",
  "ingest the latest clips", "process the transcripts", "file these notes",
  "I saved an article", or drops a file and expects it filed. Routes to the
  right pipeline, dedupes first, and never leaves the source modified.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Ingest

One front door. Joshua should never have to know which pipeline a thing belongs
to, and no session should ever spend its first minutes hunting for a file he
just saved.

## Route first

Identify what is being ingested, then jump to that section. If ambiguous, ask
once — do not guess and file it somewhere wrong.

| Input | Section |
|---|---|
| Web clip saved by Obsidian Web Clipper | [Clips](#clips) |
| Gemini session notes / transcripts (`.docx`, `.txt`) | [Transcripts](#transcripts) |
| A source document meant to become wiki knowledge | defer to `second-brain-ingest` |
| A bulk export (Takeout, platform dump) | [Bulk exports](#bulk-exports) |

`second-brain-ingest` owns `raw/` to `wiki/` knowledge pages and stays the
authority there. This skill does not duplicate it — for a knowledge source, do
the dedupe check below and then hand off.

## Always, before any pipeline

1. **Find the file without asking Joshua where it is.** Search all the places
   things land, in this order, newest first:
   ```
   Clippings/  raw/inbox/  raw/sources/  ~/Downloads/  ~/Desktop/
   ```
   Only ask if the search genuinely comes up empty. He has had to answer "where
   is it" too many times.
2. **Dedupe by content hash, not by name.** A byte-identical copy under a
   different filename has already been ingested at least once.
   ```
   shasum -a 256 <candidate>
   ```
   Compare against anything already filed with the same size. If it is a
   duplicate, say so and stop — do not ingest it twice, and do not delete the
   duplicate without asking.
3. **Check the log.** `wiki/log.md` records every ingest. If the source name is
   already there, confirm with Joshua before re-running.
4. **Never modify the source.** `raw/` is immutable. Clips and exports are read,
   never edited or moved, unless Joshua explicitly says to move them.

## Clips

Obsidian Web Clipper writes to `Clippings/`. These are external source material,
unprocessed.

1. List `Clippings/` newest-first. If Joshua said "the latest", take the newest;
   if he named a topic, match on it; if several are new, list them and ask which.
2. Run the dedupe check above.
3. Read the clip fully.
4. Summarize the 3 to 5 takeaways and ask whether any should be emphasized or
   skipped. Wait for confirmation.
5. Write or update the wiki page(s) the clip touches. One authoritative page per
   subject — update the existing page rather than growing a parallel one.
6. Update `wiki/index.md`.
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <title>` with the source
   path and which pages changed.

One clip at a time, supervised, unless Joshua says batch.

## Transcripts

Gemini session notes live in `raw/data-about-me/transcripts/` as `.docx` (plus
occasional `.txt` chat/caption exports). This is unprocessed PII and git-ignored
— never read the folder wholesale into context.

**Start with the inventory. Do not re-derive the mapping by hand.**

```
python3 system/scripts/transcript-inventory.py             # full report
python3 system/scripts/transcript-inventory.py --unmatched # only the gaps
python3 system/scripts/transcript-inventory.py --json      # machine-readable
```

It parses every filename shape present, maps each transcript to a student folder
using `students/_aliases.md`, and prints what it cannot resolve. It is read-only.

Then, per transcript being ingested:

1. Confirm the student mapping from the inventory. If the file is unmapped,
   resolve it before filing:
   - a name variant of an existing student → add it to the `## Aliases` section
     of `students/_aliases.md`, re-run the inventory, continue;
   - a consultation or one-off, not an ongoing student → add to
     `## Not students` so it stops surfacing;
   - a real recurring student with no folder → **ask Joshua before creating
     one.** Creating a student folder is a judgment call about the
     relationship, not a filing detail.
2. Read the transcript. Extract: what was taught, what the student struggled
   with, what was assigned, what to follow up on.
3. Write the distillation into the student's folder, respecting the
   primary/mirror boundary in `students/README.md`:
   - teaching content and judgments → `teaching-notes.md` (**primary** — append,
     never overwrite, never regenerate)
   - a dated session record → `transcripts.md` (primary)
   - anything needing a follow-up action → `open-loops.md`
   - never write to a `*.generated.md` file; those mirror a live backend.
4. Append to `wiki/log.md`.

Filing a distillation is not the same as copying the transcript. The `.docx`
stays in `raw/`; what lands in the student folder is what a human would want to
read before the next session.

## Bulk exports

Takeout and platform dumps land in `raw/data-about-me/` and are git-ignored PII.

- Never read one wholesale — it will blow the context window and has before.
- Inventory first (file counts, types, date ranges), report, and let Joshua pick
  what matters.
- Duplicate exports are common and large. Report duplicates by hash and size;
  do not delete without asking.
- If analysis is needed across many files, delegate to a sub-agent that returns
  a summary, not file contents.

## Hard rules

- **Never delete or move a source.** Flag duplicates; Joshua decides.
- **Never create a student folder without asking.**
- **Never write to `*.generated.md`.** Those are backend mirrors and get
  overwritten.
- **Dedupe before ingesting, every time.** The same clip has been ingested twice
  before because the check was skipped.
- **One source at a time, supervised,** unless Joshua explicitly says batch.
- **Government IDs stay out.** If an export contains them, stop and say so.
- Prefer the inventory script over hand-parsing filenames. If it gets something
  wrong, fix the script or the alias file — do not work around it silently, or
  the next session re-derives the same mapping.
