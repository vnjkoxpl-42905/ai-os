---
type: teaching-notes
subject: Pedagogical Flow Locked Rule
updated: 2026-07-17
aliases: []
---

# Pedagogical Flow — Locked Rule

**Permanent rule.** Carries across all 21 LSAT U topic builds, not just Main Conclusion. Saved in Claude's memory: see `memory_snapshot/lsat_u_pedagogical_flow.md`.

## The 6-step per-module flow

1. **Lesson first.** Conceptual teaching with the voice-led prose.
2. **Guided examples during the lesson.** Worked walkthroughs embedded inline in the teaching, not held back for a quiz.
3. **Small checkpoint questions after key concepts.** Quick recognition checks to reinforce understanding while the lesson is still fresh.
4. **End-of-module drill (calibration).** Question set drawn from the module's content. This is where the student first tests themselves on the material — *after* they've been taught it.
5. **Post-drill weakness profile.** Diagnostic generated from the end-of-module drill misses, not from a cold pre-test.
6. **Spaced repetition seeded from end-of-module misses.** Anki-style scheduling kicks in here.

## What this rules out

- **No cold-test diagnostic at app open.** No "take this 10-question test before you see any lessons." That demoralizes new students and produces noisy data.
- **No assessment as gating before teaching.** The student's path through a module is teach → practice with hindsight → calibrate, not test → study what you missed.

## What this enables

- **Calibration is genuine.** When the student gets a question wrong on the end-of-module drill, it's a real weakness — not a "I haven't been taught this yet" knowledge gap.
- **Spaced repetition is meaningful.** Items in the SR queue are real misses, post-instruction.
- **The recommendation engine has good data on session 1.** Not because of a pre-test (there is none), but because the student goes through Module 1 in their first session, and the M1 capstone produces useful signal immediately.
- **Onboarding is gentle.** New students aren't humiliated by failing a test on material they haven't seen.

## Module-by-module placement of the calibration drill

| Module | Capstone location |
|---|---|
| **M1 Lessons** | Lesson 1.13 (after Lessons 1.1-1.12 + checkpoints) |
| **M2 Reference** | No standalone capstone — Reference is a companion used during other modules' calibrations |
| **M3 Drills** | Each drill has its own Stage-Gate, so module-level capstone happens implicitly |
| **M4 Question Simulator + Trap Master** | The Simulator IS the calibration mechanic that all module capstones use |
| **M5 Reading Hard Sentences** | §5.8 capstone calibration drill |
| **M6 Diagnostics** | Doesn't need a calibration; it IS the diagnostic engine |

## The principle in one line

**The diagnostic engine never runs before instruction.** Calibration after teaching, not gatekeeping before it.

## Why this is a permanent rule

Joshua's directive 2026-04-29: "do not put the diagnostic at the beginning of v1. For Main Conclusion v1, the student should learn first, then answer questions at the end. The app should not cold-test the student before instruction."

This isn't a Main Conclusion-specific decision. It's a pedagogical principle that holds across every LSAT topic. The Skill that codifies this workflow defines the same per-module structure across all 21 topics.
