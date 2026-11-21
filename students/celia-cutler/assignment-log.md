# Celia Cutler: platform operations

## 2026-10-02: five paid sessions restored

- Joshua confirmed payment for five sessions and authorized crediting Celia's account.
- Identity: Celia, celiacutler@gmail.com, student ID `749e2eae-7969-464f-bf96-a4d4cfafe2bf`.
- Before: old pass exhausted, 10/10 used, zero remaining.
- Created active pass `014de9d0-5d10-45da-80be-483c01aaba35` through `booking-pass-admin`, five 70-minute sessions, no expiry, at `2026-10-02T17:18:47.161839Z`.
- Fresh `lsatu-admin.mjs passes celiacutler@gmail.com` read confirmed 0/5 used, five remaining, active. Old exhausted pass retained.
- Automatic payment-credit investigation is in [the payment report](../../research/2026-10-02-celia-payment-crediting.md). These sessions were granted manually. Any payment replay/reconciliation must recognize this grant and avoid adding another five.
- No message or email sent.
- Stripe API independently verified USD 200.00 paid on 2026-10-01, event `evt_1ULtZOIULVCj6rqqOYGA3CEa`, correct five-session payment link and exact account email. Stripe delivery detail showed HTTP 200 at 2026-10-01 19:39:24 America/Toronto, response `{"received":true,"student_id":"749e2eae-7969-464f-bf96-a4d4cfafe2bf","grant":"awaiting_teacher"}`. Payment reached the live handler but crediting was deferred to the teacher.
- Recorded Stripe event, intent, charge and ledger linkage in the new pass notes and verified them. Cleared pending grant prompt using `admin_dismiss_stripe_payment` for row `bb89e821-778f-4ae8-bdc7-7a42478d5bda`; fresh read confirmed `grant_state=dismissed`, `match_state=matched`, pass active 5/0 and notes intact. Dismissal preserves the payment record and adds no credits. Future automatic fulfillment must skip this dismissed/manual payment.
- After Joshua approved automatic crediting deployment, Lovable applied the migration and deployed the webhook. Its rollback-only synthetic database test passed. Independently replayed the unchanged real Stripe event with the existing signing credential only after verifying Celia's dismissed state and new protection flag. HTTP 200 response `grant=dismissed`; before/after reads confirmed both passes and notes unchanged, new pass still active 5/0, and payment still dismissed with `auto_grant_eligible=false`. No additional credits or messages.

## 2026-10-15: Reading Center assigned

- Requested by Joshua: assign the Reading Center platform to Celia.
- Exact account: Celia, celiacutler@gmail.com, student ID `749e2eae-7969-464f-bf96-a4d4cfafe2bf`.
- Assigned through the live Teacher Workspace Reading Center form; start date left blank for immediate access. No due date supplied.
- UI confirmed: "Reading Center assignment verified. The student can open it from their assigned work."
- Independent fresh backend read (`node system/scripts/lsatu-admin.mjs items celiacutler@gmail.com --json`) confirmed exactly one Reading Center activity, status assigned, classroom item `3ef6c6db-ec23-4da5-9960-221466605fd1`. Before 20 items, after 21.
- [UI receipt](reading-center-assigned-2026-10-15.png). Reading Center assignment grants the tool and shared/personal library available to that student; Joshua's three private Added By Me passages were not shared by this operation. Notification/email delivery was not independently verified.
- CLI dry-run stopped before writes because the operations checkout contained unrelated hook/config edits. Those files were preserved; the live teacher interface provided the maintained assignment path.

## 2026-10-15: Three private Reading Center passages added for Celia

- Joshua explicitly requested all three imported passages be visible and openable for Celia.
- Created three Celia-owned copies through normal authenticated admin PostgREST/RLS, not service-role access. Personal owner is `749e2eae-7969-464f-bf96-a4d4cfafe2bf`; shared/public owner remains unset only on unrelated shared texts. Joshua originals retained byte-for-byte at database readback.
- Ordered titles: `1. Plants and Geological Time` (502 words), `2. Work and Quiet Desperation` (636 words), `3. Ion and Poetic Inspiration` (612 words).
- Exact saved body hashes, IDs and Celia-specific reader URLs: [access receipt](reading-center-passage-access-2026-10-15.json). Each full body matches its original after browser newline normalization.
- Fresh repeat dry-run found exactly one existing copy of each and proposed no new copies. Active Reading Center item `3ef6c6db-ec23-4da5-9960-221466605fd1` remains assigned, unlock null, assigned route `/reading-center`.
- Production bundle was checked for the non-admin assignment-gated Reading Center sidebar launcher; local current library and reader queries accept owner=self OR shared, and saved copies have owner=Celia. Her copies will appear in Added By Me.
- Verification limit: this is saved-data plus route-condition verification, not actual Celia-session navigation. No supported real-student preview exists. Asked Joshua to open a legitimate Celia-signed-in browser session for the final sidebar click-through. Did not reset credentials, impersonate her, or fabricate UI proof. No additional assignment, notification or email was sent for the text copies.

## 2026-10-15: Reading Center notification verified

Joshua requested confirming Celia receives a notification pointing her to Reading Center. Fresh authenticated admin reads found exactly one visible active immediate assignment, existing unread bell `5656242a-7d66-4125-960b-0b5e2f349388` titled `New assignment: Reading Center`, recipient Celia, link `/reading-center`, created `2026-10-15T19:08:25.693459+00:00`. Matching inbox message `5796d8bf-aff6-47c1-b71e-c00facb3ce1a` contains the same direct path. The original teacher assignment had already notified her. No duplicate notification, inbox message, email or assignment was sent. [Readback receipt](reading-center-notification-check-2026-10-15.json). Email-provider delivery was not inspected in this verification.

## 2026-10-15: Reading Center hub release preserves Celia access

Published app commit b6e09031: existing Reading Center assignment now opens a hub with Read, Recall, Colour and Speed Reading. Celia's three personal passages remain in the separate Speed Reading collection; existing RRC section assignments, recordings and results retain their IDs. No additional assignment or notification was sent. Production teacher UI and isolated account/access tests were verified; no Celia-session impersonation or microphone run.


## 2026-10-18 Reading Center side rail access

- Celia Cutler: Joshua explicitly requested Reading Center in the homepage side rail.
- Existing item reused; in_progress preserved. Item ID: 3ef6c6db-ec23-4da5-9960-221466605fd1.
- Used existing assign_reading_center RPC with exact live email/class_id resolution and a dry-run first. Fresh readback confirmed visible_to_student=true, no unlock delay, and one qualifying item. No inbox/email notifications sent by this operation.
- Backend access verified; no student-session UI verification claimed. Teacher sidebar code is a separate branch/PR change.
