---
type: source
subject: "repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part5_cnn1.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part5_cnn1.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part5_cnn1.ipynb). SHA-256 `c1c50d5ebd89e47680952cb9e0d1f274cad41761707aa2f12066830c849ed38d`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Extends character context from three to eight and composes explicit Embedding, FlattenConsecutive, Linear, BatchNorm and Tanh modules into a hierarchical network. BatchNorm handles both 2-D and 3-D inputs with appropriate reduction axes and running statistics. A saved performance log distinguishes context changes, hierarchy, batchnorm bug fix and scaling: hierarchy alone does not improve validation, while bug fix and scale do. Evaluations switch layers to inference mode, then sample names. Final code explains convolution as efficient application of linear layers across space. Saved metrics are historical, not controlled fresh benchmarks.

> - fix bug in batchnorm:

## Limits

Reviewed all 21 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.
