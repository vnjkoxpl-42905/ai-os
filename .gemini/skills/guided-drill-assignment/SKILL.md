---
name: guided-drill-assignment
description: Select and verify an LSAT U guided drill when Joshua asks for a drill recommendation or guided drill assignment. Transcript retrieval belongs to transcript-intake; transcript analysis alone does not trigger assignment. Inspection/recommendation are read-only; assign only when requested, through the current platform executor.
---

# Guided Drill Assignment

Use this skill to turn student performance context into a verified guided drill assignment in LSAT U.

Choose the mode from the request:

- **Inspect:** analyze the student evidence only; no assignment, notifications or new student run.
- **Recommend:** select and explain a drill, with available metadata/access evidence; stop before assignment.
- **Assign:** when Joshua has requested assignment, use the current `assign-lsatu-work` / `lsat-u-platform-actions` executor and its catalog, identity, duplicate, authorization and read-after-write contract. This skill supplies selection/verification knowledge, not a competing executor.

Opening a drill runner can create progress/run records; do that only within authorized QA/assignment scope. A read-only request uses existing evidence and reports untested launch status.

## Inputs

Expect one or more of:

- A student name or shorthand, such as `C`, `C. Alexander`, or another current student.
- A request to inspect a recent transcript, chat export, meeting note, student page, or platform record.
- A request to find an appropriate guided drill.
- A request to assign a drill and make sure the student is notified.

If the student identity is ambiguous and cannot be safely inferred from local context, ask one concise clarifying question before assigning anything.

## Required Context

For LSAT U vault work, follow the vault operating order before making a recommendation:

1. Read `wiki/hot.md`.
2. Read `../ai-os-projects/lsatu/README.md`.
3. Read `wiki/dashboard.md`.
4. Read the relevant student page under `students/`.
5. Read the student's `assignment-log.md` if it exists so you do not repeat assigned work unless Joshua explicitly asks for a repeat.
6. Read `wiki/guided-drill-verification-log.md` so already-verified drills are not re-QA'd unnecessarily.
7. Search all available transcripts, transcript downloads, chat exports, and meeting notes for that student.
8. Sort candidate transcript/context files by the actual meeting date, not file modification time, and use the most up-to-date transcript as the primary source of truth.

Prefer local sources first. Do not invent student weaknesses or assignment history. If an older transcript conflicts with a newer one, follow the newer transcript and mention the older file only as background.

Useful searches:

```bash
rg -n "student-name-or-shorthand|student full name|student email" wiki raw students projects
find students -path "*transcript*" -type f | rg -i "student-slug|student-name"
```

## Drill Selection

Choose the drill by matching the student's most recent need to the drill's pedagogical purpose.

Evaluate:

- Newest transcript evidence by meeting date: missed concepts, confusion, pacing, task avoidance, question type weakness, or reasoning pattern weakness.
- Student readiness: assign teach-first drills when the student needs instruction, not a cold test.
- Drill metadata: title, slug, week/module, question type, tags, pool size, question count, estimated time.
- Platform constraints: student must have classroom and drill access.
- Assignment history: avoid assigning a drill already present in the student's `assignment-log.md` unless Joshua explicitly wants a repeat or the log says it should be repeated.

When the best drill is not obvious, produce a short ranked recommendation before assigning:

```markdown
Recommended: <drill title>
Reason: <one sentence tied to transcript evidence>
Backup: <second drill title, only if meaningfully close>
Do not assign yet because: <only include if blocked>
```

If the user has already asked to assign and the best choice is clear, proceed without stopping.

## Repo Checks

Before using a drill, verify that it exists in the app data and is wired to the platform.

Common files to inspect:

- `data/guided-drills/_seed.json`
- `src/data/guidedDrillHtmlManifest.ts`
- `src/lib/guidedDrills.ts`
- `src/pages/Drill.tsx`
- `src/pages/teacher/desk/library/DeskLibraryGuidedDrillsSurface.tsx`
- `src/lib/classroomNotify.ts`
- `src/lib/assignmentEmail.ts`

Confirm:

- The drill slug and title exist.
- The drill has enough eligible questions for the configured count.
- The guided assignment flow creates `guided_drill_assignments`.
- The classroom item is created from the assignment source row.
- Completion writes `completed_at` and `status: completed`.
- Notification code attempts inbox, bell, and email where applicable.

Run targeted tests if the repo is available:

