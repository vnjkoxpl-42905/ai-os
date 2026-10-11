# Independent parent review, 2026-10-10

This checks the Karpathy agent's audit reasoning and selected findings. It does not certify that every audited workflow succeeds in a live runtime. The original audit began on 2026-10-09 and was resumed on 2026-10-10.

## Independently checked findings

- The exposed global `claude-api` labels itself `Codex-api` while prescribing Anthropic SDK usage. Healthy catalog copies preserve the Claude/Anthropic identity. The global Academy guide also substitutes Codex into Anthropic Academy addresses. These are internal provider/source contradictions, without needing a speculative claim about model availability.
- `lsatu-cc-handoff` writes and moves briefs under immutable `raw/sources` and inserts unconditional main-branch commit/push instructions. These conflict with source preservation and task-specific authorization.
- `chat-export` promises a full verbatim transcript reconstructed from current context. This cannot establish completeness after context compaction without original logs.
- `code-review` advertises work-in-progress review but specifies a committed-range three-dot diff. The isolated fixture below demonstrates the missing change class.
- `high-end-visual-design` mandates nested cards while `impeccable` forbids them. These should be explicitly selected aesthetic presets, with project design requirements authoritative.
- `setup-pre-commit` prescribes replacement hook/config bodies and a final commit without a baseline/merge-existing checkpoint. `setup-matt-pocock-skills` selects only CLAUDE.md when both runtime manuals exist; a project adaptation must preserve shared instructions for both hosts.
- The global hatch-pet body was fully reviewed jointly: the worker read lines 1–180, and the parent read 181–923 in four complete bounded ranges. Its unique sprite pipeline should remain available; automatic source/intermediate deletion and repaired-job completion ordering need correction. SHA256: `ac22ec3cbabc95ba03ee3d7cf43a1209fcd139d56c69d35b10c57b9b5f794da0`.
- The parent reviewed all eight unique unmatched LSATU project-fork bodies, using complete diffs against reviewed canonical bases for seven and a full body read for `using-git-worktrees`. Their hashes are recorded in the supplemental inventory. Older forks lose current routing, recovery, review and host adaptations.

## A predicted counterexample, then the observed comparison

An isolated temporary Git repository contained one committed file, then an uncommitted edit. Prediction: `git diff HEAD...HEAD` would return an empty diff while `git diff` would contain the edit. Both predictions were confirmed: `committed_range_empty=true`, `working_tree_contains_change=true`. The fixture used a temporary directory and local commit identity; it did not modify the AI OS repository or global Git configuration. Adding the appropriate working-tree/staged/untracked coverage is a proposed skill repair, not a repair applied during this audit.

## A suspected fault rejected by a live check

`gws gmail +send --help` completed successfully and explicitly lists `--draft` as “Save as draft instead of sending,” alongside `--dry-run`. The suspected unsupported draft flag was rejected. No message was sent and no draft was created.

The Lovable finding was also narrowed: the inspected helper requires unavailable Supabase MCP tools. The mandatory Lovable route covers Edge Function deployment; it is not a blanket prohibition on authorized direct database operations. The architecture skill's hardcoded backend identifier remains a freshness risk unless a current authoritative comparison proves it incorrect.

## Seven-rule independent grades

| Rule | Grade | Evidence |
|---|---|---|
| Reconstruct the mechanism | Pass | Findings trace trigger, instruction, source/tool, output and acceptance gaps rather than treating a folder count as capability. |
| Start with a small baseline | Pass | Core ingest/query/lint remain distinct; the Git test uses one file and one dirty edit. |
| Predict, run and compare | Pass | The Git fixture records a prediction and confirms both diff results. |
| Expose a counterexample and repair its cause | Pass for audit reasoning | The WIP counterexample demonstrates the route to correction; the GWS hypothesis was removed after contradictory live evidence. Production skill repairs remain unapplied. |
| Verify relevant behavior | Pass within stated scope | Actual Git behavior and installed CLI help were checked. Static trigger cases are not represented as native selection proof. |
| Expose assumptions and uncertainty | Pass | Semantic body review, inventory-only historical snapshots, selective supporting-file inspection and untested live workflows are distinct. |
| Earn complexity | Pass | Preserve useful capabilities and intentional runtime copies; narrow or retire competing entry points rather than deleting by name similarity. |

## What I ran

Bounded source reads, complete project-fork diffs, selected hash checks, the isolated Git fixture, and read-only GWS command help.

## What came out

High-priority findings have direct instruction evidence, a WIP review defect has a behavioral counterexample, and one suspected draft-command defect was disproved. Read the integrated summary and coverage ledger for the complete inventory and exclusions.

## What I changed

This review record only. No skill, activation, runtime manual, hook, or live system was changed by the parent audit.
