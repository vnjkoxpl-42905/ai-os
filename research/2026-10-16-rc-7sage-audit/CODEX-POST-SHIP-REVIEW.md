# Keep the releases, repair the review boundary, and verify each remaining slice

Release follow-up, 2026-10-17: Joshua authorized merging PR #219. Merged as `2f1b3bee`, synchronized in Lovable and published through the free deploy path. Live bundle `index-CUthXxh6.js` replaces `index-B9OE8OxJ.js`; served results chunk contains the explicit reveal controls. Production search pagination was exercised from passages 1-40 to 41-80. Earlier open/unpublished and CI-block statements below are historical. No production answers or section clocks were changed. Full signed-in review-save/clock/accessibility acceptance remains open.

Reviewed 2026-10-17. Scope: RC Practice and Drilling only. RC Bootcamp and Reading Center / RC Recall are excluded.

Implementation follow-up on 2026-10-17: the confirmed review/save/history/recency defects and discovery/reader fixes are implemented on `codex/rc-t06-review-reliability`, pending PR merge authorization. See the application repository's `docs/verification/rc-review-acceptance.md` for implemented behavior, browser evidence and remaining limits. The findings below preserve the pre-fix review and are not a claim that those defects remain in the branch. Production remains at `21bfefd0` until an authorized merge and publication.

