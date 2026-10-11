# Claude long-body semantic review

Reviewed 2026-10-10. All 26 assigned canonical SKILL.md files were read in full, with truncated tool-output segments recovered through bounded reads. Current SHA-256, bytes and line counts are in the JSON companion. These are static findings: no unknown scripts, provider API calls, browser writes, skill edits, deletions or native hook activation were performed. Supporting resources were checked selectively for existence, not read wholesale.

The reviewed method starts from inspectable mechanisms and evidence: [hot](../../wiki/karpathy/hot.md) and [rules](../../wiki/karpathy/rules.md). No claim is made that these catalog skills passed runtime application or trigger evaluations.

## claude-api

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/claude-api/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Correct Anthropic API capability, not a duplicate of Codex automation. Overbroad discovery and contradictory research instructions need repair.
- **Evidence:** Frontmatter lines 3-6 triggers any natural-language generate/summarize/extract/rewrite and unstated provider; Before You Start asks to switch non-Anthropic code despite SKIP; line 32 requires WebFetch undocumented bindings, Common Pitfalls near end says do not WebFetch before writing. Cached models/prices are not live verified.
- **Recommended repair:** Narrow to Anthropic implementation/API questions, honor explicit provider; choose one documentation-then-compile policy; verify live model availability before use.

## claude-automation-recommender

- **Disposition:** keep-with-host-overlay
- **Receipt:** skills/claude/claude-automation-recommender/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful read-only tailored recommendations. General MCP/default automation advice needs the machine's CLI-first and cost rules.
- **Evidence:** Body recommends only 1-2 items/category and no changes. MCP recommendation matrix includes services already reached through gws/gh/other CLIs. Host/tool metadata is Claude-oriented.
- **Recommended repair:** Keep as recommender, check current connections before proposing another server or paid automation.

## command-development

- **Disposition:** keep-compatibility-reference
- **Receipt:** skills/claude/command-development/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Legacy command reference can be useful for existing third-party plugins. It should not create a second AI OS activation path.
- **Evidence:** Opening legacy note recommends new skills already. Later examples still build .claude/commands, use $ARGUMENTS/$1 and $IF conditional templates, and plugin commands.
- **Recommended repair:** Scope to maintaining legacy plugin commands; route new AI OS capabilities to skill creation and project/catalog copies. Verify special conditional syntax before recommending it.

## design-taste-frontend

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/design-taste-frontend/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** A deliberately opinionated visual preset, not a universal product policy. Undefined dial and compulsory animation conflict with accessible app work.
- **Evidence:** Baseline defines DESIGN_VARIANCE but line 50 uses LAYOUT_VARIANCE >4. Sections 4/9 require perpetual component motion and universal bento baseline without reduced-motion gate; forced libraries/RSC assumptions may not match Vite.
- **Recommended repair:** Fix dial; make preset explicit, preserve project stack/design system, make motion conditional and honor reduced motion. Retain layout/component quality guidance.

## doc-coauthoring

- **Disposition:** keep-with-fast-path
- **Receipt:** skills/claude/doc-coauthoring/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful staged drafting and reader test, not redundant with format editors. Repeated permission/questions and root output default add friction.
- **Evidence:** Stage 1 offers workflow and initial questions; section drafting asks 5-10 questions and 5-20 options. Lines 135/367 assume create_file host tool; local-output guidance uses working directory.
- **Recommended repair:** Use existing context first; scale drafting gates to ambiguity, respect already-authorized request, adapt file tools and file output in owning folder.

## emil-design-eng

- **Disposition:** keep
- **Receipt:** skills/claude/emil-design-eng/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Distinct interface polish method with concrete before/after reviews, motion-frequency decisions and accessibility.
- **Evidence:** Full 679-line body includes Accessibility/prefers-reduced-motion at tail, touch-device hover gating, interruption/performance and clear Before/After table. Initial empty invocation only advertises course.
- **Recommended repair:** Keep as optional UI polish lens; improve empty-invocation response to describe available help. Do not strip its reduced-motion policy.

