"""Merge reviewed step-2 verdicts into a final edit set and emit guarded SQL batches.
Usage: python3 -I build_apply.py [batch_size]
Inputs: all-proposals.json, review/verdicts-*.jsonl, gap/verdicts-gap.jsonl (optional), overrides.json (optional).
Outputs: apply/final-edits.json, apply/batch-NNN.sql, apply/states.json. No database access."""
import json, glob, os, sys, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
BATCH = int(sys.argv[1]) if len(sys.argv) > 1 else 40
G = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)

props = {p['pid']: p for p in json.load(open('all-proposals.json', encoding='utf-8')) if 'row_id' in p}
if os.path.exists('gap/proposals-gap.json'):
    for p in json.load(open('gap/proposals-gap.json', encoding='utf-8')):
        if 'row_id' in p: props[p['pid']] = p
verd = {}
for f in sorted(glob.glob('review/verdicts-*.jsonl')) + sorted(glob.glob('gap/verdicts-*.jsonl')):
    for l in open(f, encoding='utf-8'):
        if l.strip():
            v = json.loads(l); verd[v['pid']] = v
over = json.load(open('overrides.json', encoding='utf-8')) if os.path.exists('overrides.json') else {}
for pid, v in over.items(): verd[pid] = dict(v, pid=pid, override=True)

states = {}; final = {}; probs = []
for pid, p in props.items():
    v = verd.get(pid)
    if not v: states[pid] = 'proposed'; continue
    if v['verdict'] == 'reject': states[pid] = 'rejected'; continue
    new = v['new'] if v['verdict'] == 'fix' else p['new']
    key = (p['table'], p['row_id'], p['column'])
    if key in final: probs.append(f'two passing edits for {key}: {final[key]["pid"]} and {pid}'); continue
    if '—' in new: probs.append(f'{pid}: em dash'); continue
    if len(G.findall(new)) > len(G.findall(p['old'])): probs.append(f'{pid}: adds gendered pronoun'); continue
    final[key] = dict(pid=pid, qid=p['qid'], table=p['table'], row_id=p['row_id'], column=p['column'],
                      old=p['old'], new=new, verdict=v['verdict'], review_note=v.get('note', ''))
    states[pid] = 'reviewed-' + v['verdict']

os.makedirs('apply', exist_ok=True)
for f in glob.glob('apply/batch-*.sql'): os.remove(f)
edits = sorted(final.values(), key=lambda e: (e['qid'], e['table'], e['row_id'], e['column']))
json.dump(edits, open('apply/final-edits.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(states, open('apply/states.json', 'w', encoding='utf-8'), indent=0)

def lit(s, tag):
    assert f'${tag}$' not in s
    return f'${tag}${s}${tag}$'

for b in range(0, len(edits), BATCH):
    chunk = edits[b:b + BATCH]; n = b // BATCH
    lines = ['DO $apply$', 'DECLARE n int; total int := 0;', 'BEGIN']
    for e in chunk:
        lines.append(f"  UPDATE public.{e['table']} SET {e['column']} = {lit(e['new'], 'v')} "
                     f"WHERE id = '{e['row_id']}' AND {e['column']} = {lit(e['old'], 'o')};")
        lines.append(f"  GET DIAGNOSTICS n = ROW_COUNT; IF n <> 1 THEN RAISE EXCEPTION 'CAS conflict on {e['pid']} {e['qid']} {e['row_id']}'; END IF; total := total + n;")
    lines.append(f"  IF total <> {len(chunk)} THEN RAISE EXCEPTION 'expected {len(chunk)} rows, got %', total; END IF;")
    lines += ['END $apply$;', '']
    open(f'apply/batch-{n:03d}.sql', 'w', encoding='utf-8').write('\n'.join(lines))

print('passing edits', len(edits), 'states', collections.Counter(states.values()),
      'batches', -(-len(edits) // BATCH), 'problems', len(probs))
for p in probs: print('  ', p)
