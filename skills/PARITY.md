# Skill parity baseline

## 2026-10-24: Chrome Extensions and Modern Web Guidance catalogue repair

Chrome Extensions and Modern Web Guidance were present as project Codex activation trees but missing from both catalogues and the project Claude activation. Both complete trees are now catalogued under each runtime and activated as ordinary project copies for Claude Code and Codex. Every file was SHA-256 compared against the existing Codex tree, including supporting references and the shared design-hub route. No global activation was added. Evidence: research/2026-10-24-skill-repair/catalog-hashes.json.

## 2026-10-09: Persona Agent Creator

`persona-agent-creator` is catalogued and activated as matching project copies in both runtimes. Its host-aware factory procedure requires actual native person-agent registration and an independently grading entry skill. It reuses existing ingest/schema conventions, derives each person's own rules, and explicitly tests new hook scope instead of inheriting Karpathy's hardcoded guard. Codex invokes `$persona-agent-creator`; generated person agents use each host's native configuration. No global activation was added.

## 2026-10-15: Geminex Codex activation

The seven Gemini-origin Geminex workflows are now present in the Codex catalog. Project activation under `.agents/skills/` remains pending because this session grants that directory read-only access. `geminex-loop` and `geminex-route` are shared bidirectional entry points. Codex-specific counterparts `gemini-review`, `gemini-build`, `grill-me-gemini`, and `grill-with-docs-gemini` pair with Gemini-side `codex-review`, `codex-build`, `grill-me-codex`, and `grill-with-docs-codex`; these pairs are recorded in `skills/runtime-pairs.toml`. `grill-by-gemini` is a Codex-host shortcut with no distinct Gemini-host counterpart. The runner and its references remain included in the Codex copies.

Declared single-runtime skills. `check-skills.py` fails on **undeclared** asymmetry only:
when you deliberately add a skill to one runtime and not the other, add it here in the same
commit. When a skill shows up as undeclared drift, either activate it for both runtimes or
declare it here **with a reason**.

Every entry below carries its justification. An entry without one is not a decision, it is a
snapshot — which is what this file was until the audit noted below.

**Audited 2026-09-12.** The Windows parity pass repaired the cross-platform validator,
catalogued kling-cli for both runtimes, and ported 25 previously undeclared Claude-only
skills to Codex: academy-guide, algorithmic-art, brand-guidelines, canvas-design,
claude-api, claude-handoff, code-review, discernment-nudge, doc-coauthoring,
docx, implement-spec, internal-comms, loop-me, mcp-builder,
migrate-to-shoehorn, pdf, pptx, retro, session-recap,
setup-ts-deep-modules, slack-gif-creator, theme-factory,
web-artifacts-builder, wizard, and xlsx. (Names are plain text on purpose: backticks would declare them single-runtime exceptions to check-skills.py, and these are catalogued for both runtimes.) Current catalog counts:
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

### Bootcamp builder shared workflow (2026-10-11)

`bootcamp-builder` now has matching Claude/Codex catalogs and project activations. The workflow uses host-available questions, preserves existing authorization, resolves current source paths, and reads the accumulated teaching-preference reference. The previously installed global copy was updated in place; no new global activation was added.

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

`second-brain-ingest` is now catalogued and activated for Codex and Claude, with matching Gemini copies. The obsolete Claude-only exception is removed. The old `second-brain-ingest` compatibility alias was deleted on 2026-10-14, and `ingest` was renamed `second-brain-ingest` the same day. Query and lint are separate shared workflows. Current-vault policy lives in `system/schema/llm-wiki.md`. Existing global copies were updated without creating new global activations. The 2026-09-12 counts above are historical audit counts.

`second-brain-task` (2026-10-14) is catalogued and activated as identical project copies for Claude, Codex and Gemini. It owns the AI action queue (`references/ai-workspace/action-queue.md`) and the LSAT U idea queue (`wiki/lsatu-idea-queue.md`); `second-brain-ingest` adds items and `pickup` reads only their counts. No global activation was created.


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



## 2026-10-10: session transcript intake separated from knowledge ingestion

`transcript-intake` is catalogued and activated as matching project copies for Claude, Codex and Gemini. It owns student/session source retrieval, filing, reconciliation and private distillation, reusing the existing shared Calendar/Drive procedure. `second-brain-ingest` dispatches session transcripts to that skill; its compilation pipeline remains for reusable knowledge sources. `post-session-recap` continues to own student-facing lessons. No new global activation or external operation is implied.


## 2026-10-10: knowledge pathway and existing user-level dispatchers

Claude/Codex project ingest, query and lint share bounded index navigation and a usable-knowledge retrieval check. Public videos stay outside session transcript-intake. Existing user-level ingest/compatibility/query/lint entrypoints now resolve the target vault project skill (catalog fallback); no new global skill activation was created. Earlier user-entrypoint bytes and hashes are preserved under research/second-brain-pathway-2026-10-10/. Fresh runtime discovery is a separate check from these files.


## 2026-10-10: reviewed skill adaptations and preserved compatibility

The full-catalog repair preserves provider identities and runtime-specific host calls. Current Codex `codex-build` and `codex-review` activations are explicit compatibility wrappers to `claude-build` and `claude-review`; their inert Codex catalog copies preserve this route. Current primary triggers remain the provider named by the caller. No additional global activations were created.

Existing catalog/activation drift was reconciled, including Gemini copies. Three previously uncatalogued Gemini browser-operation skills remain Gemini-only; they are not automatically ported or activated for Claude/Codex. The validator skips inactive/snapshot/fork container directories and checks Gemini entrypoints against their owning catalog without imposing feature parity.

