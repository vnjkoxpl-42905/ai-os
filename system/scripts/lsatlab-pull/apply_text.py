"""Overwrite chosen fields of chosen bank slots with LSAT Lab's official text.

Usage (from an LSAT U checkout root):
  python <this> --pull data/received/<pull>.json --fix PT117-S2-Q6=choices PT102-S4-Q17=stimulus,stem PT143-S4-Q5=choice:D [--key]
Fields: stimulus, stem, choices (all five), choice:<L> (one), key.
--key must be passed explicitly before any correctAnswer is changed.
"""
import argparse, glob, html as H, json, re

def clean(h, keep_paras=True):
    s = re.sub(r'<br\s*/?>', '\n', h or '', flags=re.I)
    s = re.sub(r'</p\s*>', '\n\n', s, flags=re.I)
    s = H.unescape(re.sub(r'<[^>]+>', '', s)).replace('\xa0', ' ').replace('\r', '')
    paras = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n', s)]
    paras = [p for p in paras if p]
    return paras if keep_paras else ' '.join(paras)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--pull', required=True); ap.add_argument('--fix', nargs='+', required=True); ap.add_argument('--key', action='store_true')
    a = ap.parse_args()
    lab = {f"PT{r['pt']}-S{r['sec']}-Q{r['pos']}": r for r in json.load(open(a.pull, encoding='utf-8'))}
    want = {}
    for f in a.fix:
        slot, fields = f.split('='); want[slot] = fields.split(',')
    done = []
    for path in sorted(glob.glob('public/data/PT*-LR.json')):
        raw = open(path, encoding='utf-8').read(); items = json.loads(raw); changed = False
        for q in items:
            slot = f"{q['practiceTest']}-S{q['sectionNumber']}-Q{q['questionNumber']}"
            if slot not in want: continue
            r = lab[slot]; paras = clean(r['questiontext'])
            choices = {'ABCDE'[x['pos'] - 1]: clean(x['text'], False) for x in r['answers']}
            for fld in want[slot]:
                if fld == 'stimulus': q['stimulus'] = '\n'.join(paras[:-1])
                elif fld == 'stem': q['questionStem'] = paras[-1]
                elif fld == 'choices': q['answerChoices'] = {L: choices[L] for L in 'ABCDE'}
                elif fld.startswith('choice:'): q['answerChoices'][fld[7:]] = choices[fld[7:]]
                elif fld == 'key':
                    if not a.key: raise SystemExit(f'{slot}: key change needs --key')
                    q['correctAnswer'] = r['key']
                else: raise SystemExit('unknown field ' + fld)
            changed = True; done.append(slot)
        if changed:
            open(path, 'w', encoding='utf-8', newline='\n').write(json.dumps(items, ensure_ascii=False, indent=2) + ('\n' if raw.endswith('\n') else ''))
    print('updated', len(done), sorted(done))

if __name__ == '__main__':
    main()
