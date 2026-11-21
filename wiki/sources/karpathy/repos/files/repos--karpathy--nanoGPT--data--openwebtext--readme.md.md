---
type: source
subject: "GitHub source repos/karpathy/nanoGPT/data/openwebtext/readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/openwebtext/readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanoGPT/data/openwebtext/readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/data/openwebtext/readme.md), SHA-256 `e1f86c0641994478162be888a1f120eee2777b758ac2682f9508c8835414d192`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
## openwebtext dataset after running `prepare.py` (preprocess) we get: - train.bin is ~17GB, val.bin ~8.5MB
```

Llm.c script documentation preserves comparable effective batch sizes across GPU counts while trading recomputation and microbatch size against memory and runtime; the reference scripts explicitly omit checkpoints, Hellaswag and resume. MatlabWrapper favors reuse and an interactive debugging bridge instead of reimplementing k-means, and first asks users to establish the official engine demo before wrapper-specific diagnosis. MinGPT project readmes label addition and character modeling examples, with text8/enwik8 still TODO. Nanochat covers tokenization through chat inference, uses a depth dial for principled scaling, measures bits per byte against steps/time/FLOPs together with CORE and throughput, and requires candidate changes to work across depths. It acknowledges unexercised device paths, CPU capability limits, explicit dtype choices, incomplete fp16 RL support, and AI-contribution disclosure when authors do not fully understand code. Captured price/leaderboard/hardware claims are dated results, not reruns. NanoGPT dataset readmes report token/split counts and provenance without turning training data into Karpathy beliefs; neuraltalk folder readmes separate data and checkpoints from code.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

## openwebtext dataset

after running `prepare.py` (preprocess) we get:

- train.bin is ~17GB, val.bin ~8.5MB
- train has ~9B tokens (9,035,582,198)
- val has ~4M tokens (4,434,897)

this came from 8,013,769 documents in total.

references:

- OpenAI's WebText dataset is discussed in [GPT-2 paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [OpenWebText](https://skylion007.github.io/OpenWebTextCorpus/) dataset

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
