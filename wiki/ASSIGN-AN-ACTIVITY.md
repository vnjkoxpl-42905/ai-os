# Assign an Activity — the runbook

The repeatable path for putting an LSAT U Activity into a student's hands.
Written 2026-09-07 after walking it live on lsatprep.study.

Joshua says **"assign &lt;activity&gt; to &lt;student&gt;"** and this is what happens,
end to end, with no further questions in the normal case.

Companion: [[STUDENT-PLATFORM-IDENTITY-MAP]] — which platform account is which
student. Read it before ticking a name.

## Standing authorization

Joshua granted this on 2026-09-07: assigning an Activity to a **named student**
is a **go** — do it, then report. Do not stop to ask permission first.

This is a deliberate exception to the global "draft, never send" rule, which
still holds for email, posts, and messages. It exists because assignment is the
core loop of the tutoring business and confirming each one made it useless.

**Still confirm first when:**

- assigning to **3 or more students at once** (each one emails a real person)
- the name is **ambiguous** — most importantly **Steven Morris vs "Stevie"**,
  two accounts that may be one person
- the student is on the unresolved list: **Thaniuska Vivas** (no account),
  **Amanda** (no account found)
- Joshua names a student who is **not in the identity map at all**

## The path

The Activity Centre lives at `/activities` — Classroom sidebar → **Study** →
**Activities**. Joshua's account is admin, so each card in **The library** carries
its own assign button.

1. Navigate to `https://lsatprep.study/activities`
2. `find` the button **"Assign &lt;Activity name&gt;"** (one per card, exact title)
3. Click it — a dialog opens, titled **"Assign: &lt;Activity name&gt;"**
4. Optional: fill **"Schedule for"** (a date input) if Joshua named a due date
5. `read_page` the dialog and locate the student's checkbox by display name
6. Click the checkbox — the footer button updates to **"Assign to 1 students"**
7. Click that button
8. Confirm the result, then report what was sent

The dialog is a portal — it renders **outside `<main>`**, so `get_page_text` will
not show it. Use `read_page` (with the dialog's `ref_id` to keep output small).

## The nine Activities

Assign by the exact card title:

| # | World | Activity | Grain |
|---|---|---|---|
| 01 | The Specimen Lab | Vocab Rehab | a word |
| 02 | The Signal Observatory | Spot the Relationship | a sentence |
| 03 | The Switchyard | Conditional Rephrase | a statement, translated |
| 04 | The Polarity Chamber | Negation Station | a statement, negated |
| 05 | The Argument Atelier | Find the Conclusion | an argument |
| 06 | The Debate Chamber | Rebuttal Rephrase | an argument, restated |
| 07 | The Press | Dumb it Down | a paragraph |
| 08 | The Loom | Spot the Callback | a passage |
| 09 | Out Loud | Read, Recall, Colour | a whole section, against the clock |

### Read, Recall, Colour

Assign **card 09** — the section-library door. The student then chooses any of
the 12 seeded sections, each 25 minutes:

PT1.S3 · PT21.S3 · PT101.S2 · PT102.S3 · PT103.S1 · PT104.S1 · PT105.S1 ·
PT105.S2 · PT106.S2 · PT112.S4 · PT134.S3 · PT140.S1

Every attempt is kept. Re-running a section saves a **new attempt**; it never
replaces the old one.

Only assign an individual `read-recall-colour-pt*-s*` slug when Joshua
deliberately wants her pinned to one section. The door is the default.

## What assigning actually does

`assignWork()` — `projects/lsatu/src/lib/assignWork.ts`:

1. **Snapshots** the Activity into `activity_assignments`. The snapshot is
   immutable once issued, so later content edits do not reach an assignment
   already sent.
2. **Writes a `classroom_items` row** — this is what makes it reachable at all.
3. **Notifies on four channels**: inbox message, bell, email, classroom item.

Notification failure never fails the assignment. A student can therefore hold an
assignment she was never told about — worth checking if she says she got nothing.

## Verifying it landed

After assigning, the sheet closes and a toast confirms. To verify properly:
open `/teacher` → the student's record, or have her Classroom show the item
under **Assigned work**.

If she says she cannot see it: check her **Activities access flag** first.
Flags resolve in `projects/lsatu/src/hooks/useUserPermissions.ts`. An assignment
lands regardless of flags, but the surface that displays it may be gated.

## Defects to mention when assigning Read, Recall, Colour

As of 2026-09-07 these are live and unfixed. Tell her, or fix them first:

- The door's heading reads **"Recall Rephrase Colour"** — a name that is not the
  product's — directly under a pill reading "Read, Recall, Colour".
  Hardcoded at `SectionLaunchFrame.tsx:281`; the aria-label at :314 repeats it;
  `SectionLibraryLaunch.test.tsx:54` asserts the wrong string, which is why the
  2,643-test suite stays green.
- Step 1's copy in production is the old *"Intake only…"* wording. The rewrite
  and its migration `20260906220000_simplify_recall_read_step.sql` are
  uncommitted and have never run.
- Attempt dates can render out of order — PT134.S3 shows Attempt 1 dated after
  Attempt 3. This is the `graded_at` vs `created_at` bug named in `PLAN.md`
  item 5.

## Verified working (2026-09-07)

- All 9 Activities seeded and listed
- All 12 RRC sections seeded and runnable
- `attempt_no` **is** applied in production — multi-attempt history renders
- 33 accounts in the picker; 20 map to real students

Related: [[STUDENT-PLATFORM-IDENTITY-MAP]] · [[tasks]] · [[hot]]
