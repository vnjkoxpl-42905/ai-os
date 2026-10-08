---
type: source
subject: "repos/karpathy/randomfun/MixtureDensityNets.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-authored-cell-source-and-text-output-read
---

# repos/karpathy/randomfun/MixtureDensityNets.ipynb

[Immutable raw notebook](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/randomfun/MixtureDensityNets.ipynb). SHA-256 `b0e9f955232edcd19d60cad00b23e08499882f8610464b912a3f29b81fc22e6d`. Manifest hash match: True. Repository ownership does not establish individual authorship.

## Reviewed content

Mixture-density network predicts three Gaussian means, log standard deviations and mixture coefficients rather than a single target, modeling noisy and multimodal conditional distributions. NumPy manually derives mixture responsibilities and all parameter gradients; Adagrad optimizes full-batch negative log likelihood over 200 generated examples. Saved loss falls from 1.101843 to about -0.996209. Sparse central-difference checks compare analytical and numerical gradients, restore perturbed values, check shapes and warn for tiny values. This is mechanism-level verification, but saved checks are not a fresh run.

> This means that the network knows what it doesn't know:

## Limits

Reviewed all 11 decoded cell sources and saved text outputs; serialized metadata and image payloads not semantically reviewed. Saved outputs are historical evidence, not a fresh execution. Embedded image pixels and notebook serialization metadata were not reviewed. No captured code executed.
