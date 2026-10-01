# LSAT U session lesson quality bar

The reviewed example is `brainstorms/2026-09-28-recap-format/07-quantity-statements-lesson.md` with `08-quantity-statements-visual-preview.html`. Inspect them when building a new lesson, then make a design that fits the new topic. The source is an example of depth and interaction, not a universal outline or permission to teach its topic. Read [recap calibration](recap-calibration.md) on every run for the dated feedback behind these requirements.

## What the reader experiences

- A title names the concept. The first sentence explains it in ordinary language.
- Student-facing text never calls the material a "concept lesson" or exposes internal draft, production, or design labels. Name the reasoning being taught. Check the generated HTML opening as well as the editable source.
- The first example makes the distinction visible before formal symbols or combined inferences appear.
- Define the terms before relying on shorthand. A fact tells us what is true about a particular person, object or situation; a rule states what must follow if its condition is met. When describing an arrow's direction, name its starting condition and required result. Keep definitions and their examples together, with enough space to read each step; avoid a compact glossary followed by the same examples again.
- Each section teaches one move, asks a question, and explains the answer with a *different* example when possible.
- When several building blocks are involved, introduce the overall idea, teach each component's definition, example, guarantees and limits, then compare and combine them. Teach prerequisites before asking the reader to recognize a connection. Compare the reference's teaching sequence as well as its visual design.
- For fact/rule reasoning, explicitly define the role of each input and the result of each move. Applying a rule uses a matching fact to prove something about that person or object. Linking rules produces a new conditional relationship; it does not establish an existing case. Teach rules-only chaining separately from adding a fact to a chain. Explain positive, negative and inconclusive fact scenarios in readable prose before relying on an interactive selector. When a cited lecture explains a hidden match through contraposition, include that worked connection rather than merely naming the technique.
- Audit every sentence and diagram label for teaching value. Name the actual conditions, show the matching step, explain a reason, or give an executable task. Generic imperatives such as "Read each whole idea" and "Find what the statements guarantee" do not replace an explanation. When contrasting two methods, present numbered, visually separate scenarios with their inputs, outputs and reasons; do not bury the contrast in a bolded paragraph. Use a concrete opening example rather than an abstract statement about "information." Remove repetition once the example has done the teaching.
- Render reasoning notation as clear, bold teaching type with a real arrow and short meaningful phrases, such as **Submitted late → Requires approval**. Do not use single-letter conditions, including in feedback, selectors or diagrams. Do not put formulas into inline code boxes or decorative pills. Prefer open diagrams, alignment and connective lines over enclosing every idea in a rounded card; reserve containers for controls or a contrast they actually explain.
- When linking rules, show each given rule separately, highlight the complete matching condition, then reveal the new rule. Only add a fact in a separate demonstration. Number tempting invalid moves and distinguish the given rules, proposed conclusion and counterexample. Avoid unexplained phrases such as "adding a case" or "direction."
- Visuals do reasoning work: a changing count reveals a threshold; a group diagram reveals an overlap; a counterexample shows why a proposed inference fails.
- The reader answers inline checks and a cumulative drill directly on the page. Teach the idea before its quiz, or explain an introductory Socratic question immediately. Use fresh transfer examples. Feedback exposes the governing reason, not just a verdict.
- The page feels like one lesson, not a stack of uniform cards. Typography, space, restrained color, and motion guide attention without competing with the argument.
- When Joshua requests an expressive visual treatment, build a distinctive topic-specific design. Split the opening into clear teaching beats, make examples visible as facts, rules, and conclusions, and use color and motion to show the reasoning. Prediction quizzes should reveal why an answer follows. Do not treat a new palette on an unchanged prose layout as a redesign.
- Use topic-specific illustrations, depth, space and purposeful emphasis. Motion can trace a connection or highlight the decisive match; provide a pause control for ongoing animation and honor reduced motion. Do not replace an explanatory visual with decoration. Every image has meaningful alternative text; controls have visible keyboard focus; mobile stays within the viewport.

## Reasoning review

For each claim, ask: Is it guaranteed by the premises, merely possible, or impossible? Try to construct the smallest counterexample. Check that a diagram shows the entire relevant universe and does not smuggle in existence. Keep changes of denominator, conditional direction, negation, and quantifier scope explicit when the topic uses them. A numerical example can illustrate a rule but cannot by itself prove the general inference.

## Produce it efficiently

Use the existing LSAT U preview shell and answer-check interaction as a starting point. Read the transcript once, make a short source map, and spend the saved time on the explanation and one visual that makes the central reasoning visible. Add further interaction only when changing a value, moving a group, or testing an answer teaches something that static prose cannot. A brief practice session still deserves a precise lesson, but its note can be short.

## Before handoff

- The opening defines the reusable concept before any notation or original-question detail. Read it without the session transcript: the learner should know what the lesson teaches. A rejected question-centered draft is rebuilt into a coherent lesson, rather than supplemented by another block of prose.
- Compare the actual rendered page with the Some, Most, and All reference. The opening example, visual explanation, section hierarchy, nearby checks, and cumulative drill should work together. Confirm the page does more than repeat uniform text cards.

- The session date, student, central mistake, and assigned work match the full transcript and current student record. Uncertain details are marked for review instead of filled in.
- The first sentence names the idea in ordinary language. A worked example shows why the method works. The note covers the relevant trap or boundary and ends with a fresh transfer question and explained answer.
- Check source, inherited template content and every reachable HTML answer state against the selected scope. A facts-and-rules note must not inherit quantity exercises, "some applications" examples or some/most/all teaching unless Joshua explicitly includes quantity. Ordinary incidental uses of "some" are not a banned word. Keep the editable source and every rendered state consistent.
- Every check accepts a student response and gives useful feedback. It does not claim to grade open-ended reasoning it cannot actually evaluate.
- Any diagram is logically accurate. A new or changed design is checked at desktop and narrow widths; text, controls, and answers remain readable, keyboard usable, and compatible with reduced motion. A routine repost of a reviewed design needs the headless package and backend checks.
- The student recap is the primary record, with private continuation below its divider. The interactive preview and any reusable course lesson are linked from it. Report which files were made and whether anything was posted.

## Output boundary

Markdown is the editable teaching source. The student recap is the primary session record. Marked, self-contained interactive HTML can be assigned directly through the live Classroom renderer and local `lsat-u-lessons` MCP. Keep private continuation below the student-facing divider in the recap; do not put private context into a reusable course lesson. Publication, assignment, and student messages are separate actions.
