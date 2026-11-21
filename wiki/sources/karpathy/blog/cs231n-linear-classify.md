---
type: source
subject: CS231n linear classification and objective semantics
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_linear-classify.md
semantic-status: compiled-text
---

# CS231n linear classification and objective semantics

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:07.444721Z.
Original: [CS231n linear classification and objective semantics](https://cs231n.github.io/linear-classify/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_linear-classify.md). SHA-256: `8807c46477b61a5c30ac9d865b8d559ffe558af383ef4762fbce0780be6c66a3`.

## What this source says

The note replaces nearest-neighbor storage and exhaustive inference with learned parameterized scores. It explains matrix shapes, templates, multimodal limitations, bias folding and centering before defining multiclass hinge loss, regularization and cross-entropy. Worked examples distinguish meeting a margin from continually increasing correct-class probability. Softmax receives information-theoretic/probabilistic interpretations, a max-subtraction numerical-stability implementation, and a warning that output sharpness depends on regularization. Raw losses from different objectives are not comparable.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_linear-classify.md):

> these numbers are not comparable

## Interpretation and limits

Useful teaching patterns include explicit shapes, multiple interpretations, worked counterexamples and separating scores from calibrated confidence. This is course/team material rather than established sole Karpathy authorship. Historical recommendations about SVM/softmax comparability and fixed margins remain scoped to these formulations; code and equations were read but not executed or independently certified, and figures/demo/references were not reviewed. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
