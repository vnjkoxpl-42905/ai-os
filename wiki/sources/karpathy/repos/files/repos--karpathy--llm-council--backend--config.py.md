---
type: source
subject: "GitHub source repos/karpathy/llm-council/backend/config.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/backend/config.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm-council/backend/config.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/backend/config.py), SHA-256 `f527f3c7bf88f7e02e0bf1879c3bfd7af63682d4494df5b876197fc9899704f6`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
"""Configuration for the LLM Council.""" import os from dotenv import load_dotenv load_dotenv() # OpenRouter API
```

Six sources fully read. Tokenizer.py explicitly Meta-derived lightly modified under Llama Community License, exports piece scores/UTF8 bytes, whitespace replacement/BOS EOS labels and max length to C format; not independent Karpathy belief. Train.py supports smalldebug or DDP, validates tokenizer and accumulation divisibility, records tokens-per-iteration, seed offsets, mixed precision/scaler, resume architecture/model/optimizer, compile, train/val loss, warmup-cosine LR, validation checkpoints, gradient accumulation with last-step sync, unscale-before-clip and prefetch. Optional logging failure surfaced with print; max_iters strict-greater termination adds extra iteration. Comments admit unexplained checkpoint prefix, prefer direct DDP flag over duplicative context; preserve contextual simplicity choice. Windows mmap shim is credited mman-win32, maps file/protection/flush/locks, error mapping TODO and GetTickCount wraps, no independent persona. Council package marker and config load .env key by name, four historical model IDs, Gemini chair, OpenRouter endpoint and local conversations path; no credentials read or API run.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-5.1",
    "google/gemini-3-pro-preview",
    "anthropic/claude-sonnet-4.5",
    "x-ai/grok-4",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemini-3-pro-preview"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
