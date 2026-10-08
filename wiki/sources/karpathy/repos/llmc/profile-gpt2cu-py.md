---
type: source
subject: "llm.c / profile_gpt2cu.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: profile_gpt2cu.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.704936Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/profile_gpt2cu.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `ba480446d3916eebc89816dd717b7e2eb512f1123ebc48de2d41b81eb47718bb`

## What the complete source contains

Evidence: `N_LAYERS = 12` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/profile_gpt2cu.py)). The script builds and profiles the one-layer CUDA harness, imports Nsight CSV metrics, and extrapolates repeating forward/backward kernels to a twelve-layer model while counting encoder/classifier/optimizer once.

Evidence: `Assuming that every kernel should be either fully DRAM bandwidth or tensor core limited` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/profile_gpt2cu.py)). Its efficiency report rests on an explicit bandwidth-or-tensor-bound assumption and observed maxima within that profile. It groups kernels and prints per-phase time, memory traffic and instructions; Linux modprobe/sudo and fixed CSV-column assumptions were not exercised here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
