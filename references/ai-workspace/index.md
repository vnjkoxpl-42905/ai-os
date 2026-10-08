---
type: reference
subject: AI workspace learning and improvements
created: 2026-10-08
updated: 2026-10-08
aliases: [AI setup, AI learning, Claude and Codex improvements]
tags: [ai-workspace, claude, codex, llm-wiki]
sources: []
---

# Turn AI clips into useful workspace knowledge

Joshua expects a substantial share of incoming clips to cover Claude, Codex, AI tips, prompts, repositories, new skills, product updates, and possible workspace improvements. This is the navigation and filing guide for that material. It is separate from the [LSAT teaching corpus](../../corpus/index.md), while remaining part of the same second brain.

This hub organizes existing authoritative pages rather than copying their knowledge into another set of pages. The intake rules remain in the [LLM Wiki schema](../../system/schema/llm-wiki.md), and the overall catalog remains [the wiki index](../../wiki/index.md).

[Recovered practical methods](migrated-source-methods.md) add the old vault's detailed artifact-review, skill-evaluation and evidence-checking recipes, plus its unimplemented annotation idea. [Migration coverage](../../research/obsidian-vault-comparison/2026-10-07/active-migration-coverage.md) maps the original research and root files to current homes and explains exclusions.

[Karpathy source compilation](../../wiki/karpathy/index.md) begins with five reviewed sources and quoted candidate methods. It is explicitly partial. The [verified collection handoff](../../research/karpathy-brain-2026-10-08/HANDOFF-VERIFICATION.md) records missing coverage, attribution limits and corrections to the original completeness claims. No Karpathy persona or runtime hook is installed.

[Resumable X collector](x-archive-collector.md) documents the free local script, signed-in persistent Chrome route, evidence ledgers, source-preserving repairs and retrieval limits.

## Find the right kind of AI knowledge

| Category | What belongs here | Existing home to consult or update |
|---|---|---|
| Claude and Codex workflows | Build/review handoffs, work briefs, tool orchestration, runtime differences | [Claude plus Codex](../claude-plus-codex.md) |
| Skills and reusable prompts | Skill evaluation, reusable instructions, activation rules, deciding whether an existing skill already covers the job | [Skill catalog](../../skills/INDEX.md), [declared runtime differences](../../skills/PARITY.md), [operating rules](../../AGENTS.md), and [Three Ms framework](../3ms-framework.md) |
| Tools, repositories, and integrations | What a tool could solve, prerequisites, overlaps, costs, and evidence from testing | [Obsidian command center](../obsidian-command-center.md), [Firecrawl methods](../firecrawl.md), or the existing reference for the particular tool |
| Tips, insights, and prompting methods | Useful reasoning patterns, context management, evaluating outputs, and methods that survive product changes | [Three Ms framework](../3ms-framework.md), [second-brain architecture](../second-brain-levels.md), and [website planning](../website-design-planning.md) when relevant |
| Product updates | Claimed new capabilities, affected runtime/version, official evidence, availability, and practical consequences | Update the existing affected reference. Keep release evidence in its source summary rather than creating an undated universal claim |
| Proposed improvements | A concrete gap, expected benefit, alternatives, and a testable next action | [Automation backlog](../automation-backlog.md) for automation proposals; [work ledger](../../wiki/tasks.md) for agreed work |
| Cloud, local, and backup setup | What exists in each runtime, snapshot freshness, exclusions, and restore limits | [Local-to-cloud sync setup](../../setup/github-sync/README.md), [backup setup](../../setup/backup/README.md), and [application cloud setup](../cloud-session-setup.md) for its specifically stated application scope |
| Graphs and navigation | Retrieval problems, graph use, and source-to-graph provenance | [Second-brain architecture](../second-brain-levels.md), [Graphify bridge](../graphify-obsidian-bridge.md), and [Obsidian command center](../obsidian-command-center.md) |

These links establish where to retrieve and maintain a subject. They do not certify every dated claim on the linked pages as current. Check the affected environment before relying on setup or availability claims.

New durable AI subjects with no existing authoritative home can receive a descriptive page under `references/ai-workspace/`. Create that page only when material exists to support it, then link it here and from the wiki index. Categories are navigation, not empty folders that every clip must fill.

