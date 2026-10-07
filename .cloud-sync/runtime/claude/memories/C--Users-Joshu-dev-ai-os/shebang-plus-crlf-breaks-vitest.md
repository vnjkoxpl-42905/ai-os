---
name: shebang-plus-crlf-breaks-vitest
description: "A scripts/*.mjs with a shebang AND CRLF cannot be imported by a vitest test, and the error points at the wrong file."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9a2e34c3-6cc3-41c2-b75a-b0b02f16c2dc
  modified: 2026-09-09T21:55:19.936Z
---

A `.mjs` under `scripts/` that starts with `#!/usr/bin/env node` **and** has CRLF line
endings cannot be imported by a vitest test. It fails with `SyntaxError: Invalid or
unexpected token` reported against **line 4 of the importing test file** — a comment line,
nowhere near the actual problem.

This silently skipped all 17 tests in `src/lib/__tests__/questionStatsBuilder.test.ts` on
`main`. An earlier investigation cleared that file and was correct to: it was
byte-identical to origin/main, valid UTF-8, and `node --check` passed on both imports.

**Why:** both halves are required. Isolated 2026-09-09 one variable at a time — CRLF on
the test file alone passes; CRLF on `scripts/knowledge/build-question-stats.mjs` alone
fails; the same CRLF file with its shebang removed passes. That is why 1,796 CRLF files
under `src/` are harmless: nothing strips a shebang from them.

**How to apply:** when a vitest suite fails to load with a syntax error at a position that
makes no sense, check the line endings of what it imports, not the file named. `git
status` will not help — `core.autocrlf=input` normalises on add, so a CRLF working copy
reads as clean. `.gitattributes` pins `scripts/**` to LF and
`src/lib/__tests__/lineEndings.test.ts` fails loudly if one appears anyway.

Related: [[classroom-prose-loses-list-markers]]
