---
type: source
subject: "GitHub source repos/karpathy/char-rnn/util/misc.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/util/misc.lua]
semantic-status: complete-named-text-read
---

# repos/karpathy/char-rnn/util/misc.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/util/misc.lua), SHA-256 `9264f6661e393ddb74e25ab024d34ad62f984adc65496a53fd29b51bebc1f5a5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "-- misc utilities function clone_list(tensor_list, zero_too) -- utility function. todo: move away to some utils".

Char-rnn training preserves its credited Torch lineage, checks checkpoint vocabulary and overwrites architecture settings for compatibility, initializes forget gates positively, unrolls shared-weight timestep clones and clips gradients. It separates dropout training/evaluation modes, logs validation losses and stops on NaN or exploding loss with a request for environment details. Optional synchronization explicitly trades timing accuracy for overhead. Minibatch preprocessing detects stale caches, trims tails to divisibility, sorts vocabulary deterministically and rejects empty splits. Its cache-existence condition uses OR and can miss a single absent cache; full checkpoint optimizer/RNG resume is not established. Helpers were read in full without execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

-- misc utilities

function clone_list(tensor_list, zero_too)
    -- utility function. todo: move away to some utils file?
    -- takes a list of tensors and returns a list of cloned tensors
    local out = {}
    for k,v in pairs(tensor_list) do
        out[k] = v:clone()
        if zero_too then out[k]:zero() end
    end
    return out
end
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
