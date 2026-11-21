# Repair routing and stale instructions before removing useful skills

Audit started 2026-10-09; completed 2026-10-10. Exact coverage is recorded in [coverage.json](coverage.json) and [every entry disposition](ALL-SKILL-DISPOSITIONS.md). This is a specialist skill-library audit, not a Four Cs score or evidence every workflow ran successfully.

## Recommendation

Keep the useful capabilities. Repair the exposed global provider corruption first, then restrict broad triggers that turn reading or inspection into paid calls, publication, assignments or destructive cleanup. Consolidate a few overlapping authoring routes after preserving their differences. Matching runtime copies, snapshots and compatibility aliases are not automatically redundant.

The project catalogs contain **649 physical entries: Claude 223, Codex 208, Gemini 218**. Those are copies and variants, not 649 unique capabilities. Global discovery adds entries outside those catalogs. Catalog presence alone does not mean a skill is active. Each disposition retains its exact path and scope in the complete ledger.

## Completed coverage

All **1,316 distinct physical entries** in the declared scope have current SHA-256 verification: 649 canonical catalog entries, 479 discovered non-snapshot global entries, 59 project activations and 129 stored supplemental entries. There are **zero pending semantic dispositions** and zero hash/base reconciliation errors. These paths contain 555 distinct byte hashes, not 555 proven independent capabilities.

**1,242 current, inactive or project-fork entries are semantically accounted for.** The remaining **74 frozen historical snapshots** are explicitly inventory-only. Coverage consists of 408 full-body receipts, one distributed full hatch-pet read, 697 exact-byte inheritances, 31 exact normalized-text inheritances, 47 complete-difference/base reviews and 58 original runtime-variant receipts recorded as full-body-or-complete-diff. That original variant category is retained honestly rather than inventing a more precise historical read classification.

Fresh recovery replaced generic provisional conclusions with individual reasons. Current-file and reviewed-base hashes were checked again after integration. The [machine ledger](all-skill-dispositions.json) retains the exact path, disposition, reason, read method, source receipt and base identity. No pending machine scan is counted as completed semantic review.

## Repair in this order

