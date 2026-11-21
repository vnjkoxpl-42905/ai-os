import ast
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

proof = Path(__file__).parent
repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp')
source = (repo / 'src/bootcamps/conditionals/content/foundations.source.ts').read_text(encoding='utf-8')
unit_starts = list(re.finditer(r"(?m)^  \{\n    id: '([^']+)'", source))
opening = {}
for index, start in enumerate(unit_starts[:-1]):
    if start.group(1) not in ['orientation', 'sufficient-necessary', 'group-1', 'group-2']:
        continue
    block = source[start.start():unit_starts[index + 1].start()]
    rows = []
    for line in block.splitlines():
        match = re.match(r'\s+(?:guidedExample: )?question\((.*)\),$', line)
        if not match:
            continue
        args = ast.literal_eval('(' + match.group(1) + ')')
        row = dict(zip(['id', 'prompt', 'options', 'answerIndex', 'hint', 'reasoningSteps'], args))
        rows.append(row)
    opening[start.group(1)] = rows
(proof / 'subject-audit-current.json').write_text(json.dumps(opening, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for unit_id, rows in opening.items():
    print(unit_id)
    for row in rows:
        if row['id'].endswith('-guide'):
            continue
        print(row['id'] + '\n' + row['prompt'] + '\nCorrect: ' + row['options'][row['answerIndex']] + '\nHint: ' + row['hint'] + '\nWhy: ' + ' '.join(row['reasoningSteps']) + '\n')

draft_path = proof.parent.parent / 'voice-opening-source-draft.md'
draft_text = draft_path.read_text(encoding='utf-8')
draft = json.loads(re.search(r'```json\n(.*?)\n```', draft_text, re.S).group(1))
for rows in opening.values():
    for row in rows:
        feedback_id = row['id'].removesuffix('-v2') if row['id'] != 'group-2-a1-v2' else row['id']
        draft['questionFeedback'][feedback_id] = [row['hint'], row['reasoningSteps']]
draft['questionFeedback'].pop('group-2-a1', None)
draft['units']['group-2']['commonMistake']['repair'] = "Ask exactly what was promised. Having a current pass meets the requirement for entry, but it doesn't establish that someone entered. Must attend establishes required attendance, not actual attendance. Keep that distinction in the diagram and conclusion."
draft_text = re.sub(r'```json\n.*?\n```', '```json\n' + json.dumps(draft, ensure_ascii=False, indent=2) + '\n```', draft_text, flags=re.S)
draft_text = draft_text.replace('Three earlier replacements reused IDs whose HEAD originals have a different meaning.', 'Three earlier replacements reused IDs whose HEAD originals have a different meaning. Actual inspection also retires group-2-a1 because its original assessed a later operation; its current replacement is group-2-a1-v2, a direct-direction translation preserving the full emergency appointment and permission.')
draft_text = draft_text.replace('Keep the exact originals from `visual-proof/voice-application/historical-questions.json` in a historical-only lookup.', 'Keep the exact four originals from `visual-proof/voice-application/historical-questions-v2.json` in a historical-only lookup; the earlier three-row proof is preserved.')
draft_text += '\n## Actual inspection 1 corrections, 2026-10-02\n\nOR-1: My feedback rewrite used performance where the preserved prompt says rehearsal. The hint and every reasoning sentence now keep rehearsal. OR-7: The reference repair now uses the taught current-pass/entry example. OR-6: The old group-2-a1 is available only for saved work; its new -v2 question directly asks for the complete appointment requirement and permission. Other 61 prompts, option order, keys and levels remain unchanged.\n\nOR-9: Before this voice rewrite, group-2-b3 changed Every registered buoy always broadcasts its identifier to A registered buoy always broadcasts its identifier. Always preserves the universal claim about registered buoys. Options and answer index 1 are unchanged, so this cosmetic wording needs no retired question. This is documented alongside the earlier cosmetic obligation wording in group-2-a2.\n\nPortable practice fingerprint (62 approved current questions): 2cc25820135dd0c10ccfcd629a68758d4d924a9a3a3545df857dfbca1fc0f534. Preserved 61-question fingerprint: e4f9a1577a66ac70ca1e0fc26b6b96b6bb561e8160c00bf052517c3a4417a5f9. Four exact historical objects: 0d0ff240d9b0597515efb0b02f50f62e1af234cb1d12027d419f37ea5e76a6aa.\n'
draft_path.write_text(draft_text, encoding='utf-8')
