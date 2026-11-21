---
type: source
subject: GD4AI's Obsidian plugin implementing Karpathy's LLM Wiki, read as README plus a source snapshot
created: 2026-10-14
updated: 2026-10-14
aliases: [Karpathy LLM Wiki Plugin for Obsidian, GD4AI obsidian-llm-wiki, karpathywiki plugin]
tags: [ai-workspace, second-brain, llm-wiki, obsidian, lint, contradictions]
evidence: "../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/GD4AI obsidian-llm-wiki README.md"
sha256: d5224564ce46fccc45d5ed4f4e0bf2ff0d1ebdfa72e7886069bd1db79e23d661
sources: [../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/PROVENANCE.md, ../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/PROVENANCE.md]
contradictions: []
---

# GD4AI's wiki plugin: copy its measured gates, skip its graph retrieval

"Karpathy LLM Wiki Plugin for Obsidian" is the README of the GitHub repository GD4AI/obsidian-llm-wiki ([GitHub](https://github.com/GD4AI/obsidian-llm-wiki)), maintained by green-dalii (author) and DocTpoint. The README's publication date is unknown; the inbox file was last modified 2026-10-14. A separate source snapshot was taken the same day: 96 files from `main` at commit `afa3d3f`, committed 2026-10-12, retrieved read-only through `gh`. It is a selection (docs plus ingest, contradiction, provenance, lint, query and schema modules), not the whole repository. The plugin was not installed or run. Read on 2026-10-14: the full README; in full, `AGENTS.md`, `ROADMAP.md`, every file in `src/wiki/prompts/`, `src/wiki/contradictions.ts`, `src/core/paragraph-provenance.ts`, `src/core/source-requirements.ts`, `src/core/ingest-state.ts` and `src/wiki/lint/controller.ts`; in part, the other modules linked below and `MEMORY.md`.

Evidence: [README clip, provenance and hashes](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/PROVENANCE.md). SHA-256 `d5224564ce46fccc45d5ed4f4e0bf2ff0d1ebdfa72e7886069bd1db79e23d661`. Code: [snapshot provenance](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/PROVENANCE.md), with a `SHA256SUMS` covering every snapshot file (all verified 2026-10-14).

## What it says

### The README

- **Positioning (Why this plugin?).** A one-click Obsidian plugin for Karpathy's LLM Wiki idea, with no embedding model and no vector database. It compares itself with nashsu/llm_wiki, SamurAIGPT/llm-wiki-agent and atomicstrata/llm-wiki-compiler. It claims 16+ model providers and 11 languages.
- **Ingest (Quick Start, Core commands).** Ingest one note, a folder, or a picked set of files. Output lands in `wiki/sources/`, `wiki/entities/` and `wiki/concepts/`. The README says the plugin never modifies original notes. A pre-ingest gate rejects empty, whitespace-only or frontmatter-only notes before any model call, and content-hash dedup catches identical files. An optional candidate gate drops names that appear only in parentheses, enumerations or short list items.
- **Knowledge quality (Features).** Entity and concept extraction at configurable granularity. Every page must carry at least one alias. Tiered duplicate detection. Smart merge with contradiction flags. Pages marked `reviewed: true` are protected from overwrite. One tag vocabulary with a write gate; the README says small and local models still drift, about one in ten returning their built-in taxonomy.
- **Verbatim quotes (Document / PDF / Image ingest).** Since v1.27.0 every source page carries a "Mentions in Source" section built from the verbatim quotes the extraction captured.
- **Lint and Smart Fix (Query & maintenance).** Lint finds duplicates, dead links, empty pages, orphans, missing aliases and contradictions. Smart Fix All repairs in causal order: aliases, then duplicate merges, then dead links, then orphans, then empty pages. A setting can stop it from writing stub pages for unresolvable links.
- **Query (How retrieval works).** Five stages: a lexical match on titles and aliases; 8 to 12 model-generated cross-language keywords; a local substring scan with those keywords; a model fallback; then Personalized PageRank over the `[[wiki-link]]` graph (Monte Carlo, 3,000 walks of 50 steps). The README claims PPR@5 of 27.1% against a 24.1% kNN baseline on the project's own corpus.
- **Models.** Long context (200K+) for vaults over about 500 pages; instruction-following matters more than raw capability; local models for query, cloud models for ingest.
- **Privacy.** No backend of its own. The optional MinerU document path uploads files to mineru.net, which the README says publishes no retention statement.

### The code and planning docs (snapshot)

- **Extraction prompt** ([ingestion.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/prompts/ingestion.ts)). Each item needs 2 to 4 verbatim quotes. A `coverage` field records whether the source "defined", "discussed" or only "named" the item, and the prompt tells the model to report, not judge. A numbered entity-versus-concept decision tree ends "prefer concept over entity". A wiki-link test: if no other note would link to it, do not extract it.
- **Page prompts** ([generation.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/prompts/generation.ts)). Aliases are required. A `reviewed: true` page is never rewritten; new facts go into a dated "New Information" section, and contradicting facts are not added. A schema-advisor prompt only proposes changes; nothing applies until the user clicks Apply.
- **Merge triage** ([merge.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/prompts/merge.ts)). Four strategies: skip, merge, complementary, contradictory. A contradictory item must copy the conflicting page sentence verbatim (`existing_statement`). When unsure, merge rather than drop.
- **Contradiction gates** ([contradiction-gates.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/page-factory/contradiction-gates.ts)). The header records a measurement: of nine contradictions recorded in one night, two were real, three were views the source only reported, and four conflicted with nothing on the page. A prompt-only rule removed the false positives and the planted true positive alike. Two checked gates replaced it: the quoted sentence must be on the page, and a separate small call must confirm the source holds the claim itself (24/24 and 48/48 in their test).
- **Durable carriers** ([contradiction-record.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/core/contradiction-record.ts), [contradicted-marker.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/core/contradicted-marker.ts)). An open contradiction lives in a `contradictions:` frontmatter list and a record file. An inline "Potential Contradiction" body block is not durable, because the next model rewrite strips sections the schema does not know.
- **Citation preservation** ([paragraph-provenance.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/core/paragraph-provenance.ts)). On a multi-source page, a paragraph footnoted to source X may disappear only when X itself is being merged. Lost paragraphs are put back and stripped footnotes re-attached.
- **Drift** ([ingest-state.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/core/ingest-state.ts), [source-requirements.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/core/source-requirements.ts)). Each source page stores a hash of the note body it was built from. A mismatch marks the note "drifted". Pages with several origins answer "not drifted" because one stored hash cannot tell which origin changed.
- **Lint orchestration** ([controller.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/lint/controller.ts)). The Smart Fix order in code: polluted pages, aliases, duplicates, dead links, orphans, empty pages, retagging. The full report is written to the log.
- **Query fallback** ([assemble-context.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/query-engine/pipeline/assemble-context.ts)). With no matching pages, the answer is labeled as coming from the model's general knowledge, not the vault.
- **Saving answers** ([conversation.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/prompts/conversation.ts)). A value check, then a dedup check against the index; a fully redundant answer is not saved.
- **Log, hubs.** The log is trimmed at 512 KB, dropping the oldest entries ([log-writer.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/wiki/engine-internals/log-writer.ts)). Hub pages are detected by in-degree and retired by clustering percentile ([hub-retirement.ts](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/src/core/hub-retirement.ts)).
- **Their own measured warnings** ([ROADMAP.md](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/ROADMAP.md), `MEMORY.md`). About 95% of graph edges stay within one source, and 9 in 10 pages have no incoming link from another source. A query test lost 3 of 5 multi-note questions at the lexical seed stage, before any graph step. `monte-carlo-ppr.ts` defaults its random generator to `Math.random`, so reruns move the numbers; seeding it is listed as a prerequisite.
- **Process** ([AGENTS.md](../../raw/sources/clips/gd4ai-obsidian-llm-wiki-readme/repo-snapshot-afa3d3f/AGENTS.md)). Six quality gates, explicit "push it" and "merge it" approvals, a plain-English writing standard, and a rule that no document may only grow. One line only; it is about their code project.

## Mentions in source

> "The plugin modifies nothing in your original notes" (Quick Start)

> "empty / whitespace / frontmatter-only notes are rejected before any LLM call; content-hash dedup catches identical files across paths" (Query & maintenance)

> "Small/local models still drift (about one in ten returns the model's built-in taxonomy)" (Features)

> "every link you write already enriches retrieval; no separate tagging/embedding/indexing step" (Is it for me?)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. Decisions and their implementation status are in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md). "Live" marks a check in `system/scripts/wiki-maintenance.py`; the other adopted rows are rules in the [vault schema](../../system/schema/llm-wiki.md) and the ingest, query and lint skills, all added 2026-10-14.

| Their idea | Here | Verdict |
|---|---|---|
| Pre-ingest gate for empty or frontmatter-only sources | Ingest workflow | Adopted |
| Stored source hash with drift detection; a separate `evidence:` field | `evidence:` and `sha256:` frontmatter; `evidence-drift` lint (live) | Adopted |
| Coverage test (defined, discussed, named) before creating a page; entity versus concept rule | Ingest workflow | Adopted |
| Verbatim mentions with a quote-grounding lint | This page's quote section; `ungrounded-quote` lint (live) | Adopted |
| Citation-set preservation when a multi-source page is edited | Ingest workflow | Adopted |
| Four-way merge triage: skip, merge, complementary, contradictory | Ingest workflow | Adopted |
| Two contradiction gates and a durable `contradictions:` carrier | `contradictions:` frontmatter; `open-contradiction` lint (live) | Adopted |
| `reviewed: true` lock | Page convention | Adopted |
| Aliases required and shown in the catalog | `missing-aliases` lint (live); generated catalog | Adopted |
| Query keyword variants plus one-hop link expansion; "not wiki-backed" label; redundancy gate before filing answers | `second-brain-query` | Adopted |
| Smart Fix order; duplicate candidates; thin-page check; cross-source linking step | `second-brain-lint`; duplicate candidates and `thin-page` lint (live) | Adopted |
| The plugin itself; embeddings; PageRank graph retrieval | Their roadmap records an unseeded generator and losses at the keyword stage | Skipped |
| Hub detection and retirement | Needs hundreds of concept pages | Skipped |
| Log trimming at 512 KB | `wiki/log.md` is append-only | Skipped |
| Alias-based link resolution | Obsidian does not resolve `[[Alias]]` links, so it would hide real breakage | Skipped |

- **The value is in their measured failures, not their features.** Four are worth recording here. About 95% of links stay within one source, so cross-source linking needs its own step. Prompt-only contradiction rules removed real contradictions along with false ones. Inline contradiction notes in a page body disappear on the next rewrite. Free-form tags drift.
- **Their roadmap undercuts their headline retrieval claim.** The README leads with PageRank, but their own measurement says the loss happens earlier, at the keyword stage, and reruns are not reproducible until the generator is seeded. Keyword variants and one-hop expansion keep the useful part without the graph machinery.
- **The contradiction design fits our existing rule.** `CLAUDE.md` already says conflicts stay explicit until adjudicated. Their two gates make that rule checkable: a conflict needs a sentence on the page and a claim the source actually holds.

Related: [LLM Wiki pattern](llm-wiki-pattern.md), [vault schema](../../system/schema/llm-wiki.md), [Nate Herk's LLM wiki demo](fable-5-karpathy-llm-wiki-nate-herk.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- The plugin was not installed or run. Every behavior above is read from the README or from code, not observed.
- README claims were not verified: the "Obsidian Review Perfect Score", the PPR@5 benchmark (their own corpus and script), the provider and language counts, and the model list.
- The snapshot is 96 selected files, not the full repository. `MEMORY.md` was read only around its cross-source measurement record (lines 670 to 700) and by search; `CHANGELOG.md` only by search. Some modules were read only in their headers.
- Their measurements (the nine-contradiction night, 24/24 and 48/48, the 95% figure) come from their own vaults and were not reproduced.
- Adopted rules are written into the schema and skills; whether they improve real ingests is untested until the next sources go through them.
