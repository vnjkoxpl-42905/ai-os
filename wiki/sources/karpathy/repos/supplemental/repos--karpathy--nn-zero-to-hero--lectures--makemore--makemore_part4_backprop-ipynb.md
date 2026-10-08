---
type: source
subject: "repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part4_backprop.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part4_backprop.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part4_backprop.ipynb). SHA-256 `44e0d932803c14279bf9795cddfb061db9d849e32f0f4e22f749c79981730dda`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Four exercises derive every intermediate gradient manually, simplify cross-entropy and batch-normalization derivatives, then train using a custom backward pass. Nonstandard nonzero initialization is intentional so zeros cannot mask mistakes. Comparison utility checks exact equality, approximate closeness and maximum difference; saved primitive gradients all match exactly and simplified formulas approximately. Batch-norm calibration uses the training set before split evaluation and sampling. Captured training/validation losses are about 2.0705/2.1099. This supports semantic checks and explicit numerical tolerances; not a fresh execution.

> could mask an incorrect

## Limits

Reviewed all 29 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.
