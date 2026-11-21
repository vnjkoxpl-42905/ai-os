---
type: source
subject: "GitHub source repos/karpathy/minGPT/projects/chargpt/readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minGPT/projects/chargpt/readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/minGPT/projects/chargpt/readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minGPT/projects/chargpt/readme.md), SHA-256 `569745d5ae468101cdb1f9387352f8b90b1381c2dac5e08c3ac6e78a6cedbf90`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# chargpt chargpt trains a character-level language model. We support three settings: 1 convenience setting
```

Llm.c script documentation preserves comparable effective batch sizes across GPU counts while trading recomputation and microbatch size against memory and runtime; the reference scripts explicitly omit checkpoints, Hellaswag and resume. MatlabWrapper favors reuse and an interactive debugging bridge instead of reimplementing k-means, and first asks users to establish the official engine demo before wrapper-specific diagnosis. MinGPT project readmes label addition and character modeling examples, with text8/enwik8 still TODO. Nanochat covers tokenization through chat inference, uses a depth dial for principled scaling, measures bits per byte against steps/time/FLOPs together with CORE and throughput, and requires candidate changes to work across depths. It acknowledges unexercised device paths, CPU capability limits, explicit dtype choices, incomplete fp16 RL support, and AI-contribution disclosure when authors do not fully understand code. Captured price/leaderboard/hardware claims are dated results, not reruns. NanoGPT dataset readmes report token/split counts and provenance without turning training data into Karpathy beliefs; neuraltalk folder readmes separate data and checkpoints from code.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# chargpt

chargpt trains a character-level language model.

We support three settings: 1 convenience setting and 2 "benchmark" settings that have acedemic literature results:

- a user specified `input.txt` file that we train an LM on (e.g. get tiny-shakespear (1.1MB of data) [here](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt))
- TODO [text8](http://mattmahoney.net/dc/textdata.html): also derived from Wikipedia text but all XML is removed and is lowercased to only 26 characters of
- TODO [enwik8](http://prize.hutter1.net) benchmark ("Hutter Prize"), first 100M bytes of a Wikipedia XML dump, with 205 unique tokensEnglish plus spaces

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
