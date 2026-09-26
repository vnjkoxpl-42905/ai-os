#!/usr/bin/env python3
"""sw - Superwhisper from the terminal, on Windows.

Superwhisper's own CLI (`curl https://superwhisper.com/install-cli.sh | bash`) is macOS-only:
its install script exits on anything but Darwin and the only release asset is a macOS binary
(checked 2026-09-26). This does the same jobs against the same local files.

  sw search <text>          full-text search across every dictation
  sw last [n]               the last n dictations (default 10)
  sw stats                  recordings, words, time, speed, models, modes
  sw add "heard --> wanted" add a replacement, sync, restart
  sw vocab [term]           list the vocabulary, or add a term
  sw rules [text]           list replacements, optionally filtered
  sw export [n]             last n dictations as markdown on stdout
  sw scan [days]            run the transcript scan
  sw sync                   push the vault config and restart the app
  sw mode [name]            show the active mode, or switch to one

Everything reads and writes through the UNC path so the Claude Desktop sandbox cannot
redirect it (see CLAUDE.md rule 1).
"""
import json, os, re, subprocess, sys, collections, datetime, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
APP = r"\\localhost\C$\Users\Joshu\AppData\Local\com.superwhisper.app"
REC = os.path.join(APP, "recordings")


def load(limit=None, days=None):
    out = []
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=days)) if days else None
    for d in os.listdir(REC):
        f = os.path.join(REC, d, "meta.json")
        if not os.path.exists(f):
            continue
        try:
            m = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if cutoff and datetime.datetime.fromisoformat(m["datetime"]) < cutoff:
            continue
        out.append(m)
    out.sort(key=lambda m: m["datetime"])
    return out[-limit:] if limit else out


def settings():
    return os.path.join(APP, "settings", "settings.json")


def run_sync(restart=True):
    cmd = [sys.executable, os.path.join(HERE, "sync.py")] + (["--restart"] if restart else [])
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    subprocess.run(cmd, env=env)


def cmd_search(args):
    if not args:
        sys.exit("usage: sw search <text>")
    q = " ".join(args).lower()
    hits = [m for m in load() if q in (m.get("result") or m.get("rawResult") or "").lower()]
    print(f"{len(hits)} of {len(load())} dictations match {q!r}\n")
    for m in hits[-40:]:
        text = (m.get("result") or m.get("rawResult") or "").replace("\n", " ")
        i = text.lower().find(q)
        print(f"{m['datetime'][:16]}  {m.get('modeName','?')}")
        print(f"   ...{text[max(0, i - 70):i + 110]}...\n")


def cmd_last(args):
    n = int(args[0]) if args else 10
    for m in load(limit=n):
        print(f"\n{m['datetime'][:16]}  {m.get('modeName','?')} / {m.get('languageModelName') or 'no AI'}")
        print("  " + (m.get("result") or m.get("rawResult") or "").replace("\n", "\n  ")[:600])


def cmd_stats(args):
    rows = load()
    words = sum(len((m.get("result") or "").split()) for m in rows)
    secs = sum(m.get("duration", 0) for m in rows) / 1000
    wpm = [len((m.get("rawResult") or "").split()) / (m["duration"] / 60000)
           for m in rows if m.get("duration", 0) > 3000 and m.get("rawResult")]
    s = json.load(open(settings(), encoding="utf-8"))
    print(f"{len(rows)} dictations, {rows[0]['datetime'][:10]} to {rows[-1]['datetime'][:10]}")
    print(f"{words:,} words, {secs/3600:.1f} hours recorded, median {statistics.median(wpm):.0f} wpm")
    print(f"{len(s['replacements'])} replacements, {len(s['vocabulary'])} vocabulary, {len(s['modeKeys'])} modes")
    print("\nby mode:      " + ", ".join(f"{k} {v}" for k, v in
          collections.Counter(m.get("modeName", "?") for m in rows).most_common()))
    print("by model:     " + ", ".join(f"{k} {v}" for k, v in
          collections.Counter(m.get("languageModelName") or "no AI" for m in rows).most_common()))
    # only recordings that actually went through a language model could have had them removed
    ai = [m for m in rows if m.get("languageModelName")
          and (m.get("rawResult") or "").strip() and (m.get("result") or "").strip()]
    # Counted per recording, not per phrase: one S1-Language run on 2026-09-11 looped and
    # turned 19 "thank you"s into 2,346, which swamps any total.
    n = lambda t: len(re.findall(r"(?i)\bthank you\b", t))
    had = [m for m in ai if n(m["rawResult"])]
    still = [m for m in had if n(m["result"])]
    runaway = [m for m in ai if n(m["result"]) > n(m["rawResult"]) + 5]
    if had:
        print(f'silence "thank you": {len(had)} dictations heard it, {len(still)} still had it '
              f'after the AI pass ({100 * (1 - len(still) / len(had)):.0f}% cleaned)')
    if runaway:
        print(f"  {len(runaway)} runaway: the model repeated it more than it heard "
              f"({', '.join(m['datetime'][:10] + ' ' + (m.get('modeName') or '') for m in runaway[:3])})")


