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
- User-confirmed in Round 4: use one Google Calendar, specifically Joshua's primary calendar; show its events. Do not create a backlog of task rows for historical sessions at launch. For an existing student's completed session, surface homework and notes to handle. For a consultation, surface a follow-up or check-in task, with exact wording/timing still unclear.
- User-confirmed in Round 4: add a second, manually editable to-do area where Joshua can add items and cross them off. He also wants appropriate automatic tasks, such as an enrollment action after a package payment, and a student-oriented task/checklist view with progress or blocker tracking. The meaning of “course through the district checklist” is unclear and not treated as a confirmed feature name.
- User-confirmed after Round 4: a quick manual to-do list must appear directly on the teacher Home/dashboard, with a link to a full, more expansive Tasks page in the platform.
- User-confirmed in Round 5: Joshua accepted the recommendations for Q21-Q25. The Home should show separate “Needs your attention” and “My list” areas; consultations get one follow-up task after ending; task progress counts Joshua's tasks per student and blockers are manual; manually added tasks stay private to Joshua; a paid package creates an “Enroll and grant passes” item for Joshua instead of automatic grant. The unclear checklist phrase remains unresolved despite this acceptance.
- New idea in Round 5, corrected by Joshua in Round 6: a prominent shortcut to generate a link for an individual student with a custom number of session credits such as five. This is **not a payment request**. The mechanism of redemption and credit grant is still open.
- Tentative: a completed session could show its transcript or a link to it. Joshua expects the Google Calendar event may have an attached note/transcript. Code inspection on 2026-09-27 found a different current path: Gemini Notes email/Doc ingestion stores transcripts with sessions, while Calendar title/time help with matching. No automatic extraction from Calendar event notes was found. This is code evidence, not live verification.
- Verified earlier on 2026-09-27: `/teacher/today` has a Payments panel with 37 charges from the last 90 days and a manual Stripe sync. `/classroom` still shows the student-style Home to the signed-in teacher. These observations do not prove a full payment reconciliation or immediate arrival of every event.
- Visual references: image 2 offers the clearest light command-center information hierarchy; image 3 suggests a compact schedule and task layout; image 6 suggests an approachable left-rail and progress cards. Images 1, 4, and 5 contribute atmosphere or chart styling, but their ornamental data should not dictate the teacher's metrics. This is an interpretation, not Joshua's selected direction.

## Code fact check (2026-09-27, read-only)
- `/teacher/today` already renders signup, payment, calendar, and task areas. Its calendar query is roughly a 24-hour window and includes general Google events, so it does not yet provide a reliable upcoming student-session preview (`src/pages/teacher/shell/DeskTodaySurface.tsx`, `src/pages/teacher/desk/scheduleEvents.ts`).
- The active student dossier has overview, work, notes, messages, and schedule routes, but no dedicated analytics route. Its work view does not expose individual homework questions and answers even though assignment records can include question ids (`src/App.tsx`, `src/pages/teacher/students/DossierWork.tsx`, `src/components/hub/HubAssignments.tsx`).
- Session transcripts are ingested through Gemini Notes email/Doc workflows with manual scan/match steps. The dossier Notes area lists stored sessions and transcripts. Calendar metadata supports matching; there is no code path found that automatically imports a transcript from an event note or creates a post-session assignment task (`src/pages/teacher/TeacherSessionIngest.tsx`, `supabase/functions/scan-session-notes/index.ts`, `src/pages/teacher/students/DossierNotes.tsx`).
- These are code findings from `projects/lsatu-stripe`, not confirmation of live behavior. Claude's uncommitted `supabase/functions/mcp/index.ts` was not edited.
- Tier access code: null `access_tier` on a non-admin, non-archived account defines the current signup queue. Tier 1 enables all 12 feature switches; Tier 3 enables Classroom, Messages, and Schedule (assigned work remains visible); Tier 2 preserves customized switches. The active dossier has per-feature toggles. Payment package pass grants use a separate `grant_state='awaiting'` and must remain a distinct queue (`src/lib/adminUsers.ts`, `src/components/teacher/SignupQueue.tsx`, `src/pages/teacher/students/DossierOverview.tsx`, `src/components/teacher/PaymentsPanel.tsx`). Code finding only.

