---
type: source
subject: RoboNuggets one-prompt self-improving Karpathy-style knowledge base
created: 2026-11-20
updated: 2026-11-20
aliases: [Build a Self-Improving Claude Knowledge Base with ONE Prompt, Dream Sequence, RoboNuggets second brain prompt]
tags: [ai-workspace, second-brain, llm-wiki, scheduled-lint]
evidence: ../../raw/sources/clips/self-improving-claude-knowledge-base-one-prompt-robonuggets/clip.md
sha256: f1dca52b57fee69193e681ed888e8abc0b6b53ad5dc7b0afde9f973873fb0d9f
contradictions: []
sources:
  - ../../raw/sources/clips/self-improving-claude-knowledge-base-one-prompt-robonuggets/PROVENANCE.md
---

# One pasted prompt builds a raw, wiki, outputs and scheduled-lint knowledge base

Jay / RoboNuggets, [Build a Self-Improving Claude Knowledge Base with ONE Prompt](https://www.youtube.com/watch?v=K2BpNt3UBOQ). Publication date unknown; clipped 2026-11-20 (local file time); about 12.5 minutes. [Preserved text](../../raw/sources/clips/self-improving-claude-knowledge-base-one-prompt-robonuggets/clip.md), [provenance](../../raw/sources/clips/self-improving-claude-knowledge-base-one-prompt-robonuggets/PROVENANCE.md), [hash manifest](../../raw/sources/clips/self-improving-claude-knowledge-base-one-prompt-robonuggets/SHA256SUMS).

## What the source says

- **Thesis:** one prompt makes Claude Code build a self-maintaining Karpathy-style wiki with no Obsidian, vector database or RAG. He says it is far more powerful on day 100 than on day one.
- **Five blocks:**
  - `raw/`: a messy dump. The agent can also fill it, for example through deep research.
  - `wiki/`: three files. `index.md` (table of contents of concepts, entities and sources), `log.md` (date-stamped) and `processed.md` (a registry of raw files already ingested).
  - An outputs folder for finished PDFs, slide packs and apps.
  - `CLAUDE.md`: the operating manual, which the agent itself maintains.
  - A "dream sequence": a scheduled job, weekly by default. It ingests anything new in `raw/` and lints for contradictions, stale claims, duplicates and orphans. He edits the schedule by prompt (daily; skip wiki updates at ingest). It appears under Routines in the Claude desktop app.
- **The prompt** is parameterised by topic and by internet research versus your own files, and teaches three actions: feed it, ask it, let it dream. The prompt text is a gated Skool download and is not in the clip.
- Joshua's [Second_Brain_Prompt.pdf](file:///C:/Users/Joshu/Downloads/Second_Brain_Prompt.pdf) in Downloads has the same architecture and operations. That it is this video's prompt is inferred, not verified.

## Limits and distrust

- "No tools, no RAG" leans on Karpathy's own scale of about 100 articles. A read-only check found his post adds that this works at a small scale and that the model keeps index files; the clip drops that qualifier. Index-only retrieval is unproven at ai-os scale.
- "Karpathy highlighted this exact system" overstates: he described a pattern, not this prompt.
- The agent edits its own manual and runs unattended on a schedule with no review gate.
- Community upsell and affiliate tools throughout. No measurements.

## What this adds here

Already in ai-os: raw, wiki, index, log, ingest, lint, hash-based dedup ([schema](../../system/schema/llm-wiki.md), [LLM Wiki pattern](llm-wiki-pattern.md)). Not in ai-os: a single `processed.md` registry (processed status is inferred from provenance, source page and log), a separate `outputs/` folder, and a scheduled consolidate-then-lint pass. Scheduled lint was declined on 2026-10-14 ([adoption ledger](../../references/ai-workspace/second-brain-adoptions.md), [decisions](../../decisions/log.md)). An unattended pass that rewrites pages would also collide with the compare-and-swap rule; a report-only version would fit. That is a recommendation from this ingest, not a decision.

Related: [Ultimate Second Brain (ARMS)](ultimate-second-brain-arms-robonuggets.md), [one vault versus many](../second-brain-one-vault-vs-many.md).

## Coverage

Read in full on 2026-11-20 by a read-only research pass; line references and quotations were not re-checked line by line by the main session. Video, audio and the gated prompt were not inspected.
