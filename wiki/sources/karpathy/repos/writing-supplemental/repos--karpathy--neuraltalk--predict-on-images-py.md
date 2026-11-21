---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/predict_on_images.py
---

# repos/karpathy/neuraltalk/predict_on_images.py

Original: [captured source](https://github.com/karpathy/neuraltalk). Capture: 2026-10-08T09:35:06.485083Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/predict_on_images.py). SHA-256: `5769f94ec11b9fef509a8c3f4ca004126fab4963c115ea5640403e5d861f7934`.

## Source account

```text
This script is used to predict sentences for arbitrary images
```

Caption inference loads a trusted pickle checkpoint, tasks.txt image names and aligned 4096-column MATLAB features, decodes captions and writes JSON plus an HTML image/caption gallery. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/predict_on_images.py).

```text
html += '<img src="%s" height="400"><br>'
```

Output HTML interpolates paths/text without escaping, and feature/name alignment is assumed. Beam-size advice is a captured comment, not verified monotonic quality improvement. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/predict_on_images.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
