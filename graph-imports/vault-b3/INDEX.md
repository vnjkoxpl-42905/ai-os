# Batch 3 — the skill catalog as a knowledge graph

750 concepts, 1,174 edges, one connected component, 17 communities, built from
`skills/` on 2026-07-20. Verified by `../vault-run-b3/verify.py`: 14 checks pass,
0 failures.

This graph answers three questions the flat catalog cannot: **what can this OS
actually do**, **which skills overlap or duplicate each other**, and **what
chains into what**. It is built around concepts, not skills — a technique three
skills share is one node referenced three times, not three near-identical nodes.
That is what keeps any single large skill from owning a community.

## Scope — what is and is not in here

`skills/` holds 1,103 markdown files. This graph is built from **392** of them.
The gap is deliberate, not sampling:

| Step | Files | Why |
|---|---|---|
| All `.md` under `skills/` | 1,103 | starting point |
| after content-hash dedup | 625 | 478 were byte-identical copies, almost all `claude/` ↔ `codex/` mirrors |
| after scope filter | 460 | dropped `_snapshots`, `_project-forks`, `_inactive`, `reference/open-design` — third-party authorship |
| after vendor shallow rule | **392** | 13 vendor skills (higgsfield, notebooklm, shadcn, openai-docs, imagegen, chrome-devtools, discord) contribute only their `SKILL.md`, not their reference docs |

Vendor skills are **present as capability nodes** — the OS really can do image
generation and NotebookLM work, and a graph that denied it would be wrong. Only
their SDK boilerplate was skipped, which cut ~250k tokens of low-insight text.

**Dedup did not lose provenance.** Each note's `## Source` lists the canonical
file and, where one existed, the byte-identical twin as "also at". A concept
with a twin is live in *both* runtimes; one without is live in only one. That
asymmetry is real information and is preserved.

## Communities

| # | Community | Nodes | Cohesion |
|---|---|---|---|
| 0 | Frontend Design Craft (impeccable) | 87 | 0.05 |
| 1 | EA Operations and Safe Outbound Actions | 84 | 0.04 |
| 2 | Plan Review, MCP Building and Cross-Runtime Parity | 70 | 0.05 |
| 3 | Platform Automation and Codebase Practice | 63 | 0.04 |
| 4 | Interview-Driven Discovery and Evaluation | 56 | 0.05 |
| 5 | Skill Catalog, Docs and Plan Artifacts | 52 | 0.05 |
| 6 | LSAT Bootcamp Build and Gated Execution | 47 | 0.06 |
| 7 | Debugging Discipline and Mutation Gates | 46 | 0.05 |
| 8 | Claude-Codex Handoff and Cross-Model Build | 45 | 0.06 |
| 9 | Adversarial Verification and Variant Generation | 36 | 0.07 |
| 10 | Skill Authoring and Progressive Disclosure | 32 | 0.08 |
| 11 | Command Authoring and Completion Discipline | 29 | 0.08 |
| 12 | Tool-Layer Security and Least Privilege | 28 | 0.09 |
| 13 | Browser Verification and Design Tokens | 23 | 0.09 |
| 14 | Skill Quality Engineering | 22 | 0.12 |
| 15 | Design Taste and Anti-Generic Aesthetics | 20 | 0.14 |
| 16 | Hooks, Bundling and Untrusted Input | 10 | 0.29 |

The distribution is flatter than either prior batch — largest community 11%,
against batch 2's 14% and batch 1's 174-node Dakota cluster. The `impeccable`
skill was the skew risk here (36 files, 99 raw nodes, one indivisible chunk) and
it did not dominate: the top hub in the whole graph is `gws CLI` at degree 31,
with `impeccable` second at 23.

## Where to start

- **Graph view** — one connected mass. Islands mean a rebuild regressed.
- **`_COMMUNITY_*`** — 17 overviews with cohesion scores and dataview queries.
- **Any concept note** — `## Connections` gives neighbours, `## Source` opens the
  skill file it came from plus its deduped twin.
- **`../vault-run-b3/graphify-out/GRAPH_REPORT.md`** — god nodes, surprising
  connections, suggested questions.
- **`graph.canvas`** — structured community layout.

## Findings worth acting on

These came out of extraction and are claims about the catalog, not about the
graph. Each is worth a look before it is treated as true.

- **Two browser-automation stacks with no shared source.** `codex/playwright`
  (CLI-first, ref-based) and `claude/webapp-testing` (Python, selector-based)
  independently teach the same reconnaissance-then-action technique and the same
  staleness failure mode. The clearest consolidation candidate in the catalog.
- **`grill-me` and `grill-me-codex` share a byte-identical Act 1** interview
  (attributed to Matt Pocock, MIT).
- **A live contradiction between two design skills:** `image-to-code` bans
  nested containers while `high-end-visual-design` mandates the nested
  double-bezel shell. Recorded as a tension, not reconciled.
- **A second tension:** `setup_preflight_gate` says never announce success, while
  `writing-plans` and `finishing-a-development-branch` mandate announcing the
  skill at start.
- **A third, and the sharpest:** read-only isolation is the correct posture for
  *review* subagents and is precisely the silent-failure mode for *extraction*
  subagents. This run produced a live instance — see residuals.
- **`command-development` is self-declared legacy**, pointing at
  `skill-development` as preferred.
- **The `gws-*` family is machine-generated** and near-identical in shape; four
  separate extraction agents independently collapsed it the same way.

## What went wrong, and what was done about it

Five defects surfaced. Four are fixed in the pipeline, not just in the output —
the distinction matters, because a fix applied only to built files evaporates on
the next rebuild.

