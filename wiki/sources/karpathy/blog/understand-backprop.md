---
type: source
subject: Yes you should understand backprop
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_yes-you-should-understand-backprop-e2f06eab496b.md
semantic-status: compiled-text
---

# Yes you should understand backprop

Author: Andrej Karpathy. Published: Mon, 19 Dec 2016 19:50:08 GMT. Captured: 2026-10-08T09:36:44.693544Z.
Original: [Yes you should understand backprop](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_yes-you-should-understand-backprop-e2f06eab496b.md). SHA-256: `c038b2c302de83444f5c2afd6a4e648231154202dcb82c91cf7d3de9bc789f4a`.

## What this source says

Karpathy explains why CS231n assignments require manual forward and backward passes despite automatic differentiation frameworks. Saturated sigmoid activations, dead ReLUs, repeated recurrent multiplication and incorrect clipping illustrate how a plausible forward computation can have harmful gradients. He describes finding an implementation that clipped raw Q-error, eliminating gradients outside the clipping interval, and replacing this with a Huber-loss approach. He recommends intuition about the mechanism and implementation exercises rather than relying only on formal derivations.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_yes-you-should-understand-backprop-e2f06eab496b.md):

> Backpropagation is a leaky abstraction

## Interpretation and limits

Understand enough of an abstraction to diagnose its failure modes. Teach with a concrete mechanism, then let the learner implement or reproduce it. Code snippets and TensorFlow limitations are historical, not verified current API guidance. Referenced diagrams were not visually inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
