---
type: reference
subject: AI workspace learning and improvements
created: 2026-10-08
updated: 2026-10-21
aliases: [AI setup, AI learning, Claude and Codex improvements]
tags: [ai-workspace, claude, codex, llm-wiki]
sources: []
---

# Turn AI clips into useful workspace knowledge

## Use the 2026-10-29 guide collection

The supplied guides are preserved as evidence and are usable from either Claude or Codex where the method applies. Start with the result you want:

| Need | Route |
|---|---|
| Strengthen the outcome, professional method, or range of perspectives | [Three types of AI ambition](../../wiki/sources/guide-ai-ambition-2026.md). Choose additional review only when it adds evidence and the runtime permits it. |
| Diagnose weak prompts, overloaded context, or unsafe setup | [23 Claude mistakes](../../wiki/sources/guide-claude-mistakes-2026.md). Its general principles transfer; its Claude commands do not automatically work in Codex. |
| Find the existing applications, routines, memory and skills | [Operating inventory](operating-inventory.md), with [ARMS v1](../../wiki/sources/guide-arms-agentic-os.md) and [v2](../../wiki/sources/guide-arms-agentic-os-v2.md) as source context. The guides do not replace this workspace. |
| Clarify a dense answer or improve prose | [Jargon fixer guide](../../wiki/sources/guide-claude-jargon-fixer.md); use `wait-what` for a re-explanation and `humanizer` for a faithful prose edit. A Claude output style is a Claude setting, not a Codex setting. |
| Find recommended plugins and effects | [Plugin guide](../../wiki/sources/guide-claude-plugins-2026.md). Check actual installation and compatibility before relying on a tool; design components belong in the target project. |
| Browse visual examples | [Mobbin screen index](../../design/mobbin-sample-pack-100.md), via the shared [design hub](../../design/README.md). The supplied pack is for personal reference and does not grant republishing rights. |

The source prompts are examples, not new standing instructions. Linked community-only packages, paid services, scheduled jobs and global settings are not established by these PDFs. See each source record for coverage and limitations.

The project copies now include `be-ambitious` for improving a task's outcome and method, `bro` for a short plain-language restatement, `wait-what` for a contextual re-explanation, `no-ai-slop` for editing prose, and `i-have-adhd` for an explicitly requested action-first response. They are available in both project runtime skill folders. The existing `humanizer` also covers prose editing; choose the one suited to the task. The focus skill is optional and does not enable a persistent setting. Availability in a newly started runtime still needs a fresh-session check.

The [integration review](../../research/2026-10-29-ai-guides/integrations-review.md) records `calibrate` and `asd-ste100` project installations, Ribbon's tests and remaining installation limits, and resources that require community access or paid services. The [command guard evaluation](../../research/2026-10-29-guard/REPORT.md) records a Windows Codex hook bypass and its test side effects; the guard is not installed.

Joshua expects a substantial share of incoming clips to cover Claude, Codex, AI tips, prompts, repositories, new skills, product updates, and possible workspace improvements. This is the navigation and filing guide for that material. It is separate from the [LSAT teaching corpus](../../corpus/index.md), while remaining part of the same second brain.

This hub organizes existing authoritative pages rather than copying their knowledge into another set of pages. The intake rules remain in the [LLM Wiki schema](../../system/schema/llm-wiki.md), and the overall catalog remains [the wiki index](../../wiki/index.md).

[Recovered practical methods](migrated-source-methods.md) add the old vault's detailed artifact-review, skill-evaluation and evidence-checking recipes, plus its unimplemented annotation idea. [Migration coverage](../../research/obsidian-vault-comparison/2026-10-07/active-migration-coverage.md) maps the original research and root files to current homes and explains exclusions.

[Karpathy source compilation](../../wiki/karpathy/index.md) now spans domain source pages and explicit semantic coverage. [Use the teaching setup](karpathy-method.md) for the reviewed rules, project agent, teaching skill and scoped Python execution gate. Compilation of the saved collection is complete according to the [current compilation audit](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md). This does not establish exhaustive public-source acquisition or full understanding of binary, generated or media payloads. The [verified collection handoff](../../research/karpathy-brain-2026-10-08/HANDOFF-VERIFICATION.md) records missing coverage, attribution limits and corrections to the original completeness claims.

[Resumable X collector](x-archive-collector.md) documents the free local script, signed-in persistent Chrome route, evidence ledgers, source-preserving repairs and retrieval limits.

