---
type: source
subject: "GitHub source repos/karpathy/char-rnn/convert_gpu_cpu_checkpoint.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/convert_gpu_cpu_checkpoint.lua]
semantic-status: complete-named-text-read
---

# repos/karpathy/char-rnn/convert_gpu_cpu_checkpoint.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/convert_gpu_cpu_checkpoint.lua), SHA-256 `b8386f67d3b905237f07f96793edcec963359265813e214bf97f99c293177e7c`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "--\\[\\[ A quick patch for converting GPU checkpoints to CPU checkpoints until I implement a".

Calorie is a simple in-memory personal counter with fixed resting-burn and target-deficit assumptions; it offers no persistence or individualized medical validation. Char-rnn defines explicit recurrent, GRU and LSTM timestep graphs with dropout between layers and a log-softmax decoder. Inspection prints checkpoint options and validation losses; GPU conversion is explicitly a temporary patch. Sampling credits the Oxford practical, initializes recurrent state, supports seeded prompts, temperature or argmax, evaluates dropout mode and prints CPU fallback warnings when GPU libraries are unavailable. Checkpoint/device compatibility is warned about rather than automatically guaranteed; no model execution occurred.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
--[[
A quick patch for converting GPU checkpoints to 
CPU checkpoints until I implement a more long-term
solution. Takes the path to the model and creates
a file in the same location and path, but with _cpu.t7
appended.
]]--

require 'torch'
require 'nn'
require 'nngraph'
require 'lfs'

require 'util.OneHot'
require 'util.misc'

cmd = torch.CmdLine()
cmd:text()
cmd:text('Sample from a character-level language model')
cmd:text()
cmd:text('Options')
cmd:argument('-model','GPU model checkpoint to convert')
cmd:option('-gpuid',0,'which gpu to use. -1 = use CPU')
cmd:option('-opencl',0,'use OpenCL (instead of CUDA)')
cmd:text()

-- parse input params
opt = cmd:parse(arg)

-- check that cunn/cutorch are installed if user wants to use the GPU
if opt.gpuid >= 0 and opt.opencl == 0 then
    local ok, cunn = pcall(require, 'cunn')
    local ok2, cutorch = pcall(require, 'cutorch')
    if not ok then print('package cunn not found!') end
    if not ok2 then print('package cutorch not found!') end
    if ok and ok2 then
        print('using CUDA on GPU ' .. opt.gpuid .. '...')
        cutorch.setDevice(opt.gpuid + 1) -- note +1 to make it 0 indexed! sigh lua
    else
    	print('Error, no GPU available?')
        os.exit()
    end
end

-- check that clnn/cltorch are installed if user wants to use OpenCL
if opt.gpuid >= 0 and opt.opencl == 1 then
    local ok, cunn = pcall(require, 'clnn')
    local ok2, cutorch = pcall(require, 'cltorch')
    if not ok then print('package clnn not found!') end
    if not ok2 then print('package cltorch not found!') end
    if ok and ok2 then
        print('using OpenCL on GPU ' .. opt.gpuid .. '...')
        cltorch.setDevice(opt.gpuid + 1) -- note +1 to make it 0 indexed! sigh lua
    else
        print('Error, no GPU available?')
        os.exit()
    end
end

print('loading ' .. opt.model)
checkpoint = torch.load(opt.model)
protos = checkpoint.protos

-- convert the networks to be CPU models
for k,v in pairs(protos) do
	print('converting ' .. k .. ' to CPU')
	protos[k]:double()
end

local savefile = opt.model .. '_cpu.t7' -- append "cpu.t7" to filename
torch.save(savefile, checkpoint)
print('saved ' .. savefile)



```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
