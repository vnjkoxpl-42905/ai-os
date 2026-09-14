---
title: Students — one folder per student
type: operating-layer
tags: [students, operating-layer]
created: 2026-07-03
updated: 2026-09-10
status: active
subject: Students - one folder per student
aliases: []
---

# Students

One folder per student, holding **everything** about them (D2, locked 2026-07-16): transcripts, correspondence, homework, notes, schedules, profile. Open the student's folder and their whole working record is there. This is one of the brain's three knowledge systems, beside [[../wiki/index|wiki]] and [[../corpus/index|corpus]].

## Current students

- [[adriana-varea/adriana-varea|Adriana Varea]] · [[amanda/amanda|Amanda]] · [[asia/asia|Asia]] · [[avneet-natt/avneet-natt|Avneet Natt]] · [[celia-cutler/celia-cutler|Celia Cutler]] · [[charles-moore/charles-moore|Charles Moore]] · [[dakota/dakota|Dakota]] · [[david-salgado/david-salgado|David Salgado]] · [[ethan/ethan|Ethan]] · [[favour/favour|Favour]] · [[fernande-charleus/fernande-charleus|Fernande Charleus]] · [[ivory-johnson/ivory-johnson|Ivory Johnson]] · [[nicole/nicole|Nicole]] · [[ore/ore|Ore]] · [[sofia/sofia|Sofia]] · [[steven-morris/steven-morris|Steven Morris]] · [[vinay-kalva/vinay-kalva|Vinay Kalva]] · [[whit-wilson/whit-wilson|Whit Wilson]] · [[yahunatan-zetvy/yahunatan-zetvy|Yahunatan Zetvy]] · [[zeina-borji/zeina-borji|Zeina Borji]]

**Taught in the last month** (2026-08-08 to 2026-09-08, transcripts pulled 2026-09-08): Celia Cutler (6), Adriana Varea (5), Steven Morris (4), Sofia (2), Vinay Kalva (2), Yahunatan Zetvy (2), Asia (1), Charles Moore (1), Fernande Charleus (1), Whit Wilson (1).

## Former students

Live in [[non-students/CLAUDE|non-students/]] as of 2026-09-10. Records preserved, excluded from every sweep. Read that folder's `CLAUDE.md` before touching anything in it.

## The primary/mirror boundary (D4 — read before regenerating anything)

Every file in a student folder is one of two kinds, and the distinction decides what a rebuild may overwrite:

- **Primary — the brain is the only home.** Transcripts, teaching notes, judgments, prep briefs, study plans, anything Joshua or an agent authored about the student. **Never regenerate, never overwrite; retain forever.**
- **Mirror — a projection of a live backend.** Session/booking state (Cal.com + Google Calendar), homework/dossier/publish state (LSAT U Supabase), payment events (Stripe), correspondence indexes (Gmail). On any disagreement the backend wins, silently.

**Convention:** mirror files MUST be named `*.generated.md` (or carry `generated: true` frontmatter). A file without that marker is primary by definition and must be treated as precious. Pre-2026-07-16 files (`email-context.md`, `payment-links.md`, `transcripts.md`) predate the marker — treat as primary until individually re-derived and renamed. No Markdown file here is ever the source of operational truth — no package balances, no running totals (all services are paid upfront; Cal.com answers sessions-used).

## Standard files per student folder

- `<student-slug>.md` — compact student index and routing page (primary).
- `email-context.md` — synthesized Gmail context.
- `email-correspondence.md` — Gmail message-id corpus for the student's confirmed address.
- `payment-links.md` — verified payment, billing, and scheduling links.
- `transcripts.md` — transcript and meeting-note inventory.
- `teaching-notes.md` — durable, evidence-backed learning judgments and teaching patterns (primary).
- `open-loops.md` — unfinished follow-ups and pending decisions (primary).
- `live-status.generated.md` — refreshable operational summary from Calendar, Gmail, payments, and LSAT U (generated mirror).
- `transcript-downloads/` — full local transcript exports (primary — the brain is their only home).
- `sessions/YYYY-MM-DD-session-name/` — new self-contained session packages.
- `assignment-log.md` — running log of assigned work and notification evidence so repeats are avoided (primary).
- `Practice_Test_Reports/` — the student's PT score reports as received (intake form, screenshots, exports). Raw evidence — read for diagnosis, never edit.
- `Student_Specific_Homework/` — work assigned to this student specifically. Distinct from the shared banks in `corpus/Curriculum/*/Homework/`, which are the source material it draws from.

## Conventions

- New student → new folder `students/<slug>/` with a `<slug>.md` profile page.
- New session → `sessions/YYYY-MM-DD-session-name/` containing `transcript.md`, `summary.md`, and `topic-map.md`.
- `transcript.md` preserves the raw source. `summary.md` records the auto-saved summary, action items, and appended corrections. `topic-map.md` is a timestamped link index to relevant LSAT concepts, student records, and source material.
- Session summaries are append-only. Later corrections go in a dated correction section and never erase the original summary.
- Generated operational state is clearly marked with `generated: true` and never overrides primary teaching records.
- Wikilink student pages into corpus concepts and LSAT U material as they become relevant.
- Tier A note: transcripts and correspondence are trackable (Tier-A amendment, 2026-07-16). True secrets (credentials, IDs, payment instruments) still never enter Git — `private/` only.

## Operating contract

For each new consultation or transcript, Jay 2 must report what was found, what was created or updated, what was inferred, what remains missing, what is recommended, and what Joshua should confirm or reject. During the learning period, no student-facing message, assignment, or platform action is implied by record preparation alone.
