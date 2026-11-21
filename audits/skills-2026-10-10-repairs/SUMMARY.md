# Skills repaired with useful workflows preserved

Implemented 2026-10-10 against the [completed audit](../skills-2026-10-09/SUMMARY.md), using the installed Karpathy agent and independent review. Corrected actionable skill instructions and supporting code, then reconciled actual catalog and activation files. Two legacy input dependencies remain unavailable, listed below.

## Highest-risk repairs came first

| Problem | Result |
|---|---|
| Provider names, SDK identity and hardcoded model defaults were confused | Anthropic implementation stays Anthropic; Codex host instructions use actual host tools. Model availability and signatures require current evidence. Explicit provider/model choices are preserved. |
| Reviews could miss unstaged/untracked work | Review modes explicitly distinguish committed, working-tree and combined scope. Isolated Git fixtures exercise the previous omission. |
| Skills could stage unrelated changes, delete work or imply sending/publication | Scope and existing authorization are respected; staging stays bounded; drafts, reviews and intake do not imply sending, publishing or deletion. Useful workflows remain available. |
| Broad triggers intercepted unrelated tasks | API skills require their provider; hosted YouTube references require that provider; ordinary captions stay free; chat export requires an actual file-export request; persona creation, intake, query, lint and handoff retain distinct purposes. |
| Old paths, copied activations and literal unavailable host tools | Current-root routing and supported host entrypoints replace known invalid calls. Compatibility aliases remain thin wrappers and are catalogued. Existing Gemini-specific skills are catalogued without adding Claude/Codex/global activations. |
| Video helpers could delete frames or upload audio automatically | Fresh output directories required; existing frames/audio preserved; FFmpeg uses no-overwrite; paid audio transcription requires an explicit provider. Missing captions/keys remain visible. Missing Codex-global watch payload installed in the already-existing activation. |
| MCP examples used unsafe HTML and weak filesystem containment | User data rendered as text nodes; resolved filesystem targets checked against the registered root. Isolated JavaScript fixtures verify these mechanisms; this is not real-browser or adversarial race certification. |
| Graphify incremental imports could collide or retain stale data | Basename collisions stop visibly; changed/deleted sources require rebuilding. Graphify's actual remote/model pipeline was not exercised. |
| Verification tracer timed out resolving every executed line | Filename resolution happens once per filename; current execution receipts complete. Existing hook adapter regression tests pass. Hook trust/configuration was not changed. |

Originals, extra useful payloads, raw sources and historical snapshots are preserved. No files were deleted, no emails/messages sent, no paid provider called, and no commit, push or publication performed. Existing unrelated working-tree edits were not reset.

## Verification describes what actually ran

- `check-skills.py` passes: Claude 224, Codex 211, Gemini 222 catalog entries. Project activations resolve and match their runtime catalog; the generated index is complete.
- YAML parses for 1,732 current catalog/activation/global entrypoints, excluding inactive/historical project forks. Four malformed descriptions were quoted without changing their meaning.
- 900 distinct repaired or added skill/support/validator/override files are reconciled, with current hashes and original backups where a file already existed. This count is physical files, not 900 distinct skills.
- 84 direct regression checks and 30 earlier literal checks pass. All 649 original catalog dispositions remain accounted for. All 74 frozen snapshot hashes are unchanged.
- Nine video-boundary fixture tests, four validator/generator fixture tests and two MCP scaffold mechanism tests pass. The original/fixed comparisons cover relevant faults; these are isolated local tests, not live account operations.
- All 82 existing Karpathy hook/gate regression tests pass. This does not establish fresh native child-hook acceptance.
- Claudex offline updater dry run: zero copies changed, zero conflicts. The existing override mechanism preserves the Claude-host repairs. Matt Pocock dry run preserves locally adapted copies; this is deliberately not an upstream reset/adoption.
- Independent skill review confirmed the final transcript/provider/video fixes on current disk. Native selector behavior and every vendor integration are outside these local checks.

[Full current-file hashes and backups](FINAL-VERIFICATION.json), [catalog disposition mapping](CANONICAL.json), [global repairs](global-repairs.json), [core mechanisms](CORE.md), and [direct instruction repairs](DIRECTIVES.md).

## Two legacy dependencies are unavailable

1. `bootcamp-parity-audit`: original `bootcamp-quality-bar.md`, `intro-to-lr-product.md`, and `intro-to-lr-design.md` are absent. The skill now searches current authoritative documentation and can report observed differences, but cannot claim the missing benchmark's full parity standard. Historical content was not invented.
2. `research-deep`: the original `validate_json.py` is absent. Its instructions now resolve an actual installed validator before dispatch and refuse a validated-completion claim without it. A replacement schema/validator was not invented because the original field contract is unavailable. Ordinary sourced research remains available.

Runtime discovery is a separate limitation: an independently recorded 2026-10-10 terminal check reported a Codex skill-context budget warning and omitted descriptions. This repair pass verifies files and narrows triggers; it does not claim that every installed global skill is automatically visible in every running IDE or terminal. Existing processes may retain previously loaded skills until a new session.

## Seven Karpathy rules applied

Mechanisms and scope are explicit; fixtures isolate the fault; expected and observed behavior are compared; failing legacy cases explain the repairs; modified production helpers actually execute; unavailable inputs/live checks are disclosed; changes preserve useful knowledge rather than replacing the library. Local evidence passes these rules. Missing inputs and native/vendor acceptance remain separate from that result.

### Current execution receipts

- Video helpers and nine tests: `3244fdf462d34cf39d223dc4b9c9fcf2`.
- Validator/generator and four tests: `191d8fed90b14b2081f7c93178fcc02e`.
- MCP scaffolds and two tests: `c548b88c45d047edaa5311428ed67076`.
- Full final hash, YAML and regression readback: `5ab00370f48f489a903d4258160ed8fb`.
- Catalog core/direct/host repairs: receipts are recorded in CANONICAL.md and stage reports. Earlier tracer timeouts are failed attempts, not passing evidence.

Source collection, old-vault migration, live ingestion, student records and Google Drive/GitHub publication were not part of this repair request.
