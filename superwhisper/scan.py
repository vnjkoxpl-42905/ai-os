#!/usr/bin/env python3
"""Scan Joshua's Superwhisper transcripts for words that keep going wrong and terms worth adding.

Reads every recordings/<id>/meta.json (rawResult = what the voice model heard) through the
sandbox-bypass path, compares against vocabulary.md and replacements.md, and writes a dated
report to research/SCAN-<date>.md. Prints the short version.

Usage:
  python scan.py              all recordings
  python scan.py --since 7    only the last 7 days
  python scan.py --min 2      show candidates seen at least 2 times (default 3)

What it looks for:
  1. near-misses  : tokens that look like a vocabulary term or student name but are not it
                    (difflib ratio >= 0.72). These are the mis-hearings to add as replacements.
  2. rules-not-firing : "heard" strings from replacements.md that still appear in transcripts
                    recorded AFTER the rule's date. Means the app was not restarted, or the
                    match needs a different spelling.
  3. candidates   : capitalised or dotted tokens (names, products, domains) that appear >= min
                    times and are not vocabulary, not a replacement target, and not a common
                    word. Worth adding only if the model gets them wrong; the report says how
                    they were spelled each time so you can tell.
  4. frequent terms : the most-used domain words overall, for context.
"""
import json, os, re, sys, glob, collections, difflib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REC = r"\\localhost\C$\Users\Joshu\AppData\Local\com.superwhisper.app\recordings"
STUDENTS = r"C:\Users\Joshu\dev\ai-os\students"

args = sys.argv[1:]
since = int(args[args.index("--since") + 1]) if "--since" in args else None
minc = int(args[args.index("--min") + 1]) if "--min" in args else 3

COMMON = set("""i im ill ive id okay ok so and the but if it what we you this that can then also now is do let yes no just
like for in on a to of my or there they he she when where how why because not all one two three first second actually
basically right well oh um yeah hey go make get give tell have want need think know see look which again here some any
every each those these their his her our its as at by from with about into over after before up down out off than too
very should would could will did does was were are be been being use using put add change update create build run check
save send fix thank thanks please sorry alright maybe something anything everything nothing once say says said done
good great perfect only more most same different next last new old here there whatever wherever whenever ever never
always sometimes today tomorrow yesterday tonight monday tuesday wednesday thursday friday saturday sunday january
february march april may june july august september october november december am pm lets thats its whats hes shes
theyre were youre dont doesnt didnt cant couldnt wouldnt shouldnt isnt arent wasnt werent hasnt havent wont
canada canadian ontario michigan god lord man page pages section sections step steps part parts able clear even event
seen wait whip data nate matt lsat super figure google github api kling name names time times work works word words
link links email emails file files code test tests drill drills student students session sessions message messages
account accounts back front open close start stop record recording button click press type text note notes list
line lines number numbers question questions answer answers point points thing things way ways kind sort little
big small long short high low fast slow early late still already yet also even though although while until since
""".split())
CONTRACTION = re.compile(r"'")

def load_config():
    vocab = [l[2:].strip() for l in open(os.path.join(HERE, "vocabulary.md"), encoding="utf-8") if l.startswith("- ")]
    reps = []
    for l in open(os.path.join(HERE, "replacements.md"), encoding="utf-8"):
        if l.startswith("|") and not l.startswith("| Heard") and not l.startswith("|---"):
            c = [x.strip() for x in l.strip("|\n").split("|")]
            if len(c) >= 3 and c[0]:
                reps.append({"heard": c[0], "wanted": c[1], "date": c[2]})
    names = []
    for d in os.listdir(STUDENTS):
        if d.startswith("_") or d in ("README.md", "roster.generated.md", "non-students") or "." in d:
            continue
        names += [p.capitalize() for p in d.split("-")]
    return vocab, reps, sorted(set(names))

def load_recordings():
    rows = []
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=since)) if since else None
    for f in glob.glob(os.path.join(REC, "*", "meta.json")):
        try:
            m = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        dt = datetime.datetime.fromisoformat(m["datetime"])
        if cutoff and dt < cutoff:
            continue
        rows.append({"dt": m["datetime"][:10], "raw": m.get("rawResult") or "", "result": m.get("result") or "", "mode": m.get("modeName", "")})
    return sorted(rows, key=lambda r: r["dt"])

