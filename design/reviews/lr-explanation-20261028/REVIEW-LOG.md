# Claudex LR explanation refinement

- Host/planner/builder: Codex. Independent plan reviewer and final inspector: Claude.
- Models: CLI configured default, unresolved until observed. No override or inspection opt-out.
- Scope authorized: implement local visual refinement; no merge/publication.
- Plan: design/reviews/lr-explanation-20261028/PLAN.md in ai-os; target checkout C:/Users/Joshu/dev/ai-os-projects/lsatu-lr-explanation-20261028.
- Baseline: 9b1eec11bde0746f899c34ec9b5d42630395bfe8. Plan rounds 5; inspections 2; fix rounds 2.

## Plan review 1
Result: C:/Users/Joshu/AppData/Local/Temp/claudex-xo6o2w72/result.json
Observed model: claude-sonnet-5-5; CLI 2.1.309.
{
  "verdict": "REVISE",
  "summary": "The plan targets the right component and keeps the right behavioral invariants. Two layout details need to be specified before implementation, and two smaller gaps remain. The 44px toggle would enlarge every choice row, and it competes with the Restore button for width on phones. The shrink fix is also underspecified. The plan's file list stops short of the other consumers of the same pane and toggle. This is a static review of the source only; I did not run any tests.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "src/components/drill/official/OfficialQuestionPane.tsx:361,512-519",
      "evidence": "Each choice row is `grid-cols-[auto_1fr_auto_auto] items-start px-3 py-1.5` with 24px controls. Making ChoiceNoteToggle a 44px box grows every row that has a note toggle from about 36px to about 50px or more. That happens as soon as Explanation is on, so the choice list shifts and rows become uneven against rows that have no note. When a verdict choice is also crossed out, the fourth column holds Restore (p-1, about 24px) plus the 44px toggle. That is about 72px plus a 12px gap, taken from the choice text at 320px.",
      "fix": "Keep the visual button compact and get the 44px target without changing row height. Use a pseudo-element hit area (`relative before:absolute before:-inset-2`) or negative margins on a 44px button. Alternatively, accept the taller rows deliberately and check them in the 320px screenshots, including the Restore plus toggle case."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "src/components/drill/official/OfficialQuestionPane.tsx:361",
      "evidence": "The plan says the choice grid middle column must be able to shrink. `1fr` is `minmax(auto,1fr)`, so a long unbroken string in the choice text or in the note, such as a URL or a long tag, forces horizontal overflow. The note wrapper is `col-start-2 col-end-5` and spans the columns. A `min-w-0` on the note wrapper alone does not fix the track sizing.",
      "fix": "Change the column template to `grid-cols-[auto_minmax(0,1fr)_auto_auto]`. Add `min-w-0` and `break-words` or `[overflow-wrap:anywhere]` to the note wrapper and the prose, and to the tag and metadata spans. Add the long-token case to the screenshot matrix."
    },
    {
      "id": "F3",
      "severity": "low",
      "path": "src/components/drill/shared/LRQuestionModal.tsx; src/pages/Drill.tsx; src/components/drill/SectionReviewWalk.tsx",
      "evidence": "These files import from InlineChoiceExplanation or use the same pane (grep results). A restyle of the shared toggle and note therefore also changes the modal, the Drill page and the section review walk. These surfaces may have different backgrounds, such as a dark or tinted modal. The plan's verification covers only the OfficialQuestionPane harness.",
      "fix": "Add a check, or at least a screenshot, of the LRQuestionModal and SectionReviewWalk usages. Make the warm surface and text colors explicit, so they stay legible on non-white parents."
    },
    {
      "id": "F4",
      "severity": "low",
      "path": "src/components/drill/official/OfficialQuestionPane.tsx:341,524-534",
      "evidence": "When `choiceNoteExpanders` is false, `noteOpen` is always true and no toggle renders. The panel is then always visible on every choice that has a note. The new inset panel, with its extra padding and border, makes that always-open mode much heavier. The plan only describes the toggle-driven closed and open states.",
      "fix": "Verify the always-open mode (expanders off) with the new panel, and keep spacing between consecutive notes tight enough that five panels do not bury the choices."
    }
  ],
  "coverage": [
    "Read the plan in full.",
    "Read InlineChoiceExplanation.tsx in full.",
    "Read OfficialQuestionPane.tsx lines 340-557 (choice grid, toggle and note placement, Restore column).",
    "Read InlineChoiceExplanation.test.tsx. It has no visual-class assertions.",
    "Grepped for other consumers and writers of the component, the toggle and related class patterns: LRQuestionModal, Drill, SectionReviewWalk, RcChoiceDisclosure."
  ],
  "limitations": [
    "Static review only; I ran no tests, build or browser.",
    "I did not read OfficialQuestionPane.review.test.tsx, so I cannot rule out class-based assertions there.",
    "I did not inspect the design hub guidance, the Neanderthal fixture or the proposed harness, which does not exist yet.",
    "I did not inspect the consumers' parent backgrounds in LRQuestionModal, Drill or SectionReviewWalk."
  ]
}

