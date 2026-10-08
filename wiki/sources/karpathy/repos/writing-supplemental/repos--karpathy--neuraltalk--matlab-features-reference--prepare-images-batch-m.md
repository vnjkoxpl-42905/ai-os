---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/prepare_images_batch.m
---

# repos/karpathy/neuraltalk/matlab_features_reference/prepare_images_batch.m

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.558812Z. Attribution: karpathy; classification: `authored_preprocessing_reference`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/prepare_images_batch.m). SHA-256: `9bebf0cb7ced5a9abb6c5b8005bd7ea123433871bd5aeda7d51c8165680c09f8`.

## Source account

```text
% RGB -> BGR
```

Prepares fixed ten-image tensors by resizing to 224x224, reordering RGB to BGR, swapping x/y dimensions and subtracting VGG channel means. Unfilled final-batch slots remain padded and are discarded by the caller. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/prepare_images_batch.m).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
