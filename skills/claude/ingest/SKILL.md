---
name: ingest
description: >
  The single front door for adding sources to the current knowledge base. Use
  for "ingest this", "process this source", "file these notes", "add this to
  my second brain", "ingest the latest clips", or a supplied document meant
  to become saved knowledge. Finds the input, checks content hashes, preserves
  provenance, and compiles it into linked wiki pages. Session write-ups and
  student-facing post-session recaps belong to post-session-recap. Student and
  consultation session transcripts belong to transcript-intake, not this pipeline.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Ingest sources into the current brain

One public skill owns discovery, duplicate checks, preservation, routing, and
wiki compilation. `second-brain-ingest` is a compatibility name for this same
workflow, not another pipeline. Read the internal
`references/wiki-compilation.md` when processing knowledge sources.

## Resolve the vault and schema first

Find the vault root from the current workspace and its nearest instruction files.
Read `system/schema/llm-wiki.md` relative to that root. It is the authority for
folder conventions, page metadata, provenance, index, log, and ingest/query/lint
workflows. Do not assume a saved Windows or Mac path. If no schema exists in the
target vault, report that gap before changing its structure; never initialize a
second vault to solve a request about an existing one.

## Route first

Identify what is being ingested, then jump to that section. If it is genuinely
ambiguous, ask once. Do not guess and file it somewhere wrong.

| Input | Where it lands | Section |
|---|---|---|
| Web clip from Obsidian Web Clipper (`.md` in `raw/inbox/`) | `raw/inbox/` | [Clips](#clips) |
| A clip that is a YouTube / video page | `raw/inbox/` | [Clips](#clips), read via `watch` |
| Student or consultation session transcript, live or archival | Student records | Delegate to `transcript-intake`; do not compile through this pipeline |
| Superwhisper `recordings/` dirs (`meta.json` + `output.wav`) or `settings.json` | wherever they were dropped | hand to `superwhisper`; not this skill's |
| Student evidence: PT score report, screenshot, homework export | `~/Downloads`, chat attachment | [Student evidence](#student-evidence) |
| A source document meant to become wiki knowledge | `raw/` | dedupe below, then read `references/wiki-compilation.md` |
| Takeout or platform dump | `raw/data-about-me/` | [Bulk exports](#bulk-exports) |

Student/session transcript intake is owned by `transcript-intake`.
Knowledge-source compilation is this skill's internal reference. `post-session-recap`
owns the complete student-facing session write-up workflow. A request only to
retrieve or file a transcript stays narrow; a recap request goes directly to that
skill without asking for a second activation.

## Always, before any pipeline

1. **Find the file without asking where it is.** Search newest-first:
   ```
   raw/inbox/   raw/sources/   ~/Downloads/   ~/Desktop/   students/*/transcript-downloads/
   ```
   Ask only if that comes up empty. He has answered "where is it" too many
   times. `raw/inbox/` is the single intake queue; the old top-level
   `Clippings/` folder was folded into `raw/sources/clips/` on 2026-09-08, so a
   `Clippings/` path in an old note is stale.
2. **Dedupe by SHA-256, not by name.** On Windows use `Get-FileHash` or
   Python `hashlib`. Check existing archive manifests, source-page metadata,
   and dated ingest entries. A matching filename alone is not proof. A matching
   hash with completed wiki output means report the existing output and stop.
   An archived hash without finished output means resume compilation, not
   discard the source. Never delete duplicates.
3. **Check the log and source summary.** Record whether the candidate was
   previously processed and whether this is a new revision. Preserve both
   generations when content changed. A deliberate re-ingest updates the
   existing source page with revision provenance, not a duplicate truth.
4. **Preserve the input byte-for-byte.** Copy external attachments or inbox
   inputs to an appropriate `raw/sources/` archive and verify the SHA-256 before
   citing the preserved copy. Record origin, URL/author/date when known,
   capture date, archived date, filename, size, and hash. Do not move, delete,
   overwrite, or edit original source bytes. Do not follow symlinks outside a
   registered source root. Existing archived inputs can be read in place.

## Clips

Obsidian Web Clipper writes `.md` files to `raw/inbox/`. Anything else sitting
there (a `recordings/` tree, a `settings.json`) is not a clip; route it by the
table above and tell Joshua it was in the wrong place rather than processing it
here.

1. List `raw/inbox/*.md` newest-first. "The latest" means the newest; a named
   topic means match on it; several new ones means list them and ask which.
2. Dedupe (above).
3. Read the clip fully. If it is a video page with no transcript, use the
   appropriate transcript intake workflow; do not treat its thumbnail as evidence.
4. Copy and hash-verify the clip into `raw/sources/clips/<slug>/`, using
   `PROVENANCE.md` and `SHA256SUMS`. Reuse an existing identical archive.
   Preserve the inbox original. Processed status comes from its hash, source
   page, and log, not from whether the original still exists in the inbox.
5. Follow `references/wiki-compilation.md` through the source summary,
   relevant existing pages, index update, log entry, and verification.

One source at a time unless Joshua explicitly asks for batch work. Discuss
important takeaways as part of the work. An explicit instruction to implement,
file, or ingest with a stated focus authorizes completing that scope; do not
introduce an extra confirmation step. Ask when unresolved emphasis, identity,
or contradictory evidence materially changes what should be written.

## Session transcripts use a separate workflow

Student and consultation transcripts go to the sibling
`transcript-intake/SKILL.md`. Delegate the authorized lookup, filing, or
reconciliation there without running this skill's source-summary, wiki-page, or
index-compilation steps. A requested student-facing lesson instead goes directly
to `post-session-recap/SKILL.md`. Do not ask the user to invoke a second skill.

Public lecture transcripts and research interviews supplied as reusable knowledge
remain knowledge sources for `ingest`. Purpose determines the route.

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

- Never move, delete, or modify original sources. Preserve revisions and hashes.
- Never create a student folder without resolving the relationship with Joshua.
- Never hand-edit `*.generated.md`; use its owning generator.
- Dedupe before ingesting. Distinguish archived from successfully compiled.
- Process one source at a time unless batch work is explicitly requested.
- Government IDs stay outside this OS. Do not ingest them.
- Use the current machine's tools and paths, resolved from the vault root.
- No email, platform publishing, or assignment is implied by local ingestion.
- Read current target contents before changing pages. Automated writes only
  modify generated files or fenced generated sections and compare their expected
  hash before writing; on a mismatch, re-read and merge instead of overwriting.