def main():
    vocab, reps, names = load_config()
    rows = load_recordings()
    if not rows:
        raise SystemExit("no recordings found")
    text_by_day = collections.defaultdict(list)
    for r in rows:
        text_by_day[r["dt"]].append(r["raw"])
    all_raw = "\n".join(r["raw"] for r in rows)

    targets = set(v.lower() for v in vocab) | set(r["wanted"].lower() for r in reps) | set(n.lower() for n in names)
    heard = set(r["heard"].lower() for r in reps)
    known_terms = [v for v in vocab] + names

    # tokens: words, dotted/at things (domains, emails)
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9'\-]*(?:[.@][A-Za-z0-9\-]+)*", all_raw)
    freq = collections.Counter(tokens)
    lower_freq = collections.Counter(t.lower() for t in tokens)

    # 1. near-misses against vocabulary and student names
    near = collections.defaultdict(collections.Counter)  # term -> {misspelling: count}
    for tok, n in lower_freq.items():
        if tok in targets or tok in heard or tok in COMMON or len(tok) < 4:
            continue
        for term in known_terms:
            t = term.lower()
            if len(t) < 4 or tok == t:
                continue
            if tok[0] != t[0]:
                continue
            ratio = difflib.SequenceMatcher(None, tok, t).ratio()
            need = 0.8 if len(t) <= 6 else 0.72
            if ratio >= need and abs(len(tok) - len(t)) <= 3:
                near[term][tok] += n
    # multi-word phrases: check 2-grams against multi-word vocab (e.g. "blind review", "claude code")
    words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", all_raw)]
    bigrams = collections.Counter(f"{a} {b}" for a, b in zip(words, words[1:]))
    for term in [t for t in known_terms if " " in t]:
        t = term.lower()
        for bg, n in bigrams.items():
            if bg == t or bg in heard:
                continue
            if difflib.SequenceMatcher(None, bg, t).ratio() >= 0.8:
                near[term][bg] += n

    # 2. rules not firing: heard string present in a transcript dated after the rule
    not_firing = []
    for rp in reps:
        h = rp["heard"].lower().rstrip(".")
        for day, texts in text_by_day.items():
            if day > rp["date"]:
                hits = sum(len(re.findall(r"(?<![A-Za-z])" + re.escape(h) + r"(?![A-Za-z])", t.lower())) for t in texts)
                if hits:
                    not_firing.append((rp["heard"], rp["wanted"], day, hits))

    # 3. candidates: capitalised or dotted tokens, frequent, unknown
    cand = collections.Counter()
    spellings = collections.defaultdict(collections.Counter)
    for tok, n in freq.items():
        low = tok.lower()
        if low in targets or low in COMMON or low in heard:
            continue
        if not (tok[0].isupper() or "." in tok or "@" in tok):
            continue
        if len(tok) < 3 or CONTRACTION.search(tok):
            continue
        cand[low] += n
        spellings[low][tok] += n
    # drop sentence-initial capitalisation noise: keep only if it also appears capitalised mid-sentence or is dotted
    mid_caps = collections.Counter(m.group(1).lower() for m in re.finditer(r"[a-z,;]\s+([A-Z][A-Za-z0-9'\-]+)", all_raw))
    candidates = [(t, n) for t, n in cand.most_common() if n >= minc and (mid_caps[t] >= 1 or "." in t or "@" in t)]

    # 4. frequent domain-ish words (not common, length >= 5)
    domain = [(t, n) for t, n in lower_freq.most_common(400) if t not in COMMON and len(t) >= 5 and n >= 5][:40]

    # ---- report
    today = datetime.date.today().isoformat()
    out = [f"---\ntitle: Superwhisper transcript scan {today}\ntype: research\ncreated: {today}\n---\n",
           f"# Transcript scan {today}\n",
           f"{len(rows)} recordings, {rows[0]['dt']} to {rows[-1]['dt']}" + (f", last {since} days" if since else "") + f". {len(vocab)} vocabulary terms, {len(reps)} replacements in force.\n"]
    out.append("## 1. Near-misses of known terms (add as replacements)\n")
    if near:
        out.append("| Term | Heard as | Times |\n|---|---|---|")
        for term, c in sorted(near.items(), key=lambda kv: -sum(kv[1].values())):
            for mis, n in c.most_common():
                out.append(f"| {term} | {mis} | {n} |")
    else:
        out.append("None.")
    out.append("\n## 2. Replacement rules that did not fire\n")
    if not_firing:
        out.append("Heard string still present after the rule's date. Usually the app was not restarted; otherwise the spelling differs from the rule.\n")
        out.append("| Rule | Wanted | Day | Hits |\n|---|---|---|---|")
        for h, w, d, n in sorted(not_firing, key=lambda x: (x[2], x[0])):
            out.append(f"| {h} | {w} | {d} | {n} |")
    else:
        out.append("None. Every rule in force is holding.")
    out.append(f"\n## 3. Candidate terms (seen >= {minc} times, not in vocabulary)\n")
    out.append("Only worth adding if the spellings vary or are wrong. Consistent spelling means the model already knows the word.\n")
    if candidates:
        out.append("| Term | Times | Spellings seen |\n|---|---|---|")
        for t, n in candidates[:60]:
            sp = ", ".join(f"{s} ({k})" for s, k in spellings[t].most_common(4))
            out.append(f"| {t} | {n} | {sp} |")
    else:
        out.append("None.")
    out.append("\n## 4. Most-used domain words (context)\n")
    out.append(", ".join(f"{t} ({n})" for t, n in domain))
    report = "\n".join(out) + "\n"
    path = os.path.join(HERE, "research", f"SCAN-{today}.md")
    open(path, "w", encoding="utf-8").write(report)

    print(f"scanned {len(rows)} recordings ({rows[0]['dt']} to {rows[-1]['dt']})")
    print(f"near-misses: {sum(len(c) for c in near.values())} | rules not firing: {len(not_firing)} | candidates: {len(candidates)}")
    for term, c in sorted(near.items(), key=lambda kv: -sum(kv[1].values()))[:12]:
        print(f"  {term:22s} <- " + ", ".join(f"{m} x{n}" for m, n in c.most_common(4)))
    print(f"report: {path}")

if __name__ == "__main__":
    main()