| Priority | Skill or route | Confirmed instruction problem | Concrete repair and check |
|---|---|---|---|
| 1 | Global `claude-api`, exposed as `Codex-api` | Claude identity was mechanically replaced with Codex while the instructions still require the Anthropic SDK. Its trigger also catches generic language and persona-agent tasks. | Restore Anthropic/Claude identity; trigger only Anthropic API implementation. Persona creation must route to `persona-agent-creator`. Preserve the healthy catalog API reference. |
| 1 | Global `academy-guide` | Anthropic Academy URLs and course identities were changed into `academy.Codex.com` and Codex product names. | Restore source identities and URLs; narrow to an explicitly relevant academy-learning request. |
| 1 | `lsatu-cc-handoff` | Operational briefs are written/moved under immutable `raw/sources`; its generated brief defaults to direct main commits and push after each step. | Use `handoffs/` for operational briefs, preserve sources, and carry the actual branch/commit/push authorization from the task. |
| 1 | `chat-export` | Promises a full verbatim conversation while reconstructing the currently visible context. Compaction can omit earlier turns. | Retrieve the actual transcript/log or explicitly label a visible-context export and missing ranges. Never fabricate vanished turns. |
| 2 | `code-review` and `requesting-code-review` | Commit-range comparisons omit dirty work during a work-in-progress review. | Inventory and include requested committed, staged, unstaged and untracked changes. Record the exact reviewed scope. The isolated fixture below proves this Git limitation. |
| 2 | `bootcamp-parity-audit` | Three mandatory benchmark anchors were absent at both literal legacy and current-root equivalents. | Resolve existing authoritative benchmarks before asserting parity; do not invent replacements. |
| 2 | `guided-drill-assignment` | Transcript inspection/recommendation triggers lead into an assignment workflow and compete with the current assignment executor. | Separate inspect, recommend and assign modes. A transcript-only request must make no live write. Keep lesson-selection knowledge. |
| 2 | Consultation draft skills | Existing unsent draft reuse is not explicitly checked by stable event/thread/recipient key. | Reuse the matching draft; a repeated sweep should not create another. No duplicate live draft was created in this audit. |
| 2 | `qa` | General QA trigger instructs immediate GitHub issue publication without review. | Distinguish report-only QA from explicitly authorized issue filing. |
| 2 | `test-driven-development` | Commands deleting/restarting existing implementation solely because a failing test was not written first. | Preserve user work; use meaningful red-green regression tests proportionately. Never delete existing work as a ceremony. |
| 2 | `resolving-merge-conflicts`, `setup-pre-commit` | Stage-all/automatic commit defaults risk including unrelated work. Hook setup also lacks preserve/merge guidance for existing hook configuration. | Capture baseline, stage only owned paths, preserve existing hooks and honor explicit commit scope. |
| 2 | `youtube-full`, `watch`, inactive transcript aliases | Broad YouTube triggers select keyed/credit-consuming services; watch adds another secret home and cleanup deletion. | Free existing caption collector first, explicit optional paid fallback and bounded authorization, central secret route, preserve captures until removal authorized. |
| 2 | Codex `lovable-prompt` | Requires Supabase MCP tools absent from this session. | Route through an available approved transport. Mandatory Lovable deployment applies to Edge Functions, not a blanket ban on direct SQL. Verify app-specific safe-push route separately. |
| 2 | Codex catalog `imagegen` | Chromakey guidance assumes built-in transparency is unavailable, but the current exposed tool has `transparent_background`. | Use the actual built-in parameter and inspect output. The current global system skill already has the correct capability; the catalog copy is stale. |
| 3 | `decision-mapping`, Codex `research-deep` | Misspelled `domain-modelling` route and an absent hardcoded research validator path. | Resolve exact installed dependencies before invocation; use the skill's actual support directory. |
| 3 | Literal Claude `Skill` calls in Codex copies | No native Skill invocation tool is exposed in this Codex session. | Read the appropriate skill entry point or use the supported host route. Preserve vendor sources and maintain a small project overlay. |
| 3 | Gemini legacy audit/Claudex/Kling copies | Mac paths, launchctl, old host roles and older Kling contract survive outside the validator's Claude/Codex scope. | Reconcile deliberate host differences and current shared runner/version; add Gemini validation. |
| 3 | High-end design presets | Generic triggers impose nested cards while another design skill says nested cards are always wrong. Other redesign instructions fabricate organic data/dates. | Make aesthetics explicit optional presets; preserve the project's design system, facts and accessibility. |
| 3 | `webapp-testing`, `web-artifacts-builder`, `teach` | Universal networkidle is not UI readiness; artifact builds default into cwd and discourage testing; learning workspace defaults can clutter the vault. | Select sibling application/learning homes, assert actual readiness and run relevant checks before completion. |
| 3 | `setup-matt-pocock-skills`, `setup-ts-deep-modules` | Select one instruction file when this project requires shared rules in both manuals. | Host/project overlay must mirror shared pointers without regenerating hand-owned manuals. |

## Cleanup candidates, preserving information

| Candidate | Recommended disposition | Why |
|---|---|---|
| `obsidian-vault` for this AI OS | Leave inactive/deactivate its current-vault trigger | Targets `/mnt/d/Obsidian Vault/AI Research` and a flat no-folder layout, conflicting with this structured vault. Current ingest/query/lint own the work. |
| `lsat-u-topic-builder` | Retire broad entry after preserving useful references | `bootcamp-builder` explicitly supersedes it; old Mac search and unsafe source/duplicate heuristics remain. |
| `example-command`, `example-skill` | Reference-only | Educational samples have value but should not compete with real creator workflows. |
| `brand-guidelines` | Explicit Anthropic-brand only | Its palette is Anthropic's, not Joshua's. |
| `using-superpowers` | Narrow or explicit invocation | Catch-all every-conversation loading adds routing and approval friction. |
| `high-end-visual-design` | Explicit aesthetic preset | A valid style choice should not override every frontend brief. |
| `to-issues` and `to-tickets` | Consolidation candidate | Share vertical-slice breakdown; to-tickets adds local tracker/native edges and expand-contract. Preserve compatibility and approval semantics. |
| `writing-beats` and `writing-shape` | Consolidation candidate | Both shape a fixed source pile collaboratively; beat mode can share one authoring core. Keep `writing-fragments` as the separate exploration phase. |
| `writing-great-skills` and `writing-for-agents` | Shared reference candidate | Repeated vocabulary and hierarchy guidance can live once, with skill-specific mechanics retained. |
| `ubiquitous-language` and domain modeling glossary routes | Consolidation candidate | Avoid competing `UBIQUITOUS_LANGUAGE.md` and `GLOSSARY.md` truths; preserve explicit ambiguity and relationship analysis. |
| Inactive YouTube aliases | Keep inactive, optional provider reference | They offer overlapping keyed TranscriptAPI routes. Do not reactivate a dozen broad names; preserve any unique search/channel/playlist references. |
| Original Nate handoff copies | Keep historical reference | Customized current handoff supersedes them. Their broad body triggers conflict with the frontmatter's explicit-only boundary if reactivated. |

