"""Parse and validate Revamp rewrite drafts. Usage: python3 -I parse_drafts.py draft.md [more.md] [--json out.json]
Prints one line per problem. Exit 1 if any problem. With --json, writes the parsed drafts."""
import json, re, sys, csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
AIOS = os.path.abspath(os.path.join(HERE, '../../../../..'))
DB = os.path.join(AIOS, 'system/scripts/lsatlab-pull/data/db/')
INV = os.path.join(AIOS, 'corpus/lr-explanations/fixes/revamp-inventory.csv')
GENDER = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
BANNED = re.compile(r"logic games?|\bgreat question\b|it'?s important to note|hot garbage|dumpster", re.I)

def norm(s):
    paras = re.split(r"\n\s*\n", s.strip())
    return "\n\n".join(p.strip() for p in paras)

def parse(path):
    text = open(path, encoding='utf-8').read()
    out = {}
    for sec in text.split("\n## ")[1:] if not text.startswith("## ") else ("\n" + text).split("\n## ")[1:]:
        head = sec.split("\n", 1)[0]
        parts = [x.strip() for x in head.split("|")]
        if len(parts) == 2 and parts[1] == 'FLAG':
            out[parts[0]] = dict(flag=sec.split("\n", 1)[1].strip() if "\n" in sec else ''); continue
        if len(parts) != 3:
            out[head] = dict(error=f"bad header: {head}"); continue
        qid, qtype, key = parts
        m = re.search(r"^explanation_id:\s*([0-9a-f-]{36})", sec, re.M)
        steps, notes = [], {}
        bd = sec.split("### Argument Breakdown", 1)
        if len(bd) == 2:
            part = bd[1].split("### Choice Notes", 1)[0]
            for sm in re.finditer(r"^\*\*([^*\n]+?):\*\* (.+?)(?=\n\n\*\*[^*\n]+?:\*\* |\Z)", part.strip(), re.S | re.M):
                steps.append((sm.group(1).strip(), norm(sm.group(2))))
        cn = sec.split("### Choice Notes", 1)[1] if "### Choice Notes" in sec else ""
        for nm in re.finditer(r"^\*\*\(([A-E])\) (.+?)\.\*\* (.+?)(?=\n\n\*\*\([A-E]\) |\Z)", cn.strip(), re.S | re.M):
            notes[nm.group(1)] = dict(tag=nm.group(2).strip(), body=norm(nm.group(3)))
        out[qid] = dict(type=qtype, key=key, explanation_id=m.group(1) if m else None, steps=steps, notes=notes)
    return out

def main():
    args = sys.argv[1:]; jout = None
    if '--json' in args:
        i = args.index('--json'); jout = args[i + 1]; args = args[:i] + args[i + 2:]
    inv = {r['qid']: r for r in csv.DictReader(open(INV, encoding='utf-8')) if r['verdict'] == 'Revamp'}
    qs = {q['qid']: q for q in json.load(open(DB + 'lr_questions.json', encoding='utf-8'))}
    probs = []; alld = {}
    for p in args:
        for qid, d in parse(p).items():
            if qid in alld: probs.append(f"{qid}: drafted twice")
            alld[qid] = d
            if 'error' in d: probs.append(f"{p}: {d['error']}"); continue
            if 'flag' in d: continue
            if qid not in inv: probs.append(f"{qid}: not on the Revamp list"); continue
            if d['explanation_id'] != inv[qid]['explanation_id']:
                probs.append(f"{qid}: explanation_id {d['explanation_id']} != target {inv[qid]['explanation_id']}")
            if d['key'] != qs[qid]['correct_choice']: probs.append(f"{qid}: key {d['key']} != DB key {qs[qid]['correct_choice']}")
            if len(d['steps']) < 2: probs.append(f"{qid}: only {len(d['steps'])} breakdown steps parsed")
            if sorted(d['notes']) != list('ABCDE'): probs.append(f"{qid}: notes parsed for {sorted(d['notes'])}")
            for L, n in d['notes'].items():
                if (n['tag'].lower() == 'correct') != (L == d['key']): probs.append(f"{qid}: note {L} tag '{n['tag']}' vs key {d['key']}")
            stim = qs[qid]['stimulus'] + ' ' + qs[qid]['prompt']
            texts = [('step ' + l, b) for l, b in d['steps']] + [('note ' + L, n['body']) for L, n in d['notes'].items()]
            for where, t in texts:
                if '—' in t: probs.append(f"{qid}: em dash in {where}")
                if BANNED.search(t): probs.append(f"{qid}: banned phrase in {where}: {BANNED.search(t).group(0)}")
                if not t.strip(): probs.append(f"{qid}: empty {where}")
                g = set(w.lower() for w in GENDER.findall(t))
                if g: probs.append(f"{qid}: gendered pronoun {sorted(g)} in {where} (allowed only if the stimulus itself uses it for that person: stimulus has {sorted(set(w.lower() for w in GENDER.findall(stim)))})")
    for pr in probs: print(pr)
    print(f"parsed {len(alld)} ({sum('flag' in d for d in alld.values())} flags), problems {len(probs)}")
    if jout: json.dump(alld, open(jout, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(1 if probs else 0)

main()
