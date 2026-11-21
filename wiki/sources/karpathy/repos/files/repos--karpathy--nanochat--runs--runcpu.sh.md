---
type: source
subject: "GitHub source repos/karpathy/nanochat/runs/runcpu.sh"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/runs/runcpu.sh]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/runs/runcpu.sh

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/runs/runcpu.sh), SHA-256 `68bcbc16f3c2024cba6344a44d8c09f002d001a3ddcbe96b8027d1fe61a1d4ea`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
#!/bin/bash # Showing an example run for exercising some of the code paths on the
```

Tokenizer trains with rustbpe and infers with tiktoken, explicitly narrows numeric chunks to two digits for its 32K vocabulary, preserves reserved conversation/tool delimiters and supervises assistant text/tool calls while masking user and actual tool-output tokens. Role alternation assumptions are asserted and original conversations deep-copied before surgery; colored token/mask visualization exposes training data. Truncation may cut messages and pickle loading requires trusted artifacts. Miniseries sweeps model depth and OOM-aware device batch sizes, records CSV/log provenance, but hardcodes tokens per step despite automatic batch scaling and does not enable pipefail, so results need validation. CPU run explicitly promises an educational weak model and hardware-specific historical timings rather than useful full-scale training.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
#!/bin/bash

# Showing an example run for exercising some of the code paths on the CPU (or MPS on Macbooks)
# This script was last updated/tuned on Jan 17, 2026.

# Run as:
# bash runs/runcpu.sh

# NOTE: Training LLMs requires GPU compute and $$$. You will not get far on your Macbook.
# Think of this run as educational/fun demo, not something you should expect to work well.
# You may also want to run this script manually and one by one, copy pasting commands into your terminal.

# all the setup stuff
export NANOCHAT_BASE_DIR="$HOME/.cache/nanochat"
mkdir -p $NANOCHAT_BASE_DIR
command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
[ -d ".venv" ] || uv venv
uv sync --extra cpu
source .venv/bin/activate
if [ -z "$WANDB_RUN" ]; then
    WANDB_RUN=dummy
fi

# train tokenizer on ~2B characters (~34 seconds on my MacBook Pro M3 Max)
python -m nanochat.dataset -n 8
python -m scripts.tok_train --max-chars=2000000000
python -m scripts.tok_eval

# train a small 6 layer model
# I tuned this run to complete in about 30 minutes on my MacBook Pro M3 Max.
# To get better results, try increasing num_iterations, or get other ideas from your favorite LLM.
python -m scripts.base_train \
    --depth=6 \
    --head-dim=64 \
    --window-pattern=L \
    --max-seq-len=512 \
    --device-batch-size=32 \
    --total-batch-size=16384 \
    --eval-every=100 \
    --eval-tokens=524288 \
    --core-metric-every=-1 \
    --sample-every=100 \
    --num-iterations=5000 \
    --run=$WANDB_RUN
python -m scripts.base_eval --device-batch-size=1 --split-tokens=16384 --max-per-task=16

# SFT (~10 minutes on my MacBook Pro M3 Max)
python -m scripts.chat_sft \
    --eval-every=200 \
    --eval-tokens=524288 \
    --num-iterations=1500 \
    --run=$WANDB_RUN

# Chat with the model over CLI
# The model should be able to say that it is Paris.
# It might even know that the color of the sky is blue.
# Sometimes the model likes it if you first say Hi before you ask it questions.
# python -m scripts.chat_cli -p "What is the capital of France?"

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
