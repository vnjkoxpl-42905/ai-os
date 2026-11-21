# Dashboard design readiness, 2026-10-23

## What was checked

Read all 15 pages and all 25 tips in `C:/Users/Joshu/Desktop/25 Claude Design Tricks Guide.pdf`. Checked the latest Claude setup chat `7e5892fc-cc12-43d3-a32e-c1bf2521b10b` and Codex chat **Add react-bits to skills** (`01a16750-61c0-7ce2-a1fe-582b2dbfd23d`), current files, and selected official resource documentation. The guide is third-party advice, not an instruction to install every linked tool.

The complete tip-by-tip decisions and source links live in [the shared resource map](../.agents/skills/design-resource-library/references/resources.md).

## Already usable

- Tavily, not Tablet: eight global skills in both runtimes. Latest Claude setup chat records successful search and extract.
- Firecrawl: CLI retained; redundant MCP removed in newer setup. Latest chat records successful search and scrape. Bash/Windows PowerShell startup now loads only the Tavily and Firecrawl keys from the central `.env`; no credential values included here. PowerShell 7 startup is not verified.
- Godly: both runtimes point to the existing sibling server. Search/detail tools provide public metadata and image links; inspect images in a browser to evaluate design. A tool connection alone is not visual review.
- React Bits: existing live-registry helper is active in both project runtimes and catalogs. Library clone lives in `C:/Users/Joshu/dev/ai-os-projects/react-bits`. A helper skill is not an installed dependency in every target app.
- Taste, Impeccable, extract-design, existing voice guidance and eight GSAP skills already cover much of the PDF. Preserve customized copies.
- The app already declares shadcn UI dependencies, Lucide, Tabler, GSAP, Three.js and Framer Motion. Check the selected component's exact dependency names before reuse; the separate motion package must not be assumed installed. Optional Canvas UI or Iconify assets can be selected when useful.
- Headless Playwright/Edge capture works via [the existing checker](../system/scripts/verify-dashboard-browser.cjs). It captures screenshots and reports real overflow rather than certifying the UI. The prior Carrel390 check found80px overflow; the favicon404 is minor. Recheck current source after edits.

## Added or repaired in this pass

- Added `design-resource-library` to both project skill activations and both runtime catalogs. It supplies all25 resource decisions, verified links, component-fetching patterns, licence qualifications and visual-check guidance without selecting an aesthetic.
- Corrected the React Bits helper's unsupported pointer to four upstream animation skills. The referenced GitHub directory returned404 and the current tree does not contain them. No phantom skills installed.
- Refero Styles, font sources, Canvas UI, icon libraries and Lordicon are now mapped for discovery. No account/paid entitlement is implied.
- Prepared a local font library at `C:/Users/Joshu/dev/ai-os-projects/dashboard-design-assets/fonts`: Manrope, Newsreader, Space Grotesk and IBM Plex Mono, each with its official Google Fonts repository source, included OFL licence, and SHA-256 manifest. These are optional ready assets, not a prescribed typography direction.
- Added shadcn MCP4.22.1 for Claude and Codex. Its [launcher](../system/scripts/start-shadcn-mcp.cjs) starts in the actual LSAT U checkout: the accepted `--cwd` option did not affect registry handlers in the tested version. Added only the Canvas UI registry URL to that checkout's `components.json`. Actual MCP queries returned48 Canvas matches for liquid and33 shadcn matches for button. No components, app dependencies or layouts were changed.

## Deliberately not installed in advance

Unused effect components, font bundles and icon packs need an artistic selection first. Native Apple HIG is a reference, not a replacement for web accessibility requirements. A Kie account/test generation, new reference-capture extension, universal slider-and-bake tool, video transcription/rendering stack and whole-machine design asset index are separate capabilities, not prerequisites to resume this homepage. Existing image/video skills may be used if needed; no paid generation was run here.

## Ready React workspace

`C:/Users/Joshu/dev/ai-os-projects/dashboard-design-lab` is an independent component workspace with its own lockfile and dependencies. It includes React 18, Vite, TypeScript, Tailwind 3, GSAP, Motion, Framer Motion compatibility, Lucide and Tabler. Local fonts and licences are copied into `public/fonts`. Existing reusable source repositories are adjacent at `react-bits` and `canvas-ui`.

Start with `npm run dev` in that folder, opening `http://127.0.0.1:5187`. `npm run build` typechecks and builds. With the dev server running, `npm run check:browser` uses the existing sibling Playwright installation and Microsoft Edge, writing screenshots and results to `artifacts`. See its README for exact usage. The neutral harness is optional when React components are useful; it does not replace or alter the unfinished HTML directions.

Validation: `npm run build` passed TypeScript and Vite production build. The lab browser check passed in headless Microsoft Edge at 1440px and 390px, with interaction, reduced-motion and overflow checks and no reported errors. Root inspected the rendered desktop screenshot. These checks validate the resource harness, not the unfinished dashboard designs. Evidence: `C:/Users/Joshu/dev/ai-os-projects/dashboard-design-lab/artifacts/browser-check.json`, `desktop.png` and `mobile.png`.

## Remaining access limits

Earlier actual probes found valid21st MCP authentication but catalogue-search failure; signed-in website browsing was available in the checked Chrome profile. Pinterest API token was absent; Pinterest/Mobbin/Dribbble browser logins require rechecking. Cosmos and21st were signed in in that Chrome profile. Fresh headless contexts and the Claude side browser do not automatically inherit it. MotionSites search is available; premium prompt content depends on entitlement. No setup pass can truthfully guarantee every site/account is available.

## Resume

Read the new resource skill selectively, reconnect changed MCPs, continue the paused design work and the owner's original creative brief. Use references/components that earn their place. Visually inspect rendered screenshots and natural motion rather than infer appearance from metadata or test assertions. Do not repeat the full setup inventory before making progress.
