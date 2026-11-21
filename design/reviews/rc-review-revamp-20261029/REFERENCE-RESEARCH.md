# RC drill review: make the reading set tangible

2026-10-29. Read-only source research for the authorized Review-page overhaul. The approved finder and builder conditions panel are outside this redesign.

## What was actually inspected

- Firecrawl CLI 1.26.3 authenticated; status reported 1,254 credits available. Two targeted searches and two first-party scrapes completed. The first overconstrained multi-domain search returned zero results and cost zero credits. Targeted searches reported two credits each. No feedback telemetry sent.
- Read first-party page text and image references for Readwise Reader and Things. Saved results are beside this report. These establish product claims and available visual-reference URLs, not runtime behavior.
- Fresh pixels were NOT inspected by this child: child CUA exposed no IAB browser and a separate Chrome research-tab creation detached. No existing parent tab or app code was touched. URLs below should be opened by the parent's working CUA before visual acceptance.
- Read the current shared design hub, principles, methods, local question-access research and current product direction. Read Taste v2's entire app-screens reference in bounded chunks, Impeccable bolder reference and Emil's interaction guidance.

## Two directly relevant references

### Readwise Reader: a publication, not a database row

Primary page: https://readwise.io/read

Specific first-party visual regions exposed by the scrape:

- Library-to-reading relationship: https://d34adp677peecb.cloudfront.net/static/images/reader/Hero-Screen@1x.72ad6bf1deaa.webp
- Mobile reading object: https://d34adp677peecb.cloudfront.net/static/images/reader/Hero-Phone@1x.f61ef28b293d.webp
- Document and annotation: https://d34adp677peecb.cloudfront.net/static/images/reader/Highlight-Alpha-No-Note@1x.28c2c4cc2706.webp

Observed in source text: Reader unifies multiple document types and treats annotations as a primary feature. The first-party page offers dedicated library, mobile and highlighted-document images.

Transfer to RC, proposed rather than observed: the passage title should be the object of attention, with the official address and question count supporting it. A deliberate revealed state should become a readable document surface, not a tiny text dump below a generic row. Restrict unexposed Review to metadata; never use document excerpts as decorative imagery.

Do not transfer Reader's open-ended annotations or automatic document opening into RC. RC has explicit exposure and launch contracts.

Saved source: readwise-reader.md; search: firecrawl-reader.json.

### Things: a concrete plan with a controlled expansion

Primary page: https://culturedcode.com/things/features/

Specific first-party visual regions exposed by the scrape:

- Ordered project groups: https://static.culturedcode.com/things/videos/2017-05-18-website-videos/4-headings-mac.png
- Detail expansion/checklist: https://static.culturedcode.com/things/videos/2017-05-18-website-videos/5-checklists-mac-2.png
- Today/evening separation: https://static.culturedcode.com/things/videos/2017-05-18-website-videos/2-today-mac.png

Observed in source text: Things groups projects with headings, keeps optional detail subordinate, and describes opening a task into a paper-like writing surface. These are first-party descriptions; motion has not been played here.

Transfer to RC, proposed rather than observed: treat the selected passages as a short ordered itinerary. Keep a strong numeral/address anchor, a readable passage title and one concise factual line per passage. Opening one passage expands that exact object in place or into a focused reading sheet. The surrounding set remains oriented; it does not become a second editor.

Do not transfer task checkboxes, completion rings or decorative deadlines. No passage is completed at the review stage.

Saved source: things-features.md; search: firecrawl-things.json.

## Strongest composition: an ordered reading set plus a launch contract

The screen's first question is: **Is this the reading set I intend to start, and under which conditions?**

Use a cohesive two-part composition with a shared top alignment and one decisive next action. On desktop, the passage sequence takes roughly two thirds of the content width, while a narrow charcoal launch column carries the count, timing, answer policy and Start. This should feel like a prepared set of reading material beside a compact session instrument, rather than a dashboard of cards.

| Before, from the parent brief | After, proposed | Why |
| --- | --- | --- |
| Flat beige rows with nearly equal visual weights | One warm-paper reading-set plane. Passage title at 22-28px; address and facts at a legible 14-15px; substantive sequence numeral at 20-24px | The selected reading material becomes the subject |
| Large unassigned horizontal gaps | Grid built from title length, metadata and action placement; 24-32px item spacing, short dividers where needed | Calm comes from repeated geometry, not leftover width |
| Repeated generic reveal buttons | One precise per-passage disclosure, aligned to that passage, with explicit exposure consequence | The action says what opens and does not compete with Start |
| Weak isolated CTA | Compact charcoal session contract with one full-width, high-contrast Start drill button; Edit setup remains a quiet text action | The summary and commitment become one decision |
| Post-click text dump | Readable passage sheet, clear address/title anchor, narrow prose measure, restrained question/answer boundary, explicit close/back | The revealed state deserves as much design as the closed state |

