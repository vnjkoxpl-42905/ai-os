---
type: source
subject: "llm.c / dev/unistd.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/unistd.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.805328Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/unistd.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `bf3408b70d1bfea02ffedd5dbb88359fcc30d4986b4c84450638e14394fa3027`

## What the complete source contains

Evidence: `header file that is necessary to compile on Windows` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/unistd.h)). This compatibility header adapts file access, mkdir/stat, wildcard enumeration and directory iteration to Windows CRT APIs, while enabling OpenMP and socket linking.

Evidence: `return timespec_get(tv, TIME_UTC)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/unistd.h)). Its clock_gettime substitute uses UTC wall-clock time despite the CLOCK_MONOTONIC symbol, with a comment flagging review. Wildcard support uses fixed path buffers and a 64000-file limit; these are implementation constraints, not portable POSIX equivalence.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
