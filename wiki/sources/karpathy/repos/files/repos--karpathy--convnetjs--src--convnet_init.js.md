---
type: source
subject: "GitHub source repos/karpathy/convnetjs/src/convnet_init.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/src/convnet_init.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/src/convnet_init.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/src/convnet_init.js), SHA-256 `fb552bc6520d485f331dc2ebcb90b679ee915f886790d221376a494b33de9e2b`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
var convnetjs = convnetjs || { REVISION: 'ALPHA' };
```

Convnet dot-product layers implement convolution weight sharing and dense connectivity explicitly, with chain-rule data/weight gradients, JSON serialization and separate bias decay. Optimized convolution credits mdda and acknowledges direct-array speed versus modularity tradeoffs. Dropout openly calls itself inefficient and distinguishes training from prediction; prediction multiplies by drop probability rather than retention probability, equivalent only at the default half, so general correctness is not claimed. Input is an identity layer and export supports browser or Node. Speedtest times a declared forward-only convolution; trainer prose is personal historical experience qualified by tuning, not a verified universal ranking.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
var convnetjs = convnetjs || { REVISION: 'ALPHA' };

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
