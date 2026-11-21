# Conditional opening: Impeccable polish, 2026-10-03

Local preview: http://127.0.0.1:8097/dev/conditional-opening-preview?unit=orientation#co-reading

## What changed

The approved reference order and teaching copy remain intact. Scoped OKLCH room tokens, flat chapter boundaries, consistent heading/paragraph spacing, legible helper text, clearer selected/disabled states, full-width phone diagram choices and a non-wrapping exercise number improve the four opening units. Colored sidebars in the polished exhibits are removed. The low-contrast dark-section kicker now measures 8.91:1; selected diagram answers measure 10.81:1.

Contents is now an opt-in native inline details/summary disclosure. Native keyboard opening and ordered anchor navigation are verified. The shared floating default remains unchanged for other consumers. Obsolete lesson-specific floating-menu protection state is removed.

## Three browser verification passes

1. Desktop: inspected opening reading layout and dark section; keyboard contents opening and anchor navigation; exact missing-requirement feedback. Evidence: desktop-reading.png.
2. Responsive: four units at target viewport widths320/390/720/768/1190,20 checks with equal root client/scroll width. Existing browser zoom80% and scrollbar account for measured301/371/701/749/1171 widths. Tablet contents and phone reading inspected. Evidence: responsive.json, tablet-contents.png, phone-reading.png. Paired diagram checking verified correct original/contrapositive feedback; phone numbering fix rechecked.
3. Accessibility/motion: Enter activates native contents and prediction; system reduced-motion matches and shows zero running animations. Contrast values measured from computed colors via browser canvas. Evidence: contrast.json and motion.json. Temporary viewport/media overrides reset.

Some deep-scroll screenshots returned blank or misplaced captures because of the browser capture/zoom behavior. phone-feedback.png and phone-practice.png are rejected captures, excluded from visual acceptance. They are retained rather than deleted. DOM state and the explicitly listed reading/contents screenshots provide the verified evidence. No physical-device or exhaustive assistive-technology acceptance is claimed.

## Checks

- 174 Vitest tests across11 files pass, including2 inline-contents tests.
- Typecheck passes.
- Final direct Vite production build passes:7,145 modules,1m33s. Existing asset/chunk/Tailwind/Browserslist warnings remain.
- Canonical exclusion passes across771 dist files.
- Scoped ESLint:0 errors,5 existing Fast Refresh warnings. Scoped whitespace check passes.
- Preservation audit:30 units/296 practice questions;62 opening contracts,61 baseline practices;26 later units,4 guided contracts and4 historical originals unchanged.
- No new Claude review or approval claim. No publication, commit, push, live assignment or paid action.
