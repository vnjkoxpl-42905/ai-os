---
type: source
subject: CS231n Transfer Learning
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_transfer-learning.md
semantic-status: compiled-text
---

# CS231n Transfer Learning

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:34.543266Z.
Original: [CS231n Transfer Learning](https://cs231n.github.io/transfer-learning/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_transfer-learning.md). SHA-256: `a3a44eaf5d7b58edabbf598070a335a6010e47cd72cd94a06d762093ac5c1467`.

## What this source says

The draft course notes distinguish a frozen pretrained ConvNet feature extractor, partial/full fine-tuning and using shared pretrained checkpoints. Their four scenarios depend on target-data size and similarity to the pretraining data. They discuss more generic early features, dataset-specific later features, architecture constraints and lower learning rates for pretrained layers.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_transfer-learning.md):

> the size of the new dataset

## Interpretation and limits

Choose reuse depth based on target evidence and distribution shift rather than automatically starting from scratch. Historical AlexNet/Caffe examples and runtime claims are not current prescriptions. Attribution is course/team material; linked papers were not separately reviewed. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
