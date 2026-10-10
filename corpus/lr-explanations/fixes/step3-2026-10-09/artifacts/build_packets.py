"""Build one JSON packet per Revamp question from the fresh mirror, plus batch files."""
import json, csv, glob, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
DB = 'C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/'
BANK = 'C:/Users/Joshu/dev/ai-os-projects/lsatu/public/data/'
OUT = os.path.dirname(os.path.abspath(__file__))
L = lambda t: json.load(open(DB + t + '.json', encoding='utf-8'))
qs = {q['id']: q for q in L('lr_questions')}
ch = {}
for c in L('lr_answer_choices'):
    ch.setdefault(c['question_id'], {})[c['letter']] = c
ex = {e['id']: e for e in L('lr_explanations')}
steps, notes = {}, {}
for s in L('lr_explanation_steps'):
    steps.setdefault(s['explanation_id'], []).append(s)
for n in L('lr_explanation_choice_notes'):
    notes.setdefault(n['explanation_id'], []).append(n)
bank = {}
for f in glob.glob(BANK + 'PT*-S*-LR.json'):
    for b in json.load(open(f, encoding='utf-8')):
        bank[f"{b['practiceTest']}-S{b['sectionNumber']}-Q{b['questionNumber']}"] = b
rows = [r for r in csv.DictReader(open('C:/Users/Joshu/dev/ai-os/corpus/lr-explanations/fixes/revamp-inventory.csv', encoding='utf-8')) if r['verdict'] == 'Revamp']
packets = []
for r in rows:
    q = qs[r['question_id']]
    e = ex.get(r['explanation_id'])
    if not e:
        print('NO EXPLANATION ROW', r['qid']); continue
    b = bank.get(r['qid'])
    choices = {l: c['choice_text'] for l, c in sorted(ch.get(q['id'], {}).items())}
    bank_choices = None
    if b:
        ac = b.get('answerChoices')
        bank_choices = ac if isinstance(ac, dict) else {x.get('letter', chr(65 + i)): x.get('text') for i, x in enumerate(ac)} if ac else None
    packets.append({
        'qid': r['qid'], 'type': q.get('question_type'), 'difficulty': r['difficulty'], 'key_db': q['correct_choice'],
        'stimulus_db': q['stimulus'], 'stem_db': q['prompt'], 'choices_db': choices,
        'bank': ({'stimulus': b.get('stimulus'), 'stem': b.get('questionStem'), 'choices': bank_choices, 'key': b.get('correctAnswer')} if b else None),
        'explanation_id': e['id'], 'style': e['style'],
        'steps': [{'row_id': s['id'], 'position': s['position'], 'label': s['label'], 'body': s['body']} for s in sorted(steps.get(e['id'], []), key=lambda s: s['position'])],
        'notes': [{'row_id': n['id'], 'letter': n['letter'], 'body': n['body']} for n in sorted(notes.get(e['id'], []), key=lambda n: n['letter'])],
        'known_problem': r['verdict_note'], 'tags': r['tags'],
    })
packets.sort(key=lambda p: (int(re.search(r'PT(\d+)', p['qid']).group(1)), p['qid']))
os.makedirs(OUT + '/packets', exist_ok=True)
for p in packets:
    json.dump(p, open(f"{OUT}/packets/{p['qid']}.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump([p['qid'] for p in packets], open(OUT + '/all_qids.json', 'w'))
print(len(packets), 'packets')
