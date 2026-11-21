---
type: source
subject: "llm.c / scripts/multi_node/run_gpt2_124M_mpi.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: scripts/multi_node/run_gpt2_124M_mpi.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.340775Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_mpi.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c616810d0dad825adcbb494a902318e0b0dcd666e2cf26a74be33a3d810bac95`

## What the complete source contains

Evidence: `mpirun -np 16 --host $host1:8,$host2:8` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_mpi.sh)). The MPI variant launches sixteen ranks across two configured hosts.

Evidence: `-pi "mpi"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/multi_node/run_gpt2_124M_mpi.sh)). It uses MPI initialization, sets FineWeb train/validation paths and network variables, copies the binary to the worker, and disables resume in this recipe.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
