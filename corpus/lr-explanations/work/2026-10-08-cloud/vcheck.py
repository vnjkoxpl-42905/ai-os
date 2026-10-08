"""Self-check a verdicts JSONL against its chunk. Usage: python3 -I vcheck.py chunk.json verdicts.jsonl"""
import json, re, sys, collections
G = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
chunk = json.load(open(sys.argv[1], encoding='utf-8'))
by = {p['pid']: p for p in chunk}
v = [json.loads(l) for l in open(sys.argv[2], encoding='utf-8') if l.strip()]
probs = []
seen = set(); final = collections.Counter()
for x in v:
    p = by.get(x.get('pid'))
    if not p: probs.append(('unknown pid', x.get('pid'))); continue
    if x['pid'] in seen: probs.append(('pid twice', x['pid']))
    seen.add(x['pid'])
    if x.get('verdict') not in ('approve', 'fix', 'reject'): probs.append(('bad verdict', x['pid']))
    if x.get('verdict') in ('approve', 'fix'):
        final[(p['row_id'], p.get('column'))] += 1
        new = x['new'] if x['verdict'] == 'fix' else p['new']
        if not new or not new.strip(): probs.append(('empty final', x['pid']))
        if '—' in new: probs.append(('em dash in final', x['pid']))
        if len(G.findall(new)) > len(G.findall(p['old'])): probs.append(('adds gendered pronoun', x['pid']))
        if re.search(r'logic games?', new, re.I): probs.append(('mentions Logic Games', x['pid']))
        if new == p['old']: probs.append(('final equals old (no-op)', x['pid']))
missing = [p['pid'] for p in chunk if p['pid'] not in seen]
if missing: probs.append(('missing verdicts', missing))
for r, n in final.items():
    if n > 1: probs.append(('more than one approve/fix for row+column', r))
print('verdicts', collections.Counter(x.get('verdict') for x in v), 'problems', len(probs))
for pr in probs: print('  ', pr)
