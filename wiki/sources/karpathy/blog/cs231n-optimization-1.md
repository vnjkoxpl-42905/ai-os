---
type: source
subject: CS231n optimization: iterative refinement
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_optimization-1.md
semantic-status: compiled-text
---

# CS231n optimization: iterative refinement

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:19.603151Z.
Original: [CS231n optimization: iterative refinement](https://cs231n.github.io/optimization-1/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_optimization-1.md). SHA-256: `cc65f9066f159bf82dc549f551b071fc918e72d6c4adfcdadc9ee93e17c9df55`.

## What this source says

The course separates score function, loss and optimization, then motivates iterative refinement through random search, local perturbation and gradient descent. A blindfolded-hiker analogy explains direction while distinguishing the separate step-size decision. Numerical derivatives are simple but costly; analytic derivatives are efficient but implementation-prone, so the note compares both. Minibatch updates trade a full-dataset gradient for more frequent approximate feedback.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_optimization-1.md):

> This is called a **gradient check**

## Interpretation and limits

This is course/team explanation, not proof of sole Karpathy authorship. Toy accuracy outputs and performance claims were not rerun. Numerical checking is approximate and limited by finite precision and nonsmooth points. The preserved text contains replacement characters and illustrative variable inconsistencies; source fidelity is retained without treating it as a certified executable program. Figures were not inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
