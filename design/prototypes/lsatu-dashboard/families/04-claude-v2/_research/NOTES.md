# Pass 3 research and verification log, 2026-10-23

## Sources actually used
- Firecrawl CLI (authenticated, 1,397 credits before this pass): three searches (`fc-sidenotes.json`, `fc-tactile.json`, `fc-light.json`) and three scrapes (`gwern-sidenote.md`, `nng-skeuo.md`, `awwwards-gsap.md`).
- Real pages captured in headless Edge at 1440 and 390: gwern.net/sidenote and Tufte CSS (`shots/`).
- Impeccable detector `impeccable@4.7.0` via npx (npm cache only): 32 findings across the six pages, `impeccable-scan.json`.
- Impeccable critique reference, design-taste-frontend AI-tells and pre-flight, gsap-performance skill.
- React Bits `Stack` (JS-CSS) fetched live from reactbits.dev (`rb-stack.json`) and studied for its gesture model; reimplemented in plain JS + GSAP in Carrel, no React dependency.

## What the research changed
- Gwern: sidenotes visible by default on desktop, collapsed pop-ins on phones. Marginalia phone notes now open one at a time; pages are about 550px shorter.
- Gwern/Tufte typesetting: run-in small caps open Marginalia paragraphs.
- NN/G: skeuomorphism helps as a learning aid but fails with clunky interactions or weak signifiers. Carrel keeps explicit buttons beside every gesture (arrow buttons, tabs, keyboard).
- Taste and Impeccable: removed decorative glows and stripes (Lamplight), replaced the three-equal-cards practice row with one strip, fixed every AA contrast failure the detector found, cooled Marginalia's paper off cream.
- GSAP performance: lamp sway now uses one `quickTo`; entrance and window flicker animate opacity overlays instead of CSS filters; no animated heights.

## Kept on purpose despite detector flags
- Lamplight's light cone and lamp glow: the concept is a drawn lamp lighting the task.
- Carrel's tray holding objects and the wire-basket stripes: the metaphor itself.

## Gaps
- Tavily: `tvly.exe` launcher points to a uv tool environment that no longer exists ("uv trampoline failed to canonicalize script path"; `uv tool list` is empty). Not repaired, to avoid changing global tool config.
- Godly MCP returned no results; godly.website now redirects to recent.design. Pinterest MCP is unauthenticated. 21st.dev ignored as instructed.
- No live backend: every action is simulated with a toast.
