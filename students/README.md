---
title: Students — one folder per student
type: operating-layer
tags: [students, operating-layer]
created: 2026-07-03
updated: 2026-09-25
status: active
subject: Students - one folder per student
aliases: []
---

# Students

One folder per student, holding **everything** about them (D2, locked 2026-07-16): transcripts, correspondence, homework, notes, schedules, profile. These are internal working records for Joshua, Claude, and Codex, not pages for students to open. Open the student's folder and their whole working record is there. This is one of the brain's three knowledge systems, beside [[../wiki/index|wiki]] and [[../corpus/index|corpus]].

## Current students

- [[adriana-varea/adriana-varea|Adriana Varea]] · [[amanda/amanda|Amanda]] · [[asia/asia|Asia]] · [[avneet-natt/avneet-natt|Avneet Natt]] · [[celia-cutler/celia-cutler|Celia Cutler]] · [[charles-moore/charles-moore|Charles Moore]] · [[dakota/dakota|Dakota]] · [[david-salgado/david-salgado|David Salgado]] · [[ethan/ethan|Ethan]] · [[favour/favour|Favour]] · [[fernande-charleus/fernande-charleus|Fernande Charleus]] · [[gianna/gianna|Gianna Jean]] · [[ivory-johnson/ivory-johnson|Ivory Johnson]] · [[nicole/nicole|Nicole]] · [[ore/ore|Ore]] · [[sandra/sandra|Sandra Kooh]] · [[sofia/sofia|Sofia]] · [[steven-morris/steven-morris|Steven Morris]] · [[venusa-laveaux/venusa-laveaux|Venusa Laveaux]] · [[vinay-kalva/vinay-kalva|Vinay Kalva]] · [[whit-wilson/whit-wilson|Whit Wilson]] · [[yahunatan-zetvy/yahunatan-zetvy|Yahunatan Zetvy]] · [[zeina-borji/zeina-borji|Zeina Borji]]

**Taught in the last month** (2026-08-08 to 2026-09-08, transcripts pulled 2026-09-08): Celia Cutler (6), Adriana Varea (5), Steven Morris (4), Sofia (2), Vinay Kalva (2), Yahunatan Zetvy (2), Asia (1), Charles Moore (1), Fernande Charleus (1), Whit Wilson (1).

## Former students

Live in [[non-students/CLAUDE|non-students/]] as of 2026-09-10. Records preserved, excluded from every sweep. Read that folder's `CLAUDE.md` before touching anything in it.

## The primary/mirror boundary (D4 — read before regenerating anything)

Every file in a student folder is one of two kinds, and the distinction decides what a rebuild may overwrite:

- **Primary — the brain is the only home.** Transcripts, teaching notes, judgments, prep briefs, study plans, anything Joshua or an agent authored about the student. **Never regenerate, never overwrite; retain forever.**
- **Mirror — a projection of a live backend.** Session/booking state (Cal.com + Google Calendar), homework/dossier/publish state (LSAT U Supabase), payment events (Stripe), correspondence indexes (Gmail). On disagreement, the verified backend governs operational state. Preserve and report the discrepancy with its evidence rather than silently erasing a conflicting primary record.

**Convention:** mirror files MUST be named `*.generated.md` (or carry `generated: true` frontmatter). A file without that marker is primary by definition and must be treated as precious. Pre-2026-07-16 files (`email-context.md`, `payment-links.md`, `transcripts.md`) predate the marker — treat as primary until individually re-derived and renamed. No Markdown file here is ever the source of operational truth — no package balances, no running totals (all services are paid upfront; Cal.com answers sessions-used).

## Standard files per student folder

This is the target layout, not a checklist to satisfy with empty files. Create a record when its source or a real teaching judgment supports it. Leave an absent record absent until there is verified content to put in it.

