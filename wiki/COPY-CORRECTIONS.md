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

