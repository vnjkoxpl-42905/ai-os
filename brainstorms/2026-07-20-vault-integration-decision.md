---
type: brainstorm
subject: Vault Integration Decision Brainstorm / Discovery Notes
updated: 2026-07-21
aliases: []
---

# Vault Integration Decision: Brainstorm / Discovery Notes

Date: 2026-07-20 · Goal: Decide how the four graph vaults and the distillates become one second brain, and what "integrated" actually has to mean to deliver what Joshua wants.

## Context going in

- Architecture settled earlier today in `2026-07-20-second-brain-architecture.md`: four-tier distillation layer, Tier 2 playbooks per curriculum topic, one unified graph after ingest, three jobs (retrieve, synthesize, critique).
- Joshua's stated goal, restated three times: an executive assistant with complete context on him, able to retrieve anything, generate work by inference from everything he has done, spot connections and weaknesses he does not see, improve over time, be browsable by him, and be token efficient.
- Joshua's correction: the four vaults were never four intended products. They are staged batches held unmerged pending his call on whether merging would flood the working vault.
- `2026-07-20-mbox-ingest-design.md` is parked pending this decision.

## Resolved by inspection (no interview needed)

Measured 2026-07-20:

- **`~/ai-os` IS the Obsidian vault.** `.obsidian/` sits at the root, so `graph-imports/` is already inside it. Nothing needs moving to be visible.
- **Graph notes already link into real notes, and the links resolve.** 1,963 of 1,968 batch-1 notes carry a `## Source` wikilink. Spot check: `Dakota Assignment Log.md` links `[[students/dakota/assignment-log]]`, and `students/dakota/assignment-log.md` exists.
- **Reverse direction is free.** Zero real notes link out into `graph-imports/`, but Obsidian generates backlinks automatically, so opening a real note already surfaces the graph notes pointing at it.
- **Conclusion: the vaults are not segregated.** They are in the vault, in the graph view, in search, and linked bidirectionally in effect. Whatever the problem is, it is not integration.

The remaining candidate problems are therefore **quality** (stub notes with no content) and **volume** (5,406 generated against 419 curated), not connection.

## Summary / key decisions

(running synthesis, updated as we go)

## Q&A log

### Q1 — what does "one vault" have to mean, given integration already works?
- Asked: Offered three candidate problems. (A) volume, 5,406 generated against 419 curated. (B) quality, most generated notes are stubs. (C) coverage, business and decisions are not in the vault at all. Recommended B and C, with A as a symptom of B.
- Captured: Joshua did not pick one. He restated the goal, and the restatement carries the answer implicitly. Wants "a unified brain my personal executive assistant can use effortlessly", "a powerful AI-OS instead of disjuncted", "fully informed context", "maximally useful for all ranges of tasks whether it is handling business tasks through email or creating lectures or teaching using transcripts and my LSAT corpus", "growing stronger and stronger through time", able to "find places for me to improve or places where links could be made", to "emulate me in every way or improve me in ways I don't see", and it "should be visually easy to work through".
- Read: this confirms **B and C together**, plus visual usability as a hard requirement. "Visually easy to work through" is incompatible with a 5,406-node stub hairball, and "handling business tasks through email" is C stated outright.
- Flags: he has now declined three times to sequence the work (question 13 in the architecture interview, and twice here). Treat sequencing as something to be derived and proposed, not asked again.

### Q2 — one artifact or two?
- Asked: The brain currently exists as two parallel structures describing the same material: real authored notes, and 5,406 generated graph notes that mostly shadow them. That duplication IS the disjunction. (A) keep two layers, real notes plus a generated graph layer. (B) one layer, the real notes ARE the graph, linked directly by wikilinks, no shadow notes; the pipeline produces links and findings, not notes.
- Captured: **B. LOCKED.** One layer. The graph pipeline stops emitting note files and instead writes wikilinks into existing notes plus a findings report. Intermediate concept nodes are scaffolding, discarded after extraction.
- Consequence accepted implicitly: loses concept-level nodes as their own dots in the graph view (e.g. "Symmetry Breaker"). That content lives as headings inside curriculum pages and `_playbook.md`, not as graph nodes. Joshua chose B without contesting this, so the trade is accepted.
- This is the core decision. It means: the four existing vaults are not the product and will be superseded, not merged. The real vault becomes the graph.

### Q3 — what happens to the 5,406 existing notes and the pipeline?
- Asked: archive / delete / keep the note files; keep the pipeline separately.
- Captured: **Joshua reframed the purpose.** The 5,406 notes are not meant as a browsing surface. They are meant as a **retrieval/routing layer for his AI agents** — a map that directs an agent to where information lives when it needs to search and retrieve for a task. "wiki directing and informing them where to find things." This is why he wants them kept.
- Read: this is a real and correct need (a retrieval index / map), and it matches what the architecture doc already called the "hub layer" and what the `_COMMUNITY_` notes were reaching for. But it does NOT require 5,406 stub notes. A retrieval map is a SMALL curated set of hub/index notes, not one shadow per concept. The open question is the SHAPE of the retrieval layer, not whether to have one.
- Evidence already on record: the 5,406 stubs FAILED as a retrieval aid. Querying "comparative passages" against the batch-1 graph returned zero correct hits; grep on the real files returned five. So the current note pile does not actually serve the retrieval purpose Joshua wants it for.
- Reconciliation with B (locked): decision B does not remove retrieval aids. It says the retrieval aid should be a MAP (wiki hubs + a manifest/index with one-line summaries), built over the real notes, not 5,406 shadow notes. This is compatible with what Joshua is describing.

