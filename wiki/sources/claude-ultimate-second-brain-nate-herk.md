---
type: source
subject: Nate Herk video, his Claude Fable second brain and the Four Cs
created: 2026-10-12
updated: 2026-10-12
aliases: [I Turned Claude Into the Ultimate Second Brain, Herk 2 walkthrough]
tags: [ai-workspace, second-brain, claude, four-cs, skills]
sources: [../../raw/sources/clips/claude-ultimate-second-brain/PROVENANCE.md]
---

# Nate Herk's own second brain: ai-os already runs nearly all of it

"I Turned Claude Into the Ultimate Second Brain" is a YouTube video by Nate Herk ([YouTube](https://www.youtube.com/watch?v=8QQ_INxAhRs), published 2026-06-10, clipped 2026-09-07). The full description and transcript (about 34:09) were read on 2026-10-12. It had been pending in the inbox since 2026-09-08.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/claude-ultimate-second-brain/PROVENANCE.md). SHA-256 `61100aa59cee7ef01d00bbc4d142111c50896e35b64ae5ebf45a9282d9c5527a`.

He sells a course and community; the model claims (Claude Fable pricing, availability window, Karpathy quotes) are his, as of June 2026, and were not checked.

## What he says

- **Default first (1:54).** The operating system starts with a habit: do everything through one harness instead of scattered chat tabs. Second brain (knowledge) comes before OS (doing things).
- **Four Cs, in order (2:47).** Context and Connections make the second brain; Capabilities and Cadence make the OS.
- **Context is a routing tree (4:55).** His `CLAUDE.md` is mainly a router to rules, references, skills, wiki, hot cache and index. His test for "too much": can he and the agent both find a file quickly? He starts at about 40k tokens.
- **Other projects inside the main repo (7:21).** He moved his other Claude projects into an "other worlds" folder inside Herk 2, so one GitHub push syncs everything and the main agent can reach them.
- **Connections (9:51).** Separate static facts from live data. List where revenue, customers, calendar, comms, tasks, meetings and knowledge live. Prefers APIs and CLIs over MCP for control and cost. Static snapshots go stale (his subscriber count was off by about 180k).
- **Capabilities (16:48).** A skill can be one repeated prompt. Every run is feedback: "update the skill." Work in phases with `/clear` between research, draft and polish; delegate parallel work to cheaper models.
- **Cadence (22:53).** Earn automation with battle-tested skills; triggers are manual, event or schedule. "A prompt is never a permission layer"; assume that if it can, it will. His team's agent once emailed an unintended discount code to 150k to 200k people.
- **Usage tips (26:15).** Make it argue back; have it interview you with grill-me (his version of Matt Pocock's skill, writing brainstorm docs); make it verify its own work, including with Playwright and personas.
- **Tool-agnostic (29:35).** It is all folders and files: `.claude`, `.codex`, `.agents`, `CLAUDE.md` and `AGENTS.md` side by side.

## How it compares with ai-os (interpretation)

Almost everything here is already in place, because ai-os was built from his course material ([Three Ms framework](../../references/3ms-framework.md), [second-brain levels](../../references/second-brain-levels.md)):

| His practice | ai-os today |
|---|---|
| Router `CLAUDE.md`, hot cache, index | Root routing map, `wiki/hot.md`, `wiki/index.md` |
| Static vs live data | `connections.md`; "backend wins" rule |
| CLIs over MCP | `gws`, Firecrawl CLI, `gh` by rule |
| grill-me with brainstorm docs | `grill-me` skill, `brainstorms/` folder |
| Four Cs audit | `audit` skill |
| Keys, not prompts | Root rule "Safety is the tool layer, not prompts" |
| Claude + Codex side by side | Twin `CLAUDE.md` / `AGENTS.md`, [Claude plus Codex](../../references/claude-plus-codex.md) |

**The one real difference:** he keeps other projects inside the main repo; ai-os deliberately keeps application repos in sibling `../ai-os-projects/`, outside the vault. That rule stands; this video is not a reason to change it.

**Worth keeping in mind:** his habit of updating a skill after every run matches the root rule "when a skill run exposes a gap, improve the skill." His stale-subscriber example is the same failure ai-os guards against by letting live systems win.

## Status

Captured. No change made; nothing to install. The AIS-OS starter repo he mentions is behind his paid community; the course copy already in the vault is under `raw/sources/personal/herk-ea-course/`.

Related: [Every level of a Claude second brain](../../raw/sources/clips/every-level-of-a-claude-second-brain-explained/PROVENANCE.md), [GPT-6 Astra second brain](gpt-6-astra-ultimate-second-brain-nate-herk.md), [AI workspace hub](../../references/ai-workspace/index.md).
