---
type: source
subject: "llm.c / .github/workflows/ci_tests.yml"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: .github/workflows/ci_tests.yml

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.788310Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci_tests.yml) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `89b13eca8fdb9214af0be51565aab7d0240aefbaca858f548b37fbbe203cfca9`

## What the complete source contains

Evidence: `fsanitize=address` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci_tests.yml)). The dataloader job runs a normal and AddressSanitizer build on Ubuntu.

Evidence: `retention-days: 30` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci_tests.yml)). A second job produces and uploads PTX/SASS assembly artifacts for default, A100 and H100 targets. Those definitions make kernels inspectable but no emitted artifacts or passing logs were reviewed here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
