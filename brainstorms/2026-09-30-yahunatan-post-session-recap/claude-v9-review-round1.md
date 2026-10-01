# V9 first Claude review

I reviewed V9 statically. Its reasoning sequence and concept coverage match V8, and both V8 polish items are fixed: the definitions are now built from the source, and Practice 1 uses "Quinn". The page still has 7 inline checks and 4 mixed problems, each with worked reasoning, and the assigned work is unchanged. The three invalid moves are now numbered, each with a concrete counterexample. The new join demo keeps both rules fixed and matches the exact phrase "Requires special approval". It does not claim that an application exists. Its motion runs once per click and stops when motion is paused or reduced. The checks say plainly that answers are not graded. One material defect remains, which goes against user correction 6: the rendered HTML still shows a single-letter name, "J needs a signature.", in the TWO-OUTPUTS visual. The builder's guards miss it. There is also a keyboard-focus loss in the join demo. The remaining items are low-severity or optional.

## V9-1

The TWO-OUTPUTS visual in build-preview-v6.py:108 contains "<strong>J needs a signature.</strong>". The V9 cleanup at build-preview-v9.py:36-37 and :103 only replaces 'Application J', "J's" and 'about J'. The rendered HTML (line 23) therefore shows "Rules + This application's fact" above "<strong>J needs a signature.</strong>". This breaks user correction 6 (short descriptive phrases, not single letters) in section 05, the step that teaches adding a fact. The guards miss it: the rejected-string list has no 'J needs', and the regex at :112 only catches a capital letter followed by an arrow. The same visual also says 'Late → Needs a signature' while the surrounding text says 'Submitted late → … Needs a supervisor's signature', in the section that teaches exact matching.

Fix: Override p.base.VISUALS['TWO-OUTPUTS'] in V9. Use 'Submitted late → Needs a supervisor's signature' and 'This application needs a supervisor's signature.' Add a guard that rejects any standalone single capital letter used as a name in student text, for example re.search(r'(?<![\w.])[A-Z](?=\s|\'s|\.)', visible_text), excluding the pronoun 'I' and the start of a sentence. Alternatively, add 'J needs' and a general check against capital-letter names to the rejected list.

## V9-2

JS line 75: on the second activation, the click handler sets joinStep.hidden=true while that button has keyboard focus, then shows joinReplay. Hiding the focused element sends focus to the document body. A keyboard or screen-reader user who presses Enter on 'Show the new rule' loses their place just as the new rule appears. They must tab again from the top of the page or the previous focus point. The plan asks for keyboard controls to be checked.

Fix: After revealing the result, call joinReplay.focus(). Alternatively, give #join-result tabindex="-1" and focus it, as the check and quiz feedback already do.

## V9-3

build-preview-v6.py:83 shows the same verdict for every quiz: 'Correct. The direction matters.' The quiz V9 keeps, POP-QUIZ-2 in section 06 #2, is about a shared starting condition, not arrow direction. So a student who answers correctly sees a reason that does not apply. User correction 5 asks for better feedback design, and the quality bar says feedback should expose the governing reason.

Fix: Use a verdict for each quiz, for example from a data-verdict attribute. For quiz 2: 'Correct. A shared starting condition does not connect the two results.'

## V9-4

Section 04 states the answer before the interaction. Line 95 ('Match: "Requires special approval" is the result of the first rule…') comes before <!-- JOIN-RULES -->, and the demo's first button then asks the student to 'Show the matching condition'. The demo repeats prose the student has just read instead of letting them find the match, which weakens the 'show, then connect' sequence the user asked for in correction 2.

Fix: Move the Match paragraph after the JOIN-RULES block, or delete it and let the demo's status text and the 'Why' paragraph carry the explanation.

## V9-5

The same rule is shortened two different ways. Lines 57 and 125 use 'Is trained → Has a badge', while lines 177, 191 and 252 use 'Trained → Has a badge'. Section 06 #1 (line 125) is labelled 'Given rules:' but gives one rule written twice. The lesson asks students to match complete conditions exactly, so inconsistent shorthand for one condition is a small mixed signal.

Fix: Use one form throughout, for example 'Is trained → Has a badge'. Change the label at line 125 to 'Given rule:'.

## Limits

- Static review only. I did not render the page or test it in a browser, so layout, contrast, the 390-1600px widths, the actual motion, focus behaviour and screen-reader output are unverified. The PNG screenshots in research/ were not inspected.
- I did not run the builder, any tests, a JavaScript syntax check or a publish dry-run. I also did not compute SHA256 hashes, so I cannot confirm that the HTML was built from this exact source and builder. Spot greps are consistent with it.
- The HTML is minified onto a few long lines and was checked only through targeted greps, not compared line by line with the source.
- I did not read SKILL.md, wiki/teaching-voice.md or the Some/Most/All reference lesson 07 in full. Voice was judged against COPY-CORRECTIONS.md and the quality bar.
- I did not check the canonical student recap for a V9 block. The V9 builder reads concept-lesson-v9.md directly.
- Optional preference, not a defect: V9 turns each chapter into a white rounded panel and adds tinted rounded boxes for the reasoning steps. The quality bar warns against a 'stack of uniform cards', so the visual judgement needs a live check. The fact explorer's continuous signal and pulse animations, kept from V8 at the user's request, loop until paused.