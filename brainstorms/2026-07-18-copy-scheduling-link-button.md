---
type: brainstorm
subject: Copy Scheduling Link Button Brainstorm / Discovery Notes
updated: 2026-07-19
aliases: []
---

# Copy Scheduling Link Button: Brainstorm / Discovery Notes
Date: 2026-07-18 · Goal: Design a "copy link" button so Joshua can send a scheduling/booking link to students, so they can open the booking form directly.

## Summary / key decisions (LOCKED)

**Feature:** A "Copy link" button per student in the Teacher Workspace Session Booking panel. Copies that student's stable, personalized booking URL. Joshua sends it; the student opens it (no login) and books a 1:1 session Calendly-style, respecting their credits.

1. **Per-student link (A).** Each student has one unique, stable URL that carries their own pass/credits. `lsatprep.study/book/<firstname>-<shortRandomCode>` (e.g. `josh-8f3k`) — personal-looking, unguessable via the random tail (CSPRNG), not clunky.
2. **No login (B).** The token IS the credential. Frictionless like Calendly. Containment = admin regenerate/revoke (below), not login.
3. **Token carries identity (A).** No name/email form — the student record tied to the token supplies identity; confirmations go to the email on file.
4. **One stable link, admin-controlled lifecycle.** Link never changes on its own and never time-expires. Admin (Joshua) can **Regenerate** (rotate code, kill old URL) and **Revoke** (disable link) from his side. Revoke disables booking + link.
5. **Calendly-clone page — for BOTH the public token page AND the existing in-app `/booking` page.** One consistent UI everywhere. Public page = no app chrome. Layout: left host card (minimal Calendly-default: "Joshua" · "1:1 LSAT Session" · "1 hr 10 min" · "Google Meet link provided on confirmation"), right = date/time picker + timezone (in student's local zone).
6. **Same booking engine (A).** Confirm dialog ("Are you sure?") -> real Google Calendar event + Meet link, credit -1, confirmation emails to BOTH student + admin, confirmation screen. Zero credits -> "no sessions available, contact Joshua" instead of calendar.
7. **Calendar invite:** student added as attendee on the Google event (native Google invite + Meet link), not just email.
8. **Concurrency: backend-enforced** — slot re-checked at confirm against live Google Calendar + existing bookings; no double-booking.
9. **Multiple bookings allowed** — student can book as many future sessions as they have credits (1 credit each).
10. **Cancel/reschedule: admin-only for now** (self-serve deferred, matches PLAN.md).

**Locked config:** session **70 min**; **15 min** buffer after each; slots every **30 min**; **24h** minimum notice; availability from the seeded Weekly Hours windows minus Google Calendar conflicts, next-24h, and buffers.

**KEY CHANGE FLAG:** the booking system built last session uses **60 min** — must change to **70 min** everywhere (slot gen, calendar event length, emails, UI labels).

## What the screenshot shows (Joshua's reference)
Two images from Calendly:
1. A "Copy link" pill button (link icon + "Copy link") in the top-right of a booking page, next to a "Menu" dropdown.
2. The full Calendly public booking page it links to: left column = host identity ("Joshua" / "30 Minute Meeting" / "30 min" / "Web conferencing details provided upon confirmation"), right column = "Select a Date & Time" month calendar with available days highlighted + a time-zone selector ("Eastern Time - US & Canada"). "Powered by Calendly" ribbon top-right.

## Joshua's stated intent (verbatim gist)
- Wants a "Copy link" button he can send to a student.
- The link opens a page **like the Calendly screenshot** (host card on left, date/time picker on right), and "maintains the same" look/flow.
- The link should be **personalized for each student** — "based off their specific [pass] / what they paid for."
- Must **maintain the credit system** — the personalized link still respects that student's remaining sessions/credits.

## Q&A log

### Q1 — Who does the link belong to: student, or "meeting type"?
- Asked: Is the copy-link a unique per-student URL that carries that student's pass/credits (A), or one shared link for Joshua where credit-check happens after login (B)?
- Captured: **(A) Per-student link.** Each student has their own unique URL (e.g. `lsatprep.study/book/josh-<token>`). "Copy link" on that student in Teacher Workspace copies THEIR link. Opening it shows the booking page bound to that student's pass + remaining credits; if credits exhausted, page says so. Personalized to what they paid for.
- Flags: none

### Q2 — Does opening the link require login?
- Asked: Login still required (A), or is the link itself the credential, no login, pure Calendly-style (B)?
- Captured: **(B) NO login required.** The personalized link alone gets the student to the booking page, frictionless like Calendly. The token in the URL IS the credential/identity.
- Consequence (flagged for design): a forwarded/leaked link could let someone else consume that student's credits and book on Joshua's real calendar. Need containment: token hard to guess, and decide on expiry / revocation / rate-limit (see later Qs).
- Flags: containment strategy for leaked links -> resolve in later Qs

### Q3 — How does the student prove identity when booking (no login)?
- Asked: Token carries identity, no form (A), or student re-enters name+email like Calendly (B)?
- Captured: **(A) Token carries identity, NO form.** Open link -> pick slot -> confirm. Name/email already attached from the student record tied to the token. Confirmation emails go to the address on file. Most Calendly-like, fits "personalized."
- Flags: none

### Q4 — Button placement + one link vs many per student?
- Asked: Button in the Session Booking panel (Schedule tab, selected student) + one stable link per student with a regenerate option?
- Captured: **One STABLE link per student — stays the same for that person, forever.** Joshua copies it from that student's panel and sends it; the link lets them schedule. Reusable, send once. Placement: the Session Booking panel for the selected student (confirmed by "saved/available there"). Regenerate option: not explicitly addressed by Joshua -> flag to confirm.
- Flags: confirm whether a "Regenerate link" (rotate token, kill old) action is wanted -> Joshua

### Q5 — Regenerate link + Revoke disables link?
- Asked: (5a) include a tucked-away "Regenerate link" that kills old URL + issues new; (5b) Revoke disables the link?
- Captured: **YES to both.** As admin, Joshua wants full control from his side: ability to **reset/regenerate the link** (kills old URL, new one issued) AND **kill the link** (revoke disables it). Admin-driven link lifecycle.
- Design implication: token stored per-student; regenerate rotates it (old token 404s / shows "link no longer active"); revoke sets link inactive (opening shows "no active booking / contact Joshua"). Both are admin actions in the Session Booking panel.
- Flags: none — leaked-link containment resolved via admin regenerate/revoke.

### Q6 — What does the booking page look like; reuse existing or new?
- Asked: Does the link open the existing `/booking` page or a new Calendly-clone page? Recommended: clean standalone public page (no app chrome), Calendly two-column layout (host card left, date/time+timezone right).
- Captured: **Build a Calendly-CLONE page — and make it the design for BOTH** the public token page AND the existing in-app `/booking` page. The existing `/booking` page should be reworked to match the Calendly-clone layout too. ONE consistent booking UI everywhere (public + in-app).
  - Public token page: clean, no app sidebar/nav (student not logged in).
  - In-app `/booking`: same Calendly-clone visual, but rendered inside the app for logged-in students.
- Open sub-questions carried forward: (6a) session length 30 vs 60 min; (6b) contents of left host card.
- Flags: 6a, 6b pending.

### Q7a — Session length
- Asked: 30 or 60 min?
- Captured: **Neither — 1 hour 10 minutes (70 minutes).** Sustained 70-min session. NOTE: this differs from the "60 min each" currently wired into the booking system built last session — the 70-min duration must become the real config value everywhere: slot generation, Google Calendar event length, host-card duration label, confirmation emails. Prior "60 min" copy is now WRONG and must be updated.
- Flags: 7b (host-card contents) still pending.

### Q7b — Host card contents (left column)
- Asked: Minimal Calendly-default (A) / photo+copy (B) / custom (C)?
- Captured: **(A) Minimal, Calendly-default.** Left card = "Joshua" · "1:1 LSAT Session" · clock "1 hr 10 min" · video "Google Meet link provided on confirmation." No photo, no extra copy.
- Flags: none

### Q8 — What happens on confirm (the "booked" moment)?
- Asked: Same engine as in-app flow + confirmation screen + zero-credit "contact Joshua" state (A), or something different (B)?
- Captured: **(A) Same booking engine, reached via token instead of login.** On confirm: "Are you sure?" dialog -> "Yes, book it" -> creates real Google Calendar event + Meet link, decrements credit by 1, fires both confirmation emails (student + admin), shows a confirmation screen ("You're booked — date/time, Meet link sent to email").
  - After last credit used: reloading the link shows "no sessions remaining."
  - Opening link with zero credits: shows "no sessions available — contact Joshua" state instead of the calendar.
- One booking engine, one behavior; only the front door differs (token vs login).
- Flags: none

### Q9 — Token/URL shape + expiry
- Asked: Random opaque token at `/book/<token>` + no time-based expiry (credits + admin govern)?
- Captured:
  - **Expiry: NONE by time.** Link is stable/reusable; access governed by credits + admin revoke/regenerate. Confirmed.
  - **URL aesthetics: token must be UNGUESSABLE but NOT ugly.** Joshua doesn't want a long clunky random string that looks awkward/clunky when sent to a student. Wants it "disguised" / prettier while staying secure.
- Design implication (options to resolve in Q9b): (i) friendly slug + hidden entropy e.g. `/book/josh-quiet-harbor` (word-based, still ~unguessable), (ii) short random code `/book/x7GkP2` (short but still random-looking), (iii) student-name slug + short token `/book/josh-8f3k`, (iv) a branded path like `lsatprep.study/josh`. Need Joshua to pick the aesthetic.
- Flags: 9b — pick the link aesthetic.

### Q9b — Link aesthetic (chosen)
- Captured: **Name + short code.** Format: `lsatprep.study/book/<firstname>-<shortRandomCode>` e.g. `lsatprep.study/book/josh-8f3k`. First name (personal) + short random tail (unguessable). Not clunky.
  - Random tail must carry enough entropy to be unguessable despite being short (~6+ url-safe chars from a CSPRNG; avoid ambiguous chars). The name portion is cosmetic; the code is the real secret.
  - On regenerate: name stays, code rotates (`josh-8f3k` -> `josh-q2p7`), old URL dies.
  - Collision handling: if two students share a first name, the random tail disambiguates (or append nothing special — tail is unique).
- Flags: none

### Q10 — Double-booking + multiple bookings
- Captured:
  - **10a — Concurrency: YES, backend-enforced.** At confirm, slot is re-checked against live Google Calendar + existing bookings; race can't double-book. Loser sees "just taken, pick another."
  - **10b — Multiple bookings: YES.** A student can book up to as many future sessions as they have credits; each booking consumes one credit.
- Process note: Joshua wants remaining grill questions asked via POPUP (AskUserQuestion UI), not in chat prose.
- Flags: none

### Q11 — Can student cancel/reschedule?
- Captured: **Admin-only for now.** Student link is BOOK only. Cancels/reschedules handled by Joshua directly. Matches PLAN.md's deferred reschedule decision. No self-serve cancel/reschedule in this build.
- Flags: none

### Q12 — Confirmation emails + calendar invite
- Captured: **Both + calendar invite.** Student AND admin get confirmation emails. Student is added as an ATTENDEE on the Google Calendar event -> Google sends a native calendar invite (they get it on their own calendar), plus the Meet link. Admin email = "X booked <date/time>."
- Design implication: when creating the Google Calendar event, include the student's email as an attendee (with sendUpdates/sendNotifications so Google emails the invite). Existing booking-confirmation transactional emails still fire for both parties.
- Flags: verify the current event-creation call includes attendee + sendUpdates; if it only creates the event without inviting the student, that's a change to make.

### Q13 — Lead time / booking notice
- Captured: **Minimum 24-hour notice.** No slot less than 24h from now is bookable. Slot generation must exclude anything inside the next 24h.
- Carry-forward: also consider a small between-session buffer so back-to-back 70-min sessions don't collide (confirm in backstop).
- Flags: confirm buffer-between-sessions in backstop.

### Q14 — Backstop batch (buffer / spacing / placement)
- Captured:
  - **Buffer between sessions: 15 min.** After any booked/calendar-blocked session, next bookable slot starts 15 min later (session is 70 min, so effective footprint = 85 min).
  - **Slot spacing: every 30 min** (:00 and :30) within the daily availability windows.
  - **Button placement: in the Session Booking panel** for the selected student (with Reset/Revoke). Controls grouped: Copy link + Regenerate + Reset + Revoke. (Not adding to Booking passes tab for now.)
- Flags: none

## Config values (locked)
- Session length: **70 min** (1h10m)
- Buffer after session: **15 min**
- Slot spacing: **every 30 min**
- Min booking notice: **24 hours**
- Availability windows (seeded, already in Weekly Hours): Mon 2:00pm-8:00pm, Tue 1:00pm-7:30pm, Wed 1:00pm-7:00pm, Thu 1:00pm-7:30pm, Fri 1:00pm-6:30pm, Sat 2:00pm-5:00pm, Sun off. (These already drive the editor; slot gen must also subtract Google Calendar conflicts + next-24h + 15m buffers.)

### Q15 — Codex-review-driven decisions (Rev 3)
- **Legacy route `/schedule/pass/:token`: RETIRE ENTIRELY.** Remove from App.tsx, delete the token path in `booking-pass`. All booking via new `/book/<slug>` links. (Kills the pre-existing name/email PII leak in `publicPass()`.) Joshua confirmed no need to preserve old :token links.
- **60->70 existing passes: UPDATE ALL ACTIVE PASSES to 70.** `UPDATE booking_passes SET session_length_minutes=70 WHERE status='active'`. Booked redemption durations always preserved (never rewritten). No custom-length passes exist currently, so no marker column needed.

## Open flags (pending input)
- ACTION: change session length from 60 -> 70 min across slot gen, calendar event, emails, UI labels
- ACTION: ensure Google Calendar event adds student as attendee w/ invite (sendUpdates)
- ACTION: slot gen excludes next 24h (min notice) + 15m buffer + 30m spacing
- ACTION: retire /schedule/pass/:token; bulk-update active passes to 70