Release candidate: [PR #219](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/219), head `c4bebe58`, open and mergeable. Typecheck/build passed; 658 integrated tests plus overlapping focused checks passed. CI activation was blocked by missing OAuth workflow scope; the apply-ready workflow patch is included in the PR. The untracked local workflow and generated MCP bundle artifact were preserved outside the commits. No merge/publication or production student mutation occurred.

## Verdict

The architecture and initial corrections are largely sound. The execution produced useful partial releases, but T03 through T05 did not meet the plan's own independent review and running-browser acceptance gates. Do not label the entire T01-T05 range complete. T06 is the correct next implementation priority, with a wider spoiler boundary than its current packet describes.

This review read the full available transcript in `handoffs/2026-10-17_rc-drilling-t01-t05-ship.md`, the review handoff, and the plan/disposition documents, and independently inspected the relevant current source. The transcript excludes tool payloads; current repository/API checks establish the state below.

## Current evidence supersedes the earlier snapshot

- GitHub confirms #213, #214, #216, #217 and #218 merged. Current `origin/main` is `21bfefd0632e62a34da45b76b8d4a1864ca857da`.
- The full transcript includes Joshua's explicit #218 merge/publish approval at lines 989-991. The earlier snapshot saying approval was pending is obsolete.
- Lovable `latest_commit_sha` matches that merged HEAD. Production HTML serves `assets/index-B9OE8OxJ.js`. This confirms the reported build identity, not full signed-in feature acceptance.
- #215 remains open. Do not resume the cancelled GEMINI instruction edit or infer merge approval.
- The application checkout is clean, on `codex/rc-t05-standalone-rc-reader`, with no source diff against `origin/main`.
- Fresh verification: typecheck passed; 49 test files and 618 tests passed across RC, timed/testing, section launch, standalone history, AcademyMainhub and Finder. These results do not replace browser acceptance.

## What worked and what remains

| Packet | Assessment | Remaining boundary |
|---|---|---|
| T01 | Substantial integrity repair: excluded sessions, stable pagination, first-take semantics and honest passage states. | Recent accuracy still uses an exposure timestamp; see finding below. |
| T02 | Launch errors now propagate, clock copy follows actual routing, and Start is guarded. | Establish whether backend preflight creation changes Fresh before the student starts. |
| T03 | Preview routing preserves question identity; held-back defaults and offset-preserving Find are sensible. | Search truncates at 200 per result category; builder filter link and exposure policy remain open. Show more is incremental rendering, not virtualization. |
| T04 part 1 | Academy history names sources and uses acknowledged, non-destructive Discard. | Saved sets/recipes are absent; older history surfaces retain Delete. Completed scores conflict with the no-score-before-reveal requirement. |
| T05 part 1 | Sharing RcTimedReader is a sensible correction to the original toolbar-copy proposal. | Real sitting acceptance, local-save failure/account switching, comparative/display/responsive controls and Find counter remain incomplete. |

## Findings that change the next work order

1. **P1: spoiler protection must span the whole journey.** `RcResults.tsx` still renders credited answers, correctness and aggregate results before an explicit reveal. `standaloneDrillHistory.ts:82` and `RcSessionHistory.tsx:33` also show completed scores without a reveal decision. PLAN's blind-review criterion forbids scores and correctness-derived cues before reveal. Hiding answer columns alone cannot satisfy it. Include Completed cards, passage scores, recommendations, missed-only actions, old/direct links, back navigation and refresh. Decide access from persisted reveal state separately from immutable performance.

2. **P2: skipped or abandoned retakes promote old grades into recent accuracy.** `rcProgress.ts:554` and `:563` advance `lastSeenAt` while preserving the prior graded correctness; `rcAdaptive.ts:167` sorts that timestamp for its recent window. Keep exposure recency separate from last graded first-take recency. Test more than 40 graded questions, then skip/abandon a retake of an old question.

3. **P2: review actions need acknowledged failure handling.** `RcResults.tsx:209-218` has no busy/error recovery around drill-misses creation and optimistically changes analytics exclusion without rollback. The excluded-state label at `:615` also says it is counted. `RcPlayer.tsx:969-983` advances the local review pick before persistence succeeds, without retrying that exact failed command. Require visible failure/retry and truthful labels. A busy button alone does not prevent duplicates after a lost server response: retry the same operation identity or recover the exact sitting.

4. **T04 parity is narrower than the headline.** `RcHubSurface.tsx:663` / `:1172` and `RcSessionHistory.tsx:66` retain destructive Delete paths. No records were deleted during this review. Audit reachability and explicitly replace or retire those paths before claiming all RC history uses safe Discard.

5. **Fresh currently means attempt-based eligibility, not verified non-exposure.** PLAN's strict exposure/Unknown policy conflicts with MASTER's retained semantics and untracked full-text previews. Keep current wording truthful. Stage a separate exposure contract, historical Unknown handling and metadata-first reveal before offering strict Fresh. Do not infer historical non-exposure.

6. **T03 does not meet unlimited discovery or bounded DOM claims.** `rcSearch.ts:333-334` caps each result category at 200 without continuation. `RcHubSurface.tsx:992` grows the rendered slice on Show more. Keep the accepted incremental implementation, but label it accurately and either bound pages/windowing or measure and explicitly revise the worst-case DOM criterion.

7. **P2: T05 local marks need validation and save feedback.** `TimedStandaloneSectionRunner.tsx:59-60` accepts any object as marks; `RcPassagePane.tsx:91` expects an array and calls `filter`. Malformed stored entries can crash the reader. Storage-write failures are silently caught at runner `:66-67`. Validate mark arrays/ranges and show a truthful device-save error. Only marks are serialized; display settings do not survive reload. Owner/sitting keys and the readiness guard correctly protect normal account switching. `RcTimedReader.tsx:54` fixes reveal to false, and no answer/explanation or passage-map leak was found. Annotation blocking during pause and Find navigation still need explicit policy and tests.

## Revised execution order

1. **T06A: close spoiler boundaries.** Branch and PR from fresh `origin/main`. Persist reveal state; gate results/history/derived cues; preserve old links and protected records. Test unrevealed/revealed, direct/back/refresh and account/session isolation.
2. **T06B: make review writes and retry reliable.** Acknowledged reanswers with retained unsaved picks, exclusion rollback, retry identity after uncertain creation, and protected-session restrictions. Keep first-take grades immutable.
3. **T06C: improve review usability.** Source badges, Passage Summary beside the passage, and contextual tutor link. Verify actual keyboard and responsive behavior.
4. **Close T03 omissions.** Builder-to-search link and real continuation beyond 200. Resolve exposure semantics before implementing exposure-based Fresh.
5. **Accept and finish T05.** First exercise the real shared reader/controller with a local or preview sitting. Then comparative A/B/Both, Display controls, responsive panes and zero-match feedback. Verify local persistence limits and sealed policies. Do not start a production clock for this audit.
6. **T04 part 2.** Prepare a concrete additive storage recommendation for fixed sets versus recipes, with LR isolation and reuse-as-new-sitting semantics. The previous ambiguous “go” did not choose a storage design or authorize a migration.
7. **T07.** Repair graded recency, then expose target difficulty, sample size and review correction labels with truthful semantics.
8. **T09 inventory can begin early.** Identify actual explanation coverage and missing states; do not put this behind optional T08 overlays.
9. **T10 integrates already accepted slices.** Each preceding PR needs relevant browser/failure-path checks, independent review, and responsive/accessibility evidence where affected. T08 remains a separately scoped training enhancement.

No merge, publish, backend deployment or application source change was performed during this review. No signed-in browser journey, production Discard, real section clock, mobile or screen-reader acceptance was performed. Those remain explicit gates, not implied by passing tests or a served bundle.
