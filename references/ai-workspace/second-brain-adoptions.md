---
type: reference
subject: Second-brain ideas from outside setups, with what ai-os built, deferred and declined
created: 2026-10-14
updated: 2026-10-14
aliases: [second-brain adoption ledger, LLM wiki upgrade ledger, second brain upgrades 2026-10-14]
tags: [ai-workspace, second-brain, llm-wiki]
sources:
  - ../../wiki/sources/gd4ai-obsidian-llm-wiki.md
  - ../../wiki/sources/fable-5-karpathy-llm-wiki-nate-herk.md
  - ../../wiki/sources/jev-claude-os-chase-ai.md
  - ../../wiki/sources/ai-system-so-smart-dan-martell.md
  - ../../wiki/sources/7-claude-hacks-austin-marchese.md
  - ../../wiki/sources/harness-engineering-austin-marchese.md
  - ../../wiki/sources/stop-prompting-claude-karpathy-method-austin-marchese.md
  - ../../wiki/sources/karpathy/llm-wiki.md
---

# Second-brain upgrades: what ai-os took from outside setups, and what it refused

On 2026-10-14 Joshua asked for every second-brain idea in his clipped sources that ai-os did not already have, judged through the Karpathy method and folded into the existing setup rather than a rebuild. Three reviews ran in parallel: the GD4AI plugin's actual code, the second-brain videos, and the project Karpathy agent grading ai-os against Karpathy's LLM Wiki idea file. This page records the outcome for each idea. **Built** means it is in a file today and the check named beside it ran. **Pending** waits on Joshua. **Declined** carries the reason.

## The sources

| Source | Creator | Summary page | Status |
|---|---|---|---|
| obsidian-llm-wiki plugin: README and a 96-file code snapshot | GD4AI | [GD4AI wiki plugin](../../wiki/sources/gd4ai-obsidian-llm-wiki.md) | Ingested 2026-10-14 |
| Fable 5 + Karpathy's LLM Wiki is Basically Cheating | Nate Herk | [LLM wiki demo](../../wiki/sources/fable-5-karpathy-llm-wiki-nate-herk.md) | Ingested 2026-10-14 |
| This NEW Jev + Claude OS Just Changed Every AI Workflow | Chase AI | [Claude OS](../../wiki/sources/jev-claude-os-chase-ai.md) | Ingested 2026-10-14 |
| This AI System Will Make You So Smart It's Almost Unfair | Dan Martell | [AI brain](../../wiki/sources/ai-system-so-smart-dan-martell.md) | Ingested 2026-10-14 |
| 7 Claude Hacks That Feel Illegal (And 3 to Avoid) | Austin Marchese | [AI advice tier list](../../wiki/sources/7-claude-hacks-austin-marchese.md) | Ingested 2026-10-14 |
| Stop Prompting Claude. Start Harness Engineering | Austin Marchese | [Harness engineering](../../wiki/sources/harness-engineering-austin-marchese.md) | Ingested 2026-10-14 |
| Stop Prompting Claude. Use Karpathy's Method Instead | Austin Marchese | [Karpathy's method](../../wiki/sources/stop-prompting-claude-karpathy-method-austin-marchese.md) | Archived 2026-09-08; summary written 2026-10-14 |
| Obsidian in 24 Minutes | Tina Huang | [Obsidian levels](../../wiki/sources/obsidian-in-24-minutes-tina-huang.md) | Ingested 2026-10-14 |
| Personal Agents, Clearly Explained | Jeff Su | [Personal agents](../../wiki/sources/personal-agents-clearly-explained-jeff-su.md) | Ingested 2026-10-14 |
| How to Make AI Sound EXACTLY Like you | Dan Martell | [Voice method](../../wiki/sources/make-ai-sound-like-you-dan-martell.md) | Ingested 2026-10-14 |
| Karpathy's LLM Wiki idea file | Andrej Karpathy | [LLM Wiki](../../wiki/sources/karpathy/llm-wiki.md) | Already compiled; the reference design |
| I Turned Claude Into the Ultimate Second Brain; I Turned GPT-6 Astra Into the Ultimate AI Second Brain | Nate Herk | [Claude](../../wiki/sources/claude-ultimate-second-brain-nate-herk.md), [Codex](../../wiki/sources/gpt-6-astra-ultimate-second-brain-nate-herk.md) | Already compiled; used for comparison |
| I Built Another Andrej Karpathy Using Claude | Nate Herk | [Existing summary](../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md) | Not re-ingested. Joshua reversed its first ingest on 2026-10-08, and the inbox copy is the same bytes as then. The [Karpathy sub-wiki](../../wiki/karpathy/index.md) carries that work |

