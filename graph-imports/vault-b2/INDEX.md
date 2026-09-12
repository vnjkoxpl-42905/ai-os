# ai-os knowledge graph — batch 2 (the teaching corpus)

A concept map of what actually gets taught in sessions. Nodes are **concepts, not
sessions**: 125 distilled session notes became 1,368 concepts joined by 2,848 edges,
in one connected component. Every concept links back through its distillate to the
untouched raw Gemini transcript, so any claim here is checkable against the evidence.

Built 2026-07-20. Method and traps: `references/graphify-obsidian-bridge.md`.

## What is in scope

The 125 distillates in `graph-imports/distillates/`, covering 143 tutoring sessions
with 34 distinct people (students, prospects, and consultations that never
converted). Source transcripts live under `students/<name>/transcript-downloads/`
and `students/_other-sessions/`.

**Not** in this batch: `projects/lsatu/` and `skills/`. Those were originally
labelled "batch 2" in the batch-1 index; they are now **batch 3**. The distillates
jumped the queue because they are the highest insight-density material in the vault
and batch 1's index itself flags lsatu/skills as high-node-count, low-insight.

## Two-hop provenance

Every concept note's `## Source` section gives both hops:

    concept note  ->  graph-imports/distillates/<path>  ->  students/<path>

The distillate is what was extracted from. The raw transcript is the untouched
evidence. Both are there because the distillate is a lossy summary, and any claim
worth challenging has to be checkable against what was actually said. 125/125
distillates resolved to a live raw transcript.

## How to use it

- **`graph.canvas`** — structured layout, communities as groups. Best first look.
- **Graph view** — one connected mass. Islands would mean a rebuild regressed.
- **`_COMMUNITY_*` notes** — 17 overviews with cohesion scores and dataview queries.
- **A person's note** — every concept ever taught to them, in one place. This is the
  batch-2 feature batch 1 did not have: `[[Meghan Mullins]]` is a teaching history.
- **Any concept note** — `## Connections` gives the neighbours, `## Source` opens
  both the distillate and the raw transcript.
- **`../vault-run-b2/graphify-out/GRAPH_REPORT.md`** — god nodes, surprising
  connections, suggested questions.
- **`../vault-run-b2/graphify-out/graph.html`** — interactive, no server needed.

## Communities

| Community | Nodes | Cohesion |
|---|---:|---:|
| Causal and Conditional Attacks | 193 | 0.02 |
| Reading Comprehension Method | 176 | 0.02 |
| Main Conclusion and Argument Signals | 171 | 0.02 |
| Flaw Types and Parallel Reasoning | 169 | 0.02 |
| Prephrasing and Answer Calibration | 116 | 0.03 |
| Assumptions and the New-Concept Rule | 113 | 0.02 |
| CEER and RC Discipline | 95 | 0.03 |
| Role, Assumptions and Review Habits | 67 | 0.05 |
| Argument Structure and De-Abstraction | 64 | 0.04 |
| Conditional Logic Core | 59 | 0.05 |
| Reading Strategy and Study Method | 51 | 0.06 |
| Validity and Certainty Language | 42 | 0.06 |
| Score Plateaus and Practice-Test Doctrine | 18 | 0.14 |
| The Four-Step Argument Framework | 13 | 0.15 |
| Answer-Choice Strength Language | 8 | 0.25 |
| Process Over Intuition and the Clock | 7 | 0.29 |
| Scope and Granted Premises | 6 | 0.33 |

## Known shape and residuals

**The Dakota skew is fixed.** Batch 1's largest community was "Dakota Session Arc"
at 174 nodes off 10 transcripts — one student's sessions dominating the graph.
Batch 2's largest community is a general LR-methods cluster at 193 nodes (14%), and
Dakota holds 9 personal-state nodes with everything else filed as shared corpus
concepts. Extraction was instructed to prefer the concept over the session.

**God nodes are all people, by construction.** Joshua (272 edges), Meghan (160),
Dakota (131), David (116), Lydia (102). Every concept carries a `references` edge to
the student it was taught to, so people accumulate degree by design. This is the
feature, not a defect — but do not read it as "these concepts are central."
For conceptual centrality, look inside a community, not at the god-node list.

**Residual near-duplicate labels.** The merge collapses labels only on exact
normalized match, so variants survive: "Two-Step Conclusion Test" vs "Two-Step Main
Conclusion Test", "The Answers Live on the Left Side" vs "The Answers Are on the
Left Side of the Screen". They are joined by `semantically_similar_to` edges rather
than merged. A fuzzy-match collapse pass would fix this; not run.

**22 stitch edges are INFERRED, not extracted.** Ten small orphan components (22
nodes) were bridged into the main component by reasoning from concept labels, not
from source text. They carry confidence 0.65–0.97 and justifications are in
`../vault-run-b2/graphify-out/.stitch.json`. Treat them as weaker than the rest.

**The 2026-05-10 David distillate has no transcript body**, only a Gemini summary.
All 12 of its edges are marked AMBIGUOUS at 0.2–0.3. Worth re-pulling from Drive.

## Rebuild

    cd graph-imports/vault-run-b2
    $(cat graphify-out/.graphify_python) merge.py         # collapse + ship gate
    $(cat graphify-out/.graphify_python) apply_stitch.py  # bridge orphans
    $(cat graphify-out/.graphify_python) wire_sources.py  # two-hop source links

The ship gate is `components: 1`. Anything else is not shippable.
