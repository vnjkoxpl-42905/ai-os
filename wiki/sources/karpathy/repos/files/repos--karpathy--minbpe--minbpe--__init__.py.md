---
type: source
subject: "GitHub source repos/karpathy/minbpe/minbpe/__init__.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/minbpe/__init__.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/minbpe/minbpe/__init__.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/minbpe/__init__.py), SHA-256 `d01f1961bdef63cec9c0435053c303756a7d329a59ca465f84f65383d9174119`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
from .base import Tokenizer from .basic import BasicTokenizer from .regex import RegexTokenizer from .gpt4 import
```

Five minbpe sources fully read. Lecture is explicitly unfinished draft ending to-be-continued, character tokenizer65/Shakespeare example, embeddings as indexed vectors, GPT2 byteBPE, whitespace and irregular numeric splits, diagnostic list of tokenizer-related weaknesses includes humor not universal proof. Base pair counts and nonoverlapping merge, deterministic bytes-to-merge vocabulary, escaped control display, lossless .model versus lossy UTF8 .vocab for inspection only. Base includes pattern/specials for simplicity concession. GPT4 wrapper reconstructs ranked merge forest from cl100k_base, regex3digit pattern and special IDs, historical byte permutation/inverse, prevents train/save/load explicitly rather than polluting simple base for quirks. Uses private tiktoken fields and dated GPT4 naming, not universal current model tokenizer. Package exports and empty tests marker captured. No tokenizer execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
from .base import Tokenizer
from .basic import BasicTokenizer
from .regex import RegexTokenizer
from .gpt4 import GPT4Tokenizer

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