## What the Karpathy review found

The design is right and the gaps were small. Karpathy's argument is that a wiki compiles knowledge once at ingest and keeps it current, where retrieval-only setups rediscover it on every question ([LLM Wiki](../../wiki/sources/karpathy/llm-wiki.md)). Graded against that, ai-os is strong on raw evidence, schema and ingest, partial on query and the index, and weak on lint. Three concrete gaps:

1. **Lint was blind to 98% of the wiki.** The provenance check only looked at pages directly inside `wiki/sources/`, so the 3,831 nested Karpathy captures were never checked. Fixed: it now checks every depth and accepts an archive link plus SHA-256 in the body. Rerun result: 0 provenance findings across 3,903 pages.
2. **The index is too big to read first.** `wiki/index.md` is 1.14 MB, about ten times the scale the idea file vouches for, and 3,831 of its 3,903 rows are per-file Karpathy captures. Only 72 pages are curated knowledge. Decided and fixed: the index is now 30,958 bytes, see below.
3. **A renamed skill was still named in the hot page.** `wiki/karpathy/hot.md` told agents to use `ingest`. Fixed, along with eight other current files found by a sweep.

The review's "do not add" list stands as policy: no embeddings, vector database or search server; no Dataview, Marp or Canvas as requirements; no scheduled lint at today's finding counts; no empty `entities/` or `concepts/` folders to match a template; no rewriting old log entries; no automatic ingest of `raw/inbox/` or `raw/data-about-me/`.

## Built on 2026-10-14

| Idea | From | Where it lives | Check |
|---|---|---|---|
| Provenance at every depth under `wiki/sources/`; body SHA-256 counts for bulk captures | Karpathy review | `wiki-maintenance.py --lint` | 0 findings, 3,903 pages |
| Aliases on new knowledge pages, printed in the catalog after "Also:" | GD4AI | [Schema](../../system/schema/llm-wiki.md) conventions; catalog generator | `missing-aliases` |
| `evidence:` and `sha256:` on new source summaries, with drift detection | GD4AI | Schema; lint | `missing-evidence-hash`, `evidence-drift` |
| Verbatim `## Mentions in source` quotes, grounded word for word | GD4AI | Schema; ingest compilation step 4; lint | `ungrounded-quote`: 28 quotes on the 7 new pages pass |
| `contradictions:` frontmatter and two gates before recording one | GD4AI | Schema ingest step 7; compilation step 5; lint | `open-contradiction` |
| `reviewed: true` lock: approved pages are never rewritten | GD4AI | Schema; ingest, query and lint skills | Rule |
| A page only for subjects defined or discussed; entity versus concept; stop on an ambiguous name | GD4AI | Schema, "When a subject earns its own page" | Rule |
| Skip, merge, complementary or contradictory for every page touched; citations of other sources survive edits; link across sources | GD4AI | Schema steps 6 and 7; compilation steps 5, 6 and 9 | Reported in each ingest |
| Every ingest report ends with one schema suggestion | Nate Herk; GD4AI's schema advisor | Schema step 8; compilation step 9 | Rule |
| Stop on an empty source; short archive names past the Windows path limit | GD4AI; found during this ingest | `second-brain-ingest` steps 4 and 5 | Rule |
| A pasted URL becomes an inbox file: Firecrawl for pages, captions for videos, `gh api` plus a snapshot for repositories | Nate Herk | `second-brain-ingest` URLs section | Used for the GD4AI snapshot |
| Repeated extraction passes on long sources | GD4AI | Compilation step 1 | Rule |
| Query by aliases and keyword variants, then one hop of links and backlinks | GD4AI | Schema query section; `second-brain-query` step 1 | Rule |
| Say "not in the compiled wiki" before answering from elsewhere | GD4AI; Austin Marchese's KB answer | `second-brain-query` step 4 | Rule |
| Classify an answer as redundant, partly new or new before filing it | GD4AI | `second-brain-query` step 5 | Rule |
| Log retrieval misses with a `Miss:` line | Austin Marchese's feedback loop | Schema query section; `second-brain-query` step 6 | `rg "Miss:" wiki/log.md` |
| Thin pages and duplicate-name candidates | GD4AI | Lint | `thin-page`, `possible-duplicate` |
| Fix in causal order; fix orphans with links; retarget links before an approved merge | GD4AI | Schema lint section; `second-brain-lint` step 7 | Rule |
| Staleness and size check on context that loads every session | Austin Marchese's fridge | `second-brain-lint` step 4 | Manual |
| Search for an old name after any logged rename | Karpathy review | `second-brain-lint` step 4 | First sweep fixed 9 files |
| Entity candidates and folder-growth proposals, approved by Joshua | Dan Martell; Nate Herk | `second-brain-lint` step 5 | Report only |
| Re-hash every archive against its `SHA256SUMS` | Austin Marchese's hooks argument; GD4AI drift | `wiki-maintenance.py --evidence` | 439 files, 46 manifests, 0 findings |
| Commitments and stated preferences from session transcripts | Dan Martell | `transcript-intake` distillation step 4 | Rule |
| Scan the last 30 days of sessions for skill candidates | Chase AI | `level-up` inputs | Rule |
| Knowledge entries in the log always use `ingest`, `query` or `lint` | Karpathy review | Schema log section | `grep` |

