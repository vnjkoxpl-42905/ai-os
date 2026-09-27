import json,glob,collections,re,sys
sys.stdout.reconfigure(encoding='utf-8')
DB='C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/'
BANK='C:/Users/Joshu/dev/ai-os/projects/lsatu-wt-glossary/public/data/'
L=lambda t: json.load(open(DB+t+'.json',encoding='utf-8'))
qs=L('lr_questions'); ex=L('lr_explanations'); st=L('lr_explanation_steps'); nt=L('lr_explanation_choice_notes')
S=collections.defaultdict(list); N=collections.defaultdict(dict)
for s in st: S[s['explanation_id']].append(s)
for n in nt: N[n['explanation_id']][n['letter']]=n['body']
E={}
for e in ex:
  if e['style'] in('single','standard'): E[e['question_id']]=e
bank={}
for f in glob.glob(BANK+'PT*-S*-LR.json'):
  for b in json.load(open(f,encoding='utf-8')): bank[f"{b['practiceTest']}-S{b['sectionNumber']}-Q{b['questionNumber']}"]=b
def fam(t,stem=''):
  t=(t or '').lower(); s=(stem or '').lower()
  for k,v in [('parallel flaw','ParFlaw'),('parallel flawed','ParFlaw'),('parallel','Parallel'),('flaw','Flaw'),('paradox','Paradox'),('explain','Paradox'),('necessary','NA'),('sufficient','SA'),('method','Method'),('agree','AgreeDis'),('disagree','AgreeDis'),('principle-strengthen','PrinStr'),('principle strengthen','PrinStr'),('justif','PrinStr'),('principle','PrinConf'),('main','MC'),('role','Role'),('weaken','Weaken'),('strengthen','Strengthen'),('evaluate','Evaluate'),('must be false','MBF'),('must','MBT'),('support','MBT')]:
    if k in t: return v
  return 'Other'
def shape(text):
  t=(text or '').lower(); out=set()
  if re.search(r'\b(if|only if|unless|any|every|all|requires|must)\b',t): out.add('cond')
  if re.search(r'\b(cause|caused|because of|leads? to|result|effect|due to)\b',t): out.add('causal')
  if re.search(r'\b(study|studies|survey|researchers|percent|sample)\b',t): out.add('study')
  if re.search(r'\b(some|most|many|few)\b',t): out.add('quant')
  if re.search(r'\bshould\b',t): out.add('plan')
  if len(re.findall(r'^[A-Z][a-z]+:',text or '',re.M))>=2: out.add('2spk')
  return out
def quality(eid):
  steps=S[eid]; notes=N[eid]
  if not steps or len(notes)<5: return None
  txt=' '.join(s['body'] for s in steps)+' '+' '.join(notes.values())
  words=len(txt.split()); labels=' '.join(s['label'].lower() for s in steps)
  nw=[len(v.split()) for v in notes.values()]
  verdict=sum(1 for w in nw if w<20)
  tests=len(re.findall(r'negat|would (this|it) weaken|trigger|why should we believe|argue|how could|given that|imagine|for example|let\'s say|say ',txt,re.I))
  dash=txt.count('\u2014')/max(words,1)*1000
  q=min(words,900)/100 + ('goal' in labels or 'predict' in labels or 'anticipat' in labels)*2 - verdict*1.5 + min(tests,8)*0.5 - (dash>3)*4
  return round(q,1)
cand=[]
for q in qs:
  slot=f"PT{q['preptest']}-S{q['section']}-Q{q['question_number']}"
  e=E.get(q['id']); b=bank.get(slot)
  if not e or not b or b.get('status')=='removed' or not b.get('stimulus'): continue
  qu=quality(e['id'])
  if qu is None: continue
  cand.append(dict(slot=slot,fam=fam(q['question_type'] or b.get('questionType'),q['prompt']),feat=set(b.get('questionFeatures') or []),shape=shape(b['stimulus'])|({'except'} if 'except' in (b['questionStem'] or '').lower() else set()),diff=b.get('questionDifficulty'),q=qu))
json.dump([dict(c,feat=list(c['feat']),shape=list(c['shape'])) for c in cand],open('pilot/cand.json','w'))
picks=json.load(open('pilot/picks.json',encoding='utf-8'))
override={'PT156-S4-Q10':'Paradox','PT117-S3-Q8':'Method'}
res={}
for p in picks:
  f=override.get(p['slot'],p['fam']).replace('Parallel Flaw','ParFlaw')
  sh=shape(p['stimulus'])|({'except'} if 'except' in p['stem'].lower() else set())
  pf=set(p['feat'])
  sc=[]
  for c in cand:
    if c['fam']!=f or c['slot']==p['slot']: continue
    s=len(pf&c['feat'])*2+len(sh&c['shape'])+c['q']/2-abs((c['diff'] or 3)-(p['diff'] or 3))*0.5
    sc.append((round(s,1),c['slot'],c['q'],sorted(pf&c['feat']),sorted(sh&c['shape'])))
  sc.sort(reverse=True); res[p['slot']]=sc[:4]
  print(p['slot'],f,sorted(pf),sorted(sh),'pool',len(sc))
  for x in sc[:4]: print('   ',x)
json.dump(res,open('pilot/neighbors.json','w'))
