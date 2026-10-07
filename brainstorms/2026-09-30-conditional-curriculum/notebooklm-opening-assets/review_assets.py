"""Create reviewed derivatives; downloaded NotebookLM evidence remains immutable."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
cards = json.loads((ROOT / 'opening-flashcards.json').read_text())
def replace_card(index, front, back):
    cards['cards'][index] = {'front': {'flashcardContentBlock': [{'type': 'text', 'content': front}]},
                            'back': {'flashcardContentBlock': [{'type': 'text', 'content': back}]}}
replace_card(1, 'What does A → B mean?',
             'If A is true, B must be true. The arrow by itself does not establish a cause or a time order.')
replace_card(2, '“Every order marked ready has been packed.” Does this prove that an order is marked ready?',
             'No. The rule tells us what follows for any order marked ready. It does not tell us that a particular order meets that condition.')
replace_card(3, '“Every order marked ready has been packed.” How do the two groups fit together?',
             'All orders marked ready fit inside the packed-orders group. A ready order cannot sit outside packed. The rule allows packed orders whose ready status is unknown.')
replace_card(6, 'Every order marked ready has been packed. Order B is packed. Do we know whether it is ready?',
             'No. Order B could be marked ready or it could still be waiting for a pickup label. Packed alone does not establish its ready status.')
replace_card(11, 'Does “Every order marked ready has been packed” require more packed orders than ready orders?',
             'No. All ready orders must be packed, but the rule does not require the groups to differ in size. It allows packed orders outside ready.')
replace_card(30, 'Translate: “Where a pickup light is green, an order is ready.”',
             'Pickup light is green → Order is ready. “Where” refers to the green pickup light. Under this stated rule, that complete condition goes left.')
replace_card(61, '“Where a pickup light is green, an order is ready.” An order is ready. Does that establish the pickup light is green?',
             'No. The stated rule makes a green pickup light enough to establish readiness. It does not make readiness enough to establish a green light.')
replace_card(70, 'What does “Marked ready → Packed” tell us about an order not marked ready?',
             'This rule does not determine whether that order is packed. An order not marked ready may be packed or unpacked.')
replace_card(47, 'Translate: “A finalist must attend the interview.” What does the statement establish?',
             'Finalist → Required to attend interview. “Must” states an obligation here. It establishes what finalists are required to do, not that they actually attend.')
replace_card(53, '“A finalist must attend the interview.” Maya attended. Does that prove she is a finalist?',
             'No. The rule gives finalists an obligation to attend. It does not say that only finalists attend, or that everyone who attends has that obligation.')
replace_card(54, '“A finalist must attend the interview.” Maya is a finalist. What follows?',
             'Maya is required to attend the interview. We have established her obligation. The statement does not tell us whether she complies.')
replace_card(57, 'What is the difference between sufficient and necessary?',
             'Sufficient means enough to guarantee the other condition. It goes on the left. Necessary means required whenever the sufficient condition is met. It goes on the right.')
replace_card(60, '“All volunteers wear badges.” Sam wears a badge. What do we know about his volunteer status?',
             'We cannot determine whether Sam is a volunteer. The rule allows volunteers and other people to wear badges.')
replace_card(69, '“Reports submitted before noon are reviewed.” A report arrived at 2 PM. Do we know whether it is reviewed?',
             'No. This rule guarantees review for submissions before noon. It leaves later submissions open to being reviewed or not reviewed.')
# Keep this opening set within the current seven-word group list.
cards['cards'] = [card for i, card in enumerate(cards['cards']) if i != 72]
(ROOT / 'opening-flashcards-reviewed.json').write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding='utf-8')

quiz = json.loads((ROOT / 'opening-quiz.json').read_text())
quiz['questions'][1] = {
    'type': 'multiple_choice',
    'question': 'Every order marked ready has been packed. Order B has been packed. What do we know about its ready status?',
    'answerOptions': [
        {'text': 'It could be ready or not ready.', 'isCorrect': True, 'rationale': 'The rule guarantees packed whenever ready is met. It does not make packed enough to establish ready.'},
        {'text': 'It must be marked ready.', 'isCorrect': False, 'rationale': 'That reverses the rule. A packed order might still be waiting for its pickup label.'},
        {'text': 'It cannot be marked ready.', 'isCorrect': False, 'rationale': 'A ready order would be packed too. The fact that it is packed is compatible with being ready.'},
        {'text': 'No order can be marked ready.', 'isCorrect': False, 'rationale': 'The rule permits ready orders. It only requires that they are packed.'}
    ],
    'hint': 'Which condition starts the rule, and which condition do we know?'
}
quiz['questions'][25] = {
    'type': 'fill_in_the_blank',
    'question': 'Under “Marked ready → Packed,” packed is a ___ condition for being marked ready.',
    'bestAnswer': 'necessary', 'acceptableAnswers': ['necessary condition', 'required'],
    'rationale': 'Every order marked ready must be packed. Packed is required whenever ready is met, so it goes on the right.',
    'hint': 'Ask which condition is required whenever the left side is met.'
}
quiz['questions'][10]['acceptableAnswers'] = ['applicant who submits late', 'an applicant who submits late', 'applicant submits late']
quiz['questions'][13]['grading']['requiredAttributes'] = [
    'Explains that sufficient means enough to guarantee the other condition.',
    'Explains that necessary means required whenever the sufficient condition is met.'
]
quiz['questions'][11]['answerOptions'][1]['rationale'] = 'This would guarantee permission for every electric vehicle. The original statement only makes being electric a requirement for permission.'
quiz['questions'][15]['answerOptions'][3]['rationale'] = 'This is a different rule. It does not express that a signature is required for approval.'
must = quiz['questions'][16]
must['answerOptions'][0] = {'text': 'Finalist → Required to attend interview', 'isCorrect': True,
                           'rationale': 'Here “must” states an obligation. Being a finalist establishes a requirement to attend, not actual attendance.'}
must['answerOptions'][2] = {'text': 'Finalist → Actually attends interview', 'isCorrect': False,
                           'rationale': 'The rule establishes what a finalist must do. It does not establish that the finalist complies.'}
must['answerOptions'][3]['rationale'] = 'The sentence gives finalists an obligation. It does not establish anyone’s finalist status from their attendance.'
quiz['questions'][24]['answerOptions'][3]['rationale'] = 'This adds a different guarantee: having a station prevents operation. The original rule does not say that.'
(ROOT / 'opening-quiz-reviewed.json').write_text(json.dumps(quiz, ensure_ascii=False, indent=2), encoding='utf-8')

report = (ROOT / 'opening-study-guide.md').read_text()
report = report.replace('The arrow expresses a purely logical relationship. It does not express physical cause and effect. It does not describe a sequence in time.', 'The arrow records the logical relationship. By itself, it does not establish physical cause and effect or a sequence in time.')
report = report.replace('A conditional rule only flows in the direction of the arrow.', 'For the forward inference taught here, read from the sufficient condition to the necessary condition. Later lessons will add other valid ways to use the same rule.')
report = report.replace('You must strictly apply a rule to a factual premise in the forward direction.', 'You may apply a conditional rule to a matching fact to find what must follow. Later lessons cover additional valid inferences.')
report = report.replace('demonstrating that logical deduction can only move forward along the path and cannot flow backward against the arrow.', 'showing why knowing the left side gives the right side, while knowing the right side alone does not establish the left.')
report = report.replace('Deep Dive on', 'Read')
report = report.replace('| A finalist must attend the interview. | Attends the interview. | `Finalist -> Attends interview` |', '| A finalist must attend the interview. | Is required to attend the interview. | `Finalist -> Required to attend interview` |')
report += '\n\n### Read “must” in context\n\nIn the interview sentence, “must” states an obligation. It tells us what a finalist is required to do. It does not establish that the finalist actually attends. In other sentences, “must” can express logical necessity. Keep the complete meaning when you diagram.\n'
(ROOT / 'opening-study-guide-reviewed.md').write_text(report, encoding='utf-8')
print('Created reviewed derivatives: 79 flashcards, 27 quiz questions and corrected study guide.')