[Chase AI's seven design skills clip](../../wiki/sources/top-7-claude-design-skills-chase-ai.md) records which suggestions already existed, which skills were activated for Claude and Codex, the pinned GSAP/Design Lang/React Bits repositories, and the unresolved transition-skill identity.

[ChatGPT subscription API credits](../../wiki/sources/openai-chatgpt-subscription-api-credits.md) explains eligibility, linking an API organization, and what the benefit covers.

## Find the right kind of AI knowledge

| Category | What belongs here | Existing home to consult or update |
|---|---|---|
| Claude and Codex workflows | Build/review handoffs, work briefs, tool orchestration, runtime differences | [Claude plus Codex](../claude-plus-codex.md); [four Claude Code strategies](../../wiki/sources/4-claude-engineering-prompt-strategies-austin-marchese.md) (overlap with existing practices; source claims remain attributed) |
| Skills and reusable prompts | Skill evaluation, reusable instructions, activation rules, deciding whether an existing skill already covers the job | [Skill catalog](../../skills/INDEX.md), [declared runtime differences](../../skills/PARITY.md), [operating rules](../../AGENTS.md), and [Three Ms framework](../3ms-framework.md). Skill-writing method: [Matt Pocock's process](../../wiki/sources/matt-pocock-system-claude-skills-austin-marchese.md); voice cloning: [Dan Martell](../../wiki/sources/make-ai-sound-like-you-dan-martell.md) |
| Tools, repositories, and integrations | What a tool could solve, prerequisites, overlaps, costs, and evidence from testing | [Obsidian command center](../obsidian-command-center.md), [Firecrawl methods](../firecrawl.md), [video generation options](../../wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md) for Remotion and plain-JavaScript video, or the existing reference for the particular tool. Repo roundups: [five repos incl. SkillSpector](../../wiki/sources/greg-isenberg-5-github-repos-ai-slop.md). Recent source claims: [Nate Herk's AI tools roundup](../../wiki/sources/100-ai-tools-nate-herk.md), [Ajane Pinnock's Claude Code editing workflow](../../wiki/sources/claude-code-video-editing-ajane-pinnock.md) |
| Tips, insights, and prompting methods | Useful reasoning patterns, context management, evaluating outputs, and methods that survive product changes | [Three Ms framework](../3ms-framework.md), [second-brain architecture](../second-brain-levels.md), [second-brain adoption ledger](second-brain-adoptions.md) for outside setups weighed against ai-os, and [website planning](../website-design-planning.md) when relevant |
| Product updates | Claimed new capabilities, affected runtime/version, official evidence, availability, and practical consequences | Update the existing affected reference. Keep release evidence in its source summary rather than creating an undated universal claim |
| Proposed improvements | A concrete gap, expected benefit, alternatives, and a testable next action | [Automation backlog](../automation-backlog.md) for automation proposals; [AI action queue](action-queue.md) for source-derived items; [work ledger](../../wiki/tasks.md) for agreed work. Automation design: [Austin Marchese's six steps](../../wiki/sources/automate-99-percent-work-claude-austin-marchese.md), [managing an agent: job description, tool limits, fresh reviewer](../../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md), [Jeff Su's file rulebook](../../wiki/sources/stop-organizing-files-yourself-jeff-su.md) |
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

Use [Ingest](../../.agents/skills/second-brain-ingest/SKILL.md) for intake, [Query](../../.agents/skills/second-brain-query/SKILL.md) for retrieval and useful synthesis, and [Lint](../../.agents/skills/second-brain-lint/SKILL.md) for consistency. Structural lint is not proof that a product claim is true or fresh.


## Shared design domain

[Design hub](../../design/README.md) is the dedicated design entry point for Claude Code and Codex. Design clips still use the single intake/archive/source-summary pipeline; the hub connects skills, repositories, tips, methods and research. Existing AI references and queues remain authoritative at their current paths.


## Inbox batch processed 2026-10-26

[Batch report](../../research/2026-10-26-inbox-ingest/REPORT.md) records duplicate checks, preserved revisions, new summaries and coverage limits. New sources include [ARMS and retrieval](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md), [small-business skills](../../wiki/sources/anthropic-small-business-13-skills-austin-marchese.md), and [Karpathy expert-agent commentary](../../wiki/sources/karpathy-expert-agent-nate-herk.md). Source claims are captured, not current product verification. The canonical Karpathy record already links five inspected numbered prompt cards and the actual test command; this batch did not repeat playback. Follow-up is in AQ-033 through AQ-041; existing items retain their statuses.

## Practical source implementation (2026-10-26)

[Implementation report and current19-item queue](../../research/2026-10-26-source-implementation/REPORT.md) records actual work and no-adoption decisions. Use the [operating inventory](operating-inventory.md) to find application/routine/memory/skill owners, or [compiled retrieval](compiled-retrieval.md) for bounded evidence candidates and its limitations. Existing source summaries carry completion, decline and partial records; archived evidence is unchanged.
