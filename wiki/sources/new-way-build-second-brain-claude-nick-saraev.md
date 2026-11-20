---
type: source
subject: Nick Saraev's Engram retrieval design: BM25, ingest-time summaries, recency weighting
created: 2026-11-20
updated: 2026-11-20
aliases: [The NEW Way to Build a Second Brain w Claude (2027), Engram, Nick Saraev second brain]
tags: [ai-workspace, second-brain, retrieval]
evidence: ../../raw/sources/clips/new-way-build-second-brain-claude-nick-saraev/clip.md
sha256: 5a0e129507ec3f27877832b2309a5492449bba4d57250215d6e5efa7607974eb
contradictions: []
sources:
  - ../../raw/sources/clips/new-way-build-second-brain-claude-nick-saraev/PROVENANCE.md
---

# A second brain is a searchable pile of your own data plus fast lookup

Nick Saraev, [The NEW Way to Build a Second Brain w Claude (2027)](https://www.youtube.com/watch?v=LP7bfT4vOlo). Publication date unknown; the "(2027)" in the title is not verified by the clip. Clipped 2026-11-20. [Preserved text](../../raw/sources/clips/new-way-build-second-brain-claude-nick-saraev/clip.md), [provenance](../../raw/sources/clips/new-way-build-second-brain-claude-nick-saraev/PROVENANCE.md), [hash manifest](../../raw/sources/clips/new-way-build-second-brain-claude-nick-saraev/SHA256SUMS).

## What the source says

- **Thesis:** most flashy second-brain content is slop. A useful one is a searchable pile of your own stuff that the AI looks up before it answers. He calls his system "Engram" and describes about 35 to 50 thousand records.
- **Pipeline:**
  - One small connector script per source (git history, company Claude sessions, video transcripts, email, Slack, call transcripts). Each pulls only what is new since its last run and stamps date and time. His Gmail example is read-only, pulled a year of email from three accounts, then runs every 15 minutes.
  - Index your Claude and ChatGPT sessions, which he says are normally deleted after 30 days.
- **Ingest-time metadata:** a cheap model writes a short summary per item (including the question someone would type to find it) plus "atoms": exact error messages, exact fixes, working commands, decisions with reasons. The agent searches the summaries, then is pointed to the raw item.
- **Search:** plain text with BM25 (word-frequency scoring), no embeddings. Recency weighting: boost new items, decay old ones, so a two-year-old price does not outrank a new one. Periodic sweeps prune items that are no longer valuable. At query time a fast inference step picks a search term, search returns in under half a second, and the matches are appended to the prompt.
- **Freshness:** a background script checks that connectors still work, because keys rotate and permissions change.
- He argues against dumping everything into the context window (context rot, cost, latency) and dismisses 3D brain graph views.

## Limits and distrust

- "3 or 4 minutes" to set up conflicts with the multi-connector pipeline he then describes.
- The "9/10" cost and speed reductions have no data. The claim that Boris Cherny said plain search beat every approach is hearsay.
- "Same system used by multi-billion dollar companies" sits beside the admission that it builds on a Cohere ingestion pipeline.
- The claim that ChatGPT sessions are stored locally as plain text looks wrong for web sessions (inferred, unchecked).
- The rebuild prompt is behind his free community and is not in the clip. No Obsidian involved.

## What this adds here

This is the only new retrieval design among the 2026-11-20 clips. It is a separate retrieval store, not a vault layout. Its four transferable ideas are an ingest-time summary that includes the likely question, "atoms" for exact fixes and decisions, recency decay, and connector freshness checks. ai-os currently routes through `wiki/index.md` and `system/scripts/query-brain.py` ([adoption ledger](../../references/ai-workspace/second-brain-adoptions.md)); none of these four is adopted. No action taken in this ingest.

Related: [Ultimate Second Brain (ARMS), brain.js retrieval](ultimate-second-brain-arms-robonuggets.md), [one vault versus many](../second-brain-one-vault-vs-many.md).

## Coverage

Read in full on 2026-11-20 by a read-only research pass; claims about the video were not independently re-checked. No earlier version exists in the vault.
