"""LR explanation coverage: live lr_* tables vs the question bank.

Writes wiki/lr-missing-explanations.md and wiki/lr-missing-explanations-by-category.md.
States (brainstorms/2026-09-26-lr-explanation-coverage.md): Complete, Notes-only
(Choice Notes, no Argument Breakdown), Unexplained (neither), Unloaded (in the bank,
not in lr_questions). Read-only against the database.

Run from the vault root: python system/scripts/lr-explanation-coverage.py
"""
import collections, glob, json, re, urllib.request, datetime

env={}
for f in ['.env','projects/lsatu/.env']:
  for l in open(f,encoding='utf-8'):
    m=re.match(r'([A-Z_]+)=(.*)',l.strip())
    if m: env[m[1]]=m[2].strip('"')
U=env['VITE_SUPABASE_URL'];K=env['VITE_SUPABASE_PUBLISHABLE_KEY']
def req(p,body=None,tok=None):
  r=urllib.request.Request(U+p,data=json.dumps(body).encode() if body else None,headers={'apikey':K,'Content-Type':'application/json','Authorization':'Bearer '+(tok or K)})
  return json.load(urllib.request.urlopen(r))
tok=req('/auth/v1/token?grant_type=password',{'email':env['LSATPREP_ADMIN_EMAIL'],'password':env['LSATPREP_ADMIN_PASSWORD']})['access_token']
def all_(t,sel):
  out=[];o=0
  while True:
    b=req(f'/rest/v1/{t}?select={sel}&limit=1000&offset={o}',tok=tok);out+=b;o+=1000
    if len(b)<1000:return out

Q=all_('lr_questions','id,preptest,section,question_number')
E=all_('lr_explanations','id,question_id')
steps={s['explanation_id'] for s in all_('lr_explanation_steps','explanation_id')}
notes={n['explanation_id'] for n in all_('lr_explanation_choice_notes','explanation_id')}
byq=collections.defaultdict(list)
for e in E: byq[e['question_id']].append(e['id'])
st={}
for q in Q:
  k=(q['preptest'],q['section'],q['question_number']); ids=byq.get(q['id'],[])
  if any(i in steps for i in ids): continue
  st[k]='Notes-only' if any(i in notes for i in ids) else 'Unexplained'
indb={(q['preptest'],q['section'],q['question_number']) for q in Q}
M={}
for f in glob.glob('projects/lsatu/public/data/PT*-LR.json'):
  for x in json.load(open(f,encoding='utf-8')):
    k=(int(str(x['practiceTest']).lstrip('PT')),int(x['sectionNumber']),int(x['questionNumber']))
    M[k]=x
    if k not in indb: st[k]='Unloaded'
D=datetime.date.today().isoformat();keys=sorted(st);C=collections.Counter(st.values())
ORDER=['Unexplained','Notes-only','Unloaded']
lst=lambda x:x if isinstance(x,list) else ([x] if x else [])
o=[f"""# LR questions missing explanations

Generated {D} by `system/scripts/lr-explanation-coverage.py` from the live LSAT U database and the question bank (`projects/lsatu/public/data/PT*-LR.json`). LR only. Regenerate; do not hand-edit.

States follow [[../brainstorms/2026-09-26-lr-explanation-coverage]]. Only Complete (Argument Breakdown plus Choice Notes) counts as explained.

| State | Meaning | Count |
|---|---|---|
| Unexplained | In the explanation tables, no Argument Breakdown and no Choice Notes | {C['Unexplained']} |
| Notes-only | Choice Notes, no Argument Breakdown | {C['Notes-only']} |
| Unloaded | In the question bank, not in the explanation tables | {C['Unloaded']} |
| **Total missing** | | **{len(st)}** of {len(M)} |

By type, reasoning and features: [[lr-missing-explanations-by-category]].
"""]
bypt=collections.defaultdict(list)
for k in keys: bypt[k[0]].append(k)
for pt in sorted(bypt):
  ks=bypt[pt];cc=collections.Counter(st[k] for k in ks)
  o.append(f"\n## PT{pt} ({len(ks)}: "+", ".join(f"{cc[s]} {s.lower()}" for s in ORDER if cc[s])+")\n")
  for sec in sorted({k[1] for k in ks}):
    for s in ORDER:
      qs=[k[2] for k in ks if k[1]==sec and st[k]==s]
      if qs: o.append(f"- **S{sec}, {s}:** "+", ".join(f"Q{q}" for q in qs))
open('wiki/lr-missing-explanations.md','w',encoding='utf-8').write("\n".join(o)+"\n")
def fam(t):
  t=(t or '').lower()
  for p,n in [('parallel','Parallel / Parallel Flaw'),('principle|psa','Principle'),('sufficient','Sufficient Assumption'),('necessary','Necessary Assumption'),('paradox|resolve|explain','Paradox'),('weaken','Weaken'),('strengthen','Strengthen'),('flaw','Flaw'),('method|descriptive','Method'),('role|argument part','Role'),('conclusion|main point','Main Conclusion'),('agree|dispute|point at issue','Agree/Disagree'),('must be false','Must Be False'),('must be true|supported|fill in|complete the','Must Be True / Most Supported'),('evaluat','Evaluate')]:
    if re.search(p,t): return n
  return 'Other / unlabeled'
def tab(title,col,get):
  c=collections.defaultdict(collections.Counter)
  for k in keys:
    for v in (get(M[k]) or ['(none)']): c[v][st[k]]+=1
  r=[f"## {title}\n",f"| {col} | "+" | ".join(ORDER)+" | Total |","|---|---|---|---|---|"]
  for v,cc in sorted(c.items(),key=lambda x:-sum(x[1].values())):
    r.append(f"| {v} | "+" | ".join(str(cc[s]) for s in ORDER)+f" | {sum(cc.values())} |")
  return "\n".join(r)+"\n"
o=[f"""# LR missing explanations, by category

Same {len(st)} questions as [[lr-missing-explanations]], generated {D}. Type, reasoning, features and difficulty come from the question bank. A question with several reasoning types or features counts under each, so those tables sum past {len(st)}. Family grouping of raw type labels is Claude's, not canonical.
""",tab('By question type, grouped','Family',lambda m:[fam(m.get('questionType'))]),
tab('By question type (raw labels)','Type',lambda m:lst(m.get('questionType'))),
tab('By reasoning type','Reasoning',lambda m:lst(m.get('reasoningType'))),
tab('By feature','Feature',lambda m:lst(m.get('questionFeatures'))),
tab('By difficulty','Difficulty',lambda m:[str(m['questionDifficulty'])] if m.get('questionDifficulty') is not None else []),
"## Every question\n","| PT | S | Q | State | Type | Reasoning | Features | Diff |","|---|---|---|---|---|---|---|---|"]
for k in keys:
  m=M[k];o.append(f"| {k[0]} | {k[1]} | {k[2]} | {st[k]} | {m.get('questionType') or ''} | {'; '.join(lst(m.get('reasoningType')))} | {'; '.join(lst(m.get('questionFeatures')))} | {m.get('questionDifficulty') if m.get('questionDifficulty') is not None else ''} |")
open('wiki/lr-missing-explanations-by-category.md','w',encoding='utf-8').write("\n".join(o)+"\n")
print(dict(C),'total',len(st))