"Rule" means the behavior is written into the schema or a skill and will be proven by the next real run, not by today's checks.

## Decided by Joshua and built (2026-10-14)

Settled in [the decision interview](../../brainstorms/2026-10-14-second-brain-upgrade-decisions.md).

| Decision | What was built | Check |
|---|---|---|
| Lock archived evidence | `system/scripts/hooks/guard-raw-sources.py`, a PreToolUse hook in `.claude/settings.json`: Claude's Write and Edit are refused on existing files under `raw/sources/`; new files and `PROVENANCE.md` notes are allowed. Codex and shell commands rely on `--evidence` | 12 simulated cases pass; a live no-op rewrite of an archived `SHA256SUMS` was refused and its hash is unchanged |
| Cap `wiki/hot.md` | 47 older session sections moved unchanged to [hot-archive/2026-10.md](../../wiki/hot-archive/2026-10.md), each with a matching log date; the page keeps the 3 newest sessions plus Active priorities, Now and Open threads. `wrapup` now enforces the cap | 122,010 bytes became 10,181; kept plus moved equals the original |
| Small index | `--index` writes one `catalog.generated.md` per Karpathy capture folder and lists those 5 hubs; the schema rule is now "every page reachable from the catalog" | `wiki/index.md` went from 1,145,933 to 30,958 bytes; the hubs list all 3,831 capture pages |
| A running to-do list from sources | New `second-brain-task` skill owns the [AI action queue](action-queue.md) and the [LSAT U idea queue](../../wiki/lsatu-idea-queue.md). Ingest step 6 adds every actionable item; a finished item is removed and recorded on its source page. `pickup` shows one line of counts | Backfill from 19 AI sources: 8 open items, every link resolves, every item ends in a Check step |

## Declined or deferred

| Idea | From | Reason |
|---|---|---|
| Embeddings, vector search, PageRank retrieval | GD4AI | Their own roadmap records an unseeded random generator and losses at the keyword stage; keyword variants and one-hop links keep the useful part |
| Hub detection and retirement | GD4AI | Needs hundreds of concept pages; there is one |
| Trimming the log at 512 KB | GD4AI | `wiki/log.md` is append-only. Yearly archive files are the fallback if Obsidian slows down |
| Resolving `[[Alias]]` links | GD4AI | Obsidian does not resolve them, so lint would hide real breakage |
| A controlled tag vocabulary | GD4AI | Their drift came from small models tagging at volume. Revisit when concept and entity pages number in the dozens |
| A nightly job that creates, merges and prunes pages | Dan Martell | Unattended automation writes only generated files; nothing is deleted without Joshua; conflicts stay visible. The read-only half lives in lint |
| Scheduled lint | Dan Martell; the clip review | Two findings today do not justify it. Revisit if findings accumulate between runs |
| Separate vaults per data type | Nate Herk | One connected vault was recommended on 2026-10-07; a nested sub-wiki like `wiki/karpathy/` is the compatible form |
| Letting the model move files and folders | Chase AI | Pages link by path and evidence is immutable; no bulk move without approval |
| Syncing copies of Drive or Notion into the wiki | Austin Marchese | Live systems stay authoritative and are read live, per [connections](../../connections.md) |
| Jev request routing | Chase AI | Unidentified product; claims unverified |
| Dashboard and headless skill buttons | Chase AI | Already weighed in [the command-center reference](../obsidian-command-center.md) |
| A daily three-to-five-line note; a general `people/` folder | Dan Martell | Not evaluated. Revisit if non-student contacts start recurring |

