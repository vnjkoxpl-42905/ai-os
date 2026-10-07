import hashlib
import json
import re
from pathlib import Path

repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp')
proof = Path(__file__).parent
draft_path = proof.parent.parent / 'voice-opening-source-draft.md'
draft_text = draft_path.read_text(encoding='utf-8')
draft = json.loads(re.search(r'```json\n(.*?)\n```', draft_text, re.S).group(1))
baseline = json.loads((proof / 'curriculum-before.json').read_text(encoding='utf-8'))
opening_ids = ['orientation', 'sufficient-necessary', 'group-1', 'group-2']
replacements = {'group-1-a3': 'group-1-a3-v2', 'group-2-m2': 'group-2-m2-v2', 'group-2-a3': 'group-2-a3-v2'}

# Actual Claude scope review removes the optional expression extensions.
draft['units']['group-1']['teaching'] = draft['units']['group-1']['teaching'][:-2]
draft['units']['group-2']['teaching'] = draft['units']['group-2']['teaching'][:11] + draft['units']['group-2']['teaching'][-1:]

# The worked indicator lab and independent recorded drills use separate examples.
# These explanatory anchors match the existing formative lab, not the 62 drills.
group1 = draft['units']['group-1']['teaching']
group1[2] = "When can introduce the event that's enough: When the alarm sounds, the staff evacuate. Ask when what. The alarm sounds. Under this rule, that event guarantees evacuation. Whenever makes the same repeated-case meaning explicit. But When I checked the desk, a notice was there reports one occasion; it doesn't promise a notice every time I check."
group1[3] = "Where can make a rule about a location or situation: Where a station is available, the service operates. Which locations does the rule cover? Locations with an available station. At one of those locations, the service has to operate. Keep the location connection when you read the rule back; a station elsewhere hasn't met this location's condition."
group1[4] = "All covers the whole group it names: All registered guests receive a wristband. All what? Registered guests, not guests generally. Being one of those registered guests is enough for a wristband. Another guest may receive one too; the sentence hasn't told us. It also hasn't told us that a registered guest exists."
group1[5] = "The only needs careful reading: The only vehicles permitted inside are electric vehicles. The only what? Vehicles permitted inside. If a vehicle is permitted inside, it must be electric. Try electric vehicle → permitted inside. That would grant permission to every electric vehicle, which the sentence never promised. The grammatical target is the whole permission description, not the word electric."
group1[6] = "Every takes the members one at a time but covers them all: Every finalist receives an invitation. Choose a finalist. That person has to receive an invitation under the rule. All finalists receive an invitation would express the same relationship. Neither wording says everyone receiving an invitation is a finalist."
group1[7] = "Any says that whichever member of the named group you choose, the rule applies: Any applicant who submits late pays a fee. Choose a late-submitting applicant and that person pays a fee under the rule. Choose an applicant who submits on time and this sentence doesn't settle the fee question. Submits late stays with applicant in your diagram."
draft['units']['group-1']['method'][1] = "Name both complete ideas. Keep who or what they concern, as well as restrictions such as registered or submits late."

group2 = draft['units']['group-2']['teaching']
group2[3] = "Only if introduces a condition that has to be met: A student graduates only if the student completes the project. If the student graduates, the project must be completed. Project completion by itself doesn't promise graduation. Read the reverse aloud and you'll hear the extra guarantee it adds."
group2[4] = "Only when makes an event or state required: A review occurs only when a complaint is filed. A complaint has to be filed for this review to occur. Imagine a complaint has been filed. Does this sentence say a review now occurs? No. It says what a review requires, not that every complaint gets one."
group2[5] = "Only where makes a location condition required: The service operates only where a station is available. Wherever the service operates, a station has to be available there. A station at another location isn't enough. Nor has the sentence promised service to every place with an available station."
group2[6] = "Always describes the result that holds throughout the named cases: A finalist always receives an invitation. Start with a finalist. Under that claim, the person receives an invitation. The subject supplies the sufficient idea; receiving an invitation is the required result. Always belongs in this teaching group, but it doesn't mean the next word automatically goes on the right. Read the complete subject and result."
group2[7] = "Requires tells you what is needed: Entry requires a current pass. Requires what? A current pass. Entry goes left, having the current pass goes right. Change the wording to A current pass is required for entry. The requirement appears first now, but the relationship hasn't changed. A pass alone isn't a promise that you can enter, and an expired pass doesn't meet the full requirement."
group2[10] = "Keep every part of a requirement. In Entry requires a current pass, pass would drop current. In Only members may use this room, actually uses the room would change permission into an action. The right direction can't repair a label that has lost part of the idea."

units = {}
for unit in baseline:
    if unit['id'] not in opening_ids:
        continue
    unit.update(draft['units'][unit['id']])
    for question in [unit['guidedExample'], *(question for level in ['beginner', 'medium', 'advanced'] for question in unit['drills'][level])]:
        hint, steps = draft['questionFeedback'][question['id']]
        question.update(hint=hint, reasoningSteps=steps, explanation=' '.join(steps))
        question['id'] = replacements.get(question['id'], question['id'])
    units[unit['id']] = unit

