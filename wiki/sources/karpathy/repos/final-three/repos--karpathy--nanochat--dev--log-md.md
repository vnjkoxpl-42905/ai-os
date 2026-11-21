---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md
---

# repos/karpathy/nanochat/dev/LOG.md

Original: [captured source](https://github.com/karpathy/nanochat). Capture: 2026-10-08T09:35:02.369364Z. Classification: `authored_experiment_record`.

[Physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md). SHA-256: `a21cad0c01d21eded600f94cec307a1c5a8ee28d4ff069036f887dc918cc83d6`.

## Source account

```text
wall clock time to capability
```

Dated experiment log prioritizes capability reached per wall-clock time over isolated per-step or kernel improvements, documenting rejected DyT, parameter-golf tweaks, MoE, SwiGLU, Hyperball, multi-token prediction, clipping and several pretraining mixtures. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md).

```text
Don't over-tune on small proxies.
```

Optimizer sweeps explicitly found small-scale improvements did not transfer to target scale. Microbenchmark gains also disappeared in full training; conclusions are bounded by the tested model/data/hardware. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md).

```text
Removed bigram embeddings (engram-lite) from the codebase.
```

January 27 records successful bigram embeddings and a new default; January 28 reverses it after larger-scale wall-clock/VRAM assessment. Retain chronology instead of promoting the earlier result as the final recommendation. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md).

```text
the actual speedup (when you match performance) is closer to 5%
```

February FP8 tensorwise throughput gain of 17% became about 5% after matching capability. January lm_head-only FP8 was a negative result despite faster microbenchmarks. Claims remain author-reported experiments, not new measurements. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md).

```text
sixth attempt at beating FineWeb-EDU on CORE score
```

March 4 reports ClimbMix succeeding after earlier dataset failures, improving the GPT-2 speedrun from 2h46m to 2h1m and permitting a smaller model. The same date records explicit dtype management and fp16 GradScaler; this is dated source history, not verified current installed behavior. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md).

```text
makes all previous experiments not comparable in absolute value of the loss
```

BOS-aligned best-fit cropping trades discarded document tails for fully utilized/context-aligned batches and changes validation-loss scale, so before/after absolute losses cannot be compared directly. Other accepted changes include value embeddings, residual scalars, attention fallback/windowing, optimizer refinements and batch scaling. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/LOG.md).

## Limits

All 63218 decoded UTF-8 characters read through EOF in seven contiguous bounded reads. Reported experiments not rerun. Recommendations and negative results are specific to dates, tested scale, data and hardware. Some entries describe private branches or later reversals; do not silently blend them into current settings. Raw unchanged. No new persona rule promoted by this compilation.
