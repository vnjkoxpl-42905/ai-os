---
type: source
subject: CS231n minimal neural-network case study
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-case-study.md
semantic-status: compiled-text
---

# CS231n minimal neural-network case study

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:16.819963Z.
Original: [CS231n minimal neural-network case study](https://cs231n.github.io/neural-networks-case-study/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-case-study.md). SHA-256: `37f7b6e4f0fd245ac9d0d2d5bace2139ec8602717d3128c8c2367f16b8d26e07`.

## What this source says

The course note implements a three-class spiral dataset, a linear Softmax classifier and a two-layer ReLU network. It walks through score shapes, probability normalization, cross-entropy plus regularization, analytic gradients and parameter updates. The nonlinear extension changes the forward representation and adds one backward stage while retaining the surrounding training loop. Reported training accuracy rises from 49 to 98 percent.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_neural-networks-case-study.md):

> very few changes are necessary

## Interpretation and limits

This demonstrates a minimal controlled extension, not held-out generalization: the printed accuracies are on training data. Code and equations were read but not executed or exhaustively audited; the illustrative exponentiation lacks explicit stabilization. Sole Karpathy authorship is not established by the course manifest label. Figures and downloadable notebook were not separately reviewed. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