## Live Calendar fact check (2026-09-27, read-only)
- Google Calendar CLI on Joshua's primary calendar returned three confirmed tutoring sessions on Friday 2026-09-25. All three have one attached Google Doc titled “Notes by Gemini.” This confirms Joshua's observation that Friday event records have a notes attachment. The event descriptions themselves are booking metadata, not the transcript text.
- A primary-calendar query for 2026-09-27 through 2026-10-05 returned the first upcoming tutoring session on 2026-09-28 at 15:20 Eastern and additional sessions later that week. The 2026-10-02 primary-calendar query returned no events at inspection time. The CLI also lists several secondary calendars; those have not been checked for upcoming events, so “all my calendar events” needs an explicit calendar-set decision or a cross-calendar aggregation.
- These are live Calendar observations, not evidence that LSAT U currently displays or syncs all those events.

## Calendar implementation finding (2026-09-27, code only)
- `gcal-sync-pull` syncs one configured calendar (default `primary`) into `schedule_events`, from 14 days behind through 90 days ahead on a full pull, then incrementally. It stores title, description, time, status, Calendar link, and related fields, but drops attachments. Friday's Gemini Notes attachments therefore exist in Google Calendar but are not mirrored into LSAT U (`supabase/functions/gcal-sync-pull/index.ts`, `supabase/functions/_shared/googleCalendar.ts`).
- Teacher Today triggers a Calendar pull on mount and every 120 seconds while visible; its event list refetches every 60 seconds. A production cron is mentioned in migration comments, but its actual active status was not verified. The Today query is limited to roughly 24 hours and the surface narrows further to the current day, which explains why the 2026-09-28 upcoming session is not shown on Sunday 2026-09-27 (`src/pages/teacher/desk/scheduleEvents.ts`, `src/pages/teacher/shell/DeskTodaySurface.tsx`).
- Best proposed path, subject to Joshua's remaining decisions: show a longer upcoming agenda from the already synced schedule; use each event's stored Google Calendar link to open the event and its attached note there; create a per-session, manually handled assignment-or-notes task after the event ends. Keep upcoming events and outstanding tasks distinct. No transcript ingestion is required for this scope.
- An event's scheduled end is not proof the lesson occurred. The follow-up should be worded as a review/assignment reminder, with a way to dismiss if no action is needed.

## Link generation implementation finding (2026-09-27, code only)
- The active teacher UI has no Stripe payment-link generator for a named student and custom session quantity. Existing 5- and 10-hour package links are fixed offers shown to students. An older booking-pass creator can make a private 1/5/10/custom-session pass immediately, without a Stripe charge, and its former route now redirects; it must not be presented as a paid-link action (`src/pages/teacher/BookingPasses.tsx`, `src/App.tsx`, `src/components/booking/BookingOfferHub.tsx`).
- Current package recognition relies on a registered Stripe Payment Link ID, validated paid amount/currency, and email matching. A paid recognized package can reach `grant_state=awaiting`; teacher grants passes with one click. A new custom student-specific Checkout flow would need its own verified mapping from local quote/student to Stripe Checkout Session and ledger, then the existing teacher grant pattern. It cannot safely assume that any custom Stripe link automatically creates credits (`supabase/functions/booking-commerce-webhook/index.ts`, `supabase/functions/_shared/stripeLedger.ts`, `src/components/teacher/PaymentsPanel.tsx`).
- Superseded recommendation (Round 6 correction): a “Create payment request” action using Stripe Checkout was proposed before Joshua clarified that his requested link is **not for payment**. Do not build that proposal for this shortcut. Stripe's Checkout docs were consulted for that discarded branch: https://docs.stripe.com/api/checkout/sessions/create .

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

### Round 4
#### Q17 - Which calendars
- Asked: primary calendar versus all visible calendars.
- Recommended: primary calendar initially.
- Captured: “Stick with my Google Calendar. Just stick with one calendar.” Use the primary calendar already connected to LSAT U.

#### Q18 - Which events create a task
- Asked: tutoring sessions only versus consultations and other events.
- Recommended: tutoring sessions create work/notes tasks; other events visible without task.
- Captured: sessions for existing students should create homework-and-notes work. Consultations should create a follow-up or check-in task. Joshua's phrase “And three consultations, check-in” needs clarification before defining timing or a sequence.
- Flags: exact consultation action/timing and detection of consultation versus existing student -> Joshua and implementation audit.

