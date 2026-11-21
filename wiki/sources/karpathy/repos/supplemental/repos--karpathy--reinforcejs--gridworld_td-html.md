---
type: source
subject: "repos/karpathy/reinforcejs/gridworld_td.html"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reinforcejs/gridworld_td.html

Captured repository text; ownership does not establish individual authorship. Original date: 2015-04-19T02:35:59Z (created); pushed 2019-02-18T20:11:56Z. Captured: 2026-10-08T09:35:29.102684Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/gridworld_td.html). SHA-256 `97ec7d9cdf044116f8bb91259ef76fe9aaca1ec3061ebd38f7d4a37ea5b62893`. Manifest hash match: True.

## Reviewed content

Interactive 10x10 finite deterministic Gridworld teaches temporal-difference learning by deriving action value, Bellman recurrence, SARSA on-policy and Q-learning off-policy updates. Controls expose exploration, reward changes, eligibility traces and model-based planning. A priority schedule propagates surprising TD errors backwards; smooth policy updates are explicitly a non-standard visualization choice. Code records actions to reach goal, not a universal reward score, and executes user-edited agent specs via eval. Static review; figures/dependencies/demo execution not reviewed.

> **Smooth Q function updates**. The last REINFORCEjs settings are `spec.smooth_policy_update` and `spec.beta`. This is non-standard and something I added for nicer visualizations. Normally you update the policy to always take the action that lead to highest Q. With this setting, I am using stochastic policy but smoothly updating the policy to converge slowly to the argmaxy action. This makes for nicer, smoother visualizations of the policy arrows.

## Limits

Complete preserved text read, lines 1-752. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