## Plan review 2
Result: C:/Users/Joshu/AppData/Local/Temp/claudex-_htjtx9i/result.json
{
  "verdict": "APPROVED",
  "summary": "The revised plan resolves all four prior findings, and I found no new material defects. F1: taller rows are now a stated decision, and the plan adds a 320px check with Restore beside the toggle. F2: the plan specifies `grid-cols-[auto_minmax(0,1fr)_auto_auto]`, `min-w-0` on the choice text and note wrapper, and `overflow-wrap:anywhere`, and its test matrix includes long unbroken tokens. F3: the plan adds inspection of the LRQuestionModal and SectionReviewWalk wrappers, renders their pane configurations, and requires panel colors independent of the parent theme. It also records that authenticated parent routes cannot be exercised. F4: the plan adds always-open mode (expanders off) with all five notes. This is a static review of the plan against source I read in the previous round. I did not run tests.",
  "findings": [],
  "coverage": [
    "Checked the revised plan against each prior finding (F1-F4).",
    "Re-used the earlier source reads: InlineChoiceExplanation.tsx, OfficialQuestionPane.tsx lines 340-557, InlineChoiceExplanation.test.tsx, and the consumer grep.",
    "Confirmed the plan's grid and wrapping changes match the current `grid-cols-[auto_1fr_auto_auto]` source and the `col-start-2 col-end-5` note wrapper."
  ],
  "limitations": [
    "Static review only; I ran no tests, build or browser.",
    "I did not read OfficialQuestionPane.review.test.tsx, so class-based assertions there are unchecked. The plan already covers updating obsolete assertions.",
    "I did not inspect the LRQuestionModal or SectionReviewWalk wrapper code in detail. The plan assigns that to implementation.",
    "The verification harness does not exist yet, so its isolation from production routes and auth is unreviewed. The plan states the constraint but cannot show it is met."
  ]
}
Approval check passed for SHA256 3013917c689ba50a1dfc444e55bd6b33429282218fa833ff1d80d0b8264667cc.

## Plan review 3
{
  "verdict": "REVISE",
  "summary": "The phone-width toggle change contains one factual error that affects the exact case the plan says to verify: Restore beside the toggle at 320px. The 6px hit extension would overlap the Restore button. All earlier findings stay resolved. This is a static review of the plan against source I read earlier. I did not run tests.",
  "findings": [
    {
      "id": "F5",
      "severity": "low",
      "path": "src/components/drill/official/OfficialQuestionPane.tsx:496-520",
      "evidence": "The plan says the existing 12px grid gap prevents the toggle's 6px pseudo-element hit extension from overlapping adjacent actions. Restore and ChoiceNoteToggle are not separated by the grid gap. They are siblings inside `<div className=\"flex items-start gap-1\">` (line 496), so the gap is 4px. A 6px extension on each edge overlaps the Restore button by about 2px. The Restore button is a p-1 button with a 24px footprint. At 320px, for a verdict choice that is also crossed out, a tap near the boundary can toggle the note instead of restoring the choice, or the reverse, depending on stacking order. The 12px gap does separate the toggle from the column-3 cross-out or verdict control, so the claim holds only there.",
      "fix": "Make the extension at most 4px on the Restore-facing edge, for example `before:-inset-y-1.5 before:-inset-x-0.5` (maintaining the 44px height). Alternatively, raise the gap in that inner flex to at least 12px at phone widths (`gap-1 max-sm:gap-3`). Correct the plan sentence, and include a 320px tap-boundary check of Restore plus toggle in verification."
    }
  ],
  "coverage": [
    "Checked the revised phone-toggle paragraph against OfficialQuestionPane.tsx lines 356-361 and 493-523 (grid gap and the inner flex container).",
    "Re-confirmed that earlier findings F1-F4 remain addressed in the plan text."
  ],
  "limitations": [
    "Static review only; I ran no tests, build or browser.",
    "I did not read OfficialQuestionPane.review.test.tsx.",
    "The harness and implementation do not exist yet, so the rendered overlap is inferred from class values."
  ]
}
Result: C:\Users\Joshu\AppData\Local\Temp\claudex-s7fbsuuo/result.json