Specific character should come from RC: actual official passage addresses, true order, passage/question counts and exact timing. No invented cover images, random categories, fake confidence scores or generic activity artwork.

## Material and behavior constraints

- Preserve selected warm off-white, soft charcoal, Outfit and any approved existing display face. The local principle is a ground, a reading plane and a focal working plane. A subtle edge/contact shadow can make paper tangible; a blurred haze or another rounded card per metadata item cannot.
- All four passages of a full set should be recognizable on an ordinary desktop first view when titles fit. A one-passage set should keep its natural content height, not stretch a row into an empty page.
- The launch summary follows the set on phone, but its compact summary/Start must remain easy to reach. A sticky action dock is acceptable only with reserved bottom space and no covered text. Do not hide passage identity to fit secondary decoration.
- Expanded preview uses an appropriate prose measure, about 60-75 characters, and body type at least 16px. Preserve comparative passage A/B structure. Use a clear exposure acknowledgment before revealing, and retain the existing backend semantics.
- Keep order, exact IDs, reveal mode, timing, training restrictions and shortfall/duplicate-start recovery unchanged. Visual hierarchy must not imply that looking at metadata recorded exposure.
- Use visible focus, 44px touch targets and valid expanded/collapsed relationships. Error/retry stays by the operation that failed; existing material should not disappear during refresh.
- Emil: do not animate frequent keyboard interaction; occasional disclosure can use a short, interruptible transition. No entrance parade, parallax or continually moving header. Honor reduced motion. Test closing and returning focus, not just opening.

## Taste v2 app workflow, adapted to the brief

Read whole: C:/Users/Joshu/dev/ai-os/.agents/skills/design-taste-frontend/references/app-screens.md.

1. Inventory real objects, fields/units, magnitudes, jobs and product-specific objects; write the first question and next questions before composing.
2. If dealing a direction, run from the app checkout:

```text
node C:/Users/Joshu/dev/ai-os/.agents/skills/design-taste-frontend/scripts/draw.mjs --app --kind <listed-kind> --brief "RC drill review: ordered reading set and explicit launch conditions" --screens detail,builder --theme light --keep palette,type --options 3
node C:/Users/Joshu/dev/ai-os/.agents/skills/design-taste-frontend/scripts/draw.mjs --app --kind <listed-kind> --brief "RC drill review: ordered reading set and explicit launch conditions" --screens detail,builder --theme light --keep palette,type --style <chosen-id>
```

Use --list kinds if needed; do not invent an accepted kind or choose a style merely because it is familiar. The explicit user brief and selected LSAT U material language override generic no-shadow/no-hero defaults. Record the reason for the choice or adaptation. Do not rebuild the approved finder/right builder or whole app shell.

3. Grid arithmetic and both shell widths first, then real data, then empty/zero/loading/error/hover/selected/focus/disabled states. Derive repeated counts from the same data. Biggest thing must answer the screen's question. Peer items share edges and pitch; do not stretch short content into voids.
4. Static lint:

```text
node C:/Users/Joshu/dev/ai-os/.agents/skills/design-taste-frontend/scripts/lint.mjs --app <changed-source-files>
```

The skill normally calls inspect.mjs --app for 1440/768/390 screenshots and measurements. This environment's browser rule requires CUA, so use CUA for equivalent checks and state that the standalone inspector was not run. Relevant checks: real loaded type, no horizontal overflow, intended edge alignment, no unassigned voids, no words under11px, real contrast4.5:1, action visible and reachable, dark/light treatment, keyboard and reduced motion.
5. Critique pictures, fix the worst three, inspect again. Skill caps visual iteration at three rounds. Report chosen style/seed if dealt, product-specific face/signature, one question, allowed exceptions and actual data/verification limits. No motion floor applies.

## Evidence boundary

The composition recommendations are a local synthesis. The two first-party references support specific interaction concepts, but their pixels and natural playback have not yet been seen by this child. Do not label the proposed composition visually validated until the parent opens the referenced regions and compares matched local desktop/phone Review and revealed states.
