---
type: operating-layer
subject: Index
updated: 2026-09-30
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

- [[tasks]] — living Now / Next / Done work ledger; `/pickup` reads it first (content carried from the pre-rebuild ledger)
- [[hot]] — last-session cache and automation alerts; rebuilt fresh
- [[log]] — append-only history of ingests, queries, and lint passes; started fresh (old log archived)
- [[dashboard]] — product ground-truth pointers; regenerable, backends are authority
- [[lovable-cloud]] — what the Lovable Cloud backend can do, Jay 2's reach vs Lovable-only operations, and the export escape hatch
- [[lsatu-backend-map]] — live DB structure: 82 tables by domain, RPCs, triggers, RLS posture, cron; reuse flags for new features

## Entities

- [[entities/aspiring-attorneys]] — the tutoring business: who Joshua is, offers, pricing channels, tools, priorities, gaps (seeded from the 2026-07-16 onboarding intake)

## Voice & policy

- [[teaching-voice]] — canonical voice doc with coaching, teaching-content, and brand registers; LSAT material uses Joshua's selected 2026-10-02 source standard
- [LSAT teaching voice standard](../references/lsat-teaching-voice-standard.md): detailed wording, cadence, questions, lesson progression, original calibration examples, and review rubric; [source summary](sources/conditional-reasoning-voice.md). The [conditional content-order skeleton](../brainstorms/2026-09-30-conditional-curriculum/2026-10-02-opening-lessons-source-map.md) records Joshua's 2026-10-03 selection of the full supplied sequence.
- [[ACCOMMODATIONS-REQUEST-TEMPLATE]] — approved LSAT accommodations email (sent by the accommodations-email skill, QP form attached) + LSAC deadlines and category notes
- [[reddit-chat-voice]] — ground truth reference of 10 real Reddit chat conversations, tone patterns, and DM dispatch standards
- [[HANDLING]]: current credential/data policy and advisory remote checks, aligned with the root manuals.
- [[protected-records]]: current storage routes and the explicitly retired encrypted-bundle design.

## Operations

- [[guided-drill-verification-log]] — living QA log of guided drills verified to launch on the platform (restored from the pre-rebuild archive 2026-07-16; skills cite it before re-verifying)
- [[lr-missing-explanations]] + [[lr-missing-explanations-by-category]]: the 772 LR questions with no, partial, or never-loaded explanations (PT/S/Q list, then by type, reasoning, feature, difficulty); snapshot 2026-09-26
- [[../corpus/lr-explanations/golden-set|LR golden set]]: the 50 model explanations (and rubric) the missing ones are written from; 2026-09-26
- [[automation-backlog]] — how Joshua's email/ops time actually breaks down (from 944 authored emails) + the leverage-ranked build backlog; the 19% "apology tax" is the north-star target. Walked by `/level-up`

## References (OS method / meta)

- [Stripe API access](../references/stripe-api.md): verified account-read route while the connected app requires reauthentication.
- [Audit repair outcome](../research/audit-repairs-2026-10-08/outcome.md): corrected rules, routes, skills, diagnostics and remaining decisions.
- [Recovered historical evidence](../research/audit-repairs-2026-10-08/lint-cal-repair.md): surviving dated app documents for retired worktree citations; old wiki history remains unchanged.
- [Prepared Obsidian sync plan](../research/audit-repairs-2026-10-08/obsidian-sync-plan.md): current vault is disconnected, existing remote is separate, and candidate working content is small enough for selective sync.

- [AI workspace knowledge hub](../references/ai-workspace/index.md): Claude/Codex updates, skill ideas, repository evaluations, prompts, tips and workflows, kept separate from LSAT teaching.
- [Recovered AI methods](../references/ai-workspace/migrated-source-methods.md): detailed review, skill-evaluation and source-checking recipes from the old vault.
- [Completed old-vault migration](../research/obsidian-vault-comparison/2026-10-07/migration-outcome-2026-10-08.md): all 100 original file dispositions, useful active homes, exact exclusions and unimplemented structural suggestions.
- [Recovered Loophole method library](../corpus/loophole-online/method-library.md): actionable practice protocols; captured instructor editions for [reading](../corpus/loophole-online/reading-lectures.generated.md), [question strategies](../corpus/loophole-online/question-strategies.generated.md), [review/workouts](../corpus/loophole-online/review-workouts.generated.md), and [worked examples](../corpus/loophole-online/worked-examples.generated.md) remain attributed teacher research, separate from approved curriculum.

