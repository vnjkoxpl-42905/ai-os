---
name: codex-model-roles
description: "Which Codex model does what — gpt-6-astra designs, specs and reviews; gpt-6-luna high builds; a 400 on sol or luna means a stale CLI; check codex --version (0.162.1 in dev/tools/node as of 2026-10-10)."
metadata:
  node_type: memory
  type: feedback
  originSessionId: fe553725-d881-4068-8809-1fb7b342eee9
  modified: 2026-10-11T01:47:56.474Z
---

Codex model by role (Joshua, 2026-09-23):
- **Design, spec writing, plan review** (`/codex-review`, design critique): `gpt-6-astra` (he picked medium effort for plan review).
- **Building code** (`/codex-build`, any Codex implementation run): `gpt-6-luna` at `high` reasoning effort. Never astra.
- The config default (`gpt-6-luna`, low) is neither; always pass `-m` and `-c model_reasoning_effort=` explicitly and echo them before launch.

- **Fixed 2026-09-23, path changed 2026-10-10:** a 400 "not supported when using Codex with a ChatGPT account" on sol/luna meant an outdated CLI, not the login. The fix then was 0.156.1 in `C:\Users\Joshu\dev\tools\node\codex`, but that directory no longer exists. On 2026-10-10 the folder was recreated and Codex CLI 0.162.1 installed there from npm (first on the user PATH, signed in with ChatGPT). A second copy in `AppData\Roaming\npm` exists but is invisible inside Herdr, see [[powershell-msix-breaks-npm-clis]]. Whether sol and luna run on 0.162.1 was not tested; if a 400 returns, check `codex --version` first. Joshua does not want an API-key login and picked `gpt-6-luna` high for builds (never luna low).

**Why:** building from a frozen spec does not need the strongest model; astra's value is in thinking through design and specs. He objected when astra built Classroom Home phase 1 (PR #133).

**How to apply:** on every Codex launch, choose the model by role, state it before running. Related: [[firecrawl-via-cli-not-mcp]] (same "use the cheaper path when it does the job" instinct).