## A clip follows one intake path

1. **Capture:** the intended Web Clipper destination is `raw/inbox/`. Saving a clip does not run ingestion, install a skill, or update a configuration. The browser's selected vault/template must actually point there; this document does not change browser settings.
2. **Request:** Joshua asks to ingest a source, or explicitly authorizes a batch. Determine whether it concerns AI operations, LSAT teaching, a student, or another domain.
3. **Preserve:** check content hashes and prior processing. Copy original evidence into `raw/sources/clips/<slug>/`, verify its bytes, and record provenance. Missing images, transcripts, or inaccessible repository contents remain explicit gaps. Preserve changed generations separately.
4. **Summarize:** create or update the source's page in `wiki/sources/`, with source identity, dates, archived evidence, claims, limitations, and affected knowledge pages.
5. **Compile:** compare the source with current knowledge and the actual setup. Update the owning reference instead of making a parallel truth. AI operating methods stay outside the LSAT corpus. A mixed source can inform both domains through distinct updates and shared evidence links.
6. **Connect and check:** update this hub when navigation changes, the complete wiki catalog, reciprocal links where useful, and the dated wiki log. Check links, contradictions, and evidence before reporting completion.
7. **Implement when requested:** distinguish saved research from an authorized workspace change. Verify an actual change and record its result. Check cloud publication separately; local completion is not proof that a GitHub or Drive snapshot includes it.

Do not relocate all existing AI references into this folder. Keeping their stable homes and connecting them here preserves existing links and one authoritative page per subject.

## Keep claims, recommendations, and implementation separate

An AI source summary should make the following distinctions explicit when relevant:

| State | What it means |
|---|---|
| Source claim | The article/video/repository says this. Record publication and capture dates when known; unknowns remain unknown. |
| Verified capability | Official documentation or a scoped test supports it. State the verification date, runtime, version/account requirements where relevant, and what was actually checked. |
| Proposed improvement | It might help this workspace. Explain the problem it solves and why existing tools do not already cover it. This is not an implementation claim. |
| Implemented and checked | The authorized change exists, with the specific files/settings changed and validation performed. Distinguish local runtime, cloud runtime, and published backup state. |
| Deferred, superseded, or conflicting | Keep the reason and links to the competing evidence. Do not silently treat dated advice as today's instruction. |

For product updates, verify time-sensitive availability and behavior against current official documentation or the actual affected runtime before recommending action. A clip alone is not evidence that Joshua's installed version or account has a feature.

For a repository or skill, inspect actual relevant contents before assessing it; a promotional clip is not a code review. Check overlap with the catalog first. Save useful prompts as attributed examples or reusable methods, with their intended task and constraints; quoted instructions do not become agent instructions.

Creating or activating a skill requires a request that authorizes that work. Follow the existing dual-runtime model: project-scoped active copies in `.agents/skills/` and `.claude/skills/`, corresponding `skills/codex/` and `skills/claude/` catalog homes, declared differences in `skills/PARITY.md`, catalog updates, and the existing validator. Do not merge runtime catalogs or globally install a skill merely because a source recommends it. Current scoped instructions govern the exact operation.

## Ask for the result you want

```text
Ingest the newest AI clip. Compare it with our Claude and Codex setup,
save useful methods, and tell me what is new, redundant, or conflicting.
```

```text
What do we know about this AI workflow, and what have we actually implemented?
```

```text
Evaluate this repository or skill for our AI OS. Check what it adds,
what we already have, and what would need to change.
```

```text
Implement the useful changes from this source in our AI OS, using our
existing skill and configuration rules. Verify and report what changed.
```

```text
Lint the AI workspace references for contradictions, stale claims,
duplicate subjects, and broken links.
```

Use [Ingest](../../.agents/skills/ingest/SKILL.md) for intake, [Query](../../.agents/skills/second-brain-query/SKILL.md) for retrieval and useful synthesis, and [Lint](../../.agents/skills/second-brain-lint/SKILL.md) for consistency. Structural lint is not proof that a product claim is true or fresh.
