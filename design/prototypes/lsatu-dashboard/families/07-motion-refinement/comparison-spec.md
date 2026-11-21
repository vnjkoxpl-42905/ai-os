# LSAT U reference motion inspection, 2026-10-22

Host/builder: Codex. Independent inspector: Claude, requested model Opus. Maximum two fresh inspections for this refinement. This is the second and final inspection after accepted fixes. Earlier inspections concerned the previous motion treatment and do not cover these changes.

## User request
Visit the current public LexPrep homepage before changes, then reproduce its staggered fade-up / scroll reveal uniformly across LSAT U page, sidebar, tab and signed-in entry transitions using GSAP. Preserve the existing product layout, account data, active work, focus and reduced-motion behavior. Changes remain local.

## Fresh reference evidence
Live https://www.lexprep.ai/ inspected in Codex browser before implementation. Its current 35 public static chunks were fetched read-only and examined, with source hashes and byte offsets recorded in C:/Users/Joshu/Downloads/LexPrep-Live-Motion-2026-10-22/reference.md and source-evidence.json.
Scroll-section preset is opacity 0 to 1, y14 to 0, blur10px to 0, duration .3s, CSS easeOut cubic-bezier(0,0,.58,1), initial .05 delay and .15 stagger, once with viewport margin -100px. Homepage hero separately uses .5s/y10/blur8 with longer delays. Product pages intentionally share the scroll-section preset rather than introducing five hero-specific delays everywhere.
Live DOM confirmed Study Mode hidden below-fold, then opacity .9744 / blur .2559px while entering after native scroll. Before/after screenshots and DOM measurement are in this evidence directory.

## Implementation to inspect
Base c0fe7c8b8343946339d34e202e395259ff6f76ca. Inspect all changed source and tests relative to it. Shared useClassroomMotion owns the reference preset, scoped GSAP cleanup, meaningful data-motion-item groups, data-motion-ready/aria-busy gates, newly mounted explicit groups, nested scrollers and safe reachable triggers. Four items per group, 24 total per semantic navigation bounds work. Additional content remains visible. Pending targets are armed before paint with a one-second visible fallback, after which the same identity never re-hides. Stable named or rendered-slot identities prevent refresh/remount replays. Text/count/style updates do not replay the page. Interaction finishes the affected reveal immediately. Active sessions and local motion owners remain excluded. Below-fold independently triggered sections start at .05 seconds; persistent group indexes bound in-view stagger.
Home competing CSS entrances are disabled narrowly, preserving SectionBriefing. The destination header has its own local motion owner keyed by destination, so unchanged headings remain still across inner tabs. Library search and dialogs are outside animated ancestors. RC setup has four granular content groups. Page-only attributes add meaningful heading/description/action/section groups and loading readiness to major student, Practice, analytics, Reading Center and teacher surfaces. Stable navigation and active drills are not lifted or blurred.

## Host verification already performed
- Actual app http://127.0.0.1:8120, real signed-in account and backend, not synthetic RC fixture.
- Home, My Work tabs, Practice LR/RC, Review, Library tabs, Progress Overview/History/Topics, Reading Center Dashboard/Speed Reading, teacher workspace/Today navigation exercised.
- Observed Home title settled while subtitle opacity .8995 / blur1.0047 and tools opacity .3643 / blur6.357, showing actual stagger. Home targets computed animation-name none after competing CSS removal.
- Progress lower loaded sections at top2047/2373 remained opacity0 blur10 until scrolling into view, then opacity1 filter none.
- Authenticated reload returned to Home, no runtime console errors observed.
- Actual CSS widths 320/390/768/980/1440: no horizontal overflow or in-view content left opacity0 after settling. See responsive.json and progress-WIDTH.png.
- Mobile sidebar open/select/close restores body scrolling and focus. Reduced motion renders targets immediately opacity1/filter none/no transform.
- Final integrated proof after all fixes: 277 tests across 12 relevant files passed, typecheck passed, production prebuild/build/postbuild passed. Unrelated generated MCP output restored to HEAD. See docs/verification/platform-motion-20261022.md for current refinement coverage.

## Visual evidence to read
You can Read images, but cannot play video or run browser/proof tools under this inspection. Do not claim direct live or video observation. You MUST attempt to Read reference.md and these images in this evidence directory: lexprep-before-scroll.png, lexprep-after-scroll.png, frames/0013.jpg (mid-reveal actual Home), home-desktop.png (settled), progress-320.png, progress-1440.png, rc-setup-desktop.png. If image reading fails, report the actual failure. State exactly which images you read. platform-reference-motion.mp4 is for the user/host, not proof that you watched it. Read review-log.md for round-one dispositions and C:/Users/Joshu/AppData/Local/Temp/claudex-hd_sgod4/result.json for the previous findings. This is a fresh inspection, not a resumed plan review.

## Review focus and limits
Compare parameters and stagger structure against the verified public source, evaluate likely timing/scroll safety and accessible behavior, catch source defects and gaps in primary navigation coverage. Report concrete findings with severity/path/evidence/fix, actual coverage and limits. No invented finding quota. Exact pixel/temporal perceptual equivalence cannot be proved through static screenshots. No active student work was launched/completed or account data changed for testing; rare editor/payment/assignment states were not exhaustively exercised. No deployment is authorized by this inspection.
