---
type: source
subject: Nate Herk's five AI OS tips: context failures, router CLAUDE.md, audit skill, segmenting knowledge
created: 2026-11-20
updated: 2026-11-20
aliases: [Steal My Exact AI OS Setup (5 simple tips), Nate Herk AI OS audit, context poisoning bloat confusion clash]
tags: [ai-workspace, second-brain, routers, audit, vaults]
evidence: ../../raw/sources/clips/steal-my-ai-os-setup-5-tips-nate-herk/clip.md
sha256: b047998b4b9bde668900c45da2bb8df67eb99b4c15efea0951e9c89977323607
contradictions: []
sources:
  - ../../raw/sources/clips/steal-my-ai-os-setup-5-tips-nate-herk/PROVENANCE.md
---

# Keep an AI OS accurate as it grows: route, audit, refresh, segment, trace mistakes

Nate Herk, [Steal My Exact AI OS Setup (5 simple tips)](https://www.youtube.com/watch?v=Ek1NBfnnTH0). No date in the clip; his mentions of July 22 and June 29 suggest about 2026-07-22 (inferred). About 25 minutes. [Preserved text](../../raw/sources/clips/steal-my-ai-os-setup-5-tips-nate-herk/clip.md), [provenance](../../raw/sources/clips/steal-my-ai-os-setup-5-tips-nate-herk/PROVENANCE.md), [hash manifest](../../raw/sources/clips/steal-my-ai-os-setup-5-tips-nate-herk/SHA256SUMS). An older generation with a shorter description is in [the recovered old-vault archive](old-obsidian-vault-2026-10-07.md); the transcript bodies are identical, this generation adds the full description and chapters.

## What the source says

- **Four context failures:** poisoning (a false fact in context; fix with verification), bloat (too much data, context rot; harder), confusion (an irrelevant or missing fact the agent fills with a guess), clash (old and new sources disagree, his refund-policy example).
- **Expertise versus situational context:** expertise is the rulebook loaded every run (who you are, policies); situational is just-in-time lookup.
- **Tip 1, `CLAUDE.md` as master router.** His whole OS is one big folder pushed to GitHub as a unit, which he calls a convenience, not the optimal setup. The root `CLAUDE.md` is a routing table plus pointers (wiki path, hot cache, index, a fallback search, memory, tools, skills, decisions, projects, "other worlds"). Subfolders can carry their own `CLAUDE.md`. "Other worlds" are standalone projects, each with its own repo, sitting inside the main folder. Flat or nested does not matter; routing rules do.
- **Tip 2, the human test:** can you find a recent deliverable in the file explorer without search or asking Claude? If yes, an agent with routing rules probably can.
- **Tip 3:** cron jobs pull recurring data (Q&A, leadership meetings) into the project.
- **Tip 4, segment knowledge:** he split one master wiki into YouTube transcripts and meeting transcripts after Claude Code suggested it. Narrower search means less bloat and confusion. Client work: internal client knowledge in `clients/<client>/` inside the OS; client-facing deliverables in a separate repo outside it.
- **Tip 5:** when the agent misses data, have it backtrack: what it searched, where it should have looked, why, then fix the routing.
- **OS audit skill:** read-only; writes a report to `audits/` with about 10 findings and a fix list marked awaiting approval; reads the prior report first; fans out one Explore subagent per check for 100+ folder projects. Checks routing integrity (including misroutes), index truth, freshness (fresh, drifting, frozen, retired, on-demand), memory, and bloat, duplication, organisation. His demo flagged an index saying 55 folders against 79 on disk.
- Team syncing is unsolved: a people and habit problem, not a tech one.

## Limits and distrust

The audit ran three times that day on a deliberately old project and grades itself. Segmenting wikis "makes answers faster and cheaper" is asserted, not measured. The four failure modes overlap. Sponsor reads and promo links throughout. The human test disagrees with [the RoboNuggets clip](new-agentic-os-standard-claude-5-robonuggets.md), which says not to worry about file names.

## What this adds here

[Second-brain levels](../../references/second-brain-levels.md) compiles only the failure taxonomy and the backward trace. Not yet in the vault: expertise versus situational context, the audit skill's specific checks and five freshness states, tips 3 and 4 (including the client folder split), the explorer test. ai-os already has an `audit` skill that scores structure against the Four Cs; whether it checks index truth against disk and freshness is not verified here. Nate's segmenting is the nearest source for splitting knowledge, and it splits wikis inside one folder, not vaults. Related: [Nate Herk's Herk 2 video](claude-ultimate-second-brain-nate-herk.md), [one vault versus many](../second-brain-one-vault-vs-many.md). No action taken.

## Coverage

Read in full on 2026-11-20 by a read-only research pass.
