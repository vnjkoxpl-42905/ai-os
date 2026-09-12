# ai-os knowledge graph — batch 1 (knowledge core)

A concept map of the vault's knowledge core. Nodes are **concepts, not documents**:
306 source files became 1,942 concepts joined by 2,745 edges, in one connected
component. Every concept links back to the real vault file it came from, so this is
a navigation layer over the vault rather than a copy of it.

Built 2026-07-20. Method and traps: `references/graphify-obsidian-bridge.md`.

## What is in scope

corpus · students · wiki · decisions · references · brainstorms · research ·
handoffs · raw/sources/clips (was Clippings, folded in 2026-09-08) · context

**Not** in this batch: `projects/lsatu/` (2,024 files) and `skills/` (1,103 files).
Together those are 60% of the vault by word count and are mostly application code
and skill definitions — high node count, low insight density. Batch 2 decides
whether they earn their place.

## How to use it

- **`graph.canvas`** — structured layout, communities as groups. Best first look.
- **Graph view** — one connected mass. Islands would mean a rebuild regressed.
- **`_COMMUNITY_*` notes** — 25 overviews with cohesion scores and dataview queries.
- **Any concept note** — `## Connections` gives the neighbours, `## Source` opens
  the vault file it was extracted from.
- **`../vault-run/graphify-out/GRAPH_REPORT.md`** — god nodes, surprising
  connections, suggested questions.
- **`../vault-run/graphify-out/graph.html`** — interactive, no server needed.

## Communities

| Community | Nodes | Cohesion |
|---|---:|---:|
| Dakota Session Arc | 174 | 0.02 |
| Main Conclusion Bootcamp Build | 134 | 0.02 |
| Flaw Module and Bootcamp Design | 124 | 0.02 |
| Sofia and Nicole Records | 121 | 0.02 |
| Wiki Ledgers and Automation Backlog | 105 | 0.03 |
| Causation and Conditional Logic | 96 | 0.03 |
| Role, Parallel and Flaw Drills | 95 | 0.02 |
| Second Brain Architecture | 92 | 0.02 |
| Bella and Adriana Records | 91 | 0.03 |
| Decisions Log and Three Ms | 86 | 0.03 |
| Takeout Ingest and Session Mining | 84 | 0.03 |
| Lydia and Meghan Records | 78 | 0.05 |
| Agentic OS Power Phrases | 76 | 0.03 |
| Assumption and Principle Homework | 75 | 0.03 |
| LR Taxonomy and Curriculum Meta | 68 | 0.04 |
| Booking Admin and Links Design | 64 | 0.03 |
| David and Ethan Records | 64 | 0.04 |
| Argument Structure Core | 61 | 0.05 |
| Live Status and Smaller Rosters | 54 | 0.05 |
| C. Alexander and Booking Passes | 53 | 0.06 |
| Business Model and Onboarding | 51 | 0.04 |
| Question-Feature Index and Graph Bridge | 38 | 0.08 |
| Lovable Cloud Platform | 24 | 0.09 |
| Calendly Teardown and Booking UI | 18 | 0.14 |
| Graphify and Knowledge Graph Layer | 16 | 0.15 |

Cohesion is low across the big communities because this corpus is genuinely
cross-cutting — a Dakota session touches curriculum, teaching method, and student
record at once. Low cohesion here reads as "the vault is interconnected," not
"clustering failed."

## Verified at build time

- 1 connected component, 1,942 / 1,942 nodes (100%)
- 306 / 306 source files produced at least one node
- 1,942 / 1,942 concept notes carry a `## Source` link
- 9,678 / 9,678 wikilinks resolve
- 0 dangling edges after ID validation

## Rebuild

Scripts live in `../vault-run/`: `merge.py` (merge + dedupe + connectivity gate),
`apply_stitch.py` (validate and apply bridge edges), `wire_sources.py` (source
wiring). Re-extraction needs the chunk manifest at
`../vault-run/graphify-out/.chunks.json`.

**Ship gate:** `nx.connected_components` must return 1. Node and edge totals look
identical whether a graph is whole or shattered — they are not evidence of health.
