---
type: reference
subject: The 5 levels of a Claude second brain where ai-os stands
updated: 2026-10-08
aliases: []
---

# The 5 levels of a Claude second brain — where ai-os stands

Comparative analysis of ai-os against Nate/Herk's "Every Level of a Claude Second Brain Explained" and the Karpathy LLM-wiki video (both in the NotebookLM `SETUp` notebook). Written 2026-07-18.

## The model

Each level answers a harder retrieval question. **Higher is not better.** The doctrine: find the *lowest* level that removes an actual pain, and do not build past it. A project is not one level — each folder can sit at a different one.

| Lvl | Question | Mechanism |
|---|---|---|
| 1 | Find by exact word/file | CLAUDE.md as router + `context/` `projects/` `decisions/` |
| 2 | Pull everything on a topic together | LLM wiki — index + log + backlinks + hot cache + automemory + references |
| 3 | I searched different words than I wrote (meaning) | Semantic search / vector DB, per-folder where it fits |
| 4 | Trace a chain: topic X back to topic A | Knowledge graph — typed relationships (LightRAG, graphify) |
| 5 | Never think about it | Always-on autonomous OS (GBrain, crons, constant sync) |

Two doctrines that outrank the levels:
- **Context vs Connections.** Ingest *evergreen* data (locked decisions, quarterly priorities). Do NOT ingest *volatile* data (email, Slack, CRM, payments) — give the brain routing to grab it live instead. Otherwise you spend every month deleting noise.
- **Reverse-engineer from the question.** How you will recall it dictates how you file it.

The source's own author parks his primary EA brain ("Herk 2") at **Level 2**. He does not run Level 4 or 5 day-to-day. That is the benchmark.

## Architecture evidence and the historical level comparison

The original level comparison was written 2026-07-18. The table below was qualified on 2026-10-08 using the current root routing map and documented sync setup. A documented capability or prior successful upload does not establish continuous availability, device installation, or cloud authentication.

| Level | Status | Evidence |
|---|---|---|
| 1 | Complete, exceeds reference | CLAUDE.md router with explicit routing-map table; `context/{about-me,work,priorities}`, `decisions/log.md`, `projects/`. |
| 2 | Current documented operating pattern | `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`, native automemory, `references/`, and domain homes in `corpus/` and `students/`. These routes do not certify that every page is complete or current. |
| 3 | Not part of the documented retrieval order | Root instructions use indexes, domain pages and live-system escalation. Add semantic retrieval only for an observed retrieval failure; file counts alone do not justify it. |
| 4 | On-demand graph research | Graphify is cataloged and generated graph imports exist. Their existence does not prove freshness, a continuously maintained graph, or improved retrieval. Graph work was deferred in the old-vault intake. |
| 5 | Scheduled snapshot sync is documented; an autonomous OS is not established | [Sync setup](../setup/github-sync/README.md) describes two-minute GitHub/Drive checks while signed in. The intake's local verification receipt records a matching GitHub/Drive snapshot at `2026-10-08T04:20:38.800373+00:00`, commit `9378793aafed94b946845b205a35cdf39fc46a9e`. This is a past verification, not a claim that later edits are uploaded or that a sleeping/offline laptop keeps syncing. |

**Headline:** ai-os's Context/Connections separation is *more* formalized than the source's — Nate keeps the split in his head; ai-os has it written as `connections.md` (7 data domains, backend wins on conflict) + the "don't read the wiki unless the task needs it" rule + the Four Cs in `references/3ms-framework.md`. The video references the Four Cs as Nate's own framework; ai-os has already absorbed it.

## Recommendation

### Keep one connected brain with separate domain homes

Recommendation recorded 2026-10-07 after the old-vault intake review. Keep `ai-os` as one working Obsidian vault, with the [wiki](../wiki/index.md), [teaching corpus](../corpus/index.md) and [student records](../students/README.md) as distinct knowledge domains. This preserves the existing architecture; it does not authorize a folder move, vault split or Sync change.

The useful unit is a connected reasoning chain. A student's session evidence supports a dated teaching judgment in their record. That judgment links to a reusable concept or method in the corpus. Its student-facing explanation uses [Joshua's selected teaching voice](lsat-teaching-voice-standard.md). Product or pedagogy choices link to the [decision log](../decisions/log.md), while sources remain evidence with provenance. [Business context](../context/work.md) and [Joshua's identity](../context/about-me.md) explain the purpose and preferences behind the work. Keeping those links in one vault makes the whole chain available without copying each shared lesson into every student folder.

Separate vaults would require additional cross-vault retrieval and synchronization conventions. They would be justified by a real access, collaboration or workflow boundary, not merely by teaching and student notes being different subjects. No such new boundary was established in this task.

This can preserve Joshua's expressed judgments, demonstrated wording, source evidence and decision reasons. It is not a complete replica of his mind or permission to turn a vendor method into his personal preference. Keep observed, inferred, recommended and decided distinct. The [old-vault source summary](../wiki/sources/old-obsidian-vault-2026-10-07.md) illustrates those boundaries.

### Diagnose a context failure before adding another retrieval layer

The recovered “Steal My Exact AI OS Setup” clip offers four useful failure labels: a wrong fact entering context, too much irrelevant context, missing or misrouted context, and contradictory source generations. These categories overlap; use them to locate evidence, not as a new score or replacement for the current audit rubric. [Recovered-source review](../research/obsidian-vault-comparison/2026-10-07/research-review.md); [provenance](../wiki/sources/old-obsidian-vault-2026-10-07.md).

For a failed lookup, record the requested fact, the route actually taken, the correct source, and the narrow routing change that would have prevented it. This makes “look before asking” actionable without assuming semantic search or a new plugin is the answer. The clip's architecture overlaps the existing router and live-system authority; no old runtime rule was activated.

Investigate a new retrieval layer when actual queries miss relevant evidence despite correct routes. Measure the failure in the affected domain, such as teaching sources or student transcripts, before choosing a tool. Continue maintaining indexes, provenance and explicit authority boundaries; the older page-count and empty-folder observations are not current inventory evidence.

Related: [[3ms-framework]], the LLM-wiki schema in CLAUDE.md.
