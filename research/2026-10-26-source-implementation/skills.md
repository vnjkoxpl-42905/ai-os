# Practical skill improvements, 2026-10-26

The current user request authorizes practical adoption and routine choices. No external send, new remote install, or deletion occurred.

| Item | Outcome | Evidence and remaining limit |
|---|---|---|
| AQ-003 | Implemented locally | Added identical Verify by plan guardrail to both root manuals. Guardrails sections compare equal. Manuals were already 19,205/19,200 bytes; now 19,350/19,345. Fresh-session adoption remains unverified. |
| AQ-004 | Keep existing models | Read prior two-skill benchmark in references/claude-plus-codex.md. It does not support cheaper model equivalence. No new model benchmark or model setting change; historical measurements stay dated. |
| AQ-005 | Skip duplicate editor | Read complete prior comparison research/no-ai-slop-vs-humanizer-2026-10-14.md. It supports keeping humanizer on that one draft, with stated prompt contamination and limited detection coverage. No new SlopMonster comparison, upstream inspection or install. |
| AQ-008 | Inventory reconciled | All six named utilities exist in both home Claude and home agents skill roots; neither catalog has them. Declared intentional existing shared home packages in skills/PARITY.md, preserving package homes and avoiding duplicate project activation. Presence is not functionality. No corruption repair claim. |
| AQ-009 | Existing implementation confirmed; decision owned by parent | Both catalogs already require draft only, duplicate draft lookup and fail-closed price/link check. Parent should supersede historical auto-send decision using current explicit user/root instructions. Live Stripe amount/identity verification remains undone. |
| AQ-012 | Partial implementation | Applied two teaching fixes (define a term before use; new scenario for practice) and interview plain-term fix to Claude/Codex/Gemini catalogs. Existing installed copies synced; provider-specific grill-me differences preserved. Prior 2026-10-14 report is not a new 30-day scan. Did not apply blanket apology/promise restriction because approved sample contains those phrases. |
| AQ-013 | Conservative partial cut | Removed only The detailed standard is maintained in one place. from lsat-u-voice, 50 bytes in each catalog. Guardrails retained. No claim five-skill audit is finished or real-run quality measured. |
| AQ-038 | Deferred full audit | Existing concrete interview owner boundaries preserved. No briefing consolidation justified without reading actual outputs. No new routing-collision acceptance claim. |

## Checks

- Targeted copy updater wrote 9 files across 8 existing installs for lsat-u-voice, grilling and grill-me, with built-in backups/receipts. Gemini existing project entrypoints synced separately. It also reconciled the existing home-agents grill-me agents/openai.yaml from catalog; no new activation.
- Root guardrails compare byte-identically after newline decoding. Per-file edit sizes: skill-edits.json.
- Full check-skills.py initially reported three Gemini entries stale from these edits (subsequently repaired), plus pre-existing cli-anything-aios parity and six handoff dependency peer errors. Loaded home drift warnings are broad existing state, not resolved by this bounded work. Re-run result reported to parent.

## Sources actually consulted

- wiki/sources/matt-pocock-system-claude-skills-austin-marchese.md and its archived source: raw/sources/clips/matt-pocock-system-claude-skills-austin-marchese/Matt Pocock's EXACT System To 10x Your Claude Skills.md.
- wiki/sources/stop-prompting-claude-karpathy-method-austin-marchese.md and raw/sources/clips/stop-prompting-claude-karpathy-method/Stop Prompting Claude. Use Karpathy_s Method Instead..md.
- wiki/sources/consultation-followup-workflow-memory-2026-07-07.md and complete archived workflow raw/sources/consultation-followup-workflow-memory-2026-07-07/post_consultation_follow_up_workflow_memory (1) (1).md.
- research/send-backs-2026-10-14.md, research/skill-noop-cuts-2026-10-14.md, research/no-ai-slop-vs-humanizer-2026-10-14.md, and benchmark section references/claude-plus-codex.md. These are prior local observations, not independently rerun results.
- Current affected skill entrypoints and six home-package entrypoints (combined tool output truncated some large package descriptions; no complete support-tree audit claimed).

## AQ-009 actual dry execution, 2026-10-26

Both catalogs and all three existing home roots (.claude/.agents/.codex) contain the checker with matching SHA-256 d32a9f6ee6c839cb5ad42bb49fa9d620dc0555953f4456159840c2bd04928629. Each SKILL.md routes explicitly to python scripts/check_links.py --live and requires NEVER send. No project activation exists for this skill; none was created. Ran both standard and higher dry tier checks in all five roots: all 10 exited 0, PASS with three price/link pairs. Every higher check warned that the $60 Stripe ID has 18 characters versus 23 for others. Matching scratch standard draft exited 0 with draft matched; deliberately mismatched scratch links exited 1 FAIL. No live flag, provider request, Gmail write or send occurred. This validates syntax/template matching and fail-closed draft mismatch only; Stripe identity/amount and Cal.com liveness remain unverified. Full dry results: consultation-link-check.json; scratch fixtures/results retained beside it.

## AQ-009 live read-only check, 2026-10-26

Inspected the complete helper before live execution: --live sends urllib GET only for CAL-matching Cal.com booking URLs, with 20-second timeout. It does not request Stripe URLs, submit a form, create a booking or send mail. Ran the existing home .agents checker with --live --tier standard: exit 0, PASS 3 pairs, no network WARN or FAIL. For the one Cal.com session-link, the helper's no-warning success branch means HTTP 200. Ran --live --tier higher: exit 0, PASS 3 pairs, same unusual $60 ID warning; that tier contains only Stripe links, so no live HTTP request occurred. This proves the standard booking endpoint responds; the check does not prove event identity, available slots, Stripe link liveness or charge amounts. Stripe backend amount verification remains outstanding.
