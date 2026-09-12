---
type: reference
subject: Automation & Workflow Analysis Joshua's tutoring operation
updated: 2026-07-20
aliases: []
---

# Automation & Workflow Analysis — Joshua's tutoring operation

**Built:** 2026-07-18. **Source:** 944 emails Joshua authored (mid-2025 → mid-2026, from the Gmail takeout) + the current skill library + business structure. **Status:** analysis + build backlog.

## Build status (updated 2026-07-20)

| Item | Status |
|---|---|
| **A. Morning brief** | **Built** — `morning-brief` skill. Drafts only, payment flag-only, logs to `wiki/send-ledger.md`. **Not yet scheduled** — runs on request until Joshua opts into a cron. |
| **B. Reschedule assistant** | Not built. Now the highest-leverage remaining item (25% of his mail). |
| **C. Payment follow-up** | Not built. `morning-brief` deliberately flags payment rather than drafting it, so this stays a conscious gap. |
| **D. Session-notes ingest** | **Built** — `ingest` skill + `system/scripts/transcript-inventory.py`. Maps 44 of 52 transcripts; the rest are named gaps, not failures. |
| **E. Student roster** | **Built** — `system/scripts/build-roster.py` → `students/roster.generated.md`. Implemented as a generated markdown table rather than an Obsidian Base, since the data is small and a script is portable to Codex. |
| **F. Gone-quiet detector** | Not built, but now cheap: the roster carries last-session dates, which is the data it needed. |

The apology-tax finding below (19%) is what ranked A first; the session-mining
sweep in `brainstorms/2026-07-19-session-mining-reflection.md` independently
re-derived the same ranking.

This is a map of how Joshua actually spends his email/ops time and where a skill, workflow, or automation removes or assists that work. It separates what's a real GAP (build it) from what's already COVERED (a skill exists — the job is to use or sharpen it). Read this before building anything so you don't duplicate the existing library.

---

## 1. What the corpus shows about his workload

944 authored messages, classified by workflow (messages can hit more than one category):

| Workflow | Msgs | Share | Mechanical? |
|---|---|---|---|
| Scheduling / calendar | 239 | 25% | High — reschedules, invites, availability |
| Homework delivery | 185 | 20% | Medium — per-student judgment + a link |
| Encouragement / check-in | 167 | 18% | Low — genuine, but templatable openers |
| **Apology / delay** | **181** | **19%** | High — he is chronically behind on replies |
| Consultation (reminder + follow-up) | 152 | 16% | High — near-identical templates |
| Inbound lead reply | 91 | 10% | High — same "yes I'm available, here's the link" |
| Payment / billing | 71 | 8% | High — invoices, payment nudges |
| Session notes / recap | 47 | 5% | Medium — depends on his notes |

**Relationship shape:** 155 distinct recipients. 43 are active relationships (≥5 messages) — the real student book. 71 are one-offs (leads/prospects who emailed once). So ~half his inbound is lead traffic that never converts, and he still hand-replies to it.

**The headline finding:** **19% of everything he writes is an apology for being slow to reply.** That is not a voice problem, it's a throughput problem. The single highest-leverage automation is anything that keeps him from falling behind on his inbox in the first place. Speed of reply is the bottleneck, not quality.

---

## 2. Already COVERED (don't rebuild — use or sharpen)

He has a strong library already. These map directly onto the workflows above:

- **`consultation-inquiry-drafts`** — daily sweep, drafts consultation-link replies to new inquiries. Covers most of "inbound lead reply."
- **`consultation-followup-drafts`** — daily, drafts follow-ups from consultation Gemini notes. Covers "consultation follow-up."
- **`inbound-tutoring-replies`** — drafts replies to leads across channels (FB, Superprof, TutorOcean, Reddit, email).
- **`guided-drill-assignment`** + **`lsat-u-platform-actions`** — transcript → pick a drill → assign on-platform → verify notification. Covers the platform side of "homework delivery."
- **`gws-*` suite** (gmail-triage, gmail-reply, gmail-send, calendar-insert, calendar-agenda, drive, docs, workflow-meeting-prep, workflow-weekly-digest, etc.) — the primitives for almost any email/calendar/drive automation already exist. Most gaps below are *orchestration* over these, not new capability.