1. **An extraction agent misreported its own coverage.** Chunk 09 claimed "48 of
   48 files read, every file contributed a node" while the entire
   `obsidian-markdown` skill (4 files) had produced nothing. **A subagent's
   self-report is a claim, not evidence.** Fixed: patched to 392/392, and
   `verify.py` now recomputes every number from artifacts on disk rather than
   trusting any reported figure.
2. **A note was born hidden.** `.claude/plugin-name.local.md settings pattern`
   sanitized to a leading-dot filename — invisible to Obsidian, skipped by shell
   globs, despite carrying degree 8. It was found only because two file counts
   disagreed by one. Fixed at the cause: `fix_vault_names.py` runs as a pipeline
   step and is idempotent. The label is deliberately left dotted, because
   `.claude/...` is the file's real name and rewriting it would make the graph
   lie.
3. **`merge.py` silently dropped provenance.** It unioned only `source_file`
   (batch 2's shape) while batch 3's agents emit `sources` (a list), so every
   merged node would have lost its source list and read as unsourced. Fixed
   before it could ship.
4. **Two edges were category errors.** `higgsfield-soul-id → PLAN.md frozen
   spec` at 0.40 (its own evidence conceded "weak, label-level only") and
   `guided-drill-assignment → TDD cycle` at 0.55 (evidence explicitly said the
   target was wrong as written). Fixed via `corrections.json` +
   `apply_corrections.py`, kept as reviewable data rather than a hand edit. The
   first could not simply be dropped — it was that node's only edge, so deleting
   it would have orphaned a real capability and broken the ship gate. It was
   repointed to `generative_media_creation` instead.
5. **`skills/INDEX.md` was truncated** at line 273 of 412 by a read cap, and the
   agent's "already covered" judgment went unverified. **Now verified and
   closed:** of 136 skill names in the tail, only 20 appear nowhere else, 13 of
   those had their own `SKILL.md` extracted, and the remaining 7 are `lsatu:`
   project-fork entries the scope filter excluded by design. The truncation cost
   nothing.

## Known residuals — read before trusting

- **Community assignment is not reproducible.** Louvain clustering is
  stochastic: re-running it on the same graph produced 18 communities instead of
  17, with membership shifted enough that several labels mapped onto two
  clusters each. The partition published here is the original hand-labelled one,
  retained deliberately. **A rebuild reproduces the nodes and edges exactly, but
  not necessarily these communities.** Treat community boundaries as one valid
  cut, not the cut.
- **128 edges are INFERRED**, reasoned from labels rather than source text. 30
  sit below 0.65 confidence. Both were reviewed once; the two clearest errors
  were corrected and the rest are defensible but thin. Treat as leads.
- **18 INFERRED edges are hand-authored stitch edges** in
  `../vault-run-b3/graphify-out/.stitch.json`, bridging 5 orphan components.
  They took connectivity from 98.7% to 100%, so **the 100% figure is partly
  hand-made**, not fully emergent.
- **Fuzzy collapse is conservative by choice.** Only word-order duplicates merge.
  Semantically-equivalent but differently-worded labels — "Chat-only context
  handoff" vs "Context Handoff Before Reset" — stay separate, joined by a stitch
  edge. Force-merging those risks destroying real distinctions.
- **Chunk 10 read some reference docs at heading/skim depth** rather than in
  full. Coverage counts them; depth is lower than the `full` flag implies.
- **Cohesion is low across the board** (0.04–0.29). Expected for a catalog of
  loosely-related tools rather than a single argument, but community boundaries
  are softer than the confident labels suggest.

## On merging this into the vault root — recommendation: do not

The open question across several sessions has been whether these graph vaults
render usefully in Obsidian or as one undifferentiated mass. The premise was
wrong, which is why it never resolved:

**`~/ai-os` is itself the Obsidian vault** (`.obsidian/` sits at the root), so
`graph-imports/` is already inside it. These notes are already in the graph view
and already in search. Nothing needs merging to make them visible.

The counts:

| | notes |
|---|---|
| `graph-imports/` (all generated) | 5,406 |
| everything else in the vault | 3,171 |

Generated content already outnumbers real notes roughly 1.7 : 1, and
`.obsidian/app.json` sets **no `userIgnoreFilters`**, so nothing is excluded from
search or the graph view.

So the vault-root merge would not add reach — it would only remove the folder
boundary that is currently the single thing keeping the real notes findable.
**Recommendation: do not merge.** Instead add `graph-imports/` to Obsidian's
excluded-files setting so the working vault stays usable, and open each graph
vault as its own vault when exploring it.

Not verified: how this actually looks on screen. The counts and config are
measured facts; visual rendering was not observed.

## Rebuild

    cd graph-imports/vault-run-b3
    P=$(cat graphify-out/.graphify_python)
    $P merge.py             # collapse + fuzzy pass + coverage + ship gate
    $P apply_stitch.py      # bridge orphan components
    $P apply_corrections.py # reviewed edge fixes, refuses orphaning drops
    # ... regenerate vault via graphify export (see wiki/log.md) ...
    $P wire_sources.py      # source + dedup-alias links
    $P fix_vault_names.py   # rescue notes born as hidden dotfiles
    $P verify.py            # independent check — recomputes, trusts nothing

The ship gate is `components: 1`. Anything else is not shippable. Node and edge
totals look identical whether a graph is whole or in pieces, so connectivity is
the only honest health signal.

`verify.py` is the backstop and exits non-zero on failure. Its rule: **never
verify a graph with a number the thing being verified supplied.** Every count it
reports is recomputed from files on disk. That rule exists because the one
defect that nearly shipped was an agent confidently certifying its own coverage.

Corpus definition lives in `graphify-out/.b3_corpus.json` (392 canonical files
with depth flags and dedup aliases) and `graphify-out/.b3_chunks.json`.
