"""Full LR audit: LSAT U question bank + database vs LSAT Lab.

Needs: crawl_public.py output in data/public/, the LSAT Lab props dump in data/,
and a database dump dir (lr_questions.json, lr_explanations.json,
lr_explanation_steps.json, lr_explanation_choice_notes.json) from db_pull.py.

Usage (from an LSAT U checkout root):
  python <this> --db <dump dir> --out <report.md>
Also writes <report>.json with every finding.

Checks, per LR slot:
  key        bank key vs LSAT Lab key vs database key
  text       bank stimulus / stem / each choice's opening words appear on LSAT Lab's page
  slots      questions LSAT Lab lists for a test that the bank lacks, and the reverse
  explained  LSAT Lab has a written explanation where LSAT U's Coverage State is not Complete
  labels     bank difficulty / reasoning type / features vs LSAT Lab props
"""
import argparse, collections, glob, json, os, re, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'data', 'public')
nz = lambda s: re.sub(r'\W+', '', (s or '').lower())
PASSAGE = re.compile(r'^\s*The following passage is used for[^.]*\.\s*', re.I)
def opening(s, n=30):
    # public pages show only the opening words; compare at most the first sentence
    s = PASSAGE.sub('', s or '')
    first = re.split(r'(?<=[.?!])\s', s, 1)[0]
    return nz(first)[:n] if len(nz(first)) >= 12 else nz(s)[:n]
num = lambda x: int(re.sub(r'\D', '', str(x)))

def load_tagger():
    spec = importlib.util.spec_from_file_location('tag_bank', os.path.join(HERE, 'tag_bank.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--db', required=True); ap.add_argument('--out', required=True)
    a = ap.parse_args(); tb = load_tagger()
    J = lambda n: json.load(open(os.path.join(a.db, n), encoding='utf-8'))
    dbq = {(num(q['preptest']), num(q['section']), num(q['question_number'])): q for q in J('lr_questions.json')}
    ex = collections.defaultdict(list)
    for e in J('lr_explanations.json'): ex[e['question_id']].append(e['id'])
    has_steps = {s['explanation_id'] for s in J('lr_explanation_steps.json')}
    has_notes = {n['explanation_id'] for n in J('lr_explanation_choice_notes.json')}
    def coverage(k):
        q = dbq.get(k)
        if not q: return 'Unloaded'
        ids = ex.get(q['id'], [])
        st = any(i in has_steps for i in ids); no = any(i in has_notes for i in ids)
        return 'Complete' if st and no else 'Notes-only' if no else 'Unexplained'
    bank = {}
    for f in glob.glob('public/data/PT*-LR.json'):
        for q in json.load(open(f, encoding='utf-8')):
            bank[(num(q['practiceTest']), q['sectionNumber'], q['questionNumber'])] = q
    lists = json.load(open(os.path.join(PUB, '_lists.json'), encoding='utf-8')) if os.path.exists(os.path.join(PUB, '_lists.json')) else {}
    F = collections.defaultdict(list)
    for k, b in sorted(bank.items()):
        slot = 'PT%d-S%d-Q%d' % k
        p = os.path.join(PUB, slot + '.json')
        if not os.path.exists(p): F['not_crawled'].append(slot); continue
        r = json.load(open(p, encoding='utf-8'))
        if r.get('status') != 200: F['lsatlab_no_page'].append({'slot': slot, 'status': r.get('status')}); continue
        t = r['norm_text']; d = dbq.get(k)
        lab = r.get('key'); bk = b.get('correctAnswer'); dk = d and d['correct_choice']
        if lab and (bk != lab or (dk and dk != lab)):
            F['key_mismatch'].append({'slot': slot, 'bank': bk, 'db': dk, 'lsatlab': lab})
        if b.get('status') == 'removed': continue
        stim = opening(b.get('stimulus')); stem = nz(b.get('questionStem'))[:40]  # public pages show only the opening words
        if stim and stim not in t: F['stimulus_not_on_lsatlab'].append(slot)
        elif stem and stem not in t: F['stem_not_on_lsatlab'].append(slot)
        bad = [L for L, c in (b.get('answerChoices') or {}).items() if nz(c)[:12] and nz(c)[:12] not in t]
        if bad: F['choice_not_on_lsatlab'].append({'slot': slot, 'choices': bad})
        if d and opening(d['stimulus']) not in t: F['db_stimulus_not_on_lsatlab'].append(slot)
        written = bool(r.get('steps')) and sum(1 for x in r['answers'].values() if x.get('explanation')) >= 5
        partial = bool(r.get('steps')) or any(x.get('explanation') for x in r['answers'].values())
        cov = coverage(k)
        if cov != 'Complete' and partial:
            F['lsatlab_explained_lsatu_not'].append({'slot': slot, 'coverage': cov, 'lsatlab': 'full' if written else 'partial',
                                                     'steps': len(r['steps']), 'choice_expl': sum(1 for x in r['answers'].values() if x.get('explanation'))})
        x = tb.LAB.get(k)
        if x:
            dd, rr, ff = tb.labels(x)
            if b.get('questionDifficulty') != dd or sorted(b.get('reasoningType') or []) != sorted(rr) or sorted(b.get('questionFeatures') or []) != sorted(ff):
                F['labels_differ'].append(slot)
    # slot coverage per test from LSAT Lab's own lists
    for pt, items in lists.items():
        n = num(pt)
        for i in items:
            if i.get('sectionType') == 'Reading Comprehension' or i.get('testNumber') != n: continue
            k = (n, i['sectionNumber'], i['questionNumber'])
            if k not in bank: F['in_lsatlab_not_in_bank'].append('PT%d-S%d-Q%d' % k)
    lab_slots = {(num(pt), i['sectionNumber'], i['questionNumber']) for pt, items in lists.items() for i in items
                 if i.get('sectionType') != 'Reading Comprehension' and i.get('testNumber') == num(pt)}
    crawled_pts = {num(pt) for pt in lists}
    for k in bank:
        if k[0] in crawled_pts and k not in lab_slots: F['in_bank_not_in_lsatlab_list'].append('PT%d-S%d-Q%d' % k)
    json.dump(F, open(os.path.splitext(a.out)[0] + '.json', 'w', encoding='utf-8'), indent=1)
    L = ['# LR audit: LSAT U vs LSAT Lab', '', '| Check | Count |', '|---|---|']
    L += ['| %s | %d |' % (k, len(v)) for k, v in sorted(F.items())]
    for k, v in sorted(F.items()):
        L += ['', '## ' + k, '']
        L += ['- ' + (json.dumps(x, ensure_ascii=False) if isinstance(x, dict) else x) for x in v[:400]]
        if len(v) > 400: L.append(f'- ... {len(v) - 400} more in the JSON')
    open(a.out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print({k: len(v) for k, v in F.items()})

if __name__ == '__main__':
    main()
