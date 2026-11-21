# Copy corrections

Every student-facing wording fix, with the reason it was wrong. Read this before
writing or editing copy for LSAT U so the same mistake is not made twice.

Companion to [[teaching-voice]], which says how the writing should sound. This
says what has actually gone wrong and why.

Started 2026-09-07 from a Read, Recall, Colour pass. Add to it every time a
correction is made.

## The rules these corrections came from

Three rules already existed and all three leaked anyway, because each was
enforced on the components that happened to exist when it was written. A surface
added later starts uncovered.

- **No em dashes, ever.** [[teaching-voice]], Core voice.
- **No internal vocabulary in student copy.** `projects/lsatu/src/features/activity-centre/CONTEXT.md`
  carries the glossary and marks what to avoid.
- **Every CSS token a stylesheet uses must be defined in it.** `projects/lsatu/CLAUDE.md`.

Guards now live with the content rather than with each component:
`content/instructions-voice.test.ts` checks the authored instructions, so every
surface that renders them is covered, including surfaces not written yet.

## Corrections

### Student notes name the task, not the internal design (2026-10-25)

Joshua rejected "Session Manual" in Ore's recap header. **Manual must not appear in student-facing copy**, including headings, browser titles, labels and hidden answers. Use "Session recap" for a recap, "Before you start" for a drill primer, and "Reference" for a method page. Historical design names and asset filenames can remain private. Keep the approved layout; change the wording. Check generated HTML as well as sources and sync the current student-facing Markdown.

### Contrapositive and arrow lessons: cut the sophistry (2026-10-11)

Joshua rejected the first contrapositive lesson as 'terribly done' and then rejected the rewrite for 'a lot of sophistry'. Rules from the two rounds:

