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
- **Words:** 'Correct', not 'Right', on a correct answer. Bold the word 'if' where the point is that the rule says what follows *if* something is true.

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

