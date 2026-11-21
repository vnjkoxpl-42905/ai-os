---
type: source
subject: "GitHub source repos/karpathy/char-rnn/inspect_checkpoint.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/inspect_checkpoint.lua]
semantic-status: complete-named-text-read
---

# repos/karpathy/char-rnn/inspect_checkpoint.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/inspect_checkpoint.lua), SHA-256 `e82a1b3b5138f635a650c501d8f9fb7e0bb05b9b2563faad673e17637bc3a6dc`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
-- simple script that loads a checkpoint and prints its opts require 'torch' require 'nn'
```

Calorie is a simple in-memory personal counter with fixed resting-burn and target-deficit assumptions; it offers no persistence or individualized medical validation. Char-rnn defines explicit recurrent, GRU and LSTM timestep graphs with dropout between layers and a log-softmax decoder. Inspection prints checkpoint options and validation losses; GPU conversion is explicitly a temporary patch. Sampling credits the Oxford practical, initializes recurrent state, supports seeded prompts, temperature or argmax, evaluates dropout mode and prints CPU fallback warnings when GPU libraries are unavailable. Checkpoint/device compatibility is warned about rather than automatically guaranteed; no model execution occurred.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
-- simple script that loads a checkpoint and prints its opts

require 'torch'
require 'nn'
require 'nngraph'

require 'util.OneHot'
require 'util.misc'

cmd = torch.CmdLine()
cmd:text()
cmd:text('Load a checkpoint and print its options and validation losses.')
cmd:text()
cmd:text('Options')
cmd:argument('-model','model to load')
cmd:option('-gpuid',0,'gpu to use')
cmd:option('-opencl',0,'use OpenCL (instead of CUDA)')
cmd:text()

-- parse input params
opt = cmd:parse(arg)

if opt.gpuid >= 0 and opt.opencl == 0 then
    print('using CUDA on GPU ' .. opt.gpuid .. '...')
    require 'cutorch'
    require 'cunn'
    cutorch.setDevice(opt.gpuid + 1)
end

if opt.gpuid >= 0 and opt.opencl == 1 then
    print('using OpenCL on GPU ' .. opt.gpuid .. '...')
    require 'cltorch'
    require 'clnn'
    cltorch.setDevice(opt.gpuid + 1)
end

local model = torch.load(opt.model)

print('opt:')
print(model.opt)
print('val losses:')
print(model.val_losses)


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