- [[../references/second-brain-levels]]: retrieval architecture, dated comparison, current domain routes and sync limitations.
- [[../references/obsidian-command-center]]: attributed command-center methods, historical plugin research and device-verification limits.
- [[../references/claude-plus-codex]] — running Claude Code + Codex on one project; shared-file architecture, plan/critique workflow, and the installed Herdr session layer for visible, persistent dual-agent execution
- [[../references/graphify-obsidian-bridge]] — turning any corpus into a linked concept map in the vault (`--obsidian`); the source-wiring step and the fragmentation trap that silently guts the result
- [[../references/3ms-framework]] — the Three Ms operator brain (walked weekly by `/level-up`)
- [Website planning](../references/website-design-planning.md): recovered visitor-journey, asset-planning and rendered-review methods.
- [Older vault comparison](../research/obsidian-vault-comparison/2026-10-07/report.md), [historical every-file dispositions](../research/obsidian-vault-comparison/2026-10-07/excluded-from-active-knowledge.md), and [current organization audit](../research/obsidian-vault-comparison/2026-10-07/organization-audit-2026-10-08.md): recovered knowledge, authorized cleanup, overlap, conflicts and verification limits.
- [Cal.com stuck bookings](CALCOM-STUCK-BOOKINGS.md) — unpaid bookings hold slots invisibly; run scripts/calcom-pending-sweep.mjs
- [LSAT U booking policy](LSATU-BOOKING-POLICY.md) — one generator, one predicate, one config row; mirrors Cal.com session-link (buffer 10, pitch 80, 45 days)

- `superwhisper/` (vault root): dictation setup, source of truth for Superwhisper vocabulary, replacements, and modes; `sync.py` pushes it to the app. Research report inside. Ledger: [[SUPERWHISPER-DICTIONARY]].

<!-- BEGIN GENERATED WIKI CATALOG -->

## Complete wiki catalog

Every Markdown page under `wiki/` is listed below; this index is the catalog itself.
Regenerate this section after page changes with `py system/scripts/wiki-maintenance.py --index`.

### Operating pages