### Q4 — what shape should the retrieval layer be?
- Asked: (A) wikilinks inside real notes for routing, plus (B) a top-level auto-generated index, one line per note with a one-sentence summary.
- Captured: **A + B, LOCKED.** A must be done well. B is definitely needed ("we definitely need a top level index"). The top-level index is the "wiki directing them where to find things" made concrete: agent reads one manifest first, jumps to the right note, avoids blind search.

### Q5 — what else enhances the brain for token efficiency and intelligence?
- Asked: recommended a bundle. 1) consistent frontmatter schema, 2) aliases on notes (fixes the comparative-passages miss), 3) summary line atop long notes, 4) distillate-first read rule. Skip 5 (split long notes) and 6 (tag cleanup).
- Captured: **1-4 confirmed good.** Open to more ideas. Plus a major reframe of what the brain optimizes for.
- **Reframe (important):** specific students like Dakota are NOT the focus. Per-student lookup is wanted but secondary. The PRIMARY value is the aggregate data across ALL students, including the many he no longer teaches, used as fuel to "enhance everything." "a lot of students were students I don't teach anymore but I want to use the data to my benefit to enhance everything." This confirms the earlier architecture decision: Tier 2 is de-personalized, organized by concept and arc. Former students' transcripts are training data for the playbooks, not lookup targets.
- **Added requirement: task-type routing.** "it should have a unified brain that serves different tasks depending on what I need." The brain must pull the right slice by task type: business email vs creating lectures vs teaching a live student. Live/active students must be distinguishable from former (data-only) ones so the brain knows which to "pick up depending on type of task."
- **Added requirement: up to date.** The brain must stay current; freshness matters.

### Q6 — three more enhancements matching the reframe: task lenses, aggregate/critique notes, freshness?
- Asked: 7) task lenses (entry-point note per task type), 8) active/former partition enforced in frontmatter, 9) freshness/staleness report.
- Captured: not yet explicitly confirmed; superseded by Q7 collage which validates and extends. Treat 7/8/9 as recommended-and-standing unless contradicted.

### Q7 — the PKM design-brief collage
- Asked: nothing; Joshua pasted a set of second-brain / PKM principles describing the qualities he wants.
- Captured: used as a design checklist. Mapping to locked decisions:
  - "[[Note Title]] interconnected web / personal graph view / surface old ideas / networks of knowledge" -> decision B (real notes ARE the graph). COVERED.
  - "a google for my brain / stores and surfaces info when you need it / retrieves only relevant context" -> top-level index + task lenses + progressive disclosure. COVERED.
  - "find connections you didn't know existed / think better" -> pipeline writes findings + wikilinks (job 3, critique). COVERED.
  - "the format the AI reads matters more than most realize / second brain is also the AI's knowledge base" -> the whole token-efficiency bundle (frontmatter, summaries, distillate-first). COVERED, and validates 1-4.
  - "navigate effortlessly / visually easy" -> ~500 dense real notes instead of 5,406 stubs. COVERED.
  - "remembers across chats / Claude and Codex read relevant memory and project files at start of each session" -> lean Tier 1 always-loaded + pickup + dual-runtime. COVERED (AGENTS.md mirror already exists).
  - "Create one source of truth" -> decision B, one note per subject, no shadow layer. COVERED. This IS decision B restated.
- **NET-NEW requirement 1 — frictionless capture.** "Captures everything without friction, so nothing important is lost." The ingest/capture path must be effortless or it won't happen (the 07-19 plan proved this: friction = not done). Reinforces the fast-path-on-wrapup design and argues for an even lower-friction inbox drop.
- **NET-NEW requirement 2 — improve after every task.** "Each completed session updates project status, lessons learned, and next actions, making future work faster." A self-improvement feedback loop: every session writes back lessons + next actions, so the brain compounds. This is the concrete form of "grows stronger over time" and "improve me in ways I don't see." Becomes part of wrapup: distillate feeds the playbook, and a lessons/next-actions delta is recorded.

