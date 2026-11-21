---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c
---

# repos/karpathy/llama2.c/runq.c

Original: [captured source](https://github.com/karpathy/llama2.c). Capture: 2026-10-08T09:34:45.012275Z. Classification: `authored_code`.

[Physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c). SHA-256: `ba9cc681afca79f994f815dfeffc4a61c5b3ca8c5d4d4dcb75c8d375856ba548`.

## Source account

```text
int8 quantized forward pass.
```

Pure-C Llama-2 inference maps version-two quantized checkpoints, keeps RMSNorm weights in float, dequantizes token embeddings, and performs groupwise int8 activation/weight products with int32 accumulation and float scales. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c).

```text
int num_groups = n / GS;
```

Quantization uses maximum absolute value divided by 127 in each group; dimensions must fit group partitions. All-zero groups have no explicit zero-scale guard, and checkpoint group size/configuration is trusted rather than fully validated. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c).

```text
RoPE relative positional encoding: complex-valued rotate q and k in each head
```

Forward inference implements RMSNorm, rotary Q/K encoding, grouped/multiquery KV-cache attention, residual branches and SwiGLU, parallelizing matrix rows and attention heads with OpenMP. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c).

```text
merge the best consecutive pair each iteration, according the scores in vocab_scores
```

Tokenizer loads scored vocabulary, builds a sorted lookup, handles UTF-8/byte fallback, and merges highest-scoring adjacent pieces. Sampling supports greedy, temperature/multinomial and top-p with xorshift randomness. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c).

```text
is not safely implemented, it's more a proof of concept atm.
```

Generation forces prompt tokens before sampling and reports measured token throughput when run. Chat uses fixed buffers and unbounded strcpy/sprintf; the source explicitly calls it an incompletely tested proof of concept. This archived source was not compiled or executed. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/runq.c).

## Limits

All 43353 decoded UTF-8 characters read through EOF in contiguous bounded chunks. Historical educational implementation, not runtime proof or a secure checkpoint/chat parser. Raw unchanged. No new persona rule promoted by this compilation.
