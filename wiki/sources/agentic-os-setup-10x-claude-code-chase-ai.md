---
type: source
subject: Chase AI's four levels of an agentic OS, and the vault index-at-every-level rule
created: 2026-11-20
updated: 2026-11-20
aliases: [The Agentic OS Setup That Will 10x Claude Code, Chase AI agentic OS four levels]
tags: [ai-workspace, second-brain, skills, obsidian, routines]
evidence: "../../raw/sources/clips/agentic-os-setup-10x-claude-code/The Agentic OS Setup That Will 10x Claude Code.md"
sha256: 25e3e7fdf8c6d8b7870193d2d57864c3128507db8df27eb2d2b725541f8af26a
contradictions: []
sources:
  - ../../raw/sources/clips/agentic-os-setup-10x-claude-code/PROVENANCE.md
---

# Skills and memory are 90 percent of an agentic OS; the dashboard is polish

Chase AI, [The Agentic OS Setup That Will 10x Claude Code](https://www.youtube.com/watch?v=HRw-vP0j8OM). Published 2026-06-24, clipped 2026-07-18, archived 2026-09-08 (from the archive's own provenance); about 31 minutes. This is the first wiki page for an already-archived source. [Archived text](../../raw/sources/clips/agentic-os-setup-10x-claude-code/The%20Agentic%20OS%20Setup%20That%20Will%2010x%20Claude%20Code.md), [provenance](../../raw/sources/clips/agentic-os-setup-10x-claude-code/PROVENANCE.md). A re-clip in `raw/inbox/` (2026-11-20, different bytes) has an identical transcript and lacks the archive's 11-line header; it was not archived again.

## What the source says

- **Four levels.** L1 skill architecture and loop engineering. L2 memory and state. L3 the interface (web dashboard or Obsidian plugin, with skill buttons calling headless `claude -p`, local voice). L4 distribution. He says levels 1 and 2 hold about 90 percent of the value.
- **L1 sub-phases:** workflow audit (do the task manually first, then turn it into a skill; or have Claude mine your last 3 to 20 sessions for repeated tasks; or have Claude interview you), skill creation with skill-creator, a scheduled Desktop routine that runs the skill, and loops that read past run logs.
- **L2 memory:** Obsidian is optional; a database also works. Designate a folder as the vault, copy a domain's data into it, open Claude Code there. With no database and no Obsidian, a coherent file structure gets you "99 percent of the way".
- **Structure:** a folder with ten million unlinked files makes Claude slow and expensive (rhetorical, unmeasured). He recommends Karpathy's `raw/` (unstructured), `wiki/` (structured articles) and a third folder for outputs, with an `index.md` at every folder level read on the way down, even for a one-article folder. The folders are "somewhat arbitrary". The vault `CLAUDE.md` holds the folder conventions and a navigation pattern. Run outputs are logged in one place so loops can see past runs. His own vault has `content`, `notes`, `runs`, `inbox`, `ops`, `projects` and more.
- Multiple vaults are never discussed: one designated folder holds everything.

## Limits and distrust

"90 percent of the value" is an unsupported figure repeated three times. The claim that `claude -p` still draws on the Max plan conflicts with the 2026-05 claim recorded in [the Obsidian command center reference](../../references/obsidian-command-center.md) from a different Chase AI video (headless runs billed at API rates); the two dated claims are unreconciled and neither was checked against current Anthropic pricing here. The Karpathy "over 20 million views" and "local voice model is free" claims are unverified. Sales pitch for his paid community.

## What this adds here

Present in this clip but not in [Chase AI's later Jev video](jev-claude-os-chase-ai.md): the four-level scheme, the manual-first audit option, the distribution tradeoff (a web app shares by GitHub or zip; the Obsidian version needs hands-on setup), and "run logs belong in the vault". That later page says "this is not a RAG system" and recommends letting the AI move files; this clip uses RAG only in air quotes and the vault rejected file-moving on 2026-10-14. Related: [one vault versus many](../second-brain-one-vault-vs-many.md). No action taken.

## Coverage

Read in full on 2026-11-20 by a read-only research pass; the transcript comparison against the archive was done by that pass after whitespace normalisation.
