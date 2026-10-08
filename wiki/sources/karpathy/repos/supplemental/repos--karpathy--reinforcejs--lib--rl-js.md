---
type: source
subject: "repos/karpathy/reinforcejs/lib/rl.js"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reinforcejs/lib/rl.js

Captured repository text; ownership does not establish individual authorship. Original date: 2015-04-19T02:35:59Z (created); pushed 2019-02-18T20:11:56Z. Captured: 2026-10-08T09:35:29.161944Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/lib/rl.js). SHA-256 `8555292d2fe4afff33866c1ecf8f279b6b583043789510ef0ed967f1ab77950b`. Manifest hash match: True.

## Reviewed content

Handwritten matrix/autodiff graph records backward closures, accumulates shared gradients, uses max-shift softmax and RMSProp with clipping, and implements LSTM gates. RL layer supplies finite-state DP, epsilon-greedy SARSA/Q-learning with eligibility traces and prioritized learned-model planning, plus two-layer tanh DQN with replay and clamped TD gradients. Three policy-gradient classes are explicitly labeled buggy/nonworking and excluded from exports; do not promote them as reliable methods. Some comments are imprecise (sigmoid backward comment labels tanh), and static declarations are not passing tests.

> // buggy implementation as well, doesn't work

## Limits

Complete preserved text read, lines 1-1534. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
