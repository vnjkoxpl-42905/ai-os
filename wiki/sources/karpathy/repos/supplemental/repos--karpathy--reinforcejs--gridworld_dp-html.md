---
type: source
subject: "repos/karpathy/reinforcejs/gridworld_dp.html"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reinforcejs/gridworld_dp.html

Captured repository text; ownership does not establish individual authorship. Original date: 2015-04-19T02:35:59Z (created); pushed 2019-02-18T20:11:56Z. Captured: 2026-10-08T09:35:29.097136Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/gridworld_dp.html). SHA-256 `3b0cd5bdb2ff04c0e258eb6ef06a59777c100b106b1dc024291eee033550d4c5`. Manifest hash match: True.

## Reviewed content

A deterministic 10x10 Gridworld exposes state rewards, policy arrows and value colors, with separate one-sweep evaluation and greedy update controls plus reward sliders. The tutorial derives Bellman expectation and backups before code, explains tie probability distribution, and distinguishes one-backup value iteration from converged evaluation in policy iteration. It explicitly limits the nextStateDistribution API to one deterministic next state despite its name, contrasts exact small-state DP with unavailable real-world dynamics and continuous spaces, and links Sutton for proof. Static UI/code/text fully read; no demo execution.

> - `env.nextStateDistribution(s,a)`, which is a misnomer, since right now the library assumes deterministic MDPs that have a single unique new state for every (state, action) pair. Therefore, the function should return a single integer that identifies the next state of the world

## Limits

Complete preserved text read, lines 1-627. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
