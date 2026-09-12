# graph-imports — inventory of what already exists (map before build)

Built 2026-07-20 as a stock-take before executing the second-brain build plan
(`../brainstorms/2026-07-20-vault-integration-decision.md`). Read-only snapshot.
Nothing here was modified to produce this map.

## The four graphs

| Vault | Notes | Nodes / edges | Stub-like (<60w) | Communities | Built from |
|---|---|---|---|---|---|
| `vault` (batch 1) | 1,964 | 1,942 / 2,745 | 1,070 (54%) | 25 | students, corpus, brainstorms, wiki, context, decisions |
| `vault-b2` (batch 2) | 1,386 | 1,368 / 2,848 | 851 (61%) | 17 | the 125 distillates |
| `vault-b3` (batch 3) | 768 | 750 / 1,174 | 210 (27%) | 17 | skills, agents, docs |
| `claude-code-docs` | 983 | (obsidian-only cfg) | 659 (67%) | 21 | Anthropic's Claude Code docs (vendor) |

- Four separate connected components. No edges cross between batches. Each was
  independently verified as one component at build time.
- They share a consolidation point already: collectively they wikilink to 1,152
  distinct REAL vault files. Batch 1 points into 257 corpus/student files, batch
  3 into 622 skill/corpus files, overlapping on shared corpus pages.
- Stub split corrected 2026-07-20: NOT "mostly empty." Roughly half carry real
  extracted content; vault-b3 is majority substantive. Decision (Joshua's
  override): keep all of them, pointers included, as the navigation layer.

## Communities by graph

- **`vault` (25):** Argument Structure Core · Causation and Conditional Logic ·
  Flaw Module and Bootcamp Design · Main Conclusion Bootcamp Build · LR Taxonomy
  and Curriculum Meta · Role/Parallel/Flaw Drills · Assumption and Principle
  Homework · Dakota Session Arc · David and Ethan Records · Lydia and Meghan
  Records · Sofia and Nicole Records · Bella and Adriana Records · C. Alexander
  and Booking Passes · Live Status and Smaller Rosters · Business Model and
  Onboarding · Booking Admin and Links Design · Calendly Teardown and Booking UI
  · Lovable Cloud Platform · Decisions Log and Three Ms · Wiki Ledgers and
  Automation Backlog · Second Brain Architecture · Graphify and Knowledge Graph
  Layer · Question-Feature Index and Graph Bridge · Takeout Ingest and Session
  Mining · Agentic OS Power Phrases.
- **`vault-b2` (17):** The Four-Step Argument Framework · Argument Structure and
  De-Abstraction · Main Conclusion and Argument Signals · Assumptions and the
  New-Concept Rule · Scope and Granted Premises · Causal and Conditional Attacks
  · Conditional Logic Core · Flaw Types and Parallel Reasoning · Role, Assumptions
  and Review Habits · Answer-Choice Strength Language · Prephrasing and Answer
  Calibration · Validity and Certainty Language · CEER and RC Discipline ·
  Reading Comprehension Method · Reading Strategy and Study Method · Process Over
  Intuition and the Clock · Score Plateaus and Practice-Test Doctrine.
- **`vault-b3` (17):** Skill Authoring and Progressive Disclosure · Skill Catalog,
  Docs and Plan Artifacts · Skill Quality Engineering · Command Authoring and
  Completion Discipline · Plan Review, MCP Building and Cross-Runtime Parity ·
  Claude-Codex Handoff and Cross-Model Build · Interview-Driven Discovery and
  Evaluation · Adversarial Verification and Variant Generation · Debugging
  Discipline and Mutation Gates · Platform Automation and Codebase Practice ·
  LSAT Bootcamp Build and Gated Execution · EA Operations and Safe Outbound
  Actions · Tool-Layer Security and Least Privilege · Hooks, Bundling and
  Untrusted Input · Frontend Design Craft (impeccable) · Design Taste and
  Anti-Generic Aesthetics · Browser Verification and Design Tokens.
- **`claude-code-docs` (21):** vendor doc structure (Agent Loop, Hooks and Memory
  Files, MCP and Channels, Permissions and Trust Boundaries, Subagents and Agent
  Teams, Workflows and Worktree Isolation, SDK Skills, etc.). Anthropic's
  material, not Joshua's.

## Distillates — the rich Tier-3 asset (125 files, ~270k words, ~2,000 words median)

Per-student session distillates. Coverage:

| Files | Student |
|---|---|
| 51 | `_other-sessions` (mixed historical) |
| 17 | meghan |
| 11 | david-salgado |
| 10 | dakota |
| 8 | lydia |
| 7 | adriana-varea |
| 6 | ethan |
| 4 | sofia |
| 2 each | yahunatan-zetvy, thaniuska-vivas, c-alexander, bella-lorenzo |
| 1 each | nicole, lexi, favour |

Transcripts only. No homework, practice-report, or email distillates exist (those
source folders are empty vault-wide).

## Pipeline (the machine — keep and repurpose)

- `vault-run/` (b1), `vault-run-b2/`, `vault-run-b3/` — each holds the build
  scripts. b3 is the most complete: `merge.py`, `apply_stitch.py`,
  `apply_corrections.py` + `corrections.json`, `wire_sources.py`,
  `fix_vault_names.py`, `verify.py`, plus `graphify-out/`.
- `graphify-out/` (top level) — `GRAPH_REPORT.md`, `graph.html`, `graph.json`,
  `manifest.json`, `cost.json`, `cache/`.
- `verify.py` is the trust-nothing checker: recomputes every count from disk.
- Ship gate is `components: 1`.

## What this means for the build plan

- **Phase 3 (unify the graph)** is a MERGE of four existing components plus a
  fresh graphify pass, not a from-scratch build. The 1,152 shared real-file
  targets are the natural seams to stitch on.
- **Phase 2 (playbooks)** already has both inputs on disk: `corpus/Curriculum/`
  (planned) and `distillates/` (delivered).
- **`claude-code-docs`** is the one graph that is vendor material, not Joshua's.
  Flag for a keep/scope decision at unify time (it may belong in the graph as
  capability reference, or may be excluded as not-his-brain).
- Nothing is dropped (Joshua's override). Unification + index + lenses is how
  usability is achieved, not pruning.
