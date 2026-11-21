# Workout catalog browser verification

Verified 2026-10-15 in the Codex browser against the generated local catalog.

- Loaded all 84 workout cards and 62 referenced Prep Map records.
- RC plus TRANSLATION filters returned 15 workouts; searching all captured wording for Cappuccino within those results returned six.
- Expanded Decaf includes its tenth instruction, the 12-minute out-loud / 8-minute silent goal, nested numbered lists, and the original LawHub footnote.
- No links leaked into collapsed Prep Map summaries after the HTML repair.
- All nine saved attachment URLs returned HTTP 200 through the local preview server.
- All 21 files in the corrected source manifest matched their SHA-256 values. Coverage issues are empty; 33 original Prep Map URLs still show source errors, each with a separately captured working topic variant.

[Preview screenshot](catalog-browser.png). [Coverage](../verification.generated.json).

This is a local source-reference catalog. It does not reproduce remote exercises or download all linked lecture recordings and thumbnail images. The reusable browser helper was checked separately; this receipt describes the actual captured catalog.
