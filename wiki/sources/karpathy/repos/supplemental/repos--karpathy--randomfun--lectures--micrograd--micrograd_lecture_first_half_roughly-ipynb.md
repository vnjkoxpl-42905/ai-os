---
type: source
subject: "repos/karpathy/randomfun/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/randomfun/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/randomfun/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb). SHA-256 `b3e6d408fee3631c8f5acae4642666c2df37127b35ac9ef21c9190a68ffc4e53`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Polynomial finite differences introduce scalar derivatives, then a Value class tracks arithmetic graphs, local backward closures and reverse topological propagation. Addition and multiplication accumulate gradients with +=, including a shared operand example. A two-input tanh neuron is differentiated manually and with backward. Graphviz trace code was read, but rendered graph pixels were not reviewed.

> self.grad += other.data * out.grad

## Limits

Reviewed all 34 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.

## Duplicate provenance

This physical path is byte-identical to the fully reviewed notebook `repos/karpathy/nn-zero-to-hero/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb`. The complete decoded-content review is reused because the physical bytes are identical; this is not an independent execution or additional authored evidence.
