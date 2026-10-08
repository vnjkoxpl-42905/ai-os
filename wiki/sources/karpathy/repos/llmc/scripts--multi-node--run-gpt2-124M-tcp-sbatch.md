---
type: source
subject: "llm.c / scripts/multi_node/run_gpt2_124M_tcp.sbatch"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: scripts/multi_node/run_gpt2_124M_tcp.sbatch

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.345297Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_tcp.sbatch) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `789e8141c9c7346d423ef6b0dbdd7f24981c0d56acb0e4187a04067c4ffdf8da`

## What the complete source contains

Evidence: `-pi "tcp"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_tcp.sbatch)). The two-node SLURM launch uses TCP initialization and a configurable process-zero server address.

Evidence: `Did you forget to run with sbatch? Aborting.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_tcp.sbatch)). It rejects a missing SLURM job ID, copies binaries to other hosts if needed, and configures NCCL networking. Paths, network interface and IP are examples to replace, not Joshua configuration.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
