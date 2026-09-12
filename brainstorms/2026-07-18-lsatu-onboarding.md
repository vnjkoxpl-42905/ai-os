---
type: brainstorm
subject: LSAT U Onboarding Brainstorm / Discovery Notes
updated: 2026-07-18
aliases: []
---

# LSAT U Onboarding: Brainstorm / Discovery Notes
Date: 2026-07-18 · Goal: Design a clean onboarding process that runs when a new user signs up on lsatprep.study, ending in an implementable design spec.

## Summary / key decisions (FINAL)
1. **Purpose:** placement/personalization intake. Flow ORDER locked to mirror a competitor reference (LexPrep) Joshua approved.
2. **Flow (7 screens):** name (step 0, reuse existing) → (1) last LSAT score band → (2) experience free-text (optional) → (3) schools, up to 5 (optional) → (4) target score band → (5) which best describes you (Undergrad/Grad/Working/Other) → (6) study time per day Sun–Sat. Final button "Finish".
3. **Design:** Academy design system (marble/bronze/obsidian + serif), RESTRAINED vs the landing — minimal animation, no showpiece motion. Dark theme only, no per-step light/dark toggle. Bronze accent, not LexPrep blue.
4. **Storage:** `profiles.onboarding jsonb` (all answers) + `profiles.onboarding_completed_at timestamptz` (the gate). No new table.
5. **Gate (one-time):** completed once, never re-shown. `onboarding_completed_at` set ONLY by explicit Skip button OR Finish. Closing the tab ≠ complete → resumes at first unanswered step. Same gate for email + Google signups. Backfill existing students to now().
6. **Skippable:** "Skip for now" on each step; a Skip press = permanently done (best-effort intake; Joshua chases stragglers via inbox). Per-step save so partial answers persist and resume works.
7. **No AI:** step 4 target score is typed/picked by the student — no AI recommendation, no median lookup, no sparkle affordance. (truthfulness rule)
8. **No mic** on step 2 (native OS dictation suffices). **No analytics** in v1.
9. **Finish = data-only v1:** save + set gate + land on Foyer. No app-side branching on answers yet (light personalization is a scoped follow-up). Vault mirror into `students/<name>/` = yes, but as a brain-side ingestion follow-up, NOT part of the app build.
10. **Routing:** single `/onboarding` route, internal step state, progress bar 1/6→6/6, Back/Continue.
11. **Score enum shared** across steps 1 & 4: `lte_150,151_155,156_160,161_165,166_170,171_175,176_180` + per-field extras (`not_taken`/`not_sure` for last, `not_sure` for target).
12. **v1 bar:** functional + on-brand, verified in-browser before "done" (LSATU hard gate).

## Existing state (from code, not asked)
- Auth: email/password + Google OAuth, via bottom-sheet drawer on the "Academy" landing (`src/pages/Auth.tsx`). Sign-up collects name, email, password.
- Onboarding today (`src/pages/Onboarding.tsx`): single step — asks "What should we call you?" (name), upserts `profiles` row (`class_id`, `display_name`), navigates to `/mainhub`. That's the whole thing.
- Routing gate: `redirectAfterAuth(user.id)` decides landing; Mainhub gates on profile row existing.
- Permissions: per-feature flags (`has_practice_access`, `has_drill_access`, `has_chat_access`, `is_admin`, ...) in `src/hooks/useUserPermissions.ts`.
- Stack: React 18 + Vite + TS + Tailwind + shadcn/ui + Supabase. Lovable canonical, GitHub mirror.

## Q&A log

