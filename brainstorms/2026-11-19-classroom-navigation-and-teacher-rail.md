# Classroom navigation and Teacher tools rail
Date 2026-11-19 · Goal is to agree on the follow-up pause, notifications, docked right rail, student conversations, and collapsible navigation.

## Summary / key decisions

- Joshua wants Follow-ups removed from Teacher Home temporarily and added to the to-do list for refinement.
- The supplied reference shows a top-right notifications control, a right panel beside the main content, chat controls in that panel, and icon-only left navigation.
- Start with Teacher Classroom only. The top-right bell includes all current alerts, including unread messages.
- New chat uses a student picker and the existing 1:1 Inbox conversation. Multiple students can be open as chat tabs.
- Leave Recent results where it is for this round.

- Keep the right rail available across Teacher Classroom routes and use a full-screen view with Back on phones.
- Keep chat tabs and unsent drafts when the rail closes. Clear them when the user closes the chat tab or signs out.
- For a student with no conversation, open a composer and create the 1:1 thread on the first send.

- Left navigation starts expanded, collapses to icons, and remembers the teacher's choice.
- Message and signup notifications open their matching rail view. Other alerts lead to their relevant page.
- The rail has three clearly labeled views. The third covers homework, notes, and history of assigned work.
- The active chat shows the student name and one Open student record link.

## Q&A log

### Round 1

- Q1, rollout scope. Teacher Classroom only.
- Q2, notification contents. All current alerts, including unread messages.
- Q3, conversation model. Pick a student, open their existing 1:1, and allow multiple open student tabs.
- Q4, Recent results. Leave it where it is for this round.

### Round 2

- Q5, route coverage. Keep the right rail available across Teacher Classroom pages.
- Q6, chat lifetime. Keep tabs and drafts until the chat tab closes or the teacher signs out.
- Q7, first message. Open a draft and create the 1:1 conversation on first send.
- Q8, mobile. Open full-screen with a clear Back button.

### Round 3

- Q9, navigation. Start expanded, collapse to icons on click, and remember the choice.
- Q10, notification destinations. Open matching chat or signup in the rail; route other alerts to their destination.
- Q11, rail organization. Three plainly labeled views. Joshua wants homework assignment, notes, and history of what was assigned in the third.
- Q12, chat context. Student name and one Open student record link.

### Round 4

- Q13, label. Student work.
- Q14, student context. Use the student in the active chat or student page, with a picker to switch.
- Q15, opening view. Remember the last view used, starting with Messages.

### Round 5

- Q16, assignment creation. Build and submit entirely inside the rail.
- Q17, notes. Joshua requested grill-with-docs to clarify which type of note is meant before deciding how to display or edit it.
- Q18, work default. Recent assignment history, newest first, with status.

### Round 6

- Q19, materials. Show Assigned notes and Session recaps. Also expose saved Google Meet transcripts as a distinct source.
- AI. Add a preconfigured AI chat entry point that can scan or find relevant information. Joshua asked to stop the interview here.
- Default to direct browsing and ordinary search across the selected student's assignments, assigned notes, session recaps, and available Meet transcripts.
- AI is off by default. A visible AI toggle enables a free-text question in the selected student's context. Toggling on prepares the interface; only submitting a question calls the AI. Turning it off restores ordinary search. Opening the rail, switching students, typing, and applying filters make no AI calls.
- AI answers should link to the exact records used and identify missing or inaccessible sources. Keep the answer in the teacher view until Joshua takes an explicit sharing action. Verify transcript text availability separately from whether a Drive link exists.
- Google Meet creates a transcript when transcription runs. The organizer's Drive stores it. Classroom already has a Sessions and transcripts surface. Actual teacher-account coverage, matching and source permissions need verification.

## Open flags (pending input)

- Implementation and release have not been approved as a complete design.
- Verify which Meet transcripts are already linked for actual sessions, and how the assistant reads the selected student's authorized sources.

