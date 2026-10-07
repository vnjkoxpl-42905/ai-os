---
name: codex-model-roles
description: "Which Codex model does what — gpt-6-astra designs, specs and reviews; gpt-6-luna high builds; a 400 on sol or luna means a stale CLI, use dev/tools/node/codex."
metadata:
  node_type: memory
  type: feedback
  originSessionId: fe553725-d881-4068-8809-1fb7b342eee9
  modified: 2026-09-23T17:32:39.178Z
---

Codex model by role (Joshua, 2026-09-23):
- **Design, spec writing, plan review** (`/codex-review`, design critique): `gpt-6-astra` (he picked medium effort for plan review).
- **Building code** (`/codex-build`, any Codex implementation run): `gpt-6-luna` at `high` reasoning effort. Never astra.
- The config default (`gpt-6-luna`, low) is neither; always pass `-m` and `-c model_reasoning_effort=` explicitly and echo them before launch.

- **Fixed 2026-09-23:** a 400 "not supported when using Codex with a ChatGPT account" on sol/luna meant an outdated CLI, not the login. The stale 0.153.4 in `AppData\Roaming\npm` sits first on the bash PATH; the current CLI is `C:\Users\Joshu\dev\tools\node\codex` (0.156.1), where sol and luna both run on the ChatGPT login. Call it by full path. Joshua does not want an API-key login and picked `gpt-6-luna` high for builds (never luna low).

**Why:** building from a frozen spec does not need the strongest model; astra's value is in thinking through design and specs. He objected when astra built Classroom Home phase 1 (PR #133).

**How to apply:** on every Codex launch, choose the model by role, state it before running. Related: [[firecrawl-via-cli-not-mcp]] (same "use the cheaper path when it does the job" instinct).