- [[wiki/ACCOMMODATIONS-REQUEST-TEMPLATE|Accommodations request email]]: The email Joshua sends a student after they've talked through LSAT testing accommodations.
- [[wiki/ACTIVE-STUDENTS-LAST-MONTH-2026-09-08|Active students, last month : 2026-08-08 to 2026-09-08]]: Pulled 2026-09-08 from the calendar (82 events) and Drive (40 Gemini docs).
- [[wiki/ASSIGN-AN-ACTIVITY|Assign an Activity : the runbook]]: The repeatable path for putting an LSAT U Activity into a student's hands.
- [[wiki/automation-backlog|Automation & Workflow Analysis : Joshua's tutoring operation]]: Related: entities/aspiring-attorneys · teaching-voice · ../skills/INDEX · ../references/3ms-framework
- [[wiki/CALCOM-STUCK-BOOKINGS|Cal.com stuck bookings]]: When a student says scheduling or payment "isn't working", first ask **which link**. A
- [[wiki/CELIA-RRC-REPLY-DRAFT-2026-09-08|Celia · reply to "still being marked" (DRAFT, not sent)]]: Channel: LSAT U platform message, from Joshua's admin account. Send via the assign-lsatu-work skill only after Joshua approves the text.
- [[wiki/CONSULTATION-FOLLOW-UP-TEMPLATE|Consultation follow-up email]]: The email Joshua sends after a free consultation. Reconstructed 2026-09-11 from the
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
- [[wiki/log|Log]]: Codex isolated `codex/review-170-finish` from latest main0f48e65, outside Claude's #171 builder allowlist and the pending #176 branch. Fixed Activity Review completion/provenance g
- [[wiki/lovable-cloud|Lovable Cloud (LSAT U backend platform)]]: Source: Lovable Cloud docs clipping (`raw/sources/clips/lovable-cloud/`) (docs.lovable.dev/integrations/cloud, ingested 2026-07-19). This is what runs the LSAT U production backend
- [[wiki/lr-missing-explanations-by-category|LR missing explanations, by category]]: Same 772 questions as lr-missing-explanations, generated 2026-09-26. Type, reasoning, features and difficulty come from the question bank. A question with several reasoning types o
- [[wiki/lr-missing-explanations|LR questions missing explanations]]: Generated 2026-09-26 by `system/scripts/lr-explanation-coverage.py` from the live LSAT U database and the question bank (`projects/lsatu/public/data/PT*-LR.json`). LR only. Regener
- [[wiki/lsatu-backend-map|LSAT U backend map (live database structure)]]: Captured 2026-07-19 via the Lovable Cloud SQL editor (source CSV: `query-results-export-2026-07-19_03-00-03.csv` in Joshua's downloads; introspection query in log). This is the **s
- [[wiki/LSATU-BOOKING-POLICY|LSAT U booking policy]]: Every LSAT U booking page (pass link `/book/<slug>`, in-app `/schedule`, single session
- [[wiki/magic-mouse-log|Apple Magic Mouse 2 Execution Log]]: Date: 2026-09-18
- [[wiki/PRE-CONSULT-LOG|Pre-consultation check-in log]]: One row per Cal.com consultation the `pre-consultation-check-in` skill has
- [[wiki/protected-records|Protected records: current policy and retired design]]: Current policy is HANDLING and the root operating manuals. Credentials and bank/account information belong only in the git-ignored root `.env`; government IDs stay outside this OS.
- [[wiki/reddit-chat-voice|Reddit Chat Voice Reference]]: Ground truth reference for Joshua's actual communication style in Reddit DMs (`attornkas`), derived directly from the real conversation history across 10 different prospects and st
- [[wiki/RRC-BRIEFING-CRITIQUE-2026-09-08|Read, Recall, Colour section briefing page: design critique]]: Date: 2026-09-08. Method: `$impeccable critique` on
- [[wiki/RRC-DRILL-AUDIT-CRITIQUE-2026-09-09|Read, Recall, Colour: full audit, critique and fix plan]]: Date: 2026-09-09. Method: `$impeccable audit` then `$impeccable critique` over the whole drill: the door (library and section pages), the briefing page, the runner, the handover an
- [[wiki/send-ledger|Send ledger]]: Append-only record of every outbound message Jay 2 drafts or sends on Joshua's
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

### Karpathy

- [[wiki/karpathy/hot|Use the reviewed method and preserve its limits]]: Prompt 2 remains partial: source pages and explicit coverage now span writings, repositories, lectures and X. A first working method uses seven corroborated rules; it does not repr
- [[wiki/karpathy/index|The Karpathy method is installed; compilation continues]]: The saved video now has a working first implementation: seven provisional rules, Claude and Codex agent/skill copies, a scoped Claude execution gate and an actually executed tokeni
- [[wiki/karpathy/log|Record compilation separately from collection]]: Compiled reviewed domain sources with explicit coverage ledgers; full corpus remains incomplete. Seven provisional quoted rules; activated Claude/Codex skill and agent copies; scop
- [[wiki/karpathy/methods|Project methods are evidence, not installed workflows]]: The comparisons below preserve the initial four-document compilation. Later source pages review named code files and additional writings, X posts and transcript passages with expli
- [[wiki/karpathy/principles|Candidate observations need wider evidence]]: The observations below preserve the initial five-source compilation. The current operational synthesis is seven reviewed rules, with two distinct source locations per rule. Additio
- [[wiki/karpathy/rules|Seven rules for a reviewed teaching method]]: These rules are an operational synthesis of reviewed public evidence, not Karpathy's endorsement or private mind. Each has two distinct source locations. They are the strongest use

### Sources

- [[wiki/sources/conditional-reasoning-voice|Conditional Reasoning supplies the selected LSAT teaching voice]]: Joshua supplied this HTML on 2026-10-02 and explicitly selected its tone, wording, cadence, point of view, explanatory flow, and depth as the standard for LSAT teaching material. T
- [[wiki/sources/i-built-another-andrej-karpathy-using-claude|Build an evidence-grounded teaching agent]]: Nate Herk's video describes collecting public sources, compiling an interconnected wiki, deriving corroborated rules, creating a teaching agent and skill, enforcing execution, and
- [[wiki/sources/karpathy/animals-vs-ghosts|Animals and LLMs may occupy different paths to intelligence]]: Original: Animals vs Ghosts, Andrej Karpathy, published 2025-10-01 according to the preserved article. Collection and compilation date 2026-10-08. The complete preserved Markdown t
- [[wiki/sources/karpathy/autoresearch-readme|Autoresearch bounds an experiment loop]]: Original: autoresearch README, repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and compilation date
- [[wiki/sources/karpathy/blog/about-pointer|About: website pointer]]: Author: Andrej Karpathy. Published: unknown. Captured: 2026-10-08T09:34:48.931151Z.
- [[wiki/sources/karpathy/blog/alphago-in-context|AlphaGo, in context]]: Author: Andrej Karpathy. Published: Wed, 31 May 2017 20:41:38 GMT. Captured: 2026-10-08T09:36:44.615987Z.
- [[wiki/sources/karpathy/blog/append-and-review|The append-and-review note]]: Author: Andrej Karpathy. Published: 2025-03-19T07:00Z. Captured: 2026-10-08T09:36:16.693020Z.
- [[wiki/sources/karpathy/blog/auto-grade-hn|Auto-grading decade-old Hacker News discussions with hindsight]]: Author: Andrej Karpathy. Published: 2025-12-10T15:00Z. Captured: 2026-10-08T09:36:00.030134Z.
- [[wiki/sources/karpathy/blog/biohacking-lite|Biohacking Lite]]: Author: Andrej Karpathy. Published: 2020-06-11. Captured: 2026-10-08T09:35:03.352835Z.
- [[wiki/sources/karpathy/blog/bitcoin-from-scratch|Bitcoin from scratch: learning versus production boundaries]]: Author: Andrej Karpathy. Published: 2021-06-21. Captured: 2026-10-08T09:34:58.574395Z.
- [[wiki/sources/karpathy/blog/books-preferences|Andrej Karpathy: Books]]: Author: Andrej Karpathy. Published: unknown. Captured: 2026-10-08T09:36:51.887508Z.
- [[wiki/sources/karpathy/blog/breaking-linear-classifiers|Breaking Linear Classifiers on ImageNet]]: Author: Andrej Karpathy. Published: 2015-03-30. Captured: 2026-10-08T09:35:22.862506Z.
- [[wiki/sources/karpathy/blog/calculator|I love calculator]]: Author: Andrej Karpathy. Published: 2024-09-08T17:00Z. Captured: 2026-10-08T09:36:22.472767Z.
- [[wiki/sources/karpathy/blog/chemical-hygiene|Chemical hygiene]]: Author: Andrej Karpathy. Published: 2025-12-18T18:00Z. Captured: 2026-10-08T09:35:57.344934Z.
- [[wiki/sources/karpathy/blog/chrome-extension-programming-2013|Chrome Extension Programming]]: Author: Andrej Karpathy. Published: 2013-11-23. Captured: 2026-10-08T09:35:40.444705Z.
- [[wiki/sources/karpathy/blog/cognitive-discontinuity-fiction|A Cognitive Discontinuity: speculative AI fiction]]: Author: Andrej Karpathy. Published: 2015-11-14. Captured: 2026-10-08T09:35:15.837550Z.
- [[wiki/sources/karpathy/blog/computer-vision-2012|The state of Computer Vision and AI]]: Author: Andrej Karpathy. Published: 2012-10-22. Captured: 2026-10-08T09:35:42.959146Z.
- [[wiki/sources/karpathy/blog/course-project-publication|Taking a Course Project to Publication]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:00.615170Z.
- [[wiki/sources/karpathy/blog/cs183c-organizational-models|CS183c Assignment 3]]: Author: Andrej Karpathy. Published: Sun, 15 Nov 2015 09:04:51 GMT. Captured: 2026-10-08T09:36:44.700890Z.
- [[wiki/sources/karpathy/blog/cs231n-2016-assignment-1|CS231n 2016 Assignment 1]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:30.424964Z.
- [[wiki/sources/karpathy/blog/cs231n-2016-assignment-2|CS231n 2016 Assignment 2]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:32.864269Z.
- [[wiki/sources/karpathy/blog/cs231n-2016-assignment-3|CS231n 2016 Assignment 3]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:35.063029Z.
- [[wiki/sources/karpathy/blog/cs231n-2018-assignment-1|CS231n 2018 Assignment 1]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:37.251080Z.
- [[wiki/sources/karpathy/blog/cs231n-2018-assignment-2|CS231n 2018 Assignment 2]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:39.413492Z.
- [[wiki/sources/karpathy/blog/cs231n-2018-assignment-3|CS231n 2018 Assignment 3]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:41.389892Z.
- [[wiki/sources/karpathy/blog/cs231n-2019-assignment-2|CS231n 2019 Assignment 2]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:43.427711Z.
- [[wiki/sources/karpathy/blog/cs231n-2019-assignment-3|CS231n 2019 Assignment 3]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:45.583828Z.
- [[wiki/sources/karpathy/blog/cs231n-2021-assignment-1|CS231n 2021 Assignment 1]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:47.713062Z.
- [[wiki/sources/karpathy/blog/cs231n-2021-assignment-2|CS231n 2021 Assignment 2]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:49.888176Z.
- [[wiki/sources/karpathy/blog/cs231n-2021-assignment-3|CS231n 2021 Assignment 3]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:52.050260Z.
- [[wiki/sources/karpathy/blog/cs231n-2026-assignment-1|CS231n 2026 Assignment 1]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:54.066501Z.
- [[wiki/sources/karpathy/blog/cs231n-2026-assignment-2|CS231n 2026 Assignment 2]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:56.095564Z.
- [[wiki/sources/karpathy/blog/cs231n-aws-tutorial|CS231n AWS Tutorial]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:37:58.291080Z.
- [[wiki/sources/karpathy/blog/cs231n-classification|CS231n image classification and validation]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:02.944858Z.
- [[wiki/sources/karpathy/blog/cs231n-convolutional-networks|CS231n convolutional architectures and resource accounting]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:05.181738Z.
- [[wiki/sources/karpathy/blog/cs231n-linear-classify|CS231n linear classification and objective semantics]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:07.444721Z.
- [[wiki/sources/karpathy/blog/cs231n-minimal-network|CS231n minimal neural-network case study]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:16.819963Z.
- [[wiki/sources/karpathy/blog/cs231n-neural-networks-1|CS231n neural networks: architecture and activation]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:09.740220Z.
- [[wiki/sources/karpathy/blog/cs231n-neural-networks-2|CS231n neural networks: preprocessing and objectives]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:11.867073Z.
- [[wiki/sources/karpathy/blog/cs231n-neural-networks-3|CS231n neural networks: learning diagnostics]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:14.257815Z.
- [[wiki/sources/karpathy/blog/cs231n-optimization-1|CS231n optimization: iterative refinement]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:19.603151Z.
- [[wiki/sources/karpathy/blog/cs231n-optimization-2|CS231n optimization: staged backpropagation]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:22.035632Z.
- [[wiki/sources/karpathy/blog/cs231n-python-numpy|Python NumPy tutorial with notebooks]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:25.034942Z.
- [[wiki/sources/karpathy/blog/cs231n-rnn|CS231n recurrent neural networks]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:27.589487Z.
- [[wiki/sources/karpathy/blog/cs231n-software-setup|CS231n Software Setup]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:29.968700Z.
- [[wiki/sources/karpathy/blog/cs231n-terminal-tutorial|CS231n Terminal.com Tutorial]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:32.302550Z.
- [[wiki/sources/karpathy/blog/cs231n-transfer-learning|CS231n Transfer Learning]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:34.543266Z.
- [[wiki/sources/karpathy/blog/cs231n-understanding-cnn|CS231n Understanding CNNs]]: Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:36.720662Z.
- [[wiki/sources/karpathy/blog/datascience-weekly-interview-pointer|Interview with Data Science Weekly on Neural Nets and ConvNetJS]]: Author: Andrej Karpathy. Published: 2014-04-26. Captured: 2026-10-08T09:35:35.936539Z.
- [[wiki/sources/karpathy/blog/digital-hygiene|Digital hygiene]]: Author: Andrej Karpathy. Published: 2025-03-17T18:08Z. Captured: 2026-10-08T09:36:20.243228Z.
- [[wiki/sources/karpathy/blog/feature-learning-escapades|Feature Learning Escapades]]: Author: Andrej Karpathy. Published: 2014-07-03. Captured: 2026-10-08T09:35:29.588942Z.
- [[wiki/sources/karpathy/blog/forward-pass-fiction|Short Story on AI: Forward Pass]]: Author: Andrej Karpathy. Published: 2021-03-27. Captured: 2026-10-08T09:35:00.910169Z.
- [[wiki/sources/karpathy/blog/hacker-news-collection-2013|Quantifying Hacker News with 50 days of data]]: Author: Andrej Karpathy. Published: 2013-11-27. Captured: 2026-10-08T09:35:38.042791Z.
- [[wiki/sources/karpathy/blog/homepage-source-directory|Andrej Karpathy homepage]]: Author: Andrej Karpathy. Published: unknown. Captured: 2026-10-08T09:36:49.596537Z.
- [[wiki/sources/karpathy/blog/iclr-arxiv-sanity-2017|ICLR 2017 vs arxiv-sanity]]: Author: Andrej Karpathy. Published: Tue, 14 Mar 2017 02:52:52 GMT. Captured: 2026-10-08T09:36:44.662311Z.
- [[wiki/sources/karpathy/blog/icml-institution-stats-2017|ICML accepted papers institution stats]]: Author: Andrej Karpathy. Published: Wed, 24 May 2017 19:09:35 GMT. Captured: 2026-10-08T09:36:44.626126Z.
- [[wiki/sources/karpathy/blog/imagenet-human-comparison|What I learned from competing against a ConvNet on ImageNet]]: Author: Andrej Karpathy. Published: 2014-09-02. Captured: 2026-10-08T09:35:25.307109Z.
- [[wiki/sources/karpathy/blog/lecun1989-reproduction|Deep Neural Nets: 33 years ago and 33 years from now]]: Author: Andrej Karpathy. Published: 2022-03-14. Captured: 2026-10-08T09:34:54.438714Z.
- [[wiki/sources/karpathy/blog/llm-year-in-review-2025|2025 LLM Year in Review]]: Author: Andrej Karpathy. Published: 2025-12-19T18:00Z. Captured: 2026-10-08T09:35:54.425893Z.
- [[wiki/sources/karpathy/blog/machine-learning-trends-2017|A Peek at Trends in Machine Learning]]: Author: Andrej Karpathy. Published: Fri, 07 Apr 2017 17:43:46 GMT. Captured: 2026-10-08T09:36:44.640178Z.
- [[wiki/sources/karpathy/blog/manual-cifar10|Lessons learned from manually classifying CIFAR-10]]: Author: Andrej Karpathy. Published: 2011-04-27. Captured: 2026-10-08T09:35:45.501409Z.
- [[wiki/sources/karpathy/blog/medium-routing-pointer|Started posting on Medium instead]]: Author: Andrej Karpathy. Published: 2018-01-20. Captured: 2026-10-08T09:35:07.989312Z.
- [[wiki/sources/karpathy/blog/microgpt|microgpt]]: Author: Andrej Karpathy. Published: 2026-02-12. Captured: 2026-10-08T09:34:52.019287Z.
- [[wiki/sources/karpathy/blog/phd-survival-guide|A Survival Guide to a PhD]]: Author: Andrej Karpathy. Published: 2016-09-07. Captured: 2026-10-08T09:35:10.573499Z.
- [[wiki/sources/karpathy/blog/pong-policy-gradients|Pong from pixels and the limits of policy gradients]]: Author: Andrej Karpathy. Published: 2016-05-31. Captured: 2026-10-08T09:35:13.391647Z.
- [[wiki/sources/karpathy/blog/power-to-the-people|Power to the people]]: Author: Andrej Karpathy. Published: 2025-04-07T18:00Z. Captured: 2026-10-08T09:36:11.850443Z.
- [[wiki/sources/karpathy/blog/quantifying-productivity|Quantifying Productivity]]: Author: Andrej Karpathy. Published: 2014-08-03. Captured: 2026-10-08T09:35:27.483271Z.
- [[wiki/sources/karpathy/blog/recipe|A Recipe for Training Neural Networks]]: Author: Andrej Karpathy. Published: 2019-04-25. Captured: 2026-10-08T09:35:05.717093Z.
- [[wiki/sources/karpathy/blog/rnn-effectiveness|Recurrent networks: mechanisms, examples and caveats]]: Author: Andrej Karpathy. Published: 2015-05-21. Captured: 2026-10-08T09:35:20.590606Z.
- [[wiki/sources/karpathy/blog/selfie-proxy-study|What a Deep Neural Network thinks about your selfie]]: Author: Andrej Karpathy. Published: 2015-10-25. Captured: 2026-10-08T09:35:18.149040Z.
- [[wiki/sources/karpathy/blog/sequoia-ascent-2026|Sequoia Ascent 2026 summary and edited transcript]]: Author: Andrej Karpathy. Published: 2026-04-30T16:00Z. Captured: 2026-10-08T09:35:52.178157Z.
- [[wiki/sources/karpathy/blog/sleep-tracker-self-experiment|Finding the Best Sleep Tracker]]: Author: Andrej Karpathy. Published: 2025-03-24T23:00Z. Captured: 2026-10-08T09:36:14.327052Z.
- [[wiki/sources/karpathy/blog/software-2-0|Software 2.0]]: Author: Andrej Karpathy. Published: Sat, 11 Nov 2017 22:18:53 GMT. Captured: 2026-10-08T09:36:44.579078Z.
- [[wiki/sources/karpathy/blog/space-of-minds|The space of minds]]: Author: Andrej Karpathy. Published: 2025-11-29T18:00Z. Captured: 2026-10-08T09:36:02.476864Z.
- [[wiki/sources/karpathy/blog/switching-to-jekyll|Switching Blog from Wordpress to Jekyll]]: Author: Andrej Karpathy. Published: 2014-07-01. Captured: 2026-10-08T09:35:33.775311Z.
- [[wiki/sources/karpathy/blog/twitter-tsne-2014|Visualizing Top Tweeps with t-SNE in Javascript]]: Author: Andrej Karpathy. Published: 2014-07-02. Captured: 2026-10-08T09:35:31.717446Z.
- [[wiki/sources/karpathy/blog/undergraduate-study-advice|Doing well in your courses]]: Author: Andrej Karpathy. Published: unknown. Captured: 2026-10-08T09:36:47.236181Z.
- [[wiki/sources/karpathy/blog/understand-backprop|Yes you should understand backprop]]: Author: Andrej Karpathy. Published: Mon, 19 Dec 2016 19:50:08 GMT. Captured: 2026-10-08T09:36:44.693544Z.
- [[wiki/sources/karpathy/blog/verifiability|Verifiability]]: Author: Andrej Karpathy. Published: 2025-11-17T17:00Z. Captured: 2026-10-08T09:36:04.865552Z.
- [[wiki/sources/karpathy/blog/vibe-coding-menugen|Vibe coding MenuGen]]: Author: Andrej Karpathy. Published: 2025-04-27T12:00Z. Captured: 2026-10-08T09:36:09.542765Z.
- [[wiki/sources/karpathy/blog/virtual-reality-2017|Virtual Reality: still not quite there, again]]: Author: Andrej Karpathy. Published: Tue, 17 Jan 2017 20:26:49 GMT. Captured: 2026-10-08T09:36:44.678858Z.
- [[wiki/sources/karpathy/blog/zero-to-hero|Neural Networks: Zero to Hero]]: Author: Andrej Karpathy. Published: unknown. Captured: 2026-10-08T09:36:54.284471Z.
- [[wiki/sources/karpathy/jobs-readme|Keep job-market estimates separate from predictions]]: Original: US Job Market Visualizer README, repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and comp
- [[wiki/sources/karpathy/lectures/2okjtvyslmy|Stable diffusion dreams of steampunk brains]]: Original: 2oKjtvYslMY; channel Andrej Karpathy. Upload date 2022-08-17. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/7xtgnnlpymi|Deep Dive into LLMs like ChatGPT]]: Original: 7xTGNNLPyMI; channel Andrej Karpathy. Upload date 2025-02-05. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/96jn2ocofls|Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan]]: Original: https://www.youtube.com/watch?v=96jN2OCOfLs. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2
- [[wiki/sources/karpathy/lectures/ewvnqjaaohw|How I use LLMs]]: Original: EWvNQjAaOHw; channel Andrej Karpathy. Upload date 2025-02-27. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/kcc8fmeb1ny|Let's build GPT: from scratch, in code, spelled out.]]: Original: kCc8FmEb1nY; channel Andrej Karpathy. Upload date 2023-01-17. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/kvpdarqzdrq|Stable diffusion dreams of psychedelic faces]]: Original: kVpDARqZdrQ; channel Andrej Karpathy. Upload date 2022-08-19. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/kwsvtq7dziu|Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI]]: Original: https://www.youtube.com/watch?v=kwSVtQ7dziU. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2
- [[wiki/sources/karpathy/lectures/l8prsuu81pu|Let's reproduce GPT-2 (124M)]]: Original: l8pRSuU81PU; channel Andrej Karpathy. Upload date 2024-06-09. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/p6sfmutpumc|Building makemore Part 3: Activations & Gradients, BatchNorm]]: Original: P6sfmUTpUmc; channel Andrej Karpathy. Upload date 2022-10-04. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/pacmpygffxo|The spelled-out intro to language modeling: building makemore]]: Original: PaCmpygFfXo; channel Andrej Karpathy. Upload date 2022-09-07. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/q8sa3rm6cki|Building makemore Part 4: Becoming a Backprop Ninja]]: Original: https://www.youtube.com/watch?v=q8SA3rM6ckI. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2
- [[wiki/sources/karpathy/lectures/sm9bozw295q|Stable diffusion dreams of tattoos]]: Original: https://www.youtube.com/watch?v=sM9bozW295Q. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2
- [[wiki/sources/karpathy/lectures/t3yj5hkimq0|Building makemore Part 5: Building a WaveNet]]: Original: https://www.youtube.com/watch?v=t3YJ5hKiMQ0. Author/channel Andrej Karpathy. Upload date is preserved in raw metadata. Captured and compiled 2026-10-08. Automatic English
- [[wiki/sources/karpathy/lectures/tch_1bhy58i|Building makemore Part 2: MLP]]: Original: TCH_1BHY58I; channel Andrej Karpathy. Upload date 2022-09-12. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/vmj-3s1tku0|The spelled-out intro to neural networks and backpropagation: building micrograd]]: Original: VMj-3S1tku0; channel Andrej Karpathy. Upload date 2022-08-16. Captured 2026-10-08, compilation 2026-10-08. Automatic English captions, not verified against audio.
- [[wiki/sources/karpathy/lectures/zdusfxrajke|Let's build the GPT Tokenizer]]: Original: https://www.youtube.com/watch?v=zduSFxRajkE. Author/channel Andrej Karpathy, except interviewer passages. Upload date is preserved in raw metadata. Captured and compiled2
- [[wiki/sources/karpathy/lectures/zjkbmfhnj_g|[1hr Talk] Intro to Large Language Models]]: Original: https://www.youtube.com/watch?v=zjkBMFhNj_g. Author/channel Andrej Karpathy. Upload date is preserved in raw metadata. Captured and compiled 2026-10-08. Automatic English
- [[wiki/sources/karpathy/llm-wiki|Compile knowledge into maintained pages]]: Original: LLM Wiki gist, Andrej Karpathy. Publication date unknown; collection and compilation date 2026-10-08. The complete preserved Markdown text was read. The gist revision was
- [[wiki/sources/karpathy/micrograd-readme|Micrograd exposes a small learning implementation]]: Original: micrograd README, repository owner Andrej Karpathy; individual passage authorship not independently verified. Publication date unknown; collection and compilation date 20
- [[wiki/sources/karpathy/repos/autoresearch-program|Autoresearch defines a measured experiment loop]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/autoresearch. Publication date unknown; captured and compil
- [[wiki/sources/karpathy/repos/build-nanogpt-readme|Build nanoGPT preserves a step-by-step reproduction]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/build-nanogpt. Publication date unknown; captured and compi
- [[wiki/sources/karpathy/repos/llm-council-readme|LLM Council separates independent answers from peer review]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/llm-council. Publication date unknown; captured and compile
- [[wiki/sources/karpathy/repos/llm101n-readme|LLM101n is an archived course plan]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/LLM101n. Publication date unknown; captured and compiled 20
- [[wiki/sources/karpathy/repos/makemore-readme|Makemore keeps the educational model hackable]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/makemore. Publication date unknown; captured and compiled 2
- [[wiki/sources/karpathy/repos/micrograd-engine|Micrograd makes reverse-mode differentiation inspectable]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/micrograd. Publication date unknown; captured and compiled
- [[wiki/sources/karpathy/repos/micrograd-neural-network|Micrograd builds neural networks from inspectable scalar parts]]: Original repository: https://github.com/karpathy/micrograd. Publication date unknown; captured and compiled 2026-10-08. Raw evidence, SHA-256 `f54453501abc4fd38ae724a8b378d6a5d23bf
- [[wiki/sources/karpathy/repos/minbpe-basic-tokenizer|Basic BPE exposes training and decoding boundaries]]: Original repository: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 2026-10-08. Raw evidence, SHA-256 `d240f8b54f25d8c65e81f3da1cc7c3a390a7692c
- [[wiki/sources/karpathy/repos/minbpe-exercise|The tokenizer exercise adds one complication at a time]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 202
- [[wiki/sources/karpathy/repos/minbpe-readme|Minbpe separates tokenizer mechanisms]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 202
- [[wiki/sources/karpathy/repos/minbpe-regex-tokenizer|Regex BPE separates ordinary input from special tokens]]: Original repository: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 2026-10-08. Raw evidence, SHA-256 `2f79fc32d719c5805782c441e6311c10790ba987
- [[wiki/sources/karpathy/repos/mingpt-readme|MinGPT separates a small educational implementation from scale]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/minGPT. Publication date unknown; captured and compiled 202
- [[wiki/sources/karpathy/repos/nanogpt-readme|NanoGPT chooses a comparable baseline and adapts to hardware]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/nanoGPT. Publication date unknown; captured and compiled 20
- [[wiki/sources/karpathy/repos/rendergit-readme|Rendergit makes code review a single document]]: Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/rendergit. Publication date unknown; captured and compiled
- [[wiki/sources/karpathy/x/autoresearch-results|Reported gains were checked at a larger scale]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2031135152349524125`, published 2026-03-09T22:28:51.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/chronological-batch-001|70 captured posts read in chronological batch 001]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-002|70 captured posts read in chronological batch 002]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-003|70 captured posts read in chronological batch 003]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-004|70 captured posts read in chronological batch 004]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-005|70 captured posts read in chronological batch 005]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-006|70 captured posts read in chronological batch 006]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-007|70 captured posts read in chronological batch 007]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-008|58 captured posts read in chronological batch 008]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-009|70 captured posts read in chronological batch 009]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-010|35 captured posts read in chronological batch 010]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-011|70 captured posts read in chronological batch 011]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-012|70 captured posts read in chronological batch 012]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-013|70 captured posts read in chronological batch 013]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-014|70 captured posts read in chronological batch 014]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-015|70 captured posts read in chronological batch 015]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-016|49 captured posts read in chronological batch 016]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-017|70 captured posts read in chronological batch 017]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-018|70 captured posts read in chronological batch 018]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-019|62 captured posts read in chronological batch 019]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-020|37 captured posts read in chronological batch 020]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-021|62 captured posts read in chronological batch 021]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-022|70 captured posts read in chronological batch 022]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-023|68 captured posts read in chronological batch 023]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-024|70 captured posts read in chronological batch 024]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-025|46 captured posts read in chronological batch 025]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-026|55 captured posts read in chronological batch 026]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-027|67 captured posts read in chronological batch 027]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-028|46 captured posts read in chronological batch 028]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-029|70 captured posts read in chronological batch 029]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/chronological-batch-030|70 captured posts read in chronological batch 030]]: Author attributed by handle: Andrej Karpathy. Capture/compilation date:2026-10-08. This page groups the exact listed post IDs for navigation, not a claim that an entire month was r
- [[wiki/sources/karpathy/x/claude-coding-notes|Agent coding needs explicit assumptions and success criteria]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2015883857489522876`, published 2026-01-26T20:25:39.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/dependency-risk|Simple functionality can avoid a large dependency tree]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2036487306585268612`, published 2026-03-24T16:56:24.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/empirical-setting|Deep learning improvements are setting-dependent]]: Author attributed by captured handle: Andrej Karpathy. Post ID `1619749146340237313`, published 2023-01-29T17:27:44.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/experiment-design-failures|Automation still needs fair experiments]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2027521323275325622`, published 2026-02-27T23:08:47.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/explicit-delegation|Understand what you delegate]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2026735109077135652`, published 2026-02-25T19:04:39.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/explicit-local-memory|Personalization should be inspectable and portable]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2040572272944324650`, published 2026-04-04T23:28:36.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/idea-files|Share an idea so an agent can tailor its implementation]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2040470801506541998`, published 2026-04-04T16:45:23.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/inspectable-running-code|Readable code and visible measured output fit together]]: Author attributed by captured handle: Andrej Karpathy. Post ID `1620187595979513857`, published 2023-01-30T22:29:59.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/llm-knowledge-bases|Knowledge is compiled and queried as files]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2039805659525644595`, published 2026-04-02T20:42:21.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/objective-and-simplicity|An experiment objective includes cost and simplicity]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2029957088022254014`, published 2026-03-06T16:27:39.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/reproduction-limit|A belief is weaker than a hardware reproduction]]: Author attributed by captured handle: Andrej Karpathy. Post ID `1613261828095905792`, published 2023-01-11T19:49:27.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/research-community|Collaborative research should retain distinct branches]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2030705271627284816`, published 2026-03-08T18:00:40.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/teacher-contribution|Teaching supplies a small organizing contribution]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2030387285250994192`, published 2026-03-07T20:57:06.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/two-metric-acceptance|Lower loss is insufficient when training took longer]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2031144226696868077`, published 2026-03-09T23:04:55.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/karpathy/x/voice-context|A spoken ramble can expose missing intent]]: Author attributed by captured handle: Andrej Karpathy. Post ID `2079610838143623371`, published 2026-07-21T16:53:55.000Z, captured 2026-10-08. Original post; preserved ledger, loca
- [[wiki/sources/llm-wiki-pattern|Compile knowledge once, then keep it current]]: The supplied idea file describes an LLM-maintained wiki between curated source documents and the questions a person asks.
- [[wiki/sources/lsat-demon-abstract-conditionals|Move from a familiar rule to an abstract relationship]]: Joshua supplied this LSAT Demon clip and requested its integration into the Conditional Bootcamp on 2026-10-03. The entire supplied transcript, 0:00 to 9:10, was read. The closing
- [[wiki/sources/lsat-demon-mastering-conditional-statements|One sufficient route need not be the only route]]: Joshua requested all clipped LSAT Demon conditional material for intuitive original examples. This generic-title article was found after the two explicitly named Demon clips. Unlik
- [[wiki/sources/lsat-demon-sufficient-necessary|A conditional rule does not say its trigger occurred]]: Joshua supplied this LSAT Demon clip and requested its integration into the Conditional Bootcamp on 2026-10-03. The complete supplied transcript, 0:04 to 5:17, was read. The speake
- [[wiki/sources/lsat-lab-conditional-logic-clip|LSAT Lab's opening boards explain roles before keyword fluency]]: Joshua clipped Patrick's **Conditional Logic / LSAT Logical Reasoning** on 2026-10-03, with a transcript and twelve embedded screenshots. This bounded review covers the transcript
- [[wiki/sources/old-obsidian-vault-2026-10-07|Useful material recovered from the older local Obsidian vault]]: Joshua authorized a complete local-file comparison and integration of useful missing content on 2026-10-07. The source is the older local vault at `C:\Users\Joshu\Documents\Ai-os`,

<!-- END GENERATED WIKI CATALOG -->
