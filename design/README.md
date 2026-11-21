---
type: reference
subject: Shared design knowledge and work router
created: 2026-10-24
updated: 2026-10-27
aliases: [Design hub, Design brain, Design wiki, UI library]
tags: [design, llm-wiki, claude, codex]
sources: []
---

# Start design work here

This is Joshua's shared design home for Claude Code and Codex: UI, visual composition, colour, typography, components, motion, interaction, research and design tooling. It is a domain of the existing second brain, not a second vault.

Before any design build or review, read the current brief and the relevant [principles](principles.md). For material, depth and surface work, start with [the selected near-white/charcoal reference and its lessons](principles.md#material-depth-and-a-richer-layered-feel). Apply its reasoning across projects; its palette is the LSAT U baseline, not a universal preset.

| Need | Read |
|---|---|
| **Symbols and icons**: get, make or replace one; the symbols already made | [Symbols and icons](symbols.md) |
| Tips, design process and quality checks | [Methods](methods.md), then the linked owning references |
| **Saved UI components** (21st.dev carousels, stepper, showcase; ones already in LSAT U) | [Component library catalog](../wiki/component-library.md) |
| Principles and historical briefs | [Principles router](principles.md) and [document registry](documents.generated.md) |
| Installed skills, component repositories, fonts and useful research | [Library](library.md) and [current file catalogue](catalog.generated.md) |
| A source or a recently clipped design video | [Sources and batch coverage](sources.md) |
| Work to consider doing | Existing [AI action queue](../references/ai-workspace/action-queue.md) and [LSAT U idea queue](../wiki/lsatu-idea-queue.md). No parallel design task queue. |
| All saved dashboard versions | [Open the labelled archive](prototypes/lsatu-dashboard/index.html), [archive guide](prototypes/lsatu-dashboard/README.md) |
| My Work notes: source-led local refinement | [Notes ledger decisions and rendered evidence](reviews/my-work-notes-20261027/REPORT.md) |
| My Work organization: notes, assignments and completed records | [Organization findings, local refinements and checks](reviews/my-work-organization-20261027/REPORT.md) |
| Teacher Home charcoal/off-white quality review and local calendar restoration | [Rubric, implementation, final Claude inspection and limits](reviews/classroom-quality-20261028/REPORT.md) |
| My Work live assignment/read synchronization | [Release, independent Codex review and preservation evidence](reviews/my-work-assignment-sync-20261028/REPORT.md) |
| Dashboard research and context | [Library: prototypes](library.md#dashboard-prototypes-and-visual-evidence) |
| Full skill, repo and document audits | [Skill routes](skill-routing-audit.md), [repositories](repositories.md), [document coverage](document-routing-audit.md) |
| Current skill setup and validation | [21-finding repair and verification](../research/2026-10-24-skill-repair/REPORT.md) |
| How to ingest the next clip | [Filing route](#when-another-design-clip-arrives) |

## Use this folder to improve a design

Point the agent to this file, then name the target project, page or artifact and the improvement you want. The hub selects relevant skills; reading a folder does not activate every skill or grant access to every service. Read the chosen runtime's `SKILL.md` and its required references before applying it. Check current tool availability when the workflow needs a browser, generator or connected service.

| Work needed | First skill or route |
|---|---|
| Stronger visual direction, richer composition, complete website/app polish | [Taste Skill v2](../.agents/skills/design-taste-frontend/SKILL.md), then [its provenance and limits](../.agents/skills/design-taste-frontend/UPSTREAM.md) |
| Improve an existing interface through critique and focused refinements | [Impeccable](../.agents/skills/impeccable/SKILL.md) and [methods](methods.md) |
| Study a supplied reference and translate its design decisions | [Extract design](../.agents/skills/extract-design/SKILL.md) |
| Find components or visual resources | [Design resource library](../.agents/skills/design-resource-library/SKILL.md), then [library](library.md) |
| Emil Kowalski UI, animation, mobile and prototyping skills | [Emil collection](library.md#emil-kowalskis-design-and-engineering-skills) |
| Add purposeful components or motion | [React Bits](../.agents/skills/react-bits/SKILL.md), [GSAP](../.agents/skills/gsap-core/SKILL.md), or [scroll-craft](../.agents/skills/scroll-craft/SKILL.md), selected for the actual task |
| Inspect a rendered build and interactions | [Playwright CLI](../.agents/skills/playwright-cli/SKILL.md), subject to that runtime's browser instructions |
| Other visual work, including documents, icons and media | [Full skills register](skills.generated.md), [symbols](symbols.md), and [library](library.md) |

The direct links above open project Codex copies. Claude should use the same named skill in `.claude/skills/` where present; other existing homes and vendor namespaces are listed in [skill routes](skill-routing-audit.md). A catalogue-only skill must be loaded explicitly from its entry point if the runtime permits it; it is not automatically active. Do not copy or install every listed resource.

Taste means the updated **tasteskill v2**, pinned to `12af471f627f866411b4bd785b19646d3672784c`, rather than the older High-Agency Frontend Skill. Its website and app workflows differ. Its upstream scroll-scene payload is incomplete; use the separate motion routes when that capability is needed. The project brief and approved design references take precedence over optional skill aesthetics.

Paste this into the chat working on the target project:

```text
Read C:/Users/Joshu/dev/ai-os/design/README.md and follow its relevant routes to improve this project's visual design. Use Taste Skill v2 for art direction and select other skills only where they help. Confirm the exact skill paths loaded. Inspect the current rendered design, propose your strongest direction, and wait for my approval before editing. After approval, implement, inspect desktop and phone results, and refine the weakest parts. Report actual checks and unavailable capabilities. Do not commit, push or publish.
```

## When another design clip arrives

1. Capture it in `raw/inbox/`, the existing single intake queue.
2. On an authorized ingest run, use `second-brain-ingest`: hash-dedupe, preserve source bytes/provenance, read the body, compile one canonical source summary and connect useful knowledge to its existing subject.
3. Add the source to this design hub. Cross-domain clips also remain linked from the AI workspace or media home. A title containing Dashboard does not establish that its content is design-related.
4. Route every actionable suggestion to the existing queues, or record already-here coverage. Clipping never installs a tool or approves its proposed use.
5. Update the relevant reviewed inventory under `research/2026-10-24-design-completeness/` when sources, skills, repos or documents change. Refresh linked registries with `py system/scripts/design-catalog.py`, then the wiki index with `py system/scripts/wiki-maintenance.py --index`; check evidence, links and coverage. The renderer does not discover new files automatically.

This route applies to both runtimes. It runs when ingestion is invoked; saving a browser clip alone does not launch an agent or background job.

## One home to find things, one authority per subject

Design-owned navigation and synthesis live in this folder. Existing authoritative methods, source summaries, skills and repositories are linked rather than duplicated or uprooted. Evidence stays immutable under `raw/sources/`; executable repositories stay outside the Obsidian vault; runtime skills stay in their required activation/catalog directories. Follow links from here without searching the whole machine.

The [catalogue](catalog.generated.md) is a findability inventory, not proof that every tool is authenticated, every repo was reviewed, or every referenced design is approved. Inspect current files and capabilities before use.
