import ast
import hashlib
import json
import re
import subprocess
from pathlib import Path

proof = Path(__file__).parent
repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp')
head = subprocess.check_output(['git', 'show', 'HEAD:src/bootcamps/conditionals/content/foundations.source.ts'], cwd=repo).decode('utf-8')
line = next(line for line in head.splitlines() if "question('group-2-a1'," in line)
args = ast.literal_eval('(' + re.search(r'question\((.*)\),$', line.strip()).group(1) + ')')
question = dict(zip(['id', 'prompt', 'options', 'answerIndex', 'hint', 'reasoningSteps'], args))
question['explanation'] = ' '.join(question['reasoningSteps'])
question.update(unitId='group-2', unitTitle='Group 2: Keep the Requirement on the Right', difficulty='advanced')
originals = json.loads((proof / 'historical-questions.json').read_text(encoding='utf-8'))
originals.append(question)
(proof / 'historical-questions-v2.json').write_text(json.dumps(originals, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Historical four SHA256: ' + hashlib.sha256(json.dumps(originals, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest())
