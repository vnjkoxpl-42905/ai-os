---
type: source
subject: "GitHub source repos/karpathy/char-rnn/model/RNN.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/model/RNN.lua]
semantic-status: complete-named-text-read
---

# repos/karpathy/char-rnn/model/RNN.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/model/RNN.lua), SHA-256 `19b80484d21b9a08be88185402e9156979a58101e0d9ce398e53412655682c50`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
local RNN = {} function RNN.rnn(input_size, rnn_size, n, dropout) -- there are n+1 inputs (hiddens
```

Calorie is a simple in-memory personal counter with fixed resting-burn and target-deficit assumptions; it offers no persistence or individualized medical validation. Char-rnn defines explicit recurrent, GRU and LSTM timestep graphs with dropout between layers and a log-softmax decoder. Inspection prints checkpoint options and validation losses; GPU conversion is explicitly a temporary patch. Sampling credits the Oxford practical, initializes recurrent state, supports seeded prompts, temperature or argmax, evaluates dropout mode and prints CPU fallback warnings when GPU libraries are unavailable. Checkpoint/device compatibility is warned about rather than automatically guaranteed; no model execution occurred.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
local RNN = {}

function RNN.rnn(input_size, rnn_size, n, dropout)
  
  -- there are n+1 inputs (hiddens on each layer and x)
  local inputs = {}
  table.insert(inputs, nn.Identity()()) -- x
  for L = 1,n do
    table.insert(inputs, nn.Identity()()) -- prev_h[L]

  end

  local x, input_size_L
  local outputs = {}
  for L = 1,n do
    
    local prev_h = inputs[L+1]
    if L == 1 then 
      x = OneHot(input_size)(inputs[1])
      input_size_L = input_size
    else 
      x = outputs[(L-1)] 
      if dropout > 0 then x = nn.Dropout(dropout)(x) end -- apply dropout, if any
      input_size_L = rnn_size
    end

    -- RNN tick
    local i2h = nn.Linear(input_size_L, rnn_size)(x)
    local h2h = nn.Linear(rnn_size, rnn_size)(prev_h)
    local next_h = nn.Tanh()(nn.CAddTable(){i2h, h2h})

    table.insert(outputs, next_h)
  end
-- set up the decoder
  local top_h = outputs[#outputs]
  if dropout > 0 then top_h = nn.Dropout(dropout)(top_h) end
  local proj = nn.Linear(rnn_size, input_size)(top_h)
  local logsoft = nn.LogSoftMax()(proj)
  table.insert(outputs, logsoft)

  return nn.gModule(inputs, outputs)
end

return RNN

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
