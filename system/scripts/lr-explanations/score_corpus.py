"""Score every complete LR explanation in the DB dump and write per-type shortlists.
Usage: python score_corpus.py OUT_DIR [per_type=30]
Reads system/scripts/lsatlab-pull/data/db/*.json (run db_pull.py first, including lr_answer_choices)
and the LSAT U bank for features, difficulty and choice text."""
import json, glob, collections, re, sys, os

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(ROOT, '..', 'lsatlab-pull', 'data', 'db')
BANK = 'C:/Users/Joshu/dev/ai-os/projects/lsatu-wt-glossary/public/data/'
L = lambda t: json.load(open(os.path.join(DB, t + '.json'), encoding='utf-8'))
qs = L('lr_questions'); ex = L('lr_explanations'); st = L('lr_explanation_steps')
nt = L('lr_explanation_choice_notes'); ac = L('lr_answer_choices')
S = collections.defaultdict(list); N = collections.defaultdict(dict); A = collections.defaultdict(dict)
for s in st: S[s['explanation_id']].append(s)
for n in nt: N[n['explanation_id']][n['letter']] = n['body']
for c in ac: A[c['question_id']][c['letter']] = c
E = {}
for e in ex:
    if e['style'] in ('single', 'standard'): E[e['question_id']] = e
bank = {}
for f in glob.glob(BANK + 'PT*-S*-LR.json'):
    for b in json.load(open(f, encoding='utf-8')):
        bank[f"{b['practiceTest']}-S{b['sectionNumber']}-Q{b['questionNumber']}"] = b


def family(stem, label):
    """Question family from the stem (the stored type labels are unreliable)."""
    s = (stem or '').lower()
    if re.search(r'(pattern of|similar to|parallel|most closely parallels|most similar)', s):
        return 'Parallel Flaw' if re.search(r'flaw|questionable|erroneous|vulnerable', s) else 'Parallel'
    if re.search(r'disagree|point at issue|agree (that|about|over|on)|committed to (dis)?agreeing', s): return 'Agree-Disagree'
    if re.search(r'if assumed|enables|follows logically if|properly drawn if|properly inferred if', s): return 'Sufficient Assumption'
    if re.search(r'main (conclusion|point)|overall conclusion|expresses the conclusion|conclusion drawn|most accurately expresses', s): return 'Main Conclusion'
    if re.search(r'\brole\b|figures in the argument|plays which|function', s): return 'Role'
    if 'principle' in s:
        if re.search(r'justif|support|strengthen', s) and not re.search(r'conform|illustrat|in accordance|exemplif', s): return 'Principle-Strengthen'
        return 'Principle-Conform'
    if re.search(r'least vulnerable|flaw|vulnerable|criticism|questionable|error|does not follow logically|weakness in the reasoning', s): return 'Flaw'
    if re.search(r'technique|strateg|method|proceeds by|responds|responding|respond|counters?|counter .* by|by doing which|in which one of the following ways|does which one of the following|structured to', s): return 'Method'
    if re.search(r'issue in dispute|dispute between', s): return 'Agree-Disagree'
    if re.search(r'explain|resolve|reconcile|discrepancy|paradox|conflict', s): return 'Paradox'
    if re.search(r'evaluat|most useful to (know|determine|establish)|most relevant', s): return 'Evaluate'
    if re.search(r'assum|depends|relies|presuppos|requires', s): return 'Necessary Assumption'
    if re.search(r'weaken|undermine|doubt|calls? into question|limits the effectiveness', s): return 'Weaken'
    if re.search(r'must be false|cannot be true|could be true except|incompatible|violat|reject', s): return 'Must Be False'
    if re.search(r'strengthen|(most|strongest) support(s)? (for )?the [a-z’ ]*(argument|reasoning|conclusion|claim|hypothesis|prediction|recommendation|position|explanation)|supports the [a-z’ ]*(argument|reasoning|conclusion|claim|hypothesis)', s): return 'Strengthen'
    if re.search(r'must (also )?be true|inferred|conclu|follows logically|strongly supported|best supported|most supported|supported by|support (to|for)? ?which|supports which|illustrat|complete|evidence for', s): return 'Must Be True - Most Supported'
    l = (label or '').lower()
    for k, v in [('parallel flaw', 'Parallel Flaw'), ('parallel', 'Parallel'), ('flaw', 'Flaw'), ('paradox', 'Paradox'), ('necessary', 'Necessary Assumption'),
                 ('sufficient', 'Sufficient Assumption'), ('method', 'Method'), ('agree', 'Agree-Disagree'), ('principle-strengthen', 'Principle-Strengthen'),
                 ('principle', 'Principle-Conform'), ('main', 'Main Conclusion'), ('role', 'Role'), ('weaken', 'Weaken'), ('strengthen', 'Strengthen'),
                 ('evaluate', 'Evaluate'), ('must be false', 'Must Be False'), ('must', 'Must Be True - Most Supported'), ('support', 'Must Be True - Most Supported')]:
        if k in l: return v
    return 'Other'


