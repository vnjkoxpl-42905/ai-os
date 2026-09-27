# Teacher command center: Brainstorm / Discovery Notes
Date: 2026-09-27 · Goal: Define a distinct, functional teacher Home for Joshua that brings together student progress, requests, work, messages, schedule, and Stripe activity.
Status: in progress
Context sources: `brainstorms/2026-09-27-stripe-admin-home.md`; `brainstorms/2026-09-23-classroom-home-PLAN.md`; live Teacher Workspace audit from 2026-09-27; six user-supplied dashboard reference images.

## Summary / key decisions
- User-confirmed in the request: the teacher/admin Home should be distinct from the student Home; it should show student performance and provide access to individual analytics, new signup or teacher requests, tasks students need to do, messages, and payments in one command center.
- User-confirmed earlier: show all new Stripe activity and searchable history for roughly the prior three months. Package payments require a one-click teacher grant; unmatched payers go to review; only session/package payments can create platform access.
- User-confirmed in Round 1: lead with items needing Joshua's attention, grouped into distinct queues. Also show upcoming sessions and payments. Recent test results should be brief on Home. Clicking any student should open a full view of their work, performance data, and questions attempted in homework.
- User-confirmed in Round 1: the dashboard should include homework to do, be utility oriented, and remain visually easy to scan. Use the best ideas across the six references and other suitable patterns, rather than copying a single reference.
- User-confirmed in Round 2: do not make tutoring requests, student homework review, missed homework, or generic session follow-ups into Home queues. Focus the queue on Joshua's tasks: unread student messages, paid packages awaiting a grant, student access awaiting a grant, and work Joshua needs to assign after a session.
- User-confirmed in Round 2: calendar sessions should drive a task to assign work after teaching. The assignment varies by student; Joshua wants a workflow that helps determine what to assign from the session context or notes. This workflow is still to be designed.
- User-confirmed in Round 2: upcoming sessions should link to a useful prep view. Student message alerts should clear on opening the message or notifications, but the precise read behavior needs one clarification.
- User-confirmed in Round 2: access grants need a quick action for tier 1, 2, or 3, plus a path to adjust individual features. The Home queue should make students awaiting a grant obvious and connect to the existing Teacher Workspace access controls.
- User-confirmed in Round 3: show every event from Joshua's Google Calendar in the teacher dashboard, including sessions and consultations, with upcoming events visible and clickable through to Calendar. After a completed tutoring session, show an assignment-or-notes task. The task stays until Joshua explicitly marks it handled; it must not disappear automatically when an assignment is saved.
- User-confirmed in Round 3: importing transcripts into LSAT U is not necessary for this dashboard. Joshua says Friday Calendar events have notes/transcripts attached and asked for a read-only check. Calendar events are the source for upcoming schedule visibility.
- Tentative: a completed session could show its transcript or a link to it. Joshua expects the Google Calendar event may have an attached note/transcript. Code inspection on 2026-09-27 found a different current path: Gemini Notes email/Doc ingestion stores transcripts with sessions, while Calendar title/time help with matching. No automatic extraction from Calendar event notes was found. This is code evidence, not live verification.
- Verified earlier on 2026-09-27: `/teacher/today` has a Payments panel with 37 charges from the last 90 days and a manual Stripe sync. `/classroom` still shows the student-style Home to the signed-in teacher. These observations do not prove a full payment reconciliation or immediate arrival of every event.
- Visual references: image 2 offers the clearest light command-center information hierarchy; image 3 suggests a compact schedule and task layout; image 6 suggests an approachable left-rail and progress cards. Images 1, 4, and 5 contribute atmosphere or chart styling, but their ornamental data should not dictate the teacher's metrics. This is an interpretation, not Joshua's selected direction.

