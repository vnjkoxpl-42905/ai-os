import json,glob,os,collections,sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'system' / 'scripts'))
from project_paths import project_path
DB='C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/'
BANK=str(project_path('lsatu-wt-glossary','public','data'))+'/'
if not glob.glob(BANK+'PT*-S*-LR.json'): sys.exit('No bank files at '+BANK)
L=lambda t: json.load(open(DB+t+'.json',encoding='utf-8'))
qs=L('lr_questions'); ex=L('lr_explanations'); st=L('lr_explanation_steps'); nt=L('lr_explanation_choice_notes')
steps=collections.Counter(s['explanation_id'] for s in st); notes=collections.Counter(n['explanation_id'] for n in nt)
byq=collections.defaultdict(list)
for e in ex:
  if e['style'] in('single','standard'): byq[e['question_id']].append(e['id'])
qslot={f"PT{q['preptest']}-S{q['section']}-Q{q['question_number']}":q for q in qs}
out=[]
for f in sorted(glob.glob(BANK+'PT*-S*-LR.json')):
  for b in json.load(open(f,encoding='utf-8')):
    if b.get('status')=='removed': continue
    slot=f"{b['practiceTest']}-S{b['sectionNumber']}-Q{b['questionNumber']}"
    q=qslot.get(slot)
    if not q: state='Unloaded'
    else:
      S=sum(steps[i] for i in byq[q['id']]); N=sum(notes[i] for i in byq[q['id']])
      state='Complete' if S and N>=5 else 'Partial-notes' if S and N else 'Notes-only' if N else 'Steps-only' if S else 'Unexplained'
    out.append(dict(slot=slot,state=state,type=b.get('questionType'),diff=b.get('questionDifficulty'),feat=b.get('questionFeatures') or [],reason=b.get('reasoningType') or []))
c=collections.Counter(o['state'] for o in out); print(len(out),c)
gaps=[o for o in out if o['state']!='Complete']
json.dump(gaps,open(os.path.dirname(__file__)+'/gaps.json','w'),indent=0)
print(collections.Counter(o['type'] for o in gaps).most_common(40))
