---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/deploy_features.prototxt
---

# repos/karpathy/neuraltalk/matlab_features_reference/deploy_features.prototxt

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.554106Z. Attribution: karpathy; classification: `third_party_architecture_reference`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/deploy_features.prototxt). SHA-256: `6c21cf4d4f7c58d8fa742c02d1d6b286adcf929b5c11a019a93aeb7fb3579dae`.

## Source account

```text
name: "VGG_ILSVRC_16_layers"
```

Legacy Caffe VGG-16 feature definition accepts ten 3-channel 224-pixel images, stacks thirteen padded 3x3 convolutions with ReLU/max-pooling, then 4096-unit fc6 and fc7 layers. The classifier head is absent; this is a feature-extraction architecture associated with VGG rather than an original Karpathy belief. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/deploy_features.prototxt).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