No usage telemetry was gathered. An unfamiliar specialized skill is not proven useless. There is no recommendation to blanket-delete GWS helpers, media tools, runtime copies or specialist references.

## Keep these core boundaries

- `ingest`: add a new source and compile knowledge.
- `second-brain-query`: answer from saved knowledge with evidence and freshness escalation.
- `second-brain-lint`: check knowledge structure, contradictions, stale claims and missing pages.
- `audit`: system health; `skill-lint`: package checks; `skill-doctor`: actual usage evidence. These do different jobs.
- `persona-agent-creator`: build another documented-method agent; `karpathy-teach`: use the existing reviewed teaching agent.
- Claudex provider pairs and compatibility wrappers: deliberate runtime directions in `PARITY.md`, not accidental duplicates.
- GWS domain/helper skills: API surfaces and specific actions, not dozens of copies of one workflow.

## Trigger counterexamples to use during repairs

These are static instruction comparisons, **not observed native selector execution**.

| Request | Correct intent | Current collision | Acceptance requirement |
|---|---|---|---|
| Create a persona agent for this author | Persona factory | Global Codex-api catches unstated-provider agent tasks | Factory route; no API/provider assumption |
| Read this student's transcript and tell me where they struggle | Inspection | Guided-drill assignment continues into execution | No assignment/send/live write |
| Give me the transcript of this YouTube URL | Free caption extraction first | Broad keyed/credit routes | Keyless collector or explicit limitation; paid fallback only authorized |
| Review my uncommitted changes | Worktree review | Three-dot HEAD range | Includes actual dirty/staged/untracked scope |
| Polish this UI using our current design system | Preserve existing visual language | Presets impose contradictory universal aesthetics | Follow actual design system; motion/accessibility preserved |
| Improve this small approved configuration | Direct authorized scoped edit | Generic brainstorming imposes new approval ceremony | Existing authorization honored |
| What do my saved notes say about this? | Query | Generic old Obsidian workflow | Current schema/index retrieval, no alternate vault |

## What was checked and what was not

Full semantic entry-point reads were recovered after the original concatenated output truncated. Exact byte copies inherit a fully reviewed base; nonidentical variants require reviewed complete differences and a fully reviewed base. SHA-256 receipts identify physical files. LF-normalized exact text is explicitly distinguished from byte identity. Fresh hash reconciliation prevents stale review receipts from being silently counted.

The full per-entry table records scope and recommended disposition. Historical snapshots are inventoried and preserved; unmatched inactive entry points are reviewed separately. Supporting scripts, vendor payloads, assets and external plugin cache trees were not exhaustively executed. Their presence and selected routes were checked where relevant. This is not a claim every file on the machine was read or every third-party skill installed in every possible plugin root was tested.

The existing validator checks project activated/catalog drift and Claude/Codex parity; it does not certify owned global body correctness or Gemini. Add bounded owned-global/provider sanity and Gemini checks rather than mirroring every external vendor package into this repo.

## Workspace helper findings

The fresh global GWS review found a broken shared-auth prerequisite in the synced `gws-gmail-read` copy: its `../gws-shared/SKILL.md` target is absent. Top-level GWS prerequisites are present. Other concrete corrections are the Forms `forms.update` prose versus `batchUpdate` inventory, apparent agent-task/message-stream resources mixed into Workspace Events, an unread-mail query described as inbox triage, and meeting preparation that promises linked-document contents without demonstrating retrieval. The shared GWS prerequisite does require write/delete confirmation, so local omissions are evaluated against that existing policy rather than reported as universally unguarded writes.

## Recipe and global routing recovery

The fresh recipe/persona review preserves useful Google Workspace endpoint references but identifies concrete contract mistakes. `recipe-find-free-time` creates an event after a find-only request; `recipe-plan-weekly-schedule` queries 2025 free/busy while inserting a 2026 event; `recipe-copy-sheet-for-new-month` renames hardcoded sheet ID 123 instead of the response ID. Other recipes promise initial presentation slides, feedback questions, an attachment or bounded vacation dates without supplying those steps. The Gmail filter recipe removes INBOX during a generic labeling workflow, and the expense tracker appends a sample expense as real data. Repair these narrow contracts before reuse, rather than deleting all recipes.

Role personas such as event coordinator or researcher are convenience routers, not evidence-based replicas of a real person's method. Keep their distinct Workspace recipes but narrow automatic publishing and role-wide triggers. The reusable `persona-agent-creator` remains a different capability.

