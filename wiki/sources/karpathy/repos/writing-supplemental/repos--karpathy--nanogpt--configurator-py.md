---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/configurator.py
---

# repos/karpathy/nanoGPT/configurator.py

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.127387Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/configurator.py). SHA-256: `5cc23aca26b4ab3c0d9e5f82740f4781f9444f42718c15abcee70d93c5aabe8f`.

## Source account

```text
I just really dislike configuration
```

Simple configuration overrides execute trusted Python files then apply typed --key=value overrides to globals via literal_eval, falling back to strings. Unknown keys/type changes fail. Config files are executable code, not safe data. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/configurator.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
