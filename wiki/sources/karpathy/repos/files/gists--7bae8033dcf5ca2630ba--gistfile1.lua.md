---
type: source
subject: "GitHub source gists/7bae8033dcf5ca2630ba/gistfile1.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/gists/7bae8033dcf5ca2630ba/gistfile1.lua]
semantic-status: complete-named-text-read
---

# gists/7bae8033dcf5ca2630ba/gistfile1.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/gists/7bae8033dcf5ca2630ba/gistfile1.lua), SHA-256 `a32c8691d908a4bd4d3945cb9de3272445597229fa8f109cd23c50ea86d3c246`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "--\[\[ Efficient LSTM in Torch using nngraph library. This code was optimized by Justin Johnson".

The batched NumPy LSTM gist implements explicit gate/cell forward and backward passes, compares sequential and batched computations, and numerically checks every gradient with central differences. Its Python2 syntax and integer-division assumptions are historical; a forget-gate comment conflicts with the positive bias assigned, so inspect code rather than inherit the comment. The NES gist shows a fixed-variance Gaussian population, standardized rewards and a noise-weighted parameter update against a known toy target; printed convergence is a captured example, not a rerun. The Torch fast-LSTM gist explicitly credits Justin Johnson for optimization and batches gate matrix operations; do not count it as an independent Karpathy invention. MicroGPT contains dependency-free scalar autograd, character tokenization, a one-layer cached causal transformer, stable softmax, RMS normalization, Adam and generation in one file; its names dataset and educational scale do not demonstrate production quality or human identity knowledge. The CSS gist changes historical Google Slides speaker-note geometry; it has no broad engineering-rule evidence.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
--[[ 
Efficient LSTM in Torch using nngraph library. This code was optimized 
by Justin Johnson (@jcjohnson) based on the trick of batching up the 
LSTM GEMMs, as also seen in my efficient Python LSTM gist.
--]]

function LSTM.fast_lstm(input_size, rnn_size)
  local x = nn.Identity()()
  local prev_c = nn.Identity()()
  local prev_h = nn.Identity()()

  local i2h = nn.Linear(input_size, 4 * rnn_size)(x)
  local h2h = nn.Linear(rnn_size, 4 * rnn_size)(prev_h)
  local all_input_sums = nn.CAddTable()({i2h, h2h})

  local sigmoid_chunk = nn.Narrow(2, 1, 3 * rnn_size)(all_input_sums)
  sigmoid_chunk = nn.Sigmoid()(sigmoid_chunk)
  local in_gate = nn.Narrow(2, 1, rnn_size)(sigmoid_chunk)
  local forget_gate = nn.Narrow(2, rnn_size + 1, rnn_size)(sigmoid_chunk)
  local out_gate = nn.Narrow(2, 2 * rnn_size + 1, rnn_size)(sigmoid_chunk)

  local in_transform = nn.Narrow(2, 3 * rnn_size + 1, rnn_size)(all_input_sums)
  in_transform = nn.Tanh()(in_transform)

  local next_c           = nn.CAddTable()({
      nn.CMulTable()({forget_gate, prev_c}),
      nn.CMulTable()({in_gate,     in_transform})
    })
  local next_h           = nn.CMulTable()({out_gate, nn.Tanh()(next_c)})

  return nn.gModule({x, prev_c, prev_h}, {next_c, next_h})
end
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
