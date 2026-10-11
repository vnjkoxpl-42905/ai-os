# Conditional indicator flashcards: Brainstorm / Discovery Notes
Date: 2026-10-11 · Goal: Pin down the redesigned indicator flashcards (indicator word on the front, student commits to a group, card flips, back says the group and what to do with it)
Status: in progress
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

## Open flags (pending input)
- Whether rounds mix both groups (Q6 unanswered in round 1).
- What happens to the old question-style cards and the 4 concept cards.
