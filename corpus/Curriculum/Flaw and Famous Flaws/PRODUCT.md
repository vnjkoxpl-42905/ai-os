---
type: teaching-notes
subject: Product
updated: 2026-07-17
aliases: []
---

# Product

## Register

product

## Users

LSAT students across three cohorts, with the bootcamp centered on the second:

- **First-timers** in mid-prep, scoring 150s, hitting Flaw questions cold.
- **Stuck retakers** in the 160–165 plateau where Flaw is leaking 2–4 points per LR section. *Primary design target.* They have prior knowledge but it's miscalibrated.
- **Late-stage 170+** students hunting the last few misses on hard Flaw items.

Context of use: long study sessions, often hours at a time, on a laptop or tablet. Many are studying tired, evenings after work or late at night. Many have seen other LSAT prep and arrive skeptical of dressed-up edtech.

Job to be done: stop missing Flaw questions by learning to read arguments hostilely, formulate the right objection, classify the answer-language, and trap-spot — all under timed conditions. Bootcamp is the intensive 7-day path to that calibration.

## Product Purpose

A 7-day intensive bootcamp module within the larger LSAT U "Flaw and Famous Flaws" curriculum. Teaches the procedural lens for Flaw questions through escalating daily lessons, woven mid-day reps, and end-of-day calibration drills.

Runs as a parallel track alongside the self-paced approach + catalog + drill suite. Student picks one path or the other; both should land the student in the same calibrated end state.

Success = **≥80% accuracy on the Day 7 live-fire calibration drill.** That single metric is the contract. Misses from that drill seed the spaced-repetition queue that follows the student into subsequent weeks.

## Brand Personality

**Coach · scholar · operator.**

- **Coach** — pushes hard, names what you're doing wrong, doesn't soften the verdict. Sets the day's task and expects you to clear it. Earned warmth, not default warmth.
- **Scholar** — precise about the underlying logic, names tools as proper nouns (Logical Hostility, the Three Languages, the Five Fast Eliminators), respects the student's intelligence by refusing to dumb down the formal moves.
- **Operator** — mechanical about the protocol. When the move is "make X false, ask if the argument crashes," it says exactly that. No vibes, no fluff. Procedure is the point.

The voice runs in two registers and switches between them mid-passage:
- **Decisive** for protocols, drill instructions, verdicts. Imperative, mono-set, courtroom-flat.
- **Whimsical** for metaphor and example. Cake on blocks, "Objection, Your Honor, Dr. Stupid just did this," parodied stimulus authors, parenthetical asides, mid-prose ALL-CAPS for emphasis.

## Anti-references

What this should explicitly NOT feel like:

- **PowerScore Bibles and similar textbook-density LSAT prep.** The primary anti-reference. Wall-of-text density without interactive payoff. The student reads, nods, closes the book, and remembers nothing. We earn every interaction with a teaching beat.
- **Generic edtech (Khan Academy, Magoosh).** Cheery dopamine framing, friendly mascots, badge-and-streak gamification. Treating adult students like middle-schoolers. We don't congratulate. We calibrate.
- **Duolingo-style guilt loops.** Push-notification streak guilt, character mascots, ruthless gamification disguised as encouragement. We never shame absence. The bootcamp is intensive but the student remains a competent adult.
- **Consumer-SaaS dashboard chrome.** Card grids of sameness, "hero metric · supporting stat · gradient accent" templates, generic onboarding tours. The surface should read editorial-print first, app second.

## Design Principles

1. **Calibrate, never gatekeep.** End-of-day drills exist to surface what to drill again, not to lock the student out of tomorrow. Verdict screens read as readouts, not pass/fail walls. We never say "you failed."
2. **Every interaction earns its teaching beat.** Animations, drag-drops, classifiers — each one has to make a point the student couldn't get from prose. If a UI flourish doesn't teach, it doesn't ship. Cake on Blocks is the bar.
3. **Procedural over inspirational.** When the answer is "run this protocol," show the protocol. No motivational filler. The student trusts the work because the work is specific.
4. **Two-register voice held in tension.** Decisive protocols sit next to whimsical metaphors on the same page, on purpose. Flattening either register flattens the lesson. The Coach voice and the Scholar voice take turns; the Operator voice stays in the box that says "Protocol."
5. **Reading is the workload.** These students read for hours. Type, contrast, line length, and rhythm get treated as load-bearing infrastructure, not decoration. A long passage that feels easy to read is doing real work.

## Accessibility & Inclusion

- WCAG 2.2 AAA contrast across all text. Default ink-on-paper measures 12.3:1. Verdigris on cream measures 7.4:1. No exceptions for "decorative" text.
- **High-contrast mode** as a first-class user toggle — pushes ink to near-black on near-white, drops the grain overlay, and removes paper warmth. Persists in localStorage. Not buried in settings; surfaced in the masthead.
- `prefers-reduced-motion` respected everywhere. Cake-on-Blocks animation collapses to a fade. Drag-drop drills fall back to click-to-select.
- Keyboard navigation across all drill flows. Verdict screens, gates, and reveal-answer toggles reachable by Tab + Enter.
- Mobile responsive but laptop/tablet first. The bootcamp's primary read surface is a 13-inch laptop in a study session.
- Body line length capped at ~70ch. Display headlines uncapped.
- No autoplay video, no autoplay audio, no surprise modals. Modals are reserved for genuine confirmation moments and never as a first thought.
