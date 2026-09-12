---
type: reference
subject: Running Claude Code and Codex on one project the idea, and where ai-os stands
updated: 2026-07-19
aliases: []
---

# Running Claude Code and Codex on one project — the idea, and where ai-os stands

Distilled from two clips ingested 2026-07-18 (archived at `raw/sources/clips/youre-using-claude-code-wrong-add-codex/` and `raw/sources/clips/codex-projects-in-5-mins/`), method/architecture sources about the OS itself, not business or LSAT knowledge. Siblings of [[obsidian-command-center]] and [[second-brain-levels]].

- **"You're Using Claude Code Wrong (Add Codex)"** — Chase AI, YouTube `VdxUKiF8CWI`, 2026-05-07. The *why + the tandem workflow*.
- **"How to Use Your Claude Code Projects in Codex in 5 Mins"** — Nate Herk, YouTube `kB9iMD0EjT8`, 2026-05-18. The *how of file structure* — one project, both agents.

## The pitch: it's "and," not "or"

Don't pick Claude Code *or* Codex. Run both on the same project and let each check the other. The Venn diagram is ~99% overlap, so learning one gets you the other for free. The argument underneath is **tool agnosticism**: you owe these companies zero loyalty, models are converging, and pitting them against each other gets better output than staying tribal. Practical upside beyond quality: if one tool is down or stuck, you switch in seconds without losing context.

## The tandem workflow (Chase)

Run Codex in its desktop app (openai.com/codex) with a terminal open inside it, then run `claude` in that terminal, so both operate in the same directory. Then bounce work between them:

- **Plan review.** Codex plans → copy the plan into Claude ("what's missing, any blind spots?") → paste Claude's critique back → Codex revises. Two expert second-opinions before any code. Works in reverse too.
- **Adversarial code review.** One builds, the other reads the same files and hunts bugs. In the demo Claude found ~20 real bugs on Codex's first pass. Telling the reviewer the *other* model wrote it may make it usefully more adversarial. There is a Codex plugin skill for Claude literally called "adversarial review."
- **Cost logic.** Uses more tokens up front, but catching bugs and weak plans early saves tokens in aggregate.
- Desktop-app niceties Chase leans on: in-app browser + sidebar dev server, click-to-annotate/screenshot front-end reviews, diff viewer, "pets" background-activity indicator. Context note: GPT-5.5 Pro ~258k window vs Claude's ~1M; new chat = the `/clear` equivalent.

## The file-structure map (Nate) — one project, both agents

Both agents read the **same shared knowledge** (docs, references, scripts, context files). Only the tool-specific wrappers differ:

| Concern | Claude Code | Codex |
|---|---|---|
| Instructions file | `CLAUDE.md` | `AGENTS.md` |
| Config folder | `.claude/` | `.codex/` |
| Skills folder | `.claude/skills/` | `.agents/skills/` |
| Skill files | markdown + YAML front matter | **identical** markdown |
| Agent files | markdown | **TOML** (same job, different format) |
| Both support | global (`~/.claude`, `~/.codex`) + project-level scope | same |

**3-layer mental model:** (1) shared knowledge any agent reads unchanged, (2) skills + agents — same content, just placed in each tool's folder, (3) tool-specific config that genuinely differs. Maintenance rule: a major change to `CLAUDE.md` gets mirrored to `AGENTS.md` (and skills/agents to their twin). Codex sub-agents don't auto-invoke — you call them explicitly.

**Convert-any-project prompt (Nate's):**

```
I built this project using Claude Code, but I need you, Codex, to be able
to use it too. Create an AGENTS.md that uses the CLAUDE.md as inspiration,
create a .codex config, put all skills in .agents, put all agents in .codex
(as TOML). Research both the Codex and Claude Code documentation and make
sure everything important converts over.
```

**Session handoff** (Nate's own skill) is the bridge: summarize decisions / active files / next steps, paste into the other tool, keep going. When one gets stuck, hand off and the other often unsticks it in seconds.

## Where ai-os stands (gap-check, 2026-07-18)

ai-os **already runs this exact pattern** — it was built dual-runtime from the reform (see `wiki/log.md` 2026-07-17, and [[../decisions/log.md]]). Point-by-point:

- **`CLAUDE.md` + `AGENTS.md` hand-owned twins** — present, mirrored, near-identical byte size. The only diffs are the *intentional* Claude↔Codex swaps (twin pointer, folder paths, the dual-runtime section written from each runtime's view). Voice section is in full parity. **No drift.**
- **`.claude/` and `.codex/` config folders** — both present (`.codex/hooks.json` mirrors the SessionStart bootstrap).
- **Skills as identical markdown, activated by copy** — `.claude/skills/` (22) and `.agents/skills/` (12); Codex runs the same business set minus the wiki/Obsidian/graphify/youtube extras, which is deliberate, not a gap.
- **`session-handoff` skill** — Nate's skill, already installed and active in both runtimes.
- **Agents as TOML for Codex** — catalog holds `agents/codex/web-researcher.toml`. Note: that agent is authored to activate **globally** (its module path is `~/.codex/agents/web-search-modules/`), so it is not project-activated into `~/ai-os/.codex/agents/`, and that is by design, not missing wiring.

**Conclusion:** these clips validate the setup rather than expose work. ai-os conforms to both videos with nothing to fix. The one thing they add that ai-os does *not* lean on is Chase's **Codex-desktop-app tandem loop** (in-app browser, annotate-to-comment, the plan↔critique ping-pong) — worth trying when a hard problem stalls Claude, but a workflow habit, not a config change.

## What's new vs already-known

- **New / worth adopting as a habit:** the plan↔critique and adversarial-review ping-pong between the two models on genuinely hard or high-stakes work; reach for the Codex desktop app's live browser + annotation when doing front-end review.
- **Already true in ai-os:** the whole file-structure map, twin instruction files, copy-based skill activation, session-handoff bridge, tool-agnostic stance.
