---
type: source
subject: RoboNuggets plugin and component recommendations
created: 2026-10-29
updated: 2026-10-29
tags: [ai-workspace, claude, codex, design]
evidence: ../../raw/sources/ai-guides-2026-10-29/claude-plugins/claude-plugins-summary.pdf
sha256: d608b8aad667abb6a70271a3b6b6e2a3aad5131e2a21827ef05b6be32dd4919f
sources:
  - ../../raw/sources/ai-guides-2026-10-29/claude-plugins/PROVENANCE.md
aliases: [Free Claude Code plugins guide]
contradictions: []
---

# Evaluate each plugin and visual effect for its job

RoboNuggets, *Free Claude Code Plugins*, seven pages, marked 2026 with no specific publication date. [Archived PDF](../../raw/sources/ai-guides-2026-10-29/claude-plugins/claude-plugins-summary.pdf) and [provenance](../../raw/sources/ai-guides-2026-10-29/claude-plugins/PROVENANCE.md).

| Source recommendation | Use described in guide | What must be checked |
|---|---|---|
| [Destructive Command Guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Blocks patterns of potentially destructive commands; guide claims support for Claude Code, Codex, Gemini CLI and Copilot. | Actual hooks, Windows behavior, configuration, permissions and interaction with existing guardrails. |
| [CanvasUI](https://canvasui.dev/) and [repository](https://github.com/DavidHDev/canvas-ui) | GPU effects copied into a site; guide gives a shadcn registry command. | Current license, actual source and performance, accessibility, framework compatibility and fit with brief. The guide describes MIT plus Commons Clause; do not assume unrestricted MIT. |
| Jakub Antalik [orbs](https://orbs.jakubantalik.com/), [beam](https://beam.jakubantalik.com/), [metal](https://metal.jakubantalik.com/) | Individual effects for an indicator, border and shader. | Source availability and license, reduced motion, performance and design fit. |
| [no-ai-slop](https://github.com/petergyang/no-ai-slop) | Writing revision and pattern detection. | Actual skill content and overlap with existing voice and humanizer workflows; source's global install suggestion is not proof of suitability. |
| [i-have-adhd](https://github.com/ayghri/i-have-adhd) | Claude plugin prescribing action-first answers and an always-on toggle. | Inspect plugin behavior and compatibility with Joshua's preferences; do not infer a diagnosis or impose an always-on style. |

> “what each one does, why it matters, and where to get it” (p. 1).

The guide gives installation directions and claims about performance, platform support and licensing. Those are attributed guide claims, not independently verified implementation results. It also promotes the RoboNuggets community and mentions `/quick` and an in-house humanizer without supplying their code. Do not treat a mention or a link as an installed component. Use the [design hub](../../design/README.md) for visual references and the [AI workspace](../../references/ai-workspace/index.md) for skill and tool evaluation. Current project scope, licenses and runtime instructions govern any installation.

All seven extracted pages were read. Linked repositories, demos, licenses and runtime behavior were not independently checked in this source compilation.

## Local implementation (2026-10-29)

`no-ai-slop` and optional `i-have-adhd` are installed in the Claude and Codex project catalogs and active folders with pinned provenance and licenses. Their skill files match across the four copies; fresh-session discovery and invocation remain untested. No persistent focus mode was enabled. Canvas UI is already routed through the design library. The command guard remains an evaluation item, AQ-043; it is not installed or proven to protect these runtimes.

## Guard evaluation (2026-10-29)

[Evaluation report](../../research/2026-10-29-guard/REPORT.md): release checksum and synthetic payload checks passed, but real runtime dispatch was not tested and upstream documents a Windows Codex unified_exec bypass. The guard was not installed. The first probe added a Claude hook through self-heal; that entry was removed and all other parsed settings verified unchanged. AQ-043 remains open.
