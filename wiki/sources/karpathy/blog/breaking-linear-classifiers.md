---
type: source
subject: Breaking Linear Classifiers on ImageNet
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2015_03_30_breaking-convnets.md
semantic-status: compiled-text
---

# Breaking Linear Classifiers on ImageNet

Author: Andrej Karpathy. Published: 2015-03-30. Captured: 2026-10-08T09:35:22.862506Z.
Original: [Breaking Linear Classifiers on ImageNet](https://karpathy.github.io/2015/03/30/breaking-convnets/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2015_03_30_breaking-convnets.md). SHA-256: `338f4af6e6eb5689d15ecf4380ed99b5ad43b80a27a023b98b57ded39ec7d860`.

## What this source says

Karpathy explains adversarial perturbations by first reversing parameter updates into input updates, then replacing a ConvNet with an ImageNet linear classifier and finally a ten-dimensional logistic-regression example. Aligned small coordinate changes accumulate into a large score change. He reports a regularization tradeoff between ordinary validation accuracy and resistance, and notes that standard training objectives do not demand uncertain predictions outside the natural-data region.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2015_03_30_breaking-convnets.md):

> condensing the problem to the smallest toy example

## Interpretation and limits

Simplify a puzzling phenomenon until the mechanism is inspectable, and distinguish ordinary accuracy from stress-case behavior. These are educational 2015 experiments, not executed tests or a complete modern theory of adversarial robustness. Reported numbers and speculation about other classifiers remain source claims. Figures and linked notebook were not executed or visually reviewed. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
