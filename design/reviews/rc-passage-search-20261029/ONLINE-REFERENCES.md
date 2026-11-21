# Online reference research for the left-side passage picker

2026-10-29. Read-only research by supporting Codex agent, separate from Claude Design generation. Original right-side builder is locked. No app files changed.

## Tools actually used

- Firecrawl CLI through existing system/scripts/firecrawl-local.py credential wrapper. First search plus extraction succeeded: five results, reported7credits. JSON: .firecrawl/rc-picker-creative-reference-20261029.json. Warning: some tool-discovery results unavailable; web results and extracted Markdown were returned.
- Tavily basic search through saved TAVILY_API_KEY, loaded only in process memory. Five results returned. No key or unrelated credential output. Search confirmed Tavily access rather than assuming it absent.
- Second Firecrawl search returned four Pinterest paper-sculpture boards. JSON: .firecrawl/rc-picker-material-reference-20261029.json.
- Three bounded search calls total. No autonomous/deep agent. No feedback transmission, installs or configuration changes.

## Three complementary reference directions

| Reference | Evidence obtained | Useful transfer for this task | Limits |
| --- | --- | --- | --- |
| [Raycast](https://www.raycast.com/) | Official product page Markdown extracted by Firecrawl | A compact search instrument with a clear current scope, selected item and visible keyboard affordances. The useful idea is fast intent-to-result rather than a dashboard ornament. | Text extraction only here. No live interaction or screenshot inspection by this agent. Do not claim its visual palette/motion was studied from this extraction. |
| [cmdk by Paco](https://cmdk.paco.me/) and [source repository](https://github.com/pacocoursey/cmdk) | Tavily returned component-source content through a GitHub mirror, describing composable input/list/groups and adaptive list height. Official canonical project route is named in the local upstream pick-ui-library guidance. | Bounded result list, contextual groups, keyboard highlight distinct from chosen state, smoothly adapting result region. Reuse existing RC primitives unless a new dependency earns its cost. | Canonical demo not visually opened in this supporting pass; source excerpt is discovery evidence, not tested library compatibility or current implementation proof. |
| [Pinterest: intricate3Dpaper sculpture](https://www.pinterest.com/ideas/intricate-3d-paper-sculpture/957444621292/) and [paper architecture](https://www.pinterest.com/ideas/3d-paper-architecture/910229752819/) | Firecrawl returned titles/descriptions for exact board URLs, including layered kirigami/paper architecture themes | Inspiration candidate for a layered paper aperture: a recessed search channel, a shallow raised lip, nested address scopes and a panel that unfolds with coherent light/depth. Create original treatment rather than copying an artwork. | Search-result text only. Individual artworks/authors/licences and actual pixels not inspected. Pinterest access was not proven blocked or usable beyond search indexing. Parent/Claude should inspect actual imagery before attributing visual influence. |

## Supporting examined text source

[Command Palette Interfaces, Philip Davis](https://philipcdavis.com/writing/command-palette-interfaces) was fully extracted by Firecrawl. It explicitly distinguishes quick entry, contextual insert, grouping/nesting and palettes inside palettes, with image references to Things3, Notion, Framer and Raycast. Useful transfer: the RC task is contextual selection, not an omnibox performing unknown commands. Keep scope changes legible and make selection explicit. The images were returned as Markdown links but were not opened by this supporting agent.

The first query also returned [react-cmdk](https://react-cmdk.com/) (official component examples), [ReUI command](https://reui.io/components/command) and a LogRocket tutorial. These were discovered/extracted text, not selected as separate visual directions.

## Synthesis and verification boundary

Suggested signature: a search surface with the physical clarity of a carefully machined paper tray. On focus, a precise lip/edge and subordinate layered panel communicate depth. Address steps transform into compact tactile tokens, while results keep crisp title/address/count hierarchy. Use GSAP only if sequencing needs coordinated interruptibility; simple panel open/highlight motion can be CSS/WAAPI. Preserve reduced-motion and pointer-independent access. Do not make result text tilt, blur or wobble.

This record establishes online tool access and reference candidates. The parent also has separately inspected local Mobbin stills. It does not establish visual acceptance of the final Claude Design output, a live search flow, backend correctness, or permission to alter the right panel.
