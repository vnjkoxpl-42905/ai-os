---
type: brainstorm
subject: Second brain architecture what it is for, and what to build
updated: 2026-07-20
aliases: []
---

# Second brain architecture: what it is for, and what to build

Date: 2026-07-20 · Method: `/grill-with-docs` interview, 13 questions · Status: architecture agreed, sequence pending final go-ahead

## The goal, in Joshua's words

An executive assistant that has full context on everything about him, functions as a second version of him, retrieves any piece of information on demand, generates new work (lesson plans, replies, decisions) by inference from everything he has done before, spots weaknesses and connections he does not see, improves over time, and is token efficient and readable to the model. Business and teaching are not separable: the homework, the interactions, and the correspondence are all the same body of material.

## What was actually found

The interview was meant to decide the fate of the generated graph vaults. It found something more useful.

### 1. The graphs have never been consulted

Four build sessions, 5,406 generated notes, zero occasions where one was opened and something came back. The value banked so far is seven findings, and all seven came out of the extraction pass (agents reading the catalog and reasoning about it), not out of anyone navigating the finished vault.

### 2. Two retrieval tests, both lost

- **Lookup.** Query "comparative passages" against `vault` (the corpus and students graph). Zero hits on the phrase. It surfaced four nodes containing "comparative", all of them about comparative *claims* in Logical Reasoning, a different concept. Plain `grep` on raw source returned five correct files instantly, including the transcripts where it was discussed.
- **Connection.** `Dakota Assignment Log.md`, pulled in full, has one edge and no content. Its entire payload is a link back to the source file.

The cause is structural, not a build defect. A concept graph keeps concepts and discards instances. "Comparative passages are hard for Lydia" is an instance, and instances are what a second brain most needs to remember.

### 3. The four vaults are staged batches, not four products

Corrected by Joshua mid-interview. They were built as batches and deliberately held unmerged while he decided whether merging would flood the working vault. The caution was correct and the blocking question was the right one. What does not survive: the node quality is too thin to assemble. Merging four batches of stubs produces one large stub graph.

### 4. Half the generated notes are off-target

| Graph | Built over | Serves "understand me"? |
|---|---|---|
| `vault` (1,968) | students, corpus, brainstorms, wiki, context, decisions | Yes |
| `vault-b2` (1,386) | the 125 distillates | Yes, second order |
| `vault-b3` (768) | skills, agents, docs | No, tooling |
| `claude-code-docs` (1,155) | vendor docs | No, Anthropic's manual |

The two most recent batches graph the assistant's own capabilities and Anthropic's documentation. Neither serves the stated goal.

### 5. The right artifact already exists and was never wired in

`graph-imports/distillates/`: 125 files, 269,935 words, compressing 1.8M words of transcript at roughly 7:1 while preserving Joshua's voice. Section headings are `## LSAT concepts` and `## Teaching moves`. Verbatim quotes throughout: the wedding cake on blocks, LeBron and Kyrie for conclusion hierarchy, the international lawyer for accepting premises, "basically true is the enemy of the LSAT".

This is the fuel for lesson generation. It is not a stub layer. It is filed inside `graph-imports/`, a folder named for a process it is not part of, and it is at risk of being treated as generated exhaust.

### 6. The vault holds almost nothing beyond transcripts (corrected 2026-07-20)

Each student folder *appears* to hold seven material types: `transcript-downloads/`, `Practice_Test_Reports/`, `Student_Specific_Homework/`, `email-correspondence.md`, `teaching-notes.md`, `assignment-log.md`, `open-loops.md`. Every folder in `distillates/` contains only `transcript-downloads/`.

**The first reading of this was wrong.** It implied six rich un-ingested sources. Measured directly:

- `Practice_Test_Reports/` and `Student_Specific_Homework/` are **empty across every student**. Scaffolded folders, no files.
- `teaching-notes.md`, `email-correspondence.md`, `open-loops.md` and `assignment-log.md` total roughly **5,400 words across all students combined**.

So there is essentially nothing left in the vault to ingest. Transcripts are distilled, `corpus/` is synthesized, and the rest is scaffolding. **The mbox is the only real source of new material**, which is what makes it the ingest target rather than one option among several.

Note the consequence: there is **no outcome data anywhere in the brain**. Nothing records whether the teaching worked. Practice test reports would have been that and were never filed.

### 7. The concept axis already exists as folders

`corpus/Curriculum/` is organized by LSAT concept: Main Conclusion (21 pages), Flaw and Famous Flaws (11), Necessary Assumption (7), Conditional Logic (7), Causation (6), and more, each with `Notes/` and `Homework/`. 118 pages, plus a 33-page question-feature index over PTs 101 to 159.

The gap is a **join**. What Joshua planned to teach lives in `corpus/Curriculum/`. What he actually taught lives in `distillates/`. Nothing connects them. The wedding cake analogy sits in Dakota's 2026-03-07 distillate; the 21 pages under `Main Conclusion` do not know it exists.

That gap is also the critique signal. Intended versus delivered, per concept, is where "places I missed" is computable.

### 8. A fully specified ingest plan was written and never executed

