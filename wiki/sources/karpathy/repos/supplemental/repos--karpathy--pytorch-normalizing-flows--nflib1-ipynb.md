---
type: source
subject: "repos/karpathy/pytorch-normalizing-flows/nflib1.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/pytorch-normalizing-flows/nflib1.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/pytorch-normalizing-flows/nflib1.ipynb). SHA-256 `d190de88dbba49148fd96f411ab5ffd052a96975fdc14feff36dcba1aedc6f1c`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Two-dimensional normalizing flows compare affine, NICE, MAF, IAF, Glow and spline configurations over moon/mixture/SIGGRAPH datasets. Active spline coupling layers are interleaved with ActNorm and invertible convolutions under a logistic prior. Negative log likelihood combines prior probability and Jacobian determinant; Adam trains minibatches. Visual code exposes sample transport and layer-by-layer grid warps. Saved numeric losses are read, rendered plots not inspected. A late cell openly duplicates code due to fatigue and has an early break in the visualization loop; not a clean production pipeline.

> code duplication because

## Limits

Reviewed all 9 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.