### Q8 — design is complete; move to sequencing?
- Asked: completeness backstop + full design read-back.
- Captured: Joshua responded with an apparent contradiction that must be resolved before sequencing. He said: use graphify to incorporate ALL the ~5,000 knowledge-graph files into the vault, lose nothing, "perfectly executed RAG system that is my second brain," "use all those knowledge graphs and we have one unified second brain."
- **Tension 1 — 5,000 files.** This seems to reopen decision B (which drops the shadow notes). Two readings: (a) literally keep the 5,000 stub files; (b) lose none of the KNOWLEDGE/CONNECTIONS in them — regenerate one unified graph over the real vault via graphify so every connection is absorbed into real notes, and the stub files become unnecessary because their content was always in the real files. Reading (b) is consistent with B and with "one unified second brain"; reading (a) is not.
- **Tension 2 — "RAG system."** Architecture doc decided AGAINST embeddings in favor of tiered distillation. Joshua keeps saying "RAG." Likely means "a retrieval system that feeds the AI the right knowledge" (= index + wikilinks + distillate-first + lenses), not literally a vector DB. Needs a one-line confirm.
- Resolution proposed to Joshua: reading (b). Re-run graphify over the UNIFIED real vault (existing real notes + ingested business material) to produce ONE graph whose nodes are the real notes and whose edges + index are freshly regenerated. Old stub batches archived, not deleted. Nothing lost because knowledge lived in the real files all along; the connections are rebuilt better over the complete corpus.

### Q9 — confirm the reconciliation (absorb, not retain; retrieval-system not literal-vector-DB)
- Asked: proposed dropping the pure-stub pointers, folding in content notes, keeping distillates.
- Captured: **OVERRIDE by Joshua. Nothing is dropped.** "the pointers are good, I want the pointers there so it can navigate much easier, they are all needed, use it all." Decision: KEEP everything — pointer stubs, content notes, distillates. The pointers are wanted as a navigation/connective layer in the graph view.
- **This overrides the "drop shadow notes" part of decision B (Q2).** What survives from B: the real notes must ALSO be first-class, cross-linked nodes, and the four fragments must become ONE unified graph. What is reversed: the generated layer is NOT discarded; it stays as the navigation + retrieval scaffold.
- Honest cost, stated and accepted by choice: keeping ~5,000+ generated notes means a dense graph view. Usability is then achieved NOT by deletion but by: (1) unifying the four fragments into one connected graph, (2) the top-level index, (3) task lenses, (4) Obsidian's local-graph, filters, and color groups for focus. Folder boundaries remain so the real notes stay findable.
- "RAG system" reading: a retrieval system that reliably feeds the AI the right knowledge (index + links + distillate-first + lenses). Not confirmed as a literal vector DB; treat as retrieval-system unless Joshua asks for embeddings.

### REVISED MODEL (supersedes Q2's "one layer / drop shadows")
- One UNIFIED knowledge graph over everything: real notes + generated concept/pointer notes + distillates, all cross-linked, built/refreshed by graphify.
- Real notes get enriched with wikilinks so they are full participants, not just link targets.
- Business half added via mbox ingest so the graph covers business + teaching.
- Retrieval layer on top: top-level index, task lenses, consistent frontmatter, aliases, summaries, distillate-first, freshness report, feedback loop on wrapup.
- Nothing deleted. Four fragments unified into one. Navigation solved by structure + tooling, not pruning.

### Q10 — is the revised model right; ready for the build plan?
- Asked: presented sequenced build plan (Phase 0-5).
- Captured: Joshua cut the mbox/inbox/Takeout ingest entirely. "don't worry about phase 2, we don't have to touch the inbox yet, takeout for now leave that out of the plan, we are not worrying about the inbox." Phase 2 (business-half ingest) is DEFERRED, removed from the current plan. Consequence accepted: the brain stays teaching-focused for now; business-half coverage is a later phase. `2026-07-20-mbox-ingest-design.md` is parked, not dead.

## REVISED BUILD PLAN (inbox/mbox/takeout removed)

- **Phase 0 — Frontmatter foundations.** Consistent schema across all real notes (`type`, `subject`, `status: active|former`, `updated`, `aliases`). Aliases fix the comparative-passages retrieval miss.
- **Phase 1 — Top-level index + task lenses.** One generated manifest (one line + summary per note) plus lens entry-points (write-a-lecture, teach-a-live-student, etc., minus business-email until the ingest happens). The "wiki that directs the agent."
- **Phase 2 — Tier 2 playbooks.** `_playbook.md` per curriculum topic joining planned teaching (`corpus/Curriculum/`) with delivered teaching (distillates), plus curriculum arc. The lecture-generation engine.
- **Phase 3 — Unify the graph.** Re-run graphify over the enriched vault; merge the four fragments into one connected component; cross-link real notes as first-class nodes. Keep every existing note (Joshua's override: nothing dropped).
- **Phase 4 — Compounding loop.** Distillate-first read rule, freshness report, wrapup feedback loop (lessons + next actions written back each session).
- **Deferred (not in current plan):** mbox/inbox/Takeout ingest, `students/former-students/` population, domain wiki decision-extraction, business-email lens.

## Open flags (pending input)

- Sequence question 13 from the architecture interview (ingest before graph) never explicitly answered.
- Moving `graph-imports/distillates/` out to the vault root still needs an explicit yes.
- 07-19 ingest plan: do its ten decisions still stand? Asked, not yet answered.