**Implication:** the gap is less "build new skills" and more "wire the existing ones into a daily rhythm that runs without him asking." A lot of these are described as "daily" but require him to invoke them. The leverage is making them proactive.

---

## 3. The GAPS — ranked by leverage (build these)

Leverage = (time saved or dropped-ball prevented) × (frequency) × (how mechanical). Highest first.

### TIER 1 — build first

**A. Daily inbox triage + draft queue ("morning brief").**
The fix for the 19% apology problem. One scheduled run each morning that: sweeps Gmail for anything needing a reply, classifies it (lead / active student / logistics / payment / consultation), and produces a single ranked queue of *drafts* — using the existing consultation/inbound skills where they apply, and the newly-enriched `wiki/teaching-voice.md` for tone. He reviews and sends. Never auto-sends (his rule). This collapses "I'm behind on email" into a 15-minute daily review.
- *Builds on:* `gws-gmail-triage`, `gws-gmail-read`, the three drafting skills, `teaching-voice.md`.
- *New work:* the orchestration + classification + a single digest surface. Consider a scheduled cloud agent (`/schedule`) so it runs before he wakes up.

**B. Reschedule / scheduling assistant.**
25% of his mail. When a student asks to move a session, the move is: check the calendar, propose/confirm a slot, send the invite, update anything downstream. Highly mechanical, currently all hand-done.
- *Builds on:* `gws-calendar-agenda`, `gws-calendar-insert`, Cal.com.
- *New work:* a skill that reads a reschedule request, checks availability, and drafts the confirmation + invite in his voice ("No worries at all. It happens...").

**C. Payment / billing follow-up.**
71 messages, and money that slips is money lost. A skill that tracks who owes what (from Stripe + invoice emails) and drafts the gentle nudge.
- *Builds on:* Stripe connection (in `connections.md`), `gws-gmail`.
- *New work:* reconcile sessions-delivered vs. paid, surface gaps, draft the reminder. Sensitive — draft only, never auto-send.

### TIER 2 — build next

