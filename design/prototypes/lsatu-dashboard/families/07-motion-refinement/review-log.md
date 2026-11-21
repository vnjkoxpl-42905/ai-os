# Motion comparison review log, 2026-10-22

Host/builder Codex; inspector Claude; requested Opus, observed claude-opus-5-5. Maximum two fresh inspection rounds for this refinement. Changes stay local.

## Round 1
Artifact: C:/Users/Joshu/AppData/Local/Temp/claudex-hd_sgod4/result.json
Verdict: REVISE. Core reference parameters confirmed. Inspector read source/reference evidence but explicitly did not read screenshots or watch video. No visual approval claimed.

Dispositions:
- F1 readiness blink, accepted. Pending painted targets must not be re-hidden after late loading. Pre-arm pending targets with bounded visible fallback, interaction settlement and cleanup.
- F2 persistent heading replay, accepted. Give the destination heading a separate owner/key so entering a destination animates it, switching its inner tabs does not.
- F3 remount replay, accepted. Deduplicate stable semantic item identities within navigation, including refresh/filter remounts, while allowing first asynchronous content arrival.
- F4 stagger structure, accepted in part. Independently triggered below-fold sections begin at .05s rather than inheriting a root index; counts persist across discovery. Separate sections in the same viewport may intentionally enter in parallel, as independent reference sections do.
- F5 whole Library page, accepted. Search chrome/dialogs stay outside animated ancestors; heading, description and loaded shelves become separate items.
- F6 Home CSS blanket rule, accepted. List actual settling targets so SectionBriefing retains its own entrance.

Additional host correction: Home test render helper wrapped only the initial UI, losing Router on rerender. Baseline Home source loaded read-only from c0fe7c8b reproduces 52 pass / 1 failure. Fix helper using RTL wrapper option without changing assertions or production navigation.

Final inspection must read at least the reference and app image frames using Read, report which images it actually inspected, and state that static images cannot establish temporal equivalence. No claim of independent browser testing is permitted.

## Round 2, final
Artifact: C:/Users/Joshu/AppData/Local/Temp/claudex-61wt5ccb/result.json
Requested Opus; observed claude-opus-5-5. Verdict APPROVED. All six round-one findings addressed in source. Inspector read all seven requested images and compared the exact reference parameters, all 24 changed-file diffs and the relevant owners. It did not run the browser, tests or build, or play video. Browser verification and 277 passing tests/typecheck/build belong to the host.

Four low-priority notes remain, none rated material:
- R2-1: a ResizeObserver arriving during a reveal may finish it early. Host checked installed GSAP: kill clears animation.scrollTrigger, so the reviewer's post-kill retained-reference premise is inaccurate. Before the trigger is killed, settling a target that moved into view can still finish motion early. Current behavior prioritizes leaving content readable after asynchronous layout changes. No source change after approval.
- R2-2: independent heading/body groups can enter in parallel. Retained as a deliberate compact product-page adaptation; individual semantic groups preserve the reference stagger instead of serializing the entire dashboard.
- R2-3: Home/teacher datelines and supporting summary lines remain static anchors while primary content enters. Retained as minor hierarchy polish rather than another animated item.
- R2-4: My Work's prescribed week remains stable while the assignment list enters. Recorded as a coverage/polish gap, not a data or interaction defect.

No third round. Production source unchanged after this approval. Final browser matrix repeated after fixes: 320/390/768/980/1440, no overflow or settled visible targets left hidden; reduced motion remains opacity1/filter-none. Native final clip: platform-motion-final.mp4. App remains local at http://127.0.0.1:8120/classroom.
