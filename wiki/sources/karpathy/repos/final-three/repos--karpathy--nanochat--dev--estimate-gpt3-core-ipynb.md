---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb
---

# repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb

Original: [captured source](https://github.com/karpathy/nanochat). Capture: 2026-10-08T09:35:02.356706Z. Classification: `joint_authored_notebook_with_generated_tables`.

[Physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb). SHA-256: `4ab4018530098ba1d512902713570c976cacb33fa61a1761849c2733b78695dd`.

## Source account

```text
**Authors**: Claude Code Opus 4.5, Andrej Karpathy
```

Jointly attributed notebook estimates historical GPT-3 CORE scores using GPT-2 calibration because GPT-3 models were not available for direct evaluation. Its methodology is evidence of this analysis, not solely Karpathy-authored prose. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb).

```text
We only have 4 calibration points
```

Uses four GPT-2 calibration models and six overlapping tasks, centered against guessing baselines, to fit simple averaging, ridge regression and a PIQA proxy. Few-shot counts and evaluation methods differ; calibration size is small. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb).

```text
Averaging the Simple and Ridge approaches for final estimates
```

Averages linear and ridge predictions for eight GPT-3 model sizes, reporting approximately 0.1484 for 125M through 0.4272 for 175B. These are regression estimates, not direct measured CORE outcomes. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb).

```text
These are estimates
```

Explicit caveats include limited calibration, imperfect six-to-22-task representation and evaluation differences. Strong calibration R-squared is in-sample, not established out-of-family validation. Captured prose mentions unregularized weights +18/-22, while the adjacent displayed table shows about +6.55/-8.03; preserve this inconsistency. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/dev/estimate_gpt3_core.ipynb).

## Limits

All 38 cells, authored source and stream/text/plain outputs read through EOF in a 29154-character extraction. Entire JSON and generated HTML tables parsed deterministically; HTML markup/CSS is not claimed as a semantic full model read. No images present. Notebook not rerun; external paper measurements not independently reverified. Raw unchanged. No new persona rule promoted by this compilation.