TONE = re.compile(r'hot garbage|so,? so dumb|unthinkably|dumpster fire|stupid question|idiotic', re.I)
EXM = re.compile(r"\b(imagine|for example|for instance|let's say|say that|picture|it's like|like if|analogy|suppose)\b", re.I)
GEN = re.compile(r"\b(whenever|any ?time|usually|almost always|most of the time|on (flaw|necessary|sufficient|paradox|parallel|main|role|method|principle|strengthen|weaken|must|most|agree|evaluate)[a-z ]*questions?)\b", re.I)
TEST = re.compile(r"negat|would (this|it) weaken|trigger|why should we believe|support test|how could we|given that|descriptively accurate|can we support", re.I)

rows = []
for q in qs:
    e = E.get(q['id'])
    if not e: continue
    steps = sorted(S[e['id']], key=lambda s: s['position']); notes = N[e['id']]
    if not steps or len(notes) < 5: continue
    slot = f"PT{q['preptest']}-S{q['section']}-Q{q['question_number']}"
    b = bank.get(slot) or {}
    key = (q['correct_choice'] or b.get('correctAnswer') or '').strip()
    txt = ' '.join(s['body'] for s in steps) + ' ' + ' '.join(notes.values())
    words = len(txt.split())
    ev = ' '.join(s['body'] for s in steps if re.search(r'evaluat|how could|why is it|how can', s['label'].lower()))
    goal = ' '.join(s['body'] for s in steps if re.search(r'goal|predict|anticipat|prephrase', s['label'].lower()))
    wl = {k: len(v.split()) for k, v in notes.items() if k != key}
    right = notes.get(key, '')
    verdict = sum(1 for w in wl.values() if w < 20)
    pct = {k: (A[q['id']].get(k) or {}).get('student_percent') for k in 'ABCDE'}
    wrongpct = {k: p for k, p in pct.items() if k != key and p is not None}
    trap = max(wrongpct, key=wrongpct.get) if wrongpct else None
    trap_ok = trap is not None and wl and wl.get(trap, 0) >= max(wl.values()) * 0.8
    dash = txt.count('\u2014') / max(words, 1) * 1000
    score = (min(words, 1000) / 125 + min(len(ev.split()), 250) / 50 + (3 if goal else 0) + min(len(goal.split()), 80) / 40
             - verdict * 2 + min(len(TEST.findall(txt)), 10) * 0.5 + min(len(EXM.findall(txt)), 5) * 0.7
             + min(len(GEN.findall(txt)), 5) * 0.6 + min(len(right.split()), 160) / 40 + (1.5 if trap_ok else 0)
             - (5 if dash > 3 else 0) - len(TONE.findall(txt)) * 3
             - (4 if e['style'] == 'standard' and q['preptest'] in (157, 158) else 0))
    rows.append(dict(slot=slot, fam=family(q['prompt'], q['question_type']), diff=b.get('questionDifficulty'),
                     feat=b.get('questionFeatures') or [], score=round(score, 1), words=words, verdict=verdict,
                     trap=trap, trap_ok=bool(trap_ok), dash=round(dash, 1), style=e['style'], qid=q['id']))

out = sys.argv[1]; per = int(sys.argv[2]) if len(sys.argv) > 2 else 30
os.makedirs(out, exist_ok=True)
json.dump(rows, open(os.path.join(out, 'scores.json'), 'w'), indent=0)
Q = {q['id']: q for q in qs}
byf = collections.defaultdict(list)
for r in rows: byf[r['fam']].append(r)
for f, rs in sorted(byf.items(), key=lambda x: -len(x[1])):
    rs.sort(key=lambda r: -r['score'])
    pick = []
    for band in ([r for r in rs if (r['diff'] or 3) <= 2], [r for r in rs if r['diff'] == 3], [r for r in rs if (r['diff'] or 0) >= 4]):
        pick += band[:max(6, per // 4)]
    for r in rs:
        if len(pick) >= per: break
        if r not in pick: pick.append(r)
    pick = sorted(pick[:per], key=lambda r: -r['score'])
    print(f"{f:32s} complete={len(rs):4d} shortlisted={len(pick)} top={pick[0]['score']} cut={pick[-1]['score']}")
    with open(os.path.join(out, f'shortlist-{f.replace(" ", "-")}.md'), 'w', encoding='utf-8') as fh:
        fh.write(f'# {f}: {len(pick)} candidates (of {len(rs)} complete)\n')
        for r in pick:
            q = Q[r['qid']]; e = E[q['id']]; b = bank.get(r['slot']) or {}
            fh.write(f"\n\n=================== {r['slot']} | diff {r['diff']} | key {q['correct_choice']} | score {r['score']} | features: {', '.join(r['feat']) or '-'}\n")
            fh.write('STIMULUS: ' + (b.get('stimulus') or q['stimulus'] or '') + '\nSTEM: ' + (b.get('questionStem') or q['prompt'] or '') + '\n')
            for k in 'ABCDE':
                c = A[q['id']].get(k) or {}
                fh.write(f"({k}) [{c.get('student_percent', '?')}% | {c.get('tag') or ''}] {(b.get('answerChoices') or {}).get(k) or c.get('choice_text') or ''}\n")
            fh.write('--- BREAKDOWN\n')
            for s in sorted(S[e['id']], key=lambda s: s['position']): fh.write(f"## {s['label']}\n{s['body']}\n")
            fh.write('--- CHOICE NOTES\n')
            for k in sorted(N[e['id']]): fh.write(f"({k}) {N[e['id']][k]}\n")
