---
type: source
subject: "GitHub source repos/karpathy/llm.c/dev/data/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm.c/dev/data/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/README.md), SHA-256 `163cbb490dbda4795f4985d29c24af9d4e795f500daf66a70d5580e209384440`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# dev/data organization The idea is that each dataset has a .py file here in".

The council frontend README is an unchanged React/Vite template voice, not personal Karpathy opinion. Llm.c CUDA development begins with a naive kernel, compares CPU reference outputs on GPU, times launch configurations, then substitutes a measured faster kernel; documented complexity and runtime tradeoffs are explicit. Data scripts own per-dataset cache directories and share helpers. The evaluation README pins a harness version for comparability and admits unresolved bfloat16 scoring and unexpectedly expensive runtime issues instead of hiding them. The root llm.c README keeps simple frozen CPU/fp32 references alongside fast production-oriented kernels, cross-checks logits/loss/training trajectories against PyTorch, supplies a stepwise layernorm tutorial, and distinguishes platform-specific distributed launch options without declaring one universally superior. It explicitly may reject 2-percent performance for 500 lines and an exotic dependency, while accepting a standard one-line library call. These are project constraints rather than universal bans on dependency use.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# dev/data organization

The idea is that each dataset has a .py file here in the root of `dev/data`, and each dataset then creates a directory here, and writes and caches anything inside that directory. So for example:

- running `python tinystories.py` will create a directory `tinystories` with its .bin files inside it
- running `python tinyshakespeare.py` will create a directory `tinyshakespeare` with its .bin files inside it

And so on. This way we can nicely organize multiple datasets here, share common utilities between them, and then point the .py/.c code in the root of the project accordingly to these.

Note: we support "gpt-2" and "llama" (llama 3 in particular) models and the above scripts will tokenize gpt-2 by default.

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
