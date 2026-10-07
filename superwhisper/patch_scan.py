"""2026-09-23: fix scan.py section 2 and add two new checks."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "scan.py")
s = open(p, encoding="utf-8").read()

# 1. carry the post-replacement text through
s = s.replace(
    'rows.append({"dt": m["datetime"][:10], "raw": m.get("rawResult") or "", "result": m.get("result") or "", "mode": m.get("modeName", "")})',
    'rows.append({"dt": m["datetime"][:10], "raw": m.get("rawResult") or "", "result": m.get("result") or "", "mode": m.get("modeName", "")})')

# 2. section 2 must test the FINAL text, not the raw transcript. The raw is what the voice
#    model heard, so every rule "fails" there by definition; only the result proves a miss.
s = s.replace(
    '    text_by_day = collections.defaultdict(list)\n    for r in rows:\n        text_by_day[r["dt"]].append(r["raw"])',
    '    text_by_day = collections.defaultdict(list)\n    for r in rows:\n        text_by_day[r["dt"]].append(r["result"] or r["raw"])')

# 3. new checks: rules firing inside other words, and silence hallucination
s = s.replace(
    '    # 3. candidates: capitalised or dotted tokens, frequent, unknown',
    '''    # 2b. rules that fire INSIDE other words. Superwhisper matches substrings with no word
    # boundaries, so a short rule like "cli" turns "click" into "CLIck". Any hit here is a bug.
    all_out = "\\n".join(r["result"] or r["raw"] for r in rows)
    mangled = []
    for rp in reps:
        h = rp["heard"].lower()
        if not re.fullmatch(r"[a-z][a-z ]*", h):
            continue
        n = len(re.findall(r"(?<=[a-z])" + re.escape(h) + r"|" + re.escape(h) + r"(?=[a-z])", all_out.lower()))
        if n:
            mangled.append((n, rp["heard"], rp["wanted"]))
    mangled.sort(reverse=True)

    # 2c. silence hallucination: the voice model fills pauses with "Thank you" and similar.
    halluc = collections.Counter()
    for r in rows:
        for phrase in ("thank you", "thanks for watching", "mm-hmm", "bye."):
            halluc[phrase] += r["raw"].lower().count(phrase)

    # 3. candidates: capitalised or dotted tokens, frequent, unknown''')

s = s.replace(
    '    out.append(f"\\n## 3. Candidate terms',
    '''    out.append("\\n## 2b. Rules firing inside other words (bugs, delete these)\\n")
    if mangled:
        out.append("Superwhisper matches substrings, not words, so these rules corrupt ordinary text.\\n")
        out.append("| Rule | Wanted | Times inside a word |\\n|---|---|---|")
        for n, h, w in mangled:
            out.append(f"| {h} | {w} | {n} |")
    else:
        out.append("None. No rule is matching inside another word.")
    out.append("\\n## 2c. Silence hallucination (voice model filling pauses)\\n")
    out.append(", ".join(f"{k}: {v}" for k, v in halluc.most_common() if v) or "None.")
    out.append("\\nIf these are high, turn on Silence Removal in Sound and keep the mode prompt's drop rule.")
    out.append(f"\\n## 3. Candidate terms''')

s = s.replace(
    '    print(f"near-misses: {sum(len(c) for c in near.values())} | rules not firing: {len(not_firing)} | candidates: {len(candidates)}")',
    '    print(f"near-misses: {sum(len(c) for c in near.values())} | rules not firing: {len(not_firing)} | mangling rules: {len(mangled)} | candidates: {len(candidates)}")\n'
    '    for n, h, w in mangled[:6]:\n'
    '        print(f"  BUG: {h!r} fires inside other words {n}x")')

open(p, "w", encoding="utf-8").write(s)
print("patched scan.py")
