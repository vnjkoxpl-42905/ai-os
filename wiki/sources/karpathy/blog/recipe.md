---
type: source
subject: A Recipe for Training Neural Networks
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2019_04_25_recipe.md
semantic-status: compiled-text
---

# A Recipe for Training Neural Networks

Author: Andrej Karpathy. Published: 2019-04-25. Captured: 2026-10-08T09:35:05.717093Z.
Original: [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2019_04_25_recipe.md). SHA-256: `eba46d890bf2a3bffb3e2b3d506003227eba239f5b41498ee6378a3cf8eaba39`.

## What this source says

Karpathy describes neural-network training as a leaky abstraction that can fail silently. His six stages are inspect the data, build an end-to-end training/evaluation skeleton with simple baselines, establish capacity by overfitting, regularize, tune, and extract final improvements. He recommends inspecting actual model inputs, checking initial loss, fitting a tiny batch, tracing dependencies with gradients, and adding one complexity change at a time. He distinguishes training-loss checks from validation improvement and recommends preserving a correct specific implementation before generalizing it.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2019_04_25_recipe.md):

> generalize a special case

## Interpretation and limits

Use explicit hypotheses, a trusted baseline and a measured improvement before extending a pipeline. The numerical optimizer defaults, supervised-pretraining claims and ensemble gain estimates are dated 2019 recommendations, not universal current rules. Fixed seeds alone do not guarantee determinism on every modern backend. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
