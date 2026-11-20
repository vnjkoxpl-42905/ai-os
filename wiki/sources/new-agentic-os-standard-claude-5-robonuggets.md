---
type: source
subject: RoboNuggets ARMS ladder: router-first files, skill folders, routines, apps
created: 2026-11-20
updated: 2026-11-20
aliases: [The NEW Agentic OS standard for Claude 5 Models is here, RoboNuggets ARMS levels, Agentic OS Guide R66]
tags: [ai-workspace, second-brain, skills, routers]
evidence: ../../raw/sources/clips/new-agentic-os-standard-claude-5-robonuggets/clip.md
sha256: 4c5a00d7b143bb05a480c268d2e2d7333781de29251b14257bc87873e6cf4471
contradictions: []
sources:
  - ../../raw/sources/clips/new-agentic-os-standard-claude-5-robonuggets/PROVENANCE.md
---

# ARMS in three levels each, and organise files for agents, not people

Jay / RoboNuggets, [The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)](https://www.youtube.com/watch?v=8NSyI-npJCU). No publication date; he mentions an artifact "back in the 5th of August", so it was recorded after that (inferred). About 21 minutes. [Preserved text](../../raw/sources/clips/new-agentic-os-standard-claude-5-robonuggets/clip.md), [provenance](../../raw/sources/clips/new-agentic-os-standard-claude-5-robonuggets/PROVENANCE.md), [hash manifest](../../raw/sources/clips/new-agentic-os-standard-claude-5-robonuggets/SHA256SUMS).

## What the source says

- **Thesis:** the dashboard is 20 to 30 percent of the value; 70 percent is how context and the workspace are organised underneath. He names the frame ARMS (Applications, Routines, Memory, Skills) and teaches it bottom-up: skills, memory, routines, apps.
- **Skills:** L1 prebuilt skills plus skill-creator (prompt for the same task twice, make it a skill). L2 a skill is a folder whose `skill.md` routes to reference files. L3 trigger skills headlessly from a dashboard (`claude -p`).
- **Memory:** L1 a workspace of files; his folder had roughly 60,000 files, which he assumes hurts retrieval speed and plan usage. L2 organise for agents: a root `CLAUDE.md` that routes to departments, a router file per department listing its skills and references, and little attention to file names. L3 a visual graph app.
- **Routines:** L1 Claude Desktop routines (computer must be on). L2 always-on agent (Hermes) with the workspace synced by Syncthing. L3 Claude Code on a VPS, which he predicts vendors will ship.
- **Apps:** L1 desktop connectors. L2 a skill that searches for an official connector, CLI, API or MCP. L3 build your own connectors and micro apps.

## Limits and distrust

- The 20/30/70 split, "better than 99% of people" and the Claude 5 framing are opinion.
- The 60,000-file slowdown is assumed, not measured. His file counts across videos (60,000; 35,466 in [another clip](ultimate-second-brain-arms-robonuggets.md); 420,000 in [the v2 guide](guide-arms-agentic-os-v2.md)) are unreconciled.
- Syncing skills and memory to a remote agent has security implications he does not discuss (inferred).
- Upsell: Skool, RUBRIC, affiliate links. The advertised nine-page guide is not in the clip.

## Vault stance and conflict

One workspace folder, no separate vaults. Routing has three layers: root `CLAUDE.md`, department routers, skill folders. He says not to worry about file names; [Nate Herk's clip](steal-my-ai-os-setup-5-tips-nate-herk.md) says to test that a human can find files in the explorer. Conflict left open.

## What this adds here

Not in the earlier [ARMS v1 guide](guide-arms-agentic-os.md): the three-level ladders, skill folders with reference files, department routers, the 60,000-file anecdote, Hermes with Syncthing, search-connectors, micro apps. The router idea already exists in ai-os `CLAUDE.md`. No action taken.

Related: [one vault versus many](../second-brain-one-vault-vs-many.md).

## Coverage

Read in full on 2026-11-20 by a read-only research pass. No earlier version of this video exists in the vault.