## Plan review 4
Result: C:\Users\Joshu\AppData\Local\Temp\claudex-5_d3q0v5/result.json
{
  "verdict": "APPROVED",
  "summary": "F5 is resolved. The plan now sets `gap-1 max-sm:gap-3` on the inner Restore/toggle wrapper, so the 12px gap exceeds the 6px hit extension. It also corrects the earlier inaccurate grid-gap claim and adds pointer-boundary checks at 320px. I found no new material defects. This is a static review of the plan against source I read earlier. I did not run tests.",
  "findings": [],
  "coverage": [
    "Checked the revised phone-toggle paragraph against OfficialQuestionPane.tsx lines 493-523, where the inner flex wrapper currently has `gap-1`.",
    "Confirmed that F1-F5 are addressed in the plan text."
  ],
  "limitations": [
    "Static review only; I ran no tests, build or browser.",
    "I did not read OfficialQuestionPane.review.test.tsx.",
    "The implementation and harness do not exist yet. Their isolation from production routes and auth, and the rendered pointer boundaries, are unverified."
  ]
}
Approval check passed for 1b09a28d2116adc6a93a360eb43f05496545a1cb4ac039fa5fca25bc436ef7a1.

## Inspection 1
Result: C:\Users\Joshu\AppData\Local\Temp\claudex-i40g6asb/result.json
{
  "verdict": "REVISE",
  "summary": "The Choice Note changes look correct. The one material defect is the unrelated supabase/functions/mcp/index.ts rewrite, which is in the working tree and must not ship in this branch. I did not find defects in the CSS, the toggle, or the grid and gap changes.",
  "findings": [
    {
      "id": "F1",
      "severity": "high",
      "path": "supabase/functions/mcp/index.ts",
      "evidence": "The diff replaces the bundled MCP edge function (589 lines removed) with `import mcp from \"npm:C:\\\\Users\\\\Joshu\\\\dev\\\\ai-os-projects\\\\lsatu-lr-explanation-20261028\\\\src\\\\lib\\\\mcp\\\\index.ts\"`. It also bumps @lovable.dev/mcp-js from 0.20.0 to 0.20.1. A Windows absolute path cannot resolve in Supabase's deploy environment, so deploying or merging this file as-is would break the production MCP function (admin note/homework tools and student reads). The host says this is a concurrent change and not part of the task. It is still present in the working tree and will be swept into any commit or PR of this branch.",
      "fix": "Revert supabase/functions/mcp/index.ts to the baseline (`git checkout 9b1eec1 -- supabase/functions/mcp/index.ts`), or stage and commit only the seven intended files. Confirm the final branch diff does not contain it. If the regeneration was real, it needs its own task and a bundled output with no local paths."
    },
    {
      "id": "F2",
      "severity": "low",
      "path": "scripts/verification/check-lr-explanation.mjs",
      "evidence": "The harness HTML, TSX and checker are untracked and would be committed under scripts/. The standalone preview entry produced lint warnings. The user-screenshot D text and the synthetic stress notes live in checked-in code. Nothing here has a backend or auth effect, but the files are dev-only and not wired to production routes.",
      "fix": "Keep these files in the branch only if Joshua wants them. Otherwise leave them out of the PR or move them under a clearly dev-only path. Label the synthetic notes in-file as not teaching content, and confirm the Vite production build does not include the harness entry."
    }
  ],
  "coverage": [
    "Read InlineChoiceExplanation.css in full.",
    "Read the OfficialQuestionPane.tsx fourth-column and note-wrapper region (lines 485-545).",
    "Reviewed the full tracked diff: InlineChoiceExplanation.tsx, the OfficialQuestionPane.review.test.tsx assertion change, the OfficialQuestionPane.tsx grid/gap/min-w-0 changes, and the mcp/index.ts diff.",
    "Checked the gap-3 sm:gap-1 deviation: it gives a 12px phone gap and a 4px desktop gap, which matches the plan's intent.",
    "Checked the 32px phone toggle with a 6px ::before extension and the 44px desktop toggle against the plan.",
    "Checked the reduced-motion fallback.",
    "Checked that the aria-expanded and aria-label attributes are retained."
  ],
  "limitations": [
    "I did not run tests, build, typecheck or the browser harness. The host's reported results (36 tests, tsc, 9 browser cases) are unverified by me.",
    "I did not read the harness files (lr-explanation.tsx, lr-explanation.html, check-lr-explanation.mjs) in full.",
    "I did not read the full InlineChoiceExplanation.tsx beyond the diff, or the existing InlineChoiceExplanation test file.",
    "I did not inspect LRQuestionModal or SectionReviewWalk.",
    "Signed-in parent routes were not exercised, as the host also states."
  ]
}
Disposition F1: accepted. Investigation proved Vite mcpPlugin regenerates this generated file; externalizeBareAsNpm treats Windows absolute path as a package. Host earlier concurrency interpretation was incorrect. All host dev/preview servers stopped, generated MCP restored from baseline; git status now shows only seven intended files. F2: retained as explicitly labelled dev-only fixtures under existing scripts/verification. Production asset search found no harness title/stress tokens. They are not production routes.

