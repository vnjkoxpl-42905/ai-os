---
type: operating-layer
subject: Aspiring Attorneys the business
updated: 2026-07-17
aliases: []
---

# Aspiring Attorneys — the business

Authored context — what the business is and how it runs. One authoritative home (moved from `wiki/entities/aspiring-attorneys.md`, 2026-07-17); the router points here. Source of the underlying answers: `aios/aios-intake.md` (Q1–Q7, 2026-07-16).

North star: **automate everything around the sessions so Joshua only shows up and teaches.**

## What is sold, to whom

- Personalized 1-on-1 LSAT tutoring/coaching: individual sessions, and five-hour / ten-hour packages **with between-session coaching included**. All paid upfront — no package-balance model exists.
- Standard post-consultation offers are a single session at **$45/hour**, a five-hour package at **$40/hour**, and a ten-hour package at **$35/hour**.
- In the prospect-facing standard follow-up, show only those hourly rates. Do not display the five-hour or ten-hour package totals. The workflow still validates the underlying total charged by each payment link before scheduling and sending.
- Label the single-session link `Schedule here`. Label the five-hour and ten-hour package links `Purchase here`.
- Post-consultation emails present all three standard offers with a verified action link for each only when no special arrangement exists. A verified person-specific arrangement replaces the standard menu entirely; never mix bespoke terms with unrelated standard offers.
- A special arrangement exists only when Joshua explicitly states it, including an explicit statement preserved in the consultation notes or email thread. Never infer a discount or bespoke offer from financial concerns, fee-waiver status, geography, historical links, or other circumstances.
- The standard consultation follow-up time is **3:00 PM Toronto time on the next calendar day, including weekends and statutory holidays**, after confirming the consultation occurred, usable notes exist, no follow-up was already sent, and the prospect has not paid.
- Consultation follow-ups are scheduled automatically and send at the standard time unless Joshua stops or changes them beforehand. This approval-by-silence rule applies only to the bounded consultation follow-up workflow.
- Only one or two lines in a consultation follow-up are personalized from the notes. They prioritize the prospect's goal, test timeline, and central LSAT problem; scores appear only when central, and sensitive details are not repeated merely to demonstrate personalization. The lines must sound specific and human, not generic or AI-written.
- Do not include a breathing-room line claiming Joshua waited a couple of days or gave the prospect time to think. The standard follow-up sends the next calendar day, and the email must describe timing truthfully.
- If the prospect uses 7Sage and their 7Sage profile URL is not already available, the consultation follow-up asks them to send the URL.
- The request must specifically ask for the URL copied from the 7Sage Analytics page. Accept only the canonical `https://7sage.com/u/usr_<id>/review` form as an analytics URL. Drill-builder links, settings pages, and login-token URLs are not substitutes; login-token URLs must be treated as credentials and rejected.
- Place the conditional 7Sage Analytics request beside the LSAT U signup step near the end of the consultation follow-up. It is a locked conditional line, not one of the one or two AI-personalized recap lines.
- Variant C in `email system/Post-Consultation Follow-Up Template.md` is the canonical consultation follow-up base when no special arrangement exists. Workflow automation may fill its bounded personalization, 7Sage, pricing, and verified-link fields, but should not invent a replacement sales structure.
- Remove the application-form step from Variant C. Consultation follow-ups must not send Google Forms or `gformsapp.com` links; intake belongs inside LSAT U during onboarding.
- The consultation follow-up includes LSAT U account creation near the end of its next steps using `https://lsatprep.study`. A prospect may sign up before payment because Joshua controls student permissions. Intake, permissions, and teaching access still begin only after confirmed payment.
- Send the consultation follow-up inside the existing consultation conversation when a usable Gmail thread exists. Otherwise, start a new message with the fixed subject `Next steps + tutoring options`.
- Confirmed payment, not an email reply, triggers onboarding. Standard payments resolve through Stripe for packages and Stripe-linked Cal.com for single sessions; a verified special arrangement uses its stated authority. Cancel any scheduled consultation follow-up if payment arrives before its send time.
- Automatic consultation follow-ups fail closed unless the recipient, current prospect state, prices, and price-to-link mapping all verify. Reject placeholders, malformed URLs, form editor links, login-token URLs, self-addressed tests, and one payment link reused across distinct paid tiers without an explicit arrangement. Run validation before scheduling and again before sending.
- Verified standard links, all three re-checked live against Stripe/Cal.com on 2026-09-08: single session, `https://cal.com/joshua-jtx5ud/session-link` at $45 for 70 minutes; five-hour package, `https://buy.stripe.com/4gMaEY05F3dc9x13NqdZ61x`, renders "5 hours — $200.00"; ten-hour package, `https://buy.stripe.com/3cI6oI2dN5lk4cHcjWdZ61O`, renders "10 hour reduced — $350.00". The ten-hour link is correct; the earlier note that no verified $350 link existed was stale. Historical ten-hour links that charge $500 must still not be used.
- Students in the **United States and Canada**.
- Also building **LSAT U** (lsatprep.study) — the online prep platform; code and product docs live in `projects/lsatu/`.

## Money and booking

- **Stripe** — packages; **Cal.com (Stripe-linked)** — individual paid sessions and free consultations; **e-transfer** rare (Canada).
- All sessions land on **Google Calendar** and are conducted on **Google Meet**.
- Tracking today is mainly the Stripe dashboard. **Gap:** no single per-student view of payments and sessions-used vs purchased — Cal.com answers sessions-used; a mirror view belongs in `students/` as `*.generated.md`, never a Markdown ledger.
- **Self-scheduling links are situational.** Send the appropriate booking link, instead of proposing times, when a student has paid for a session but has not scheduled it, needs to reschedule, or has paid for a package with sessions to book. Do not apply this as a blanket rule to every prospect or email.
- **Billing is contextual.** Before drafting a billing or payment reply, reconstruct the specific person's payment source, purchase type, amount or package, relevant agreement, session history, and timeline from the student file and authoritative live systems. Different students can legitimately have different arrangements. Do not force a generic billing answer onto incomplete facts.

## Channels

- **Gmail (contact@aspiringattorneys.com)** is the main channel — consultations, student threads, follow-ups. The **LSAT U in-app inbox** (Supabase) is a growing second. WhatsApp/iMessage negligible. Solo operator — no team.
- Google Meet generates **full transcripts + notes after every session**, arriving by Gmail, attached to the calendar event, and in Drive — the reliable ingest signal for `students/<name>/`.

## The weekly time-sucks (ranked)

1. **Post-session work** — notes, homework, assigning work, study schedules.
2. **Session prep** — per-student, analytics-informed (7Sage + platforms). Target state: prep is "nearly mindless"; the system reviews everything and prepares the session.
3. **Pre/post-consultation email workflow** — partly covered by the `consultation-*` skills.
4. Conducting sessions — the one part Joshua keeps.

## Known gaps

- No centralized teaching-materials store (scattered, mostly Google Drive) → `corpus/` is the designated home.
- No centralized per-student records → `students/` is the designated home.
- No central tutoring-business tracker (students, sessions, homework, follow-up state) → future cadence build; mirrors from backends (live systems are authority, the brain mirrors).

Voice for anything a student or prospect reads: `wiki/teaching-voice.md`.
