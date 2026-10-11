---
name: transcript-intake
description: >
  Retrieve, file, and reconcile student or consultation session transcripts,
  including Google Meet Notes by Gemini and archival session files. Use for
  "pull the session transcripts", "file this student's transcript", or
  "reconcile transcripts for this date range". A student-facing lesson belongs
  to post-session-recap; articles and teaching/research sources belong to ingest.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Intake session transcripts into student records

Resolve the current vault from its instructions. Read `students/README.md` and
applicable student instructions before writing. This skill owns session-source
retrieval, filing, reconciliation, and private distillation. It does not compile
session records into the general wiki or create a student-facing lesson.

## Match the requested result

- A lookup, inspection, or question about a transcript stays read-only and narrow.
- Filing preserves the source and records its identity and provenance. Add
  direct local export links to `transcripts.md` and needed student profile-router
  links; do not create a session summary/package unless requested. Do not
  silently add teaching notes when only a source lookup or filing was requested.
- A requested intake/reconciliation window includes filing, private distillation,
  and a session-by-session completion report.
- A recap, session write-up, or student-facing lesson goes to the sibling
  `post-session-recap/SKILL.md` and its complete lesson workflow. Do not ask for
  a second activation when the user already requested that result.
- An article, public lecture transcript, or research document intended as reusable
  knowledge goes to the sibling `ingest/SKILL.md`. Route by purpose, not extension.

## Live Calendar and Drive sources

Use section 1 of the sibling
`post-session-recap/references/transcript-intake-and-record.md` for the shared
Calendar/Drive retrieval procedure only. Resolve sibling paths from the active
skills root. Do not follow its lesson-drafting sections for intake alone.
For a lookup, use the shared procedure only to locate/read the requested source;
do not save an export, create a package, or update records.
Read the runtime's `skills/<runtime>/gws-shared/SKILL.md` from the vault root
(or its available active copy) before using Google Workspace; use the gws CLI.
If this reference is unavailable, report the missing dependency.

Honor the supplied person, source, and date range. Match Calendar guests by email,
check both attached and unattached native Notes by Gemini Docs, and deduplicate by
native Doc ID. Uploaded Markdown copies are not additional sessions. Record the
locations and completed searches actually checked; retain source identity and
SHA-256 provenance with any new local export. Preserve changed generations rather
than overwriting old source bytes. Never create a student folder without approval;
consultations and unknown people follow the existing `_other-sessions` route.

An existing downloaded transcript is not proof of completed processing. Reuse it
and inspect its provenance and dated records. Resume missing distillation or
inventory steps after an interruption; never duplicate completed dated entries.

## Private distillation when requested

For each source in the requested intake window, including previously downloaded
sources whose processing is incomplete:

1. Read the full transcript, not only Gemini's summary. Describe what the record
   supports; do not invent an answer choice or misreading absent from the source.
2. Inspect existing dated teaching notes, open loops, transcript inventory and
   intake evidence before appending. Preserve completed work and resume only
   missing steps. Existing folders may use established session-package formats;
   follow their scoped instructions rather than creating a parallel record.
3. Follow `students/README.md` for the session package (`transcript.md`,
   `summary.md`, `topic-map.md`) and the student profile record router. Preserve
   complete source text, summary history and dated corrections; topic links use
   actual source timestamps when available, never invented timestamps.
4. Append supported teaching observations to `teaching-notes.md` and actionable
   follow-ups to `open-loops.md`. Record student, absolute session date, and source.
   Create a missing standard file from a sibling's structure without copying its
   private contents. Never regenerate old records or hand-edit generated mirrors.
5. Add newest-first direct local export and session-package links under
   `transcripts.md` / `Local session files` if absent, with source/status.
   Link only files that exist and preserve raw-only historical entries.
6. Append a dated intake entry to `wiki/log.md` with actual completion and gaps.
   This operational log entry does not authorize a wiki source-summary or lesson.

## Archival local transcripts

Inventory first; do not read `raw/data-about-me/` wholesale. Use the existing
read-only `system/scripts/transcript-inventory.py` with `--unmatched`, `--json`,
or `--text "<file>.docx"` as needed. Resolve aliases with `students/_aliases.md`;
former students retain their established homes. Preserve original files and
changed generations; deduplicate by source identity and content hash. Apply only
the filing or distillation scope requested above. Unknown recurring-student
relationships require Joshua's decision before creating a folder.

## Finish with an honest reconciliation

Read back changed records, verify source hashes and inventory links, and use
`py system/scripts/check-student-records.py` before calling a student-record intake complete. Report any existing unrelated
validator failures separately. Report each requested session as completed, already complete, source
not found in completed searches, or blocked/incomplete. A cancelled, future or
attendance-uncertain event is not proof that a session occurred.

A failed or incomplete Calendar/Drive search is unresolved, never "no Gemini doc
anywhere". State the failure and unchecked coverage. No lesson drafting, wiki
compilation, posting, assignment, email, or source deletion follows from intake.
