import json, glob, re, os, copy
BANK = r"C:\Users\Joshu\dev\ai-os-projects\lsatu-wt-bankfix-b02\public\data"
V = {r['slot']: r for r in json.load(open('verdict.json', encoding='utf-8'))}

def fmt_of(raw, d):
    for ind in (2, 4):
        for asc in (False, True):
            s = json.dumps(d, indent=ind, ensure_ascii=asc)
            for nl in ('\n', '\r\n'):
                t = s.replace('\n', nl)
                for tail in ('', nl):
                    if t + tail == raw:
                        return ind, asc, nl, tail
    raise SystemExit('no round-trip format')

log = []
for f in sorted(glob.glob(os.path.join(BANK, 'PT*-S*-LR.json'))):
    raw = open(f, 'rb').read().decode('utf-8')
    d = json.loads(raw)
    ind, asc, nl, tail = fmt_of(raw, d)
    orig = copy.deepcopy(d)
    for q in d:
        if q.get('status') == 'removed':
            continue
        slot = f"{q['practiceTest']}-S{q['sectionNumber']}-Q{q['questionNumber']}"
        r = V[slot]
        if r['app'] != r['verdict']:
            log.append(dict(slot=slot, field='questionType', old=q.get('questionType'), new=r['verdict']))
            q['questionType'] = r['verdict']
        if re.search(r'\bexcept\b', q.get('questionStem', ''), re.I):
            feats = q.get('questionFeatures') or []
            if not any('except' in x.lower() for x in feats):
                log.append(dict(slot=slot, field='questionFeatures', old=q.get('questionFeatures'), new=feats + ['EXCEPT']))
                q['questionFeatures'] = feats + ['EXCEPT']
    if d != orig:
        for a, b in zip(orig, d):
            if a != b:
                assert set(k for k in set(a) | set(b) if a.get(k) != b.get(k)) <= {'questionType', 'questionFeatures'}, f
        out = json.dumps(d, indent=ind, ensure_ascii=asc).replace('\n', nl) + tail
        open(f, 'wb').write(out.encode('utf-8'))

json.dump(log, open('bank-changes.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len([l for l in log if l['field'] == 'questionType']), 'type changes,', len([l for l in log if l['field'] == 'questionFeatures']), 'EXCEPT tags')
