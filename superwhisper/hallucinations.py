"""Find text the voice model invented. Usage: python hallucinations.py [--since DAYS]

Flags a recording when its raw transcript has a known filler phrase, a sentence looping 3+
times, or far more words than its length allows (a 1 s clip cannot hold 200 words). Reports
whether the invented text reached the pasted result, and by length, mode, and device.
Writes research/HALLUCINATIONS-<date>.md.
"""
import collections, datetime, glob, json, re, sys
from pathlib import Path

REC = "//localhost/C$/Users/Joshu/AppData/Local/com.superwhisper.app/recordings"
SIGNATURES = [r"thank you", r"thanks for watching", r"world is a world", r"part of the world",
              r"very good feeling about it", r"very popular culture", r"world is not the only one",
              r"very good point about it", r"please subscribe"]
SIG = re.compile("|".join(SIGNATURES), re.I)
MAX_WPS = 5  # nobody dictates above ~4 words per second


def loops(text):
    s = [x.strip().lower() for x in re.split(r"(?<=[.!?])\s+", text) if len(x.strip()) > 8]
    return [k for k, n in collections.Counter(s).items() if n >= 3]


def bucket(sec):
    return "<2s" if sec < 2 else "2-5s" if sec < 5 else "5-30s" if sec < 30 else "30s+"


def main():
    days = int(sys.argv[sys.argv.index("--since") + 1]) if "--since" in sys.argv else 7
    cut = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
    tot, hit, leak = collections.Counter(), collections.Counter(), 0
    by_mode, by_dev, phrases, rows = collections.Counter(), collections.Counter(), collections.Counter(), []
    for m in glob.glob(REC + "/*/meta.json"):
        try:
            d = json.load(open(m, encoding="utf-8"))
        except Exception:
            continue
        if d.get("datetime", "")[:10] < cut:
            continue
        sec, raw, res = d.get("duration", 0) / 1000, d.get("rawResult") or "", d.get("result") or ""
        tot[bucket(sec)] += 1
        why = []
        if SIG.search(raw):
            why.append("phrase")
            phrases.update(x.lower() for x in SIG.findall(raw))
        if loops(raw):
            why.append("loop")
        if sec > 0 and len(raw.split()) / sec > MAX_WPS and len(raw.split()) > 15:
            why.append(f"{len(raw.split())} words in {sec:.1f}s")
        if not why:
            continue
        hit[bucket(sec)] += 1
        by_mode[d.get("modeName")] += 1
        by_dev[d.get("recordingDevice")] += 1
        pasted = bool(SIG.search(res) or loops(res))
        leak += pasted
        rows.append((d["datetime"][:16], f"{sec:.1f}s", d.get("modeName"), ", ".join(why),
                     "yes" if pasted else "no", raw[:80].replace("|", "/").replace("\n", " ")))
    n, h = sum(tot.values()), len(rows)
    out = [f"# Hallucination report {datetime.date.today()} (last {days} days)\n",
           f"{h} of {n} recordings had invented text; {leak} reached the pasted result.\n",
           "| Length | Affected | Total |", "|---|---|---|"]
    out += [f"| {b} | {hit[b]} | {tot[b]} |" for b in ["<2s", "2-5s", "5-30s", "30s+"]]
    out += ["", f"By mode: {dict(by_mode)}", f"By device: {dict(by_dev)}", f"Phrases: {dict(phrases.most_common(10))}", "",
            "| When | Length | Mode | Why | Pasted | Raw start |", "|---|---|---|---|---|---|"]
    out += ["| " + " | ".join(r) + " |" for r in sorted(rows, reverse=True)[:60]]
    p = Path(__file__).parent / "research" / f"HALLUCINATIONS-{datetime.date.today()}.md"
    p.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(out[1].strip())
    print({b: (hit[b], tot[b]) for b in ["<2s", "2-5s", "5-30s", "30s+"]})
    print("report:", p)


if __name__ == "__main__":
    main()
