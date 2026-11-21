---
type: source
subject: "repos/karpathy/pytorch-normalizing-flows/nflib/flows.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/pytorch-normalizing-flows/nflib/flows.py

Captured repository text; ownership does not establish individual authorship. Original date: 2019-12-09T17:55:39Z (created); pushed 2020-01-27T18:37:10Z. Captured: 2026-10-08T09:35:21.238606Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/pytorch-normalizing-flows/nflib/flows.py). SHA-256 `22801dfba4a32512f557040d3d2c42e08379663d384c3256234f5df8ce0c6843`. Manifest hash match: True.

## Reviewed content

Flow library implements constant affine transforms, first-batch ActNorm, parity coupling, slow/MADE autoregressive transforms, inverse direction tradeoffs and LU-parameterized invertible mixing. Composition sums log determinants and combines a prior with flow density or sampling. Backward means inversion, not gradient backpropagation. Papers retain credit for methods; static code not executed.

> Notice that backward() is not backward as in backprop but simply inversion.

## Limits

Complete preserved text read, lines 1-294. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
