---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/data_provider.py
---

# repos/karpathy/neuraltalk/imagernn/data_provider.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.530496Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/data_provider.py). SHA-256: `290a83618de2cb3632932b55e667250592c982027e1f39788eb4fb25a71a0815`.

## Source account

```text
load the image features into memory
```

Loads dataset JSON and VGG MATLAB features, groups train/validation/test images, lazily caches paths and image feature columns, samples image-caption pairs and yields individual or bounded batches. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/data_provider.py).

```text
just return raw internal img sent structs
```

Returns mutable internal records to permit caching; sampling chooses an image then one caption, not uniformly across all captions. Supported dataset names are Flickr8k, Flickr30k and COCO. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/imagernn/data_provider.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