def cmd_add(args):
    text = " ".join(args)
    m = re.split(r"\s*-{1,3}>+\s*|\s*=>\s*", text, maxsplit=1)
    if len(m) != 2:
        sys.exit('usage: sw add "heard --> wanted"')
    heard, wanted = m[0].strip(), m[1].strip()
    if re.fullmatch(r"[a-z]{1,4}", heard.lower()):
        print(f"refusing {heard!r}: short strings match inside other words (CLAUDE.md rule 11)")
        return
    path = os.path.join(HERE, "replacements.md")
    existing = {l.split("|")[1].strip().lower() for l in open(path, encoding="utf-8") if l.startswith("| ")}
    if heard.lower() in existing:
        print(f"{heard!r} already has a rule")
        return
    today = datetime.date.today().isoformat()
    open(path, "a", encoding="utf-8").write(f"| {heard} | {wanted} | {today} | added with sw |\n")
    print(f"added: {heard} -> {wanted}")
    run_sync()


def cmd_vocab(args):
    path = os.path.join(HERE, "vocabulary.md")
    if not args:
        s = json.load(open(settings(), encoding="utf-8"))
        print(f"{len(s['vocabulary'])} terms live in the app:\n  " + "\n  ".join(s["vocabulary"]))
        return
    term = " ".join(args)
    text = open(path, encoding="utf-8").read()
    if term.lower() in [l[2:].strip().lower() for l in text.splitlines() if l.startswith("- ")]:
        print(f"{term!r} is already in the vocabulary")
        return
    open(path, "a", encoding="utf-8").write(f"- {term}\n")
    print(f"added {term!r} to the vocabulary")
    run_sync()


def cmd_rules(args):
    s = json.load(open(settings(), encoding="utf-8"))
    reps = s["replacements"]
    if args:
        q = " ".join(args).lower()
        reps = [r for r in reps if q in r["original"].lower() or q in r["with"].lower()]
    for r in reps:
        print(f"  {r['original']:<38} -> {r['with']}")
    print(f"\n{len(reps)} rules" + (f" matching {' '.join(args)!r}" if args else ""))


def cmd_export(args):
    n = int(args[0]) if args else 50
    for m in load(limit=n):
        print(f"\n## {m['datetime'][:16]} · {m.get('modeName','?')}\n")
        print(m.get("result") or m.get("rawResult") or "")


def cmd_scan(args):
    cmd = [sys.executable, os.path.join(HERE, "scan.py")] + (["--since", args[0]] if args else [])
    subprocess.run(cmd, env=dict(os.environ, PYTHONIOENCODING="utf-8"))


def cmd_sync(args):
    run_sync()


def cmd_mode(args):
    prefs = os.path.join(APP, "preferences.json")
    p = json.load(open(prefs, encoding="utf-8"))
    modes = {}
    for f in os.listdir(os.path.join(APP, "modes")):
        d = json.load(open(os.path.join(APP, "modes", f), encoding="utf-8"))
        modes[d["key"]] = d
    if not args:
        a = modes[p["activeMode"]]
        print(f"active: {a['name']} ({a['key']}) · voice {a['voiceModelID']} · "
              f"language {a['languageModelID'] or 'none'}")
        print("\navailable:")
        for k, d in modes.items():
            print(f"  {d['name']:<17} {k:<15} {d['languageModelID'] or 'no AI'}")
        return
    want = " ".join(args).lower()
    hit = next((d for d in modes.values() if want in d["name"].lower() or want == d["key"]), None)
    if not hit:
        sys.exit(f"no mode matching {want!r}")
    p["activeMode"] = hit["key"]
    json.dump(p, open(prefs, "w", encoding="utf-8"), indent=2)
    print(f"active mode set to {hit['name']}. Restarting so the app picks it up.")
    run_sync()


CMDS = {"search": cmd_search, "last": cmd_last, "stats": cmd_stats, "add": cmd_add,
        "vocab": cmd_vocab, "rules": cmd_rules, "export": cmd_export, "scan": cmd_scan,
        "sync": cmd_sync, "mode": cmd_mode}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(__doc__)
        sys.exit(0)
    cmd = sys.argv[1]
    if cmd not in CMDS:
        sys.exit(f"unknown command {cmd!r}. Try: " + ", ".join(CMDS))
    CMDS[cmd](sys.argv[2:])
