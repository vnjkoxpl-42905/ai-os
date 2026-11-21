# 02: Give question lookup one consistent selection state

**Blocked by:**01 reviewed. **Scope:** RC-20,21,24 and selection portion of19.

Own shared QuestionFinder/QuestionJump selection logic, finder hooks and related styles/tests. Use the existing shared finder. Sidebar and landing entry must open it with the same selected bank/address. Leave the final Open question action disabled until ticket03 supplies the safe preview; replace immediate selection launch now.

Retain bank/test/section/question choices. Group RC question options beneath passage title and official range; show concise item labels with full accessible addresses. Auto-select the sole RC section. A genuine bank/test change resets invalid dependent choices. Loading failures preserve valid choices and offer Retry. Use container-aware wrapping and visible scroll affordances.

Existing behavioral seams: QuestionJump.test.tsx, QuestionFinder.test.tsx, questionFinderSearch.test.ts. Replace the old expectation that selecting a question immediately launches.

## Passage groups must have visible boundaries

Joshua confirmed this design requirement on2026-10-08: within an RC practice section, visually separate each passage's questions, following the grouped lookup pattern observed in LSAT Lab.

Use a non-selectable heading such as **Passage1 · Questions1–6**, with the passage title on a quieter second line when available. Place a thin contrasting horizontal rule and12px of separation before each subsequent passage heading. Keep questions compact beneath it: **Question1**, **Question2**, etc., without repeating the passage on every row. Preserve official section question numbers rather than restarting at1 for each passage. Derive ranges from the complete bank; never fabricate a missing question to make a range appear complete.

Use restrained background tint behind headings, readable text, and a selected-row indicator distinct from hover. A divider alone is insufficient: the heading must identify the passage. Headers and rules are not selectable options and are skipped by arrow-key navigation. Use the select library's accessible group/label semantics and give each selectable question a full source address. Keep the menu bounded with visible scrolling; groups stay in official passage order. On narrow widths allow heading/title wrapping rather than horizontal scrolling.

Example layout, using the verified PT140S4 first two passage ranges:

```text
Passage1 · Questions1–6
  Question1
  Question2
  …
  Question6
────────────────────────────
Passage2 · Questions7–13
  Question7
  Question8
  …
  Question13
```

This grouping is also the visual model for ticket05's in-drill question overview. The shared reader should separate passage groups in its navigation; it does not insert rules between unrelated paragraphs within the passage text.

- [ ] Choosing a question retains its label without navigation or persistence.
- [ ] Both finder entries share state; PT140S4 selections survive opening the finder.
- [ ] Q1–27 appear under the correct four passage groups.
- [ ] Every passage transition has a visible rule, space and labelled heading; group headers cannot be selected and keyboard navigation skips them.
- [ ] Official numbering, selected-row visibility and group relationships remain clear at narrow width and200% text resize.
- [ ] Bank/test resets, unique-section selection and invalid addresses behave predictably.
- [ ] Read failure shows Retry, with no silent empty success.
- [ ] Keyboard arrows/typeahead/Escape/focus return work; no clipped action at narrow/docked width.

This intermediate slice may show a clear unavailable preview action; never route to the current session-creating RC passage entry as a substitute.
