# Capture complete routines through the rendered browser

Use `loophole-routine-browser-capture.mjs` in the authorized CUA runtime. Read that runtime's current documentation before binding adapters. This module does not launch a browser or use CDP, cookies, credentials, network requests, hidden state, or guessed URLs.

A routine is an ordered sequence of workouts and sometimes other tasks. A catalog overview alone is not a routine capture. On 2026-10-15, the observed listing had three page buttons and 58 routines, distributed 25/25/8. These are audit expectations for this generation, not universal constants.

## Bind observed UI operations

Inject `ui`, `observe(state)`, `checkpoint(state)`, and the observed `catalogUrl` into `makeRoutineCapture`. `initialState` accepts the previously checkpointed arrays. Bind only operations documented by the active CUA session:

| Adapter | Behavior |
|---|---|
| `currentUrl`, `navigate(url)`, `refresh` | Read or navigate the already authorized tab; refresh returns current AX state for human/agent inspection. Stop on authentication or unrelated pages. |
| `isButtonEnabled(name)`, `isCurrentPage(number)`, `clickButton(name,index)`, `countButton(name)` | Exact observed accessible button names. The selected Page button is disabled and must not be clicked. |
| `readOverviewRows`, `openOverview(identity)`, `readExpandedOverview` | Capture rendered row identities in order, open their observed `Open view` control, then return `{name,text,html,links}` from the expanded overview. Links contain observed absolute hrefs only. Do not click bookmarks or completion controls. |
| `waitForDetailHeading` | Wait for the navigated routine's visible h1 using the documented locator wait. |
| `readDetailPart(request)` | Read-only DOM extraction using `readRoutineDOM`'s body. Root is the observed `h1.closest('header').parentElement`. No unbounded strings in tool output. |
| `readScheduleRows` | Read every rendered schedule row after Show More expansion. Return stable observed row identity, title, amount, and index. Distinguish schedule rows from other tables. |
| `openScheduleRow(identity,index)` | Locate that exact schedule row with the documented `getByRole('row')` API and click its observed `Open view` control. If already open, leave it open. Reacquire locators after updates. |
| `readSchedulePart(identity,index,request)` | Same metadata/length/slice protocol as `readDetailPart`, scoped to the currently expanded schedule row and its inline instructions. Metadata includes `{name,amount,links}`. Text and HTML must include the complete inline expanded content, not just the collapsed name/amount. |
| `readFootnoteTriggers`, `revealFootnote`, `readVisibleFootnote`, `dismissFootnote` | Observe each inline instruction marker, reveal through documented UI interaction, capture `{text,html,links}`, then dismiss. Do not infer tooltip content from marker labels. |
| `openFilter(group)`, `readOpenFilter(group)`, `closeFilter(group)` | Capture observed dropdown content as `{text,html,options}`. Options preserve parent dimension and label, selected state, and any displayed counts. No inferred options. |

`observe` must expose fresh UI state and stop for sign-in, source errors, or changed structure. Do not substitute guessed adapters if the UI differs. Imported JavaScript closures may not serialize into browser evaluation: paste the pure DOM extraction body into the runtime's documented read-only callback when necessary.

## Preserve every schedule occurrence

Run `captureCatalog()`, then `captureDetails()`. The helper opens every schedule row individually and stores its complete content in `sequence`. Accordion expansion can close the previously open row. Therefore the parent detail HTML alone is insufficient: **the ordered sequence array is authoritative**. It intentionally preserves repeated names, amounts, and positions. The first observed routine had six steps, including Test Day Timed Section at both positions two and three.

For every text and HTML field, capture length, then slices of at most 50,000 characters, reconstruct locally, compare exact lengths, and recheck the current length. There is no 200,000-character total cap. Never print a large reconstructed record through the tool channel. `[Truncated]`, short slices, or changed lengths fail capture.

After the listing capture, call `captureFacets` with the five actual observed group labels: Section Impact, Prep Stage, Challenge Index, Routine Progression, and Useful Filters. Capture Useful Filters' nested dimensions separately in `options`; retaining only group names does not establish membership. A compiler must map each option from captured evidence rather than derive it from similar workout labels.

## Checkpoint and resume safely

Use injected local filesystem operations, outside browser evaluation, to write the entire state after each overview, schedule occurrence, completed detail, and filter. Write to a temporary file and atomically rename. Use a new dated intake generation; never overwrite an immutable source archive. The state includes `overviews`, `details`, `facets`, `footnotes`, `failures`, and an optional `partial` routine.

Pass parsed saved state as `initialState` to resume. Completed detail records are skipped. Partial routines restart their schedule capture from row one; incomplete sequences are never treated as completed records. Overview deduplication uses actual observed routine URLs. Duplicate routine URLs across pages fail, while repeated workout names inside a routine remain separate.

Capture failures are checkpointed and raised after one retry with fresh UI inspection. A script's completion is not proof of source coverage. Before compiling, compare captured routines and pagination counts, inspect every expected schedule length, verify no remaining Show More controls, reconcile dropdown membership, and audit linked tasks, Prep Map points, templates, inline footnotes, and media separately. Preserve broken source references explicitly.

## Compile self-contained routine files

The capture helper records exact rendered source content; the compiler owns local presentation and dependency resolution. Each routine file and expanded catalog entry must include its own full instructions, ordered schedule, all notes and examples, and the complete captured instructions for every referenced workout. Reuse the canonical 84-workout source generation when identities match, while preserving routine-specific amounts and changes. Never substitute a source URL for missing instructions. Non-workout tasks and Prep Map content need full local captures too. Keep source URLs only in provenance, separate from the usable routine body.

Record unresolved dependencies, source errors, unexported attachments, and unavailable recordings explicitly. Remote image references are not locally saved images. A capture script cannot truthfully promise that unobserved or inaccessible material was recovered.
