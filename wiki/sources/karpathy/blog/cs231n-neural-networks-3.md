---
type: source
subject: CS231n neural networks: learning diagnostics
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-3.md
semantic-status: compiled-text
---

# CS231n neural networks: learning diagnostics

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:14.257815Z.
Original: [CS231n neural networks: learning diagnostics](https://cs231n.github.io/neural-networks-3/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-3.md). SHA-256: `4ba7273d1c6de885496c124db128735fd5bc43e9c23a69b3f491f269c00d3dbd`.

## What this source says

The note turns gradient checking into a diagnostic process: centered differences, relative error, double precision, characteristic states, kink detection, reproducible randomness and checking every parameter family. Before scaling, it expects sensible chance loss and tiny-set overfitting but warns that those can still mask bugs. Training diagnostics include loss, train/validation gap, update-to-weight ratio and distributions. It surveys SGD, momentum, adaptive updates, coarse-to-fine random hyperparameter search, saved checkpoints and ensemble diversity/cost.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-3.md):

> Even if the gradient check succeeds at that point

## Interpretation and limits

A single passing numerical point or overfit test does not prove global correctness. This is course/team guidance, not established sole Karpathy authorship; heuristic thresholds and optimizer preferences are historical. The captured kink example appears inconsistent in its exponent, and encoding artifacts remain. No training, numerical audit or visual inspection of charts was performed. Ensemble claims concern these model settings, not guaranteed independence of LLM reviewers. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
