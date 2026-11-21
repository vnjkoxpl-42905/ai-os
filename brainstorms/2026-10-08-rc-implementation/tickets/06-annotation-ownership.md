# 06: Keep passage marks with the actor who made them

**Blocked by:** None. **Scope:** RC02,03.

Own useRcHighlights, rcProgress and their annotation hydration/debounce tests. Annotations belong to actor+passage and restore across sessions. Explicitly actor-filter reads, including admin reads; include actor identity in hydration dependencies. Capture actor and passage identity at edit time; key pending work by both. Cancel or reject stale work after account/passage changes while preserving unsaved intent under its original actor+passage recovery key. Use a load-state contract that gates editing until loaded, or a versioned merge proven to retain new local edits. A failed read cannot become an editable empty saved map.

Prefer existing hook/storage seams: useRcHighlights.test.ts and rcProgress.test.ts. Control deferred reads/writes deterministically.

- [ ] Actor A edit followed by account B switch never writes A's mark as B.
- [ ] Admin mixed-owner rows are filtered before hydration; a passage-key map cannot collapse another actor's marks into the current actor's view.
- [ ] Same-passage account switch reloads the correct actor's annotations; session changes retain that actor's passage marks.
- [ ] Delayed load cannot overwrite a newer local edit.
- [ ] Read failure preserves recoverable data and offers Retry.
- [ ] Rapid passage changes do not attach marks to the wrong passage.
- [ ] Debounced work is invalidated predictably on actor/surface teardown.
- [ ] Teardown preserves the final pending edit for recovery under its original owner instead of silently dropping it.
- [ ] Protected source answers remain unchanged.

Document the chosen gate-or-merge behavior in the product spec. Return failing-before/passing-after race tests and a bounded browser walkthrough.
