# LSAT U session lesson quality bar

The reviewed example is `brainstorms/2026-09-28-recap-format/07-quantity-statements-lesson.md` with `08-quantity-statements-visual-preview.html`. Inspect them when building a new lesson, then make a design that fits the new topic. The source is an example of depth and interaction, not a universal outline.

## What the reader experiences

- A title names the concept. The first sentence explains it in ordinary language.
- The first example makes the distinction visible before formal symbols or combined inferences appear.
- Each section teaches one move, asks a question, and explains the answer with a *different* example when possible.
- Visuals do reasoning work: a changing count reveals a threshold; a group diagram reveals an overlap; a counterexample shows why a proposed inference fails.
- The reader answers inline checks and a cumulative drill directly on the page. Feedback exposes the governing reason, not just a verdict.
- The page feels like one lesson, not a stack of uniform cards. Typography, space, restrained color, and motion guide attention without competing with the argument.
- Every image has meaningful alternative text; controls work by keyboard; motion can be reduced; mobile stays within the viewport.

## Reasoning review

For each claim, ask: Is it guaranteed by the premises, merely possible, or impossible? Try to construct the smallest counterexample. Check that a diagram shows the entire relevant universe and does not smuggle in existence. Keep changes of denominator, conditional direction, negation, and quantifier scope explicit when the topic uses them. A numerical example can illustrate a rule but cannot by itself prove the general inference.

## Produce it efficiently

Use the existing LSAT U preview shell and answer-check interaction as a starting point. Read the transcript once, make a short source map, and spend the saved time on the explanation and one visual that makes the central reasoning visible. Add further interaction only when changing a value, moving a group, or testing an answer teaches something that static prose cannot. A brief practice session still deserves a precise lesson, but its note can be short.

## Before handoff

- The session date, student, central mistake, and assigned work match the full transcript and current student record. Uncertain details are marked for review instead of filled in.
- The first sentence names the idea in ordinary language. A worked example shows why the method works. The note covers the relevant trap or boundary and ends with a fresh transfer question and explained answer.
- Every check accepts a student response and gives useful feedback. It does not claim to grade open-ended reasoning it cannot actually evaluate.
- Any diagram is logically accurate. The page has been opened at desktop and narrow widths; text, controls, and answers remain readable, keyboard usable, and compatible with reduced motion.
- The student recap is the primary record, with private continuation below its divider. The interactive preview and any reusable course lesson are linked from it. Report which files were made and whether anything was posted.

## Output boundary

Markdown is the editable teaching source. The student recap is the primary session record. Interactive HTML is a local review artifact until LSAT U supports its behavior in the app. Keep private continuation in the student's folder under `session-recap`; do not put private context into a reusable course lesson. Publication, assignment, and student messages are separate actions.
