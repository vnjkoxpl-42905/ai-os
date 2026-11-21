# Tutoring and scheduling audit, 2026-10-14

Requested: separate Tutoring from Schedule & Calendar; make credit assignment easy and account-linked; verify on the saved student test account.

## Live findings

- Signed in normally using the saved student test account, `joshua.fisseha01@gmail.com`, rendered as josh.
- Existing rail Schedule opened `/schedule`; Book a session opened account-linked `/booking`. A separate public link is not required for signed-in students.
- Added exactly one credit to the existing pass `54c4d524-e663-461a-ad2a-784ea6b10709`, from 5 to 6 remaining. Original slug retained. Fresh admin read verified 6; student browser showed 6 after reload.
- Reproduced stale balance: an already-open booking screen stayed at 5 after the grant until reload.
- Student selected Friday 2026-10-16 at 14:20 America/Toronto and reached final confirmation. Canceled before Book it. No booking, invite, or credit consumption was tested.
- Initially confused the separately named tester (`stunned-glory-eats@duck.com`) with the saved student test account. Restored that account from 6 to its original 5. The saved test account retains the requested additional credit.
- Existing teacher grant UI defaulted to five credits and only offered an absolute reset to five on an existing pass, rather than a one-credit increment.
- Earlier live pause calls returned HTTP 500 with `[object Object]`; this remains an unresolved live backend failure. Do not claim source availability proves deployed SQL readiness.

## Implemented in local preview

- Independent Tutoring (`/booking`, preserving old URLs) and Schedule & Calendar (`/schedule`) rail entries.
- Tutoring page exposes session credits and booking. Calendar retains tasks, due work, and booked sessions.
- Booking credit refresh on focus, return to visible tab, 30-second interval, and explicit Refresh credits.
- Shared request generations prevent stale background requests overwriting newer post-booking balance/history.
- Teacher panel defaults new grant to one, supports custom count, adds one/custom amount to existing pass, retains original link and usage, and displays status/expiry. Lookup failures block accidental replacement creation.
- New backend `add_credits` action forwards to the existing row-locked SQL routine. Real backend error messages are preserved.

## Verification and limits

- Local signed-in tester: both rail destinations, balance, available times, and Refresh credits preserving chosen time checked through browser.
- Local teacher: student dossier Schedule shows 6/6, active, no expiry, Add 1 session and custom Sessions to add controls.
- Tutoring and calendar browser captures at 390, 768, 1024, 1440 pixels: no horizontal overflow. Screenshot evidence is in this folder.
- 33 focused component/navigation/pass-selection tests passed. Typecheck and production build passed; the final typecheck after merging current main is recorded separately in chat.
- Source commit `26a3dbb0`, integrated with current main in `957882e6`, in `C:/Users/Joshu/dev/ai-os-projects/.lsatu-booking-messages-20261014`. No unrelated generated MCP stub was included.
- Not published yet. New teacher increment action requires Lovable-managed backend deployment, explicit immediate credit-spend confirmation, then live teacher-to-student verification. Source tests do not verify deployed endpoint/SQL behavior.

Final source head: f5f16169. Integrated typecheck passed. Explicit six-argument RPC calls added as compatibility hardening; live error root cause remains unverified. No push or deployment occurred. New teacher increment action must be live-tested after approved backend deployment.

## 2026-10-14 | Tutoring payment options

Live student-booking info returned enabled single-session, 5-hour, and 10-hour offers. Both Stripe payment links and /book/session returned HTTP 200; single-session entry displayed $45 and available times. No purchase made. Local tester browser verified all three link destinations and email-matching guidance; 13 focused tests covered no-pass, exhausted, available credits, empty registry, hub links and booking-card refresh. Existing payment URLs/pricing retained. Source commit 092d595d; not pushed/published pending earlier Lovable deployment approval. Generic package links rely on checkout email matching account email; automatic payment-to-credit issuance not live-tested.
