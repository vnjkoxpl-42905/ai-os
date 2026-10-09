# Skill parity baseline

## 2026-10-09: Persona Agent Creator

`persona-agent-creator` is catalogued and activated as matching project copies in both runtimes. Its host-aware factory procedure requires actual native person-agent registration and an independently grading entry skill. It reuses existing ingest/schema conventions, derives each person's own rules, and explicitly tests new hook scope instead of inheriting Karpathy's hardcoded guard. Codex invokes `$persona-agent-creator`; generated person agents use each host's native configuration. No global activation was added.

Declared single-runtime skills. `check-skills.py` fails on **undeclared** asymmetry only:
when you deliberately add a skill to one runtime and not the other, add it here in the same
commit. When a skill shows up as undeclared drift, either activate it for both runtimes or
declare it here **with a reason**.

Every entry below carries its justification. An entry without one is not a decision, it is a
snapshot — which is what this file was until the audit noted below.

**Audited 2026-09-12.** The Windows parity pass repaired the cross-platform validator,
catalogued `kling-cli` for both runtimes, and ported 25 previously undeclared Claude-only
skills to Codex: `academy-guide`, `algorithmic-art`, `brand-guidelines`, `canvas-design`,
`claude-api`, `claude-handoff`, `code-review`, `discernment-nudge`, `doc-coauthoring`,
`docx`, `implement-spec`, `internal-comms`, `loop-me`, `mcp-builder`,
`migrate-to-shoehorn`, `pdf`, `pptx`, `retro`, `session-recap`,
`setup-ts-deep-modules`, `slack-gif-creator`, `theme-factory`,
`web-artifacts-builder`, `wizard`, and `xlsx`. Current catalog counts:
**claude=211 codex=188**.

Note that DB parity is not activation. The DB is the complete catalog; Codex's activated set
in `.agents/skills/` is a deliberately small ops core. Porting a skill here does not activate
it, and is not meant to.

## Claude only

### Vendor / plugin snapshots (24) — not authored here

`a11y-debugging`, `agent-development`, `build-mcp-app`, `build-mcp-server`, `build-mcpb`,
`chrome-devtools`, `claude-automation-recommender`, `claude-md-improver`,
`command-development`, `debug-optimize-lcp`, `discord-access`, `discord-configure`,
`example-command`, `example-skill`, `hook-development`, `imessage-access`,
`imessage-configure`, `math-olympiad`, `mcp-integration`, `playground`, `plugin-settings`,
`plugin-structure`, `skill-development`, `troubleshooting`

These live under `skills/claude/_snapshots/` and ship with Claude plugins. They document
Claude's own extension surfaces (hooks, plugins, MCP authoring) or vendor integrations. A
Codex copy would describe machinery Codex does not have. Correct as Claude-only, permanently.

### Claudex package: mirrored runtime directions since 2026-09-30

Joshua authorized universal activation and an inverse Codex version of every skill in chaseai-yt/claudex-loop. All six package workflows are available in both catalogs and project/global activation roots. Codex uses claude-review, claude-build, grill-me-claude, and grill-with-docs-claude; Claude retains codex-review, codex-build, grill-me-codex, and grill-with-docs-codex. These deliberate name differences are paired equivalents, not missing skills. Their SKILL.md entry points deliberately differ by runtime; shared upstream supporting files remain complete.

| Skill | Claude host | Codex host |
|---|---|---|
| claudex-loop | Claude plans, Codex reviews; host builds by default | Codex plans, Claude reviews; host builds by default |
| claudex-route | Default cross-provider handoff to Codex | Default cross-provider handoff to Claude |
| codex-review | Codex reviews, Claude revises | Claude reviews, Codex revises |
| codex-build | Codex builds, Claude inspects | Claude builds, Codex inspects |
| grill-me-codex | Claude interviews, Codex reviews | Codex interviews, Claude reviews |
| grill-with-docs-codex | Same direction with context, glossary, ADRs | Inverse direction with context, glossary, ADRs |

Codex entry-point names identify Claude as the delegate. The updater maps upstream names to these installed names and retires the old Codex-side copies into inactive backups. Explicit user provider/model choices still take precedence in the general loop and route. The additional grill-by-claude shortcut is intended for a Codex host.

