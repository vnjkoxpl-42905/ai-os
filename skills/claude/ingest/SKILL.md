---
name: ingest
description: >
  Front door for getting anything into the brain. Use whenever Joshua says
  "ingest this", "ingest the latest clips", "process the transcripts", "pull
  this week's transcripts", "file these notes", "I saved an article", "what's
  in the inbox", or drops a file, a screenshot, or a score report and expects
  it filed — even when he does not say "ingest". Routes each input to its
  pipeline (clips, Gemini session transcripts, Superwhisper recordings, student
  evidence, bulk exports), dedupes by hash first, and never modifies a source.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Ingest

One front door. Joshua should never have to know which pipeline a thing belongs
to, and no session should spend its first minutes hunting for a file he just
saved. The skill ends when the source is archived with provenance, the
distillation is filed where the next session will look, and `wiki/log.md`
says so. Anything short of that is a pile, not an inbox.

## Route first

Identify what is being ingested, then jump to that section. If it is genuinely
ambiguous, ask once. Do not guess and file it somewhere wrong.

| Input | Where it lands | Section |
|---|---|---|
| Web clip from Obsidian Web Clipper (`.md` in `raw/inbox/`) | `raw/inbox/` | [Clips](#clips) |
| A clip that is a YouTube / video page | `raw/inbox/` | [Clips](#clips), read via `watch` |
| Gemini "Notes by Gemini" from a live session (this week, last week) | Google Drive | [Transcripts, live](#transcripts-live) |
| Archival Gemini `.docx` / `.txt` (Apr to Jul 2026 Takeout batch) | `raw/data-about-me/transcripts/` | [Transcripts, archival](#transcripts-archival) |
| Superwhisper `recordings/` dirs (`meta.json` + `output.wav`) or `settings.json` | wherever they were dropped | hand to `superwhisper`; not this skill's |
| Student evidence: PT score report, screenshot, homework export | `~/Downloads`, chat attachment | [Student evidence](#student-evidence) |
| A source document meant to become wiki knowledge | `raw/` | dedupe below, then hand to `second-brain-ingest` |
| Takeout or platform dump | `raw/data-about-me/` | [Bulk exports](#bulk-exports) |

`second-brain-ingest` owns `raw/` to `wiki/` knowledge pages. `lsat-session-lesson`
owns writing the student-facing recap. This skill gets the source on disk,
archived, and distilled; it does not duplicate either of them.

## Always, before any pipeline

1. **Find the file without asking where it is.** Search newest-first:
   ```
   raw/inbox/   raw/sources/   ~/Downloads/   ~/Desktop/   students/*/transcript-downloads/
   ```
   Ask only if that comes up empty. He has answered "where is it" too many
   times. `raw/inbox/` is the single intake queue; the old top-level
   `Clippings/` folder was folded into `raw/sources/clips/` on 2026-09-08, so a
   `Clippings/` path in an old note is stale.
2. **Dedupe by content hash, not by name.**
   ```
   sha256sum <candidate>
   grep -rl "<hash>" raw/sources/*/*/SHA256SUMS
   ```
   A hit means it has been ingested; say so and stop. Byte-identical copies
   under different names are how three copies of one clip piled up before
   2026-09-08. Never delete the duplicate without asking.
3. **Check the log.** `grep -n "<source name>" wiki/log.md`. Already there
   means confirm with Joshua before re-running.
4. **Never modify the source.** `raw/` is immutable. Sources are read and
   archived, never edited in place, and never moved except by the archive step
   of the pipeline that owns them.

## Clips

Obsidian Web Clipper writes `.md` files to `raw/inbox/`. Anything else sitting
there (a `recordings/` tree, a `settings.json`) is not a clip; route it by the
table above and tell Joshua it was in the wrong place rather than processing it
here.

1. List `raw/inbox/*.md` newest-first. "The latest" means the newest; a named
   topic means match on it; several new ones means list them and ask which.
2. Dedupe (above).
3. Read the clip fully. If it is a video page with no transcript in the clip,
   run `watch` on the URL to get one; the clip alone is a thumbnail.
4. Summarize 3 to 5 takeaways and ask which to emphasize or skip. Wait.
5. Write or update the wiki page(s) the clip touches. One authoritative page per
   subject; grow the existing page rather than a parallel one.
6. Update `wiki/index.md`.
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <title>` with the source
   path and the pages changed.
8. **Archive.** Move the clip from `raw/inbox/` to `raw/sources/clips/<slug>/`
   (kebab-cased title) with:
   - `PROVENANCE.md`: source URL, author, published date, clipped date,
     archived date, size, where the distilled output landed. Copy the shape from
     any sibling folder.
   - `SHA256SUMS`: `sha256sum <clip> PROVENANCE.md > SHA256SUMS`.

   Done means `raw/inbox/` no longer contains the clip. A file still there
   means "not yet processed" and nothing else.

One clip at a time, supervised, unless Joshua says batch.

## Transcripts, live

Gemini writes "Notes by Gemini" docs to Google Drive after each Meet session.
The brain's copy is `students/<slug>/transcript-downloads/YYYY-MM-DD-<slug>-notes-by-gemini.md`
(primary record: the brain is its only home). Getting them there is step 1 of
`lsat-session-lesson/references/transcript-intake-and-record.md`; follow that section exactly (Calendar sweep by guest email,
Drive sweep for unattached docs, export as `text/plain`, resolve the person
with `students/_aliases.md`, consultations and unknowns to
`students/_other-sessions/`). It is the single source of truth for the pull;
do not re-derive the `gws` commands here.

Then, per transcript that is new on disk:

1. Read the whole transcript, not the Gemini summary at the top. The summary
   flattens what the student actually did; the distillation has to name the
   answer they picked and the line they misread.
2. Append to the student's `teaching-notes.md` (create it from a sibling if the
   folder lacks one; it is a standard primary file): what was taught, where they
   struggled, what was assigned, what to follow up. Dated heading, append-only,
   never regenerate.
3. Anything needing an action goes to `open-loops.md` (same rules).
4. Add one line to `transcripts.md` so the folder's inventory matches disk.
5. Never write to a `*.generated.md` file; those mirror a live backend.
6. Append to `wiki/log.md`.

Done means every session in the window either has its transcript on disk and
distilled, or is listed in the log as "no Gemini doc anywhere" with the date and
student, so the next session does not sweep it again.

If Joshua wants the recap note as well, that is `lsat-session-lesson`; say so rather
than writing one here.

## Transcripts, archival

The Takeout batch of 52 `.docx` / `.txt` files in `raw/data-about-me/transcripts/`
(2026-04-28 to 2026-07-15) was distilled on 2026-07-20 (`wiki/log.md`). It is
git-ignored PII; never read the folder wholesale into context.

**Start with the inventory. Do not re-derive the mapping by hand.**

```
python system/scripts/transcript-inventory.py              # full report
python system/scripts/transcript-inventory.py --unmatched  # only the gaps
python system/scripts/transcript-inventory.py --json       # machine-readable
python system/scripts/transcript-inventory.py --text "<file>.docx"   # one transcript as text
```

It maps each file to a folder using `students/_aliases.md`, knows that former
students live in `students/non-students/`, and prints what it cannot resolve.
`--text` exists because this box has no python-docx and no pandoc; it is how a
`.docx` gets read. The script is read-only.

For an unmapped file, resolve before filing:
- a name variant of an existing student: add it under `## Aliases` in
  `students/_aliases.md`, re-run, continue;
- a consultation or one-off: add under `## Prospects, no record yet` (the
  section the script parses) so it stops surfacing;
- a real recurring student with no folder: **ask Joshua before creating one.**
  A folder is a judgment about the relationship, not a filing detail.

Then distill exactly as in the live section, steps 1 to 6. The `.docx` stays in
`raw/`; what lands in the student folder is what a human wants to read before
the next session.

If the inventory gets a mapping wrong, fix the script or the alias file. Working
around it silently means the next session re-derives the same mapping.

## Student evidence

PT score reports, intake screenshots, homework exports, anything about one
student that arrives as a file.

1. Identify the student (filename, chat context, contents). Ask if unclear.
2. Dedupe (above).
3. Copy into the student folder under the matching standard subfolder from
   `students/README.md`: score reports to `Practice_Test_Reports/`, assigned
   work to `Student_Specific_Homework/`, otherwise the folder root with a dated
   name. These are raw evidence: read for diagnosis, never edited.
4. If it changes a judgment, append the judgment to `teaching-notes.md` with the
   file as its cited source.
5. Log it.

## Bulk exports

Takeout and platform dumps land in `raw/data-about-me/` and are git-ignored PII.

- Never read one wholesale; it has blown the context window before.
- Inventory first (file counts, types, date ranges), report, and let Joshua
  pick what matters.
- Duplicate exports are common and large. Report duplicates by hash and size;
  do not delete without asking.
- Analysis across many files goes to a sub-agent that returns a summary, not
  file contents.

## Hard rules

- **Never delete or move a source** except the archive step of its own
  pipeline. Flag duplicates; Joshua decides.
- **Never create a student folder without asking.**
- **Never write to `*.generated.md`.**
- **Dedupe before ingesting, every time.**
- **One source at a time, supervised,** unless Joshua explicitly says batch.
- **Government IDs stay out.** If an export contains them, stop and say so.
- Commands here are for this Windows box (Git Bash: `sha256sum`, `python`).
  A note that says `shasum -a 256`, `python3`, or `/Users/joshuaf/...` is from
  the Mac and is stale, not a different pipeline.
