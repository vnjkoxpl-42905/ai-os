---
type: source
subject: CS231n convolutional architectures and resource accounting
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_convolutional-networks.md
semantic-status: compiled-text
---

# CS231n convolutional architectures and resource accounting

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:05.181738Z.
Original: [CS231n convolutional architectures and resource accounting](https://cs231n.github.io/convolutional-networks/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_convolutional-networks.md). SHA-256: `47805c854c227f6ba955086bed4148e24cc2b19ac399338e5970adcbe07dfedc`.

## What this source says

The course builds CNNs as volume-transforming APIs, then derives local receptive fields, shared filters, strides, padding, spatial sizes and parameter counts with concrete indexed examples. It makes translation-sharing assumptions explicit, noting exceptions such as aligned faces. Matrix-multiply lowering exchanges duplicated input memory for efficient computation. Pooling, dilation, fully-connected/convolution conversion and shared sliding-window inference lead into architecture patterns and historical LeNet/AlexNet/VGG/Inception/ResNet cases. Detailed VGG accounting separates activation memory, parameters, gradients, optimizer caches and miscellaneous batch storage.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_convolutional-networks.md):

> the parameter sharing assumption may not make sense

## Interpretation and limits

Useful patterns are matching architectural assumptions to data and accounting separately for inference and training resources. This is course/team content, not established sole Karpathy authorship. Historical state-of-the-art, GPU limits, normalization and architecture recommendations are dated. Captured dilation numbering and stride-fit conventions can differ from current libraries, and the AlexNet input-size explanation is labeled a guess. Code, formulas, figures, demos and external references were not executed or independently verified. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
