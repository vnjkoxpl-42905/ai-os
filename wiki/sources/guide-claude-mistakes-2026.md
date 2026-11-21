---
type: source
subject: Claude session, prompt, safety and configuration advice
created: 2026-10-29
updated: 2026-10-29
tags: [ai-workspace, claude, codex, context]
evidence: ../../raw/sources/ai-guides-2026-10-29/claude-mistakes/23 Claude Mistakes Guide.pdf
sha256: 2c5b82618ee1fdad66946a54e0d644f2405cd4bb3bdbef5b53f459ef3cd71805
sources:
  - ../../raw/sources/ai-guides-2026-10-29/claude-mistakes/PROVENANCE.md
aliases: [23 Claude mistakes guide]
contradictions: []
---

# Keep task context useful and changes recoverable

RoboNuggets, *23 Claude Mistakes You're Making*, 17 pages. The guide says its facts were checked 2026-10-09; its publication date is unstated. [Archived PDF](../../raw/sources/ai-guides-2026-10-29/claude-mistakes/23%20Claude%20Mistakes%20Guide.pdf) and [provenance](../../raw/sources/ai-guides-2026-10-29/claude-mistakes/PROVENANCE.md).

## What the guide covers

Its 23 items, in source order: (1) unrelated tasks in one session, (2) switching models, (3) repeated corrections instead of rewinding, (4) side questions, (5) excessive effort, (6) vague prompts, (7) rules without reasons, (8) generic anti-AI design requests, (9) accepting a first draft, (10) drip-fed changes, (11) outdated prompting, (12) cold caches, (13) oversized instruction files, (14) disabled safety, (15) no backups, (16) excessive connections, (17) unbounded exploration, (18) not checking usage, (19) unclear alignment, (20) expiring chat history, (21) installing plugins blindly, (22) undirected compaction, and (23) using one model for all work (pp. 3–16).

Useful shared principles for Claude and Codex: retain task-relevant context and decisions, specify audience and completion evidence, bound searches, keep instructions navigable, preserve important files before risky changes, inspect plugins before installing, and use explicit visual references. Seek independent validation when appropriate. Existing project instructions and the user's preferred design direction govern application; the guide's blanket suggestion against cream backgrounds does not override a brief.

> “One task, one session” (p. 4).

## Runtime-specific claims and proposed components

The guide proposes Claude Code commands `/clear`, `/rewind`, `/btw`, `/compact`, `/usage`, `/model` and `/loop`, plus `cleanupPeriodDays` and compact instructions. These are Claude-specific claims, not Codex commands. Model names, cache lifetime, costs, settings and usage breakdowns are time-sensitive and not verified by reading this PDF. Do not run a recurring cache-warming loop merely to preserve a discount; it also uses resources. Consider risk and value before changing retention or permission settings.

The source mentions [Destructive Command Guard](https://github.com/Dicklesworthstone/destructive_command_guard) and Anthropic's [Blast Radius example](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) as supplementary safety tools, and discusses the creator's named `burst`, `align`, `personalise`, and Jev workflows without supplying their implementations. The PDF is not a code review, official installation verification, or evidence that these are installed. Refer to existing [Claude/Codex guidance](../../references/claude-plus-codex.md) and [AI workspace](../../references/ai-workspace/index.md) before adding overlapping methods.

All 17 extracted pages were read. Linked official documentation, community incident reports, and benchmark and cost claims were not independently checked in this source compilation. The page-two audit prompt and source recommendations are evidence, not instructions to change settings.
