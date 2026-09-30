---
type: source-summary
subject: LLM Wiki pattern
sources: [../../raw/sources/llm-wiki-pattern-2026-09-30/source.txt]
created: 2026-09-30
updated: 2026-09-30
tags: [second-brain, knowledge-management, llm-wiki]
---

# Compile knowledge once, then keep it current

The supplied idea file describes an LLM-maintained wiki between curated source documents and the questions a person asks.

## What the source says

1. Raw sources remain immutable evidence. The LLM reads them without rewriting them.
2. The wiki accumulates summaries, entities, concepts, comparisons, and synthesis. New sources update existing pages and expose contradictions.
3. A schema defines the folder conventions and the ingest, query, and lint workflows.
4. The index catalogs content; the log records changes chronologically. Useful answers can become durable wiki knowledge.
5. The human curates sources and directs the analysis. The LLM maintains the pages and cross-references. Search, images, plugins, slides, and batch ingestion are optional.

The source describes 10 to 15 changed pages as a possible result of one ingest, not a required count. It explicitly leaves exact folder structure and tooling to the domain.

## Evidence

- [[raw/sources/llm-wiki-pattern-2026-09-30/source.txt|Preserved source text]]
- [[raw/sources/llm-wiki-pattern-2026-09-30/PROVENANCE|Origin and copy verification]]
- [[raw/sources/llm-wiki-pattern-2026-09-30/SHA256SUMS|Source hash]]

## Where this leads

[[wiki/concepts/compiled-knowledge|Compiled knowledge]] explains the reusable idea. [[system/schema/llm-wiki|The operating schema]] defines its implementation in this existing vault. The [[wiki/index|index]] locates pages and the [[wiki/log|log]] records this ingest.
