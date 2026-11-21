---
type: source
subject: "repos/karpathy/randomfun/lectures/micrograd/micrograd_lecture_second_half_roughly.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/randomfun/lectures/micrograd/micrograd_lecture_second_half_roughly.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/randomfun/lectures/micrograd/micrograd_lecture_second_half_roughly.ipynb). SHA-256 `4d264c8328730688412e98480e0cf54e43446ad942cec0b441842fa0b7a96048`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Value gains constant coercion, powers, division, negation, exp and reverse topological backward. The exp backward includes an explicit correction to the video: use += rather than =. A tanh construction is compared with an exponential identity and PyTorch double-precision gradients. Neuron, Layer and MLP classes train four toy examples using mean-squared error and clear parameter gradients before backward. Captured losses decline from about 0.002056 to 0.001793; these are saved outputs, not a fresh run.

> NOTE: in the video I incorrectly used = instead of +=. Fixed here.

## Limits

Reviewed all 20 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.

## Duplicate provenance

This physical path is byte-identical to the fully reviewed notebook `repos/karpathy/nn-zero-to-hero/lectures/micrograd/micrograd_lecture_second_half_roughly.ipynb`. The complete decoded-content review is reused because the physical bytes are identical; this is not an independent execution or additional authored evidence.
