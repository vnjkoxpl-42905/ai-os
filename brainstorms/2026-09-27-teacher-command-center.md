# Teacher command center: Brainstorm / Discovery Notes
Date: 2026-09-27 · Goal: Define a distinct, functional teacher Home for Joshua that brings together student progress, requests, work, messages, schedule, and Stripe activity.
Status: awaiting final shared-understanding confirmation before design or implementation
Context sources: `brainstorms/2026-09-27-stripe-admin-home.md`; `brainstorms/2026-09-23-classroom-home-PLAN.md`; live Teacher Workspace audit from 2026-09-27; six user-supplied dashboard reference images.

## Summary / key decisions
- **Teacher Home:** Distinct from the student Home, led by clear action queues and a useful upcoming agenda. Joshua wants a visually easy, utility-first command center using the strongest ideas from all six reference images, without copying one.
- **Needs your attention:** Unread student messages, paid packages awaiting teacher enrollment/pass grant, new accounts awaiting access-tier choice, and post-event teaching tasks. No tutoring-request queue, student homework review queue, missed-homework queue, or routine test-result task.
- **Calendar:** Use only Joshua's primary Google Calendar; show every upcoming event and open its Google Calendar event. A clearly identified tutoring session produces “Assign work or add notes” after it ends; a consultation produces one follow-up task. Ambiguous events remain visible and can be manually labelled. No historical task flood at launch. Importing transcripts is outside this dashboard scope; Friday 2026-09-25 events were verified to have attached “Notes by Gemini” Docs in Google Calendar.
- **Tasks:** Session/consultation tasks remain active until Joshua marks them handled. Handled tasks move to history and can be reopened. Separate Home area “My list” supports private manual tasks and check-off. A full Tasks page filters by student/type and shows per-student task progress counts and manually set blockers.
- **Messages:** Opening the specific student message clears its unread alert; opening the notification list alone does not.
- **Payments:** Show new Stripe activity and searchable roughly three-month history on teacher Home. A recognized paid package creates an “Enroll and grant passes” task; unmatched payer needs review. Only session/package payments can drive access actions, and a package pass grant remains Joshua's one-click decision.
- **Student access:** A new non-admin account without a tier needs a grant decision. Quick controls are Tier 1 full, Tier 3 basic, and Customize for Tier 2. Individual feature switches remain available.
- **Students and analytics:** Show only brief recent test results on Home. Opening any student should show detailed performance and all work, including the individual questions attempted in homework. Upcoming session rows should link to useful student preparation context.
- **Quick booking-pass link:** This is not a payment request. Joshua selects a named student and session count; creating the private `/book/{slug}` link makes the sessions usable immediately without login. Adding sessions preserves the current balance (2 + 5 = 7). The link has status and revoke controls. Current code's pass replacement must be fixed before surfacing this top-up shortcut.
- **Excluded:** The “course through the district checklist” phrase was accidental dictation. There is no student redemption step and no transcript import requirement for this dashboard.
- **Observed state:** Live `/teacher/today` already had a searchable 90-day Payments panel with 37 charges on 2026-09-27; `/classroom` still showed the student-style Home to the signed-in teacher. This does not prove every Stripe event reconciles or the new dashboard behavior exists.
- **Visual interpretation for proposal:** Image 2 provides a clear hierarchy, image 3 a compact schedule, and image 6 warm task cards. Charts should have real teaching meaning and not become decoration. Joshua has not approved a specific mockup yet.

## Code fact check (2026-09-27, read-only)
- `/teacher/today` already renders signup, payment, calendar, and task areas. Its calendar query is roughly a 24-hour window and includes general Google events, so it does not yet provide a reliable upcoming student-session preview (`src/pages/teacher/shell/DeskTodaySurface.tsx`, `src/pages/teacher/desk/scheduleEvents.ts`).
- The active student dossier has overview, work, notes, messages, and schedule routes, but no dedicated analytics route. Its work view does not expose individual homework questions and answers even though assignment records can include question ids (`src/App.tsx`, `src/pages/teacher/students/DossierWork.tsx`, `src/components/hub/HubAssignments.tsx`).
- Session transcripts are ingested through Gemini Notes email/Doc workflows with manual scan/match steps. The dossier Notes area lists stored sessions and transcripts. Calendar metadata supports matching; there is no code path found that automatically imports a transcript from an event note or creates a post-session assignment task (`src/pages/teacher/TeacherSessionIngest.tsx`, `supabase/functions/scan-session-notes/index.ts`, `src/pages/teacher/students/DossierNotes.tsx`).
- These are code findings from `projects/lsatu-stripe`, not confirmation of live behavior. Claude's uncommitted `supabase/functions/mcp/index.ts` was not edited.
- Tier access code: null `access_tier` on a non-admin, non-archived account defines the current signup queue. Tier 1 enables all 12 feature switches; Tier 3 enables Classroom, Messages, and Schedule (assigned work remains visible); Tier 2 preserves customized switches. The active dossier has per-feature toggles. Payment package pass grants use a separate `grant_state='awaiting'` and must remain a distinct queue (`src/lib/adminUsers.ts`, `src/components/teacher/SignupQueue.tsx`, `src/pages/teacher/students/DossierOverview.tsx`, `src/components/teacher/PaymentsPanel.tsx`). Code finding only.

