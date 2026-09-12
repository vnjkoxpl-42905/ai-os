---
type: brainstorm
subject: Booking Admin Redesign Brainstorm / Discovery Notes
updated: 2026-07-19
aliases: []
---

# Booking Admin Redesign: Brainstorm / Discovery Notes
Date: 2026-07-19 · Goal: Lock the design + build plan for rebuilding the LSAT U booking-pass admin page ("Booking") modeled on Calendly/Cal.com admin dashboards, in a deep burgundy holographic theme.

## What we know going in (from Joshua's message + screenshots)
- Current `/teacher/booking-passes` page is "terrible" — flat list of pass cards, amber/gold accent. Rebuild the interface.
- Reference 1: Calendly Meetings admin (light, left sidebar, page header, toolbar with scope dropdown + search + filter, empty-state illustration).
- Reference 2: Cal.com Event types admin (dark, left sidebar, page title + subtitle, search + New button, dense row list: name, slug, duration/price chips, toggle, icon actions).
- Theme: NOT gold/amber. Deep burgundy red, "holographic like the blue but replace with deep burgundy red."
- Branding: should say "Booking"; replace the logo with... (unclear — flagged Q).
- Existing backend is fine: booking_passes table + booking-pass-admin edge function (create/list/update/rotate/revoke/history/availability).

