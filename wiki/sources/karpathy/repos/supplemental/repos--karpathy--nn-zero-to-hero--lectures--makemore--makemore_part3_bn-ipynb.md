---
type: source
subject: "repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part3_bn.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part3_bn.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nn-zero-to-hero/lectures/makemore/makemore_part3_bn.ipynb). SHA-256 `464c959353b5e929bf0f922c0e7547823fb514fa2f672f30a065a9d403c641e4`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

MLP diagnostics separate initially overconfident output, saturated tanh, Kaiming initialization and batch normalization in a saved loss log. Running batch statistics support inference; deeper explicit layer classes mimic the PyTorch API. The deep-network loop intentionally stops at 1000 debugging iterations, retaining intermediate gradients for activation/gradient distributions and update-to-weight ratios. Saved deep-model loss is therefore not a fully trained result. Bonus widgets and linear-versus-batchnorm statistics expose internal signal scales beyond the lecture. Rendered charts/widgets were not visually exercised.

> break # AFTER_DEBUG:

## Limits

Reviewed all 25 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.