**D. Session-notes → student-folder ingest (the deferred transcript pipeline).**
The 184 Gemini Doc transcripts + ongoing ones. Parse the `gemini-notes@google.com` subjects (student + date), fetch each Doc via `gws drive`, distill to a note, file into `students/<name>/`. This is the pipeline scoped in the prior handoff but not built. Turns his recorded sessions into durable per-student memory.
- *Builds on:* `gws-drive`, `gws-docs`, `second-brain-ingest`, the student-folder structure.
- *Note:* notes ≠ transcript ≠ homework (per the prior handoff's reframe). File them distinctly.

**E. Student roster + status dashboard.**
He has 43 active students scattered across email threads. No single view of who's active, who's gone quiet, who's owed a reply, when they last met, what's assigned. A generated dashboard (an Obsidian Base over `students/`) answers "where does everyone stand" at a glance.
- *Builds on:* `obsidian-bases`, the student folders (once D populates them).

**F. "Gone quiet" re-engagement detector.**
Cross-reference last-contact date per active student; flag anyone who's dropped off and draft a warm check-in ("hope all is well..."). Catches revenue/retention leaks he'd otherwise miss.
- *Builds on:* E's data + `teaching-voice.md` check-in register.

### TIER 3 — nice to have

**G. Homework-delivery assistant.** Given a student + what they worked on, draft the homework email with the right drill link. Partly covered by `guided-drill-assignment` (the platform side); the gap is the *email* wrapper in his voice.

**H. Consultation prep brief.** Before a consultation, assemble a one-pager on the prospect from prior email/inquiry so he walks in informed. (`gws-workflow-meeting-prep` may already do most of this — check before building.)

**I. Weekly ops digest.** What happened this week: sessions run, new leads, conversions, payments, who's owed follow-up. `gws-workflow-weekly-digest` exists — likely just needs pointing at his data.

---

## 4. Cross-cutting principles for whoever builds these

- **Draft, never send.** Joshua's hard rule: nothing to a student or prospect goes out without his review, unless it's a pre-approved template. Every automation here ends at a draft queue.
- **Route all student-facing copy through the enriched `wiki/teaching-voice.md`** (updated 2026-07-18 from this same corpus — real openings, sign-offs, signature phrases, situational templates).
- **Save-to-both.** Every new skill goes to the project `.claude/skills/` AND the DB (`skills/{claude,codex}/`), per the standing rule.
- **Prefer orchestration over new primitives.** The `gws-*` suite already covers Gmail/Calendar/Drive/Docs/Sheets. Most gaps are wiring, not new capability.
- **Scheduled where it should be proactive.** The morning brief (A) and quiet-detector (F) lose most of their value if he has to remember to run them. Use `/schedule` (cloud cron agents) so they run on their own and present him a queue.
- **The north star:** kill the 19% apology tax. Every hour of email he doesn't have to initiate is an hour toward teaching and building. Speed and never-dropping-a-ball beat polish.

---

## 5. Suggested build order for the next session

1. **A — morning inbox brief + draft queue** (highest leverage; attacks the apology tax directly).
2. **D — session-notes ingest** (unlocks E, F, H by populating student folders with real history).
3. **B — reschedule assistant** (25% of mail, very mechanical).
4. **E — student dashboard**, then **F — quiet detector** (retention).
5. **C — billing follow-up** (revenue protection; build carefully, it touches money).

Start by confirming with Joshua which of these he actually wants, and whether "draft queue" should be an email he gets, an Obsidian note, or a chat surface. Then build ONE, end to end, save-to-both, before moving to the next. (The `level-up` skill is exactly the right harness for shipping these one at a time.)

---

## 6. Addendum — 2026-07-19 full-takeout validation (Jay 2 deep analysis)

Re-ran the analysis over the complete takeout in `data about me /` (full 3,318-message mbox, main calendar ICS with 662 events, 9.1GB Drive dump). The 2026-07-18 findings hold; new evidence sharpens the priorities:

- **The funnel just surged.** The calendar shows ~25 prospect consultations between Jul 7 and Jul 21 (vs. a handful per month before). As of the Jul 16 export, consult follow-ups had gone out to Kaia, Lexi, Aastha, Luc, Taylor, Favour, Katie, Rumaysa, Liz, Netta, and YahuNathan — but **Susan (7/13), Muhammad (3 separate consults), Alexandria Strickland (7/10), and Mehvish Naqvi (7/14) show no follow-up in the corpus.** Each consult's Gemini note literally ends with "[Joshua] Send Follow-up" as a next step. Item A (morning brief) + item H (consult prep/follow-up) are now the same fire: a consultation-to-conversion pipeline is the top revenue automation.
- **Transcript debt quantified.** 52 Gemini Meet notes recovered from Drive and sorted (copies) into `data about me /transcripts-sorted/{students,consultations,unidentified}/<person>/`. Active students Lydia (8), Meghan (5), David (5, incl. two identified from "Meeting started" files), Dakota (7), Ethan (2), Sofia (5), Nicole (1), Bella (2) — plus non-vault people Adriana (4), Andrew, Thaniuska. Only Dakota/Sofia/Bella/C-Alexander have any transcripts ingested in `students/`. 3 notes remain unidentified (2026-05-19 13:23, 2026-06-04 18:20, 2026-06-19 13:12) — ask Joshua.
- **Roster gap.** `students/` holds 10 folders, but email + calendar show 20+ active or recent paying relationships (Elias, Dillen, Kristine, Queen, Fiorella, Glenn, Kevin, Malaya, Sabrina, Sonja, Mounusha, Richard, Armando, Om, …). Item E (roster/dashboard) can't work until the roster itself is complete.
- **Inbox state:** 761 of 3,318 messages carry the Unread label; 122 Cal.com notifications confirm scheduling as the top mechanical stream.
- **Business thread to not drop:** an active LSAC content-licensing conversation (`lweil@lsac.org`, "New Content Licensing Interest Form Submission") — strategic, multi-reply, deserves a tracked open loop.
