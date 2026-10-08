"""Print everything about one or more LR questions: bank text students read, DB text,
choices, key, and every explanation style with row ids.  Usage: python3 -I qshow.py PT146-S3-Q1 ..."""
import json, sys, collections, os

ROOT = os.path.dirname(os.path.abspath(__file__))
AIOS = os.path.abspath(os.path.join(ROOT, '../../../..'))
DB = os.path.join(AIOS, 'system/scripts/lsatlab-pull/data/db/')
BANK = os.environ.get('LSATU_BANK', '/home/user/lsatu-684d89db/public/data/')
L = lambda t: json.load(open(DB + t + '.json', encoding='utf-8'))
qs = L('lr_questions'); ex = L('lr_explanations'); st = L('lr_explanation_steps')
nt = L('lr_explanation_choice_notes'); ch = L('lr_answer_choices')
Q = {q['qid']: q for q in qs}
E = collections.defaultdict(list)
for e in ex: E[e['question_id']].append(e)
S = collections.defaultdict(list); N = collections.defaultdict(list); C = collections.defaultdict(list)
for s in st: S[s['explanation_id']].append(s)
for n in nt: N[n['explanation_id']].append(n)
for c in ch: C[c['question_id']].append(c)
ORDER = {'standard': 0, 'brief': 1, 'another_way': 2, 'single': 3}

def bank(qid):
    pt, s, n = qid[2:].split('-')
    f = os.path.join(BANK, f'PT{pt}-{s}-LR.json')
    if not os.path.exists(f): return None
    for x in json.load(open(f, encoding='utf-8')):
        if x.get('questionNumber') == int(n[1:]): return x

for qid in sys.argv[1:]:
    q = Q.get(qid)
    if not q: print('=====', qid, 'NOT IN DB'); continue
    b = bank(qid)
    print('=====', qid, '| type:', q['question_type'], '| DB key:', q['correct_choice'],
          '| bank key:', (b or {}).get('correctAnswer'))
    if b and b.get('stimulus'):
        print('BANK STIMULUS:', b['stimulus']); print('BANK STEM:', b.get('questionStem'))
        bc = b.get('answerChoices') or {}
        for k in sorted(bc): print(f"  BANK {k}{'*' if k == b.get('correctAnswer') else ' '} {bc[k]}")
        if b['stimulus'].strip() != (q['stimulus'] or '').strip(): print('!! DB STIMULUS DIFFERS:', q['stimulus'])
        if (b.get('questionStem') or '').strip() != (q['prompt'] or '').strip(): print('!! DB STEM DIFFERS:', q['prompt'])
        dbc = {c['letter']: c['choice_text'] for c in C[q['id']]}
        for k in sorted(set(bc) | set(dbc)):
            if (bc.get(k) or '').strip() != (dbc.get(k) or '').strip(): print(f"!! DB CHOICE {k} DIFFERS: {dbc.get(k)}")
    else:
        print('(no bank text) DB STIMULUS:', q['stimulus']); print('DB STEM:', q['prompt'])
    if not (b and b.get('stimulus')):
        for c in sorted(C[q['id']], key=lambda c: c['letter']):
            print(f"  DB {c['letter']}{'*' if c['is_correct'] else ' '} {c['choice_text']}")
    for e in sorted(E[q['id']], key=lambda e: ORDER.get(e['style'], 9)):
        print(f"--- style={e['style']} explanation_id={e['id']}")
        for s in sorted(S[e['id']], key=lambda s: s['position']):
            print(f"  [step {s['position']} id={s['id']}] {s['label']}\n{s['body']}")
        for n in sorted(N[e['id']], key=lambda n: n['letter']):
            print(f"  [note {n['letter']} id={n['id']}] {n['body']}")
