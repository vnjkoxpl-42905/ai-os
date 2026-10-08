import json,sys
D='/home/user/ai-os/system/scripts/lsatlab-pull/data/db/'
qs={q['id']:q for q in json.load(open(D+'lr_questions.json'))}
byq={}
for q in qs.values():
    byq.setdefault(q.get('qid') or q.get('slot') or q['id'],q)
ks=list(next(iter(qs.values())).keys())
ch=json.load(open(D+'lr_answer_choices.json'))
want=sys.argv[1:]
for q in qs.values():
    name=None
    for k in ('qid','slot','question_key'):
        if k in q: name=q[k]
    if name in want:
        cs=sorted([c for c in ch if c['question_id']==q['id']],key=lambda c:c['letter'])
        print(name, [(c['letter'],c['student_percent'],c['tag']) for c in cs])
