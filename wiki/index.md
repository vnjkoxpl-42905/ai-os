---
type: operating-layer
subject: Index
updated: 2026-10-10
aliases: []
---

# Index

Content catalog of the wiki. Curated navigation appears first; the complete catalog below lists every wiki Markdown page by category. The LLM updates this on every ingest; read it first when answering a query, then drill into pages. Rebuilt fresh 2026-07-16 (Karpathy LLM-wiki rebuild; prior wiki preserved at `archive/wiki-pre-rebuild-2026-07-16/`).

The brain runs three knowledge systems: **this wiki** (Joshua, the business, decisions), **[corpus](../corpus/index.md)** (LSAT teaching knowledge), **[students](../students/README.md)** (one folder per student).

[Private teaching lecture library](../corpus/lectures/index.md): reusable teacher teleprompters, Socratic prompts, boards, and worked questions, routed by Logical Reasoning/Reading Comprehension, topic, and Core/Advanced. Ask for "Core Must Be True," "applying facts to rules," or "linking rules" to retrieve the saved lecture.

## How this wiki is maintained

- [[system/schema/llm-wiki|LLM Wiki operating schema]]: folder conventions, provenance, ingest, query, index/log maintenance, and lint.
- [[wiki/sources/llm-wiki-pattern|First ingest example]]: preserved idea file, factual summary, and linked concept.

## Hubs

<!-- DESIGN HUB NAVIGATION -->
[Design hub](../design/README.md): shared Claude Code/Codex router for design clips, methods, skills, component repositories, research and visual work.
<!-- END DESIGN HUB NAVIGATION -->

- [[component-library]] — saved UI components from 21st.dev (carousels, stepper, deck showcase), where they live, how to view and add them
- [[tasks]] — living Now / Next / Done work ledger; `/pickup` reads it first (content carried from the pre-rebuild ledger)
- [[hot]] — last-session cache and automation alerts; rebuilt fresh
- [[log]] — append-only history of ingests, queries, and lint passes; started fresh (old log archived)
- [[wiki/second-brain-setup-playbook|Second brain setup playbook]] — plain library picture of the vault, ten top-tier practices ai-os does not do yet, and the recommended direction (2026-11-20)
- [[wiki/second-brain-one-vault-vs-many|One vault or several]] — second-brain source consensus on vault count, what ai-os has and lacks, and the open split decision (2026-11-20); its source pages: [[wiki/sources/every-level-of-a-claude-second-brain-nate-herk|five levels]], [[wiki/sources/steal-my-ai-os-setup-5-tips-nate-herk|five tips]], [[wiki/sources/agentic-os-setup-10x-claude-code-chase-ai|Chase AI four levels]], [[wiki/sources/new-agentic-os-standard-claude-5-robonuggets|ARMS ladder]], [[wiki/sources/self-improving-claude-knowledge-base-one-prompt-robonuggets|one-prompt KB]], [[wiki/sources/new-way-build-second-brain-claude-nick-saraev|Engram]], [[wiki/sources/grill-me-skill-10x-claude-code-nate-herk|grill-me]]
- [[dashboard]] — product ground-truth pointers; regenerable, backends are authority
- [[lovable-cloud]] — what the Lovable Cloud backend can do, Jay 2's reach vs Lovable-only operations, and the export escape hatch
- [[lsatu-backend-map]] — live DB structure: 82 tables by domain, RPCs, triggers, RLS posture, cron; reuse flags for new features

## Entities

- [[entities/aspiring-attorneys]] — the tutoring business: who Joshua is, offers, pricing channels, tools, priorities, gaps (seeded from the 2026-07-16 onboarding intake)

## Voice & policy

