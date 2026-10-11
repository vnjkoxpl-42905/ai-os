# Compare against the current Intro to LR surfaces

Reconstructed product reference, 2026-10-11. The historical `intro-to-lr-product.md` was not found. This reference describes inspected source evidence and preserves historical intent separately. It does not certify the deployed app.

## Resolve the actual target first

The local application checkout is [sibling `ai-os-projects/lsatu`](../../ai-os-projects/lsatu/). Its integrated Main Conclusion implementation lives in `src/bootcamps/main-conclusion/`. Check the requested task's actual worktree and commit; another saved checkout can be newer. Do not assume the vault is the application repository.

The [current route tree](../../ai-os-projects/lsatu/src/bootcamps/main-conclusion/routes.tsx) is mounted under `/bootcamp/intro-to-lr/*` and declares these comparison surfaces:

| Surface | Source evidence and comparison questions |
|---|---|
| Guided lessons and workbook | `modules/lessons/NewGuidedIntro.tsx`, `IntroGuidedWorkbook.tsx`, lesson-note loader in `routes.tsx`. Does the target explain a concept before asking the learner to perform it? |
| Reference | `modules/reference/`, indicator vault, flashcards and named tools. Can students retrieve the explanation relevant to a mistake? |
| Drills and practice | `modules/drills/`, `modules/practice-drills/`, active drill route switch. Does the target support an actual attempt and intelligible review? |
| Simulator and structure | `modules/simulator/`, `components/structured-dissection/`. Does the question, answer and reasoning remain traceable to source evidence? |
| Hard sentences | `modules/hard-sentences/`, guided sections and capstone. Is there a mechanism-level demonstration and a meaningful follow-up attempt? |
| Diagnostics and review | `modules/diagnostics/`, recommendations, mistake/trait profiles, review queue. Are displayed data real, relevant and saved correctly? |
| Shared workspace and persistence | `components/workspace-shell/`, `persistence/`, `hooks/`. Does navigation preserve context and does saving survive the relevant reload/account boundary? |

These directories/routes are implementation evidence, not proof that every feature is working or a requirement to add every feature to every topic. Report missing analogous capabilities only when they help the target's learning goal.

## Historical intent is not current state

- [Main Conclusion handoff](../../ai-os-projects/lsatu/docs/main-conclusion-bootcamp/MAIN_CONCLUSION_HANDOFF.md) preserves the corpus-first scope and named tools.
- [Parity artifacts](../../ai-os-projects/lsatu/docs/main-conclusion-bootcamp/parity/README.md) explain included versus deferred content. Their old counts belong to the dated inventory, not an asserted current total.
- [Gate 5 report](../../ai-os-projects/lsatu/docs/main-conclusion-bootcamp/gate-5-audit.md) recorded a 2026-05-01 `/bootcamp/structure` release and deferred simulator content. The current source route is `/bootcamp/intro-to-lr`; confirm the live URL before a browser review.
- Old standalone `App.tsx` comments and v1 no-auth/local-only assumptions do not describe the integrated application reliably. Use mounted routes, current persistence code and live-system evidence.

Apply the [current quality bar](bootcamp-quality-bar.md). Do not treat this reconstructed reference as a new product decision or silently restore a deferred feature.
