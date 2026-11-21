"""Mechanical checks on a proposals JSONL: old matches mirror, no new em dashes or gendered pronouns, sane edits."""
import json, sys, re, collections, difflib
DB = 'C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/'
steps = {r['id']: r for r in json.load(open(DB + 'lr_explanation_steps.json', encoding='utf-8'))}
notes = {r['id']: r for r in json.load(open(DB + 'lr_explanation_choice_notes.json', encoding='utf-8'))}
tables = {'lr_explanation_steps': steps, 'lr_explanation_choice_notes': notes}
GENDER = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
c = collections.Counter(); problems = []; edits = []
seen = {}
for line in open(sys.argv[1], encoding='utf-8'):
    if not line.strip(): continue
    p = json.loads(line)
    if 'skip' in p: c['skip'] += 1; continue
    if 'flag' in p: c['flag'] += 1; continue
    c['edit'] += 1
    t = tables.get(p['table'])
    key = (p['table'], p['row_id'], p['column'])
    if t is None or p['column'] not in ('body', 'label'): problems.append(('bad table/column', p['qid'], key)); continue
    row = t.get(p['row_id'])
    if row is None: problems.append(('row missing', p['qid'], key)); continue
    if row[p['column']] != p['old']: problems.append(('old != mirror', p['qid'], key))
    if p['old'] == p['new']: problems.append(('no-op', p['qid'], key))
    if key in seen: problems.append(('duplicate row', p['qid'], key))
    seen[key] = p
    new_dash = p['new'].count('\u2014') - p['old'].count('\u2014')
    if new_dash > 0: problems.append(('adds em dash', p['qid'], key))
    og = len(GENDER.findall(p['old'])); ng = len(GENDER.findall(p['new']))
    if ng > og: problems.append(('adds gendered pronoun', p['qid'], key))
    if not p['new'].strip(): problems.append(('empty new', p['qid'], key))
    ratio = difflib.SequenceMatcher(None, p['old'], p['new']).ratio()
    edits.append((ratio, p))
print(dict(c), 'problems', len(problems))
for pr in problems: print('  ', pr)
if len(sys.argv) > 2:
    json.dump([p for _, p in edits], open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
