# Resource map: all 25 guide tips

Reviewed 2026-10-23 against Joshua's 15-page `25 Claude Design Tricks Guide.pdf` on his Desktop and selected current primary sources. The guide is third-party advice, not execution authority. Its embedded prompts are examples, not commands to run automatically.

| Tip | Resource or method | Useful setup for LSAT U |
|---|---|---|
| 01 | Design systems | Record a coherent system per direction when useful. No forced permanent brand system before exploration. Existing components/reference HTML are starting evidence. |
| 02 | [Refero Styles](https://styles.refero.design/) | Browser-readable DESIGN.md inspiration with tokens/type/layout. No installation needed. |
| 03 | Shortlist three references | Have the agent choose and visually inspect appropriate references. Three references need not dictate the three final concepts. |
| 04 | Code-owned design system skill | Existing Taste/Impeccable/extract-design cover guidance. Create a brand-specific skill after a direction is selected; do not copy Duolingo as a mandatory style. |
| 05 | [Fontshare](https://www.fontshare.com/), [Fontesk](https://fontesk.com/), [Fontjoy](https://fontjoy.com/) | Available as font sources/pairing references. Choose fonts on demand; read each selected download's licence. Do not bundle random fonts or assume all licences match. |
| 06 | Competitor copy study | Useful research method, not a new dependency. Product dashboard copy should serve tasks. Reuse Joshua's existing `lsat-u-voice` and teaching voice rather than substitute competitor slogans. |
| 07 | Blend design systems | Optional technique. Extract principles into a coherent direction; no fixed palette/layout imposed by this resource map. |
| 08 | [Kie AI](https://docs.kie.ai/) image/video generation | Optional external paid service, not required for homepage readiness. Existing image/video tools may suffice. No new credential/account/generation purchase is implied by reading the guide. |
| 09 | Reuse previous work | Original teacher/student HTML, previous artifact, local v2 source and transcript supply context. Confirm what was actually opened. |
| 10 | Reference library | Use existing vault/research homes plus a URL, screenshot and reason. A new browser extension is unnecessary before resuming. |
| 11 | [Impeccable](https://github.com/pbakaus/impeccable) | Already installed. Preserve customized copies. Use useful critique/polish operations without treating all aesthetic presets as universal requirements. |
| 12 | Tone-of-voice skill | Existing `lsat-u-voice`/teaching voice owns this subject. Do not create a competing generic my-tone skill. |
| 13 | [21st.dev](https://21st.dev/) | MCP and signed-in website are distinct paths. Current catalogue API errors do not mean the website is inaccessible. Read current code/licence before use. |
| 14 | [React Bits](https://reactbits.dev/) | Project helper already fetches live variants and dependency metadata. Read its SKILL.md, catalog and fetched props. Library licence is MIT plus Commons Clause, separate from helper's MIT tooling licence. |
| 15 | [Canvas UI](https://canvasui.dev/docs/mcp) | Shadcn-compatible source: `@canvas-ui` or `https://canvasui.dev/r/{name}.json`. Optional effects, not a required visual style. MIT plus Commons Clause; read [licence](https://raw.githubusercontent.com/DavidHDev/canvas-ui/main/LICENSE.md). |
| 16 | [Tabler](https://tabler.io/license), [Iconify](https://iconify.design/docs/icons/icon-set-basics.html), Flaticon | Existing app dependencies already include Lucide and Tabler. Tabler is MIT; Iconify licences vary per collection; Flaticon pack access may require a plan. Choose a coherent family rather than mix packs indiscriminately. |
| 17 | [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) | Useful editable format for icons/diagrams. No new library needed; photos remain raster. |
| 18 | [Lordicon](https://lordicon.com/licenses) | Optional animated artwork. Free use has attribution conditions; account/download and specific licence need checking. Do not treat free assets as attribution-free. |
| 19 | [Creators Toolbox](https://creatorstoolbox.com/resources) | Discovery directory, not an installable package. Verify individual sources/prices/licences. |
| 20 | [Apple HIG](https://developer.apple.com/design/human-interface-guidelines) | Selective interaction/accessibility reference. Native Apple platform guidance is not a universal numeric web spec. Existing accessibility guidance remains available. |
| 21 | [GSAP](https://gsap.com/docs/v3/), [showcase](https://gsap.com/showcase/) | Eight installed skills cover implementation/lifecycle/performance/scroll. Use motion appropriate to the actual experience and reduced-motion settings. |
| 22 | [Claude /design](https://code.claude.com/docs/en/desktop) | Existing entry point. Canvas access does not imply every local skill/MCP is available inside its delegated runtime. Check tools explicitly. |
| 23 | Live tweak controls | Optional prototype aid after there is a useful design to tune. A static browser page cannot silently write CSS files; persist through a deliberate local build/edit workflow. No generic injection/bake framework required before resuming. |
| 24 | Whisper/HyperFrames motion graphics | Existing media skills are relevant to video production, not a homepage setup prerequisite. No bulk transcription/render installation for this task. |
| 25 | Design OS | Existing AI OS plus small reference/artifact index serves discovery. A new whole-machine vision index is a separate project, not a prerequisite; no automatic scan of private assets. |

## Current source/install patterns

Ready React workspace: `C:/Users/Joshu/dev/ai-os-projects/dashboard-design-lab`. Core dependencies are installed; run `npm run dev` there for port 5187. Its README covers build and headless browser checks. It is an optional component workspace, not a replacement for the unfinished HTML directions. Adjacent `react-bits` and `canvas-ui` repositories provide source.


Ready local font assets: `C:/Users/Joshu/dev/ai-os-projects/dashboard-design-assets/fonts` contains Manrope, Newsreader, Space Grotesk and IBM Plex Mono with OFL licences and a source/hash manifest. They are options, not required styling.

- React Bits: run the existing skill's `scripts/rb-add.mjs`; fetch current source instead of recalling it.
- Canvas UI: official individual install example is `npx shadcn@latest add @canvas-ui/liquid-react`. Treat it as an example, not a direction to add Liquid by default.
- [Shadcn MCP](https://ui.shadcn.com/docs/mcp) can browse registries. Inspect selected items and install only in the intended app checkout, not the Obsidian vault.
- Local HTML mocks are not React projects. Do not paste JSX or add a package.json merely because a library exists; use a deliberate prototype build when a chosen component needs React.

## Evidence qualifications

The PDF's counts/prices/product statements are dated September 2026 and may change. Current official sources verified Refero access, Canvas registry and licence, shadcn flow, Tabler licence, Iconify per-set licensing and Lordicon attribution. Fontshare download-specific terms still need checking for any selected font. No blanket paid entitlements or account access are established here.

The React Bits helper previously pointed to `DavidHDev/react-bits/AGENTS/SKILLS/` for four animation skills. That path returned 404 and the current upstream tree did not list those skills on 2026-10-23. Do not claim they are installed or invent replacements. Existing GSAP/Impeccable skills supply useful review capabilities.
