# Review log: Teacher Home v2 (2026-11-18)

Roles: Claude (Opus 5.5) planned and built; Codex gpt-6.2-sol, effort low (Joshua's choice), reviewed and inspected. Runner used a scratch git copy because the vault's skill-audit/.git breaks it.

- Plan review: 5 rounds. R1 REVISE THV2-01..05 (counts, mobile search, surfaces, clock, quiet rule). R2 REVISE 06..09 (bar scaling, search focus, event intervals, strip by id). R3 REVISE 10..11 (consultation action, next-per-student). R4 REVISE 12 (opener removed by refresh). R5 APPROVED. All findings accepted.
- Inspection 1 (fresh): REVISE R01..R09; all fixed (bar/strip class collision, detail focus, refresh focus, hero target rows + exhausted calendar, responsive opener fallback, SVG label rendered size, ledger from fixture, in-session planet label, stale search confirmation).
- Inspection 2 (fresh): REVISE REV-01..06; all fixed by Claude, NOT Codex-reviewed (budget of 2 used). Deviation: REV-05 counts stay always visible instead of hover-only; zero day now a dashed baseline.
- Host checks after final fixes: no console errors; orrery and labels inside the hero at 1280/1000/375; labels >= 12px rendered; no horizontal scroll at 375; dock clears last content; Esc/Close returns focus (dock, hero, strip); time states ?t=15:30 / 19:10 / 20:30 and invalid ?t=25:00; search finds Hana Ito; no em dashes.
