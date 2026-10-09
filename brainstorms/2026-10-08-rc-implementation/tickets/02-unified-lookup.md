# 02: Give question lookup one consistent selection state

**Blocked by:**01 reviewed. **Scope:** RC-20,21,24 and selection portion of19.

Own shared QuestionFinder/QuestionJump selection logic, finder hooks and related styles/tests. Use the existing shared finder. Sidebar and landing entry must open it with the same selected bank/address. Leave the final Open question action disabled until ticket03 supplies the safe preview; replace immediate selection launch now.

Retain bank/test/section/question choices. Group RC question options beneath passage title and official range; show concise item labels with full accessible addresses. Auto-select the sole RC section. A genuine bank/test change resets invalid dependent choices. Loading failures preserve valid choices and offer Retry. Use container-aware wrapping and visible scroll affordances.

Existing behavioral seams: QuestionJump.test.tsx, QuestionFinder.test.tsx, questionFinderSearch.test.ts. Replace the old expectation that selecting a question immediately launches.

- [ ] Choosing a question retains its label without navigation or persistence.
- [ ] Both finder entries share state; PT140S4 selections survive opening the finder.
- [ ] Q1–27 appear under the correct four passage groups.
- [ ] Bank/test resets, unique-section selection and invalid addresses behave predictably.
- [ ] Read failure shows Retry, with no silent empty success.
- [ ] Keyboard arrows/typeahead/Escape/focus return work; no clipped action at narrow/docked width.

This intermediate slice may show a clear unavailable preview action; never route to the current session-creating RC passage entry as a substitute.
