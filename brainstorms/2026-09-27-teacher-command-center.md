# Teacher command center: Brainstorm / Discovery Notes
Date: 2026-09-27 · Goal: Define a distinct, functional teacher Home for Joshua that brings together student progress, requests, work, messages, schedule, and Stripe activity.
Status: in progress
Context sources: `brainstorms/2026-09-27-stripe-admin-home.md`; `brainstorms/2026-09-23-classroom-home-PLAN.md`; live Teacher Workspace audit from 2026-09-27; six user-supplied dashboard reference images.

## Summary / key decisions
- User-confirmed in the request: the teacher/admin Home should be distinct from the student Home; it should show student performance and provide access to individual analytics, new signup or teacher requests, tasks students need to do, messages, and payments in one command center.
- User-confirmed earlier: show all new Stripe activity and searchable history for roughly the prior three months. Package payments require a one-click teacher grant; unmatched payers go to review; only session/package payments can create platform access.
- User-confirmed in Round 1: lead with items needing Joshua's attention, grouped into distinct queues. Also show upcoming sessions and payments. Recent test results should be brief on Home. Clicking any student should open a full view of their work, performance data, and questions attempted in homework.
- User-confirmed in Round 1: the dashboard should include homework to do, be utility oriented, and remain visually easy to scan. Use the best ideas across the six references and other suitable patterns, rather than copying a single reference.
- Tentative: a completed session could show its transcript or a link to it. Joshua expects the Google Calendar event may have an attached note/transcript; the actual storage and linking workflow need verification.
- Verified earlier on 2026-09-27: `/teacher/today` has a Payments panel with 37 charges from the last 90 days and a manual Stripe sync. `/classroom` still shows the student-style Home to the signed-in teacher. These observations do not prove a full payment reconciliation or immediate arrival of every event.
- Visual references: image 2 offers the clearest light command-center information hierarchy; image 3 suggests a compact schedule and task layout; image 6 suggests an approachable left-rail and progress cards. Images 1, 4, and 5 contribute atmosphere or chart styling, but their ornamental data should not dictate the teacher's metrics. This is an interpretation, not Joshua's selected direction.

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

## Open flags (pending input)
- Queue categories and priority rules -> Joshua.
- Distinguish student outstanding homework from Joshua's own follow-ups -> Joshua.
- Decide which notifications persist and what action resolves each -> Joshua.
- Decide which student performance signals deserve a Home alert; recent test results stay brief -> Joshua.
- Verify Calendar/session/transcript data path -> Codex.
- Decide transcript placement and automation after the data-path check -> Joshua.