## graphify

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/graphify/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful optional derived graph, but current instructions can lose identity, retain stale relationships or reject valid output, and create competing intake.
- **Evidence:** Lines 291/347: agent Output ONLY valid JSON while success requires .graphify_chunk_NN.json on disk, with no explicit write instruction in exact prompt. Line 338 filename-stem entity IDs collide across same basename directories. Lines 914-921 remove deleted-file nodes then update new graph, leaving removed nodes/edges from modified files. For add writes ./raw and automatic update; install uses --break-system-packages; claude install writes manual-owned CLAUDE.md.
- **Recommended repair:** Require file output or parent writes returned JSON; path-qualified identity aligned with extractor; replace affected-file subgraph on modification. Route sources through existing ingest, artifacts/deps to approved homes, and native instruction integration only as reviewed proposal.

## hook-development

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/hook-development/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Claude hook reference must be runtime-scoped and internally schema-consistent. It cannot prove native Codex hook trust.
- **Evidence:** Lines 64-79 require plugin hooks wrapper, line 115 says user-settings events directly top-level, Plugin Hook Configuration later omits wrapper. Prompt event supported list conflicts with later PostToolUse prompt example. Local currently supported schemas need authoritative verification.
- **Recommended repair:** Fix contradictory examples after current host/schema check; explicit Claude scope; route Codex project hooks to .codex/hooks.json and /hooks trust. No native activation claimed.

## image-to-code

- **Disposition:** keep-as-explicit-preset
- **Receipt:** skills/claude/image-to-code/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Image-first design method can add value, but broad mandatory regeneration is expensive and can replace authoritative supplied visuals.
- **Evidence:** Claude catalog frontmatter names Codex. Sections 2/4 require generate first and one image per section; sections 5/6 prohibit crops and assert regenerated render is same design. Text extraction lacks approved-copy/factual authority gate; 38 repeated sections.
- **Recommended repair:** Narrow to requested image-first exploration; preserve user supplied image when faithful implementation requested; cap iterations based on observable quality, use approved copy, consolidate repeated body.

## json-canvas

- **Disposition:** keep
- **Receipt:** skills/claude/json-canvas/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Distinct JSON Canvas format authoring, unrelated to graph extraction or note ingestion.
- **Evidence:** Body covers text/file/link/group nodes, edges, colors, geometry, JSON validation and Obsidian reopen test. 16-character ID convention is asserted as field requirement rather than clearly a generation convention.
- **Recommended repair:** Retain; verify exact Canvas spec before treating ID length convention as universal validity requirement. No live renderer test performed.

## kling-cli

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/kling-cli/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful account/parameter/credit-aware video/image tool, with overbroad triggers and unrequested feedback behavior.
- **Evidence:** Frontmatter includes generic install/MCP/global/region and image/video generation. Lines 300-307 explicitly allow silent agent-initiated feedback without authorization. Body otherwise verifies who_am_i, model parameter support and prevents automatic paid retry.
- **Recommended repair:** Narrow to Kling tasks; feedback only when user authorized; retain paid submission/identity/region discipline and use efficient status polling.

## lsat-lab-mega-set

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/lsat-lab-mega-set/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Distinct full-PT LR set assembly with useful count/URL gates, but destructive recovery and stale paths need correction.
- **Evidence:** Lines 55/141 log to ~/ai-os/output/lsat-u/lsat-lab-set-log.md but lines 40/234 use output/lsat-lab-set-log.md. Line 120 deletes bad created set automatically; line 127 Cmd+A assumes Mac; footer assumes S1 Q1.
- **Recommended repair:** Use canonical owned log path, Windows/browser documented shortcuts, ask exact deletion confirmation, verify actual first section rather than hardcode S1.

## lsat-lab-transcribe

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/lsat-lab-transcribe/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Detailed capture workflow with strong completeness/provenance intent, but resume and first-item ordering can skip a question.
- **Evidence:** Line 99 confirms NEXT pointer then advances; line 120 per-question loop starts with click Next. Body infers styles from prose heuristics, uses stale ref_34 example, asserts authorship wholesale and converts -- to em dash.
- **Recommended repair:** Capture current confirmed item before advance; separate last-completed and next pointers. Verify UI style label, dynamic refs, retain raw transcription and limit normalization to verified cases; document actual source rights.

## math-olympiad

