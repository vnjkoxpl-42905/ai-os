# 01: Make every RC bank question discoverable

**Blocked by:** None. **Scope:** RC-18; generated search/address integrity. Read the parent README first.

Own the RC search and finder-address generators, their generated artifacts and necessary build wiring. Locate current owners by their generator names. Preserve question bodies, explanations, keys, frozen exam manifests and attempts.

Current evidence: full bank2150 questions versus published indexes1602. PT140S4 should have27; Q3/id1590 and Q17/id1604 are absent from lookup. Treat counts as the audited baseline; if the current bank changed, document the reason and enforce exact set equality instead of hardcoding an obsolete total. Normal prebuild currently builds the finder index without first rebuilding RC search. Check the RC generator's URL-path handling on Windows.

Deliver regeneration in dependency order and an automated guard for equal question ID/address sets, duplicate rejection and stale-artifact detection. Reuse current generators rather than adding a competing index.

- [ ] PT140S4 exposes all27 official addresses, including Q3 and Q17.
- [ ] Every current bank question appears exactly once in search and address outputs.
- [ ] Missing or duplicate index entries produce a failing check with actionable addresses.
- [ ] Build runs required generation/checks in order on Windows and the project's normal runtime.
- [ ] Compare bank/key hashes before/after; no key or attempt changes.
- [ ] Focused generator regression, typecheck/build and signed-in finder verification pass.

Completion report includes counts, set-difference results, generation commands and intended files. Return for independent review before ticket02.
