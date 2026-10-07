"""Crawl LSAT Lab's public explanation pages for every LR question in the LSAT U
bank and save what each page says, for audit_bank.py to compare.

No login needed. One page per question: www.lsatlab.com/lsat-explanations/PT<n>-S<s>-Q<q>
(redirects to the full slug). Each page also embeds its whole test's question list
(slug, key, type tag, difficulty), which reveals questions LSAT Lab has and the bank lacks.

Usage (from an LSAT U checkout root):
  python <this> [--pts 113,117] [--workers 6]
Writes data/public/<slot>.json and data/public/_lists.json next to this file.
Already-fetched slots are skipped; delete data/public/ to refetch.
"""
import argparse, glob, json, os, re, time, urllib.request, html as H
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'public')
UA = {'User-Agent': 'Mozilla/5.0 (LSAT U audit; contact@aspiringattorneys.com)'}
ITEM = re.compile(r'\{"slug":"PT\d+-S\d+-(?:P\d+-)?Q\d+".*?"canonicalPath":"[^"]+"\}')

def fetch(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.status, r.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code == 404: return 404, ''
            time.sleep(2 * (i + 1))
        except Exception:
            time.sleep(2 * (i + 1))
    return 0, ''

def rsc(page):
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', page, re.S)
    return ''.join(json.loads('"' + c + '"') if True else c for c in chunks)

def parse(slot, page):
    try: t = rsc(page)
    except Exception: t = ''
    items = []
    for m in ITEM.findall(t):
        try: items.append(json.loads(m))
        except Exception: pass
    me = next((i for i in items if i['slug'] == slot), None)
    # answers block for this question: letter, correct flag, percent, trap, explanation text
    answers = {}
    for m in re.finditer(r'\{"letter":"([A-E])","text":\[.*?\],"correct":(true|false),"percent":(\d+|null)(?:,"trap":("(?:[^"\\]|\\.)*"|null))?(?:,"explanation":("(?:[^"\\]|\\.)*"|null))?', t):
        L = m[1]
        if L in answers: continue
        answers[L] = {'correct': m[2] == 'true', 'percent': None if m[3] == 'null' else int(m[3]),
                      'trap': json.loads(m[4]) if m[4] and m[4] != 'null' else None,
                      'explanation': json.loads(m[5]) if m[5] and m[5] != 'null' else None}
    text = H.unescape(re.sub(r'<[^>]+>', ' ', page))
    steps = [H.unescape(s).strip() for s in re.findall(r'<h5[^>]*>(.*?)</h5>', page, re.S)]
    return {'slot': slot, 'list_entry': me, 'answers': answers,
            'key': next((L for L, a in answers.items() if a['correct']), None) or (me or {}).get('correctAnswer'),
            'steps': [re.sub(r'<[^>]+>', '', s) for s in steps],
            'norm_text': re.sub(r'\W+', '', text.lower())}, items

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--pts'); ap.add_argument('--workers', type=int, default=6)
    a = ap.parse_args(); os.makedirs(OUT, exist_ok=True)
    want = {int(x) for x in a.pts.split(',')} if a.pts else None
    slots = []
    for f in sorted(glob.glob('public/data/PT*-LR.json')):
        for q in json.load(open(f, encoding='utf-8')):
            pt = int(q['practiceTest'][2:])
            if want and pt not in want: continue
            slots.append(f"PT{pt}-S{q['sectionNumber']}-Q{q['questionNumber']}")
    lists_path = os.path.join(OUT, '_lists.json')
    lists = json.load(open(lists_path, encoding='utf-8')) if os.path.exists(lists_path) else {}
    todo = [s for s in slots if not os.path.exists(os.path.join(OUT, s + '.json'))]
    print(f'{len(slots)} slots, {len(todo)} to fetch')
    def one(slot):
        code, page = fetch(f'https://www.lsatlab.com/lsat-explanations/{slot}')
        if code != 200:
            rec = {'slot': slot, 'status': code}; items = []
        else:
            rec, items = parse(slot, page); rec['status'] = 200
        json.dump(rec, open(os.path.join(OUT, slot + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        return slot, items
    done = 0
    with ThreadPoolExecutor(a.workers) as ex:
        for slot, items in ex.map(one, todo):
            pt = slot.split('-')[0]
            if items and pt not in lists: lists[pt] = items
            done += 1
            if done % 200 == 0: print(done, 'fetched'); json.dump(lists, open(lists_path, 'w', encoding='utf-8'))
    json.dump(lists, open(lists_path, 'w', encoding='utf-8'))
    print('done')

if __name__ == '__main__':
    main()