## Summary / key decisions (FINAL — locked Q13)
1. **Own workspace** at `/booking` (admin) with left sidebar; students keep their booking page at the same route. Replaces `/teacher/booking-passes` as the primary surface.
2. **Branding:** "Booking" wordmark + small LSAT U monogram, top-left of sidebar.
3. **Theme:** light base (Calendly-style white), deep burgundy (~#6e1423 family) as the accent playing Calendly-blue's role; animated iridescent sheen (burgundy → wine → rose-gold) on wordmark, primary buttons, active states only.
4. **Sidebar sections (5):** Passes (landing), Bookings, Students, Availability, Settings.
5. **Passes:** Cal.com dense rows — name + copyable slug, chips (duration, credits left, expiry), pause/unpause toggle, icon actions + overflow (Edit / Rotate / Revoke / History). Toolbar: search + New pass.
6. **Pause/unpause:** new `paused` status in backend; paused link shows "booking paused" to the student; revoke stays permanent.
7. **Bookings:** Upcoming/Past tabs across all students (new list-all-redemptions backend action); rows: student, date/time, duration, status, Meet link; cancel / no-show actions.
8. **Students:** list = students with (or formerly with) a pass; detail = pass status/credits, private link, their bookings, and a LIVE preview that is the real /book/:slug page (hard requirement: preview IS what the student sees).
9. **Settings:** admin-side defaults only (default session length, credits, expiry for new passes).
10. **Theme scope:** admin AND student-facing pages (in-app booking page + /book/:slug landing) get the burgundy "Booking" treatment.
11. **Build:** all in one go, verified in browser before a single push. Fully responsive. Existing LSAT U fonts.

## Q&A log

### Q1 — Overall page shape
- Asked: own full workspace with left sidebar (Calendly/Cal.com style) vs single page in teacher shell.
- Captured: **Own workspace + sidebar.** Dedicated Booking area with its own left sidebar (sections like Passes, Bookings, Availability, Settings), page header + toolbar. Should feel like a real scheduling product.

### Q2 — Branding
- Asked: what replaces the logo; "Booking" wordmark alone or with LSAT U mark.
- Captured: **"Booking" wordmark + small LSAT U monogram beside it** in the sidebar top-left (like Calendly/Cal.com place their logo). Wordmark gets the burgundy holographic treatment. Resolves the "replace the logo with that" flag.

### Q3 — Theme base
- Asked: dark Cal.com-style base vs light Calendly-style base vs theme-toggle.
- Captured: **Light base, Calendly style.** White/near-white surfaces; deep burgundy holographic used as the accent (wordmark, active nav, primary buttons, chips) — the burgundy plays the role Calendly's blue plays.

### Q4 — Sidebar sections
- Asked: which sidebar sections.
- Captured: **All five: Passes (landing), Bookings, Availability, Settings, plus Students.** Students section (his words): "students should have there own where i can click on them and see the ones they booked, their link, and their landing page for when they open their link — what they see." So a per-student detail view: their pass(es), booked sessions, their private link, and a preview of the student-facing landing page for that link.

### Q5 — Passes list layout
- Asked: Cal.com dense rows vs redesigned cards.
- Captured: **Cal.com dense rows.** One row per pass: student name + copyable link slug; chips for duration, credits remaining (e.g. 4/5), expiry; active/paused toggle; icon actions (preview, copy link, overflow menu with Edit / Rotate / Revoke / History).

### Q6 — Theme scope
- Asked: admin only, or also student-facing pages.
- Captured: **Admin + student pages.** One coherent "Booking" product: the admin workspace AND the student /book/:slug landing + in-app booking page get the light burgundy-holographic treatment and "Booking" branding.

### Q7 — Row toggle semantics
- Asked: what the per-row switch does.
- Captured: **Real pause/unpause.** New `paused` status in backend; while paused the student link shows a "booking paused" message; can flip back anytime. Revoke remains the permanent kill, tucked in the overflow menu.

### Q8 — Holographic treatment
- Asked: concrete definition of "holographic burgundy".
- Captured: **Iridescent gradient sheen.** Deep burgundy (~#6e1423 family) as the solid accent; animated iridescent sheen (burgundy → wine → rose-gold shimmer) reserved for the wordmark, primary buttons, and active states. Subtle and premium — not rainbow, not full foil.

### Q9 — Bookings section
- Asked: content of the Bookings section.
- Captured: **Upcoming + Past tabs.** All booked sessions across every student; rows show student, date/time, duration, status, Meet link; actions: cancel / mark no-show. Requires a small new backend action (list all redemptions across passes) — approved.

### Q10 — Students section detail
- Asked: student list source + landing preview fidelity.
- Captured: **Pass students + live preview.** List = students who have (or had) a pass. Detail view: pass status/credits, their private link (copyable), their bookings, and a live iframe preview of the actual /book/:slug page exactly as the student sees it.

### Q11 — Settings section
- Asked: what Settings holds in v1.
- Captured (his words, cleaned): "Settings section should only apply to the admin side, and I want you to make sure the preview page IS what the student sees." Interpretation: Settings = admin-side defaults only (nothing student-facing configured there for now), and a hard requirement that the Students-section preview shows the REAL student-facing page (true live render of /book/:slug), not an approximation.

### Q12 — Build phasing
- Asked: phases vs single build.
- Captured: **All in one go.** Build the full workspace (shell, all 5 sections, pause status, cross-pass bookings action, student detail + live preview, student-facing restyle), verify in browser, single push.

### Q14 — Holo button flicker (follow-up grill, post-ship)
- Reported: the "New pass" button flickers. Cause: `.holo-surface` animates `background-position` across a gradient with a hard dark→light band; on a small button the moving band edge reads as flicker rather than sheen.
- Decided: **Smooth subtle sheen.** Solid deep burgundy base; faint slow-moving low-contrast highlight, eased, no visible band edge. Wordmark keeps its stronger sheen.
- CORRECTION (second report): softening the gradient did not stop it. Root cause found: the shadcn Button base applies `transition-all duration-200` and swaps background-color on hover, which fights any background-position keyframe animation frame-by-frame (plus the loop restart snapped). Final fix: buttons are fully static (rich burgundy gradient, brightness on hover); the animated sheen lives ONLY on the "Booking" wordmark. Rule: never put keyframe background animations on shadcn Buttons.

### Q15 — Friendly links (post-ship follow-ups)
- Decided: links always use canonical lsatprep.study (never Lovable preview origin), and slugs are **plain first name** — /book/josh — with a short suffix only on name collision. Joshua explicitly accepted guessable links: "doesn't have to be encrypted since this is a private tutoring service." Rate limiting stays. Rotating a slug pass regenerates the slug (old URL dies).

## Open flags (pending input)
- (none)
