# Conditional indicator flashcards: Brainstorm / Discovery Notes
Date: 2026-10-11 · Goal: Pin down the redesigned indicator flashcards (indicator word on the front, student commits to a group, card flips, back says the group and what to do with it)
Status: built and pushed to PR #204 (2026-10-11). Resume point: none; open items are the Group 1 lesson decision (below) and the preview of how it reads in the course.
Context sources: `ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/` (`components/StudyDeck.tsx`, `components/FlashcardTools.tsx`, `content/indicatorFlashcards.ts`)

## What exists today (verified 2026-10-11, from the code)
- 30 cards: 4 "foundation" (concepts), 16 Group 1, 10 Group 2. Each front is a full question ("Every folder marked complete contains a signed form. Which condition is enough...") and the back is the explanation. Not the indicator word alone.
- Student picks an indicator from a dropdown inside a focused deck, taps the card to flip it. Nothing is committed before the flip.
- Decks are reached from Tools > Flashcards (3 sets) and embedded as "Recall" steps in the lessons.

## Joshua's request, as first stated (verbatim intent)
- Front: just the indicator word or phrase ("only", "only if", "always", "if").
- The student must say which group it falls under. The card flips after they say it.
- Back: which group it is, and what to do with that concept.
- Mentions "five cards" for "the individual indicator" cards. Meaning not yet pinned down.

## Summary / key decisions
Confirmed by Joshua (round 1):
- The 'five cards' remark was a slip. He meant flashcards. No five-card rule.
- The new indicator-word cards REPLACE the Group 1 and Group 2 decks.
- Two buttons under the card, Group 1 or Group 2. No typing.
- Choosing a button flips the card and says right or wrong.
- A wrong pick still flips. The screen shakes, the card flips, and it says what the right group is and what was wrong.
- Back text: very short, one or two lines, mainly which group it is. Clear, organized, not complicated. Quick feedback.

## Round 2 decisions (confirmed by Joshua, 2026-10-11)
- Mixed groups only. One deck, both groups together.
- Include ALL indicator words from both groups (not my 21-word cut). Do not label the groups on the deck listing; the cards are mixed.
- Group wording: Group 2 is a "necessary condition indicator"; by the same pattern Group 1 is a "sufficient condition indicator" (my inference for Group 1).
- Back of the card: "This is a necessary condition indicator word, Group 2." One line, group named, in those words.
- Order truly randomized. No long same-group runs; a few back-to-backs are fine.
- A card answered wrong comes back ONCE, at the end of the round, after every card has been seen.
- A running count of cards done so far is shown.
- ALL progress saved to the database. The student can leave and resume exactly where they were.

## FINAL word list (Joshua, 2026-10-11, overrides my 26-card proposal)
- Group 1, sufficient condition indicator (13): if, when, whenever, where, all, every, any, anyone, anytime, every time, each, the only, who. (His list typed "every" twice; read as one card.)
- Group 2, necessary condition indicator (7): only, only if, only when, only where, always, must, requires.
- Dropped from my proposal: people who, in order to, only after, only those, required for, necessary for.
- 20 cards total.

## Round 3 decisions (confirmed by Joshua, 2026-10-11)
- "only" and "the only" are two separate cards. "Only" is Group 2 (necessary condition indicator). "The only" is Group 1 (sufficient condition indicator). His reason: the word itself is an essential part of the indicator.
- End of round (my recommendation, accepted): a second miss on the returned card is logged as missed with no third try; a one-line summary ("18 right first time. 5 needed a second look."); "Go again" reshuffles every card and keeps the earlier round's score.
- Progress is saved in the student's existing account record (the same way the drills resume), no new tables, no Lovable deploy. Saved: shuffled order, current card, each answer, the queue of missed cards.
- Lesson "Recall" steps use the new deck, limited to the words that lesson has taught so far. The 26 old question-style Group 1 and Group 2 cards stop showing as decks but their data is kept. The 4 concept cards stay as they are.
- On a wrong pick the CARD shakes (not the whole page).

## Q&A log
### Round 1
#### Q1 - What does five cards mean
- Asked: (a) five per lesson, (b) five per round, (c) only five indicators, (d) other
- Recommended: (b)
- Captured: 'I didn't mean to say five cards. I meant to say flash cards. The five cards part was a mistake.' Dropped.
#### Q2 - Replace or add beside the Group 1 / Group 2 decks
- Recommended: replace, move old example cards into lessons
- Captured: 'they should replace the group one and group two decks with new indicator word group flash cards.'
- Flags: what happens to the old example cards and the 4 concept cards was not addressed -> Joshua (asked again in round 2)
#### Q3 - How the student commits
- Recommended: two buttons
- Captured: 'there should be two buttons, either group one or group two. Shouldn't be typing an answer.' The buttons sit below the card.
#### Q4 - Wrong pick
- Recommended: flip anyway, show their pick and the right one
- Captured: 'If they get it wrong, it should flip anyway and tell them what they should be. ... the screen should shake, and it should flip the card and clarify what's wrong.'
- Tentative: shake the card rather than the whole page, and skip the shake under reduced-motion (my reading, not stated)
#### Q5 - Back of the card
- Recommended: group, which side of the arrow, one mini example, no contrapositive
- Captured: 'the answer to the explanations should have just a simple one line, like two lines, like just saying what group it is. And it should be very clear and organized and not too complicated. Very simple, clear, quick feedback.'
- Tentative: whether the arrow side ('goes on the left/right') counts as part of the two lines. His earlier words, 'what to do with that concept', suggest it might. Asked again in round 2.
#### Q6 - Mixed groups or one at a time
- Captured: not answered. Asked again in round 2.

### Round 2
#### Q6 - Mixed groups
- Captured: "mixed gorups only"
#### Q7 - Words
- Captured: include all the words for both groups, mixed, groups not named; "all of them should be specific"; order really randomized, some back-to-backs allowed but not continuous.
- Tentative: "specific" read as each indicator being its own card (not "if: condition comes last" variants). Confirm.
#### Q8 - Back wording
- Captured: "you say this is a necessary condition indicator word, group two"
- Tentative: the back is only that one line, with no arrow side and no example. Confirm.
#### Q9 - Order, repeats, counter
- Captured: shuffled; a missed card returns once at the end after all cards; counter of cards done so far; progress saved through the database and resumable.
- Not answered: end-of-round summary; a second miss on the returned card; what "go again" does.
#### Q10 - Lessons, old cards, shake
- Not answered. Asked again in round 3.

### Round 3
#### Q11 - "the only": two separate cards. Only = Group 2, the only = Group 1. Captured in his words above.
#### Q12 - Word list: NOT answered by Joshua. Falls under his round-2 rule "include all of the words for both groups".
- Recommended and proposed in recap: the 23 words from the old decks plus "anyone", "only after" and "only those", which the worksheet drills already teach as indicators (26 cards). Bare "require" is left out as a duplicate of "requires". Flagged for his confirmation.
#### Q13 - End of round: recommended, accepted ("go with the recommended")
#### Q14 - Saved progress: recommended, accepted
#### Q15 - Lessons, old cards, concept cards: recommended, accepted
#### Q16 - Shake: the card only. Accepted.

## Open flags (pending input)
- The final word list (26 cards) needs one yes from Joshua. Extra words I proposed: anyone, only after, only those, who.
