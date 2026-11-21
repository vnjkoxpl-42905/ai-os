"""Diff old vs new timed catalogs; emit qtype patch lists and Postgres-jsonb md5s."""
import json, hashlib, sys

BASE = r"C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/ea3d04fb-872d-45e2-bfa6-a69f0373cb16/scratchpad/rot3/base"
NEW = r"C:/Users/Joshu/dev/ai-os-projects/lsatu-wt-frozen/docs/implementation-plans/artifacts"


def pg_text(v):
    """Reproduce Postgres jsonb::text output."""
    if isinstance(v, dict):
        keys = sorted(v, key=lambda k: (len(k.encode('utf-8')), k.encode('utf-8')))
        return '{' + ', '.join(json.dumps(k, ensure_ascii=False) + ': ' + pg_text(v[k]) for k in keys) + '}'
    if isinstance(v, list):
        return '[' + ', '.join(pg_text(x) for x in v) + ']'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if v is None:
        return 'null'
    if isinstance(v, (int, float)):
        return json.dumps(v)
    return json.dumps(v, ensure_ascii=False)


md5 = lambda v: hashlib.md5(pg_text(v).encode('utf-8')).hexdigest()


def diff(a, b, path=()):
    if type(a) != type(b):
        yield path, a, b; return
    if isinstance(a, dict):
        for k in set(a) | set(b):
            if k not in a or k not in b: yield path + (k,), a.get(k), b.get(k)
            else: yield from diff(a[k], b[k], path + (k,))
    elif isinstance(a, list):
        if len(a) != len(b): yield path, len(a), len(b); return
        for i, (x, y) in enumerate(zip(a, b)): yield from diff(x, y, path + (i,))
    elif a != b:
        yield path, a, b


out = {}
# PT catalog
o = json.load(open(BASE + r"/timed-content-manifest-v1.generated.json", encoding='utf-8'))
n = json.load(open(NEW + r"/timed-content-manifest-v1.generated.json", encoding='utf-8'))
ob = {b['pt']: b for b in o['blueprints']}; nb = {b['pt']: b for b in n['blueprints']}
assert set(ob) == set(nb)
pt_patches = []
for pt in sorted(ob):
    for path, a, b in diff(ob[pt], nb[pt]):
        assert len(path) == 5 and path[0] == 'legs' and path[2] == 'questions' and path[4] in ('qtype', 'contentSha256'), (pt, path)
        pt_patches.append((pt, path[1], path[3], path[4], b, a))
out['pt'] = dict(old=o['manifestSha256'], new=n['manifestSha256'], patches=pt_patches,
                 old_md5={pt: md5(ob[pt]) for pt in ob}, new_md5={pt: md5(nb[pt]) for pt in nb})
# Section catalog
o = json.load(open(BASE + r"/timed-section-all-sections-v2.generated.json", encoding='utf-8'))
n = json.load(open(NEW + r"/timed-section-all-sections-v2.generated.json", encoding='utf-8'))
key = lambda s: (s['pt'], s['definition']['kind'], s['definition']['section'])
os_ = {key(s): s['definition'] for s in o['sections']}; ns = {key(s): s['definition'] for s in n['sections']}
assert set(os_) == set(ns)
sec_patches = []
for k in sorted(os_):
    for path, a, b in diff(os_[k], ns[k]):
        assert len(path) == 3 and path[0] == 'questions' and path[2] in ('qtype', 'contentSha256'), (k, path)
        sec_patches.append((k[0], k[1], k[2], path[1], path[2], b, a))
out['sec'] = dict(old=o['manifestSha256'], new=n['manifestSha256'], patches=sec_patches,
                  old_md5={f'{k[0]}|{k[1]}|{k[2]}': md5(v) for k, v in os_.items()},
                  new_md5={f'{k[0]}|{k[1]}|{k[2]}': md5(v) for k, v in ns.items()})
json.dump(out, open('catdiff.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('PT', out['pt']['old'][:8], '->', out['pt']['new'][:8], 'qtype patches', len(pt_patches), 'PTs touched', len({p[0] for p in pt_patches}))
print('SEC', out['sec']['old'][:8], '->', out['sec']['new'][:8], 'qtype patches', len(sec_patches), 'sections touched', len({p[:3] for p in sec_patches}))