- [[teaching-voice]] — canonical voice doc with coaching, teaching-content, and brand registers; LSAT material uses Joshua's selected 2026-10-02 source standard
- [LSAT teaching voice standard](../references/lsat-teaching-voice-standard.md): detailed wording, cadence, questions, lesson progression, original calibration examples, and review rubric; [source summary](sources/conditional-reasoning-voice.md). The [conditional content-order skeleton](../brainstorms/2026-09-30-conditional-curriculum/2026-10-02-opening-lessons-source-map.md) records Joshua's 2026-10-03 selection of the full supplied sequence.
- [Conditional Bootcamp coverage and proposed chapter map](../brainstorms/2026-09-30-conditional-curriculum/material-inventory.md#2026-10-25-organize-the-whole-bootcamp-from-the-source-material): source-backed homes for Groups 1–4, AND/OR, two-way rules, facts, linking, quantity reasoning and LSAT applications; distinguishes existing material, local drafts, overlap and remaining gaps.
- [[ACCOMMODATIONS-REQUEST-TEMPLATE]] — approved LSAT accommodations email (sent by the accommodations-email skill, QP form attached) + LSAC deadlines and category notes
- [[reddit-chat-voice]] — ground truth reference of 10 real Reddit chat conversations, tone patterns, and DM dispatch standards
- [[HANDLING]]: current credential/data policy and advisory remote checks, aligned with the root manuals.
- [[protected-records]]: current storage routes and the explicitly retired encrypted-bundle design.

## Operations

- [LR explanation fix ledger](../corpus/lr-explanations/fixes/index.md): Step 3 accounts for all 192 Revamp items; Step 4 records guarded correctness edits, source adjudication and unresolved quality work.
- [Homework assigning hub](homework-assigning/README.md): everything assigned to every student (export, note archive, by-topic lookup, playbook) and the per-student packages for [Sofia](../students/sofia/assigned-work/README.md) and [Celia](../students/celia-cutler/assigned-work/README.md); first pass 2026-11-14
- [[guided-drill-verification-log]] — living QA log of guided drills verified to launch on the platform (restored from the pre-rebuild archive 2026-07-16; skills cite it before re-verifying)
- [[lr-missing-explanations]] + [[lr-missing-explanations-by-category]]: the 772 LR questions with no, partial, or never-loaded explanations (PT/S/Q list, then by type, reasoning, feature, difficulty); snapshot 2026-09-26
- [[../corpus/lr-explanations/golden-set|LR golden set]]: the 50 model explanations (and rubric) the missing ones are written from; 2026-09-26
- [[automation-backlog]] — how Joshua's email/ops time actually breaks down (from 944 authored emails) + the leverage-ranked build backlog; the 19% "apology tax" is the north-star target. Walked by `/level-up`

## References (OS method / meta)

- [Matt Pocock skills field guide](../references/matt-pocock-skills-field-guide.html): interactive catalog of all 39 tracked skills, with workflows, sample requests, source status, and skill combinations.
- [Stripe API access](../references/stripe-api.md): verified account-read route while the connected app requires reauthentication.
- [Audit repair outcome](../research/audit-repairs-2026-10-08/outcome.md): corrected rules, routes, skills, diagnostics and remaining decisions.
- [Recovered historical evidence](../research/audit-repairs-2026-10-08/lint-cal-repair.md): surviving dated app documents for retired worktree citations; old wiki history remains unchanged.
- [Prepared Obsidian sync plan](../research/audit-repairs-2026-10-08/obsidian-sync-plan.md): current vault is disconnected, existing remote is separate, and candidate working content is small enough for selective sync.

- [AI workspace knowledge hub](../references/ai-workspace/index.md): Claude/Codex updates, skill ideas, repository evaluations, prompts, tips and workflows, kept separate from LSAT teaching.
- [Recovered AI methods](../references/ai-workspace/migrated-source-methods.md): detailed review, skill-evaluation and source-checking recipes from the old vault.
- [Completed old-vault migration](../research/obsidian-vault-comparison/2026-10-07/migration-outcome-2026-10-08.md): all 100 original file dispositions, useful active homes, exact exclusions and unimplemented structural suggestions.
- [Loophole library](../corpus/loophole-online/README.md): start here for separate [RC](../corpus/loophole-online/reading-comprehension/README.md), [LR](../corpus/loophole-online/logical-reasoning/README.md), and [shared methods](../corpus/loophole-online/shared/README.md). The [AI retrieval guide](../corpus/loophole-online/AI-RETRIEVAL.md) gives Codex and Claude the same bounded local search and citation lookup. The [router](../corpus/loophole-online/ROUTER.md) and [complete source catalog](../corpus/loophole-online/source-catalog.generated.md) connect recovered references, 59 RC lectures, the new How to Camo transcript, exact notes, 84 workouts, 58 routines, prep-map captures and the local LR recording/transcript library. Attributed teacher research remains separate from approved curriculum.

- [[../references/second-brain-levels]]: retrieval architecture, dated comparison, current domain routes and sync limitations.
- [Second-brain adoption ledger](../references/ai-workspace/second-brain-adoptions.md): outside setups (GD4AI plugin, Nate Herk, Chase AI, Dan Martell, Austin Marchese) weighed against ai-os on 2026-10-14; what was built, what waits on Joshua, what was declined.
- [[../references/obsidian-command-center]]: attributed command-center methods, historical plugin research and device-verification limits.
- [[../references/claude-plus-codex]] — running Claude Code + Codex on one project; shared-file architecture, plan/critique workflow, and the installed Herdr session layer for visible, persistent dual-agent execution
- [[../references/graphify-obsidian-bridge]] — turning any corpus into a linked concept map in the vault (`--obsidian`); the source-wiring step and the fragmentation trap that silently guts the result
- [[../references/3ms-framework]] — the Three Ms operator brain (walked weekly by `/level-up`)
- [Website planning](../references/website-design-planning.md): recovered visitor-journey, asset-planning and rendered-review methods.
- [Older vault comparison](../research/obsidian-vault-comparison/2026-10-07/report.md), [historical every-file dispositions](../research/obsidian-vault-comparison/2026-10-07/excluded-from-active-knowledge.md), and [current organization audit](../research/obsidian-vault-comparison/2026-10-07/organization-audit-2026-10-08.md): recovered knowledge, authorized cleanup, overlap, conflicts and verification limits.
- [Cal.com stuck bookings](CALCOM-STUCK-BOOKINGS.md) — unpaid bookings hold slots invisibly; run scripts/calcom-pending-sweep.mjs
- [LSAT U booking policy](LSATU-BOOKING-POLICY.md) — one generator, one predicate, one config row; mirrors Cal.com session-link (buffer 10, pitch 80, 45 days)

- `superwhisper/` (vault root): dictation setup, source of truth for Superwhisper vocabulary, replacements, and modes; `sync.py` pushes it to the app. Research report inside. Ledger: [[SUPERWHISPER-DICTIONARY]].

## Source implementation routes (2026-10-26)

- [Implemented source ideas and the remaining queue](../research/2026-10-26-source-implementation/REPORT.md).
- [Compiled retrieval helper](../references/ai-workspace/compiled-retrieval.md): bounded evidence sections, stale checks and measured limits.
- [Operating inventory](../references/ai-workspace/operating-inventory.md): selected applications, routines, memory and skill owners.
- [Teacher-only RC source-adoption tools](../references/rc-source-adoption-checklist.md): recall observation, vocabulary, whole-choice evaluation and comparative evidence forms.
- [MCAT question adjudications](../corpus/reading-center/mcat-question-adjudication-2026-10-26.md): twelve decisions with original keys, two quarantined items and unverified rights.

<!-- BEGIN GENERATED WIKI CATALOG -->

## Complete wiki catalog

Every Markdown page under `wiki/` is listed below, except generated captures under `wiki/sources/karpathy/*/`,
which are listed in their folder's `catalog.generated` page (3831 pages collapsed here).
Regenerate this section after page changes with `py system/scripts/wiki-maintenance.py --index`.

### Operating pages

- [[wiki/ACCOMMODATIONS-REQUEST-TEMPLATE|Accommodations request email]]: The email Joshua sends a student after they've talked through LSAT testing accommodations.
- [[wiki/ACTIVE-STUDENTS-LAST-MONTH-2026-09-08|Active students, last month : 2026-08-08 to 2026-09-08]]: Pulled 2026-09-08 from the calendar (82 events) and Drive (40 Gemini docs).
- [[wiki/ASSIGN-AN-ACTIVITY|Assign an Activity : the runbook]]: The repeatable path for putting an LSAT U Activity into a student's hands.
- [[wiki/automation-backlog|Automation & Workflow Analysis : Joshua's tutoring operation]]: Related: entities/aspiring-attorneys · teaching-voice · ../skills/INDEX · ../references/3ms-framework
- [[wiki/CALCOM-STUCK-BOOKINGS|Cal.com stuck bookings]]: When a student says scheduling or payment "isn't working", first ask **which link**. A
- [[wiki/CELIA-RRC-REPLY-DRAFT-2026-09-08|Celia · reply to "still being marked" (DRAFT, not sent)]]: Channel: LSAT U platform message, from Joshua's admin account. Send via the assign-lsatu-work skill only after Joshua approves the text.
- [[wiki/component-library|Component library: where the saved UI components live]]: Joshua's saved UI components sit in one folder outside this vault: `C:\Users\Joshu\dev\component-library`. Like app code, it stays outside the vault on purpose. This page is the po
- [[wiki/CONSULTATION-FOLLOW-UP-TEMPLATE|Consultation follow-up email]]: The email Joshua sends after a free consultation. Reconstructed 2026-09-11 from the
- [[wiki/contrapositive-teaching|Contrapositive: how Joshua teaches it]]: Gathered 2026-10-11 from his own session transcripts (Gemini auto-notes, raw ASR, so quotes are near-verbatim and unchecked against audio). Use this before writing any contrapositi
- [[wiki/COPY-CORRECTIONS|Copy corrections]]: Every student-facing wording fix, with the reason it was wrong. Read this before
- [[wiki/dashboard|Dashboard : ground-truth pointers]]: Rebuilt fresh 2026-07-16. This page points at authorities; it never accumulates state itself (D4: live systems are authority, the brain mirrors, backend wins on conflict).
- [[wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2|Drill hub: impeccable audit and critique, run 2 (2026-09-08)]]: Second pass after the fixes from DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08 shipped (commits 211d982, 1d1d351, f4cf062, f791016, published to lsatprep.study). Measured live on productio
- [[wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN3|Drill hub, run 3]]: Written 2026-09-09 by Claude (Opus 5), executing DRILL-HUB-PERFECT-SCORE-PLAN-2026-09-08 from Part 1g. Run 2 is DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2: audit 16/20, critique 31
- [[wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08|Drill hub: impeccable audit and critique (2026-09-08)]]: Target: `/classroom/drill` on production (lsatprep.study), signed in as Joshua. LR section, default stage, the Build a Set launcher stage, desktop (~740px pane) and phone (375px).
- [[wiki/DRILL-HUB-PERFECT-SCORE-PLAN-2026-09-08|Drill hub: plan to reach 20/20 audit and 40/40 critique]]: Written 2026-09-08 by Claude (Fable 5.1) for hand-off to another executor. Starting point: run 2 of DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2, published as commit f791016. Audit 1
- [[wiki/guided-drill-verification-log|Guided Drill Verification Log]]: Running log of guided drills that have already been verified in the live platform. Once a drill is listed here as `verified-working`, do not repeat full browser launch QA before as
- [[wiki/HANDLING|Personal-data handling]]: The 2026-07-17 design initially described API keys only. The current root policy explicitly includes credentials and bank/account information in the git-ignored `.env`. This is a d
- [[wiki/hot|Hot : last-session cache]]: Freshest working state; the first page `/pickup` reads. Rebuilt fresh in the 2026-07-16 vault rebuild (the old cache is archived).
- [[wiki/inbound-handled-ledger|Inbound handled ledger]]: Append-only and stateful record of inbound messages, questions, and inquiries across platforms (LSAT U, Reddit, 7Sage, Facebook).
- [[wiki/IVORY-REPLY-DRAFT-2026-09-08|IVORY-REPLY-DRAFT-2026-09-08]]: Hi Ivory,
- [[wiki/log-archive-2026-07|Log archive 2026-07]]: Entries moved unchanged from wiki/log on 2026-11-20. Newest log entries stay in `wiki/log.md`.
- [[wiki/log-archive-2026-09|Log archive 2026-09]]: Entries moved unchanged from wiki/log on 2026-11-20. Newest log entries stay in `wiki/log.md`.
- [[wiki/log-archive-2026-10|Log archive 2026-10]]: Entries moved unchanged from wiki/log on 2026-11-20. Newest log entries stay in `wiki/log.md`.
- [[wiki/log|Log]]: Entries before 2026-11 live in `wiki/log-archive-YYYY-MM.md` (moved unchanged 2026-11-20): 2026-07, 2026-09, 2026-10.
- [[wiki/lovable-cloud|Lovable Cloud (LSAT U backend platform)]]: Source: Lovable Cloud docs clipping (`raw/sources/clips/lovable-cloud/`) (docs.lovable.dev/integrations/cloud, ingested 2026-07-19). This is what runs the LSAT U production backend
- [[wiki/lr-missing-explanations-by-category|LR missing explanations, by category]]: Same 772 questions as lr-missing-explanations, generated 2026-09-26. Type, reasoning, features and difficulty come from the question bank. A question with several reasoning types o
- [[wiki/lr-missing-explanations|LR questions missing explanations]]: Generated 2026-09-26 by `system/scripts/lr-explanation-coverage.py` from the live LSAT U database and the question bank (`projects/lsatu/public/data/PT*-LR.json`). LR only. Regener
- [[wiki/lsatu-backend-map|LSAT U backend map (live database structure)]]: Captured 2026-07-19 via the Lovable Cloud SQL editor (source CSV: `query-results-export-2026-07-19_03-00-03.csv` in Joshua's downloads; introspection query in log). This is the **s
- [[wiki/LSATU-BOOKING-POLICY|LSAT U booking policy]]: Every LSAT U booking page (pass link `/book/<slug>`, in-app `/schedule`, single session
- [[wiki/lsatu-idea-queue|LSAT U idea queue: what your LSAT sources suggest building or trying]]: When an ingested LSAT source suggests something to act on, it lands here as one item with clear steps and a link to its source summary: a platform feature, a drill format, a teachi
- [[wiki/magic-mouse-log|Apple Magic Mouse 2 Execution Log]]: Date: 2026-09-18
- [[wiki/PRE-CONSULT-LOG|Pre-consultation check-in log]]: One row per Cal.com consultation the `pre-consultation-check-in` skill has
- [[wiki/protected-records|Protected records: current policy and retired design]]: Current policy is HANDLING and the root operating manuals. Credentials and bank/account information belong only in the git-ignored root `.env`; government IDs stay outside this OS.
- [[wiki/recap-ledger|Recap ledger]]: One row per post-session recap made. The Recap button reads this so a session is not
- [[wiki/reddit-chat-voice|Reddit Chat Voice Reference]]: Ground truth reference for Joshua's actual communication style in Reddit DMs (`attornkas`), derived directly from the real conversation history across 10 different prospects and st
- [[wiki/RRC-BRIEFING-CRITIQUE-2026-09-08|Read, Recall, Colour section briefing page: design critique]]: Date: 2026-09-08. Method: `$impeccable critique` on
- [[wiki/RRC-DRILL-AUDIT-CRITIQUE-2026-09-09|Read, Recall, Colour: full audit, critique and fix plan]]: Date: 2026-09-09. Method: `$impeccable audit` then `$impeccable critique` over the whole drill: the door (library and section pages), the briefing page, the runner, the handover an
- [[wiki/second-brain-one-vault-vs-many|One vault or several: the sources, and what ai-os does today]]: Written 2026-11-20 from a full read of 14 clips captured that day plus the 16 earlier second-brain source pages and `Second_Brain_Prompt.pdf`. The first half is source claims, attr
- [[wiki/second-brain-setup-playbook|How the second brain should be set up]]: Written 2026-11-20 from the second-brain source pages listed above and the one vault or several synthesis. Source claims are attributed; local state was checked on disk 2026-11-20.
- [[wiki/send-ledger|send-ledger]]: See the page for its record and context.
- [[wiki/SEVENSAGE-ANALYTICS-INDEX|7Sage analytics index]]: Built 2026-09-09 by sweeping Joshua's mailbox for `7sage.com/u/usr_...` links.
- [[wiki/STUDENT-PLATFORM-IDENTITY-MAP|Student ↔ Platform Identity Map]]: Built 2026-09-07. **Emails verified** against the live platform via
- [[wiki/SUPERWHISPER-DICTIONARY|Superwhisper dictionary]]: ../superwhisper/CLAUDE explains it; `superwhisper/vocabulary.md`, `superwhisper/replacements.md`,
- [[wiki/tasks|Tasks]]: Living ledger of project state. `/pickup` reads this first; `/wrapup` updates it.
- [[wiki/teaching-voice|Teaching Voice]]: How LSAT U sounds, across every surface. This is the canonical voice doc: route all student-facing and brand copy through it. Built from a grill with Joshua (2026-06-13), then test
- [[wiki/transcript-ingest-findings-2026-07-20|Transcript ingest findings, 2026-07-20]]: Surfaced by distilling 125 Gemini session transcripts (2025-05 to 2026-07). Every claim
- [[wiki/VIDEO-GENERATION-OPTIONS-2026-09-09|Making videos from Claude Code: the options, priced]]: Date: 2026-09-09. Method: five Firecrawl `agent` jobs (spark-1-pro) plus two

### Concepts

- [[wiki/concepts/compiled-knowledge|Let each source and useful answer improve the next answer]]: Compiled knowledge is a maintained explanation built from preserved sources, rather than a fresh reconstruction from those sources for every question.

### Entities

- [[wiki/entities/aspiring-attorneys|Aspiring Attorneys : moved]]: The authoritative business page now lives at **`context/work.md`** (Level 1 authored context, per the workspace reform). This stub exists only so old links resolve; do not add cont

### Homework-assigning

- [[wiki/homework-assigning/assignment-log|Assignment log: what followed each session]]: Each assignment is linked to the latest session on or before its added date, within 3 days. Items with no session in that window are listed under "Between sessions".
- [[wiki/homework-assigning/by-topic|By topic: what was assigned before, and what exists]]: Generated by `system/scripts/build-homework-assigning.py` from LSAT U. Do not hand-edit; fix the tag rules instead.
- [[wiki/homework-assigning/note-formula|Note formula: how a note is built and how it reads]]: Sources: the Lanae note (`model-note/Lanae - Finding the Conclusion by Asking Why.html`, 1,526 words, 7 sections) and the live notes for Charles, Sofia, Celia, Zeina, Ore and Yahun
- [[wiki/homework-assigning/notes-archive/_unmapped/2026-07-28-notification-test-bell-inbox-email-af2c76|2026-07-28-notification-test-bell-inbox-email-af2c76]]: This is a live end-to-end test of the new notification path. If it works, you should see a bell alert, an inbox message, and an email.
- [[wiki/homework-assigning/notes-archive/_unmapped/2026-07-28-test-note-f6785f|2026-07-28-test-note-f6785f]]: This is a test note sent from the admin account to confirm the classroom note pipeline works. No action needed.
- [[wiki/homework-assigning/notes-archive/_unmapped/2026-08-05-how-to-work-assumption-family-medium-set-1-f0e115|Assumption Family (Medium) Set 1]]: Every question here is an assumption question, and all ten were chosen because **Too Strong** is the trap that catches most people on them. That is the rule from our session: soft
- [[wiki/homework-assigning/notes-archive/_unmapped/2026-08-05-how-to-work-explain-curious-fact-medium-set-2-497a97|Explain Curious Fact (Medium) Set 2]]: Phenomenon questions were the third thing we flagged. The pattern is always the same: you are handed a result, and you need the answer that actually accounts for it.
- [[wiki/homework-assigning/notes-archive/_unmapped/2026-08-05-how-to-work-famous-flaws-medium-set-1-421238|Famous Flaws (Medium) Set 1]]: This set is the drill for the three kinds of flaw answer choice. Before you evaluate any option, name what kind it is: an assumption the author was standing on, an objection from o
- [[wiki/homework-assigning/notes-archive/_unmapped/2026-09-14-necessary-assumptions-find-what-the-argument-cannot-lose-279f45|2026-09-14-necessary-assumptions-find-what-the-argument-cannot-lose-279f45]]: A necessary assumption is something an argument needs in order to survive. It does not have to prove the conclusion. Remove it and the reasoning should collapse.
- [[wiki/homework-assigning/notes-archive/celia-cutler/2026-08-19-parallel-reasoning-14b81b|Parallel Reasoning]]: You decide the moment you finish reading. If the five answers come back nearly identical, go back and diagram after all.
- [[wiki/homework-assigning/notes-archive/fernande-charleus/2026-08-28-what-we-did-on-thursday-86e3f8|What we did on Thursday]]: You came in reading an argument as the issue being presented. By the second question you were pulling the conclusion out first, accepting the evidence, and building a counterexampl
- [[wiki/homework-assigning/notes-archive/no-folder-cameron/2026-09-14-necessary-assumptions-find-what-the-argument-cannot-lose-279f45|2026-09-14-necessary-assumptions-find-what-the-argument-cannot-lose-279f45]]: A necessary assumption is something an argument needs in order to survive. It does not have to prove the conclusion. Remove it and the reasoning should collapse.
- [[wiki/homework-assigning/notes-archive/no-folder-lexi-a/2026-08-05-how-to-work-assumption-family-medium-set-1-f0e115|Assumption Family (Medium) Set 1]]: Every question here is an assumption question, and all ten were chosen because **Too Strong** is the trap that catches most people on them. That is the rule from our session: soft
- [[wiki/homework-assigning/notes-archive/no-folder-lexi-a/2026-08-05-how-to-work-explain-curious-fact-medium-set-2-497a97|Explain Curious Fact (Medium) Set 2]]: Phenomenon questions were the third thing we flagged. The pattern is always the same: you are handed a result, and you need the answer that actually accounts for it.
- [[wiki/homework-assigning/notes-archive/no-folder-lexi-a/2026-08-05-how-to-work-famous-flaws-medium-set-1-421238|Famous Flaws (Medium) Set 1]]: This set is the drill for the three kinds of flaw answer choice. Before you evaluate any option, name what kind it is: an assumption the author was standing on, an objection from o
- [[wiki/homework-assigning/notes-archive/sofia/2026-09-11-parallel-reasoning-56bc18|Parallel Reasoning]]: You decide the moment you finish reading. If the five answers come back nearly identical, go back and diagram after all.
- [[wiki/homework-assigning/notes-archive/steven-morris/2026-08-10-day-2-untimed-lr-section-4e5f68|2026-08-10-day-2-untimed-lr-section-4e5f68]]: One question at a time. Check the answer immediately after each one. If you got it wrong, write one line on why before you move to the next question.
- [[wiki/homework-assigning/notes-archive/steven-morris/2026-08-10-day-3-timed-lr-section-then-close-causation-station-54b6a1|2026-08-10-day-3-timed-lr-section-then-close-causation-station-54b6a1]]: Phone in another room. No pausing. Flag anything you are unsure of and keep moving. If you have time at the end, go back to what you flagged. You do not stop early.
- [[wiki/homework-assigning/notes-archive/steven-morris/2026-08-10-day-5-rc-passages-then-blind-review-of-day-3-52ea57|2026-08-10-day-5-rc-passages-then-blind-review-of-day-3-52ea57]]: Passages first. Check answers as you go and write one line on anything you missed.
- [[wiki/homework-assigning/notes-archive/steven-morris/2026-08-10-day-6-timed-rc-section-then-redo-the-week-s-misses-c04a7d|2026-08-10-day-6-timed-rc-section-then-redo-the-week-s-misses-c04a7d]]: Same rules as Wednesday. Flag as you go, use the whole clock, do not stop early.
- [[wiki/homework-assigning/notes-archive/steven-morris/2026-08-10-day-7-blind-review-convert-to-a-score-reread-the-journal-256e48|2026-08-10-day-7-blind-review-convert-to-a-score-reread-the-journal-256e48]]: Blind review Saturday's RC section: redo every flagged question with no answers visible.
- [[wiki/homework-assigning/notes-archive/steven-morris/2026-08-21-parallel-reasoning-adceb2|Parallel Reasoning]]: The decision most people skip, and it costs more than any single rule.
- [[wiki/homework-assigning/playbook|Playbook: in this situation, assign this]]: This is what the record shows, not what Joshua has said is the rule. Each line says how many past sessions on a topic were followed by that assignment. Confirm or correct it in the
- [[wiki/homework-assigning/README|Homework assigning]]: Everything Joshua has assigned, to every student, in one place, so a new session transcript can be turned into a proposed package (notes, drills, activities) from what worked befor
- [[wiki/homework-assigning/rules|Rules: what to assign after a session]]: Hand-written. Not regenerated. `playbook.md` is the generated, inferred view; this file is what Joshua has actually said.
- [[wiki/homework-assigning/taxonomy|Tags]]: Question type, question feature and reasoning type are the platform's own fields (`src/lib/questionLoader.ts`, the guided drill catalog). Practice mode is added here for activities

### Hot-archive

- [[wiki/hot-archive/2026-10|Hot cache archive: session sections moved out of wiki/hot.md]]: Updated 2026-10-15 when the hot cache was capped. Older session sections are preserved unchanged and newest first; moved links are rebased one folder deeper. Each section's date ha

### Karpathy

- [[wiki/karpathy/hot|Teach with small mechanisms and inspectable checks]]: The collected sources are compiled. Seven rules have exact quotes from two distinct original artifacts each. They are practical synthesis, with historical exceptions retained. Josh
- [[wiki/karpathy/index|Use the compiled Karpathy sources with their evidence limits]]: Prompt 2 compilation of the preserved collection is complete: every collected source is mapped and its review scope recorded in the compilation audit. The seven rules and both runt
- [[wiki/karpathy/log|Record compilation separately from collection]]: Compiled reviewed domain sources with explicit coverage ledgers; full corpus remains incomplete. Seven provisional quoted rules; activated Claude/Codex skill and agent copies; scop
- [[wiki/karpathy/methods|Methods make a small result inspectable, testable and reusable]]: This evolving synthesis joins the reviewed domains into concrete building, teaching, research and knowledge-maintenance methods. Each attributed pattern has preserved quotation sup
- [[wiki/karpathy/principles|Principles connect mechanisms, evidence and responsibility]]: These are evolving, attributed observations compiled from the reviewed writings, lectures, interviews, repository documents and captured own-author X texts. They are topic navigati
- [[wiki/karpathy/rules|Seven strongest rules for building and teaching]]: Finalized 2026-10-08 after the collected-source compilation audit. These seven recurring patterns are a synthesis of reviewed public evidence, not Karpathy's endorsement, private m

### Sources

- [[wiki/sources/10-new-github-repos-make-money|Ten repos worth a look: mostly a launch-week hype list, two overlap with what we already have]]: "10 New Github Repos to Make Money in 19 mins" is a YouTube video by a creator who calls himself Jack (YouTube, publication date unknown). The full clip (description plus transcrip
- [[wiki/sources/100-ai-tools-nate-herk|Nate Herk's AI tools roundup: personal recommendations, not an independent tool evaluation]]: Nate Herk's YouTube video, "I Tried 100+ AI Tools. These 7 Are the Best", was published 2026-10-19 according to the clip metadata and captured 2026-10-21. The description says “The
- [[wiki/sources/100-github-repos-for-claude-nate-herk|Nate Herk's picks from 100+ Claude repos: most of the value is in tools LSAT U already touches]]: "I Tried 100+ Github Repos for Claude. These 6 Are the Best." is a YouTube video by Nate Herk (YouTube, publication date unknown). The full clip was read on 2026-10-12. The title s
- [[wiki/sources/10000-ai-websites-nate-herk|Five patterns Nate Herk says separate paid-quality AI websites]]: Nate Herk's video was published 2026-11-09 (11:18). The clip has the full auto-caption transcript with timestamps; there are no visuals, so the example sites he scrolls through wer
- [[wiki/sources/17-claude-design-use-cases-austin-marchese|Austin Marchese: seventeen Claude Design use cases]]: The creator recommends extracting a reusable design system from an existing website and reusing it across technical and nontechnical outputs (0:00 to 1:22). Inline comments and dra
- [[wiki/sources/25-claude-design-tricks-robonuggets|RoboNuggets: twenty-five Claude Design tips]]: The creator recommends extracting a system from owned assets or a reference, shortlisting three systems, naming suitable fonts, studying competitor copy and mixing selected design
- [[wiki/sources/4-claude-engineering-prompt-strategies-austin-marchese|Austin Marchese's four Claude Code strategies: useful synthesis with substantial overlap in ai-os]]: Austin Marchese's YouTube video, "The ONLY 4 Things You Need To Prompt Like An Anthropic Engineer", carries a 2026-10-21 publication date in the clip metadata and was captured 2026
- [[wiki/sources/7-claude-hacks-austin-marchese|Austin Marchese's AI advice tier list: stale context is the one new check for ai-os]]: "7 Claude Hacks That Feel Illegal (And 3 to Avoid)" is a YouTube video by Austin Marchese (YouTube). The channel is inferred from the AUSTINM referral code. The publication date is
- [[wiki/sources/7sage-group-one-indicators|Group 1 sufficient-condition indicators]]: Source: supplied 7Sage lesson text, captured under the generic filename `Dashboard 2.md`. Publication/capture date and exact original page URL unknown. Ingested 2026-10-26. Full te
- [[wiki/sources/7sage-lawgic-language|Lawgic: the language]]: Source: supplied 7Sage lesson text, captured under the generic filename `Dashboard.md`. Publication/capture date and exact original page URL unknown. Ingested 2026-10-26. Full text
- [[wiki/sources/7sage-sufficiency-relationships|Sufficiency and necessity are relationships]]: Source: supplied 7Sage lesson text, captured under the generic filename `Dashboard 1.md`. Publication/capture date and exact original page URL unknown. Ingested 2026-10-26. Full te
- [[wiki/sources/agentic-os-setup-10x-claude-code-chase-ai|Skills and memory are 90 percent of an agentic OS; the dashboard is polish]]: Chase AI, The Agentic OS Setup That Will 10x Claude Code. Published 2026-06-24, clipped 2026-07-18, archived 2026-09-08 (from the archive's own provenance); about 31 minutes. This
- [[wiki/sources/ai-system-so-smart-dan-martell|Dan Martell's AI brain: ai-os has his structure; his nightly cleanup can only run here as a read-only report]]: "This AI System Will Make You So Smart It's Almost Unfair" is a YouTube video by Dan Martell (YouTube). The channel is inferred from the go.danmartell.com links. The publication da
- [[wiki/sources/anthropic-small-business-13-skills-austin-marchese|Anthropic small business skill architecture]]: Source: https://www.youtube.com/watch?v=CNsP0mi1DLw. Archived 2026-10-26; publication and capture date unknown.
- [[wiki/sources/astra-blender-web-design-chase-ai|Prototype a 3D concept before building it in Blender]]: Concept-first exploration and performance budgets transfer directly to dashboard polish. Real-time 3D is optional and should earn its place through useful student feedback or infor
- [[wiki/sources/astra-web-design-taste-vault-chase-ai|Use a taste vault, compare design families, then refine one direction]]: This closely supports the requested design folder: keep visual examples, reasons, sources and design-family labels together while linking to existing skills and repos. It does not
- [[wiki/sources/astra-website-design-loop-jack|References, a design loop and editable website controls]]: The useful transfer is a reusable visual reference library and cheap, narrowly scoped refinement controls. For the student dashboard, direct task access and legible content remain
- [[wiki/sources/automate-99-percent-work-claude-austin-marchese|Austin Marchese's six automation steps: a skill holds the logic, and every run says what it actually checked]]: "6 EASY Steps to Automate 99% of Your Work With Claude" is a YouTube video by Austin Marchese (YouTube). Sponsor: CodeRabbit. The publication date is unknown; the inbox file was la
- [[wiki/sources/claude-code-video-editing-ajane-pinnock|Ajane Pinnock's Claude Code video-editing workflow: iterative previews become reusable skills]]: Ajane Pinnock's YouTube video, "How I Edit My Videos Using Claude Code (Fully Automated)", was captured 2026-10-21. The inbox clip does not provide a publication date, so it remain
- [[wiki/sources/claude-design-fifteen-hacks-jack|Jack: fifteen reference-led Claude Design hacks]]: The creator recommends a reference clip plus brand assets and intent, then three style options for looping animation whose first and last frames match (1:17 to 3:30). Hover lifts,
- [[wiki/sources/claude-mods-chase-ai|Claude mods are presented as persistent customizations to the coding harness]]: Source: Chase AI, Claude Mods Is The Biggest Claude Code Upgrade Since Skills. Publication and exact capture dates are unknown. Ingested 2026-10-26 from the complete supplied descr
- [[wiki/sources/claude-now-does-video-free-javascript|Claude writes the video as a function of time, then checks its own frames]]: Chase AI's video "Claude Now Does Video (FOR FREE) Thanks To JavaScript" (YouTube) argues that Claude Code can produce finished MP4s with plain JavaScript, with no Remotion, no Aft
- [[wiki/sources/claude-ultimate-second-brain-nate-herk|Nate Herk's own second brain: ai-os already runs nearly all of it]]: "I Turned Claude Into the Ultimate Second Brain" is a YouTube video by Nate Herk (YouTube, published 2026-06-10, clipped 2026-09-07). The full description and transcript (about 34:
- [[wiki/sources/claudex-loop-chase-ai|Chase AI on ClaudeX Loop: have a second model grade the plan and the build]]: Chase AI's video, This Open Source Repo Solve Claude's #1 Problem, presents the `claudex-loop` skill. The clip carries the description and a full timestamped transcript to 11:23. P
- [[wiki/sources/conditional-reasoning-voice|Conditional Reasoning supplies the selected LSAT teaching voice]]: Joshua supplied this HTML on 2026-10-02 and explicitly selected its tone, wording, cadence, point of view, explanatory flow, and depth as the standard for LSAT teaching material. T
- [[wiki/sources/consultation-followup-workflow-memory-2026-07-07|The July consultation follow-up memory: mostly superseded, two checks still worth keeping]]: "Post-Consultation Follow-Up Workflow Memory" is a Markdown note written as project memory for ChatGPT sessions, last updated 2026-07-07 by its own header. Author unknown (it addre
- [[wiki/sources/every-level-of-a-claude-second-brain-nate-herk|Pick the lowest level that removes a real pain]]: Nate Herk, Every Level of a Claude Second Brain Explained. Published 2026-06-17, clipped 2026-09-08 (from the archive's own provenance); about 31 minutes. This page was added becau
- [[wiki/sources/fable-5-1-kills-ai-website-slop|Premium AI websites come from references, layering and screenshot checks, not the model]]: Nate Herk's "Fable 5.1 FINALLY Kills AI Website Slop" (YouTube, published 2026-09-01, clipped 2026-09-08). Full clip and transcript (about 16:12) read 2026-10-12. Evidence: archive
- [[wiki/sources/fable-5-karpathy-llm-wiki-nate-herk|Nate Herk's LLM wiki demo: ai-os already compiles, the new idea is tuning ingest rules per wiki]]: "Fable 5 + Karpathy's LLM Wiki is Basically Cheating" is a YouTube video by Nate Herk (YouTube). The channel is inferred from the aiautomationsociety.ai links in the description. T
- [[wiki/sources/gd4ai-obsidian-llm-wiki|GD4AI's wiki plugin: copy its measured gates, skip its graph retrieval]]: "Karpathy LLM Wiki Plugin for Obsidian" is the README of the GitHub repository GD4AI/obsidian-llm-wiki (GitHub), maintained by green-dalii (author) and DocTpoint. The README's publ
- [[wiki/sources/gpt-6-astra-kills-ai-website-slop|Slop is also a site built for the wrong visitor]]: Nate Herk's "GPT-6 Astra FINALLY Kills AI Website Slop" (YouTube, published 2026-09-04, three days after his Fable 5.1 video; clipped 2026-09-11). Full clip and transcript (about 8
- [[wiki/sources/gpt-6-astra-ultimate-second-brain-nate-herk|The AIS-OS starter kit in Codex: every skill he gives away is already on this machine]]: "I Turned GPT-6 Astra Into the Ultimate AI Second Brain" is a YouTube video by Nate Herk (YouTube, published on or after 2026-09-07, clipped 2026-10-08). The full description and t
- [[wiki/sources/greg-isenberg-5-github-repos-ai-slop|Five repos, and a habit: install one, make one small workflow work, then decide]]: Greg Isenberg's solo episode "5 GitHub Repos: Kill AI Slop, Go Viral, Make Money" (YouTube, published 2026-09-02, clipped 2026-09-08). The full clip, description and transcript (ab
- [[wiki/sources/grill-me-skill-10x-claude-code-nate-herk|Getting knowledge out of your head is the hard part; grill-me does it]]: Nate Herk, The Skill That 10x'd My Claude Code Projects. Undated (he mentions Opus 4.8, which hints at the era); about seven minutes. Preserved text, provenance, hash manifest.
- [[wiki/sources/guide-ai-ambition-2026|Choose the goal, the expert method, and the needed perspectives]]: RoboNuggets, *3 Types of AI Ambition*, 10 pages. The guide cites Felix Rieseberg's 2026-10-13 essay; the PDF's own publication date is not stated. Archived PDF and provenance.
- [[wiki/sources/guide-arms-agentic-os-v2|ARMS Agentic OS v2 guide]]: RoboNuggets supplied guide, publication date unknown; captured 2026-10-29 from the supplied Desktop PDF. Original PDF and provenance.
- [[wiki/sources/guide-arms-agentic-os|ARMS Agentic OS setup guide]]: RoboNuggets supplied guide, publication date unknown; captured 2026-10-29 from the supplied Desktop PDF. Original PDF and provenance.
- [[wiki/sources/guide-claude-jargon-fixer|Claude Jargon Fixer guide]]: RoboNuggets supplied guide, publication date unknown; captured 2026-10-29 from the supplied Desktop PDF. Original PDF and provenance.
- [[wiki/sources/guide-claude-mistakes-2026|Keep task context useful and changes recoverable]]: RoboNuggets, *23 Claude Mistakes You're Making*, 17 pages. The guide says its facts were checked 2026-10-09; its publication date is unstated. Archived PDF and provenance.
- [[wiki/sources/guide-claude-plugins-2026|Evaluate each plugin and visual effect for its job]]: RoboNuggets, *Free Claude Code Plugins*, seven pages, marked 2026 with no specific publication date. Archived PDF and provenance.
- [[wiki/sources/harness-engineering-austin-marchese|Austin Marchese's harness engineering: ai-os is already a domain harness; the missing part was logging retrieval misses]]: "Stop Prompting Claude. Start Harness Engineering" is a YouTube video by Austin Marchese (YouTube). The channel is inferred from the clau.de/austin.marchese link. The publication d
- [[wiki/sources/herdr-claude-codex-headache|Herdr gives many coding agents one organized, persistent home]]: Chase AI's video "This Repo Just Solved The #1 Claude + Codex Headache" (YouTube, published 2026-07-16) presents Herdr, a free terminal multiplexer for running several coding agent
- [[wiki/sources/higgsfield-clone-albert-olgaard|A narrated video-generation wrapper build is not proof of a finished platform]]: The design-relevant lesson is to organize a product around one specific user need and inspect the actual interaction/error path. This clip is mostly a commercial wrapper walkthroug
- [[wiki/sources/i-built-another-andrej-karpathy-using-claude|Build an evidence-grounded teaching agent]]: Nate Herk's video describes collecting public sources, compiling an interconnected wiki, deriving corroborated rules, creating a teaching agent and skill, enforcing execution, and
- [[wiki/sources/jev-claude-os-chase-ai|Chase AI's Claude OS: mining 30 days of session logs for skills is the one step ai-os lacked]]: "This NEW Jev + Claude OS Just Changed Every AI Workflow" is a YouTube video by Chase AI (YouTube). The channel is inferred from the skool.com/chase-ai and chaseai.io links. The pu
- [[wiki/sources/karpathy/animals-vs-ghosts|Animals and LLMs may occupy different paths to intelligence]]: Original: Animals vs Ghosts, Andrej Karpathy, published 2025-10-01 according to the preserved article. Collection and compilation date 2026-10-08. The complete preserved Markdown t
- [[wiki/sources/karpathy/autoresearch-readme|Autoresearch bounds an experiment loop]]: Original: autoresearch README, repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and compilation date
- [[wiki/sources/karpathy/blog/catalog.generated|Capture catalog: wiki/sources/karpathy/blog (78 pages)]]: Generated by `py system/scripts/wiki-maintenance.py --index`; do not edit by hand. These pages are
- [[wiki/sources/karpathy/github-payload/catalog.generated|Capture catalog: wiki/sources/karpathy/github-payload (416 pages)]]: Generated by `py system/scripts/wiki-maintenance.py --index`; do not edit by hand. These pages are
- [[wiki/sources/karpathy/jobs-readme|Keep job-market estimates separate from predictions]]: Original: US Job Market Visualizer README, repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and comp
- [[wiki/sources/karpathy/lectures/catalog.generated|Capture catalog: wiki/sources/karpathy/lectures (17 pages)]]: Generated by `py system/scripts/wiki-maintenance.py --index`; do not edit by hand. These pages are
- [[wiki/sources/karpathy/llm-wiki|Compile knowledge into maintained pages]]: Original: LLM Wiki gist, Andrej Karpathy. Publication date unknown; collection and compilation date 2026-10-08. The complete preserved Markdown text was read. The gist revision was
- [[wiki/sources/karpathy/micrograd-readme|Micrograd exposes a small learning implementation]]: Original: micrograd README, repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and compilation date 20
- [[wiki/sources/karpathy/repos/catalog.generated|Capture catalog: wiki/sources/karpathy/repos (799 pages)]]: Generated by `py system/scripts/wiki-maintenance.py --index`; do not edit by hand. These pages are
- [[wiki/sources/karpathy/x/catalog.generated|Capture catalog: wiki/sources/karpathy/x (2521 pages)]]: Generated by `py system/scripts/wiki-maintenance.py --index`; do not edit by hand. These pages are
- [[wiki/sources/karpathy-expert-agent-nate-herk|Use the existing Karpathy video summary]]: This batch initially missed the canonical source page. Its caption-generation evidence and corrected coverage now live on the existing summary. Existing prompt artifacts document f
- [[wiki/sources/llm-wiki-pattern|Compile knowledge once, then keep it current]]: The supplied idea file describes an LLM-maintained wiki between curated source documents and the questions a person asks.
- [[wiki/sources/loophole-bootcamps-2026-10-18|Preserve each Bootcamp question with its observed response]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Capture date: 2026-10-18. Joshua requested the open Referential Phrasing drill and the full Bootcamps collection, includ
- [[wiki/sources/loophole-conditionals-2026-10-18|Keep the original conditional lessons and their attached practice together]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-18 from Joshua's authorized signed-in browser. Joshua requested conditional-only source capture and a c
- [[wiki/sources/loophole-how-to-camo-2026-10-15|Camo review combines missed questions with correct-answer decoys]]: Ellen Cassidy's **How to Camo** lecture on Loophole Online was captured on 2026-10-15. Its publication date is unknown. The complete 8:25 automatic-caption transcript has 54 render
- [[wiki/sources/loophole-lr-recordings-2026-10-15|Every exposed LR recording is accounted for]]: The signed-in Loophole Online database capture on 2026-10-15 covered 168 pages and 5,015 distinct LR question records. All have captured written Correct CLIR and classifications. T
- [[wiki/sources/loophole-organization-methods-2026-10-15|Integrate the Loophole library through existing routes]]: Checked 2026-10-15. These organization references support the existing Loophole integration, not adoption of its teaching prescriptions. The adoption ledger remains the broader dec
- [[wiki/sources/loophole-rc-activity-demos-2026-10-18|Preserve the demonstrations for the named RC activities]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured and ingested 2026-10-18 from the authorized signed-in browser. Joshua requested the Decaf, Cappuccino, Caffeina
- [[wiki/sources/loophole-rc-day-1-2026-10-14|Day 1: preserved lecture sources and written notes]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-14 in the signed-in Codex browser; organized into the second brain 2026-10-14. This batch contains 11 l
- [[wiki/sources/loophole-rc-day-2-2026-10-14|Day 2: preserved lecture sources and written notes]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-14 in the signed-in Codex browser; organized into the second brain 2026-10-14. This batch contains 12 l
- [[wiki/sources/loophole-rc-day-3-2026-10-14|Day 3: preserved lecture sources and written notes]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-14 in the signed-in Codex browser; organized into the second brain 2026-10-14. This batch contains 11 l
- [[wiki/sources/loophole-rc-day-6-2026-10-14|Day 6: preserved lecture sources and written notes]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-14 in the signed-in Codex browser; organized into the second brain 2026-10-14. This batch contains 13 l
- [[wiki/sources/loophole-rc-day-7-2026-10-14|Day 7: preserved lecture sources and written notes]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured 2026-10-14 in the signed-in Codex browser; organized into the second brain 2026-10-14. This batch contains 12 l
- [[wiki/sources/loophole-routines-2026-10-15|Routines retain their ordered prescriptions and complete workout instructions]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured from Joshua's authenticated browser on 2026-10-15 as private teacher research. Source filing does not adopt tea
- [[wiki/sources/loophole-workouts-2026-10-14|Every observed workout has its own full source record]]: Ellen Cassidy / Loophole Online. Publication dates unknown. Captured from Joshua's authenticated Codex browser beginning 2026-10-14 and completed 2026-10-15. This preserves the fou
- [[wiki/sources/lsat-demon-abstract-conditionals|Move from a familiar rule to an abstract relationship]]: Joshua supplied this LSAT Demon clip and requested its integration into the Conditional Bootcamp on 2026-10-03. The entire supplied transcript, 0:00 to 9:10, was read. The closing
- [[wiki/sources/lsat-demon-mastering-conditional-statements|One sufficient route need not be the only route]]: Joshua requested all clipped LSAT Demon conditional material for intuitive original examples. This generic-title article was found after the two explicitly named Demon clips. Unlik
- [[wiki/sources/lsat-demon-sufficient-necessary|A conditional rule does not say its trigger occurred]]: Joshua supplied this LSAT Demon clip and requested its integration into the Conditional Bootcamp on 2026-10-03. The complete supplied transcript, 0:04 to 5:17, was read. The speake
- [[wiki/sources/lsat-lab-conditional-logic-clip|LSAT Lab explains the arrow as certainty from sufficient to necessary]]: The 2026-10-11 capture extends this source review through the full supplied transcript, 0:02–24:19. The earlier screenshot review below remains distinct evidence. For the current M
- [[wiki/sources/make-ai-sound-like-you-dan-martell|Dan Martell's voice method: separate guides per medium, built from real samples, and the human stays at the start]]: "How to Make AI Sound EXACTLY Like you" is a YouTube video by Dan Martell (YouTube), inferred from the go.danmartell.com link and his Instagram handle. The publication date is unkn
- [[wiki/sources/manage-ai-agents-five-steps-austin-marchese|Managing an AI agent: write its job, limit its tools, check its work, turn corrections into the system]]: "The Most Valuable AI Skill to Learn In 2027" is a YouTube video on Austin Marchese's channel (YouTube). He interviews Nate Herk and narrates five steps for managing AI agents. The
- [[wiki/sources/matt-pocock-skills-v1-2|Matt Pocock's skills v1.2.0: what changed and what we already have]]: Matt Pocock's release video was published 2026-08-05 (11:37), the same day as the `mattpocock/skills` tag `v1.2.0` (commit `e903586b`, checked with `gh`). Full auto-caption transcr
- [[wiki/sources/matt-pocock-system-claude-skills-austin-marchese|Matt Pocock's skill process, via Austin Marchese: write a skill for what you keep sending back, keep it short, cut what does nothing]]: "Matt Pocock's EXACT System To 10x Your Claude Skills" is a YouTube video by Austin Marchese (YouTube) about Matt Pocock's skills (mattpocock/skills). Sponsor: AIQORA (captioned "A
- [[wiki/sources/mcat-cars-three-passages-2026-10-15|Three complete passage bodies are ready for Reading Center]]: The user-supplied clip contains three reading passages, without questions or explanations despite the file title. The original source is preserved byte-for-byte. Publication date,
- [[wiki/sources/meet-new-codex-cli|A Codex CLI walkthrough combines task management, voice and rendered output]]: Source: Meet the New Codex CLI. The supplied capture does not identify the channel/author, publication date, exact capture date, version, release channel or account requirements. I
- [[wiki/sources/mobbin-sample-pack-100|Use the Mobbin sample to compare specific interface screens]]: Joshua supplied the Mobbin UI Sample Pack on 2026-10-29. Its publication date is unknown. The archive contains 100 WebP screenshots and a README; the provenance record states each
- [[wiki/sources/new-agentic-os-standard-claude-5-robonuggets|ARMS in three levels each, and organise files for agents, not people]]: Jay / RoboNuggets, The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown). No publication date; he mentions an artifact "back in the 5th of August", so it was rec
- [[wiki/sources/new-way-build-second-brain-claude-nick-saraev|A second brain is a searchable pile of your own data plus fast lookup]]: Nick Saraev, The NEW Way to Build a Second Brain w Claude (2027). Publication date unknown; the "(2027)" in the title is not verified by the clip. Clipped 2026-11-20. Preserved tex
- [[wiki/sources/obsidian-in-24-minutes-tina-huang|Tina Huang's three levels of Obsidian plus AI: ai-os already runs level three]]: "Obsidian in 24 Minutes" is a YouTube video by Tina Huang (YouTube); she names herself at 1:49. The publication date is unknown; the inbox file was last modified 2026-10-14. The de
- [[wiki/sources/old-obsidian-vault-2026-10-07|Useful material recovered from the older local Obsidian vault]]: The Loophole home now separates RC, LR and shared methods while preserving this older recovery's evidence and caveats. New source generations are separately summarized as RC Day 1,
- [[wiki/sources/openai-chatgpt-subscription-api-credits|API credits for eligible ChatGPT subscribers]]: OpenAI's video describes subscription-linked API credits and demonstrates building an app with the OpenAI Developers plugin in Codex. The clip's publication and capture dates are u
- [[wiki/sources/personal-agents-clearly-explained-jeff-su|Jeff Su on personal agents: a folder of memory files you own beats a proactive app you rent]]: "Personal Agents, Clearly Explained" is a YouTube video by Jeff Su (YouTube), inferred from the jeffsu.org links. The publication date is unknown; the inbox file was last modified
- [[wiki/sources/rea-feature-investigation-chase-ai|REA investigation should produce claims with evidence, not a magical clone]]: For UI inspiration, capture a specific behavior, inspect what is actually visible and explain what remains unknown. Binary decompilation is not necessary for a calendar strip or qu
- [[wiki/sources/rea-output-first-workflow-nate-herk|Nate Herk: investigate a narrow feature and test the rebuilt behavior]]: This strengthens a practical design-reference workflow: inspect a particular picker, calendar or transition, save concise observations, and compare the rebuilt interaction with tha
- [[wiki/sources/reverse-engineer-anything-rea|Rea gives an agent decompiler tools; the creator calls the hype ahead of the demos]]: Nick Saraev's video "I Tested The Viral Github Repo To Reverse Engineer Anything" (YouTube, publication date unknown) tests Rea (`morluto/rea`). Both clip generations were read in
- [[wiki/sources/self-improving-claude-knowledge-base-one-prompt-robonuggets|One pasted prompt builds a raw, wiki, outputs and scheduled-lint knowledge base]]: Jay / RoboNuggets, Build a Self-Improving Claude Knowledge Base with ONE Prompt. Publication date unknown; clipped 2026-11-20 (local file time); about 12.5 minutes. Preserved text,
- [[wiki/sources/sonnet-5-5-vs-opus-5-5-nate-herk|Sonnet for a clear spec, Opus for a vague goal: Nate Herk's seven-task comparison]]: "I Tested Sonnet 5.5 vs Opus 5.5. What You Need to Know" is a YouTube video by Nate Herk (YouTube, publication date unknown, clipped 2026-10-08). The full description and transcrip
- [[wiki/sources/steal-my-ai-os-setup-5-tips-nate-herk|Keep an AI OS accurate as it grows: route, audit, refresh, segment, trace mistakes]]: Nate Herk, Steal My Exact AI OS Setup (5 simple tips). No date in the clip; his mentions of July 22 and June 29 suggest about 2026-07-22 (inferred). About 25 minutes. Preserved tex
- [[wiki/sources/stop-organizing-files-yourself-jeff-su|Jeff Su's file rulebook: the agent proposes, you approve, and the rulebook learns]]: "Stop Organizing Files Yourself" is a YouTube video by Jeff Su (YouTube), inferred from the jeffsu.org links. Sponsor: Dropbox. The publication date is unknown; the inbox file was
- [[wiki/sources/stop-prompting-claude-karpathy-method-austin-marchese|Austin Marchese on Karpathy's method: ai-os has the spec, verifier and environment; the gap is rules enforced by hooks]]: "Stop Prompting Claude. Use Karpathy's Method Instead." is a YouTube video by Austin Marchese (YouTube), published 2026-06-09, clipped 2026-07-19 with the Obsidian Web Clipper, and
- [[wiki/sources/top-7-claude-design-skills-chase-ai|Chase AI's seven design skills]]: Chase AI's video, “Top 7 Claude Design Skills (All Free)” was published 2026-10-21. The Obsidian clip has a partial transcript and no repository links. Its recorded transcript stop
- [[wiki/sources/ultimate-second-brain-arms-robonuggets|Judge a second brain by retrieval, then by its graph]]: Jay / RoboNuggets, Build your Ultimate Second Brain with Claude Fable 5 (before it's too late). Publication and original capture dates are unknown. Ingested 2026-10-26 from the sup

<!-- END GENERATED WIKI CATALOG -->

