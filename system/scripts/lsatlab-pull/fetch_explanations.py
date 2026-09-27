"""Fetch LSAT Lab's written explanation (Standard approach steps + per-choice
Standard notes) from public pages for a list of slots.
Usage: python <this> --slots-file slots.txt --out explanations.json
"""
import argparse, json, re, urllib.request, time
from concurrent.futures import ThreadPoolExecutor
UA = {'User-Agent': 'Mozilla/5.0 (LSAT U audit; contact@aspiringattorneys.com)'}

def decode(slot):
    for i in range(3):
        try:
            h = urllib.request.urlopen(urllib.request.Request('https://www.lsatlab.com/lsat-explanations/' + slot, headers=UA), timeout=30).read().decode('utf-8', 'replace')
            break
        except Exception:
            time.sleep(2 * (i + 1)); h = ''
    ch = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', h, re.S)
    return ''.join(json.loads('"' + c + '"') for c in ch)

def grab_json(t, key):
    i = t.find(key)
    if i < 0: return None
    j = t.index('{', i + len(key) - 1); depth = 0; s = False; esc = False
    for k in range(j, len(t)):
        c = t[k]
        if s:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': s = False
        elif c == '"': s = True
        elif c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0: return json.loads(t[j:k + 1])
    return None

def one(slot):
    t = decode(slot)
    ap = grab_json(t, '"approaches":{') or {}
    notes = {}
    for m in re.finditer(r'"letter":"([A-E])"', t):
        seg = t[m.start():m.start() + 20000]
        ex = grab_json(seg, '"explanations":{')
        if m[1] not in notes and ex is not None: notes[m[1]] = (ex.get('standard') or {})
    std = ap.get('standard') or {}
    return {'slot': slot, 'type': std.get('type'), 'steps': std.get('steps') or [], 'notes': notes,
            'has_brief': bool(ap.get('brief')), 'has_another_way': bool(ap.get('anotherWay'))}

if __name__ == '__main__':
    a = argparse.ArgumentParser(); a.add_argument('--slots-file'); a.add_argument('--out'); a = a.parse_args()
    slots = [l.strip() for l in open(a.slots_file) if l.strip()]
    with ThreadPoolExecutor(6) as ex: res = list(ex.map(one, slots))
    json.dump(res, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(res), 'fetched;', sum(1 for r in res if r['steps']), 'with steps')
