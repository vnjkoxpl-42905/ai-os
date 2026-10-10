"""Build guarded SQL for step 3.
Usage: python -I apply3.py <out_prefix> <proposals.jsonl> <verdicts.jsonl> [more pairs...]
Resolves each rewrite to its final steps/notes (proposal, or verifier's fix), runs hard gates,
then writes guarded UPDATEs (old body must still match) and guarded INSERTs, plus <prefix>-final.json (old kept as snapshot)."""
import json, sys, re, os, hashlib
md5 = lambda s: hashlib.md5(s.encode('utf-8')).hexdigest()
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
GENDER = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
prefix = sys.argv[1]
pairs = [(sys.argv[i], sys.argv[i + 1]) for i in range(2, len(sys.argv), 2)]
q = lambda s: "'" + s.replace("'", "''") + "'"
final, held = [], []
for pf, vf in pairs:
    props = [json.loads(l) for l in open(pf, encoding='utf-8') if l.strip()]
    verd = {}
    for l in open(vf, encoding='utf-8'):
        if l.strip():
            v = json.loads(l); verd[v['qid']] = v
    for p in props:
        if p.get('action') != 'rewrite': continue
        v = verd.get(p['qid'])
        if not v: held.append((p['qid'], 'no verdict')); continue
        if v['verdict'] not in ('approve', 'fix'): held.append((p['qid'], v['verdict'] + ': ' + v.get('note', ''))); continue
        steps, notes = (v['new']['steps'], v['new']['notes']) if v['verdict'] == 'fix' else (p['steps'], p['notes'])
        pk = json.load(open(f"{HERE}/packets/{p['qid']}.json", encoding='utf-8'))
        old_steps = {s['row_id']: s for s in pk['steps']}
        old_notes = {n['row_id']: n for n in pk['notes']}
        text = ' '.join([s['body'] + ' ' + (s['label'] or '') for s in steps] + [n['body'] for n in notes])
        old_text = ' '.join([s['body'] + ' ' + (s['label'] or '') for s in pk['steps']] + [n['body'] for n in pk['notes']])
        err = None
        if '—' in text or '–' in text: err = 'dash'
        elif len(GENDER.findall(text)) > len(GENDER.findall(old_text)): err = 'pronoun'
        elif 'logic game' in text.lower(): err = 'logic games'
        elif sorted(n['letter'] for n in notes) != list('ABCDE'): err = 'notes not A-E'
        elif any(not n['body'].strip() for n in notes) or any(not s['body'].strip() for s in steps): err = 'empty body'
        elif set(old_steps) - {s['row_id'] for s in steps}: err = 'dropped a step row'
        elif any(s['row_id'] and s['row_id'] not in old_steps for s in steps) or any(n['row_id'] and n['row_id'] not in old_notes for n in notes): err = 'unknown row id'
        if err: held.append((p['qid'], 'gate: ' + err)); continue
        final.append({'qid': p['qid'], 'explanation_id': pk['explanation_id'], 'steps': steps, 'notes': notes, 'old_steps': pk['steps'], 'old_notes': pk['notes']})
print('final', len(final), 'held', len(held))
for h in held: print('  HELD', h)
json.dump(final, open(prefix + '-final.json', 'w', encoding='utf-8'), ensure_ascii=False)
upd_steps, upd_notes, ins_steps, ins_notes = [], [], [], []
for f in final:
    os_ = {s['row_id']: s for s in f['old_steps']}; on = {n['row_id']: n for n in f['old_notes']}
    for s in f['steps']:
        if s['row_id']:
            o = os_[s['row_id']]
            if o['body'] != s['body'] or (o['label'] or '') != (s['label'] or ''): upd_steps.append((s['row_id'], o['body'], s['body'], o['label'] or '', s['label'] or ''))
        else: ins_steps.append((f['explanation_id'], s['position'], s['label'] or '', s['body']))
    for n in f['notes']:
        if n['row_id']:
            o = on[n['row_id']]
            if o['body'] != n['body']: upd_notes.append((n['row_id'], o['body'], n['body']))
        else: ins_notes.append((f['explanation_id'], n['letter'], n['body']))
print('updates: steps', len(upd_steps), 'notes', len(upd_notes), '| inserts: steps', len(ins_steps), 'notes', len(ins_notes))
files = []
def chunks(rows, size_of):
    cur, sz = [], 0
    for r in rows:
        s = size_of(r)
        if cur and sz + s > 50000: yield cur; cur, sz = [], 0
        cur.append(r); sz += s
    if cur: yield cur
for rows in chunks(upd_steps, lambda r: len(r[2]) + 200):
    vals = ',\n'.join(f"({q(r[0])}::uuid,{q(md5(r[1]))},{q(r[2])},{q(r[3])},{q(r[4])})" for r in rows)
    files.append(f"update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values\n{vals}\n) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;")
for rows in chunks(upd_notes, lambda r: len(r[2]) + 100):
    vals = ',\n'.join(f"({q(r[0])}::uuid,{q(md5(r[1]))},{q(r[2])})" for r in rows)
    files.append(f"update lr_explanation_choice_notes t set body=v.nb from (values\n{vals}\n) v(id,ob,nb) where t.id=v.id and md5(t.body)=v.ob returning t.id;")
for rows in chunks(ins_steps, lambda r: len(r[3]) + 200):
    vals = ',\n'.join(f"({q(r[0])}::uuid,{r[1]},{q(r[2])},{q(r[3])})" for r in rows)
    files.append(f"insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values\n{vals}\n) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;")
for rows in chunks(ins_notes, lambda r: len(r[2]) + 150):
    vals = ',\n'.join(f"({q(r[0])}::uuid,{q(r[1])},{q(r[2])})" for r in rows)
    files.append(f"insert into lr_explanation_choice_notes (explanation_id,letter,body) select v.e,v.l,v.b from (values\n{vals}\n) v(e,l,b) where not exists (select 1 from lr_explanation_choice_notes x where x.explanation_id=v.e and x.letter=v.l) returning id;")
for i, s in enumerate(files, 1):
    open(f"{prefix}-{i:02d}.sql", 'w', encoding='utf-8').write(s)
print(len(files), 'sql files')
