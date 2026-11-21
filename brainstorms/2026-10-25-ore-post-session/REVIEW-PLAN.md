# Ore recap accuracy and section-first homework

## Authority and scope

Joshua asks Claude to independently review Ore's note quality and make follow-up homework come after the section with explicit days. Codex coordinates and is the authorized builder. Claude reviews read-only. Default CLI model/effort; no user-selected override. Maximum five plan-review rounds and two final inspections. No publication, unrelated messages, app deployment, deletions, duplicate assignments or changes to other students.

## Existing artifacts and source

- Full session source: students/ore/sessions/2026-10-23-argument-refresher-and-causal-scope/transcript.md. Read the actual transcript, not only its automatic summary.
- Current notes: brainstorms/2026-10-25-ore-post-session/recap.src.html, recap.html, primer-recall.md/html, argument-reference.md/html.
- Canonical record: students/ore/recaps/2026-10-23-recap.md, with preserved private source map/history.
- Actual homework proof: students/ore/assignments/2026-10-25-session-delivery.md and ore-session-work-2026-10-25/*.generated.json. All three currently unlock October26 and are due November1. The existing ids must survive rescheduling.
- Current writing rules: wiki/COPY-CORRECTIONS.md, wiki/teaching-voice.md, references/lsat-teaching-voice-standard.md. No student-facing word manual. Keep the approved existing layout and teaching scope.
- Current Core Connection published slug w1-02-the-core-connection: seven questions, mixed assumption-family tasks, difficulty1–3. Match the actual authored instruction_card and native question-stem tasks; do not label it a sufficient-assumption-only set. Inspect the app's current authored instructions where useful. The primer also covers the optional real Recall routine, which is separate from question practice.

## Required result

1. Review every visible explanation and hidden practice answer for logical accuracy, source grounding, useful teaching, clear ordinary language, false personal credit and unsupported promises. Resolve material findings before publication. Preserve specific successful student reasoning only when supported by the transcript.
2. Keep the transcript's Monday study start and Sunday rest. Treat the new detailed schedule below as Joshua's currently authorized operational instruction, not words he said in the original session.
3. Make the ordered work unambiguous in recap, primer, canonical Markdown and live assignments:

| Work | Available | Complete by | Meaning |
|---|---|---|---|
| PT104.S1 (26 LR questions, standard35-minute timer) | Monday2026-10-26 | Monday2026-10-26 end of day | First task; complete the section before using the same questions for recall so the diagnostic attempt is not pre-exposed by the recall activity |
| The Core Connection (seven guided questions) | Wednesday2026-10-28 | Thursday2026-10-29 end of day | Follow-up after the section; distinguish its mixed question tasks |
| Optional Read, Recall, Colour PT104.S1 | Friday2026-10-30 | Saturday2026-10-31 end of day | Optional later review of the completed section, not another test or substitute for the first attempt |

All dates are America/Toronto. Explicitly call a due date a deadline, distinguish availability from completion day, and avoid making optional work sound compulsory. Preserve Ore's standing Sunday rest. Prefer completing optional review FridayOctober30; SaturdayOctober31 is the final optional deadline. Sunday is not a homework day.

4. Classroom calendar availability does not automatically check section completion. There is no completion dependency. Direct guided-route readers and direct activity links (including the earlier Recall notification link) do not enforce the new availability dates, so do not promise a universal access lock. Recap and primer must explicitly say: do not open Read, Recall, Colour PT104 Section1 until the timed PT104.S1 section has been submitted. A moved Classroom date does not prevent that earlier link from exposing the section. Record this limitation in the live readback and final report. Student copy says complete the section before follow-ups; dates are the intended calendar order, not a completed prerequisite check.
5. Add a bounded reschedule-plan operation to the existing headless admin CLI, because its due command cannot update all required fields and uses host timezone. This operation uses the same authenticated Supabase REST update semantics as the app scheduling helper, editing existing records only. Exact field contract: section and activity assignment source rows have no date columns, so change their Classroom unlock_at/due_at only. Guided assignment source changes scheduled_for and unlock_at, plus its linked Classroom unlock_at/due_at; due exists only on Classroom. No new assignment rows, no reassignment, no notification functions and no progress writes. Existing app helper classroomItems.ts:updateClassroomItem provides the card semantics; guidedDrills.ts has no schedule helper. This small CLI extension fills that operational gap without app deployment.

Validate strict Gregorian Toronto dates with existing lsatu-work-plan-core.mjs boundary(), use exact student/owner/type/source ids, current status and expected old dates for all three targets before any write. Restrict source table edits to guided_drill_assignments. Use compare-and-swap conditions on old dates/status, request returned representations and require exactly one row. Save the preflight and result to a generated audit. Recheck before each write, record completed targets on partial failure, and attempt rollback only with a compare-and-swap against our own resulting values; never overwrite intervening progress. Read back all three cards plus the guided source and require unchanged identities, status/progress/question configuration. Stop and report any unresolved partial state; never retry creation or notifications. Update current plan JSON dates so verify_existing agrees with live state; historical generated receipts and private initial-delivery paragraphs remain unchanged. Append a dated Rescheduled2026-10-25 record with exactIDs, new dates, command and audit path. Change only the current public schedule, retaining previous public text privately as a prior version.
6. Original assignment notifications carried earlier dates and will not be rewritten by this no-notify date edit. Report that stale notification text explicitly in the readback and final response; live Classroom will show revised dates. Offer one corrected message or posting the revised recap for Joshua approval, without sending automatically.

7. New notes remain drafts. The earlier posting question received a homework question, not explicit posting approval. An independent reviewer approves quality, not delivery. No notes posted under this request.

## Verification

- Claude plan review through installed claudex-loop runner, host=codex, exact plan hash; record findings/dispositions. This review includes current actual note content, not just abstract plan prose.
- Verify underlying and Classroom unlock/due fields for all three existing live assignments after scheduling changes. Check exact ids and saved statuses, local dates and no new copies/notifications.
- Build notes with installed builder; it validates wording before replacing output. Preserve private history and sync current student-facing Markdown, including hidden answers.
- Headless Edge/Playwright desktop1200 and phone390 for each of the three pages, no horizontal overflow/page errors/banned visible or title wording. Exercise all three native answer reveals using click, Enter and Space; inspect the schedule table at both widths.
- Student-record validator: python system/scripts/check-student-records.py.
- Final fresh Claude inspection after implementation with preserved pre-build commit, bounded scope, proof and unreviewed unrelated-state limits explicit. No claims that static review proves student reading, email receipt, learning mastery, or live signed-in browser acceptance.

## Resolved source facts and review instructions

Ore Sunday rest is standing, not merely October25. All optional deadlines in the final plan are SaturdayOctober31. Source helper research is complete: classroomItems.ts updateClassroomItem edits card date fields only; guidedDrills.ts has no schedule editor, but its source schema has scheduled_for/unlock_at. Supabase ownership/admin policies allow the authenticated existing-row schedule updates described above. This is an authorized edit to existing records, not raw insertion/recreation of assignment rows.

Add Necessary Assumption, Sufficient Assumption, Principle Strengthen and Evaluate task boundaries to the reference as applicable to the actual published drill. Both assumption tasks concern the premise-to-conclusion support, with different tests: sufficient must be enough; necessary must be required. The authored card gives shared guidance, not permission to conflate the two. Strengthen adds support, Weaken undermines support without necessarily disproving the conclusion; Flaw names an actual defect. Preserve these logical limits rather than blindly requiring a weakener to prove a false conclusion. Earlier Read, Recall, Colour activities remain available but are not part of this week's ordered work; do not call them required unfinished sections. Read its authored instruction_card from references/lsatu-guided-drill-catalog.json or the sibling app src/data/guidedDrillsLocalSeed.ts. Questions in this drill are normally generated when opened. If seven saved question ids already exist, verify native stems; if not, record that limitation and do not start the student's drill or pre-expose questions merely for review. Use the exact published question-type pool and instruction card to describe the tasks accurately. Read the three complete current note sources/HTML and current canonical public text. If the full actual transcript cannot be read, state that coverage limit, do not imply it was.

Independent review can approve this concrete safe-edit plan before implementation; final inspection must inspect actual code, source/HTML, canonical sync and generated live date readback. Reviewer cannot operate live APIs; host independently runs proof commands.