## Live Calendar fact check (2026-09-27, read-only)
- Google Calendar CLI on Joshua's primary calendar returned three confirmed tutoring sessions on Friday 2026-09-25. All three have one attached Google Doc titled “Notes by Gemini.” This confirms Joshua's observation that Friday event records have a notes attachment. The event descriptions themselves are booking metadata, not the transcript text.
- A primary-calendar query for 2026-09-27 through 2026-10-05 returned the first upcoming tutoring session on 2026-09-28 at 15:20 Eastern and additional sessions later that week. The 2026-10-02 primary-calendar query returned no events at inspection time. The CLI also lists several secondary calendars; Joshua later chose the primary calendar only (Round 4).
- These are live Calendar observations, not evidence that LSAT U currently displays or syncs all those events.
- A search of the primary calendar's 2026-09-01 to 2026-09-27 events returned 12 confirmed events with “Consultation” in the title and Cal.com details in the description. This gives a reliable-looking current pattern for consultation classification, but other/manual event naming has not been exhaustively checked. Tutoring examples on 2026-09-25 used “<student> session” titles and “Booked via LSAT U” descriptions. All events should remain visible even if their task type cannot be classified.

## Calendar implementation finding (2026-09-27, code only)
- `gcal-sync-pull` syncs one configured calendar (default `primary`) into `schedule_events`, from 14 days behind through 90 days ahead on a full pull, then incrementally. It stores title, description, time, status, Calendar link, and related fields, but drops attachments. Friday's Gemini Notes attachments therefore exist in Google Calendar but are not mirrored into LSAT U (`supabase/functions/gcal-sync-pull/index.ts`, `supabase/functions/_shared/googleCalendar.ts`).
- Teacher Today triggers a Calendar pull on mount and every 120 seconds while visible; its event list refetches every 60 seconds. A production cron is mentioned in migration comments, but its actual active status was not verified. The Today query is limited to roughly 24 hours and the surface narrows further to the current day, which explains why the 2026-09-28 upcoming session is not shown on Sunday 2026-09-27 (`src/pages/teacher/desk/scheduleEvents.ts`, `src/pages/teacher/shell/DeskTodaySurface.tsx`).
- Best proposed path, subject to Joshua's remaining decisions: show a longer upcoming agenda from the already synced schedule; use each event's stored Google Calendar link to open the event and its attached note there; create a per-session, manually handled assignment-or-notes task after the event ends. Keep upcoming events and outstanding tasks distinct. No transcript ingestion is required for this scope.
- An event's scheduled end is not proof the lesson occurred. The follow-up should be worded as a review/assignment reminder, with a way to dismiss if no action is needed.

## Link generation implementation finding (2026-09-27, code only)
- The active teacher UI has no Stripe payment-link generator for a named student and custom session quantity. Existing 5- and 10-hour package links are fixed offers shown to students. An older booking-pass creator can make a private 1/5/10/custom-session pass immediately, without a Stripe charge, and its former route now redirects; it must not be presented as a paid-link action (`src/pages/teacher/BookingPasses.tsx`, `src/App.tsx`, `src/components/booking/BookingOfferHub.tsx`).
- Current package recognition relies on a registered Stripe Payment Link ID, validated paid amount/currency, and email matching. A paid recognized package can reach `grant_state=awaiting`; teacher grants passes with one click. A new custom student-specific Checkout flow would need its own verified mapping from local quote/student to Stripe Checkout Session and ledger, then the existing teacher grant pattern. It cannot safely assume that any custom Stripe link automatically creates credits (`supabase/functions/booking-commerce-webhook/index.ts`, `supabase/functions/_shared/stripeLedger.ts`, `src/components/teacher/PaymentsPanel.tsx`).
- Superseded recommendation (Round 6 correction): a “Create payment request” action using Stripe Checkout was proposed before Joshua clarified that his requested link is **not for payment**. Do not build that proposal for this shortcut. Stripe's Checkout docs were consulted for that discarded branch: https://docs.stripe.com/api/checkout/sessions/create .
- The dormant `BookingPasses` screen already defaults to five credits, 70-minute sessions, and no expiry; it supports 1/5/10/custom credits up to 50 and accepts a name or email. Creating the pass calls `booking-pass-admin`, which immediately returns a private public `/book/{slug}` URL. Anyone holding the private URL can book without LSAT U sign-in. The screen's former route redirects to Students, so this creation control is not currently exposed there (`src/pages/teacher/BookingPasses.tsx`, `supabase/functions/booking-pass-admin/index.ts`, `src/pages/PublicBooking.tsx`).
- Critical behavior: when the provided email matches an existing student, the admin endpoint's `grant_booking_access` path revokes the prior active pass and creates a new one. A “five more sessions” top-up shortcut would therefore erase remaining credits unless the flow is changed to preserve/top up the existing balance. This must be resolved before surfacing the shortcut. Code finding, not live tested (`supabase/functions/booking-pass-admin/index.ts`).

