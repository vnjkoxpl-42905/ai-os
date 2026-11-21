---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/extract_features.m
---

# repos/karpathy/neuraltalk/matlab_features_reference/extract_features.m

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.557811Z. Attribution: karpathy; classification: `authored_feature_extraction_reference`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/extract_features.m). SHA-256: `ae6bf25d3b5460e0d1f311f5b6b473c5640cefbba5ad1583e8ecf0da8d355cfd`.

## Source account

```text
feats = zeros(4096, N, 'single');
```

MATLAB/Caffe reference extracts 4096-dimensional VGG features in batches of ten, replicates grayscale channels, supports CPU/GPU, and saves ordinary and HDF5 MATLAB feature files. Paths are hardcoded Flickr30k/VGG examples. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/extract_features.m).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