## Code fact check (2026-09-27, read-only)
- `/teacher/today` already renders signup, payment, calendar, and task areas. Its calendar query is roughly a 24-hour window and includes general Google events, so it does not yet provide a reliable upcoming student-session preview (`src/pages/teacher/shell/DeskTodaySurface.tsx`, `src/pages/teacher/desk/scheduleEvents.ts`).
- The active student dossier has overview, work, notes, messages, and schedule routes, but no dedicated analytics route. Its work view does not expose individual homework questions and answers even though assignment records can include question ids (`src/App.tsx`, `src/pages/teacher/students/DossierWork.tsx`, `src/components/hub/HubAssignments.tsx`).
- Session transcripts are ingested through Gemini Notes email/Doc workflows with manual scan/match steps. The dossier Notes area lists stored sessions and transcripts. Calendar metadata supports matching; there is no code path found that automatically imports a transcript from an event note or creates a post-session assignment task (`src/pages/teacher/TeacherSessionIngest.tsx`, `supabase/functions/scan-session-notes/index.ts`, `src/pages/teacher/students/DossierNotes.tsx`).
- These are code findings from `projects/lsatu-stripe`, not confirmation of live behavior. Claude's uncommitted `supabase/functions/mcp/index.ts` was not edited.

## Q&A log

### Round 1
#### Q1 - First thing you see
- Asked: whether action items, today's schedule, or student progress should lead.
- Recommended: action queue first, then sessions, progress, and recent activity.
- Captured: “Yeah, I need your attention.” Joshua wants queues for different student-related matters, with upcoming sessions and payments visible.
- Flags: exact queue categories and priority rules -> Joshua.

#### Q2 - Student work
- Asked: whether student assignments, Joshua's follow-ups, or both belong on Home.
- Recommended: separate student obligations from teacher follow-ups.
- Captured: Joshua wants “homework to do” on the dashboard, but did not distinguish student outstanding homework from his own follow-up work.
- Flags: precise meaning of “homework to do” and actions from the queue -> Joshua.

#### Q3 - Performance at a glance
- Asked: which performance changes and level of detail belong on Home.
- Recommended: brief attention list with reasons; detailed analytics on student page.
- Captured: recent test results should be “very brief.” Clicking any student should reveal all work and data, including questions attempted in homework and how the student is performing.
- Tentative: student detail could include session transcripts, pending verification of source and desired placement.
- Flags: whether to show student risk signals or simply latest activity on Home -> Joshua.

#### Q4 - New activity
- Asked: which events persist as actionable alerts versus appear as routine feed activity.
- Recommended: actionable requests, unread messages, payment exceptions, and work requiring response in a queue; routine completions and payments in activity.
- Captured: Joshua reiterated that payments and student messages belong on the dashboard. He mentioned a screenshot and a private student message, but no screenshot/message was attached in this reply. No alert persistence rules were confirmed.
- Flags: alert categories, resolution/read behavior, and any referenced screenshot -> Joshua.

#### Q5 - Visual direction
- Asked: which of six references should guide the page.
- Recommended: image 2 layout with image 6 warmth.
- Captured: take the best features from all six images and other suitable sources; prioritize utility and visual clarity. Joshua did not choose one reference.
- Flags: exact visual composition can be resolved during design review -> Joshua.

#### New topic raised - Completed session context
- Captured: Joshua wants a way to incorporate a transcript or completed-session record, potentially via a note attached to the Google Calendar event.
- Tentative: the Calendar note may be the source; this is not verified.
- Flags: inspect existing session/transcript data path -> Codex; decide where it appears and whether any automation is desired -> Joshua.

### Round 2
#### Q6 - Attention queues
- Asked: which events should wait for Joshua.
- Recommended: separate queues by type and put time-sensitive items first.
- Captured: unread messages; package payments requiring a grant; students requiring an access grant; Joshua's post-session work assignment. Joshua explicitly excluded tutoring requests, student homework needing review, missed homework, and generic session follow-ups.
- Flags: how to determine when a grant is actually pending and whether any other teacher tasks join this queue -> Joshua after code fact check.

#### Q7 - Homework
- Asked: student work owed, work needing Joshua's review, and work Joshua needs to assign.
- Recommended: include all three with distinct labels.
- Captured: only homework Joshua needs to assign matters on this dashboard. Student homework completion or missed homework is not a problem to surface here.
- Flags: post-session assignment task generation and completion rules -> Joshua.

