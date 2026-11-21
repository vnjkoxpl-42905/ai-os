# Repeat the rendered workout capture

Use `loophole-workout-browser-capture.mjs` inside the active `cua_repl` session, with the user's authorized Loophole tab already bound. Read the current CUA documentation first. This is a recipe with injected UI adapters, not a terminal browser scraper. It deliberately has no login, cookie, backend request, guessed API, network-fetch or credential capability.

The 2026-10-14 inventory exposed four numbered catalog page buttons, `Page 1` through `Page 4` (the selected page button is disabled). Each observed workout row had an `Open view` control. Expanded overviews supplied actual workout-detail and prep-map links. Do not infer additional URLs from titles. If the current UI differs, inspect its fresh accessibility state and update the adapters from observation.

## Bind only documented operations

Import the local module through the permitted local-file facility in the active CUA session. Inject these functions, using the exact API signatures returned by that session's CUA documentation:

| Adapter | Required behavior |
|---|---|
| `ui.currentUrl()` / `ui.navigate(url)` | Read the current observed URL; navigate the already bound tab only if different. The helper skips same-URL reloads during retries. |
| `ui.isButtonEnabled(name)` / `ui.isCurrentPage(number)` | Read observed pagination enabled/selected state. Skip a disabled button only when it is the currently selected page, otherwise stop. |
| `ui.refresh()` | Return fresh `getAXState` for that tab. |
| `observe(state)` | Emit/read the refreshed state so the agent can inspect page/auth/errors. Stop on a sign-in screen or unrelated page. |
| `ui.countButton(name)` | Count exact accessible button-name matches using the documented locator API. |
| `ui.clickButton(name, index)` | Click the exact observed button, using the supplied index or its unique match. |
| `ui.readOverviewRows()` | Read current rendered table-row identities in display order. Include only workout rows whose `Open view` control was observed. Keep their rendered title and row index. This is read-only DOM extraction. |
| `ui.openOverview(row)` | Locate that observed row again by title/index and click its `Open view` button. Do not click bookmarks or complete-workout controls. |
| `ui.readExpandedOverview()` | Read the expanded row's title, full `innerText`, `outerHTML`, and all anchor text/absolute `href` pairs. Return `{name,text,html,links}`. |
| `ui.waitForDetailHeading()` | Use the documented visible-locator wait for the navigated page h1 before expansion. Check the observed URL/title; a navigation return alone does not prove rendered content is ready. |
| `ui.isObservedSourceError()` / `ui.readSourceError()` | Inspect only rendered site error wording (for example Oops), and capture its observed name/text/HTML/links. Never treat a sign-in screen as a source error or bypass it. |
| `ui.readDetailPart(request)` | In documented read-only DOM evaluation, use the exported `readDetailDOM(document, request)` extraction body. Metadata returns only name/links/images/headings; length requests return numeric lengths; slice requests return at most 50,000 characters of text or HTML from `h1.closest('header').parentElement`. If that observed root is absent, stop and inspect. |
| `ui.readFootnoteTriggers()` | Read observed `.cursor-help` inline instruction trigger identities without DOM mutation. |
| `ui.revealFootnote(trigger)` / `ui.readVisibleFootnote()` / `ui.dismissFootnote()` | Use the documented pointer/locator interaction to reveal each observed trigger, capture the visible explanatory text/HTML/links, then dismiss it. Check the exact visible tooltip rather than guessing hidden content. |
| `checkpoint(state)` | With the injected local `fs` binding, serialize arrays to the intake folder after each capture. This is local file writing, never browser evaluation. |

The module exports ordinary JavaScript functions. Do not assume CUA can serialize imported closures into the page. Paste the pure `readDetailDOM` body into its documented read-only DOM evaluation callback if needed. No DOM mutation, app-store access, hidden browser state, injected network call, or page script execution is required.

## Capture and checkpoint

Construct `makeWorkoutCapture({ui, checkpoint, observe, catalogUrl, pageButtons:[1,2,3,4].map(number=>({number,name:`Page ${number}`}))})`. `catalogUrl` must be the observed workout listing URL. Run `captureCatalog()`, `captureDetails()`, then `capturePrepPoints()` in order. The helper:

1. Visits each of the four exact Page 1 through Page 4 controls and refreshes accessibility state. The selected disabled page is read without clicking it; any other disabled page is an error.
2. Reads rendered row identities, opens each row once, and captures the complete expanded overview. Row identities prevent accordion auto-collapse from repeating the first row.
3. Navigates only workout URLs collected from those anchors.
4. Waits for the detail h1, refreshes accessibility state, then clicks every exact `Show More`, `Show more` and `Expand section` control, and refreshes after each click. It stops if an expander fails to disappear or a guard limit is reached.
5. Captures the full detail container and records remaining expanders. It checkpoints each page separately.
6. Deduplicates linked prep-map points by full URL, including prep stage, and captures them with the same expansion procedure. Equal titles in different stages are distinct records.
7. Retries a failed UI operation once after a fresh state inspection. A second failure is checkpointed and raised, never silently skipped.

