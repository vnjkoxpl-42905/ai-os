---
name: geminex-loop
description: "Bidirectional Gemini 4 Argon (Medium) and Codex loop. Harden a plan with independent cross-provider review between Gemini 4 Argon (Medium) and Codex, then optionally build and cross-inspect the final diff. Works from either Gemini/Antigravity (--host gemini) or Codex (--host codex)."
---

# Geminex Loop: Gemini 4 Argon (Medium) <-> Codex

Pair **Gemini 4 Argon (Medium)** (`gemini-4-argon`, effort `medium`, Antigravity `MODEL_PLACEHOLDER_M418`) and **Codex** (`codex` CLI) so the host plans and coordinates while the other provider independently reviews the plan and inspects the final code changes.

Read [references/runtime.md](references/runtime.md) and [references/build.md](references/build.md). Resolve `RUNNER` as the absolute path to `scripts/runner.py` inside this skill directory. Always invoke Python with `python -X utf8` on Windows.

## Default Model Pairing

- **Gemini side**: Always defaults to **Gemini 4 Argon (Medium)** (`--model gemini-4-argon --effort medium`, mapped to Antigravity `MODEL_PLACEHOLDER_M418`).
- **Codex side**: Uses the configured Codex CLI default (or explicit `--model gpt-6-astra --effort high` / `gpt-6-luna` / `gpt-6.1-sol`).

## Roles by Host

1. **When running inside Gemini / Antigravity (`--host gemini`)**:
   - **Planner / Coordinator**: Gemini 4 Argon (Medium)
   - **Independent Plan Reviewer**: Codex (`runner.py review --host gemini`)
   - **Default Builder**: Gemini (or delegated to Codex via `--builder codex`)
   - **Independent Diff Inspector**: Opposite of the builder (`runner.py inspect --host gemini`)
2. **When running inside Codex (`--host codex`)**:
   - **Planner / Coordinator**: Codex
   - **Independent Plan Reviewer**: Gemini 4 Argon (Medium) (`runner.py review --host codex --model gemini-4-argon --effort medium`)
   - **Default Builder**: Codex (or delegated to Gemini via `--builder gemini`)
   - **Independent Diff Inspector**: Opposite of the builder (`runner.py inspect --host codex`)

## 4-Phase Workflow

### Phase 0: Recon (Read-Only)
Inspect the repository (`README`, `AGENTS.md`, `GEMINI.md`, `CONTEXT.md`, `GLOSSARY.md`, `DECISIONS.md`) and relevant files before asking questions or drafting a plan.

### Phase 1: Settle Requirements & Write `PLAN.md`
If requirements have material ambiguity, interview the user one question at a time with a clear recommendation. Once settled, write `PLAN.md` (Goals, Non-Goals, Design, Validation/Proof commands, File List, Open Risks) and initialize `GEMINEX-LOG.md`. If invoked in review-only mode on an existing adequate plan, skip the interview and proceed directly to Phase 2.

### Phase 2: Independent Cross-Provider Plan Review (`review`)
Run up to `MAX_ROUNDS=5`:
```powershell
python -X utf8 RUNNER review --host <gemini|codex> --repo <REPO_ROOT> --plan <PLAN_PATH> --model gemini-4-argon --effort medium
```
- On subsequent rounds, record host dispositions (`Accept`, `Modify`, or `Reject` with reasoning) in a UTF-8 feedback file, update `PLAN.md`, and resume the same reviewer session:
```powershell
python -X utf8 RUNNER review --host <gemini|codex> --repo <REPO_ROOT> --plan <PLAN_PATH> --resume <PREV_RESULT_JSON> --feedback <DISPOSITIONS_FILE>
```
- Stop when `result.json` reports `status == "completed"` and `response.verdict == "APPROVED"`. A failed, timed-out, or `REVISE`/`BLOCKED` run is never approval.

### Phase 3: Build & Independent Diff Inspection (`build` & `inspect`)
Only proceed to implementation when authorized by the user's request (review-only or grill-only requests stop after Phase 2).
1. Record the pre-build Git commit (`git rev-parse HEAD`).
2. Implement either in the host or via delegated build (`runner.py build --host <gemini|codex> --builder <codex|gemini> ...`).
3. Run the agreed proof commands independently.
4. Run a fresh cross-provider inspection (`runner.py inspect --host <gemini|codex> --builder <builder> --repo <REPO_ROOT> --plan <PLAN_PATH> --base <BASE_COMMIT>`). Fix accepted findings (up to `MAX_FIX_ROUNDS=2`) and re-inspect until `APPROVED`.
