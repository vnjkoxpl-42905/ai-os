---
type: source
subject: "llm.c / scripts/multi_node/run_gpt2_124M_fs.sbatch"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: scripts/multi_node/run_gpt2_124M_fs.sbatch

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.335247Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_fs.sbatch) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `4da91cdfbec02904435b466f1facbf932c980514cccb64d0ad8bd7a7da90535d`

## What the complete source contains

Evidence: `-pi "fs"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_fs.sbatch)). This SLURM recipe configures two nodes and sixteen tasks, selecting a shared-filesystem initialization path.

Evidence: `needs to be a shared filesystem path that all nodes can access` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_fs.sbatch)). It requires a filesystem visible to every node and supplies rank/process counts from SLURM, with environment-specific binary, data and network settings.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
