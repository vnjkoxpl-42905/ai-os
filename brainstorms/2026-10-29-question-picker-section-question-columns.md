# Question picker: split "Section / question" into two columns: Brainstorm / Discovery Notes
Date: 2026-10-29 · Goal: Show Section and Question as separate, labelled columns in the Questions table, without breaking the table's fit.
Status: built on branch, uncommitted (2026-10-29)
Context sources: ai-os-projects/lsatu/src/components/drill/QuestionPicker.tsx (COL widths line 107, header line 1115); screenshot from Joshua 2026-10-29.

## Summary / key decisions
- Headers: "Section" and "Q#". Widths 76px + 52px (Joshua picked 56+56, but "Section" at 16px cannot fit in 24px of content, so both cells use 16px padding and the pair is 128px). Everywhere, one shared component. No sorting.

## Facts found (verified in code, not from Joshua)
- Header today: one column "Section / question", 76px wide, cell renders `2 · 1`.
- A code comment says it was merged on purpose: two headers cost ~112px to show four characters.
- Table is `table-layout: fixed`, min width 644px; only the Question text column flexes (min 204px). Type is 128px, Difficulty 60px.
- The empty-state row uses colSpan; adding a column means updating it.

## Q&A log
### Round 1 (answered 2026-10-29)
- Q1 header wording: Section + Q#.
- Q2 fit: 56px + 56px. Adjusted at build time, see Summary.
- Q3 scope: everywhere (one shared component, QuestionPicker.tsx).
- Q4 sorting: none.

## Open flags (pending input)
- Main's COL.sectionQ was 104, not the 76 in the handoff. Table min width grows 644 -> 728 at the old stem min.
- Checked: tsc clean, 21 QuestionPicker tests pass, no overflow at 757px container, headers unclipped.
- Worktree ai-os-projects/lsatu-picker-section-q, branch claude/picker-section-q-columns. node_modules there was installed with --legacy-peer-deps because main's package-lock is out of sync.
