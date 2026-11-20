---
type: source
subject: Nate Herk's five levels of a Claude second brain, with level-picking rules and failure modes
created: 2026-11-20
updated: 2026-11-20
aliases: [Every Level of a Claude Second Brain Explained, Nate Herk five levels, second brain levels video]
tags: [ai-workspace, second-brain, levels, retrieval]
evidence: "../../raw/sources/clips/every-level-of-a-claude-second-brain-explained/Every Level of a Claude Second Brain Explained.md"
sha256: ec6c1cac0a822696ab2d204c3c06bd1864d94872777c3517ae4b2a77493485d0
contradictions: []
sources:
  - ../../raw/sources/clips/every-level-of-a-claude-second-brain-explained/PROVENANCE.md
---

# Pick the lowest level that removes a real pain

Nate Herk, [Every Level of a Claude Second Brain Explained](https://www.youtube.com/watch?v=DTCyvo6cC54). Published 2026-06-17, clipped 2026-09-08 (from the archive's own provenance); about 31 minutes. This page was added because the vault had only a reference synthesis, [second-brain levels](../../references/second-brain-levels.md), and no source page. [Archived text](../../raw/sources/clips/every-level-of-a-claude-second-brain-explained/Every%20Level%20of%20a%20Claude%20Second%20Brain%20Explained.md), [provenance](../../raw/sources/clips/every-level-of-a-claude-second-brain-explained/PROVENANCE.md). A re-clip in `raw/inbox/` (2026-11-20) has an identical body once the 11-line header is removed; it was not archived again.

## What the source says

- **Backward design:** design the data from the question you will ask. Pain test: if there is no pain, do not add a level. A project can mix levels folder by folder.
- **L1** CLAUDE.md as router, `context/`, a dated decision log, `projects/`. **L2** an LLM wiki with an index, plus `references/` and `memory.md`; Claude auto memory on with `/memory`; for Codex, point AGENTS.md at the same files. **L3** semantic search (chunk, embed, search). **L4** a knowledge graph with typed entities and relations. **L5** an always-on brain that needs crons or an agent such as Hermes.
- **Vault stance:** no separate vaults. His transcript wiki is nested inside the main project; level is chosen per folder. He rarely opens Obsidian. The only scale remarks: CLAUDE.md gets messy as it grows, wikis "degrade a little", and his graph tool slows his computer.

## Points missing from the vault's synthesis

- **Vector-chunk failure modes:** "summarise the March 5 meeting" returns about five of 20 chunks; "which week had the highest sales" on a table picks the wrong week. Vector search fits needle lookups (rule 17 of 1,000); use full markdown for summaries and aggregates.
- A wiki makes the agent read a whole page, so a graph can use fewer tokens.
- The real bottleneck at L4 is getting knowledge out of your head; he feeds the graph with grill-me sessions. Privacy: data sent to Claude is not private; consider local models.
- A CLAUDE.md can reference an `agents.md` instead of keeping a copy.
- At L5 too much context can do more harm than good; he keeps ingestion manual.
- **Level-picking:** re-explaining your setup means L1; 30+ notes you forget means L2; missing known notes means L3; chains of questions means L4; syncing offline agents means L5.
- **Evergreen versus volatile:** ingest decisions and priorities; do not ingest Slack, email or customer data, fetch it live. Team brains: adoption matters more than tech.

## Limits

"Your moat is your data" and "better than you can" are pitch lines. All claims are his own use; no benchmarks, and he says no standard is proven. The taxonomy is his framing. One level slip in the transcript (L2 said where L3 is meant) is inferred.

Related: [one vault versus many](../second-brain-one-vault-vs-many.md). No action taken.

## Coverage

Read in full on 2026-11-20 by a read-only research pass that diffed it against the archive and the vault's synthesis.