### Round 7 · 2026-11-20

- Q20, release order. First deliver shared Teacher Classroom controls, collapsible navigation, Messages, Student access, and the temporary removal of Follow-ups. Then add Student work with assignment creation, browsing, and search. Add optional AI after verifying which records it can read and cite.
- Q21, student selection. An explicitly picked student stays selected as chats and student pages change. Show the selected student in the Student work header and offer Follow active student to resume automatic switching.
- Q22, refresh. Restore open chat tabs and per-student unsent drafts after a refresh in the same browser tab. Closing a chat tab clears its draft. Signing out clears all chat tabs and drafts.
- Q23, notification read state. Opening the bell marks the alerts shown there as read immediately. Opening an alert destination is optional. Keep bell read state separate from Inbox conversation read state and the Needs access queue.

### Round 8 · 2026-11-20

- Q24. Opening the bell clears unread status. Alerts stay visible and actionable in the list.
- Q25. Bell read state follows the teacher account across devices.
- Q26. A signup alert opens the student's row in Student access, under Needs access or All students according to the student's current status.
- Q27. Joshua chose LexPrep's New Chat tabs as the interaction reference. Assignment drafts tied to one recipient while moving between chats are a proposal for the next decision.

## Teacher rail design reference · 2026-11-20

Observed on [LexPrep Home](https://www.lexprep.ai/home). The plus control opened and selected a second New Chat tab in the right rail without navigating away from Home. Typing a test draft in that tab, switching away, and switching back restored the draft. The clock opened saved history. Choosing a saved chat opened it as a third tab alongside the two drafts. The active tab had a visible close control. The draft was cleared after testing. First-send, refresh, tab-close behavior, and phone layout were outside this browser check.

### Proposed instructions for the Claude Build spec

- In Messages, put the open conversations in a compact strip across the rail header. Use student names for tabs. Keep New chat and Inbox accessible when tabs overflow. Give the active tab a clear outline or tonal fill, a keyboard focus indicator, and an accessible close control. Show an unsent-draft indicator with a text equivalent.
- New chat opens a searchable student picker. Selecting a student focuses their open tab or opens their existing 1:1. For a first-time conversation, open a named draft and create the thread on first send. An Inbox entry or message alert uses the same open-or-focus behavior. One student gets one tab.
- Below the strip, show the current student's full name and Open student record. Let the thread scroll independently above a fixed composer. Switching tabs restores the student's draft and reading position. Keep focus and page scroll stable when the rail docks or a tab changes.
- Use LSAT U's near-white and soft charcoal surfaces, subtle edges and visible focus. Keep names legible when tabs overflow. Keep the main Classroom content usable at intermediate widths, and use the full-screen rail with Back on phones. Animate panel movement only and honor reduced motion.
- Proposed Student work behavior. Show the assignment recipient throughout the builder. Let the teacher switch to Messages and return to the assignment draft under its original student. Keep the builder in Student work and use the saved draft as the return point.
- Acceptance checks. Open two student tabs and switch between them with drafts. Open an already-tabbed student from Inbox and verify the same tab activates. Use a keyboard to navigate and close a tab. Close and reopen the rail, then refresh the same browser tab. Verify recipient identity when switching from an assignment to a different student's chat and back. Check long names, overflowing tabs, and a narrow viewport with the composer visible.

Saved design evidence: [LexPrep navigation and motion teardown](../research/2026-10-21-lexprep-motion-teardown.md) for independent scroll and stable state during transitions. [Classroom design principles](../design/principles.md) for tonal hierarchy, controlled depth, and visible focus.

## Q27 confirmed and next design choices · 2026-11-20

Q27 approved. Assignment drafts belong in Student work and stay tied to their original recipient while the teacher switches between student conversations. Returning to Student work restores the recipient and edits.

### Proposed refinements to validate before Claude Build

1. **Show what changed while you were away.** On each conversation tab use a dot for unread incoming messages and a pencil for an unsent draft, each with an accessible label. Allow both indicators on the same tab. In the thread, show a New messages divider at the first unread message when opening a conversation with unread activity. On an already-open thread, keep the current reading position when the teacher is reading older messages and offer Jump to latest.
2. **Keep controls in reach when chat tabs fill up.** Reserve space for New chat and Inbox. Put hidden open tabs in an overflow menu that shows full student names and state. Activating one brings it into view. On narrow screens use the same tab model and a full-screen rail with Back. Opening the mobile keyboard keeps the composer reachable.
3. **Give the teacher one way back to unfinished work.** While an assignment is in progress, show Resume assignment for [student] at the top of Student work. Recommend a single in-progress assignment for the first Student work release. Warn before discarding it and keep the draft intact on a failed submission. The final action names the recipient, for example Assign to Jordan.
4. **Protect drafts without adding routine friction.** Closing an empty chat tab is immediate. Closing a tab with unsent text prompts Keep open or Discard draft and close. A failed message send preserves the text and offers retry. Instructor acceptance case: send failure, switch students, return, and retry under the original recipient.
5. **Protect the working page.** Give the rail enough width for a readable conversation while preserving the page's usable content width. Move to the full-screen pattern before either column gets cramped. Validate the transition in a fixture with long student names, six open chats, a long conversation and a crowded Teacher page. Keep tab focus and both scroll positions stable on desktop.

### Build handoff route

Ask Matt routes this multi-session feature through design decisions, a narrowly scoped prototype when a decision needs a runnable answer, then a behavior spec and dependency-ordered slices. Prototype the shell, chat overflow and composer at desktop, intermediate and phone widths using synthetic data. Capture reviewed states and include the acceptance walkthrough in the spec. Hand the approved spec and prototype evidence to Claude Build. First slice is shell plus one real teacher-to-student conversation through the existing Inbox, followed by signup and bell integration, then Student work. Optional AI follows verified record access. The approved phase order remains the release sequence, and Claude Build is the implementation handoff.

### Q28 confirmed · 2026-11-20

Allow one in-progress assignment in the first Student work release. Opening a conversation, switching students, closing the rail, or navigating within Teacher Classroom keeps the original recipient and edits intact. If the teacher starts a different assignment, offer Resume current assignment or Discard and start new. A failed submission leaves the draft available for retry. The lifetime across refresh and sign-out is a separate pending decision.

### Q29 and Q30 confirmed · 2026-11-20

Restore the one assignment draft after refresh in the same browser tab. Clear it on successful assignment, explicit discard, or sign-out. Build a standalone [Teacher rail prototype](../design/prototypes/teacher-rail/index.html) with synthetic data before finalizing the Claude Build spec.

## LexPrep rail, measured signed in · 2026-11-20

Joshua's direction: emulate LexPrep's right chat rail as closely as possible (docked, toggle on top, + adds a chat tab), in LSAT U's look, and improve where it falls short.

- Three panes on one off-white canvas (rgb 250,249,245). Left nav and rail sit on the canvas with no border; only the page is a raised rounded card.
- Rail is a fixed 384 px. It does not overlay: the page container gets 384 px right padding, animated 200 ms cubic-bezier(0.4,0,0.2,1). Closing the rail lets the page card widen to full width.
- One ~46 px header row. Page title left; bell and rail toggle (tooltip "Expand sidebar", shortcut ⌘O) at the page card's top right. Rail's own row: chat tab pills left, + and history clock right.
- Tabs: 11 px Lexend 500, 4×8 padding, 8 px radius. Active tab gets a tinted fill (rgb 232,230,220); inactive is plain text. + appends a new tab at the end and selects it.
- History opens as a popover menu grouped by age ("Older"). Choosing one adds a tab (prior check).
- Weakness: with 9 tabs only 4 are visible; overflow is clipped with no scroll, no menu, and the active tab can be hidden. Tabs carry no name, unread or draft state.