- `<student-slug>.md` — internal entry page and folder router (primary). Its `## Open this record` block links only to local files that exist.
- `email-context.md` — synthesized Gmail context.
- `email-correspondence.md` — Gmail message-id corpus for the student's confirmed address.
- `payment-links.md` — verified payment, billing, and scheduling links.
- `transcripts.md` — transcript and meeting-note inventory. Its `## Local session files` table links directly to every full local Markdown export and every session package, newest first. A Google Doc link is provenance, never the only way to read a session.
- `teaching-notes.md` — durable, evidence-backed learning judgments and teaching patterns (primary).
- `open-loops.md` — unfinished follow-ups and pending decisions (primary).
- `live-status.generated.md` — currently a refreshable LSAT U booking-pass mirror. Calendar, Gmail, and payment state remain in their live systems; this file does not yet summarize them.
- `transcript-downloads/` — preserved local exports of Gemini notes (source evidence; do not hand-edit). A raw export here is not itself a completed session package.
- `sessions/YYYY-MM-DD-session-name/` — new self-contained session packages.
- `assignment-log.md` — running log of assigned work and notification evidence so repeats are avoided (primary).
- `Practice_Test_Reports/` — the student's PT score reports as received (intake form, screenshots, exports). Raw evidence — read for diagnosis, never edit.
- `Student_Specific_Homework/` — work assigned to this student specifically. Distinct from the shared banks in `corpus/Curriculum/*/Homework/`, which are the source material it draws from.

## Conventions

### Connect a student observation to shared teaching knowledge

Use [tutoring diagnosis](../corpus/tutoring-diagnosis.md) as a hypothesis framework when reviewing an actual session or score report. Keep what the person said or did, Joshua's judgment and the resulting follow-up in their own teaching notes and open loops. Link the appropriate shared [corpus method](../corpus/index.md), including the recovered [RC recall check](<../corpus/Curriculum/Reading Comprehension/Notes/cumulative-translation-review.md>) when evidence supports it. Apply [Joshua's teaching voice standard](../references/lsat-teaching-voice-standard.md) to student-facing adaptations. A general source never establishes a diagnosis, assignment or commitment by itself.

- New student → new folder `students/<slug>/` with a `<slug>.md` profile page.
- A consultation followed by a subsequent student session establishes onboarding. Check the Calendar sequence and identity before creating the folder; record any uncertainty about attendance or contact aliases. Consultation-only records stay in `_other-sessions/`.
- When Joshua explicitly says a student relationship is over or to close a folder, move the preserved record to `students/non-students/<slug>/`, remove it from the current student index, and refresh the generated roster. Do not delete the record or silently infer closure from inactivity.
- New session → `sessions/YYYY-MM-DD-session-name/` containing `transcript.md`, `summary.md`, and `topic-map.md`.
- Keep the original full Gemini export as a local Markdown file in `transcript-downloads/` when available. Build the session package from verified session evidence, and link both the export and package from `transcripts.md`; older exports may predate the package convention.
- `transcript.md` preserves the raw source. `summary.md` records the auto-saved summary, action items, and appended corrections. `topic-map.md` is a timestamped link index to relevant LSAT concepts, student records, and source material.
- Session summaries are append-only. Later corrections go in a dated correction section and never erase the original summary.
- Generated operational state is clearly marked with `generated: true` and never overrides primary teaching records.
- Wikilink student pages into corpus concepts and LSAT U material as they become relevant.
- Tier A note: transcripts and correspondence are trackable (Tier-A amendment, 2026-07-16). True secrets (credentials, IDs, payment instruments) still never enter Git — `private/` only.

## Internal routing contract after each session

1. Match the Calendar event and Gemini Doc by guest email, date, and content. Preserve the complete source export in `transcript-downloads/`; never rely on a Drive link as the record.
2. Create or update the session's `sessions/YYYY-MM-DD-session-name/` package without replacing a primary transcript or summary. Record any source mismatch as a dated correction.
3. Add a newest-first row to `transcripts.md` under `## Local session files`: date, direct local full-export link, local package links, and source/status. Include raw-only historical exports and packages even when the other half is absent.
4. Update evidence-backed `teaching-notes.md` and `open-loops.md`. Refresh the student's `<slug>.md` `## Open this record` block so Joshua, Claude, and Codex can reach the latest work in two clicks. Link only to files that exist.
5. Check that all local links resolve, that the full Markdown export contains the transcript rather than only Gemini's summary, and that the session index has no unlinked export or package. Leave attendance and missing-source uncertainty explicit.
6. Run `python system/scripts/check-student-records.py` from the repo root before calling intake complete. It checks all student routers and every local Markdown export and session package link.

## Operating contract

For each new consultation or transcript, Jay 2 must report what was found, what was created or updated, what was inferred, what remains missing, what is recommended, and what Joshua should confirm or reject. During the learning period, no student-facing message, assignment, or platform action is implied by record preparation alone.
