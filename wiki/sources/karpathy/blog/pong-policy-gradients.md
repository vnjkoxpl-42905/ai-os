---
type: source
subject: Pong from pixels and the limits of policy gradients
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2016_05_31_rl.md
semantic-status: compiled-text
---

# Pong from pixels and the limits of policy gradients

Author: Andrej Karpathy. Published: 2016-05-31. Captured: 2026-10-08T09:35:13.391647Z.
Original: [Pong from pixels and the limits of policy gradients](https://karpathy.github.io/2016/05/31/rl/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2016_05_31_rl.md). SHA-256: `3596faf2c386bb1ff5d554eb2e7e30e676cbd78a8da0904ee3db5556a94ecec6`.

## What this source says

Karpathy explains reinforcement-learning progress through compute, organized data, algorithms and infrastructure, then builds a two-layer stochastic Pong policy with frame differences. He develops delayed credit assignment, reward-weighted log-probability updates, advantages, discounting, normalization and the score-function derivation. His reported experiment needs roughly 200,000 games to modestly beat the fixed opponent. He contrasts brute-force discovery with human prior knowledge and planning, extends the estimator to nondifferentiable memory/attention choices, and closes with exploration costs, expert demonstrations and simpler CEM baselines before complex policy gradients.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2016_05_31_rl.md):

> One should always try a BB gun before reaching for the Bazooka.

## Interpretation and limits

Strong independent evidence for minimal baselines before elaborate methods and for understanding mechanisms to predict failure: sparse rewards, long planning and real-time exploration change applicability. Performance is a reported historical experiment, not reproduced here. Claims about current RL state, preferred algorithms, robotics and TRPO are from 2016, not present recommendations. Code/formulas were read, not executed or numerically certified; figures and linked research were not inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
