# Student Access Tiers: Brainstorm / Discovery Notes
Date: 2026-09-22 · Goal: Pin down a three-tier access model for LSAT U before any code is written
Status: in progress
Context sources: live `profiles` access flags (13 booleans), `admin-manage-users` edge function, `DeskPeopleSurface` People page, PR #129 (revoke-all fix, merged), PR #130 (archive + permanent delete, merged)

## Starting position (established earlier today, not re-asked)

- Access today is 13 boolean columns on `profiles`, all defaulting to **true**. A new signup gets everything.
- `useUserPermissions` reads them, `ProtectedRoute` gates routes, the classroom rail padlocks items. Admins bypass all flags.
- Grant Full Access / Revoke All Access exist and now work correctly (PR #129). Archive and permanent delete exist (PR #130).
- Per-flag toggles and Trial/Standard/Full templates already exist in `adminUsers.ts` + `AdminDashboard.tsx`, but `AdminDashboard` is **not mounted on any route**, so none of it is reachable today.
- The edge function already supports single-flag `toggle` and `apply_template` actions.
- `profiles` is now in the realtime publication, so a flag change reaches an open tab immediately.
- Neither PR is live on lsatprep.study yet: the migration for #130 is unapplied and the frontend is unpublished.

## Tier sketch as stated (Joshua's words, unverified as final)

- **Tier 1** - triggered by booking one session; that one session grants full access to every feature.
- **Tier 2** - Joshua chooses which features. Individual toggles, instant effect, removing a toggle removes the thing from the platform for that student.
- **Tier 3** - access only to what he strictly assigns (e.g. one practice test section), nothing else.

## Research findings (code, 2026-09-22, not user answers)

### Booking and session lifecycle

- **Tier 1 already half exists.** `supabase/functions/_shared/grantStudentAccess.ts:26-48` turns on 9 of the 13 flags (`classroom, practice, drill, bootcamp, journal, waj, chat, schedule, activity`) and is called from `booking-commerce-webhook/index.ts:238`. It does **not** turn on `analytics`, `flagged`, `export`, `ta`.
- **Its trigger is payment, not booking.** It fires on Stripe `checkout.session.completed` with `payment_status === 'paid'`. A Cal.com booking never touches flags. Fire-and-forget: if the payer has no account yet it returns `no_account` and nothing retries.
- **Nothing ever revokes automatically.** Deliberate, per the comment at `grantStudentAccess.ts:5-7`. Revocation is manual through `admin-manage-users`.
- **"Has booked" is answerable.** `booking_pass_redemptions.status='booked'` joined via `booking_passes.student_id`, OR `single_session_bookings.user_id` with `status='booked'`. Cal.com bookings live separately in `external_booking_events`.
- **"Has attended" is NOT answerable automatically.** No provider sends a completion event. `single_session_bookings` has no completed state at all. The only genuine attendance signals are manual: `student_sessions.status` (admin/ingestion-written) and `booking_pass_redemptions.status='no_show'` (admin action).
- **"Credits used up" means fully booked, not fully attended.** `booking_passes.used_credits` increments at redemption (booking time), and cancellation refunds it.
- Two parallel booking systems coexist: Booking Passes (credit buckets) and Single Session (native Stripe, 70 min). Plus a Cal.com mirror.

**Consequence for Q4:** an expiry rule based on "the session was used" cannot be built reliably, because no automated path knows a session happened. Only a time-based rule or a manual one is implementable.

### Assignment mechanics (Tier 3)

- **`classroom_items` is the universal student feed.** One row per thing the student sees. `type` covers drill, homework, activity, bootcamp_module, note, session_recap, announcement, weekly_plan_task and more. `visible_to_student` + `unlock_at` + `status` control exposure, enforced in RLS.
- **Per-student payload tables:** `homework_assignments`, `activity_assignments`, `ta_assignments`, `guided_drill_assignments`. Each is a snapshot keyed by `student_id`. `homework_sets` is an admin-only template that never reaches a student.
- **A precedent for Tier 3 already exists, twice.** `BootcampGate` (`src/components/hub/BootcampGate.tsx`) checks for an assigned `classroom_items` row and shows "Not assigned yet" otherwise. The `/bootcamp/*` routes are wrapped in BootcampGate **alone, with no ProtectedRoute and no flag**. `Bootcamps.tsx` does the same in list form. Both bypass entirely for admins.
- **Route guards are per category, never per item.** `/classroom/:assignmentId`, `/classroom/item/:itemId` and `/classroom/ta/:assignmentId` all use `has_classroom_access` (note: the TA route does *not* use `has_ta_access`). `/activities/:assignmentId` uses `has_activity_access`.

**The Tier 3 trap — a timed section needs two flags.** Joshua assigns a timed section as a `homework_set` whose qids share one PT and section. `/section/:assignmentId` is guarded by `has_classroom_access`, but pressing GO launches into `/drill`, which is guarded by `has_drill_access` (`DrillLaunchGate`). So a Tier 3 student with drill off can open the directions screen and then hit a dead GO button. Assignment-only access cannot work while the runners stay flag-gated.

**A full practice test is not assignable at all.** `practice_test_runs` is self-started (`user_id` defaults to `auth.uid()`); the Testing Centre has no assignment lookup. `/testing` is guarded by `has_drill_access`. So a whole practice test is bought by a flag, not granted per item. This is the main gap for an assignment-only tier.

## Summary / key decisions

All confirmed by Joshua unless marked otherwise.

### The model

- A **tier is a template**. Selecting it applies a set of switch positions. The switches stay the thing the app checks, so nothing downstream changes.
- **One tier per student.** No stacking.
- **12 switches**, not 13: the two Wrong answer switches merge into one.

### The tiers

| Tier | Meaning | Applied how |
|---|---|---|
| **Tier 1** | Every feature on | Manually by Joshua only. Indefinite, never expires. |
| **Tier 2** | Joshua picks each feature individually | Manually. Instant effect. The toggles he sets persist as the student's state. What is *not* kept is a snapshot: leaving Tier 2 and returning does not restore an earlier set. |
| **Tier 3** | Only what Joshua assigns, plus the floor | Manually, or by pressing X in the signup queue. |
| **(no tier)** | Undecided. Same access as Tier 3, but sits in the queue | The state every new signup starts in. |

- **The floor** (Tier 3 and no-tier alike): Classroom home, Messages, Schedule. Nothing else.
- **Tier 1 is all-on by definition.** Turning any switch off relabels the student Tier 2. The relabel changes the label only, never access.
- **Assigned work authorises its own runner**, following the existing BootcampGate pattern. An assigned item opens regardless of switch state. This is what makes Tier 3 mean what it says.

### The governing rule

**"The access should never change by itself."** Stated twice by Joshua. Consequences:

- Payment no longer grants access. The existing `grantStudentAccess` automation is removed and replaced by a notification.
- No expiry, no automatic downgrade, no automatic upgrade.

### The signup queue

- Lives on **both** the admin homepage (Today) and the **Students** tab.
- Contains brand-new signups **and** everyone with no tier.
- **Checkmark** assigns a tier (1, 2 or 3) inline.
- **X** puts them on Tier 3 with nothing assigned, which is functionally no access. This empties the queue properly and leaves them on the student list.

### Migration day

- Everyone keeps their current access, with one deliberate exception.
- 19 with everything on -> **Tier 1**.
- 6 partial -> **Tier 2** with current toggles kept.
- 14 classroom-only -> **Tier 3**, and they **regain Messages and Schedule**. This is the one intentional widening: the floor exists so a locked-out student can ask why.
- Rewiring the mislabelled switches must not change anyone's effective access.

### Archive

- Archiving remembers the tier and keeps access off. Unarchiving shows the previous tier; Joshua still chooses what to reopen.

## Round 7 answers

- **Q26 - Per-practice-test assignment:** **Recommendation rejected. Build it.** "there's only specific practice tests I do assign... I want them to be specific to whatever I assign specifically only that specific thing they can get. We don't have to assign them for the whole feature forever; just specifically that one individual practice test section or drill or whatever it is."
- **The governing principle this establishes:** for Tier 3, access is granted **per item, never per feature**. Assigning one practice test must not hand over the Testing Centre. Assigning one drill must not hand over the question bank. This applies to every assignable kind, with no exceptions.
- **Q27 - Which runners accept an assignment:** **Answered by implication** - "that one individual practice test section or drill or whatever it is" covers every kind. All runners learn to accept an assignment: Drill (timed sections, homework, guided drills), Activities, TA worksheets, and now the Testing Centre.
- **Scope consequence:** full practice tests need a new per-student assignment path. `practice_test_runs` is currently self-started (`user_id` defaults to `auth.uid()`) with no assignment table, so this is genuinely new work rather than a rewire.

## Round 8 answers (final)

- **Q28 - What counts as one practice test:** **A practice test means the full sitting.** "If I say 'practice test,' it should be a practice test. If I want to assign a section, then build a side section." So there are two distinct assignable kinds, not one: a **Practice test** (the full Testing Centre sitting) and a **Section** (one timed 35-minute section). Do not collapse them. Sequencing between the two was not specified and is an implementation decision for the plan.
- **Q29 - Do students see their tier:** **No.** Tier is operator language only.
- **Q30 - History of tier changes:** **Not wanted.** Recommendation rejected; no audit trail.
- **Q31 - Do tiers touch anything else:** **No.** Tiers control feature access only. Nothing to do with booking rates, session length or pricing.

## Open flags

None. Every branch answered.

## Status

**Complete.** Interview finished 2026-09-22. Frontier empty. Awaiting Joshua's confirmation that the write-up reads right before any code is written.

### Resume point

Next step is a written implementation plan built from the Summary above, for Joshua's approval. Three items from earlier in the same session remain outstanding and interact with this work:
1. The PR #130 migration is not applied to the live database.
2. The frontend is not published to lsatprep.study.
3. The 14 revoked students are still classroom-only. Their fix is now folded into this plan's migration (they become Tier 3 and regain Messages and Schedule), so it should not be done separately.

## Round 6 answers

- **Q23 - What X does:** X puts them on Tier 3. Confirmed.
- **Q24 - The 14 revoked students:** Tier 3, regaining Messages and Schedule. Confirmed.
- **Q25 - Archive and tiers:** Remember the tier, keep access off. Confirmed.

## Q&A log

### Round 1

#### Q1 - What a tier actually is (tier computes the flags vs replaces them)
- Asked: Should a tier be a label that computes the 13 flags, or a new column that replaces them?
- Recommended: Tier computes the flags. Add `access_tier`, keep the flags as the enforcement layer.
- Captured: **Not answered directly.** Joshua answered in UI terms instead: "those should be on the students page. When I clicked tier two, it should have given me tier two. Let's have a see all the options."
- Tentative: His phrasing implies the tier is a control on the Students page, and that picking Tier 2 reveals the full feature list to toggle. That is consistent with the recommendation but is not an explicit answer on the data model.
- Flags: Re-ask in Round 2 -> Joshua.

#### Q2 - One tier at a time, or stacking
- Asked: Can a student hold more than one tier at once?
- Recommended: Exactly one tier at a time.
- Captured: **Confirmed.** "students should not be able to have more than one tier."

#### Q3 - Where a new signup lands
- Asked: What tier does a brand-new account get at first sign-in?
- Recommended: Tier 3 (assigned-only), with a floor of classroom home, messages, schedule.
- Captured: **Answered, and narrower than recommended.** "every time my student enrolls, the default should be no access, just the homepage, and to be able to schedule." He named **two** items: homepage and schedule. He did not name messages.
- Flags: Conflicts with his own Q5 answer (see below) -> Joshua to resolve in Round 2.

#### Q4 - When Tier 1 access ends
- Asked: Does Tier 1 full access ever expire on its own?
- Recommended: Never auto-expires; downgrade by hand.
- Captured: **Confirmed.** "tier one should be ... indefinitely."
- Supporting fact: the research above shows no automated path knows a session was attended, so an attendance-based expiry was not buildable anyway.

#### Q5 - What a Tier 3 student sees with nothing assigned
- Asked: What stays open for an assigned-only student before anything is assigned?
- Recommended: A floor of three - classroom home, messages, schedule.
- Captured: **Confirmed as recommended.** "when I assign something, what you recommended is the right way to go."
- Flags: The recommendation he accepted includes **messages**, which his Q3 answer omitted. Unresolved conflict, do not silently pick one.

### Round 2

#### Q6 - Tier sets the switches, or replaces them (re-ask of Q1)
- Recommended: The tier sets the switches; keep the switches as the enforcement layer.
- Captured: **Confirmed.** "there should be a toggle for each tier, and then it executes it. This is like templates. Yes."
- Decision: A tier is a template. Selecting it applies a set of switch positions. The 13 switches remain what the app checks.

#### Q7 - Does the default include Messages
- Recommended: Yes, include Messages, or a locked student has no way to ask why.
- Captured: **Confirmed.** "it should include messages." Conflict from Round 1 resolved: the floor is **three** items - Classroom home, Messages, Schedule.

#### Q8 - What did he click
- Captured: **"that was an accident."** No competing tier system is being built in Lovable. We are building fresh.

#### Q9 - What triggers Tier 1
- Recommended: Keep the existing automatic payment trigger and raise it to all 13 switches.
- Captured: **Rejected the automatic part.** "it should only be where I toggle tier one by myself." Tier 1 is applied manually by Joshua, not automatically by a payment or a booking.
- Flags: This contradicts live behaviour. `grantStudentAccess.ts` already fires automatically on every Stripe payment and turns on 9 switches. Must decide whether that automation is removed -> Round 3.

#### Q10 - How an assigned item runs when its switch is off
- Recommended: (a) the BootcampGate pattern - an assigned item authorises its own runner.
- Captured: **Not answered.** Re-ask in Round 3 -> Joshua.

#### Q11 - What happens to the existing 41 people
- Recommended: Map each person to the tier matching their current switches so nobody's access changes on the day.
- Captured: **Confirmed.** "for everybody right now, their access should stay the same."

### Round 3

#### Q12 - How an assigned item runs when its switch is off
- Recommended: (a) the BootcampGate pattern - an assigned item authorises its own runner.
- Captured: **Confirmed.** "it should basically authorize its own runner." Assigned work opens regardless of switch state. This is the core mechanism of Tier 3.

#### Q13 - The automatic payment grant
- Recommended: Replace the automatic grant with a notification.
- Captured: **Confirmed, and extended into a new requirement.** "No need for the tiers to be triggered by the actual payment." Plus the governing principle, stated twice: **"the access should never change by itself."**
- New requirement - a signup queue on the admin dashboard: when somebody signs up they appear on Joshua's admin homepage with an inline control (checkmark / X / slash-delete). The checkmark assigns a tier (1, 2 or 3) straight from the dashboard. The queue stays on the dashboard page.
- Also: "Every time I change the toggle, it should automatically reflect that." Already satisfied - `profiles` is in the realtime publication, so a switch change reaches an open tab immediately.
- Existing machinery to build on: `notify_admins_on_signup` trigger fires on `profiles` INSERT; `notifications` rows carry `type='signup'`; `ClassroomLayout` already counts unread signups.

#### Q14 - Tier label drift when one switch is changed
- Recommended: The student silently becomes Tier 2, because the template no longer describes them.
- Captured: **Not answered.** Re-ask -> Joshua.
- Note: his principle "access should never change by itself" concerns access, not the label. The recommendation changes only the label, never access, so the two do not conflict.

#### Q15 - Does Tier 2 remember previous toggles
- Recommended: No memory.
- Captured: **Not answered (second time).** Re-ask -> Joshua.

#### Q16 - The mislabelled switches
- Recommended: Rewire to match the labels, keeping everyone's effective access identical on the day.
- Captured: **Confirmed.** "Please rewire them to match their labels, using simple and concise language so I can easily understand what they refer to." Labels must be plain English.

### Round 4

#### Q17 - Tier label drift when one switch is changed (third ask)
- Recommended: They become Tier 2, because the template no longer describes them.
- Captured: Joshua answered **"Tier 1 should automatically enable all of the features."** That defines Tier 1 as all-switches-on rather than addressing the drift case directly.
- **Inferred, flagged for correction:** if Tier 1 means every feature on, then a student with one feature off is by definition not Tier 1, so the label becomes Tier 2. Recorded as the working decision. Joshua to correct if he meant something else.

#### Q18 - Does Tier 2 remember previous toggles
- Recommended: No memory.
- Captured: "it doesn't have to remember."
- **Corrected 2026-09-22, same session.** "No memory" was the interviewer's wording and was too broad. Joshua's correction: "it should save what I assign or which feature that I toggle on but that's about it."
- **Precise decision:** the toggles Joshua sets on a Tier 2 student **are saved** - they are the student's switch state and persist normally. What is not kept is a **snapshot of a previous Tier 2 configuration**: moving Tier 2 -> Tier 1 -> Tier 2 does not restore the earlier set, because Tier 1 turned everything on and that is now the truth. No history, no stored configurations.

#### Q19-Q22 - Signup queue location, the X action, queue contents, plain-English labels
- Captured: **Not answered.** Re-asked in Round 5 -> Joshua.

### Round 5

#### Q17 - Tier label drift (confirmed directly, superseding the Round 4 inference)
- Captured: **Confirmed.** "I can't be able to turn off the drill if I have Tier One; they should become Tier Two." The Round 4 inference was correct. Tier 1 is all-on by definition; any deviation relabels the student as Tier 2. Access is unchanged by the relabel.

#### Q19 - Where the signup queue lives
- Recommended: Today only.
- Captured: **Answered, broader than recommended.** "It should just be on my homepage for Q19. And actually, I should see my student's tab as well." The queue appears on **both** the admin homepage (Today) and the **Students** tab.

#### Q20 - What the X does
- Recommended: Archive them.
- Captured: **Rejected archive.** "[X] should just not give them any access, leaving them in a queue or essentially like they'll be student lists but just not given any access." So X means: no access, and they stay on the student list. Not archived, not deleted.
- Flags: **Conflicts with the Q21 answer.** If X leaves them with no tier, and the queue is keyed on "no tier", they never leave the queue and X records nothing durable. Resolution needed -> Round 6 (Q23).

#### Q21 - What the queue contains
- Captured: **Both.** "Brand new signups for question 21 and also everyone who has no tier."

#### Q22 - The plain-English labels
- Captured: **Confirmed as written.** 12 labels after the two Wrong answer switches merge:
  - Practice: Drill · Practice tests · Activities · Bootcamps
  - Review: Wrong answers · Flagged questions · Progress and history · Export
  - Classroom: Classroom · Messages · Schedule and booking · TA worksheets

### Reference: the 13 switches (supplied to Joshua, not a question)

| Group | Label | Column |
|---|---|---|
| Practice | Drill | `has_drill_access` |
| Practice | Practice tests | `has_practice_access` |
| Practice | Activities | `has_activity_access` |
| Practice | Bootcamps | `has_bootcamp_access` |
| Review | Wrong answers | `has_journal_access` |
| Review | Wrong answer journal | `has_waj_access` |
| Review | Flagged | `has_flagged_access` |
| Review | Analytics and History | `has_analytics_access` |
| Review | Export | `has_export_access` |
| Classroom | Classroom | `has_classroom_access` |
| Classroom | Messages | `has_chat_access` |
| Classroom | Schedule | `has_schedule_access` |
| Classroom | TA assignments | `has_ta_access` |

**Mislabelled switches - must be fixed as part of Tier 2, because Tier 2 exposes them all:**
- `has_practice_access` "Practice tests" does **not** gate the Testing Centre; `/testing` uses `has_drill_access`. It actually gates `/sets` (saved Question Sets).
- `has_ta_access` "TA assignments" does **not** gate `/classroom/ta/:assignmentId`, which uses `has_classroom_access`.
- `has_journal_access` and `has_waj_access` both point at `/journal`, which opens if **either** is on. Two switches, one page.

#### Observation from his screenshot (not a question)
- The Lovable preview shows the People page with the PR #130 panel live: Role Management, Account, and "Remove from your list / Archive". So the frontend build carries the archive work.
- The panel shows **no tier control and no per-feature toggles**. The per-feature toggle UI (`FLAG_GROUPS` in `adminUsers.ts`) lives in `AdminDashboard.tsx`, which is not mounted on any route. That is why "all the options" are not on screen.

## Open flags (pending input)

- (none yet)