`brainstorms/2026-07-19-takeout-deep-ingest-emulation.md` locked ten decisions: domain wiki pages for pricing, scheduling, pedagogy, student handling and business strategy; `students/former-students/`; a ratified auto-send template set; a skill kill list. The analysis pass ran and was logged.

None of the outputs exist. `students/former-students/` was never created. None of the domain wiki pages were written. The next day, three graph batches were built instead (`wiki/log.md` lines 385, 420, 463).

The inbox is tractable: 3,318 messages, not 16GB. Most of the Takeout bulk is Drive. 944 authored emails were already mined once for `wiki/teaching-voice.md`.

## The architecture

Three distinct jobs, which had been conflated:

1. **Retrieve.** "What did I say about X." Wants a pointer. Folder structure and `grep` win.
2. **Synthesize.** "Generate a lesson plan from my previous data." Wants aggregate patterns across 1.8M words. Needs a distilled layer.
3. **Critique.** "Where did I miss something, what should be better." Wants cross-cutting connection finding. This is what the graph pipeline demonstrably does well, and it is a core organ, not a consolation prize.

Four tiers, three of which already exist:

| Tier | What | Status |
|---|---|---|
| 1 | Lean always-loaded context: `CLAUDE.md`, `context/`, native memory | Exists |
| 2 | `_playbook.md` per topic, plus curriculum arc, plus thin student briefs | **Missing. The only real gap.** |
| 3 | Session distillates, 125 files, 269k words | Exists, unwired, misfiled |
| 4 | Raw source: transcripts, mbox, homework, practice reports | Exists, mostly un-ingested |

## Glossary

- **Tier 1 / lean layer.** The always-loaded context, read every session without a decision. Must stay small enough that loading it is never weighed. Hand-curated.
- **Tier 2 / playbook.** Synthesized, regenerable. One `_playbook.md` per topic inside `corpus/Curriculum/<Topic>/`, joining curriculum notes with the teaching moves actually used. Never merged into `Notes/`, so authored material stays distinguishable from inferred material.
- **Tier 3 / distillate.** One dense prose summary per session or artifact, roughly 7:1 compression, preserving voice and verbatim quotes. The compounding record.
- **Tier 4 / raw.** Immutable source. Read only when Tier 3 is insufficient.
- **Curriculum arc.** The order concepts are actually introduced across sessions, derived from what happened rather than what was planned. Required for generating session N with correct prerequisites.
- **Fast path.** New artifact lands, it gets distilled. Cheap, local, near-automatic, hooked to `wrapup`. Keeps Tier 3 complete at all times.
- **Slow path.** Playbook and arc regenerate in batch from distillates added since the last rebuild. Expensive, deliberate, never unattended.
- **Join.** The link between intended teaching (`corpus/Curriculum/`) and delivered teaching (`distillates/`). Both the synthesis fuel and the critique signal.
- **Stub note.** A generated note whose content is a pointer to its source. The dominant failure mode of the existing graph vaults. Token hostile: pay to read the pointer, pay again for the real file.
- **Document altitude.** Node granularity where each note carries real prose and is worth landing on standalone, as against concept-fragment altitude which produces stubs.

## Proposed sequence

1. Rescue `distillates/` out of `graph-imports/` into the vault root or under `students/`.
2. Execute the 07-19 ingest plan. Mbox, homework, practice reports, email, teaching notes. Fills the join between teaching and business, plus the domain wiki pages and `students/former-students/`.
3. Build Tier 2. `_playbook.md` per topic, plus the curriculum arc, plus thin per-student briefs marked active or former.
4. Then one unified graph over the completed brain, at document altitude, browsable by Joshua and cheap for the model.
5. Keep the four existing vaults on disk. Not hidden from view, per Joshua's explicit call that he wants to see everything.

**Why ingest precedes graph.** A graph cannot create knowledge the vault does not hold. Building now produces a map with teaching richly connected to itself and business nearly absent, and the cross-domain edges Joshua most wants would have no endpoints. Joshua's own objection, that business and teaching are intertwined, is the strongest argument for this order: the connective tissue is the homework, the correspondence and the follow-ups, and none of it is ingested yet.

**Accepted cost of step 5.** The existing 5,406 notes stay in the Obsidian graph view during steps 1 to 4 and will keep the graph view noisy until the rebuild replaces them. Accepted knowingly rather than discovered later.

## Open items

- Lecture notes partially outside the vault. Some in Google Drive, some in the LSAT U app. Drive integration needed. Eight curriculum topics are scaffolded but unfilled (Weaken, Paradox, Quantifiers, Reading Comprehension and others), their sources stranded behind dead `.gdoc` pointers.
- Business material is thin in writing. `context/work.md` plus `decisions/log.md` is roughly 3,800 words against 2.1M words of LSAT material. Step 2 is what closes this.
- `graph-imports/` is not gitignored. 5,406 generated files would enter commit history. Carried across several handoffs, still unresolved.
- `graph-imports/vault-b3/INDEX.md` line 178 states the generated-to-curated ratio as 1.7:1. The true figure is roughly 13:1. The recommendation on that line survives the correction but the stated number does not.
- The ChatGPT briefing at `~/.claude/plans/so-what-are-oy-splendid-cascade.md` is superseded by this document. It was written to have ChatGPT interview Joshua on the vault question. That interview has now happened here.
