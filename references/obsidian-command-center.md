---
type: reference
subject: The Claude Code Obsidian command center the idea, and where ai-os stands
updated: 2026-07-18
aliases: []
---

# The Claude Code + Obsidian command center — the idea, and where ai-os stands

Distilled from Chase AI's video "The Claude Code + Obsidian Setup That Now Runs My Life" (`raw/sources/clips/claude-code-obsidian-setup-runs-my-life/`, YouTube `glAoiBWVkmU`, 2026-05-15). Ingested 2026-07-18. This is a **method/architecture source about the OS itself**, not business or LSAT knowledge — the sibling of [[second-brain-levels]].

## The pitch

Opening Claude Code inside an Obsidian vault and using Obsidian only to read markdown "leaves a ton of value on the table." Turn Obsidian into a **command center on top of Claude Code**: integrated terminal (drive Claude the way you always do) plus Obsidian's visual layer (dashboards, web viewer, file tree, calendar) at eye level. You keep the terminal; you add observability the terminal can't give.

## The three moving parts

1. **Observability dashboard.** A custom Obsidian *plugin* (Claude Code wrote it — it is just code) rendering what you care about day-to-day: token burn, schedule, daily tasks, audience/metrics, research pulse (trending GitHub, Hacker News, AI headlines). Structure it however maps to your life — Chase uses overview / audience / research; others use one tab per business or per persona (owner hat vs dev hat). Design tip: prototype the look in Claude Design as if it were a web app, and ask for 3-5 style variants before committing.
2. **Skill/automation shortcut buttons.** One-click launchers for the skills you already run (plan-today, morning brief, deep research, YT pipeline, weekly review). Each button opens a **headless** Claude (`claude -p`) so it runs without polluting your active session, usually emitting a report back into the vault that the dashboard then surfaces.
3. **Free Obsidian ecosystem wins.** Community plugins: **terminal** (the integrated terminal), **hot reload** (edit the custom plugin without restarting Obsidian), **iconize** (folder icons). Core plugin: enable **web viewer** (off by default) so links open in-pane instead of kicking to Chrome.

## The architecture point (file structure)

At scale (thousands of docs) you need a legible structure or Claude burns tokens hunting and you get pushed toward a full RAG system you didn't need. The reference is the **Karpathy structure**: `raw/` (unstructured input) → `wiki/` (internal Wikipedia pages distilling the raw) → `output/` (deliverables), with an **index file at every folder level** acting as a table of contents Claude reads on the way down. But the doctrine is: *you don't have to use those exact three.* Any structure works if a human can navigate it by name — "if you can explain it and someone can understand it, Claude probably can too."

**CLAUDE.md: less is more.** At minimum it should hold (a) your vault structure so Claude knows where to go, (b) the navigation pattern for moving folder to folder, and (c) a short blurb on Obsidian best practices — wikilinks, embeds, tagging — so Claude writes files *in Obsidian format*. That is the symbiosis: Claude writes Obsidian-native, you read it natively.

## Cost note (dated, verify before quoting)

Per the video, headless/programmatic `claude -p` use no longer draws from the Max subscription — Anthropic grants ~$200/month of separate credit that headless runs bill against at API rates (~10x Max-subsidized cost). Chase judges it a non-issue at real button-click volume (you still live in the terminal). Escape hatch: swap the headless layer to Codex headless — "5 minutes to refactor," no output dip. **This is a 2026-05 claim about Anthropic billing; confirm current terms before relying on it.**

## Where ai-os already stands

| Video's idea | ai-os today |
|---|---|
| Karpathy raw/wiki/output structure | Built and exceeded — `raw/` (immutable sources), `wiki/` + `corpus/` (two LLM-wikis), index-at-each-level, plus `students/` `decisions/` `context/`. See [[second-brain-levels]] (we sit at a complete Level 2). |
| Thin CLAUDE.md = structure + navigation + Obsidian conventions | `CLAUDE.md` is a router with a routing-map table + retrieval order + a Voice section covering Obsidian-native writing. Richer than the video's minimum, same philosophy. |
| Skills as the backbone, one-click launchers | Skill DB (`skills/INDEX.md`) with copy-to-activate model; **no dashboard buttons yet** — skills fire by `/name` in the terminal. |
| Custom observability dashboard plugin | **Not built.** ai-os has `wiki/dashboard.md` (pointers, text) and `wiki/hot.md` (session cache), but no rendered visual plugin. |
| Integrated terminal + web viewer + iconize + hot reload | Terminal plugin installed; `.obsidian/` shows `open-term`, `terminal-agent-tabs`, `obsidian-icon-folder`, `claude-sidebar`, `calendar`. Closest we are to the command-center surface. |
| Headless `claude -p` button runs | Not wired. Skills run in-session. |

## What's actually worth borrowing

### Recovered plugin research requires local testing

The old vault contained three additional plugin-atlas reports, reviewed on 2026-10-07. Their recommendations disagree about Tasks, Omnisearch, Excalidraw and Tag Wrangler, and their catalog counts and performance numbers are not verified. Preserve them as [historical research](../research/obsidian-vault-comparison/2026-10-07/research-review.md), with [source provenance](../wiki/sources/old-obsidian-vault-2026-10-07.md).

The useful method is to baseline the actual device, trial one capability at a time, compare startup, navigation and typing, and retain it only when a repeated workflow improves. A shortlist is not evidence that a plugin is installed or appropriate for this laptop or phone. No plugin or Sync setting was changed by this recovery.

The structure and CLAUDE.md philosophy we already match or beat. The genuinely new capability is the **visual command-center surface**: a custom dashboard plugin + one-click headless skill launchers, so morning brief / plan-today / research-pulse outputs render at eye level instead of scrolling past in the terminal. If Joshua wants that, it's a discrete build (Claude Code writes an Obsidian plugin; wire buttons to `claude -p` skill invocations). Everything else in the video, ai-os has. Do not adopt the dashboard unless the terminal-only view becomes an actual pain — same "don't build past the pain" doctrine as [[second-brain-levels]].