Write `overviews.json`, `details.json`, `prep-points.json`, `footnotes.json`, and `failures.json` into `raw/inbox/loophole-workouts-2026-10-14/` for this source generation. Use a new dated generation for later captures. Checkpoint safely with a temporary file and atomic rename; preserve existing captured records during resume. Resume by supplying saved overview/detail arrays to `captureDetails(savedOverviews)` and `capturePrepPoints(savedOverviews,savedDetails)`, or by loading saved arrays into the returned `state` arrays before continuing. Do not overwrite a completed prior generation with a partial new run.

The generated catalog treats screenshots, media and attachments separately. Captured `images` contain URLs and alt text. The helper and compiler do **not** download image bytes, linked files, video or audio, and do not reproduce interactive exercises. Report these limits. Original exact HTML remains saved even where the safe viewer omits remote media or executable markup.

When the user authorizes preserving instructional templates, run [the read-only Google export helper](capture-loophole-workout-attachments.py). It uses the approved `gws drive files export` CLI for IDs actually observed in workout links, exporting Sheets as XLSX and Docs as text/PDF. `attachments.json` records successful files, formats, SHA-256 hashes and failures. The compiler verifies those bytes and links successful exports; a captured URL alone does not count as a saved document. Never edit or share the originals.

## Build only after the final inventory check

Compare the captured count with all four rendered pagination totals, inspect representative long numbered instructions and nested lists, and confirm zero remaining expanders on every detail/prep page. Then run:

```powershell
python system/scripts/build-loophole-workout-catalog.py --archive
```

The compiler refuses source hash conflicts, archives without deleting intake, and reports missing detail/prep coverage with exit code `2`. Read `corpus/loophole-online/workouts/verification.generated.json`; a successful script cannot independently prove that an unobserved page or hidden media asset never existed. Open `catalog.html` through the local browser and check search, section/stage filters, expansion, full instructions and prep-point links.

## Preserve broken source links

A prep-map link can render the site’s Oops/error page, especially where an overview uses a different prep stage from its detail page. Capture that response with `status: "source-error"`, preserving its original URL/text/HTML. Do not count it as full prep-point content. Capture successful URLs only when actually observed in links, label them `status: "captured"`, and retain both records. The compiler links same-slug successful captures as related alternatives while preserving the original discrepancy; this is not a claim that unseen error-page content was recovered. Report unresolved broken references separately.

## Inline instruction footnotes are separate source content

After expansion, inspect every `.cursor-help` inline marker. The 2026-10-14 set has 71 markers across 70 workout pages. Reveal each using the documented UI interaction, capture its visible `{text,html,links}`, and store one `footnotes.json` array row per workout as `{name,url,count,notes:[...]}`. Main page HTML alone does not prove this tooltip content was visible or captured. The compiler counts `.cursor-help` markers from archived detail HTML and checks captured note counts before marking footnote coverage complete. It preserves per-workout footnote text/HTML and renders them in the expanded catalog. Future generations must derive the expected count anew; do not hard-code 71 as a universal library total.

## Avoid tool-output truncation and preserve corrected generations

Never round-trip large HTML through printed tool output. Capture long strings in observed DOM chunks (for example 50,000 characters per slice), reconstruct them in the CUA local runtime, then checkpoint with `fs`. Verify reconstructed length, closing container markup and absence of literal `[Truncated]`. Read-only `innerText` is separate evidence from `outerHTML`; an intact text capture does not make truncated HTML complete. If a completed immutable archive contains a faulty capture, retain it and archive the corrected intake as a new generation:

```powershell
python system/scripts/build-loophole-workout-catalog.py --archive --archive-dir raw/sources/loophole-workouts-2026-10-14-complete
```

Generated canonical source pointers follow `--archive-dir`; the original archive remains unchanged. The compiler blocks archival if any intake JSON still contains `[Truncated]`. Its safe viewer closes retained tags so a malformed source fragment cannot turn later workout summaries into links. This rendering repair is distinct from source recapture.

## Bind the chunk adapter without returning the complete DOM string

The helper actually calls `readDetailChunked(ui)`: metadata first, length for each text/HTML string, 50,000-character slices, reconstruction in the local CUA runtime, then exact length verification and a second length check to detect page changes. Its default `readDetailDOM(document, request)` returns metadata only. Bind `ui.readDetailPart(request)` to the documented read-only DOM evaluation operation on the already bound tab, using the function body with the request fields supplied explicitly. Do not return `root.outerHTML` unbounded, and do not print the reconstructed record. The injected `checkpoint` writes its bytes locally through `fs`.

Navigation is followed by fresh AX state, an observed h1 readiness wait, another fresh AX state, expansion of both Show More spellings, and only then chunk extraction. Inline footnotes are implemented in `capturePage`: it reads observed trigger identities, reveals each through the injected documented UI adapter, refreshes AX state, reads visible text/HTML/links, dismisses the tooltip, and checkpoints the resulting footnote array. These adapters must be bound from the currently returned CUA documentation rather than guessed Playwright/CDP signatures.
