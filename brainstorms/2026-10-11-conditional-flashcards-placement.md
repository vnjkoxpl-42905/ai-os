# Conditional flashcards placement: Brainstorm / Discovery Notes
Date: 2026-10-11 · Goal: Pin down what Joshua expects to see in the Flashcards tool for the Group 1 and Group 2 word cards
Status: in progress
Context sources: `brainstorms/2026-10-11-conditional-indicator-flashcards.md`; PR #204 commits e2833518, 78a55754

## State at start (verified 2026-10-11 in the dev preview, page=tools)
Flashcards tool lists: Terms and concepts, Group 1 words (turn-over), Group 2 words (turn-over), Indicator words both groups (mixed quiz). Lessons hold no flashcards.

## Joshua's message (verbatim)
"I want the group two, group one word flashcards in the flashcard deck. So I should see flashcards for, as we stated earlier."

## Summary / key decisions
- Mixed deck only: all Group 1 and Group 2 words together, student presses Group 1 or Group 2 on each card. No single-group decks, ever. (Joshua, round 1)
- Group 1 words / Group 2 words turn-over decks (built in 78a55754) are REMOVED.
- Tentative (my reading): the mixed deck is always listed in Flashcards, whatever lessons are assigned. Q3 not answered directly; 'always a mixed deck' read as yes.

## Q&A log
### Round 1
#### Q1 - Where is he looking
- Captured: the dev preview (127.0.0.1:8097), as opened by me.
#### Q2 - One deck or separate
- Captured: 'it's mixed. There's no choice between group one and group two words... they have to choose between group one and group two, like we discussed earlier... always a mixed deck. There's no such thing as one individual deck that has one group.'
#### Q3 - Always visible
- Not answered directly. Tentative: yes.


## Open flags
- Confirm the mixed deck should show even when a student has no group lesson assigned -> Joshua
