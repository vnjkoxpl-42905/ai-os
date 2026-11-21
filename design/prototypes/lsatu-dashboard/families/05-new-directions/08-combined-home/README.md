# LSAT U combined local preview

Local interactive synthesis authorized by Joshua on 2026-10-24. Existing prototype versions and the production application remain separate. This preview uses synthetic sample people, assignments, dates, results and original demonstration questions. It does not connect to an account, send messages or publish changes.

## Open

Serve this directory with a local HTTP server. The session preview is planned at http://127.0.0.1:5198/. Open index.html through that server. There is no build step or external runtime dependency. Font and image files are included locally.

## What carries forward

- Existing sidebar and distinct Home / My Work / Practice / Review / Progress / Library destinations.
- Refined/Margin typography, paper/charcoal surfaces and orderly work rows.
- Lamplight one-task contrast within a compact assignment card.
- Atmosphere paper-landscape fragment, rather than a full-screen hero.
- Carrel message sender/time/actions and teacher student lookup.
- Marginalia task-linked context and readable links.
- Lumen/Refined selected calendar day and linked agenda.
- Studio question lookup, saved/recent access; Refined Studio result strips and revisit.
- Bounded state transitions, stable navigation and reduced-motion equivalents.

Practice owns Find a question. Library remains lessons, activities and bootcamps. Hash routes are prototype view navigation, not new production URLs.

## Boundaries

Sample question references identify original demo items only. Unsupported references must show an honest message rather than relabel an available sample. Assignment previews are not full production drills. Saved notes/bookmarks/read state use this browser's local storage only; they are not cross-device or backend persistence. Teacher preview is a demonstration, not an authenticated role switch. No outbound messaging action is provided.

## Assets and context

- assets/paper-landscape.png copied unchanged from 07-atmosphere/assets/paper-landscape.png, the original generated prototype artwork.
- Local Manrope, Newsreader (regular and italic variable) and IBM Plex Mono copied from dashboard-design-assets/fonts with included OFL notices.
- PRODUCT.md and DESIGN.md are reference snapshots from the role-home checkout, not new records of production state. BRIEF.md documents this user's later scoped direction and overrides older conflicting aesthetic declarations.
- Source design review: C:/Users/Joshu/dev/ai-os/research/2026-10-24-dashboard-adoption-review/REPORT.md.

## Verification

Completed in headless Microsoft Edge using the existing Playwright installation on this machine.

- Home rendered at 320, 390, 768, 1100, 1440 and 1920 pixels. The seven other student views were captured at 1440 and 390. Zero horizontal overflow, page errors or failed HTTP responses in those captures.
- Thirteen browser interaction groups passed: preserved resume identity; assignment/quick setup previews; work filters; calendar keyboard/agenda; preparation Save/Cancel; reply retention across mark-read and navigation; local persistence; keyboard finder and empty search; exact supported/unsupported references; bookmarks/recents; hint before explanation; Review revisit; Library keyboard tabs; teacher lookup/draft preview; mobile menu/Escape/focus; injected storage failures. Related checks share groups in the report.
- Natural route motion was sampled while running and after settling. The 220ms transition settled to full opacity; inner filter changes do not replay the heading entrance. Runtime reduced-motion changes disabled spatial motion.
- Native dialog Tab traversal did not focus underlying interactive controls. Escape and trigger focus restoration were checked, including nested teacher draft replacement.
- Teacher mobile role selection and student table rendered without horizontal overflow. Visible control focus computed to a 2px solid outline.
- Final targeted Home captures at 1440, 390 and 320 confirm the narrow agenda action starts on its own row.

Actual screenshots were opened and visually inspected. Parent inspected Home at narrow, phone, mid and desktop sizes, the finder desktop/phone, Review desktop, teacher desktop/phone and natural-motion frames. An independent visual reviewer inspected My Work, Review, Library, Progress, Messages and Reading Center at desktop and phone widths. No blocking visual finding remained in that bounded review.

An independent source reviewer found unsaved replies were lost on mark-read/navigation. The working draft is now separate from the persisted value; browser regressions and source re-review confirmed the repair. Other iteration fixes: larger supporting text and touch targets, correct variable-font weights, readable field boundaries, compact quick actions, distinct mobile/desktop role selectors, preserved nested-dialog return focus, precise negation wording, no heading animation on inner filters and the 320px agenda layout.

Evidence: artifacts/capture-report.json, interaction-report.json and motion-focus-report.json, plus the named PNGs and replayable scripts beside them. The final focused Home recaptures followed the small agenda-layout change; the earlier comprehensive capture report remains dated evidence for the other routes.

Limits: no authenticated production walkthrough, live data integration, physical-device check, complete screen-reader audit or continuous-video performance assessment. These are original sample questions and design/workflow previews, not complete live activities. No commit, push, merge, deployment or Lovable credit use.

Run the checks with Node:

```powershell
node artifacts/capture.cjs
node artifacts/interactions.cjs
node artifacts/motion-and-focus.cjs
```

The verification scripts reference the existing Playwright installation in C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules. The preview itself has no dependency on that checkout.