- **Say what it is first, in plain words, before any example.** Name the idea, say what it states, then show it. The contrapositive is the **same rule said a different way**. The two are **logically equivalent**: if one is true, the other is true, and you can use either. Lead with that. Source: his own teaching, [[contrapositive-teaching]].
- **No metaphor-of-obligation language.** Never write that a rule 'makes a promise', that the left side 'depends on' the right, or that it has 'nothing to stand on'. Say what is true and why, in the plainest reasoning: if the left side had happened, the right side would have come with it.
- **Keep it natural, intuitive and personable.** Contractions, short sentences, a teacher thinking next to the student. No lecture-hall phrasing. If a sentence sounds like it is trying to sound wise, cut it.
- **Name the lesson by its topic.** 'Contrapositive', not 'Write and read the contrapositive'.
- **A lesson explains before it drills.** Order for a concept lesson: what it is, see it work, how to do it, what it is not, the steps in short, why it matters. Do not open with an example or a question.
- **Must arrow note must say:** what the arrow says, where to start reading (the left), and what the arrow is for. Not just which side is sufficient.
- **A card front asks the question, the back gives the answer first.** The answer is the large line. Be specific: 'Can you read a rule from right to left?', not 'Can you reverse the arrow?'. Never 'the other one'.
- **Fix the vague word, not the sentence.** 'Reverse' and 'the other one' were both rejected as not specific. Say what the student actually does or what the condition actually is.
- **Never call the contrapositive 'the one other thing' a rule tells you.** Joshua (2026-10-11): it is not the only other thing you know. Say the two are equivalent and interchangeable: know one, you know the other. Do not claim a closed list of what else is known.
- **Do not use the raffle (win the raffle, get a bicycle) as the example in new contrapositive or arrow material.** Pick a fresh everyday example for each lesson. The contrapositive note now uses an elevator: if it is moving, its doors are closed. The older course text still uses the raffle; replace it as those lessons are revisited.
- **Contrapositive lesson (Joshua, 2026-10-11, final): no thought experiment, no guess box, no flip card.** An earlier coat-and-guess card confused him ('I don't know what you did about that coat example'). Follow the source HTML's explanation of the contrapositive directly, in close language, improving only where it can be made clearer: recap the rule, define it up front (if the necessary condition is absent, the sufficient condition is absent too), one first-person example, 'found within the original, waiting to be recognized', logically equivalent and interchangeable, four-situations table, write it with the squiggle and flip and negate, what it is not, read it don't always write it, why it matters. Do not use the source's own examples (coffee, breathing/air). Current example: ceiling light and power.
- **Say 'left side of the arrow' and 'right side of the arrow'** in explanations of the arrow and the contrapositive.
- **Never mention Logic Games.** Only LR and RC exist.
- **Source cautions are good, keep them:** do not say the rule and its contrapositive are 'all you know', and do not say to 'ignore the conditional'. Say the rule settles nothing in the other two situations.
- **Say 'must', not just 'is', in a rule's necessary side (Joshua, 2026-10-11):** 'If the ceiling light is on, then the power MUST be on.' The must is the point of the arrow.
- **'Foreign' is an awkward word** ('it isn't some foreign process'). Use plain, personable phrasing in his Intro to LR voice: a plain claim, a contrast, short stacked landings ('No power, no light.'), 'Here's the thing', direct 'you', contractions, dry wit.
- **Emphasis may be a little louder in the contrapositive lesson:** a slightly cheeky exclamation on the key word ('They're interchangeable!') with a one-time punch-in and glow, plus 'Can't happen!' on the forbidden case. Main Conclusion copy has no exclamation marks in teaching text, so keep them to one or two per lesson.
- **Bring lessons to life, but let motion carry the reasoning:** pulse, glow, a punch on the key word, sides that swap and a 'not' that pops on, toggles that show the four situations. Every animation needs a still, readable equivalent and must stop under reduced motion. Existing pieces to reuse: DrillDemo, HypotheticalFigure (data-in-view), SufficientConditionExperience, indicator-word-deck flip card.
- **Never show negation as a squiggle (~) beside an idea (Joshua, 2026-10-11, 'never').** Negation is either the word 'not' or a strikethrough line drawn through the idea itself. Applies to every lesson, diagram, drill and animation. Fixed so far: the contrapositive note and its flip-and-negate animation. Still using ~: reference sequence diagrams, sign patterns, worksheet drills and symbol answers (see the next fix pass).
- **Negation line runs diagonally from the idea's top left corner to its bottom right corner (Joshua, 2026-10-11).** Use it in written lines and tables as well as animations, not only boxes. Also write the contrapositive out as a plain-English sentence early in the explanation.
- **No squiggle anywhere, answer choices included (Joshua, 2026-10-12).** He still saw ~ in the multiple-choice options and the reference practice below the lesson. Every ~ in a string is rendered through the Notation component so it draws as the struck idea; a test now fails if ~ appears on the contrapositive page. Check practice buttons and answer keys, not only lesson prose.
- **Wrong must look wrong (Joshua, 2026-10-12).** Reverse and inverse are shown as red cards with an X badge and the word "Wrong", beside one green "Right" card for the contrapositive. Do not put wrong and right in the same plain table. Also: no repeated content on a page (the light and power sentences were said three times), and visuals must look sleek and high end.
- **Questions must be unmistakable; no pale green; no broken sentences; every line earns its place (Joshua, 2026-10-12).** The "what the rule tells you" interactive did not make clear what it was asking. Now: a navy panel, a "Your turn" tag, the rule, and one big question ("Which ONE of these four worlds can't happen?"), with four tappable worlds. Colour carries meaning (amber = sufficient idea, teal = necessary idea, and the colour travels with the idea when sides flip). Sentences are never split with line breaks or orphaned (balanced wrapping, one card per sentence). "Logically equivalent" pulses. Cut anything that restates what the page already said (the 4-row table, the raffle recap, the second plain-English line, the repeated light-and-power blockquote). End the lesson with checks that test use of the idea, including one that tests the reverse trap.
- **Interactive steps say what to click (Joshua, 2026-10-12).** Label them "Step 1. Click here to ..." and "Step 2. Click here to ...", not "Next step" / "Play it again". The student drives; nothing autoplays. The next step to click glows to invite the click.
- **Show the rule, do not just diagram it (Joshua, 2026-10-12).** The original and contrapositive are two tabs on one stage with a real light bulb and switches. Original tab: flip the light switch on and the power node is forced on. Contrapositive tab: cut the power and the bulb is blocked; "Try the light switch anyway" does nothing. Concept pairs get something to operate, not a static pair of boxes.
- **Simple beats clever (Joshua, 2026-10-12).** The first light bulb stage had a diagram row, sentence, two icon boxes, a wire, state chips, a switch, a bonus button and a message. He called it too complicated and messy. Rule: one idea per interactive, one control, one sentence. The tab itself carries the diagram; two plain lamps show the state; no wires, chips or extra buttons.
- **Raffle retired from the contrapositive page (2026-10-12).** The "Try the four patterns" practice used the raffle. It now has four fresh rules, one per place a "not" can sit (guest list and wristband, shop and shutters, gate and dog, stamped ticket), with reasoned feedback that names the reverse and the inverse. The raffle and bicycle still run through the earlier reference steps, the opening lessons, the media and the shared foundations source (about 300 mentions); those need their own pass and the generated bundle rebuilt.
- **Never say "patterns" or "move" to students (Joshua, 2026-10-12).** Both read as awkward jargon. Say "four rules", "try it on", "change", "flip the sides". Practice questions get the same visual quality as the rest of the page: one rule at a time on the navy panel, colour-coded idea pills, large answer tiles, instant reasoned feedback, progress dots. The weakest-looking part of a page gets rebuilt, not patched.
- **Words:** 'Correct', not 'Right', on a correct answer. Bold the word 'if' where the point is that the rule says what follows *if* something is true.

- **Contrapositive page approved as the gold standard (Joshua, 2026-10-12).** Full do and don't list, page shape and build process live in `.claude/skills/bootcamp-builder/references/teaching-preferences.md` under "Gold standard". New rules from the last pass: cut whole sections when a page is too long; one main example plus one fresh simple example, never repeated; show rule and result as if-then sentences; quiz ideas are short phrases, not letters; quiz explanations are one sentence (right answer) or "Not that one." plus one specific reason (wrong answer); no paragraph or tag line before a quiz; the quiz title is just "Pop Quiz", centered, with an effect not used elsewhere on the page.

Still to reconcile (found 2026-10-11, not Joshua decisions): 'establish' is banned below but his approved necessary copy uses it; the raffle was approved for the opening and later rejected as the sufficient anchor; see `.claude/skills/bootcamp-builder/references/teaching-preferences.md`.

### Conditional opening: define the words before using them (2026-10-03)

Joshua's marked browser paragraphs used “direction” and “guarantee” before making their meaning clear. The purpose paragraph also described an argument accepting more than its information supports without showing what that meant. Teach what a rule lets you conclude in plain language, then attach the vocabulary to a concrete relationship. Explain sufficient as enough and necessary as required before relying on those roles. Show what the must-arrow records and why English clause order does not determine the two sides.

2026-10-03 clarification: explicitly distinguish the indicator from the complete condition it refers to. Sufficient goes left; necessary goes right. The indicator itself is not a condition in the diagram. Show the same relationship with if at the beginning and in the middle, and show necessary targets both before and after requirement language. Neither sentence position nor the words immediately following the indicator determine placement. Preserve if versus only if as different complete expressions.

A rule describes what would follow **if** a condition were true; it does not say that condition happened. Bold that “if” and use meaningful in-view motion to expose the connection, with a static reduced-motion equivalent. Replace compressed ready-order wording with a natural full sentence. Give each paragraph and interaction a specific teaching job. These corrections supplement the canonical voice standard rather than adding a new writing register.

### Generic reasoning prompts → concrete numbered demonstrations (2026-09-30)

Joshua marked four parts of the V6 opening: "Read each whole idea," "Find what the statements guarantee," the abstract first sentence about information, and the paragraph combining application and linking. They named goals without showing a useful action or explanation. Replace them with numbered, separate scenarios. Show the fact and rule that prove a conclusion about one case; separately show two matching rules and their new conditional conclusion. Labels should identify actual inputs or outputs. Review the whole note for repeated umbrella instructions and make task instructions executable. This follows the teaching voice: specific, concrete, short sentences, with air between distinct ideas.

### Fact and rule definitions must explain the inference (2026-09-30)

Joshua rejected definitions that remained abstract and an explanation that did not clearly distinguish applying a rule from linking rules. Define the inputs with examples, then show the matching step and exact output. A case fact plus a rule proves something about that case. Two connecting rules produce another conditional rule without establishing a case exists. Adding a fact to the chain is a separate step. Explain all four fact situations and a hidden chain revealed by contraposition rather than leaving them implicit in an interactive model. Rules include general logical relationships, not only policies or obligations.

### Boxed `L -> R` → bold teaching notation **L → R** (2026-09-30)

Joshua rejected the recap's small monospace arrow inside a pale code box. It looked like implementation text and weakened the explanation. Use a real, clearly weighted arrow in ordinary teaching typography. Explain its complete conditions before shortening them. The Some, Most, and All reference also governs the progression: introduce the whole idea, develop the individual components, then compare and combine them. A visual refresh must review that sequence, not only colors and boxes.

### "Concept lesson" → the actual reasoning title (2026-09-30)

The recap preview exposed an internal label above the student lesson. Joshua explicitly rejected it. Use a title such as "Facts, Rules, and What Follows" and headings that teach the reasoning. Keep production labels, version metadata, and design commentary in private records. Check the rendered HTML, since its shell can introduce wording absent from the Markdown source.

### "Recall Rephrase Colour" → "Read, Recall, Colour"
The door's heading was hardcoded to a name the product does not have, one line
under a chip reading "Read, Recall, Colour". "Rephrase" belongs to a different
Activity, Conditional Rephrase. A test asserted the wrong name, which is why
2,600 passing tests never caught it.
**Lesson:** when a test pins a string, check the string is right, not just that
it matches.

### "Intake only. Nothing comes back out yet…" → plain instruction
Clinical and abstract, and the sentence then told her to read "with full
intonation" while step one is silent reading. The clause that made intonation
internal, "hear it naturally in your head", had been dropped in an earlier edit.
**Lesson:** a word like "intake" reads as jargon. And when copy is trimmed,
check what the trimmed clause was load-bearing for.

### "Three beats through the stimulus" → "Three steps"
"Beat" is the internal code name for one of the four method steps. The glossary
says students see **step**. The interface ten pixels below labelled the same four
things Step 1 to Step 4, so the page used two names for one thing.
**Lesson:** never let an implementation name reach the page.

### "22 pieces to read" → line removed
A **piece** is one chunk, roughly a sentence, and the instructions on that same
page use the word that way. The count was of stimuli, so "22 pieces" read as 22
sentences.
**Lesson:** a unit word must mean one thing per surface. Check what a word
already means on the page before reusing it.

### "say it back" → "tell it back", "The Read" → "The Recall"
The library door still carried both retired names. "The Read" was step four's
former name and collided with step one, which is why it was renamed.
**Lesson:** a rename is not finished until every row carries it. The door was
stale for months because it is a different database row from the sections.

### "then a fourth" → "then a fourth step"
The noun sat three words back and the reader had to carry it.

### "once you have got all of it" → "once you have read all of it"
Ambiguous between having read it and having remembered it, in the one clause
that triggers step four.
**Lesson:** precision matters most where the sentence is an instruction.

### The three-fact notice → one fact
"Nothing is recording yet, the microphone opens on Start, and the section
records in one take that you cannot pause." Two of those are said again in step
four and in the long version, so she skipped the paragraph.
**Lesson:** say it once, in the place it matters.

### The method, told twice → the long version collapsed
The page rendered four numbered steps and then the whole written briefing saying
the same thing at length, both open. She read the method twice and could not
tell which one to follow.
**Lesson:** two explanations of one thing is worse than either alone.

### "PT105.S1 · 24 stimuli · about 25 min" → removed
The section was already the second line of the title. The clock is at the foot
and in the long version. The stimulus count measured the work in a unit she has
no feel for.
**Lesson:** delete a line that repeats what is above it. Do not reword it.

## Booking emails: hand over the link, not the pass settings (2026-09-08)

**Cut:** "70 minutes each, and no expiration date, so there's no rush to use them."
**Keep:** "You're set up on LSAT U with 10 sessions."

Session length and expiry are admin fields. The student sees them on the booking
page when she picks a time, so putting them in the email is detail she did not ask
for and has to read past to reach the link. The credit count is worth saying because
it tells her how much she has. Everything else about the pass stays in the backend.

**Lesson:** in a booking email, say who it's for, how many sessions, and the link.
Stop there.

## Drill hub: say what the button does, not what the feature is called (2026-09-09)

Six changes on `/classroom/drill`, from the run-3 pass. The hub named its own
features, and it assumed the student had rejected something.

| Was | Now |
|---|---|
| "Start Smart Drill" | "Practice your weakest types" |
| "Start One Passage" | "Read one passage" |
| "Start a Smart Drill instead" | "Or practice your weakest types" |
| "Read one passage instead" | "Or read one passage now" |
| "Open analytics" | "See where you lose points" |
| "Open journal" | "Review your missed questions" |

"Smart Drill" is the product's internal name for the adaptive set. On a button it
asks the student to guess what she is about to get. The sentence above the button
still names it, which is where a product name belongs: after the thing has been
explained, not as the explanation.

"Instead" was the worse one. It tells the student she has just declined the
assigned work by reading past it. She has not. "Or" offers a second path without
narrating a decision she never made.

"Open analytics" and "Open journal" name a screen. A student does not want
analytics, she wants to know where the points are going.

The fallback paragraph lost "an adaptive set that follows your weakest question
types" for "the question types you miss most": the same fact, without the product
vocabulary.

**Lesson:** a button says what happens next, in the student's words. Feature names
belong in the sentence that explains them, never on the control.

## Words never to use in student copy

From the glossary. Internal names may stay in code, never on the page.

| Never | Use instead |
|---|---|
| manual, Session Manual | Session recap, Before you start, Reference, or the actual topic. Added 2026-10-25: internal design terminology does not belong in student-facing notes or browser titles |
| Recognition drill | Do not show this internal teaching/design label to students. Use the actual task, such as Negate it, or omit the extra label. Added 2026-10-25 by Joshua |
| candidate assumption | An answer you are considering. Joshua rejected the former phrasing in the Yahunatan recap,2026-10-25 |
| two complete conditions | Explain the two ideas through the actual example. Joshua rejected the abstract instruction,2026-10-25 |
| grammatical shape | Explain the meaning being tested; do not use this label in student notes. Joshua correction,2026-10-25 |
| beat, beats | step |
| chunk | piece |
| intake | plain instruction |
| briefing, phase, tab, card | the thing's own name |
| say it back | tell it back |
| The Read | The Recall |
| Recall Rephrase Colour | Read, Recall, Colour |
| em dash, en dash | a full stop, or a colon before a list |
| expression ("Which expression identifies...") | "indicators" for the taught words, "phrase" for a multi-word indicator read as one unit ("read only if as one phrase"), "idea" or "condition" for what it points to. Added 2026-10-11: "expression" is vague and stiff; the student is looking for an indicator, so name it and reinforce the term being taught |
| statement ("Statement 1 of 7") | sentence. Added 2026-10-11: students read sentences; "statement" sounds like a logic textbook |
| Practise / "N statements" on drill cards | say what the drill has the student do. Added 2026-10-11 |
| establish ("enough to establish") | prove, or tells you. Added 2026-10-11: plainer; keep "guarantee", it is plain and sticks |
| preserve ("preserves the rule") | keeps. Added 2026-10-11 |
| relationship (when a rule is meant) | rule. Added 2026-10-11 |
| stipulated | this rule. Added 2026-10-11 |
| classify | sort. Added 2026-10-11 |
| "That keeps the meaning." on every correct step | name what was right: "Right indicator.", "Right direction."; wrong: "Not quite. Try again." Added 2026-10-11 |
| Personalized If/Then | Put yourself in it. Added 2026-10-11: names what the student does, not a feature |
| target ("the sufficient target") | what it points to, or the group. Added 2026-10-11; "target" stays in code |
| the model ("compare with the model") | our version. Added 2026-10-11 |
| "has to be true for it" (legend) | "required for the result". Added 2026-10-11: "it" had nothing to refer to; every label must make sense on its own |
| wrong-answer feedback that explains the right answer | a hint about why the chosen answer fails ("“only if” introduces what is required, not what is enough"). Added 2026-10-11: the explanation gave the answer away |
| "Build the arrow" | "Build the diagram". Added 2026-10-11: the student builds a diagram; the arrow is one symbol in it |
| "Select the words that signal the rule" | "Select the conditional indicator." Added 2026-10-11: name the thing the student is looking for |
| "28 sentences", "Sentence 1 of 28", "Next sentence" | questions: "28 questions", "Question 1 of 28", "Next question". Added 2026-10-11: a sentence is not the unit of a drill and reads unprofessional |
| "Drill 1" as a title | the task itself, e.g. "Spot the condition". Added 2026-10-11: a number says nothing about the reasoning |
| "a rule makes a promise", "depends on", "nothing to stand on", "the other one" | say what is true and why, in plain words. Added 2026-10-11: reads as sophistry; vague words like "the other one" point at nothing |
| "Right." on a correct answer | "Correct." Added 2026-10-11 |

**Before designing any new homework, bootcamp, drill or note, read this table.** When a
word is rejected in review, add it here first, with the reason, then fix the copy.

## Conditional Rephrase: name the student action, not the internal model (2026-09-15)

**Cut:** “record the route,” “choose the route,” and a map presented as five rules.

**Keep:** diagram the statement on paper, choose the matching diagram, and organize
the map into four groups. “Required means right” is a separate takeaway because it
explains placement; it is not a fifth group.

“Route” described the system’s representation, not the student’s work. Calling five
unlike ideas rules also flattened the teaching structure and made the layout harder to
read.

**Lesson:** name the action the student can see herself doing. Do not force a teaching
reminder into the same hierarchy as the categories it explains.

Related: [[teaching-voice]] · [[ASSIGN-AN-ACTIVITY]] · [[STUDENT-PLATFORM-IDENTITY-MAP]]

## Session recaps: write a reusable reference, not a play-by-play (2026-09-12)

**Cut:** an opener saying the student got two questions right, followed by a summary of
which answer they chose and how they explained it.

**Keep:** the concept the student needs tomorrow, a visual model of the reasoning, a
short diagnostic check, and the exact practice they need to complete.

A student will not remember an isolated answer-choice exchange a day later, and the
exchange is not useful unless it demonstrates a reusable rule. A recap should read like
a compact study note, not a record of the conversation. Name a question only when the
details make the concept easier to apply. Praise belongs only when it identifies a
durable skill or meaningful change, not merely that an answer was correct.

**Lesson:** organize the recap around what the student can use next. Lead with the
concept, show the logic clearly, and finish with tangible practice.

### A rule is not a fact (2026-09-12)

**Cut:** describing a conditional Must Be True lesson as “applying a rule to a fact”
without checking whether the stimulus supplied a fact at all.

**Keep:** a fact is an asserted true case or condition. A rule is a general conditional
relationship. It tells you what follows if its trigger is present, but it does not say
that the trigger occurred. Some stimuli contain rules only, so the work is to chain
them. When a fact is present, apply a matching rule or a valid contrapositive.

**Lesson:** label the role of each sentence before explaining the inference. Never
invent a fact to make a rule fire.

### A post-session note is lecture material, not an email (2026-09-12)

**Cut:** a greeting, a dated recap heading, references to a question the student is
expected to remember, and a sign-off.

**Keep:** a concept title, a clear opening distinction, numbered procedures, spaced
examples, and practice that uses the lesson.

**Lesson:** the note should remain useful when the session itself is no longer fresh.
It must teach from the page instead of relying on remembered context.

The concept should not arrive as an abrupt list. Begin with a short explanation of
why the distinction matters, show the full method at a glance, and then teach each
path in the same order. Use tables for comparisons and numbered headings for a
procedure so the student can see the structure before reading the detail.

### Define the concept in Joshua's language (2026-09-28)

**Cut:** “Some, most, and all tell you how much of a group fits a description.”

**Keep:** “Some means at least one. Most means more than half. All means every one,”
grounded in a concrete set of ten cookies before drawing conclusions from the words.

The cut line is vague and does not sound like Joshua teaching. It makes the reader
decode “fits a description” before learning any of the three words. It also risks
blurring the difference between a count that is possible and one that is guaranteed.

**Lesson:** open with the actual distinction or definition Joshua taught. Use a
concrete example to show what each statement proves, then introduce notation and
the inferences. Do not write an abstract umbrella sentence merely to announce the
topic.


### Reference quality does not authorize reference topics (2026-09-30)

Joshua requested the Some, Most, and All note as a teaching-flow and visual-quality reference. Quantity examples and exercises do not belong in the separate facts/rules note. Remove that off-topic material; retain the distinction between what a rule says and what a fact establishes. Before future recaps, read the accumulated corrections in the Post Session Recap skill's `references/recap-calibration.md`. Preserve source-driven scope while matching the reference's teaching quality.

### Conditional practice: explain the decision instead of naming the operation (2026-10-07)

Joshua rejected “same rule, different words,” “equivalent-rule comparison,” “find the requirement, then place it,” “work through the expressions below,” “first choose the complete target,” “read the whole idea,” and “sentence X of Y” when these stood in for a useful explanation or made the drill feel like a collection of labeled sections. “Complete target” and similar terminology should not carry a beginner's instructions without a concrete meaning attached.

The revised local copy asks what the learner needs to decide: “Who does the rule say will receive a wristband?”, “What kind of key is needed to open the cabinet?”, and “What kind of pass does entry require?” The lesson demonstrates why before noon, current, registered and with yellow tags matter. Dropping one of those words changes which cases the rule covers. An arrow is checked by imagining its left condition and asking what the sentence then establishes, rather than treating the first English clause as the left side.

Joshua also asked for the mixed drill to train a skill and build a habit, with one question visible and a progress bar. The current local response uses five stages with a concrete purpose for each: retain the full conditions, build a diagram, attempt a translation before supplied labels, compare meanings, then transfer to unfamiliar cases. Error feedback distinguishes dropped qualifications, reversed roles, required versus enough and changed meaning. A fresh question checks the repaired distinction; correcting the exposed answer alone does not demonstrate transfer. Written translations are compared by the learner and are not represented as automatically graded.

Keep modality in the examples. An electric vehicle that is denied permission disproves the claim that being electric guarantees permission; a vehicle merely staying outside does not. A required action is an obligation, not a fact proving compliance. Confirmation practice for that mistake must test another obligation rather than an unrelated wording comparison.

These are demonstrated corrections and the current implementation response, not approval of every exact replacement sentence or proof that the voice matches Joshua identically. The [selected voice standard](../references/lsat-teaching-voice-standard.md) still governs wording, cadence, concrete reasoning and scope. [Current session record](log.md) distinguishes local work from publication.

Further steering in the same session: “Keep the complete condition” was itself awkward as a visible heading. Ask who or what the particular rule covers instead. Joshua also rejected the landing page's total question/stage counts, per-stage counts, long stage list and padded explanation of repairs. A shorter launch should explain the immediate task; each stage should introduce its purpose and instructions when the learner reaches it. That latest flow revision was requested while final verification was still pending, so this record does not certify its implementation.


### RC actions should describe what the student gets (2026-10-07)

Joshua rejected Inspect set as unclear and awkward. Use Preview drill for viewing the exact selected passages and questions before starting. Keep Start this drill distinct and explain whether answers are hidden and whether work is saved. Generic Menu is also insufficient where the actual action is Question details. This correction does not justify adding more launch instructions, repeated summaries, or unrelated assigned work inside RC setup.



### Unless: choose either idea (2026-10-12)

Joshua rejected "Find the idea that is not attached to unless." Teach the Group 3 move as: choose either idea, negate it, put it on the left; take the other idea and put it on the right exactly as written. Do not single out which idea to pick. His answer key happens to negate the non-unless idea; choosing the other gives the contrapositive, which is also correct. Applied in the LSAT U Unless drill (PR #205).

## 2026-10-13: Necessary condition, his definition and the door

- **Approved wording (Joshua, 2026-10-13):** "The necessary condition is what you can guarantee will occur if the sufficient condition happens." Keep verbatim on the Necessary page.
- **Door is allowed as a careful metaphor** (sufficient condition opens the door, necessary condition is guaranteed on the other side). Still never "door" as a unit of content. Keep it accurate: the door image must not imply the necessary condition only exists behind it, or that it causes or follows in time.
- **Avoid anything that sounds AI-written.** Plain sentences, no flourishes.

## 2026-10-13: Spot the Relationship comparisons and explanations

The activity rejected implied comparisons in questions 22 and 28 while accepting them in 31, 36 and 47. A comparison can use another object, a numeric benchmark or an earlier state clear from context. Do not teach that it always needs two named objects or the word *than*. The repaired examples remove ambiguous comparative wording from the early single-type questions rather than asking students to ignore it. Question 47 compares pressure with a pressure threshold, not flux.

Questions 33–48 now explain what each indicator connects, the complete requirement or comparison, and the causal reason. A relationship count alone is not an explanation. Several comparisons can share one relationship type; distinguish the number of types from the number of claims. These are implementation corrections under Joshua's fix request, not approval of every exact replacement sentence.

## 2026-10-14: Activity entry pages must make the task visible

Joshua's Spot the Relationship browser annotations identified invisible instructions, confusing example presentation, the term `credited answer`, and a broken Start area. He explicitly requested clear instructions, corrected colors and a usable Start button. These are requested outcomes; the exact replacement wording and visual treatment remain open to his review.

- Explain what the learner reads, what they submit and what happens after checking. Put that guidance visibly before Start. Instructions present in the DOM but unreadable on the page do not meet this requirement.
- Replace internal grading language such as `credited answer` with ordinary student language such as `answer` or `example answer`, as appropriate. Explain the reasoning when revealing an answer.
- A demonstration must clearly connect its example statement, response and reason. Remove redundant or confusing presentation that obscures that connection. The particular overlapping Before/After circles are not a reusable requirement.
- Provide one clear primary Start action on the entry page. Verify its placement, contrast, keyboard focus and narrow-screen behavior; decorative layers and sticky containers must not obscure it or the instructions.
- Describe saving, preview and practice behavior truthfully for the current mode. Do not promise account persistence merely because the interface has a save mechanism.

Reusable review: inspect entry and active practice separately at docked desktop and mobile widths. Check visible text and computed colors, then activate Start. Passing component tests alone does not verify the visual result. These checks apply across quizzes, drills and activities; the cream background, exact colors and component layout used for this repair are implementation choices, not a universal design mandate.

Reuse the app's `DESIGN.md` for visual standards and the bootcamp-builder `references/teaching-preferences.md` for accumulated teaching and interaction decisions. This page owns wording corrections and rejected copy. Keep topic-specific exceptions with their scope and distinguish user direction from a proposed implementation. Repair evidence: [Spot the Relationship acceptance record](../research/2026-10-13-spot-the-relationship-acceptance.md).


## 2026-10-14: Remove attempt-policy narration from Spot entry

Joshua explicitly rejected the paragraph beginning "You have up to 2 attempts per question" on the Spot the Relationship instructions page, including its retry/hint and answer-review narration. Remove that paragraph. The entry should explain the reasoning task and response format; introduce retry guidance when it becomes relevant during practice. This does not change the attempt limit or grading behavior, and does not authorize removing the separate preview/save status notice. Exact future replacement copy is not approved by this correction.


## 2026-10-15: Remove Spot video transcript disclosure

Joshua explicitly marked Read the video transcript and requested removal of that section, including the expanded narration text. Remove it from this activity's entry and remove stale transcript references from playback fallback copy. Preserve video captions, concise written task instructions and Start. This supersedes the earlier transcript implementation for this page, not transcript availability everywhere.

## 2026-10-15: Give the drill a plain task name

Joshua rejected `Build the sufficient side` as vague and unnatural. Use a simple title that names what the learner actually does and makes sense without surrounding lesson context. Keep the entry, active drill and navigation labels consistent. The replacement chosen during implementation is provisional until Joshua reviews it; this correction does not approve an exact replacement or authorize a broader shared design change. This extends the existing rule that labels should name the student action. The bootcamp-builder teaching-preference ledger retains the interaction context and regression check.

## 2026-10-15: RC Create must set up a new drill

Status and provenance: explicit Joshua direction relayed in the current RC Create audit task. Joshua reports that RC Create showing previous drills is broken and requests an audit/fix informed by LSAC and 7Sage. This entry records direction and pending regression checks; it is not independent reproduction, approval of literal copy or implementation, or evidence of publication or a complete RC repair. The parent owns app code and the audit report.

- Explicit direction: RC Create must create or set up a new drill. Do not list previous drills there. Existing work belongs in In progress or Completed, according to its actual status. Make starting new work clearly distinct from resuming existing work.
- Continue the standing direction to update owning design/principle files during authorized edits. Keep wording corrections in wiki/COPY-CORRECTIONS.md and reusable scoped interaction direction in teaching-preferences.md. Update app-owned design/principle files only within the parent's authorized app scope. Preserve prior decisions, unique sections and concurrent changes; do not promote this RC repair into a universal layout rule.
- Scoped implementation candidates, not approved literal wording or final design: an inline RC builder, history filtered by section and status, and truthful LR-only labeling/availability for saved sets where support is LR-only. Do not imply that an LR saved-set flow supports RC. These candidates serve the requested outcome and remain subject to actual implementation and review.
- Research boundary: use LSAC and 7Sage as audit inspiration with source attribution and clear evidence limits. Inspiration does not authorize copying their content or interface, or claiming that current authenticated competitor flows were inspected. This direction capture does not itself verify competitor behavior.

Pending regression checks for the parent audit/fix:

1. Open the exact `?section=rc&view=create` query directly, refresh it, return with browser Back, and exercise the legacy builder entry route. Each route must reach RC new-drill setup without showing existing drill rows; navigation must preserve the intended section and view.
2. Check In progress and Completed with RC and LR records in each meaningful status. History must respect both section and status, and new-drill and resume actions must remain unambiguous. Check empty histories and any LR-only saved-set labels/availability.
3. Inspect light and dark themes, narrow layouts, keyboard navigation and visible focus through setup and launch. Record rendered evidence separately from source or test results.
4. Preview must not create an attempt or write attempt progress. Freeze the selected passage/question IDs so preview and Start use the same selection rather than silently drawing another drill; verify the IDs and attempt-write behavior.

Verification boundary: these checks are requirements, not results. Report local implementation, tests, signed-in acceptance and publication separately. Do not claim this capture publishes a fix or establishes that all RC is fixed.

## 2026-10-16: Keep active drill labels useful and truthful

Joshua rejected `Intro training` as an unhelpful name and `Ready to begin` during an active conditional drill as inaccurate. Remove both from the active run. Use a plain task name and actual progress only where useful; do not replace them with filler. He also rejected the native white group dropdown and low-quality question-jump dropdown: use clear themed two-group choices and use the quiz's numbered question pills as the navigation reference, distinguishing current, completed and review-marked questions. Exact replacement copy and component styling remain provisional. Preserve keyboard access, visible selection and status beyond color alone. Scope and regression checks live in the existing bootcamp-builder teaching-preference ledger.

## 2026-10-16: Spot practice must name the task plainly

Status and provenance: explicit Joshua rules in the current Spot the Relationship correction task, following the bounded source audit and the parent's live readback of The Figure, Rung 1, the raw category chip and The textbook necessary condition. This is a record of requested outcomes and pending implementation principles. App code belongs to the parent; this capture does not establish implementation, acceptance or publication.

| Rejected wording or presentation | Direction and reason |
|---|---|
| Command/Control + Enter helper beneath the answer input | Omit shortcut helpers there by default. Retain keyboard submission, navigation, accessible controls and visible focus. Removing visible helper text must not disable keyboard operation. |
| The Field, The Figure, Rung 1 and raw difficulty categories in student task/feedback UI | Use ordinary task labels such as Sentence and Your answer. Internal metaphors and difficulty metadata make the student decode the implementation instead of doing the reasoning. Keep authoring/parser metadata internal. |
| exact words that create it | Ask the student to quote the words that signal the relationship. Keep the relationship type and supporting quotation explicit, including multiple types. Candidate full instruction: Name each relationship and quote the words that signal it. The direction is explicit; the complete replacement sentence remains an implementation candidate. |
| Question position treated as completion or accuracy | Show a real, accessible completion bar driven by resolved work. Question 48 with 47 resolved is 47 of 48 completed, not 100%. Only resolution of the final question earns full completion; revealed/unjudged completion does not mean correctness or mastery. |

Implementation principles to carry forward, pending verification: first unsuccessful feedback targets the actual response and mistake without disclosing missing answer types or unwritten indicators. Preserve both the written response and useful hint while editing a retry. Correct responses receive the full authored explanation. Explicit reveal or the existing attempt-cap resolution shows the full answer and explanation, with the illustration agreeing with the revealed answer and the earned verdict unchanged. Keep the full answer/explanation hidden during the first unresolved unsuccessful attempt. Service failure stays honestly unjudged. Evaluate verdict accuracy and feedback quality separately.

Audit-derived wording follow-through, not approved literal replacements: remove the item-1 editorial ending The textbook necessary condition in favor of explaining the rule's consequence and limit. A comparison caption must allow equality, including item 12's as strong as; More of this than that is not a complete account of comparisons. These do not authorize changing the activity's relationship taxonomy or attempt limit.

Scope: Spot active practice/feedback and the reusable default against shortcut helper clutter. Preserve existing entry/video decisions, the approved scene identity and unrelated LR Recall corrections. Keep app-owned visual constraints in DESIGN.md and its Activity Centre surface brief; mirror the interaction principles into the six existing bootcamp-builder teaching-preference copies without overwriting their unique sections.

Pending regression: inspect initial, correct, first wrong/partial, edit/retry, cap reveal, explicit reveal and unavailable grading. Verify no rejected task labels/shortcut helper; retained keyboard operation, response and hint; full-explanation boundaries; meaningful progress name/range/count at zero, resume, last unanswered and final resolution; and readable contrast, focus, reduced motion, screen-reader access and narrow/mid-width/wide/docked layouts. These are acceptance requirements, not test or live verification results.

**Implementation evidence follow-up, 2026-10-16 (parent-reported; final rollout pending).** The first repair [de5191fa](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/de5191fadc4a200557a05eddf2975205185148aa) is published and signed-in verified: public index-RQbLCKTI.js loads ActivityRunner-iEu-y23U.js with the initial three markers true. Live checks covered intro, completion progress, retained hint/text on retry, correct-answer dial and explanation, and explicit reveal without upgrading the earned verdict. Follow-up [984ed593](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/984ed5931e1e3fcdeb7d4c4cda5ba2b725bb9b12) normalizes the exact legacy fallback, suppresses resolved retry advice when an authored explanation exists, and retains explanation-before-Next order. It is merged/pushed as [6c1ddd7](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/6c1ddd7050887d5e4ecca79971d893caae630af5), preserving the parallel LR Recall commits, and Lovable synced that exact merge SHA. The free deployment request is 1208c472-6f7f-42ac-ba84-c898898e2b45; rollout remains PENDING because the fourth public hint marker is false. Reported checks passed: 191 initial focused tests, 30 follow-up tests, 31 merged integration tests, production builds and final merged typecheck; these are separate suites, not a unique-test total. This follow-through updates the earlier pending capture only for these evidenced paths; final fallback publication and live hint verification are not yet established.

**Final live verification addendum, 2026-10-16 (parent-observed).** Merge [6c1ddd7050887d5e4ecca79971d893caae630af5](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/6c1ddd7050887d5e4ecca79971d893caae630af5), containing follow-up [984ed593](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/984ed5931e1e3fcdeb7d4c4cda5ba2b725bb9b12), is published and live-observed after Lovable matched the exact source SHA before deployment 1208c472-6f7f-42ac-ba84-c898898e2b45. Fresh public assets are index-B1xv1zq7.js and ActivityRunner-SUttjone.js. In a fresh signed-in Q1, Comparative, only if received a specific appropriate partial hint without answer leakage. Show answer then suppressed the old retry hint entirely and displayed the full authored explanation, answer and illustration; completion became 1 of 48 while the conditional dial stayed unearned. This uniquely observed follow-up behavior supersedes the earlier pending-rollout status for these frontend paths. The CLI fourth-marker false result is not a rollout-failure conclusion: the scanner had not followed the shared chunk and import traversal remains under investigation. Do not claim all four CLI markers passed or a broader live audit. Existing 191 initial, 30 follow-up and 31 integration checks remain separately reported evidence; this filing agent did not rerun app tests or independently operate production.

**Scanner verification resolved, 2026-10-16 (parent-reported).** The corrected scanner followed the actual runner static imports and all four new public markers are TRUE. The shared hint is live in useStudentActivities-CQyQ6wDO.js, reached from public index-B1xv1zq7.js and ActivityRunner-SUttjone.js. This resolves the earlier fourth-marker/import-traversal limitation for published merge 6c1ddd7050887d5e4ecca79971d893caae630af5. The original user tab 1 was reloaded on the final publication and opened at Question 1, 0 of 48 completed, with an empty focused answer input. [Ready-state proof](C:/Users/Joshu/.codex/visualizations/2026/10/13/01a13430-daf2-7fb1-8451-cb685b4e6194/relationship-ready-2026-10-16.png). Earlier pending and scanner-limit statements above remain historical; their verification limitation is now resolved. No app change is part of this filing.

## 2026-10-16: Name the actual Conditional destination

Joshua rejected `Assigned work` for the Conditional course introduction because the name misrepresents the destination. He also identified `Practice Drills` and `Drill Lab` as duplicate navigation and multiple competing menus as too many places to look. Use truthful names, one clear primary course navigation and accurate active highlighting. Preserve existing routes, assignment context, drafts, saving and error feedback. `Course overview`, grouped sidebar navigation and a status-only top area are provisional implementation choices, not approved literal copy or a global layout rule. The bootcamp-builder teaching-preference ledger owns the scoped regression checks.
## 2026-10-16: Relationship keys must follow sentence meaning

Joshua authorized applying the independently reviewed Spot question corrections. Reusable rules: classify indicators in context, not by a keyword list; distinguish sufficient conditions from necessary requirements; accept one valid quotation per distinct type, including contextual alternatives; align type synonyms and split comparisons across grading and visuals; preserve hint-first disclosure. A failed instant match refers to Coach judgment and is not an incorrect verdict. Explanation-only overlays must be scoped to activity and matching prompt/order, preserving historical keys, receipts and earned work.

Implementation targets include removal of six weak standalone causal alternatives, Q31 larger, Q34 contains instead of yields, Q35 Because instead of ambiguous Since, Q40 sufficient-condition wording, Q46 offsets, and removal of stale Q47 flux commentary. [Approved correction proposal](../brainstorms/2026-10-16-spot-the-relationship-gemini-dispositions.md). App DESIGN.md and the Activity Centre surface brief now contain the reusable principles. Implementation/testing/publication status belongs to the task evidence, not this authorization record.

## 2026-10-16: Spot introduction copy and visual hierarchy supersede earlier wording

Joshua rejected the slogan Name the relationship / Find the words that signal it, Worked example, What to write, tiny-title/oversized-slogan/small-subtitle hierarchy, video-first ordering and gold controls on beige. Signal and beige are not globally banned; contextual use matters. He wants ordinary complete instructions, Example, readable consistent typography, restrained neutral buttons, written instructions first and a smaller supporting inline video. Remove repetition rather than substituting another abstract word. This explicitly supersedes the earlier signal-it recommendation in this ledger and the app brief. Preserve the full every-type/quotation requirement and the scientific content.

Existing app DESIGN.md now has a prominent pre-design checklist pointing to the relevant surface brief, teaching voice and this correction ledger. The actual Impeccable context loader reads DESIGN.md, not surface briefs automatically. Documentation improves retrieval but cannot guarantee every future agent reads it. Save rejected and revised screenshots with reasons in the app docs/design-evidence/spot-intro-2026-10-16 record. Revised visuals are implementation candidates, not Joshua-approved until he sees them. Three explicit preference update notes were saved under the native memory updates folder; MEMORY.md was not edited.

## 2026-10-17: Show the curriculum order instead of overlapping destinations

Joshua questioned the distinction between `Course overview` and `Lessons`; the earlier Course overview label was provisional and must not be treated as approved wording. He wants the full ordered hierarchy with lesson numbers such as 1.1, 1.2 and 1.3 and drills clearly identified. He explicitly confirmed that ALL current Conditional material belongs in Part 1. Future Group 3 and Group 4 content will come from him; do not invent it or claim the complete future curriculum exists. Review attempts, Journal and Reference require a purpose/overlap audit and a concrete recommendation, not automatic removal or deletion of their data. This turn is organizational audit and proposal first; implementation remains pending authorization. The existing bootcamp-builder preference ledger owns scoped continuity and proposal checks.
## 2026-10-17: One coherent contrapositive lesson and useful lesson boundaries

Joshua now authorizes implementing the discussed simpler Part 1 course. Combine conceptual and writing-contrapositive material into one coherent lesson; integrate complete-condition qualifications into sufficient/necessary teaching and relevant drill guidance; put each indicator group on its respective condition page. This supersedes the earlier nine-lesson proposal and proposal-only boundary for this consolidation. Use one Course, with all current material in Part 1. Remove Review and Journal from primary navigation while preserving their data and routes. The candidate five notes numbered 1.1–1.5 and twelve drills, including their exact titles, are implementation choices pending review. Future Group 3/4 material remains unsupplied. This capture does not establish implementation, merge or publication. Scope clarification remains in the existing bootcamp-inspection brainstorm; reusable checks remain in the bootcamp-builder preference ledger.
## 2026-10-17: Make lessons, drills and Reference clear

Joshua requests percentage Course progress instead of a fraction, visually distinct lessons and drills with text plus icons/color, an open sequence rather than boxed rows, and Classroom navigation at the bottom. He asks what Reference is for: explain its actual learner purpose. Quick reference and its explanation are provisional implementation wording. The candidate timeline, blue lessons and teal drills do not establish a globally approved palette or component. The bootcamp-builder preference ledger records scope and the public 21st.dev research fallback; no connector use, generated component, paid call or visual acceptance is claimed by this capture.
## 2026-10-17: Review each drill and use the requested rewrite prompt

Joshua rejected the proposed three-main-path consolidation and wants drill-by-drill review before deciding further structure. Remove Place conditions (`source-roles`) from the active course and remove the entire first-word/last-word condition-selection operation wherever it appears in the affected drills, while preserving source/data and complete-condition qualification teaching. His latest exact rewrite prompt is `Rewrite this conditional as if/then.` This supersedes the earlier own-words/no-if-then preference for this step; it does not impose exact-string grading. Active drills need consistent sequential numbers from current course order, with stale embedded source-worksheet numbers removed. Keep stable route/storage identifiers and saved work. No broader consolidation, implementation success or publication is claimed by this capture.
## 2026-10-18: Use condensed conditions and Next step

Joshua wants learner-written condensed conditions rather than opaque W/R letters, with a consistent diagram workflow and clear sufficient/necessary sides plus arrow. Preserve each condition's restrictions, negation and modal strength. Replace `Save and continue` with the exact label `Next step`, preserving actual saving and error feedback. Replace visible reviewed/remaining count prose with a consistent visual progress bar and percentage, separate from question position and Course completion. He rejects `My reasoning matched` / `Needs another look` as a pointless end gate: provide feedback grounded in the actual work, without claiming to grade free writing when no reliable grade exists. These explicit directions supersede conflicting older symbol-entry, progress-copy and self-rating guidance for the affected drills. Implementation and acceptance are pending.
## 2026-10-18: One question map and blank fresh condition fields

Joshua requests removal of the duplicate bottom numbered question navigation. Keep the top progress/navigation bar and bottom Previous / Next question actions. Fresh short-condition fields start blank; normal learner drafts still resume. The parent identified the filled review-preview values as its own test drafts left behind during handoff, not automatic answer prefill. Clear only those known test values through the UI, without wiping persistence or unrelated saved work. Future review previews must not silently contain the assistant's test answers. These are directions and the acknowledged cause, not a claim that cleanup or implementation has passed.
## 2026-10-18: Changed condition wording invalidates the old diagram

Editing a condensed condition must clear downstream placement, NOT choices and accepted grades so old selections are not shown as answers to the new wording. Retain written text for revision and restore untouched saved drafts normally. This is targeted dependency invalidation, not a persistence wipe. The parent's known preview test draft is being cleared through the UI; current implementation and final checks remain pending.
## 2026-10-18: Chapter labels and diagram questions

Joshua directs Chapter instead of Part in visible course UI, preserving internal keys and existing 1.1-style numbering. Diagram choices need a clear question and a readable distinction between sufficient and necessary sides. Fit the actual content panel, including a 658px-wide panel beside a rail, rather than relying only on viewport breakpoints. Current-work merge/publication is explicitly authorized but not established as completed. Chapter 2 AND/OR remains query/grill planning, with no approved final curriculum or implementation claim.

### Conditional Chapter 3: name the actual groups (2026-10-25)

Joshua rejected Translate negative language as the chapter name. Use Group 3 and Group 4 and explain their distinct procedures through complete sentences and original examples from the reviewed curriculum. Do not replace his taxonomy with an invented umbrella label. He reaffirmed the approved Contrapositive page as the gold standard; the existing bootcamp-builder teaching-preferences ledger owns that structure and its acceptance checks. New coverage, writing and visual checks are still required; the correction itself does not establish completion or approval.

## 2026-10-25: AND vs OR needs three focused pages

Joshua names lesson 2.1 `AND vs OR` and requests three internal pages: AND meaning/diagram; OR as one or both/diagram; then negating each condition and switching AND/OR while taking the whole conditional's contrapositive. This supersedes the flat 2.1 layout. Teach one concept per page; remove crowded oversized headers, repeated subtitles and excessive boxing. Use the approved gold standard and relevant design-taste/Impeccable guidance within the existing palette. Preserve lesson IDs, quiz keys and 2.2/2.3. Exact new composition and implementation remain unaccepted until reviewed; no completion or publication claim follows from this capture.

## 2026-10-25: Both conditions, either condition, and the four AND cases

Explicit Joshua correction for AND vs OR: whole group sounds clunky; full group is not an acceptable synonym swap. Prefer both conditions for AND and either condition for inclusive OR, while retaining the explanation that OR permits both. Show all four AND scenarios in a compact chart: both met, first only, second only, neither. Only both-met gets a green check plus the text Met; the other rows need clear Not met labels. Do not rely on color alone.

The chart reports whether the compound sufficient condition is met, not whether its whole conditional is violated. A missing AND component does not prove the result false. A violation requires both trigger components true and the result false. Preserve complete conditions, inclusive OR, contraposition scope, the approved three-page structure and saved learner work. Exact chart design and implementation remain provisional until rendered review. The existing bootcamp-builder teaching-preferences ledger owns the concrete four-row, truth-versus-violation, responsive and accessible regression expectations; this capture does not claim those checks passed or the change was published.

## 2026-10-25: Yahunatan recap: keep the teaching and explain the terms

Joshua rejected “two complete conditions” and “candidate assumption” as confusing and unlike his voice. Use an ordinary example to explain why a contrapositive follows; refer to “an answer you are considering.” Keep useful terms: say “negate,” then explain it as treating the answer as not true.

Joshua also corrected a revision that displaced the session’s strength heuristic with cautions. Necessary assumption teaching should clearly explain the preference for weak, conservative claims and why strong language is a warning. Show some versus most/all, then negate a remaining answer. A brief boundary can explain that weak wording still must be relevant and strong wording can be required; it must not bury or reverse the useful teaching point. Do not invent accuracy percentages or automatic word-based elimination rules.

Evidence: students/yahunatan-zetvy/sessions/2026-10-20-negation-and-necessary-assumptions/transcript.md around 01:03:52 to 01:07:08; Joshua’s direct browser/chat corrections in brainstorms/2026-10-25-yahunatan-voice-calibration.md. Revised drafts: brainstorms/2026-10-25-yahunatan-post-session/.

## 2026-10-25: Say AND or OR directly; use the requested Codex browser

Explicit Joshua correction: connector is not good student wording in AND vs OR. Name AND, OR or the + sign where appropriate. Exact replacement copy remains provisional; preserve both/either meaning, inclusive OR, complete conditions, the four-scenario distinction and whole-conditional contraposition. Do not replace one abstract term with an equally unclear synonym.

Joshua explicitly requests the Codex browser rather than Chrome for this work. At capture, only Chrome automation is exposed and the Codex open request is queued. Do not perform new Chrome visual checks as a substitute, imply a queued request completed, or label Chrome evidence as Codex verification. Keep source reading, code/test results, actual UI/browser evidence and publication status separate. The existing teaching-preferences ledger owns the concrete copy and evidence-boundary regression checks. This records the user's correction and current limitation, not implementation acceptance or publication.

The recap builder enforces a scoped subset of these exact student-facing exclusions in [.agents/skills/post-session-recap/references/session-manual/student-copy-exclusions.json](../.agents/skills/post-session-recap/references/session-manual/student-copy-exclusions.json). Historical comments and private evidence are outside that copy check. Context-dependent editorial corrections remain human review rather than universal substring bans.

## 2026-10-26 · Teach what AND and OR do, one lesson header everywhere
- Rejected: opening the AND lesson with "AND means BOTH conditions." That names the word without teaching it.
- Use: a definition of what the word does to the rule. "AND joins two conditions so they count as one. That side of the rule is met only when both conditions are true." OR: "OR joins two conditions so that either one is enough. That side of the rule is met when one condition is true, and also when both are." Then the example, then why it matters, then the diagram.
- Rejected: a one-off bold sans header with a divider for 2.1 and 2.2. Every lesson uses the same Chapter · Lesson label and italic serif title.
