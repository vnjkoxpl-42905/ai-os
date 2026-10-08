---
type: source
subject: "llm.c / llmc/logger.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/logger.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.246334Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/logger.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `6e676657b697da1358e259d7f40743aae9419886bf887fab0b9b0aa9f6b79c91`

## What the complete source contains

Evidence: `only rank 0 writes logs` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/logger.h)). The logger activates only for rank zero with an output directory and clears main.log for a fresh non-resumed run.

Evidence: `fopenCheck(logger->output_log_file, "a")` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/logger.h)). Evaluation, validation loss, training loss, learning rate and gradient norm are appended in line-oriented records. It reopens and closes the file for each event.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
