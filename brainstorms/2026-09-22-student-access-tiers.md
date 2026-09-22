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

(running synthesis, updated as answers land)

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
