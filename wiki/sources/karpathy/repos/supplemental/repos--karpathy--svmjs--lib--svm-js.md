---
type: source
subject: "repos/karpathy/svmjs/lib/svm.js"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/svmjs/lib/svm.js

Captured repository text; ownership does not establish individual authorship. Original date: 2012-07-08T22:23:19Z (created); pushed 2018-04-14T01:03:04Z. Captured: 2026-10-08T09:35:36.737693Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/svmjs/lib/svm.js). SHA-256 `8259f0df5d04efb3e709f8c9b4b164fb9668d0954825fac5c42962afe7f78946`. Manifest hash match: True.

## Reviewed content

MIT-attributed JavaScript binary SVM uses simplified SMO with random pair updates, regularization/tolerances and pass limits. Optional quadratic kernel cache trades memory for computation; linear models store weights, nonlinear models retain support vectors. JSON serialization covers linear/RBF but explicitly rejects custom kernels. Deprecated getWeights remains for compatibility; no training or tests executed.

> // Cache kernel computations to avoid expensive recomputation.

## Limits

Complete preserved text read, lines 1-367. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
