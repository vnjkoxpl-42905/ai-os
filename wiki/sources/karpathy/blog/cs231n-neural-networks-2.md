---
type: source
subject: CS231n neural networks: preprocessing and objectives
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-2.md
semantic-status: compiled-text
---

# CS231n neural networks: preprocessing and objectives

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:11.867073Z.
Original: [CS231n neural networks: preprocessing and objectives](https://cs231n.github.io/neural-networks-2/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-2.md). SHA-256: `d69e04a5da74a787f9b15c2d476718b3f26db6a18332aa8a60a9c2ebf223006e`.

## What this source says

The note covers centering, scaling, PCA/whitening, noise amplification and training-only preprocessing statistics. It explains symmetry-breaking initialization and variance scaling, introduces batch normalization, compares L1/L2/max-norm regularization and dropout, and distinguishes inverted dropout from test-time scaling. Loss choices depend on exclusive classes, independent attributes, regression or structured outputs.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-2.md):

> must only be computed on the training data

## Interpretation and limits

Keep data-leakage boundaries and objective semantics explicit. This is historical course/team material, not established sole Karpathy authorship or universal present training advice. Captured prose has encoding artifacts and loose variance terminology; formulas and illustrative code were not certified or executed. Preferences for classification over regression and blanket BatchNorm/dropout defaults remain context-bound. Figures and cited papers were not inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
