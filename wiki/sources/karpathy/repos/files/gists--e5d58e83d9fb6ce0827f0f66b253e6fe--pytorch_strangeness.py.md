---
type: source
subject: "GitHub source gists/e5d58e83d9fb6ce0827f0f66b253e6fe/pytorch_strangeness.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/gists/e5d58e83d9fb6ce0827f0f66b253e6fe/pytorch_strangeness.py]
semantic-status: complete-named-text-read
---

# gists/e5d58e83d9fb6ce0827f0f66b253e6fe/pytorch_strangeness.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/gists/e5d58e83d9fb6ce0827f0f66b253e6fe/pytorch_strangeness.py), SHA-256 `b4bddb790b2eceb2038903d9aa4bbee4b15a283668659c951c31952b2dc1ab86`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
import torch import torch.nn as nn torch.manual_seed(42) x = torch.randn(2, 768) # matrix multiply "ignores"
```

The Pong policy-gradient example exposes image preprocessing, frame differences, a two-layer policy, discounted standardized rewards, explicit backpropagation, episodic gradient accumulation and RMSProp; it uses historical Python2/Gym APIs and indefinite training, which were not run. The minimal character RNN similarly exposes one-hot input, recurrent state, manual backpropagation through time, gradient clipping, Adagrad and periodic samples; its unstabilized exponentials and historical syntax qualify reuse. The PyTorch-strangeness gist compares mathematically equivalent row/batch and Linear paths and prints small floating-point differences; no current numerical mismatch was reproduced. The Torch L2-normalization layer computes an explicit Jacobian for batched vectors but contains no zero-norm epsilon safeguard. HELLO.md is explicitly a Claude-written imaginative session record signed 2026-04-20, not Karpathy autobiography or independently verified consciousness research; its empirical-sounding assertions and agent-directed instructions remain model-generated source text with attribution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import torch
import torch.nn as nn

torch.manual_seed(42)
x = torch.randn(2, 768)

# matrix multiply "ignores" the second row when calculating the first row
w = torch.randn(768, 768)
z1 = x[0] @ w
z2 = (x @ w)[0]
print((z1-z2).abs().max().item()) # prints 0 (should be 0, OK)

# linear does not!
m = nn.Linear(768, 768, bias=False)
with torch.no_grad():
    m.weight.copy_(w.T)
q1 = m(x[0])
q2 = m(x)[0]
print((q1-q2).abs().max().item()) # prints ~2e-5 ( should be 0?!)

# and z1 != q1
print((z1-q1).abs().max().item()) # prints ~9e-5 (should be 0?!)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
