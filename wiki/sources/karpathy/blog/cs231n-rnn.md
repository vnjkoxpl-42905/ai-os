---
type: source
subject: CS231n recurrent neural networks
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_rnn.md
semantic-status: compiled-text
---

# CS231n recurrent neural networks

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:27.589487Z.
Original: [CS231n recurrent neural networks](https://cs231n.github.io/rnn/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_rnn.md). SHA-256: `e635e654539fdf98513d1246ca2cf5379b7293c1882b4ea3990962a59e2a61c0`.

## What this source says

The note introduces one-to-many, many-to-one and many-to-many sequence architectures using shared recurrent weights and state. It grounds abstract vectors in a four-character hello example, then explains stacked recurrence, gradients through time, clipping for exploding gradients and LSTM gates with a separate cell-state path. The closing section explicitly says LSTMs ease long-distance learning without guaranteeing freedom from vanishing or exploding gradients.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_rnn.md):

> LSTMs do not guarantee

## Interpretation and limits

Preserve the teaching progression from an abstract recurrence to one concrete timestep and a failure mechanism. This is course/team content, not proven sole Karpathy authorship or current architecture guidance. The captured equations and prose contain notational simplifications and apparent transcription/label errors; this compilation is not a mathematical correctness certification. Actual figures and linked material were not inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