### Q1 — Purpose of onboarding + the flow/order
- Asked: What is onboarding for? (placement vs activation vs orientation vs commitment)
- Captured: Joshua answered by providing 6 reference screenshots of a COMPETITOR onboarding (LexPrep, at lexprep.ai/onboarding) and saying **"this order is good."** So the goal is placement/personalization intake, and the STEP ORDER is locked to mirror this reference. LSAT U will adapt this flow to its own Academy design system + Supabase, NOT copy LexPrep's visuals.
- **Locked flow (6 steps, in order):**
  1. **"What did you get on your last LSAT?"** — single-select score bands: 150 & below, 151–155, 156–160, 161–165, 166–170, 171–175, 176–180, + "I haven't taken the LSAT yet" + "I'm not sure". (captures current/baseline score)
  2. **"How has your LSAT experience been so far?"** — free-text area + voice/mic input. Placeholder: "Logic Games felt easier, but Necessary Assumption questions are still hard for me." Subtext: "Share what has felt easy and what has felt hard so we can personalize your plan." (captures qualitative self-assessment / weak areas)
  3. **"What schools are you interested in?"** — searchable law-school picker, add up to 5, numbered 1–5. Subtext: "We'll build your experience with [LSAT U] around getting into these schools."
  4. **"What score are you aiming for?"** — same score bands + "I'm not sure yet". AI affordance: "✨ Pick schools to get an AI score recommendation" (derives a target from the schools chosen in step 3). Subtext: "This helps us set the right pace for your prep." (captures target score)
  5. **"Which best describes you?"** — 4 cards: Undergraduate / Graduate / Working / All Other Cases (icon + one-line desc each). (captures life context / available bandwidth)
  6. **"When can you study?"** — per-day Sun–Sat time budget: No time / < 1 hr / 1–2 hrs / 3+ hrs (default 1–2 hrs). Subtext: "Set how much time you have each day. You can always change this later." Final button: **Finish**.
- UI chrome across all steps: top-left brand logo, top-right theme (sun) toggle, a thin progress bar under the logo that fills 1/6 → 6/6, "Go back" + "Continue" buttons (last step = "Finish").
- Flags: LexPrep visuals are reference-only; must be re-skinned to LSAT U's Academy design system (marble/bronze/obsidian) -> confirm in later Q. Fields captured need a storage decision (profiles columns vs new onboarding table) -> later Q. "AI score recommendation" feature scope -> later Q.

### Q2 — Visual design
- Asked: Match the plain reference visuals, or re-skin to the Academy design system?
- Captured: **Option 3 — Academy tokens, restrained.** Use LSAT U's marble/bronze/obsidian + serif design language (continuous with Auth.tsx and current Onboarding.tsx's GlassShell/BorderBeam), so there's no visual whiplash after the Academy landing. BUT dial the showpiece effects DOWN vs. the landing: no particle bust, minimal animation, more whitespace. Onboarding's job is completion, not dazzle. Keep the reference's calm single-question-per-screen layout + progress bar + Go back/Continue rhythm, rendered in LSAT U's own tokens (bronze `#C6A467` accent instead of LexPrep blue).
- Flags: none new.

### Q3 — Storage + completion gate
- Asked: Where do the 6 answers live, and what marks onboarding complete?
- Captured: **Add to `profiles`** (not a new table). One-time-only gate — "should be only completed once": once a student finishes onboarding they NEVER see it again.
- Decisions:
  - `profiles.onboarding jsonb` — holds all six answers: `last_score_band`, `experience_text`, `schools[]`, `target_score_band`, `life_stage`, `study_time{sun..sat}`. Matches existing `layout_prefs`/`by_qtype_json` jsonb pattern. `profiles` is keyed by `class_id` (text), already home to per-student stats/prefs/flags.
  - `profiles.onboarding_completed_at timestamptz` — the gate. `redirectAfterAuth(user.id)` checks it: null → `/onboarding`, set → Foyer/mainhub. Set ONCE on Finish; never re-shown.
  - Name capture (existing step, name-not-username) stays as step 0 of the same flow.
  - **Backfill:** set `onboarding_completed_at = now()` for all existing students so only fresh signups get the intake. (confirm not explicitly re-stated but implied by "only completed once" + not ambushing active students.)
- Flags: confirm backfill of existing students (assumed yes) -> Joshua.

