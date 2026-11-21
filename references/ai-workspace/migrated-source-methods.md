---
type: reference
subject: Practical review recipes recovered from the older vault
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [ai-workspace, review, provenance]
sources:
  - "../../raw/sources/old-obsidian-vault-2026-10-07/Clippings/This Open Source Repo Solve Claude's 1 Problem 1.md"
  - "../../raw/sources/old-obsidian-vault-2026-10-07/PLAN-REVIEW-LOG.md"
  - "../../raw/sources/old-obsidian-vault-2026-10-07/No file.md"
  - "../../raw/sources/old-obsidian-vault-2026-10-07/AGENTS.md"
  - "../../raw/sources/old-obsidian-vault-2026-10-07/CLAUDE.md"
  - "../../raw/sources/old-obsidian-vault-2026-10-07/GEMINI.md"
  - "../../raw/sources/old-obsidian-vault-2026-10-07/CONTEXT.md"
---

# Use independent inspection and evidence to improve the workspace

This page compiles practical details that were previously available only in the old-vault research review. It supplements the existing [Claude and Codex workflow](../claude-plus-codex.md), [Three Ms methods](../3ms-framework.md), and [context diagnostics](../second-brain-levels.md). It does not replace active skills, alter their review limits, install a repository, or adopt a historical model/version claim.

## Inspect the artifact with a fresh reviewer