system/scripts/sync-claudex-skills.py updates four upstream support trees and three local entry points through the existing daily Codex automation. It computes separate runtime hashes, inserts runtime directions, and overlays the Codex review/build entry points from system/skill-overrides/claudex/codex. Local aliases remain under system/skill-overrides/claudex. Whole-tree compare-and-swap preserves local edits. Previous copies live outside activation roots under ~/.agents/claudex-backups. No source links or junctions join the vault to the clone.

### Blocked by a missing Codex dependency (1)

- `youtube-full` — requires a YouTube MCP server. Codex's `~/.codex/config.toml` declares
  only `node_repl`, `computer-use`, `tavily`, and `notebooklm-mcp`, so the skill cannot run
  there. **Revisit if Codex gains a YouTube MCP** — this is a capability gap, not a design
  decision.

### Claude-specific tooling (1)

- `bootcamp-builder` — built around AskUserQuestion gating and subagent fan-out. A Codex copy
  would need a rewrite, not a port.

### Other ledger workflows held to one runtime (4)

- `resume` — restores session state by reading the wiki ledgers (Codex uses `session-handoff`,
  which is chat-only and writes nothing)
- `bootcamp-parity-audit` — writes findings into the wiki
- `morning-brief` — appends to `wiki/send-ledger.md`; also bound to a Claude-specific runner
  (the launchd job shells out to `claude -p`)
- `send-booking-link` — appends to `wiki/send-ledger.md` and `students/<name>/open-loops.md`

The LLM Wiki ingest, query, and lint workflows are shared by Codex and Claude as of 2026-09-30. Other ledger workflows listed here retain their declared single-runtime scope. Never have separate runtimes editing the same page concurrently.

**Honest caveat:** `send-booking-link` and `morning-brief` are otherwise runtime-neutral ops
skills. They are held back by the ledger-collision rule, not by anything they cannot do. If
Codex ever needs to run the booking pipeline, the fix is a write-arbitration rule for the
ledgers, not a quiet port.

### Under review (1)

- `lovable-migrate` — packages a SQL change for the Lovable UI plus a verification probe.
  Mostly runtime-neutral; kept Claude-only for now only because it reads `connections.md` and
  records outcomes alongside the other ledger writers. Lowest-confidence entry in this file.

## Codex only

### Vendor / plugin skills (13)

`higgsfield-generate`, `higgsfield-marketplace-cards`, `higgsfield-product-photoshoot`,
`higgsfield-soul-id`, `higgsfield-websites`, `imagegen`, `openai-docs`, `playwright`,
`plugin-creator`, `research-add-fields`, `skill-installer`, `to-prd`, `using-git-worktrees`

Shipped with Codex or its plugins. `openai-docs` and `plugin-creator` document OpenAI's own
surfaces; the `higgsfield-*` set and `imagegen` are media-generation integrations wired to
Codex's MCP servers. Correct as Codex-only.


## 2026-09-16: grill-with-docs activation repair

The ordinary grill-with-docs, grilling, and domain-modeling skills are activated as complete project copies in both runtimes. Codex loads the two sibling SKILL.md files directly, with explicit-only discovery in agents/openai.yaml. Claude also reads sibling files directly because a dependency can disable model invocation. This is a runtime invocation adaptation, not a single-runtime skill exception. The separate Claude-only grill-with-docs-codex entry remains unchanged.

## 2026-09-26: grill-with-docs back to upstream; grill-me kept as a local rewrite

Supersedes the 2026-09-16 note above. The sibling-file workaround existed only because a local edit had added `disable-model-invocation: true` to `grilling`, which upstream (mattpocock/skills) never carries. That line is removed from every copy, so upstream `grill-with-docs` ("call the Skill tool twice, for grilling and domain-modeling") works again and is now installed verbatim in every runtime. The daily sync (`system/scripts/sync-mattpocock-skills.py`) keeps it current.

`grill-me` is deliberately NOT upstream in the Claude and Gemini copies (global, `skills/claude`, `skills/gemini`). Upstream's `grill-me` is a one-line call to `grilling`; Joshua's version adds the capture discipline (every answer checkpointed to a brainstorm file) that his brainstorm and AI OS context sessions depend on. Decided by Joshua 2026-09-26. The sync script lists it in `KEEP` and never overwrites it. The Codex copy is upstream.

