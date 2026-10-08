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
- [[HANDLING]] — Tier-A handling rules and the pre-remote scrub checklist (authority cited by core.md)
- [[protected-records]] — where sensitive records live and how they are referenced

## Operations

- [[guided-drill-verification-log]] — living QA log of guided drills verified to launch on the platform (restored from the pre-rebuild archive 2026-07-16; skills cite it before re-verifying)
- [[lr-missing-explanations]] + [[lr-missing-explanations-by-category]]: the 772 LR questions with no, partial, or never-loaded explanations (PT/S/Q list, then by type, reasoning, feature, difficulty); snapshot 2026-09-26
- [[../corpus/lr-explanations/golden-set|LR golden set]]: the 50 model explanations (and rubric) the missing ones are written from; 2026-09-26
- [[automation-backlog]] — how Joshua's email/ops time actually breaks down (from 944 authored emails) + the leverage-ranked build backlog; the 19% "apology tax" is the north-star target. Walked by `/level-up`

## References (OS method / meta)

- [[../references/second-brain-levels]] — the 5 levels of a Claude second brain; ai-os is a complete Level 2
- [[../references/obsidian-command-center]] — Chase AI's Claude Code + Obsidian command-center setup vs ai-os; only new idea is a visual dashboard plugin + one-click headless skill launchers
- [[../references/claude-plus-codex]] — running Claude Code + Codex on one project; shared-file architecture, plan/critique workflow, and the installed Herdr session layer for visible, persistent dual-agent execution
- [[../references/graphify-obsidian-bridge]] — turning any corpus into a linked concept map in the vault (`--obsidian`); the source-wiring step and the fragmentation trap that silently guts the result
- [[../references/3ms-framework]] — the Three Ms operator brain (walked weekly by `/level-up`)
- [Website planning](../references/website-design-planning.md): recovered visitor-journey, asset-planning and rendered-review methods.
- [Older vault comparison](../research/obsidian-vault-comparison/2026-10-07/report.md) and [every-file dispositions](../research/obsidian-vault-comparison/2026-10-07/excluded-from-active-knowledge.md): recovered knowledge, overlap, historical claims and explicit omission reasons.
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
- [[wiki/HANDLING|Personal-data handling]]: As of 2026-07-17 this OS stores no secret material beyond API keys in the root `.env`. The earlier design's private stores (`private/records.sparsebundle`, migration manifests, `pr
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
- [[wiki/protected-records|Protected records]]: Sensitive records are intentionally not linked file-by-file from Git-tracked pages.
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

### Sources

- [[wiki/sources/conditional-reasoning-voice|Conditional Reasoning supplies the selected LSAT teaching voice]]: Joshua supplied this HTML on 2026-10-02 and explicitly selected its tone, wording, cadence, point of view, explanatory flow, and depth as the standard for LSAT teaching material. T
- [[wiki/sources/llm-wiki-pattern|Compile knowledge once, then keep it current]]: The supplied idea file describes an LLM-maintained wiki between curated source documents and the questions a person asks.
- [[wiki/sources/lsat-demon-abstract-conditionals|Move from a familiar rule to an abstract relationship]]: Joshua supplied this LSAT Demon clip and requested its integration into the Conditional Bootcamp on 2026-10-03. The entire supplied transcript, 0:00 to 9:10, was read. The closing
- [[wiki/sources/lsat-demon-mastering-conditional-statements|One sufficient route need not be the only route]]: Joshua requested all clipped LSAT Demon conditional material for intuitive original examples. This generic-title article was found after the two explicitly named Demon clips. Unlik
- [[wiki/sources/lsat-demon-sufficient-necessary|A conditional rule does not say its trigger occurred]]: Joshua supplied this LSAT Demon clip and requested its integration into the Conditional Bootcamp on 2026-10-03. The complete supplied transcript, 0:04 to 5:17, was read. The speake
- [[wiki/sources/lsat-lab-conditional-logic-clip|LSAT Lab's opening boards explain roles before keyword fluency]]: Joshua clipped Patrick's **Conditional Logic / LSAT Logical Reasoning** on 2026-10-03, with a transcript and twelve embedded screenshots. This bounded review covers the transcript
- [[wiki/sources/old-obsidian-vault-2026-10-07|Useful material recovered from the older local Obsidian vault]]: Joshua authorized a complete local-file comparison and integration of useful missing content on 2026-10-07. The source is the older local vault at `C:\Users\Joshu\Documents\Ai-os`,

<!-- END GENERATED WIKI CATALOG -->