- **Disposition:** keep-optional-and-fix
- **Receipt:** skills/claude/math-olympiad/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Specialized mathematical proof capability is distinct and not useless merely infrequent. Generic counterexample triggers and agent budget need scoping.
- **Evidence:** Frontmatter includes generic find a counterexample/is this proof correct. Line 85 launches 8-12 simultaneous agents despite finite slots; body offers different model-tier counts, chooses hard interpretation by presumed intent, and small-n patterns as proof structure.
- **Recommended repair:** Explicit mathematical/competition domain; budget waves to available slots; resolve ambiguity from wording; small cases guide a general proof but do not replace it.

## mcp-builder

- **Disposition:** keep
- **Receipt:** skills/claude/mcp-builder/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Building MCP servers is distinct from configuring an existing server/plugin.
- **Evidence:** Body has research-first SDK/protocol guidance, Python/TypeScript tracks, build/Inspector validation, workflow-friendly tools and read-only stable evaluation tasks.
- **Recommended repair:** Retain, with project policy least privilege and only required tools/coverage. Build/Inspector not run in this read-only audit.

## mcp-integration

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/mcp-integration/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful Claude plugin MCP integration reference. Transport terminology/schema and broad external-service triggers need correction.
- **Evidence:** Line 3 includes connect external service; line 120 and transport table label HTTP as REST. Lifecycle says servers start on plugin enable but line 405 says on demand. .mcp.json example direct map differs from plugin-structure mcpServers wrapper.
- **Recommended repair:** Narrow explicit Claude MCP integration, preserve CLI-first service routes, explain MCP HTTP transport not arbitrary REST, reconcile lifecycle and verify schema/transport support live before use.

## notebooklm

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/notebooklm/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Distinct source-backed artifacts/chat, with explicit notebook IDs valuable. Examples and certainty overstate reliability.
- **Evidence:** Lines 205/228/235 return task_id but automation line 288 parses artifact_id. Line 474 claims reliable operations always work despite errors/re-auth sections. Line 116 blanket confirmation for download even already-authorized full automation; timing examples differ.
- **Recommended repair:** Verify CLI JSON output, parse actual IDs; qualify reliability/account limits and use status rather than fixed promises; retain explicit notebook IDs and use existing authorization for requested downloads.

## obsidian-bases

- **Disposition:** keep
- **Receipt:** skills/claude/obsidian-bases/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Dedicated .base views/formula authoring adds value apart from Markdown/canvas/graph.
- **Evidence:** Full body defines filters/properties/formulas/views, cards/list/map/table, syntax validation and reopen in Obsidian check.
- **Recommended repair:** Keep optional format skill, preserve current AI OS frontmatter/schema and avoid parallel intake. Renderer not tested.

## obsidian-markdown

- **Disposition:** keep-and-fix-overlay
- **Receipt:** skills/claude/obsidian-markdown/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful Obsidian syntax reference, but blanket internal wikilinks policy can conflict with portable canonical AI OS links.
- **Evidence:** Lines 14/19 mandate wikilinks internally and Markdown links external only; frontmatter broadly triggers all .md work in Obsidian.
- **Recommended repair:** Honor owning schema/current link style first; narrow to Obsidian syntax/render features. Do not automatically rewrite every portable Markdown link.

## pdf

- **Disposition:** keep-minor-fix
- **Receipt:** skills/claude/pdf/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Distinct PDF extraction/OCR/merge/forms capability should stay.
- **Evidence:** Line 25 concatenates page.extract_text() without None guard; OCR example needs installed Tesseract and Poppler beyond Python dependencies. FORMS.md and REFERENCE.md exist.
- **Recommended repair:** Guard image-only/empty extracted pages, report OCR prerequisites and missing sections; retain dedicated format workflow.

## plugin-settings

- **Disposition:** keep-and-fix
- **Receipt:** skills/claude/plugin-settings/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful configurable plugin state, but shell parsing and reload guidance can fail.
- **Evidence:** Lines 68-83 combine set -euo pipefail with optional grep pipelines; missing field aborts before defaults. sed range reads later --- body sections too. Runtime hooks read state each invocation but lines 200/369 say settings changes require restart. Quote-only escaping insufficient YAML serialization.
- **Recommended repair:** Use actual YAML parsing/serialization and missing-field defaults, bound first frontmatter; distinguish hook-definition reload from next-invocation state reads.

## plugin-structure