## New information (2026-10-14)

After the reviews above, Joshua installed the Smart Connections 4.7.2 and Smart Context 3.3.2 Obsidian plugins (local embeddings in the git-ignored `.smart-env/`) and removed "there is no semantic search and none is needed" from `CLAUDE.md` and `AGENTS.md`. The "Embeddings, vector search, PageRank retrieval" row under Declined, and the "no embeddings" line in the Karpathy review's do-not-add list, were written before that install and are left as they were. Whether agents use the plugin is AQ-010 in the [AI action queue](action-queue.md). The later batch ([Tina Huang](../../wiki/sources/obsidian-in-24-minutes-tina-huang.md), [Jeff Su](../../wiki/sources/personal-agents-clearly-explained-jeff-su.md), [Dan Martell](../../wiki/sources/make-ai-sound-like-you-dan-martell.md)) added no new second-brain method; each summary records what is already here.

## How to check it still works

From the vault root:

```bash
py system/scripts/wiki-maintenance.py --lint
py system/scripts/wiki-maintenance.py --evidence
```

The lint report (`system/generated/wiki-lint.generated.tsv`) should show no `ungrounded-quote`, `evidence-drift` or `missing-evidence-hash` rows. The evidence report (`system/generated/evidence-check.generated.tsv`) should be empty apart from its header. A row in either is evidence that something changed, not a reason to rewrite the source.

Related: [second-brain levels](../second-brain-levels.md), [AI workspace hub](index.md), [vault schema](../../system/schema/llm-wiki.md).


## New information (2026-10-26): ARMS and a retrieval test before a new graph

[RoboNuggets' ARMS walkthrough](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) supplies a complementary inventory lens: applications, routines, memory and skills, with visible relationships and direct file/skill access. Applications show both automation reach and granted trust; forgotten integrations and schedules are review candidates, not permission to disconnect or retire them. Existing connection, skill and wiki inventories provide starting material rather than a reason to rebuild the vault.

The narrator describes deterministic keyword extraction, indexed candidate ranking, section reads and pointer following before handing evidence to the model. He reports about 30,000 versus 50,000 message tokens in a two-session demonstration, but the supplied transcript contains no reproducible benchmark, correctness grades or raw traces. A local evaluation should compare answer correctness, misses, elapsed time, tokens and maintenance cost with the current index/alias workflow before adopting another retrieval layer. His graph's roughly 30% value estimate and under-ten-second reload goal are source opinions/targets, not measured ai-os outcomes.

The source names last30days, QMD, G Brain and Graphify, and promotes an R65 guide, an import-ready system and RUBRIC; exact upstream code and guide contents were not supplied. [The Graphify bridge](../graphify-obsidian-bridge.md) already covers source-connected navigation. New inventory, retrieval, resource and graph UX evaluations belong in the [AI action queue](action-queue.md); ingestion did not install tools, rebuild navigation or alter live permissions. See the source summary for the complete suggestion-by-suggestion disposition and coverage limits.

## Implemented under delegated judgment (2026-10-26)

[Full source implementation and remaining queue](../../research/2026-10-26-source-implementation/REPORT.md). Useful parts now include a [bounded compiled-page helper](compiled-retrieval.md), [generated ARMS inventory](operating-inventory.md), term-first/fresh-practice instructions, an explicit verification-plan rule, a finite design critique worksheet and teacher-only RC reference forms.

Smart Connections is retained as an optional Obsidian aid; agents keep the compiled catalog/alias route, with the helper optional after navigation. This operating choice settles AQ-010 under Joshua's delegated judgment and does not assert a new plugin benchmark, completed embeddings or a permanent ban on semantic tools. The dated 2026-10-14 no-embeddings/awaiting-choice rows above are historical rather than current restrictions.

All42 proposals were assessed:9 completed evaluations/implementations and14 deliberate no-adoption decisions are source-recorded;19 specific checks remain open. A script benchmark passed8hand-selected top-three/miss cases, not an actual model-token-cost experiment. No extra graph, replacement vault, whole business plugin, mod or tool stack was installed. Source claims, official-document checks, local regression tests and historical native acceptance remain distinct.