def js(value):
    return json.dumps(value, ensure_ascii=False)

def lines(values, indent=6):
    return '[\r\n' + ''.join(' ' * indent + js(value) + ',\r\n' for value in values) + ' ' * (indent - 2) + ']'

def question_call(question):
    return 'question(' + ', '.join(js(question[key]) for key in ['id', 'prompt', 'options', 'answerIndex', 'hint', 'reasoningSteps']) + ')'

def source_unit(unit):
    text = '  {\r\n'
    text += f"    id: '{unit['id']}', title: {js(unit['title'])}, area: '{unit['area']}', phase: '{unit['phase']}', prerequisites: {js(unit['prerequisites'])},\r\n"
    text += f"    goal: {js(unit['goal'])},\r\n"
    for field in ['teaching', 'method']:
        text += f'    {field}: ' + lines(unit[field]) + ',\r\n'
    worked = unit['workedExample']
    text += '    workedExample: {\r\n'
    for field in ['statements', 'reasoning', 'conclusion']:
        text += f'      {field}: {js(worked[field])},\r\n'
    text += '    },\r\n'
    text += '    guidedExample: ' + question_call(unit['guidedExample']) + ',\r\n'
    text += '    commonMistake: ' + '{ ' + ', '.join(f'{key}: {js(value)}' for key, value in unit['commonMistake'].items()) + ' },\r\n'
    text += '    drills: {\r\n'
    for level in ['beginner', 'medium', 'advanced']:
        text += f'      {level}: [\r\n'
        text += ''.join('        ' + question_call(question) + ',\r\n' for question in unit['drills'][level])
        text += '      ],\r\n'
    return text + '    },\r\n  },\r\n'

source_path = repo / 'src/bootcamps/conditionals/content/foundations.source.ts'
source = source_path.read_bytes().decode('utf-8')
matches = list(re.finditer(r"(?m)^  \{\r?\n    id: '([^']+)'", source))
patches = []
for index, match in enumerate(matches):
    unit_id = match.group(1)
    if unit_id in units:
        patches.append((match.start(), matches[index + 1].start(), source_unit(units[unit_id])))
assert len(patches) == 4
original_other_blocks = {match.group(1): source[match.start():matches[index + 1].start()] for index, match in enumerate(matches[:-1]) if match.group(1) not in opening_ids}
for start, end, replacement in reversed(patches):
    source = source[:start] + replacement + source[end:]
for original in original_other_blocks.values():
    assert original in source
source_path.write_bytes(source.encode('utf-8'))

historical = json.loads((proof / 'historical-questions.json').read_text(encoding='utf-8'))
legacy = "import type { ConditionalDifficulty, ConditionalQuestion } from './types';\n\n"
legacy += 'export interface LegacyConditionalQuestion extends ConditionalQuestion {\n  unitId: string;\n  unitTitle: string;\n  difficulty: ConditionalDifficulty;\n}\n\n'
legacy += '// Original questions remain available only to saved runs and attempt review.\n// They require later inference and must never enter newly assigned practice.\n'
legacy += 'const historicalQuestions: LegacyConditionalQuestion[] = ' + json.dumps(historical, ensure_ascii=False, indent=2) + ';\n\n'
legacy += 'export function findLegacyConditionalQuestion(id: string): LegacyConditionalQuestion | undefined {\n  return historicalQuestions.find(question => question.id === id);\n}\n'
(repo / 'src/bootcamps/conditionals/content/legacyQuestions.ts').write_text(legacy, encoding='utf-8', newline='\n')

# Update the concrete review draft to the authorized, actually applied scope.
draft_text = re.sub(r'```json\n.*?\n```', '```json\n' + json.dumps(draft, ensure_ascii=False, indent=2) + '\n```', draft_text, flags=re.S)
draft_text = draft_text.replace('App authoring is paused pending the actual Claude plan review. This file is an external, concrete proposal; it does not modify the app.', 'Applied to the four owned units after the coordinating agent authorized implementation under Joshua\'s build request. Claude plan round 2 returned REVISE; the host accepted the warranted corrections. Final actual Claude inspection is still required.')
draft_text = draft_text.replace('The existing optional wording extensions stay available with their limits.', 'The optional wording extensions are removed following the actual Claude scope review. The fourteen core expressions remain developed individually.')
draft_text = draft_text.replace('Nothing here teaches contraposition, combining rules, Groups 3/4 or quantities.', 'The newly authored opening teaches no contraposition, combining rules, Groups 3/4 or quantities. Historical questions remain outside new practice.')
draft_path.write_text(draft_text, encoding='utf-8', newline='\n')

projection = [(unit['id'], level, question['id'], question['prompt'], question['options'], question['answerIndex']) for unit_id in opening_ids for unit in [units[unit_id]] for level in ['beginner', 'medium', 'advanced'] for question in unit['drills'][level]]
signature = hashlib.sha256(json.dumps(projection, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest()
print(json.dumps({'openingPracticeCount': len(projection), 'practiceContractSha256': signature, 'historicalSha256': hashlib.sha256(json.dumps(historical, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest(), 'renamed': replacements}, indent=2))