## 2026-09-30: LLM Wiki workflows shared across runtimes

`ingest` is now catalogued and activated for Codex and Claude, with matching Gemini copies. The obsolete Claude-only exception is removed. `second-brain-ingest` is a compatibility alias for public `ingest`; query and lint are separate shared workflows. Current-vault policy lives in `system/schema/llm-wiki.md`. Existing global copies were updated without creating new global activations. The 2026-09-12 counts above are historical audit counts.


## 2026-09-30: validated runtime name pairs

Machine-readable equivalents live in `skills/runtime-pairs.toml`. The validator requires both sides of each pair to exist before treating their distinct names as intentional. Activation relocation is compared by resolved existing link destinations, rather than raw Markdown path spelling. Archived project support folders without SKILL.md stay preserved and appear separately from invokable skills in the generated index.


## 2026-10-08: repaired activation drift and public review triggers

- `pre-consultation-check-in` is Codex-only: its installed Windows Task Scheduler automation and observed standing authorization are maintained in the Codex package. Claude can query the shared ledger but does not own a second scheduling implementation. The complete reusable package is catalogued; runtime logs are not part of the catalog.
- Kling 0.2.0 is retained and mirrored into both catalogs; older 0.1.3 content is superseded. Codex GWS activation includes the catalogued Windows upload-directory workaround.
- From Codex use `grill-me-claude` for an interview followed by independent review, `grill-with-docs-claude` for persistent context/glossary/ADRs, `claude-review` for an existing work product, and `claude-build` for delegated implementation. From Claude use the corresponding `*-codex` triggers. Generic `grilling` is the interview without cross-provider review; `grill-with-docs` combines that interview with domain modeling. Codex legacy `grill-me-codex` and `grill-with-docs-codex` remain explicit compatibility wrappers to their Claude-review counterparts.


### Claudex updater overlays and bounded global reconciliation

2026-10-08: restored the separate `ai-os-projects/claudex-loop` clone from the declared chaseai-yt upstream, verified commit `8cf5e2c1771c5151d90c12642391d0ba8fa71b0e`. Codex Windows runner/runtime fixes and runner fixtures are explicit support overlays in `system/skill-overrides/claudex/support/codex/claudex-loop`; updated Claude-build troubleshooting remains an entrypoint overlay. The updater preserves verified Codex compatibility wrappers instead of retiring them. It completed without conflicts, then a second dry-run was a no-op. This repairs source maintenance but does not prove a future scheduled due execution.

Global query/lint copies contained obsolete generic wiki instructions and were reconciled to current root-resolving schema rules. GWS newer metadata 0.22.5 and the verified Windows upload workaround are preserved together across existing copies. Global ingest uses the global `lsat-session-lesson` route while this project uses `post-session-recap`: that contextual route difference is retained rather than blindly replacing one. Claudex runtime direction differences remain intentional. Duplicate-name precedence still requires live runtime discovery evidence; static presence is not that evidence. No whole-global-library equivalence claim is made.

## Karpathy teaching execution differs by runtime (2026-10-08)

karpathy-teach is cataloged and activated in both runtimes. Claude delegates to its project karpathy subagent. Its project Stop and Karpathy SubagentStop hooks apply only to turns using that agent or skill; PreToolUse and PostToolUse observe registered example changes. Codex invokes the skill with $karpathy-teach and requires actual registered agent_type karpathy handoff, followed by independent parent evidence review and grading. The original Claude slash spelling is rejected by Codex. Native discovery, real handoff and independent review were verified on 2026-10-09; no generic or direct-workflow fallback remains. Codex has a separate event-based project hook adapter in .codex/hooks.json; definitions require explicit review/trust before activation. Current definitions are Trusted/enabled, with direct native main Stop blocking, execution recovery and unrelated-turn acceptance. Native child blocking remains configured and unit-tested only. Tests and traced execution receipts alone are not native hook acceptance. The optional receipt tracer covers Python; the Claude project hook also recognizes ordinary execution in other supported runtimes. Failed execution remains failure and must be reported honestly. This is a declared implementation difference, not a missing skill.