```bash
npm test -- --run src/lib/guidedDrillNavigation.test.ts src/lib/classroomItems.test.ts src/components/mainhub/TodayFocusPanel.test.ts
```

If tests cannot be run, say why and continue with browser verification.

## Browser Verification

Use the in-app browser when available. The usual admin surface is:

```text
https://lsatprep.study/teacher?ws=library&tab=guided-drills
```

Before doing full launch QA, check `wiki/guided-drill-verification-log.md`.

If the selected drill is already listed as `verified-working`:

1. Do not repeat full preview/start-runner verification.
2. Cite the existing verification log entry.
3. Continue with student profile/access checks and assignment flow.

If the selected drill is not yet verified, run this sequence:

Verification sequence:

1. Open the teacher guided drills library.
2. Search the exact drill title or slug.
3. Confirm the visible card shows the expected title, module/week, question count, and tags.
4. Open the preview.
5. Confirm the launch card renders with the expected title, estimated time, and question count.
6. Click `Start Drill`.
7. Confirm the real drill runner loads with question text, answer choices, controls, and the expected URL parameters or question ids.
8. Return to the guided drill library before assigning.

Do not call the drill "perfect" unless the above checks passed. Prefer "verified to launch and load the runner" over broader claims.

Existing noisy console warnings that do not block launch should be reported only if relevant.

After a new drill passes browser verification, add it to `wiki/guided-drill-verification-log.md` with date, slug, evidence, and `verified-working` status.

## Assignment Flow

This section applies only in assign mode. Resolve and read the current platform executor before a live mutation; defer to its approved UI/API transport and duplicate checks. The UI sequence below is a fallback reference when that executor permits it.

Use the executor's approved platform transport. Do not insert rows manually unless the task explicitly authorizes a backend repair.

Teacher UI sequence:

1. On the exact drill card, click `Assign`.
2. In the assign dialog, search/select the intended student only.
3. Scope checks to the dialog so sidebar or to-do rail text does not create false positives.
4. Confirm the dialog says exactly one selected student, unless the user requested multiple students.
5. Click the primary button, usually `Assign to 1 student`.
6. Wait for the success toast.

If there is any sign that the wrong student is selected, stop before clicking assign.

## Post-Assignment Verification

After assignment, verify live state rather than relying only on the toast.

Verify:

- Student identity and access flags.
- Guided drill assignment row.
- Classroom item row visible to the student.
- Unread bell notification row.
- Notification link points to the assignment route or classroom route.
- Email leg, if available through logs or returned notification result.

After verification, update the student's `assignment-log.md` with the drill, slug, reason, platform evidence, notification evidence, and current status. If the file does not exist, create it.

Expected tables/objects:

- `profiles`
- `guided_drills`
- `guided_drill_assignments`
- `classroom_items`
- `notifications`
- `email_send_log`, if accessible

Protect secrets:

- Do not print auth tokens.
- Do not print service-role keys.
- Do not expose full student email addresses unless the user explicitly needs them.
- Redact email recipients in final reports.

Example final verification fields:

```markdown
Assignment:
- student: <display name>
- drill: <title>
- assignment status: assigned
- classroom item: visible_to_student true
- bell notification: unread assignment notification exists
- email: verified via log / returned OK by platform / not independently verified
```

## Final Response

Keep the final response short and operational.

In inspect/recommend mode, report findings/recommendation and state `Not assigned`. In assign mode use this shape:

```markdown
Assigned <drill title> to <student>.

Verified:
- <drill launch/browser check>
- <assignment row/classroom visibility>
- <notification evidence>
- <tests, if run>

Email: <verified status or limitation>
```

If assignment was not completed, say exactly where it stopped and what is needed next.

Avoid overstating. "Clear in-app notification exists" is acceptable only after verifying a notification row or student-facing UI evidence.

## Example From Prior Workflow

Student: C. Alexander.

Selected drill: `Necessary Assumption - First Taste`, slug `w2-07-necessary-assumption-first-taste`.

Reasoning: transcript context indicated Necessary Assumption needed a teach-first, calibrated drill. The drill is W2.7, 10 questions, 60 minutes, with Necessary Assumption plus Comparison/Causation tags.

Verification performed:

- Opened guided drill library.
- Found the exact card.
- Opened preview.
- Started the drill.
- Confirmed the runner loaded with 10 question ids and real question content.
- Assigned to only C. Alexander through the dialog.
- Verified the assignment row, classroom item, and unread bell notification.

Use this as a pattern, not as a default assignment for every student.
