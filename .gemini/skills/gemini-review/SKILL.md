---
name: gemini-review
description: "Codex-to-Gemini Argon 4 (Medium) review workflow. Gemini 4 Argon (Medium) independently reviews an existing plan while Codex coordinates a bounded revision loop."
---

# Gemini 4 Argon (Medium) reviews, Codex revises

Invoke this skill as `gemini-review`. It selects **Gemini 4 Argon (Medium)** (`--model gemini-4-argon --effort medium`, Antigravity `MODEL_PLACEHOLDER_M418`) as the independent plan reviewer while Codex (or the calling host) coordinates.

Load `../geminex-loop/SKILL.md` and read `../geminex-loop/references/runtime.md`. Resolve `RUNNER` from `../geminex-loop/scripts/runner.py`. Use `review --host codex --model gemini-4-argon --effort medium` with the resolved `--repo` and `--plan` path:

```powershell
python -X utf8 RUNNER review --host codex --repo <REPO_ROOT> --plan <PLAN_PATH> --model gemini-4-argon --effort medium
```

Do not restart an interview when the supplied plan is already adequate. This invocation authorizes plan review, not implementation. Evaluate Gemini's findings, record dispositions (`Accept`, `Modify`, or `Reject` with reasoning), update the plan, and resume with `--resume <PREV_RESULT_JSON> --feedback <DISPOSITIONS_FILE>` up to the round limit (`MAX_ROUNDS=5`). A failed, empty, malformed, or `REVISE`/`BLOCKED` result is never approval.
