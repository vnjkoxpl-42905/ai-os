---
type: source
subject: "repos/karpathy/randomfun/min-char-rnn-nb2.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/randomfun/min-char-rnn-nb2.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/randomfun/min-char-rnn-nb2.ipynb). SHA-256 `44d58ae1672f49489f1e18e61479099c94d7d642e48f23505a0eb3a6ec1cd3e5`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

The second RNN exercise retains single-character forward/backward derivations and sequence backpropagation, then adds a 10000-step sweep with hidden-state reset at corpus boundaries, smoothing losses and ordinary gradient descent. Its parameter-update comment says Adagrad although actual update lacks accumulation or adaptive scaling. Sampling remains TODO. Saved loss declines from about 105.117 to 81.810. Historical code is not a verified current training pipeline.

> # TODO: Implement a sampling function

## Limits

Reviewed all 27 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.
