# Build and final inspection (`geminex-loop`)

Resolve the shared runner (`../scripts/runner.py`) from the installed `geminex-loop` skill. Keep the spec and run artifacts available to both Gemini and Codex. Preserve user-selected toolchains and carry exact acceptance criteria and proof commands into the build.

## Preparation

Capture the pre-build commit before changing code. A host build may preserve and account for existing changes, but a delegated build (`runner.py build`) requires an isolated clean checkout. Use a worktree for unrelated or live changes instead of stashing another session's work.

## Delegated build

```text
python -X utf8 RUNNER build --host gemini --builder codex --repo PROJECT --plan PLAN_PATH --approval APPROVED_RESULT --proof "python -m unittest discover"
python -X utf8 RUNNER build --host codex --builder gemini --repo PROJECT --plan PLAN_PATH --approval APPROVED_RESULT --proof "npm test" --model gemini-4-argon --effort medium
```

- When `--builder codex` is selected, Codex builds with `workspace-write` and non-interactive approvals.
- When `--builder gemini` is selected, Gemini 4 Argon (Medium) (`MODEL_PLACEHOLDER_M418`) implements the frozen work order inside the target checkout via the Antigravity Language Server without committing or pushing.
- For an explicitly requested standalone work order without prior plan review, replace `--approval` with `--unreviewed-spec` and record the status.

## Verify and inspect

```text
python -X utf8 RUNNER inspect --host gemini --builder codex --repo PROJECT --plan PLAN_PATH --base BASE_COMMIT
python -X utf8 RUNNER inspect --host codex --builder gemini --repo PROJECT --plan PLAN_PATH --base BASE_COMMIT --model gemini-4-argon --effort medium
```

The runner supplies the tracked diff plus a SHA-256 manifest of all changed, deleted, and untracked files. The inspector must be the provider opposite the builder (Codex inspects Gemini builds; Gemini 4 Argon Medium inspects Codex builds). Never allow either provider to certify its own work as an independent inspection.