## Proposed teacher Home composition (awaiting confirmation)
- Teacher account's Home opens the teacher command center, not the student `/classroom` content. Student Home remains student-specific. Reuse the existing Teacher Today feeds where appropriate.
- **Top:** date, concise greeting, student search, and quick actions for Add task, Create session link, and Assign work.
- **Primary row:** Needs your attention with distinct counts/queues for unread messages, package grants, access-tier grants, and post-session or consultation tasks. Each row opens its actual action. Group by type; within a group, overdue/due work precedes recent items.
- **Alongside:** upcoming agenda from the primary Google Calendar, initially the next seven days; all event types visible; event click opens Google Calendar. A recognized past teaching session or consultation creates its durable follow-up only from launch forward. Unknown event types can be manually labelled.
- **Next row:** My list quick add/check-off, linked to full Tasks page. Payments panel shows recent account activity and opens the searchable roughly 90-day history. A paid package creates a separate grant task; a free session link never appears as payment.
- **Student area:** compact recent test results and a searchable student list. Student detail needs real analytics, all work, and per-question homework evidence. Session rows link to student prep context when identity is known.
- **Full Tasks page:** combined view with source/type/student filters, handled history and reopen, private manual tasks, per-student progress counts, and manual blocker status.
- **Create session link:** named student, 1/5/10/custom count, adjustable duration and expiry, explicit additive top-up, then Copy private `/book/{slug}` URL. No payment or redemption step. Show status and revoke action. Fix current pass replacement before release.
- Visual proposal: clear light grid from reference image 2; compact schedule rhythm from image 3; warm task-card treatment from image 6. Use dark emphasis sparingly, with no ornamental analytics.

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

### Round 7 (correction)
#### Q30 - What using the link means
- Asked: whether the student redeems a single-use credit link or the link opens a teacher grant screen.
- Captured: “I don't know what you mean by redeem it, but they should be able to use it as soon as possible. And that link should be there. If I send them a link, they should be able to use it no problem.” No student redemption ceremony is wanted.
- Superseded recommendation: provide a signed-in `/booking` link. Existing code actually provides a public private `/book/{slug}` link, which fits Joshua's no-friction requirement better.
- Flags: confirm that this existing private booking-pass link is the intended shortcut; decide whether adding sessions to an existing student must preserve unused credits -> Joshua.

### Round 8
#### Q31 - Additional sessions
- Asked: if a student has 2 sessions left and Joshua creates a 5-session link, should the student have 7.
- Recommended: yes, preserve existing sessions.
- Captured: “yes to both.” The grant is additive, not replacement. This supersedes the current `grant_booking_access` replacement behavior for this shortcut.

#### Q32 - Private no-login link
- Asked: whether an easy private link that can be forwarded is acceptable, with status and revocation controls.
- Recommended: yes.
- Captured: “yes to both.” Private `/book/{slug}` remains usable without login; Joshua needs visibility into its status and an option to revoke it.

### Round 9
#### Q33 - Unclassified Calendar events
- Asked: leave uncertain events visible and let Joshua label them Session or Consultation; auto-create tasks only for clearly classified events.
- Recommended: yes.
- Captured: Joshua approved the recommendation.

#### Q34 - Quick access grants
- Asked: Tier 1 full, Tier 3 basic, and Customize for Tier 2.
- Recommended: yes; Tier 2 opens feature picker.
- Captured: approved.

#### Q35 - Message alerts
- Asked: specific message open clears its unread alert; opening notification list alone does not.
- Recommended: yes.
- Captured: approved.

#### Q36 - Test results
- Asked: brief Home result linking to full analytics, not a task to clear.
- Recommended: yes.
- Captured: approved.

#### Q37 - Handled tasks
- Asked: checked task leaves active queue but remains in Handled history with reopen.
- Recommended: yes.
- Captured: approved.

#### Checklist phrase
- Asked: meaning of “course through the district checklist.”
- Captured: Joshua said it was accidental dictation. No such checklist is part of this dashboard brief.

## Open flags (pending input)
- Final shared-understanding confirmation of the consolidated teacher dashboard brief -> Joshua.
- The current tier, pass, and Calendar findings are code-level. Live behavior of newly proposed flows is untested because no implementation has begun.
- Queue ordering and visual composition can be settled in the mockup if Joshua approves the brief. Proposed defaults: due/urgent work before recent activity; compact light layout with warm accents and limited charting.