#### Q8 - Messages
- Asked: whether opening a message clears the alert or whether it persists until reply/handling.
- Recommended: separate unread from needs-reply.
- Captured: opening a student's message should clear its alert. Joshua also said opening notifications might clear it; the exact trigger is ambiguous.
- Flags: whether viewing the notification list alone marks each item read, versus opening the specific message -> Joshua.

#### Q9 - Upcoming sessions
- Asked: whether a session should open latest homework, recent result, prior note, agenda, or all behind one click.
- Recommended: time, student, and short prep cue on Home; full context one click away.
- Captured: yes, upcoming sessions should provide this preparation help. No narrower field selection was given.
- Flags: inspect available source data -> Codex; choose concise Home fields after seeing a proposed design -> Joshua.

#### Q10 - Student attention
- Asked: flag meaningful changes versus show every student's latest activity.
- Recommended: flag only changes needing teaching action; full activity on student view.
- Captured: Joshua emphasized an organized place for his tasks. He did not choose a student-performance alert rule.
- Flags: whether any academic-performance item belongs in the Home action queue -> Joshua.

#### New topic raised - Tier and feature access
- Captured: Joshua wants a visible queue of students who need access, a quick grant for tier 1/2/3 or full access, and a more detailed feature-permission path, using or connecting to the existing Teacher Workspace controls.
- Flags: inspect existing tier/feature model and grant paths -> Codex; define safe quick-grant defaults and trigger -> Joshua.

### Round 3 (partial answers)
#### Q11 - When to create an assignment task
- Asked: task creation on tutoring-session end, transcript timing, and exclusion of consultations/cancellations.
- Recommended: create on completed tutoring session; attach transcript later; exclude consultations/cancellations.
- Captured: all Google Calendar events should be visible on Home, including sessions and consultations. After a completed session, a task should say Joshua needs to assign work or notes. Transcript ingestion is unnecessary.
- Flags: whether consultation and non-teaching events create any handled task, and how the system distinguishes tutoring from other Calendar events -> Joshua plus code check.

#### Q12 - Figuring out what to assign
- Asked: open a student-context workspace and optionally draft suggestions for Joshua to approve.
- Recommended: context and drafts; no automatic assignment.
- Captured: Joshua narrowed the Home requirement to a reminder/task to assign work or notes after the session. He did not request automated assignment suggestions in this answer.
- Flags: whether a separate assignment-planning workspace is in scope -> Joshua, can be deferred beyond the Home build.

#### Q13 - Finishing that task
- Asked: automatic completion on saved assignment, manual completion, or either.
- Recommended: automatic on assignment save plus “No assignment needed.”
- Captured: task should stay in the queue until Joshua presses a check mark or similar “handled” control. He may leave it there if unfinished. This supersedes the automatic-completion recommendation.
- Flags: whether “handled” is reversible and whether a note is optional -> Joshua.

#### Q15 - Transcript home
- Asked: LSAT U transcript storage versus Calendar event note as source.
- Recommended: LSAT U session record with Calendar link.
- Captured: transcript ingestion is not needed for this teacher dashboard. Joshua believes Friday Calendar events already have attached notes/transcripts and requested inspection. Calendar event should open in Calendar.
- Flags: inspect Friday Calendar events and avoid moving transcript data without a later request -> Codex.

#### New question - Calendar scope
- Captured: Joshua wants all Calendar events, future events visible on Home, click through to Calendar, and a synchronized schedule. He asked whether this is possible and for the best implementation route.
- Flags: inspect current Calendar sync, event fields, Friday examples, and upcoming schedule -> Codex.

## Open flags (pending input)
- Queue priority rules and any additional teacher tasks -> Joshua.
- Define which Calendar events trigger an assignment-or-notes task -> Joshua.
- Confirm whether manual handled is reversible and whether an optional note is needed -> Joshua.
- Clarify when exactly a message becomes read -> Joshua.
- Decide whether academic performance creates Home queue items; recent results stay brief -> Joshua.
- Verify Friday Calendar examples and current sync/upcoming-event behavior -> Codex.
- Transcript ingestion is out of scope for this dashboard per Joshua's Round 3 correction.
- Verify tier/feature access model and existing grant actions -> Codex.
- Define quick-grant defaults and triggers after the access-model check -> Joshua.
