# Claude Opus 5.5 final visual critique

Observed model: claude-opus-5-5. Verdict: REVISE. Screenshots reviewed through Claude Read, not a live browser.

The design works. The cobalt, coral, yellow and lilac palette is expressive and well judged. The ceramic knot holds its own stage on every breakpoint. The order now runs hero, then session, then week, then desk, then results, then library, and that reads well. The prior changes are visible in the pixels and match the source: the 12-tick progress bar, the outlined session button with a large 7:15, labelled calendar days placed right after the hero, per-skill results rows, the dynamic 02 count badge, and the nav count removed.

The suspected phone session-button clipping is not a page defect. pass-3-hero-390.png is a 350px-wide crop that ends partway down the coral card. The full-page pass-3-390.png shows the same card complete, with its button, bottom padding and rounded corners. Nothing in the CSS clips it either: `.session` has no overflow or fixed height.

Real issues remain:
- **Visible copy bug on phone:** the results card reads "Your recentpractice." with the space missing.
- **Small type at tablet and phone:** the claim of "enlarged copy throughout" does not hold below 900px, where text drops to 8–10px.
- **Low-contrast small text:** several muted labels fall just under 4.5:1.
- **Tablet sculpture:** the knot is cut flat against the hero's right edge.
- **Planning details:** time estimates are hidden on tablet and phone, and saved day intentions don't update the week chips.
- **Accessibility gaps:** a few labelling and announcement problems.

None of these is high severity. They are concrete enough to fix before calling the prototype final.

## F1-missing-space-recent-practice (medium)

pass-3-390.png shows the yellow card heading as "Your recentpractice." (around y≈1220 in the displayed image, ≈2050px at full size). Cause: index.html:14 has `<h2>Your recent<br>practice.</h2>` with no space around the <br>, and style.css:33 (max-width:680px) hides it with `.practice-header h2 br{display:none}`, which joins the two words. The library paragraph avoids this because it already has a space after its <br>.

**Recommended fix**

Write `Your recent <br>practice.` (add a space before the <br>), or drop the br-hiding rule and control wrapping with max-width or text-wrap:balance.

## F2-subscale-type-tablet-phone (medium)

The 681–900px overrides (style.css:25 and :32) set `.metadata{font-size:8px→9px}`, `.hero-bottom>span{font-size:9px}`, `.tutor-line strong/span{10px}`, `.prep-peek{10px}`, `.session .button{10px}`, `.kind-toggle span{9px}`, `.question-ticket .ticket-ref/small{9px}` and `.shelf-tabs button{10px}`. You can see it in pass-3-768.png: "Logical reasoning • Guided drill", "One-to-one tutoring", "About 15 minutes" and the sample tickets are barely readable. On phone, style.css:33 sets the calendar's `.week .day>span` and `.day>small` to 8px; in pass-3-390.png, "Questions" and "Flaw drill" are tiny. The 768 layout has plenty of room, so this is not forced by space.

**Recommended fix**

Set a floor of about 11px for metadata and secondary labels and 12px for button text at tablet. Remove the tablet-only downsizing in the 681–900 blocks. On phone, show weekday letters plus the date, raise the task label to at least 10px (shorten to e.g. "Flaw" or "Q's"), or make the week strip scroll horizontally with wider chips.

## F3-small-text-contrast (low)

Contrast estimated from the CSS colours: unselected `.shelf-tabs button` #81738c on the console's #faf8fc is about 4.2:1 at 10–12px (style.css:23/30). `.sample-label` #76684e on the yellow card is about 4.3:1 at 10–11px (style.css:23). Unchecked `.kind-toggle span` #746582 on #ece7f2 is about 4.3:1. `.question-ticket>small` #756786 on #ede7f5 is about 4.2:1. All of these are small, non-bold text, so they fall short of WCAG AA's 4.5:1.

**Recommended fix**

Darken these muted tones by about 8–10% lightness, e.g. #6b5e78 for shelf tabs and ticket captions, #665a42 for the yellow sample label, and #62557a for the unchecked toggle. Hue and palette stay the same.

## F4-tablet-sculpture-cropped (low)

style.css:25 sets `.sculpture-stage{width:150px;right:-15px}` inside `.hero{overflow:hidden}`. sculpture.js scales the knot to about 146px wide in a 150px canvas (scale=min(w/3.7,h/3.8)), so roughly 12–15px of the knot is cut off. In pass-3-768.png the right side of the knot is sliced flat against the card edge at x≈438. It reads as an accident, not a deliberate bleed, unlike the clean centred stage at desktop and phone.

**Recommended fix**

At 681–900, use `right:0` (or a small positive inset), or shrink the stage and narrow `.hero-copy` so the whole knot fits. If a bleed is intended, push it far enough off the edge that it clearly looks deliberate.

