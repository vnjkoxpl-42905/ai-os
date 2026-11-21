---
type: source
subject: CS231n image classification and validation
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_classification.md
semantic-status: compiled-text
---

# CS231n image classification and validation

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:02.944858Z.
Original: [CS231n image classification and validation](https://cs231n.github.io/classification/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_classification.md). SHA-256: `b07ebfb747fd6b43c026f508333b49fb02285400b7f007d8e3e199c4488104a3`.

## What this source says

The course grounds image classification in pixel arrays and viewpoint, scale, illumination, occlusion and class variation. A nearest-neighbor implementation introduces train/predict interfaces, L1 versus L2 similarity and k-voting. It then separates training, validation and held-out testing, explains cross-validation, and shows why pixel similarity and convenient training cost can conceal poor semantics and expensive inference.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_classification.md):

> we cannot use the test set for the purpose of tweaking hyperparameters

## Interpretation and limits

The transferable rule is separating tuning feedback from final acceptance and checking whether a similarity metric measures the intended concept. This is course/team content rather than established sole Karpathy authorship. Reported CIFAR accuracies and timings are historical examples, not reproduced current benchmarks. Encoding artifacts and old Python syntax remain; figures and references were not inspected and code was not run. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
