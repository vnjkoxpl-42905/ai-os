---
type: source
subject: CS231n optimization: staged backpropagation
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_optimization-2.md
semantic-status: compiled-text
---

# CS231n optimization: staged backpropagation

Author: Andrej Karpathy (lead; course staff co-authors). Published: unknown. Captured: 2026-10-08T09:38:22.035632Z.
Original: [CS231n optimization: staged backpropagation](https://cs231n.github.io/optimization-2/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_optimization-2.md). SHA-256: `fa9b0773f92d30d3b03cc277eb0732e4f8ae333260bbff72f2c76319340e6559`.

## What this source says

The note interprets derivatives as local sensitivity, composes simple gates by the chain rule and shows a staged sigmoid and compound expression. It explains caching forward values, accumulating contributions at forks, and the different backward behavior of addition, multiplication and max. Matrix examples connect gradient shapes with dimension analysis and recommend deriving a small explicit example before vectorizing.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/cs231n-notes/cs231n.github.io_optimization-2.md):

> **Work with small, explicit examples**

## Interpretation and limits

The teaching pattern is local rules, concrete numbers, staged composition and shape checks. This is course/team material rather than established sole Karpathy authorship. Encoding artifacts and flattened circuit diagrams limit the preserved text; actual diagrams and references were not inspected. Equations/code were read but not exhaustively mathematically audited or executed, including max behavior at ties. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
