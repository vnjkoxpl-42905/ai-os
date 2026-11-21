---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/py_caffe_feat_extract.py
---

# repos/karpathy/neuraltalk/py_caffe_feat_extract.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.487082Z. Attribution: karpathy; classification: `third_party_contribution_ahmed_osman`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/py_caffe_feat_extract.py). SHA-256: `04f94351332beae81944b553cd23df156fd378dcb53793fb8b7cd9137a215905`.

## Source account

```text
author: ahmed osman
```

Ahmed Osman-authored Python Caffe feature extractor implements MATLAB-like cubic resizing with antialiasing, grayscale expansion, BGR conversion, VGG mean subtraction and channel-first preprocessing. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/py_caffe_feat_extract.py).

```text
The extra predictions are removed later
```

Extracts 4096-dimensional VGG features in batches, repeats the last image for an incomplete batch, trims padded predictions and saves vgg_feats.mat. CLI validates path existence but assumes listed inputs are images. This contribution is not Karpathy-authored belief evidence. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/py_caffe_feat_extract.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
