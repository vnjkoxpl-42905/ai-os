# 05: Separate official question identity from drill progress

**Blocked by:**03 reviewed. **Scope:** RC04,13,15,16.

Own player breadcrumb/details, directions, navigation overview and review wording. Use official question.position for source citations; show drill ordinal separately as N of total. Rename Set Number/Difficulty to Passage/Passage difficulty and use digital answer-choice directions.

Provide a compact passage-grouped question overview when the existing pager exceeds usable narrow-screen space. Show answered/unanswered/flagged status; expose correctness only after the configured reveal boundary. Preserve current question focus, passage scroll and keyboard navigation.

Explain protected source answers separately from any personal tools the mode permits. An in-progress session requested as review must not silently resume its timer under a read-only promise. Use an explicit route outcome consistent with ticket03.

Existing seams: RcPlayer.saveSafety.test.tsx, RcPlayer.studyAids.test.tsx, rcSessionDestination.test.ts, protected history/results and shared footer tests.

- [ ] A mixed drill's ordinal never appears as the official question number.
- [ ] Details, breadcrumb and overview agree on the selected source address.
- [ ] Narrow navigation preserves focus and passage position without answer leakage.
- [ ] Protected answer/flag/clock/completion restrictions are enforced and clearly described.
- [ ] Review of in-progress content causes no silent timer/answer mutation.

Keep correctness-key repair outside this ticket.
