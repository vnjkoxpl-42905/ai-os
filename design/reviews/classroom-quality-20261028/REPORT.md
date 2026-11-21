# Classroom design quality review

2026-10-28. Target: production /classroom, signed-in teacher view. Independent reviewer Claude Code2.1.309, observed claude-sonnet-5-5, CLI default requested. Codex coordinated. No application edits or release.

## Provisional rubric

| Dimension | Points |
|---|---:|
| Ease of use/task priority |11/20|
| Information organization |9/15|
| Visual hierarchy |8/15|
| Palette/material depth |9/20|
| Typography/spacing/detail |9/15|
| Accessibility/responsive/states |5/10, partial source assessment|
| Motion |Unassessed /5|

Assessed subtotal51/95. Claude withdrew its preliminary overall estimate in round2; no final100-point grade is supported. These are subjective diagnostic scores, not measured usability outcomes. Phone, keyboard and motion were not exercised in this review. No animation is not inherently a quality defect.

## Why it feels beige on beige

Source-consistent page canvas #f7f4ee and home surface #fbf9f4 have only slight tonal separation. Peach sidebar wash adds warmth across the environment. Teacher region styles remove borders and weaken contact shadows. Multiple equally pale rounded regions receive similar emphasis. Broad14px important overrides flatten control/body hierarchy. Large confirmed-empty regions consume attention while agenda/messages remain secondary.

## Recommended direction

Off-white and soft charcoal, preserving warmth without beige saturation. Scope teacher tokens, increase surface/edge separation, retain controlled contact shadows, condense confirmed empty states, use selective charcoal on an actual after-session action. Do not invent a hero or task priority engine. Retain distinct payment/access meanings. Clarify Not connected. Use deliberate type scale and accessible existing menu patterns. Measure control/focus contrast and verify interaction defects before declaring runtime failures. Student/shared sidebar changes require separate visual coverage.

Full findings and limitations: claude-round1/claudex-xoxb7rzq/result.json. Host dispositions: DISPOSITIONS.md. Revised acceptance specification: PLAN.md. Second round APPROVED the refined recommendation plan with no unresolved material plan findings. This is not approval of implemented code or proof of perfected runtime. Result: claude-round2/claudex-lfw6umta/result.json.

## Implemented locally after user approval

User said fix it, then requested the earlier calendar strip and more sophisticated components restored. Teacher-scoped off-white stage, one light work sheet, quiet agenda/decision rail and open lower ledgers replace equal pale cards. Interactive seven-day strip uses real agenda model and calendar timezone; snapshot freshness/coverage, partial data, past timed starts, date-only and DST behavior covered. All-empty healthy summary hidden; setup/error retained. Read/unread/backend/routes unchanged. More uses accessible menu with tested and observed booking sheet focus handoff.

Five final affected suites pass51/51. Final frozen application typecheck (tsconfig.app.json) and full npm production build including prebuild/postbuild PASS. CUA rendered widths320/390/684/1024/1441: scrollWidth equals clientWidth at every size; calendar isolated scroll on narrow. Actual selected hover/text13.74:1, selected metadata9.37:1, active search border4.50:1. Normal menu interaction and reduced-motion0s transition/animation observed. Keyboard last calendar day selected and scrolled into view; concise live announcement observed in DOM. No actual screen-reader or physical-device claim.

Independent final Claude inspection APPROVED scoped frozen code with no material findings and viewed final desktop and390px images. Findings remaining: low Label in Name wording mismatch for None shown tiles; late truncated days could be more explicit Unknown even though None shown and caption qualify absence; caption spacing/duplicate-rule nits. No post-review edits. No perfect100score assigned.

Preservation: global classroom.css/index.css and unrelated mcp/index.ts hashes unchanged. Student-style prefix matches after normalizing one teacher PostSession disabled-cursor change; all new selectors teacher-scoped. Student runtime not inspected. Synthetic sidebar simplified; production Home ancestors match. No auth/backend/student writes, commit, push, merge or publish.

Concurrent release boundary: git ls-remote verified main29cf18a8d0fb0ef0c1106f8b976f26db13b9a3c4 while local base18fc8af7 remained unchanged. This local candidate is not integrated with that newer Teacher Home release. GH CLI was unauthenticated in this process; readonly git remote succeeded. Do not publish this candidate wholesale over concurrent changes.

Evidence: after-desktop.png, viewport-390.png, responsive.json, state-checks.json, contrast.json, preserved-hashes.json; final review under claude-inspect-final.

## Student account controls follow-up

Local credit, feature-access and individual-booking-link controls: [implementation, checks and limits](account-controls/REPORT.md). This is a separate local follow-up and does not establish publication or live student mutations.

## Direct student credits and scheduling, 2026-10-28
Local candidate and review: [report](student-credits-scheduling/REPORT.md). Not published; backend source deployment and production account acceptance remain separate.