- **Disposition:** keep-and-fix-examples
- **Receipt:** skills/claude/plugin-structure/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Claude plugin organization reference is distinct from ordinary AI OS project skill activation.
- **Evidence:** Hooks example direct event root conflicts hook-development required wrapper; line 242 .mcp.json mcpServers wrapper conflicts mcp-integration direct map. Frontmatter example Skill Name conflicts own kebab-case convention.
- **Recommended repair:** Verify host schemas and align examples across reference skills; state project activation policy wins outside actual plugin development.

## pptx

- **Disposition:** keep-with-host-overlay
- **Receipt:** skills/claude/pptx/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Distinct slide creation/editing with content+visual QA is valuable.
- **Evidence:** Body requires render/inspect every slide and OOXML validation; assumes preinstalled Node/React/sharp/office tools and sandbox-specific soffice advice. Slide-image cleanup rm pattern can affect shared output directory.
- **Recommended repair:** Use workspace runtime detection; all intermediates in dedicated task directory; retain visual and schema QA. No slide generation executed.

## skill-creator

- **Disposition:** keep-and-fix-evaluation
- **Receipt:** skills/claude/skill-creator/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Best candidate primary skill-authoring workflow; evaluations and negative trigger cases useful, but broad description advice and held-out selection need repair.
- **Evidence:** Line 67 encourages pushy trigger on any company data; line 394 repeatedly evaluates candidates on held-out test and selects best by test score, making that split validation rather than untouched final test. Tool timings/browser commands are host-specific.
- **Recommended repair:** Use explicit positive+negative boundaries, validation for selection plus untouched final test, adapt actual tools/timing receipts and project/catalog activation; preserve creator baseline iteration.

## skill-development

- **Disposition:** retain-plugin-reference
- **Receipt:** skills/claude/skill-development/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful Claude plugin packaging/progressive-disclosure reference, overlapping generic creation triggers should delegate core authoring to one primary creator.
- **Evidence:** Frontmatter create a skill/write new skill overlaps skill-creator and writing-skills; Steps3/5 plugin directory/testing are unique. Testing uses cc --plugin-dir alias without verified availability; metadata example Skill Name conflicts canonical kebab-case.
- **Recommended repair:** Narrow to Claude plugin skill packaging/structure, compose primary creator evaluations, resolve actual claude executable, preserve AI OS catalog+activation policy.

## writing-skills

- **Disposition:** keep-testing-reference-and-fix
- **Receipt:** skills/claude/writing-skills/SKILL.md; full body reviewed; current hash in JSON.
- **Reason:** Useful pressure/wording tests and conditional contracts; destructive universal discipline and duplicate creator trigger are unsuitable as automatic primary authoring.
- **Evidence:** Lines 382 onward require delete existing skill on any untested edit with no exceptions, conflicting preserve/explicit-deletion policy. Required superpowers:test-driven-development needs installed resolution. Max1024 total frontmatter is overbroad spec interpretation; push deployment commit/push as mandatory.
- **Recommended repair:** Retain pressure/negative tests as optional creator reference; replace deletion with preserve/revert proposed scoped changes under authorization, narrow trigger to behavioral skill testing, verify dependency and exact current metadata limits; publish only in authorized scope.

## Seven-rule review

| Rule | Grade | Evidence |
|---|---|---|
| Mechanism reconstruction | Pass | Concrete data flow and ordering failures identified, such as graph update retaining modified-file nodes and transcript advance skipping current item. |
| Small baseline | Pass | Existing canonical bodies assessed before proposing replacements; no parallel skill implementation. |
| Prediction/run/comparison | Not applicable | No implementation or paid/side-effect workflow executed in read-only review. |
| Counterexample/fix | Needs improvement | Static counterexamples and repairs supplied; isolated runtime cases must be run before changes are accepted. |
| Relevant execution | Not applicable | Hash/line/existence inspection only, not claimed as skill execution. |
| Explicit assumptions | Pass | Runtime support, model currency, renderer behavior and full support-tree correctness not asserted. |
| Justified simplicity | Pass | Retain distinct capabilities; narrow overlapping creator references instead of deleting useful source material. |

## What I ran

Bounded Get-Content body reads, selected exact evidence lookups, selective Test-Path support checks and Get-FileHash receipts.

## What came out

26 full-body rows with justified retention and concrete repairs; no catalog deletion recommendation based solely on infrequent use.

## What I changed

Created only this review and its JSON companion. No skills or settings changed.