## F5-durations-hidden-small-screens (low)

style.css:16 (max-width:900px) sets `.assignment-end>span{display:none}`, so the "20 min" and "12 min" estimates disappear on tablet and phone. pass-3-768.png and pass-3-390.png show only arrows. Time estimates are the planning detail students most need on the device they likely use for quick sessions, and the 768 row has spare width.

**Recommended fix**

Keep the duration visible: move it into the metadata line (e.g. "Logical reasoning • Guided drill • 20 min") below 900px instead of hiding it.

## F6-day-chip-accessible-name-and-announcement (low)

app.js:43 gives each day button `aria-label="Saturday, October 24"`, which replaces its visible content (SAT / 24 / Session). Screen readers never hear the task labels (Session, Recall, Flaw drill), and the visible text "Session" is not in the accessible name (WCAG 2.5.3). selectDay (app.js:44) updates #agenda-title and #agenda-copy, but the agenda has no live region, so selecting a day gives no spoken feedback. Separately, `.segmented`, `.bars` and `.shelf-tabs` in index.html:13–15 carry aria-label on plain divs with no role, so those labels are ignored.

**Recommended fix**

Include the task in the name (e.g. `aria-label="Saturday, October 24 — Session"`) or remove the aria-label and use visually hidden text. Add `aria-live="polite"` to the agenda text container. Add `role="group"` to the labelled filter, results and shelf containers.

## F7-saved-intention-not-reflected (low)

After saving an intention for Sunday through plan() and 'save-plan' (app.js:45–46), selectDay replaces only #agenda-title. The chip label stays "Open" (hard-coded array, app.js:43), no dot appears, and #agenda-copy still says "An open day. Add one intention or leave it open." This contradicts the saved title, and the week view doesn't show that anything was planned.

**Recommended fix**

When plans[i] is set, change the chip's <small> to "Planned", show the dot, and change the agenda copy (e.g. "Your intention · Edit"). Re-render the chips after saving.

## F8-nav-affordance-coherence (low)

In index.html:5, the desktop nav's `.active` class is static: after clicking My work or Question library, "Overview" stays highlighted, as nothing in app.js updates it. "Practice" links to #practice, which is the results card, not a way to start practice. Desktop nav also omits "Your week", while mobile nav includes it. Several buttons that open in-page dialogs use the external-link ↗ glyph ("Joshua's note ↗", "Explore this sample ↗", "Saved 0 ↗"), which suggests they leave the page.

**Recommended fix**

Update the active link on click (and optionally on scroll with IntersectionObserver), using aria-current="page" or "location". Rename the nav item to "Results", or point "Practice" at the free-practice launcher. Add "Your week" to desktop nav for parity. Replace ↗ with → (or an open-panel icon) on buttons that open dialogs.

## Coverage

Read PNG: C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/05-studio/artifacts/pass-3-1440.png
Read PNG: C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/05-studio/artifacts/pass-3-hero-390.png
Read PNG: C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/05-studio/artifacts/pass-3-library-390.png
Read PNG: C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/05-studio/artifacts/pass-3-768.png
Read PNG (additional, used to settle the phone CTA question and check the phone mid-page): C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/05-studio/artifacts/pass-3-390.png
Read source in full: index.html, style.css, app.js, sculpture.js
Phone session-button clipping checked against the full 390 capture and the .session/.opening-grid CSS: no clipping. The hero-390 artifact is a cropped capture.
File modification order (Glob, oldest first) puts sculpture.js, index.html, app.js and style.css before all pass-3 PNGs, so the screenshots should reflect the current source; no later source changes found.
Interaction logic traced in source: progress/drill completion, day selection/plans, work filter count, results set selection, shelf modes, reference form, mobile menu, Ctrl+K, dialog focus return, reduced-motion handling in app.js and sculpture.js.

## Limits

Did not read the five reference-lens files (design-critique SKILL.md, impeccable product/color-and-contrast/typeset/animate). Judgments rest on general WCAG and typography practice and the brief's own criteria.
No live browser: hover, focus rings, dialogs, the sculpture intro animation and the result of each interaction were reviewed from source only, not observed. The motion-*.png, question-*.png, pass-3-1024.png and pass-3-hero/library-1440.png artifacts were not inspected.
Contrast ratios were estimated by hand from CSS hex/oklch values, not measured from pixels. The yellow and coral backgrounds were approximated from oklch.
Screenshots were viewed downscaled (1440 at 0.94×, 768 at 0.96×, full 390 at 0.6×), so fine glyph and antialiasing detail could not be judged precisely.
Tests were not run, and nothing was edited.
