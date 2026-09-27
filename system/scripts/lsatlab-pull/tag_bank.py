"""Fill LSAT Lab labels (difficulty, reasoning type, question features) into
LSAT U question-bank files, from the LSAT Lab data pulled into data/.

Usage (from an LSAT U checkout root):
  python <this> --slots PT113-S3-Q21,PT117-S2-Q1 [--dry-run]
  python <this> --slots-file slots.txt
  python <this> --missing            # every LR slot with no questionFeatures

Refresh data/ first with pull.md. Only the named slots are touched; nothing
else in a file changes. Question type is left alone (the bank uses LSAT U's
own type names; the database owns the type).
"""
import argparse, glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
Q = json.load(open(os.path.join(HERE, 'data/questions-props.json'), encoding='utf-8'))['questions']
P = json.load(open(os.path.join(HERE, 'data/properties.json'), encoding='utf-8'))
SUB = {i: n for i, n, _ in P['s']}
REASONING = {'Conditional Logic': 'Conditional Reasoning', 'Comparison': 'Comparative Reasoning', 'Causation': 'Causation'}
RENAME = {'Necessary vs. Sufficient Flaw': 'Sufficient vs. Necessary Flaw', 'Sampling Flaw': 'Sampling', 'Repetitve Answers': 'Repetitive Answers'}
LAB = {(x['t'], x['sn'], x['qp']): x for x in Q if x['s'] == 'LR' and isinstance(x['t'], int)}

def labels(x):
    names = [SUB[i] for i in x.get('qst') or [] if i in SUB]
    reasoning = [REASONING[n] for n in names if n in REASONING]
    feats = []
    for n in names:
        if n in REASONING: continue
        n = RENAME.get(n, n)
        if n not in feats: feats.append(n)
    return x['d'], reasoning, feats

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slots'); ap.add_argument('--slots-file'); ap.add_argument('--missing', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    want = set()
    if a.slots: want |= {s.strip() for s in a.slots.split(',') if s.strip()}
    if a.slots_file: want |= {l.strip() for l in open(a.slots_file) if l.strip()}
    done, nolab = [], []
    for f in sorted(glob.glob('public/data/PT*-LR.json')):
        raw = open(f, encoding='utf-8').read(); items = json.loads(raw); changed = False
        for q in items:
            slot = f"{q['practiceTest']}-S{q['sectionNumber']}-Q{q['questionNumber']}"
            if not (slot in want or (a.missing and not q.get('questionFeatures'))): continue
            x = LAB.get((int(q['practiceTest'][2:]), q['sectionNumber'], q['questionNumber']))
            if not x: nolab.append(slot); continue
            d, r, feats = labels(x)
            q['questionDifficulty'] = d; q['reasoningType'] = r; q['questionFeatures'] = feats
            order = ['practiceTest','sectionNumber','questionNumber','questionType','reasoningType','questionDifficulty','stimulus','questionStem','answerChoices','correctAnswer','questionFeatures']
            new = {k: q[k] for k in order if k in q} | {k: v for k, v in q.items() if k not in order}
            q.clear(); q.update(new); changed = True; done.append(slot)
        if changed and not a.dry_run:
            open(f, 'w', encoding='utf-8', newline='\n').write(json.dumps(items, ensure_ascii=False, indent=2) + ('\n' if raw.endswith('\n') else ''))
    print(f'tagged {len(done)}; no LSAT Lab row for {len(nolab)}: {nolab}')

if __name__ == '__main__':
    main()