Targeted local adaptations supersede old verbatim-upstream invocation claims where the actual host lacks a literal Skill/Task tool. Matt Pocock compare-and-swap maintenance preserves these edits for review. Claude-host Codex build/review corrections persist under `system/skill-overrides/claudex/claude/`; Claudex offline dry run is a clean no-op. Never use adoption/reset to discard these changes. Native skill discovery and duplicate-name precedence are distinct from static catalog validation.

[Repair report, tests and remaining dependencies](../audits/skills-2026-10-10-repairs/SUMMARY.md). Historical `_snapshots` and `_project-forks` remain preserved.

## 2026-10-11: restored support and verified native loading

Existing research-deep packages now include the recovered validator and field contract; the actual PyYAML environment is isolated outside the vault. Existing bootcamp-parity-audit packages resolve three dated reconstructed benchmark references in the vault, with current-source provenance and historical limits. No missing runtime activation was automatically added.

Watch setup, hook payloads and central credential resolution match across existing runtime copies, including the global Claude copy verified by fresh native startup. Claude loads via its actual Skill tool; Codex loads via supported file reads. Intentional provider-named build/review differences remain unchanged. Native registry discovery is valid, but Codex's bounded skill-description rendering still limits universal automatic selection. [Current verification](../audits/skills-2026-10-11-native/SUMMARY.md).

`claudex-loop` is installed for Gemini (2026-10-12) as a copy of the Claude-host version so the Gemini `codex-build` and `codex-review` entry points resolve. The runner only knows `claude` and `codex` as providers: from Gemini it can hand work to Codex, but Gemini is never a reviewer or builder in the loop.

## 2026-10-21: design and motion skills from Chase AI clip

`design-taste-frontend`, `extract-design`, and `impeccable` are active in both Claude and Codex from the existing customized catalog copies. Their source and local customization are documented in [the clip summary](../wiki/sources/top-7-claude-design-skills-chase-ai.md). Claude's existing, more extensive user-level Impeccable copy remains preferred by Claude; it was preserved, so the validator reports that one shadowed activation. `playwright-cli` was already active in both runtimes. The official GSAP skill set (`gsap-core`, `gsap-frameworks`, `gsap-performance`, `gsap-plugins`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-utils`) and the React Bits fetch helper (`react-bits`) are now catalogued and activated in both runtimes. Matching copies are intentional: each has the same purpose on Claude and Codex. React Bits component source is not vendored; the helper fetches from its registry, checks lexical and symlink-resolved destination containment, refuses overwrites, and does not install project dependencies without explicit authorization. No global CLI install was performed. The clip's final “transition skill” is unnamed and remains unresolved under AQ-017.

## 2026-10-23: Shared design resource library
The design-resource-library skill is catalogued and activated as matching project copies for Claude and Codex. It maps all25 PDF tips to installed capabilities or optional resources, preserves creative freedom, and adds no global skill activation. React Bits pointer corrections are mirrored across both catalogs and activations.



## 2026-10-24: Reference to Design activation

Joshua explicitly authorized active-list installation. reference-to-design is copied with all supporting files and MIT notice into both runtime catalogues, project activations and existing global discovery roots (.claude/skills, .agents/skills and .codex/skills). All seven copies match and point to design/README.md. Origin commit and hashes are recorded in research/2026-10-24-reference-to-design-activation/receipt.json.

## 2026-10-25: CLI-Anything for Codex and Claude

CLI-Anything is installed for both runtimes. The Codex package is the upstream self-contained Codex skill with its complete vendored methodology, command specifications, guides, templates, helper scripts, and preview protocol. Claude Code uses the upstream full plugin (slash commands, HARNESS.md, guides, scripts, and templates) plus a project skill entrypoint. These packages differ to match each host's native integration; both cover build, refine, test, validate, and list. The Codex package is catalogued and activated as `cli-anything`. Claude has the full upstream plugin installed at user scope. Its Claude-specific adapter `cli-anything-aios` is catalogued but not activated in the project; a copy is also preserved under `skills/claude/_inactive/cli-anything-aios`. The Claude loader treats the `cli-anything` slash command as a duplicate and gives the installed plugin precedence; the user-level plugin is the active Claude integration. Both user-level installs must be restarted to discover them.


## 2026-10-26: Existing home-level utilities deliberately remain outside project activation

AQ-008 verified that `onboard`, `link`, `3d-brain`, `herdr`, `orca-cli` and
`reverse-engineer-anything` are installed in both `~/.claude/skills/` and
`~/.agents/skills/`, with no project catalogs. They are existing shared home
utilities, not Claude-only missing ports. Keep their package-owned complete
homes rather than activate a second project copy. `onboard` is explicit setup
for a starter workspace; `link` changes routing on request; `3d-brain` is an
optional visualization with bundled application; Herdr and Orca guides depend
on their own installed runtime; REA owns version-matched analysis guides.
Presence does not establish functionality. Existing runtime adaptations remain
preserved; no replacement or new activation was performed.


## Taste Skill v2 replacement (2026-10-27)

`design-taste-frontend` now contains the complete upstream Taste Skill v2 payload at `Leonxlnx/taste-skill` commit `12af471f627f866411b4bd785b19646d3672784c`. Both catalogs, both project activations, and the three existing home runtime copies match. The old bodies are backed up outside activation paths. Only a narrow AI OS execution contract is added to upstream SKILL.md; the old aesthetic body is replaced. See the skill `UPSTREAM.md` for provenance and upstream packaging limits.

`post-session-recap` (2026-11-17): the Claude copy gained `references/house-look.md`, `references/examples/sara-2026-11-16-note-builder.py`, a calibration section and executor gotchas, and short SKILL.md edits (fusion pass, one scope per note, homework resolved first, open the render early). The Codex copy was not changed and still lacks them, in addition to the homework section it already lacked. Mirror when Codex next runs post-session recaps.
