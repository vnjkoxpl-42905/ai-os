# Claude 11: design and build a substantial new dashboard direction

2026-10-25. Explicit standalone implementation work order from Joshua. Builder: Claude Opus 5.5, medium effort. Coordinator and independent inspector: Codex. This supersedes the previous review-only plan for this build; it is an unreviewed standalone spec, not covered by that older plan approval.

## User intent and design authority

Joshua rejected version 10 as bland, flat, overly white and blurry-looking, weaker than his live dashboard. He now explicitly assigns Claude the design and implementation and asks for a major jump in quality. Light theme remains preferred. His latest wording says warm apricot/orange is not really the thing: do NOT make those exact colours the brief or merely recolour version 10. Warmth can remain, but Claude owns the palette, composition, typography, material, depth and meaningful motion. Be decisive and produce one excellent, substantially different design, not a collection of options or an incremental CSS patch. Do not call it world class just because the user asked for that standard; earn visual acceptance through the result.

Make the product feel like a carefully designed study environment: immediate next action, credible assignment hierarchy, personal coach context, readable working text, deliberate surfaces. Avoid generic SaaS tile soup, enormous marketing greetings, busy decorative charts, tiny over-tracked mono labels, hazy text, empty white expanses and random orange paint. Use the best saved references critically. Do not erase expressive elements merely because a generic anti-AI checklist dislikes them.

## Ownership and scope

You are not alone in the codebase. Do not revert others' work. You exclusively own NEW files inside this isolated checkout at:
design/prototypes/lsatu-dashboard/new-versions/11-claude-studio/

Write runtime index.html, style.css, app.js and a dated README.md. You may add narrowly scoped files inside that directory. Do not edit root instructions, other generations, the source archive, app repositories, archive catalog/index, or any external service. No commits, staging, push, deploy, paid provider calls, account login, real student data or connected messages. Codex handles archive registration and asset-copy integration after your build.

The checkout is intentionally sparse and initially clean, based on 7e3a37c49aad80bc3d36352b796612425fe9b051. Original source assets are readable at the absolute paths below, outside your checkout. They are references only. Do not spend time rebuilding the checkout or installing dependencies.

## Reference inputs (read relevant portions and images)

- Shared hub: C:/Users/Joshu/dev/ai-os/design/README.md, then relevant design/library.md links. Do not load the entire vault.
- Existing 10: C:/Users/Joshu/dev/ai-os/design/prototypes/lsatu-dashboard/new-versions/10-type-refinement/{index.html,app.js,style.css,PRODUCT.md,BRIEF.md}; its artifacts/home-1048-viewport.png and before-home-1048.png show 10 and09.
- Prior generation: .../new-versions/09-focus-studio/ and archive families/05-new-directions/ and families/04-claude-v2/ (inspect a bounded selection, not every file).
- Adoption research: C:/Users/Joshu/dev/ai-os/research/2026-10-24-dashboard-adoption-review/REPORT.md.
- Canonical app Home source: C:/Users/Joshu/dev/ai-os-projects/lsatu/src/components/classroom/home/{ClassroomHomeView.tsx,home.css} and ../classroom.css. It has warm top-panel light, assignment taupe, lighter sidebar, contrasting dark Continue. Source CSS has later overrides, so reading a gradient does not prove it renders. Do not use the heavily dirty role-home checkout as a live baseline.
- Optional design skills: C:/Users/Joshu/dev/ai-os/.agents/skills/impeccable/SKILL.md and C:/Users/Joshu/.agents/skills/frontend-design/SKILL.md. If applying them, follow their context gates and relevant references, but Joshua explicitly delegates design choices here. Historical DESIGN.md neutral-only Workroom rules do not override this brief. No new approval interview is required for your delegated choices.

Important evidence limit: fresh unauthenticated https://lsatprep.study/classroom redirects to /auth. No signed-in live dashboard capture exists for this task. You may build a local design study now under this explicit user authorization, but must not claim it matches or beats verified production. Do not stall on inaccessible production auth. Use source and saved renders honestly and record that limitation.

## Preserve the product's useful behaviour

Prefer reusing/adapting version 10 app.js over replacing proven behaviours with dead links. You may restructure its rendered markup extensively for your design. Keep:
- Student Home, My Work, Practice, Review, Progress, Library, Reading Center, Messages; teacher preview and student roster may remain inherited functional secondary views.
- Resume task, assignment type/status/search filtering and sensible open actions.
- Exact question finder (including typed references), demo question display, bookmarks/recents, review links opening the matching item.
- Coach message context, local reply draft, mark read, session preparation notes with draft retention.
- Keyboard shortcut, accessible labelled dialogs, focus return, Escape, no shortcut destroying an unsaved modal, responsive navigation.
- Every action is explicitly local/synthetic; do not imply a real message was sent or real work assigned. Library remains curriculum, question finder remains Practice. No external links pretend to provide implemented local features.

Original synthetic question/history fixtures must remain labelled as demo content. Preserve localStorage separation: use lsatu-claude-studio-v1 (not 09 or10's namespaces). Keep all earlier files untouched.

## Runtime and assets

Standalone portable HTML/CSS/JS, no install/build/network dependency. index.html must work over local HTTP and file:// with relative paths. Reuse local fonts/art; no CDN. Codex will copy version10's entire assets directory into your output unchanged after the build, so you may directly reference assets/fonts/manrope.ttf, newsreader.ttf, newsreader-italic.ttf, mono.ttf, and assets/paper-landscape.png. Preserve licenses/manifest. You may ask in your result for specific additional EXISTING archive assets for host copying, with source/destination; do not download fonts or images. Do not use missing font files or accidental fallbacks. Prefer clarity and thoughtful material to broad blur.

## Delivery and proof contract

Produce the concrete finished runtime, not just a design document. README explains chosen visual direction, borrowed strengths, preserved features, local synthetic limits, files authored and verification you actually ran. Include a short design-decision note identifying what changed substantially from10. Do not self-certify aesthetics with a score.

Agreed builder proof: node --check design/prototypes/lsatu-dashboard/new-versions/11-claude-studio/app.js

If your shell is denied, do not bypass permissions or reconstruct tools. Finish allowed edits and report the exact denial; host will copy assets and run proof/browser checks. Host has installed Playwright via C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright and Edge; no new browser install needed. Do not start a server or browser yourself if unavailable.

Codex independently checks every changed file and verifies rendered 1440,1048x858,390,320 views, readable text and contrast, no document horizontal overflow, whole controls, local/offline assets, keyboard/modal protection, filters/finder/review/drafts and archive registration. Codex presents a comparison board to Joshua; user visual judgement remains decisive. Independent fresh Codex inspection follows your build (two inspection rounds maximum, two fix rounds maximum). Production unchanged throughout.

## Recorded host takeover after the two bounded builder fixes

Claude's two fix rounds resolved tools overflow and numbered-cell overlap, but the final320px200% Home still measured332px document width because calendar note words exceeded the remaining third column. Codex owns a narrowly scoped compatibility edit using calendar container queries: a36rem threshold selects the contained day list and a12rem threshold gives notes a full row only when the text-scaled available width requires it. These supersede the first host380px cutoff after review found intermediate-width risk. No text shrinking, clipping, hidden overflow or JS change. This is mixed authorship limited to those CSS rules; the visual direction and runtime remain Claude authored. The two native Codex reviews cover Claude's work before this host correction. A fresh read-only Claude artifact review now covers the host correction and current final runtime; it is an explicitly recorded workflow deviation after the original Codex CLI inspection failed before launch. No third delegated build fix is requested. No new user approval is inferred from review.