#### Q19 - Existing sessions
- Asked: create a backlog from sessions before launch or start after launch.
- Recommended: start after launch.
- Captured: “No, it shouldn't fill sessions.” No historical session-task flood at launch.

#### Q20 - Marking handled
- Asked: move checked tasks into searchable Handled history with reopen.
- Recommended: yes, with history and reopen.
- Captured: “As long as I clear it, it should be…” Joshua wants a clear action that removes a handled task from the active list. He did not explicitly confirm searchable handled history or reopening.
- Flags: desired handled history and reopen behavior -> Joshua, can be resolved with a mockup.

#### New topic - Two to-do areas and student task tracking
- Captured: a second to-do list supports manual add and crossing off. Automatic items may include enrollment after package payment. Joshua wants quick visual task widgets that open a fuller page, with tasks grouped by student or task and a progress/blocker measure such as percentage or count completed.
- Tentative: there may be a course or district checklist; dictation was unclear, so no product definition is assumed.
- Flags: task-list ownership and separation, package enrollment exact action, student versus teacher task visibility, progress denominator, and meaning of the named checklist -> Joshua.

### Round 5
#### Q21 - Two task areas
- Asked: separate auto-generated Needs your attention and manually editable My list on Home, each linking to full Tasks page.
- Recommended: yes, with student/type filters in full page.
- Captured: Joshua explicitly wants a quick to-do list on Home and a link to an expansive platform page; he then accepted the recommendation for all Q21-Q25.

#### Q22 - Consultations
- Asked: whether consultations create a follow-up when they end, and what “three consultations” meant.
- Recommended: one follow-up at consultation end, manual handled.
- Captured: Joshua accepted the recommendation. The phrase “three consultations” remains unparsed and is not treated as a three-day reminder.

#### Q23 - Student task tracker
- Asked: progress count for Joshua's tasks per student and manually set blocked state.
- Recommended: yes.
- Captured: accepted.

#### Q24 - Student visibility
- Asked: manually added student-linked item private to Joshua versus visible to student.
- Recommended: private; student assignment separate.
- Captured: accepted.

#### Q25 - Package payment
- Asked: paid package creates “Enroll and grant passes” for Joshua rather than automatically granting.
- Recommended: yes, preserving prior one-click teacher grant decision.
- Captured: accepted.

#### New idea - Quick link generator
- Captured: Joshua wants an easy shortcut to create an individual-student link for a chosen session quantity, such as five, and possibly add a credit when the link is used. He asked for a judgment on whether this is a good feature.
- Superseded by Round 6: the link is not for requesting payment.
- Flags: inspect existing booking-pass flow -> Codex; determine redemption/grant behavior and why a link is needed versus direct admin grant -> Joshua.

### Round 6 (correction)
#### Q26-Q29 - Link type
- Asked about paid Checkout link, price, payment follow-up, and copy/send behavior.
- Captured: “not requesting payment.” Joshua corrected the premise. Treat this as a credit/access link with no charge; do not infer Stripe Checkout, a price, or an enrollment/payment task from this shortcut.
- Flags: does opening/redeeming the link create credits, or is it a shortcut to an admin grant screen; is it single use and bound to one student; should generated links be copied only -> Joshua.

## Open flags (pending input)
- Queue priority rules and any additional teacher tasks -> Joshua.
- Primary Calendar selected. Define how to distinguish tutoring sessions and consultations, plus exact consultation follow-up timing -> Joshua and Codex.
- Confirm whether manual handled is reversible and whether an optional note is needed -> Joshua.
- Clarify when exactly a message becomes read -> Joshua.
- Decide whether academic performance creates Home queue items; recent results stay brief -> Joshua.
- LSAT U Calendar sync/upcoming behavior checked in code; Joshua confirmed one primary calendar in Round 4.
- Transcript ingestion is out of scope for this dashboard per Joshua's Round 3 correction.
- Tier/feature access model and existing grant actions checked in code; live grant behavior untested.
- Define quick-grant defaults and triggers after the access-model check -> Joshua.
- Two Home task areas, full Tasks page, private manual tasks, student grouping/progress, and manual blockers confirmed by Joshua in Round 5. Details of task creation and layout remain for design.
- Clarify the “course through the district checklist” phrase -> Joshua.
- Existing booking-pass behavior checked in code. Joshua clarified the new shortcut is not a payment request; define its link/redemption mechanics and student binding -> Joshua.