## Inspection 2, final
Result: C:\Users\Joshu\AppData\Local\Temp\claudex-rk2w91pd/result.json
{
  "verdict": "APPROVED",
  "summary": "I found no material defects in the seven-file snapshot. The component and CSS changes preserve the existing behaviour. The three verification files are dev-only, and nothing in the production app imports them. I read all seven files and did not run any tests or builds.",
  "findings": [
    {
      "id": "N1",
      "severity": "low",
      "path": "src/components/drill/official/OfficialQuestionPane.tsx:507",
      "evidence": "The Restore button keeps its original `p-1` padding with a 16px icon, so its pointer target is about 24px. The new 44px toggle sits beside it. This is unchanged from the baseline and the plan only requires that Restore and the toggle don't overlap, which the 12px phone gap prevents.",
      "fix": "Optional follow-up: give Restore the same 44px (or 6px-extended) hit area as the toggle on phones."
    },
    {
      "id": "N2",
      "severity": "low",
      "path": "scripts/verification/check-lr-explanation.mjs:11",
      "evidence": "The script launches Playwright with `channel: \"msedge\"`, so it only runs where Edge is installed. It is dev-only and nothing in production imports it.",
      "fix": "Optional: make the browser channel configurable through an environment variable."
    }
  ],
  "coverage": [
    "Read all seven files in full: InlineChoiceExplanation.tsx and .css, the harness .tsx, .html and check .mjs, and the diffs to OfficialQuestionPane.tsx and the review test.",
    "The toggle and the Restore button in the pane's fourth grid column: the 12px phone gap against 4px on desktop, the toggle's disabled state, and its stopPropagation, which keeps a toggle click from choosing an answer.",
    "The preserved content rules: tag, percentage including 0, and \"Your answer\" metadata; whitespace-only notes (no toggle or panel); the correct vs wrong heading; and `white-space: pre-line` on the prose.",
    "The `col-span-full` / `sm:col-start-2 sm:col-end-5` note placement and the `minmax(0,1fr)` / `min-w-0` / `overflow-wrap:anywhere` overflow handling.",
    "The 32px visual control with a 6px `::before` extension on each edge (44px pointer target) below 640px, and the reduced-motion rule.",
    "A search of the other test files for the old utility classes: only the one updated assertion in OfficialQuestionPane.review.test.tsx depended on them.",
    "Harness isolation: it only fetches the checked-in /data bank file, makes no backend calls, and bypasses no authentication."
  ],
  "limitations": [
    "I did not run tests, typecheck, build, ESLint, the browser checks or screenshots. The pass results and screenshot evidence in the host's note are unverified by me.",
    "I did not inspect LRQuestionModal or SectionReviewWalk wrapper code in this pass, and the authenticated parent routes were not exercised.",
    "`gap-3 sm:gap-1` vs `max-sm:` and the claim that no backend files changed come from the host's note. I did not check them against git.",
    "Approval covers only the snapshot I read."
  ]
}
Snapshot 598e98e67b24895313191b4100642268d042d1ecc4b7f73abe534dd2410dd60c readback matched all seven files. No further code edits. Optional low findings retained and disclosed. Final production build, 36 tests, full typecheck, production browser matrix and Taste 0 FAIL confirmed.
