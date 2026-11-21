# Static design-skill review, 2026-10-24

## Coverage and limits

Read the shared design router and reused its reviewed skill registry, rather than scanning private conversations or every plugin snapshot. The registry has 2,034 records; 536 existing exact primary/supporting design skill paths were selected into `catalog.json`. These are discovered paths, not 536 distinct skills or proof of activation. Detailed inspection covered Reference to Design, design-resource-library, Taste, high-end-visual-design, Impeccable and its craft/shape references, Extract Design, GSAP core/React, Scroll Craft, frontend-ui-engineering and HTML Handoff.

The bundled skill-audit inventory was attempted with default Python, Python 3.12 and Codex's bundled runtime. Each lacks PyYAML. The existing Tavily environment also lacks it. No dependency was installed and no scanned skill scripts or remote services were run. The catalog remains useful scope evidence; do not claim the scanner succeeded. No invocation telemetry or controlled before/after evaluation was supplied to this static pass.

## Verified defects suitable for small repairs

1. **Impeccable has conflicting authorization rules.** `.agents/skills/impeccable/SKILL.md:10` says to honor the approved brief without another approval round. Lines 21 and 31 require separate user brief confirmation, and `reference/craft.md:15,37` prohibit a self-authored brief and mandate waiting. `reference/shape.md:18-27` mandates user-answer rounds. For Joshua's explicit creative delegation this can stop an already-authorized implementation. Preserve necessary clarification where scope is unresolved; reconcile the entrypoint and both references so an already supplied brief OR explicit delegated decisions satisfy the gate, recording which occurred. This is a textual contradiction, not measured proof that a particular past run stopped because of it.

2. **Impeccable hardcodes the Codex project activation path.** `SKILL.md:18,47` invokes `node .agents/skills/impeccable/scripts/load-context.mjs`, despite line 10 saying to locate the installed support directory. It fails outside this project or under a Claude-only activation. Replace with a resolved absolute skill-directory script path, maintaining the user's project cwd and context override. Check both canonical/runtime copies and support references. Do not change the context loader's project-resolution behavior accidentally.

3. **High-end preset makes the same component architecture optional and mandatory.** `C:/Users/Joshu/.agents/skills/high-end-visual-design/SKILL.md:9,47` preserves flat cards/optional nested enclosures; lines 87 and 95 demand double-bezel architecture for every major card/input/container. Make protocol/checklist conditional on the selected visual direction and retain usability/accessibility requirements. Vendor cache is read-only; edit only the user-maintained canonical copies and synchronize their authorized activations.

4. **Taste conflicts with the chosen animation engine and its own performance guidance.** `.agents/skills/design-taste-frontend/SKILL.md:76,134` demands Framer Motion and restricts GSAP to isolated scrolltelling, despite the user's GSAP UI-transition direction and the top contract preserving the current project. Line 94 says `transition: all` while lines 81-82 require transform/opacity only. Lines 75 and 209 disagree on compulsory versus optional perpetual motion. Keep this an explicitly chosen aesthetic preset; use the project's selected engine, avoid two engines controlling the same properties, make perpetual motion opt-in, and enumerate transitioned properties. Line 46's absolute dashboard-serif ban also conflicts with the accepted editorial dashboard and line 9's project-preservation rule; scope font examples to a preset rather than universal product restrictions.

5. **React Bits script location is ambiguous in a target app.** `.agents/skills/react-bits/SKILL.md:21-22` and refresh instructions use `node scripts/rb-add.mjs` / `scripts/gen-catalog.mjs` without saying these are relative to the skill, while destinations are relative to the caller's app. State `node <resolved-skill-directory>/scripts/rb-add.mjs` while retaining the app cwd. Preserve live registry/body validation, licensing, dependency/prop inspection and no-overwrite semantics. This is a reproducible path ambiguity from the prose, not an executed failing fetch.

## Inspection hypotheses, do not label measured defects

- `gsap-react/SKILL.md:43` says contextSafe callbacks “no-op after unmount.” Context recording/cleanup is not equivalent to cancellation or an automatic mounted-state guard for all future callbacks. Verify against the installed implementation and official source before altering technical guidance; preserve cleanup patterns.
- Extract Design describes a CLI accessibility score as WCAG accessibility scoring without limiting coverage. Clarify automated checks versus full WCAG conformance if updating it. This inspection did not run the CLI or verify package availability; no remote failure is claimed.
- Trigger overlap among general frontend/Impeccable/Taste is expected. Taste and high-end are explicitly non-default presets. Do not consolidate independent specialist skills merely because their descriptions share UI terms.

## Preserve

Reference to Design has strong explicit evidence-versus-inference rules, original composition guidance, scope consistency and real render checks. The resource library explicitly separates registry metadata, actual visual inspection, authentication and licensing. Scroll Craft has deep native-scroll/mobile verification and creative-delegation support. HTML Handoff preserves the current UI, bundles exact output hashes and separates export from redesign/publication. GSAP and frontend engineering retain cleanup, scope, responsive and accessibility safeguards. No retirement is justified by this static review.

## Small useful next tests

1. For Impeccable: a complete delegated dashboard brief in Claude-only and Codex-only project activation. Pass: resolves support files in both, records delegated choices, asks only material unanswered questions and reaches implementation without a redundant approval gate.
2. For Taste/high-end: the approved serif/charcoal dashboard with GSAP and reduced motion. Pass: preserves the specified tokens and engine; does not introduce mandatory nested cards or perpetual effects; static accessibility remains intact.
3. For React Bits: dry inspect helper CLI path/destination from a separate target app. Pass: resolves skill helper while keeping app-relative destination. A live fetch is a separate authorized provider test.

No installed skills were edited by this reviewer. Root owns backups, canonical-copy reconciliation, actual session evidence, authorized repairs and validation.
