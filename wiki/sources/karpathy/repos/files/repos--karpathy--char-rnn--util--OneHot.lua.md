---
type: source
subject: "GitHub source repos/karpathy/char-rnn/util/OneHot.lua"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/util/OneHot.lua]
semantic-status: complete-named-text-read
---

# repos/karpathy/char-rnn/util/OneHot.lua

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/char-rnn/util/OneHot.lua), SHA-256 `fdd20fd9942a87cd50ff3048a89fbc02e95de6b04c97e8638bbec59fac8535e4`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "local OneHot, parent = torch.class('OneHot', 'nn.Module') function OneHot:__init(outputSize) parent.__init(self) self.outputSize = outputSize -- We'll construct".

Char-rnn utilities explicitly credit adapted parameter flattening code and preserve shared storage across timestep clones; OneHot caches the identity matrix. Convnet build concatenates a declared layer order and minifies via YUI. Autoencoder demo explains a bottleneck as the mechanism forcing useful compressed representations and exposes live loss, neurons and snapshots. MagicNet demo explicitly states CSV assumptions, separates training/validation/test roles, cross-validates architectures and ensembles selected models, with export/import. The explanatory demos support interactive inspection and held-out evaluation; external datasets and borrowed utilities are not independently authored philosophy, and no browser training was performed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

local OneHot, parent = torch.class('OneHot', 'nn.Module')

function OneHot:__init(outputSize)
  parent.__init(self)
  self.outputSize = outputSize
  -- We'll construct one-hot encodings by using the index method to
  -- reshuffle the rows of an identity matrix. To avoid recreating
  -- it every iteration we'll cache it.
  self._eye = torch.eye(outputSize)
end

function OneHot:updateOutput(input)
  self.output:resize(input:size(1), self.outputSize):zero()
  if self._eye == nil then self._eye = torch.eye(self.outputSize) end
  self._eye = self._eye:float()
  local longInput = input:long()
  self.output:copy(self._eye:index(1, longInput))
  return self.output
end

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
