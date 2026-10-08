"""Helper: append proposals. Usage in spec scripts: from prop import P, skip, flag"""
import json, os, sys
DB='/home/user/ai-os/system/scripts/lsatlab-pull/data/db/'
OUT='/home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/gap/out-gap.jsonl'
L=lambda t: json.load(open(DB+t+'.json',encoding='utf-8'))
_st={r['id']:r for r in L('lr_explanation_steps')}
_nt={r['id']:r for r in L('lr_explanation_choice_notes')}
_ex={r['id']:r for r in L('lr_explanations')}
_q={r['id']:r for r in L('lr_questions')}
def _w(o):
    with open(OUT,'a',encoding='utf-8') as f: f.write(json.dumps(o,ensure_ascii=False)+'\n')
def P(item,qid,row_id,reps,kind,why,evidence,column='body',new=None):
    if row_id in _st: table='lr_explanation_steps'; r=_st[row_id]
    elif row_id in _nt: table='lr_explanation_choice_notes'; r=_nt[row_id]
    else: raise SystemExit('no row '+row_id)
    e=_ex[r['explanation_id']]; assert _q[e['question_id']]['qid']==qid,(qid,_q[e['question_id']]['qid'])
    old=r[column]
    if new is None:
        new=old
        for a,b in reps:
            c=new.count(a)
            if c!=1: raise SystemExit(f'{row_id}: {a!r} occurs {c}x')
            new=new.replace(a,b)
    assert new!=old and '—' not in new
    o={'item':item,'qid':qid,'table':table,'row_id':row_id,'column':column,'style':e['style']}
    if table.endswith('notes'): o['letter']=r['letter']
    o.update(old=old,new=new,kind=kind,why=why,evidence=evidence)
    _w(o); print('ok',qid,table[15:],e['style'],r.get('letter',r.get('label')))
def skip(item,qid,reason): _w({'item':item,'qid':qid,'skip':reason}); print('skip',qid)
def flag(item,qid,reason): _w({'item':item,'qid':qid,'flag':reason}); print('flag',qid)
