# 04: Make RC creation and reading controls easy to scan

**Blocked by:**03 reviewed. **Scope:** RC-22,23,26,12,17; preserve RC05–09/14.

Own Practice landing layout and reading-preferences controls/styles. Replace the oversized competing hero/embedded selector with compact Create RC drill and Open a question entries. Keep unrelated assignments in My Work or a clearly secondary collapsed area on this surface; keep them absent inside active setup. Give inactive tabs readable text and distinct selected/focus states.

Preserve18px /1.6 defaults, responsive passage-only width and current saved text-size behavior. Add announced selected states to spacing and color options using existing radio/pressed patterns. Keep the popup bounded and scrollable, with focus returning to its trigger. Shared LR toolbar defaults must survive.

Existing seams: AcademyMainhub.section.test.tsx, OfficialDrillToolbar.test.tsx, useRcA11y.test.ts, OfficialSmartDrillBar.test.tsx.

- [ ] Create and lookup are visually distinct and have one clear action each.
- [ ] In progress/Completed/Saved sets remain readable against the actual light background.
- [ ] Spacing/color changes are announced and retained across reload; malformed saved settings recover.
- [ ] Long standard/comparative passages remain readable without horizontal text scroll.
- [ ] Browser matrix and200% zoom/text resize show no lost controls, clipped popup or hidden selected state.
- [ ] Reproduce the original clipping condition before declaring its cause/fix; report unresolved conditions precisely.

Avoid a cosmetic test for each class name. Use rendered behavior and actual bounds/contrast/focus evidence.
