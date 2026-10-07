import json,sys,collections
import sys; sys.stdout.reconfigure(encoding="utf-8")
DB='C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/'
L=lambda t: json.load(open(DB+t+'.json',encoding='utf-8'))
qs=L('lr_questions'); ex=L('lr_explanations'); st=L('lr_explanation_steps'); nt=L('lr_explanation_choice_notes')
Q={f"PT{q['preptest']}-S{q['section']}-Q{q['question_number']}":q for q in qs}
E=collections.defaultdict(list)
for e in ex:
  if e['style'] in('single','standard'): E[e['question_id']].append(e['id'])
S=collections.defaultdict(list); N=collections.defaultdict(dict)
for s in st: S[s['explanation_id']].append(s)
for n in nt: N[n['explanation_id']][n['letter']]=n['body']
for slot in sys.argv[1:]:
  q=Q[slot]; print('=====',slot,q['question_type'],'key',q['correct_choice']); print('STIM:',q['stimulus']); print('STEM:',q['prompt'])
  for eid in E[q['id']]:
    for s in sorted(S[eid],key=lambda s:s['position']): print(f"## {s['label']}\n{s['body']}")
    for k in sorted(N[eid]): print(f"-- {k}: {N[eid][k]}")
