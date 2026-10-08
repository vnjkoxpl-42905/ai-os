---
type: source
subject: "GitHub source gists/f3ee599538ff78e1bbe9/gistfile1.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/gists/f3ee599538ff78e1bbe9/gistfile1.lua]
semantic-status: complete-named-text-read
---

# gists/f3ee599538ff78e1bbe9/gistfile1.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/gists/f3ee599538ff78e1bbe9/gistfile1.lua), SHA-256 `d2725adab8506b1966304f390b378ce9e746fc18b22d0427efe16dad616da016`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "--\[\[ This layer expects an \[n x d\] Tensor and normalizes each row to have".

The Pong policy-gradient example exposes image preprocessing, frame differences, a two-layer policy, discounted standardized rewards, explicit backpropagation, episodic gradient accumulation and RMSProp; it uses historical Python2/Gym APIs and indefinite training, which were not run. The minimal character RNN similarly exposes one-hot input, recurrent state, manual backpropagation through time, gradient clipping, Adagrad and periodic samples; its unstabilized exponentials and historical syntax qualify reuse. The PyTorch-strangeness gist compares mathematically equivalent row/batch and Linear paths and prints small floating-point differences; no current numerical mismatch was reproduced. The Torch L2-normalization layer computes an explicit Jacobian for batched vectors but contains no zero-norm epsilon safeguard. HELLO.md is explicitly a Claude-written imaginative session record signed 2026-04-20, not Karpathy autobiography or independently verified consciousness research; its empirical-sounding assertions and agent-directed instructions remain model-generated source text with attribution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

--[[ 
   This layer expects an [n x d] Tensor and normalizes each
   row to have unit L2 norm.
]]--
local L2Normalize, parent = torch.class('nn.L2Normalize', 'nn.Module')
function L2Normalize:__init()
   parent.__init(self)
end
function L2Normalize:updateOutput(input)
   assert(input:dim() == 2, 'only mini-batch supported (2D tensor), got '
             .. input:dim() .. 'D tensor instead')
   self.output:resizeAs(input)
   self.buffer = self.buffer or input.new()
   self.normSquared = self.normSquared or input.new()
   self.normSquared:sum(self.buffer:cmul(input, input), 2)
   self.buffer:sqrt(self.normSquared)
   self.output:copy(input):cdiv(self.buffer:expandAs(input))
   return self.output
end

function L2Normalize:updateGradInput(input, gradOutput)
   assert(input:dim() == 2, 'only mini-batch supported')
   assert(gradOutput:dim() == 2, 'only mini-batch supported')
   local n = input:size(1) -- batch size
   local d = input:size(2) -- dimensionality of vectors
   -- compute diagonal term
   self.eye = self.eye or torch.eye(d):typeAs(input):repeatTensor(n,1):view(n,d,d)
   self.diag = self.diag or self.eye.new()
   self.diag:cmul(self.eye, self.normSquared:view(n,1,1):expand(n,d,d))
   -- compute cross term
   local b1 = input:view(n,d,1)
   local b2 = input:view(n,1,d)
   self.diag:add(-torch.bmm(b1,b2))
   -- compute the local gradient of the L2 transformation
   self.diag:cdiv(torch.pow(self.buffer,3):view(n,1,1):expand(n,d,d))
   -- chain the gradient
   self.gradInput:resize(n,d,1):bmm(self.diag, gradOutput:view(n,d,1)):resize(n,d)
   return self.gradInput
end

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