### Q4 — "AI score recommendation" affordance (step 4)
- Asked: Build the AI recommendation, do a real static median lookup, or cut it?
- Captured: **Cut the AI/recommendation entirely. Just have the person type/pick it themselves.** No sparkle line, no "AI score recommendation," no median lookup. Step 4 ("What score are you aiming for?") is a plain single-select target-band picker (150 & below … 176–180, + "I'm not sure yet") that the student answers directly. Honest, no fake affordance, no LLM, no bundled data table.
- Flags: RESOLVED — "Scope of AI score recommendation" flag is closed (feature cut).

### Q5 — What "Finish" does + landing
- Asked: Data-only, light personalization, or full adaptive placement? + mirror answers to vault?
- Captured: **Option 1 — Data-only v1.** On Finish: save the six answers to `profiles.onboarding`, set `onboarding_completed_at`, land on the Foyer exactly as it is today. NO app-side branching on the answers yet. The value is operational: Joshua now has score/target/schedule/weak-areas per new student, personalizes by hand (his premium edge). Designed so "light personalization" (seed `daily_goal_questions` from study-time, point Foyer hero ring's primary node at a matched drill) is a clean, well-scoped FOLLOW-UP task — not in v1.
- Flags: Vault mirror (write answers into `students/<name>/`) NOT yet answered — Joshua answered the level ("1") but not the mirror sub-question. Re-ask.

### Q6 — Vault mirror
- Asked: Mirror the six answers into the student vault folder `students/<name>/`?
- Captured: **Yes, mirror it.** New-student intake (score, target, schools, schedule, weak areas) should land in `students/<name>/` so Joshua sees it in the Jay 2 EA workspace. BUT: the app CANNOT write to the local vault — so this is a brain-side PULL/ingestion, folded into how student data already gets pulled into `students/<name>/`. It is a FOLLOW-UP, out of scope for the app build. App spec = write to Supabase only; vault mirror is a separate Jay 2 ingestion task.
- Flags: RESOLVED.

### Q7 — Skippable vs mandatory
- Asked: Can a student skip onboarding, or must they complete it first?
- Captured: **Skippable — a "Skip for now" escape on each step.** Student can jump to the app; Joshua nags them later. Accepted tradeoff: some students arrive with partial/no intake data. More forgiving / less friction, premium feel over forced quiz.
- IMPLICATION to resolve (Q8): interaction between "skip" and the one-time completion gate — if they skip, is onboarding marked complete (never shown again) or pending (re-prompted)? See Q8.
- Flags: none new; drives Q8.

### Q8 — Skip vs the one-time gate (collision between Q3 and Q7)
- Asked: When a student skips, is onboarding done-forever or does it come back?
- Captured: **Skip = permanently done.** Any "Skip for now" sets `onboarding_completed_at = now()` immediately, exactly like Finish. Student never sees onboarding again, even with zero/partial answers. Gate logic stays dead simple: `onboarding_completed_at` null → show onboarding; set → never again (whether reached via Finish OR Skip).
- Consequence (accepted): intake is best-effort. A student who skips arrives with no data; Joshua chases them via the inbox (manual channel), NOT via re-routing or a Foyer banner. No re-prompt loop, no dismissible card.
- Partial answers still save: if they answer steps 1–3 then skip on step 4, steps 1–3's answers persist to `profiles.onboarding`; only unanswered fields are null.
- Flags: RESOLVED — reconciles Q3 (complete once) + Q7 (skippable) with no contradiction.

### Q9 — Voice input on step 2 textarea
- Asked: Build the mic/voice dictation or drop it?
- Captured: **Drop the mic for v1.** Step 2 ("How has your LSAT experience been so far?") is a plain optional textarea — no custom mic button. Native OS/browser dictation covers users at zero cost. Voice is a self-contained later add-on if wanted.
- Meta: from Q10 onward, Joshua wants grill questions asked via the **option-picker UI (AskUserQuestion)**, not plain chat prose.
- Flags: RESOLVED.

### Q10 — Routing / layout
- Asked: One route with internal steps, or a route per step?
- Captured: **One route, internal steps.** Single `/onboarding` route; one question on screen at a time; step index held in component state (URL stays `/onboarding`). Progress bar fills 1/6 → 6/6. Back/Continue move between steps. Matches the reference exactly, simplest plumbing.

### Q11 — Resume behavior (closing tab mid-flow)
- Asked: Resume where left off, or restart from step 1?
- Captured: **Save per-step, resume where left off.** Each Continue writes that step's answer to `profiles.onboarding` immediately. On return, land on the first unanswered step. Nothing lost.
- CONFLICT to resolve (Q13): this vs Q8 "skip = permanently done." If a student answers steps 1–3, closes the tab WITHOUT skipping/finishing (so `onboarding_completed_at` is still null), do they resume (gate not set) — yes. But if they explicitly Skip, gate IS set and they're done. So: closing the tab ≠ skipping. Need to confirm closing-tab is treated as "not yet complete, resume" while an explicit Skip button press = complete. See Q13.

### Q12 — Score band data shape
- Asked: Share one enum across step 1 and step 4?
- Captured: **Same enum, two fields.** `last_score_band` and `target_score_band` share one band value set: `lte_150`, `151_155`, `156_160`, `161_165`, `166_170`, `171_175`, `176_180`. Per-field extras: last adds `not_taken` + `not_sure`; target adds `not_sure`. One enum reused, clean to query/personalize later.

### Q13 — Close-tab vs explicit Skip (resolves Q8/Q11 conflict)
- Asked: Answer steps 1–3, close tab (no Skip/Finish), next login = ?
- Captured: **Resume onboarding.** Closing the tab is NOT skipping. `onboarding_completed_at` is set ONLY by an explicit Skip-button press or Finish. So a student who just closes the tab returns to onboarding at the first unanswered step (resume). Only a deliberate Skip or Finish ends it forever. Fully reconciles Q8 (skip=done) + Q11 (resume) + Q13: gate = {explicit Skip OR Finish}; everything else = resumable.

### Q14 — Theme toggle
- Asked: Include the reference's per-step light/dark sun toggle?
- Captured: **Match app default, no toggle.** Render onboarding in LSAT U's dark obsidian Academy theme; drop the per-step sun toggle. Consistent with the landing/Auth they just came from; one less control. ThemeContext still governs the rest of the app.

### Q15 — v1 polish bar
- Asked: How polished to ship?
- Captured: **Functional + on-brand, ship fast.** All 6 steps working, Academy-skinned, per-step save, gate, lands on Foyer. Restrained animation (simple fade between steps). Ship as soon as it works AND is verified in-browser (per LSATU hard verification gate). Polish passes are later. No showpiece motion in v1.

### Q16 — Name step
- Captured: **Keep current name step as step 0.** Existing `Onboarding.tsx` name capture ("What should we call you?") becomes step 0; the 6 reference steps follow. Name still required (name-not-username rule). Reuses working code — one continuous flow. Total = name + 6 = effectively 7 screens, progress bar spans the 6 reference steps.

### Q17 — OAuth path
- Captured: **Same gate for all signups.** Email/password AND Google OAuth both route to `/onboarding` on first entry when `onboarding_completed_at` is null. One path, no special-casing. Google users get name pre-filled from Google profile metadata (already done in current Onboarding.tsx via `user_metadata`).

### Q18 — Analytics
- Captured: **None in v1.** No per-step event tracking / funnel instrumentation. Stored answers + `onboarding_completed_at` are enough to see who finished. Funnel analytics is a later add if drop-off becomes a question.

### Q19 — Completeness backstop
- Captured: **Spec is complete.** Joshua confirmed nothing else to add — NOT choosing: editable-from-settings, copy/voice review, or explicit mobile-layout spec for v1. (These remain natural follow-ups but are out of v1 scope by his call. Note: teaching-voice copy pass on the 6 headlines/subtexts is a sensible pre-ship nicety but was not requested — leaving as optional.)

## Open flags (pending input)
(none — all resolved. Spec complete, ready to write.)
- Storage model for the 6 answers -> Joshua + code
- ~~Scope of "AI score recommendation from schools"~~ -> RESOLVED: cut, user types target themselves
