---
type: reference
subject: Graphify to Obsidian turning a corpus into a navigable map
updated: 2026-07-20
aliases: []
---

# Graphify to Obsidian: turning a corpus into a navigable map

How to take any corpus, build a knowledge graph from it, and land that graph in
the vault as linked markdown Claude can traverse. Method note, not state.

Source: Chase AI, "Graphify + Obsidian + Claude Code = CHEAT CODE" (2026-06-08),
clipped 2026-07-20, ingested the same day. First run: `graph-imports/claude-code-docs/`.

## Why it exists

Graphify alone produces a graph in a vacuum. It maps one corpus and knows nothing
about anything else. The vault is the opposite: wide context, no concept map. The
bridge writes every graph node out as a markdown note with backlinks matching the
graph edges, so the map lands inside the context.

Worth it when the corpus needs to sit next to material already reasoned about.
Not worth it when the corpus is self-contained.

## How it works

`--obsidian` (with `--obsidian-dir <path>`) is a real flag on the graphify skill
pipeline, step 6. Not a bare CLI subcommand: `graphify --help` does not list it.

Nodes are **concepts, not documents**. The first run pulled 170 doc pages into 963
concepts and 1,239 connections. That ratio is the point. One note per source page
would just be a copy; concepts plus edges are a map.

## The four integration strategies

Ranked by how easily undone:

1. **Standalone vault** - graphify's default (`graphify-out/obsidian`). Fully siloed.
2. **Quarantine subfolder** - write into the main vault under one folder. Delete
   the folder to undo. What we used.
3. **Selective harvest** - keep only the nodes worth keeping.
4. **Redistribution** - scatter notes into existing folders. Best coherence,
   hardest to reverse.

## The step that actually matters

**Generated stubs are near-worthless on their own.** A stub is a title, a list of
edges, and a `source_file:` string in frontmatter. That string is inert text: the
source document is not in the vault, so there is nothing to click and nothing for
Claude to read.

Wiring nodes to their sources is what converts the stub from a dead end into a
signpost. Copy the sources into the vault and give every concept note a `## Source`
section linking to the full document. Skipping this produces a graph that looks
impressive and answers nothing.

## Fragmentation is the real failure mode

Not mentioned in the source, found on the first run, and it would have quietly
gutted the result.

Extraction runs as parallel subagents over disjoint file chunks. Each agent only
sees its own chunk, so it only ever writes edges *within* that chunk. The naive
merge produced **27 disconnected components, the largest holding 147 of 986 nodes**.
A graph in 27 pieces cannot answer a cross-document question, which is the entire
reason to build one.

Two fixes, in order:

1. **Merge duplicate-label nodes.** IDs are `{file_stem}_{entity}`, so the same
   concept in two files gets two IDs. Normalize labels and collapse. Took 27
   components to 18 and the giant component to 92%.
2. **Run a stitching pass.** Feed one agent the orphan components plus the main
   component's hubs and ask for bridging edges. 72 edges reached 100% connectivity.

**Always check `nx.connected_components` before shipping a graph.** A single
component near 100% is the health signal. Do not trust node and edge totals alone;
they look identical whether the graph is connected or in pieces.

## Other traps

- **Give extraction agents explicit file lists, never an index into a manifest.**
  Found on the vault run. Handing each agent "take element at index 8 (chunk 9 of
  14)" saved prompt size and cost a whole chunk: one agent resolved the phrasing to
  index 9, re-extracted its neighbour's files, and left its own 22 files unread.
  Node and edge totals looked healthy throughout. Only the per-file coverage check
  caught it. Paste the paths.
- **Docs move.** The video's `docs.claude.com` path is dead; Claude Code docs are at
  `code.claude.com/docs/llms.txt`. Look for `llms.txt` before scraping.
- **Subagent deaths are not always fatal.** Five of eight agents reported a session
  limit, but all five had already written their chunk files. Check disk before
  re-running: `.graphify_chunk_*.json` existing and parsing is the success signal.
- **`to_json` refuses to shrink a graph.** Legitimate dedupe trips its guard; pass
  `force=True`.
- **Validate agent-produced node IDs** against the real ID set before merging edges,
  and drop dangling ones.
- **Verify coverage** - every source file should produce at least one node.

## Cost

Nine agents. Roughly 1.1M subagent tokens for 170 documents. Budget for a session
limit on a corpus this size, and prefer resuming over restarting.

## Relation to the levels model

This is a concrete, low-cost path to the Level 4 knowledge-graph rung that
[[second-brain-levels]] deliberately parks. It does not change the standing call:
ai-os stays a Level 2 LLM-wiki brain, and graphify stays **on demand**. Available,
not adopted. See `references/second-brain-levels.md`.

The source's own caveat cuts against the obvious next target: for code bases, stop
at graphify and skip the Obsidian merge. That argues against pointing this at
`projects/lsatu/`.