The historical [Claudex demonstration](<../../raw/sources/old-obsidian-vault-2026-10-07/Clippings/This Open Source Repo Solve Claude's 1 Problem 1.md>) distinguishes review of a proposed plan from review of the resulting build. After implementation, give an independent reviewer the requirements, actual changed files, and necessary context. Have it inspect what exists rather than approve the builder's account of what exists. A fresh session reduces dependence on the planning discussion, but does not guarantee correctness.

Classify each finding as accepted, rejected with evidence, or unresolved. An independent review is not automatically right. Preserve concrete reproduction steps, requirement references, and the reason for rejecting a finding. Verify the final mixed artifact after fixes rather than assuming that an earlier review still applies.

If a bounded review loop ends without agreement, report the unresolved findings and their implications. Preserve the plan and review record. Do not present exhaustion of the round limit as approval. Continue only within the actual skill's configured behavior and authorized scope; the video's five-plan-round and two-build-round example is historical, not this workspace's current configuration.

## Test a skill's activation separately from its execution

The historical Fable clips inform [the existing skill-review method](../3ms-framework.md). For representative real requests, record whether the correct skill activates, whether an unrelated skill activates, and whether the selected skill produces the intended artifact. A good instruction body cannot compensate for a trigger that misses the task; a good trigger cannot compensate for defective execution.

Use keep, merge, rewrite, or retire as review recommendations. Search existing skills before proposing another. Repeated friction can belong to an existing skill, a deterministic automation, a direct fix, or no action. Current activation, parity, permissions, and deletion rules govern any resulting change.

## Evaluate effort and prompting on actual work

The old secondhand Anthropic analysis is compiled in [Three Ms](../3ms-framework.md). State outcome, purpose, constraints, and completion evidence. Compare effort settings on representative tasks using artifact correctness, retrieval freshness, unnecessary steps, and correction cost. Lower effort is useful only when the actual task still succeeds. Do not substitute a speaker's benchmark or billing claims for local evidence.

For a claimed completed action, find the corresponding tool result or artifact. For visual work, inspect the rendered output. For a fact that changes over time, retrieve appropriate current evidence. Source recommendations about delegation remain subordinate to this task's applicable delegation rules.

## Check examples and attribution before adopting a lesson

The old [conditional review and triage](../../raw/sources/old-obsidian-vault-2026-10-07/PLAN-REVIEW-LOG.md) records concrete review failures worth retaining across domains:

- A restatement can look like independent support. In the teaching example, a rule and its contrapositive are equivalent; together they do not establish a biconditional.
- An example must not add an unstated term. The historical example silently changed “weather” to “good weather.” Check the translated proposition against the exact original.
- A source attribution needs actual supporting evidence. The reviewer claimed a transcript taught “the only” as an indicator, and the triage rejected that attribution after checking occurrences. A potentially valid idea does not make its claimed source true.
- Check tables against surrounding prose. A heading asserting that terms are absent from all lists conflicted with terms actually present in the tables.

These are evidence and quality checks, not adoption of the old product plan, all its proposed edits, or an obsolete curriculum state. Current teaching standards retain authority.

## Preserve the teaching-annotation idea without inventing its design

The old [annotation scratch note](../../raw/sources/old-obsidian-vault-2026-10-07/No%20file.md) records a useful product idea: the teaching side should support annotation. Keep this as a captured idea for a future teaching-interface investigation. Its supporting screenshot is absent, so annotation targets, controls, persistence and intended interaction cannot be recovered from this note. This is neither a verified missing feature nor an approved implementation specification. Compare it with the actual current teaching interface before proposing work.

## Reuse workflow patterns without pretending their old implementations exist

The older [Codex router](../../raw/sources/old-obsidian-vault-2026-10-07/AGENTS.md) and [Claude router](../../raw/sources/old-obsidian-vault-2026-10-07/CLAUDE.md) describe a richer Mac workspace than the files actually present in the old laptop vault. Full local inspection found only `.obsidian/` and `Clippings/` with its Loophole subfolders. Their mentioned skill definitions, wiki, lectures, task-board scripts and dispatch implementation are absent from that old source root. The following are captured reusable design patterns and possible improvements, not installed workflows or approved structural changes.

| Pattern from the old instructions | Useful method and boundary |
|---|---|
| Distillate-first retrieval | Start with a verified session summary or concept map; escalate to its full transcript when insufficient. Current [student session packages](../../students/README.md) provide existing homes. A separate `distillates/` tree is not required or created. |
| Shared concept notes versus session recap | Separate a reusable topic explanation from a person's session-specific learning record. Link the shared concept rather than duplicate its entire lesson in each record. Old `concept-note` and `session-recap` definitions were not available to migrate. |
| Task extraction versus project wrapup | An action should identify owner, student, due date when evidenced, and source. Record a processing receipt even when no tasks were found to avoid repeated extraction. A global generated rollup and numbered correction ledger are potential improvements, not files currently present. |
| Correction ledgers by writing task | Convert a real correction into a durable rule; keep email wording concerns distinct from lesson pedagogy when that distinction helps. Follow current teaching-voice standards; do not import older vendor voice constraints as new policy. |
| Link/template/drafting registry | One verified action link and an explicit draft route can reduce repeat errors. Old JSON schemas and command implementations are absent; do not claim the `link`, `template`, `draft-for`, or `vault-draft` commands work here. |
| Declared attachable assets | A reusable GIF or attachment record can state what it shows, intended recipient/stage, and delivery compatibility. Avoid sending onboarding assets to unpaid prospects merely because an old asset exists. Old library files are absent; no new attachment policy or library installed. |
| Reusable drill library | A useful drill record can retain purpose, exact questions, source IDs, accommodation requirements, sharing link, and companion explanation. Old 7Sage template counts and numbering equivalence are historical claims to verify before reuse. No new folder or external set created. |
| Passage and lecture navigation | Match source passages by identity/title rather than assume a constant numbering offset. Pair script beats and boards with their actual timestamps/source states; preserve source-defined lesson level rather than infer it. Old passage counts and missing lecture scripts are not recoverable source content. |
| Post-meeting dispatch | Separate pre-session preparation, post-session evidence intake, action extraction and follow-up drafts. Calendar events are triggers, not proof of attendance. The Mac scheduled task is absent; no new schedule created. |
| Source dependencies before tidying | Trace build inputs, output paths and incoming links before merging graph or prospect folders. A folder that looks redundant can be a dependency. Old graph build scripts are absent, so their claimed Windows necessity is unverified. |
| Baseline, delta and current profile | Old [business glossary](../../raw/sources/old-obsidian-vault-2026-10-07/CONTEXT.md) distinguishes one complete 7Sage history capture, later incremental changes, and a rolling current profile. Useful schema idea; old onboarding/update skill definitions and canonical frontmatter implementation are absent. No current student schema rewritten. |
| Historical commitments stay visible | The old [Gemini incident](../../raw/sources/old-obsidian-vault-2026-10-07/GEMINI.md) shows why a new session must not erase an unresolved older commitment. Use the current primary-record preservation rules; resolve with evidence and a dated closure/correction instead of silently dropping history. |

The historical [conditional cheat-sheet plan](../../raw/sources/old-obsidian-vault-2026-10-07/PLAN.md) adds a product-design distinction: a reference used mid-drill should expose recognizable lookup terms and essential rules quickly; a lesson can teach in sequence and include practice. Check both artifacts for consistency without making a lookup reference repeat an entire lesson. Old proposed accordion restructures, example edits, inline-style constraints and classroom state remain unapproved historical implementation choices. Validate the actual renderer and narrow-width behavior before making a future design change.

The old Claude graph section warns of an exporter potentially overwriting wiki files. Treat that as historical hazard evidence, not verified behavior of current software: inspect the selected command's actual write destinations and use an isolated output location before any future authorized graph trial. Do not point an unverified generator at maintained primary knowledge merely because its name suggests it produces a wiki.

## Verify that a wrapper really loads its dependencies

The old routers record an interview failure in which a named wrapper was not available and the model improvised another workflow. They also describe a second failure: a wrapper naming `grilling` and `domain-modeling` did not reliably cause those skills to load. Preserve the general check: inspect actual activation and load the applicable dependency instructions before claiming the workflow ran. Do not substitute a vaguely similar skill without explaining the difference.

The current project has `grill-with-docs`, `grilling` and `domain-modeling` files, and the inspected Codex wrapper has `disable-model-invocation: true`. The old 2026-09-01 overlay instruction is superseded by the 2026-09-26 entry in [runtime parity](../../skills/PARITY.md), which deliberately restores the ordinary wrapper to upstream. Current document-backed [cross-provider grilling](../../.agents/skills/grill-with-docs-claude/SKILL.md) delegates to Claudex and explicitly says not to restore the upstream legacy implementation. Preserve the dependency-verification lesson, but do not reinstall the old overlay or declare the ordinary wrapper defective merely because it differs from the old router. Current [skill model](../../AGENTS.md) and the actual selected skill govern execution.

See the [AI Workspace hub](index.md), [active migration coverage](../../research/obsidian-vault-comparison/2026-10-07/active-migration-coverage.md), and [source review](../../research/obsidian-vault-comparison/2026-10-07/research-review.md) for related knowledge and exclusions.