Current Gemini Superwhisper still contains an older settings.json/modeKeys workflow while current Claude/Codex bodies use the revised SQLite workflow. Align that stale runtime copy without discarding vocabulary/replacement guidance.

## Additional full-body recovery findings

The long-body review adds concrete repair candidates without discarding the underlying capability:

- **Graphify:** the chunk contract requests JSON output while later success depends on a saved disk file; basename-only graph IDs can collide across folders, and updated files may leave stale graph content. Reconcile file contracts and refresh behavior before reuse. Its independent raw intake should use the existing ingest route.
- **LSAT Lab transcription and mega-set:** require verified capture before advancing the current item; preserve deletion authorization and reconcile obsolete Mac shortcuts/log paths with the actual Windows workflow.
- **NotebookLM:** reconcile `task_id` versus `artifact_id` across the described polling/download steps. This is a static contract inconsistency, not a live service failure claim.
- **Plugin helpers:** reconcile optional grep with `pipefail`, settings reload guidance and wrapper contracts; native host tool discovery still requires verification.
- **Design taste:** define or remove the undefined `LAYOUT_VARIANCE` parameter and make perpetual motion an explicit aesthetic choice. Emil's design guidance already contains reduced-motion instructions, so missing reduced-motion support is not a supported finding.
- **Skill writing:** preserve unrelated work instead of treating deletion of every untested existing implementation as universally appropriate. Keep specialized creator and plugin-development knowledge as references rather than flattening it into one generic skill.

## AGENTS.md and CLAUDE.md

Both current root manuals were read in full. Shared routing and guardrails agree in the inspected text; runtime identity differences are deliberate. They define the canonical root, immutable source evidence, outside-vault application homes, dual-runtime copies, explicit deletion permission and live-system authority. No manual changes were needed for this audit. Legacy skill instructions should adapt to those authorities. The old session-handoff F26 drift is resolved and is not a current defect.

## Safe behavioral evidence

The parent ran an isolated temporary Git repository: commit one file, then edit it without committing. Predicted the committed three-dot range would miss the edit while worktree diff would show it. Observed `git diff HEAD...HEAD` was empty; `git diff` contained `+changed`. This demonstrates the documented review scope defect. The proposed correction is to add explicit worktree/staged/untracked inventory, not change the production skills during an audit. The temporary fixture was cleaned by its isolated TemporaryDirectory lifecycle; no AI OS commit or mutation occurred.

The parent also ran `gws gmail +send --help`, which explicitly supports `--draft` and `--dry-run`. The booking draft flag is valid. No message or draft was sent/created. The parent also ran `gws forms forms --help`: `batchUpdate` is available while `update` is absent, and `create` copies only title fields. This supports the Forms instruction and empty-form recipe findings without making a live API write.

## Seven-rule grades

Based on the [reviewed method](../../wiki/karpathy/rules.md), not a claim about Karpathy's endorsement. See the independent [parent review and behavioral receipt](PARENT-REVIEW.md).

| Rule | Grade | Concrete evidence |
|---|---|---|
| Mechanism reconstruction | Pass | Trace request, trigger, selected route and resulting side effect; show inspection vs assignment counterexample. |
| Small baseline | Pass | One file with one uncommitted edit isolates commit-range review scope. |
| Prediction/run/comparison | Pass | Parent predicted empty committed range vs visible worktree diff, then observed both. |
| Counterexample/fix | Pass for diagnostic proposal | Fixture exposes the omission and worktree comparison corrects the diagnostic coverage. Production instruction repair is intentionally not applied. |
| Relevant execution | Pass within audit scope | Safe Git fixture, actual CLI help, filesystem/hash/coverage checks. No claim live skill workflows ran. |
| Explicit assumptions | Pass | Static routing is separated from native selection; telemetry, payload and external cache limits explicit. |
| Justified simplicity | Pass | Consolidate repeated entry routes while preserving specialist knowledge and deliberate runtime differences. |

## What I ran

Catalog/global entry inventory, full semantic body and complete variant reviews, hashes and coverage reconciliation, selected support/route probes, current manuals/PARITY checks, parent isolated Git fixture and read-only GWS help.

## What came out

Ranked repair and cleanup recommendations, exact per-entry dispositions and scope evidence. The main risk is stale or overbroad instructions, not simply the number of files.

## What I changed

Audit reports and evidence ledgers only. No skill was deleted, deactivated, rewritten, committed or published; no live data or configuration was changed by this audit.
