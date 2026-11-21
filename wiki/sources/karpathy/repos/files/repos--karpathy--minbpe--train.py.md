---
type: source
subject: "GitHub source repos/karpathy/minbpe/train.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/train.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/minbpe/train.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/train.py), SHA-256 `9777e5ae36013509631d16cce163c94ba44d1d77be326fd64230936fca11b910`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Train our Tokenizers on some data, just to see them in action. The whole
```

minbpe tests validate multilingual round trips, exact cl100k token parity, known Wikipedia BPE merges, and save-load identity; the llama prose is a foreign fixture. Training builds Basic and Regex 512-token models from Taylor Swift text and saves model plus inspection vocabulary. minGPT demo trains a masked sorting toy, checks full greedy answers against torch.sort, and displays captured errors and accuracy. Hash-based splitting is process dependent; historical 100 percent toy accuracy is not an independent replication.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
from minbpe import BasicTokenizer, RegexTokenizer

# open some text and train a vocab of 512 tokens
text = open("tests/taylorswift.txt", "r", encoding="utf-8").read()

# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()
for TokenizerClass, name in zip([BasicTokenizer, RegexTokenizer], ["basic", "regex"]):

    # construct the Tokenizer object and kick off verbose training
    tokenizer = TokenizerClass()
    tokenizer.train(text, 512, verbose=True)
    # writes two files in the models directory: name.model, and name.vocab
    prefix = os.path.join("models", name)
    tokenizer.save(prefix)
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
