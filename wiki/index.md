---
type: operating-layer
subject: Index
updated: 2026-07-20
aliases: []
---

# Index

Content catalog of the wiki — every page, one line each, by category. The LLM updates this on every ingest; read it first when answering a query, then drill into pages. Rebuilt fresh 2026-07-16 (Karpathy LLM-wiki rebuild; prior wiki preserved at `archive/wiki-pre-rebuild-2026-07-16/`).

The brain runs three knowledge systems: **this wiki** (Joshua, the business, decisions), **[corpus](../corpus/index.md)** (LSAT teaching knowledge), **[students](../students/README.md)** (one folder per student).

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

- [[teaching-voice]] — canonical voice doc, 3 registers (coaching / teaching content / brand); carried verbatim through the rebuild
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
- [Cal.com stuck bookings](CALCOM-STUCK-BOOKINGS.md) — unpaid bookings hold slots invisibly; run scripts/calcom-pending-sweep.mjs
- [LSAT U booking policy](LSATU-BOOKING-POLICY.md) — one generator, one predicate, one config row; mirrors Cal.com session-link (buffer 10, pitch 80, 45 days)

- `superwhisper/` (vault root): dictation setup, source of truth for Superwhisper vocabulary, replacements, and modes; `sync.py` pushes it to the app. Research report inside. Ledger: [[SUPERWHISPER-DICTIONARY]].
