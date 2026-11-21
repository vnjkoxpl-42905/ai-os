---
type: synthesis
subject: Source-led My Work notes material refinement
created: 2026-10-27
updated: 2026-10-27
aliases: [My Work notes ledger, Notes material polish]
tags: [design, lsatu, local-preview]
contradictions: []
sources:
  - ../../principles.md
  - ../../../references/website-design-planning.md
  - ../../../wiki/sources/astra-web-design-taste-vault-chase-ai.md
  - ../../../wiki/sources/claude-design-fifteen-hacks-jack.md
  - ../../../research/2026-10-24-student-widgets/clip-findings.md
  - ../../../wiki/sources/astra-website-design-loop-jack.md
---

# Put finding and reading notes ahead of repeated chrome

Status: implemented locally in the existing lsatu-my-work-20261026 worktree, not published. Claude Opus5.5 medium read the Claude Design design-critique skill and proposed three concrete options. The host selected the lead-entry ledger; plan round4 approved. Final Claude inspection returned REVISE; host corrected its evidence/font/reduced-motion findings after the two-inspection limit. These final corrections are host-verified and not independently approved. This is a design judgement, not user acceptance or measured student retrieval improvement.

## What was actually examined

Host inspected the signed-in teacher account at /my-work/notes through the Codex browser: large empty personal editor precedes From Joshua, with one recent note and All4read but no visible archive. That is not evidence of a student data-loss bug. Existing unpublished worktree was already notes-first with search/filter/archive and personal drafts. Host inspected actual local synthetic renders; the new pass retains its functional work. Browser widths are measured CSSpx; early canvas/thumbnails are not accepted responsive proof.

## What the saved sources contributed

| Source | Existing or missing | Applied decision |
|---|---|---|
| [Visitor decisions and bounded reference critique](../../../references/website-design-planning.md) | Repeated orientation and duplicated latest note | Search before content; one linked row per note; remove decorative eyebrow and duplicate assigned-work aside. Shared Assigned work tab remains. |
| [Material principles](../../principles.md#material-depth-and-a-richer-layered-feel) | Offset paper edges and cool utility slab | One warm paper ledger; contact/lower ambient shadow; quiet row rules; warm charcoal family and paired dark theme. |
| [Taste-vault method](../../../wiki/sources/astra-web-design-taste-vault-chase-ai.md) | Need focused alternatives in same family | Claude compared featured+aside, lead ledger, featured+search. Selected ledger because it removes duplicate notes and brings retrieval earlier. |
| [25-tip application](../../../research/2026-10-24-student-widgets/clip-findings.md) | Tiny working type; progressive disclosure already present | Existing Fraunces/Outfit,14px controls,15px excerpts,12px metadata; preserve search/unread/month groups/Load more and separate notebook. No new library. |
| [Fifteen hacks](../../../wiki/sources/claude-design-fifteen-hacks-jack.md) | Feedback needs clarity | Real focus boundary; pressed tone; noncolour active-filter underline and forcedcolors border. No floating motion or decorative effects. |
| [Bounded design loop](../../../wiki/sources/astra-website-design-loop-jack.md) | Need inspected output, not score | Matched before/after, source fingerprints, viewport/contrast/zoom/interaction checks and fresh Claude inspection. |

The library is not exhausted. It has not established how students search (topic/date/title/session), typical collection sizes or which authenticated reading flow is best. Those are useful next research questions if observed use warrants change. Do not invent tags, personalization, analytics or a new notes system to fill the gap. Mobbin flow search was attempted but returned paid-plan required; no examples inspected or subscription purchased. Original source videos/galleries were not newly inspected.

## Concrete local changes

One Notes heading and short description, secondary Personal notes, search and All/Unread, then month-grouped document rows. The newest unfiltered row gets lead emphasis, appears once and is not shown over unrelated search results. Empty/loading/error states retain personal access. Existing URL state, return-focus, read mutation and personal save/draft code remain intact. Scope is CSS, archive composition and focused regression tests; no backend/schema/global-token changes.

[Desktop](after-desktop.png) · [Phone](after-phone.png) · [Phone before](local-before-phone-readable.png) · [Dark desktop](after-dark-desktop.png) · [Dark phone](after-dark-phone.png) · [Search](after-phone-search.png) · [Unread](after-phone-unread.png) · [High contrast](after-forced-colors-phone.png).

## Proof and its limits

[Host proof](PROOF.json): typecheck/build/postbuild/diffcheck pass.48 relevant test cases pass across five files and corrected archive rerun; one initial new test selector was ambiguous against its test harness output and was fixed. Measured320/390/684/768/1024/1281/1441 CSSpx have no page overflow;200% root text at390/1024 retains controls. Sampled text contrast >=5.46 light and >=6.73 dark. Search by older-body text, search return/focus, no-results/clear, unread equal emphasis,16-row Load more, keyboard boundary and synthetic personal save checked through browser. Empty/loading/error branches unit-tested rather than all visually captured. No live student/RLS/full-shell acceptance, deployment or broad app certification. Title-leading excerpts remain unchanged and can repeat the title in authored HTML.

Implementation plan and append-only review log live in the app worktree at docs/plans/my-work-material-polish.md and .review-log.md; do not treat historical first-plan approval as review of later code.

## Inspection fixes
First fresh code inspection required visible notebook conflict/retry buttons. These now have presentation-only classes and44px targets; persistence logic is unchanged. Smaller fixes give neutral notebook focus, clearer lead hover, correctly named filter group and section, removed decorative remnants, and a route-aware lead anchor regression. Final typecheck/build/postbuild pass.48 cases passed across final39-case other-file run plus9-case archive rerun. Final independent inspection returned REVISE; see final status below.

## Final status and remaining limit

Local code and preview are ready to review. Four plan rounds approved the direction; two fresh code inspections produced actionable fixes. The last inspection identified blank default captures, unloaded fixture fonts and reduced-motion button transitions. Host fixed them, rebuilt and rechecked actual-font output. Final default light/dark images are verified nonblank and visually inspected, and FontFaceSet records confirm loaded Fraunces/Outfit. At measured390x844 CSSpx first row starts567px down; viewport/zoom/contrast checks pass, all relevant reduced-motion transitions0s. The2-inspection limit is exhausted: these final host corrections have not received an independent reinspection, so final Claude approval is outstanding. No unresolved host-observed material issue is asserted as independent approval.

Only default light/dark images are final typography evidence; search/unread/high-contrast captures remain earlier interaction evidence with fallback fonts. The local fixture uses synthetic auth/data and a representative shell. Real student permissions/full production host are not accepted by these tests. No commit, push or publication. [Actual font records](fonts.json) and [nonblank capture validation](capture-validation.json).
