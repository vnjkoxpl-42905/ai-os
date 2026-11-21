#!/usr/bin/env python3
"""Build wiki/homework-assigning/ from the LSAT U export.

Reads  : wiki/homework-assigning/data/assignments.generated.json  (run lsatu-assignment-export.mjs first)
         references/lsatu-guided-drill-catalog.json, students/*/sessions, transcript-downloads, recaps
Writes : taxonomy.md, by-topic.md, assignment-log.md, playbook.md, data/*.generated.json

Tags come from the platform's own taxonomy: question type, question feature, reasoning type.
Notes and activities have no tags in the database, so they are tagged here by keyword rules
(RULES below). The rules are a first pass: read taxonomy.md, correct them, re-run.

Usage: py -I system/scripts/build-homework-assigning.py
"""
import json
import re
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "wiki" / "homework-assigning"
WINDOW_DAYS = 3

# tag -> (kind, regex). Lower-case text is searched.
RULES = {
    # question types
    "Flaw": ("question type", r"\bflaw|fallac|famous flaws|mistake first"),
    "Necessary Assumption": ("question type", r"necessary assumption|how much the answer needs|has to assume|negation|assumption family"),
    "Sufficient Assumption": ("question type", r"sufficient assumption|missing link|build the missing|sufficient-assumption"),
    "Weaken": ("question type", r"weaken"),
    "Strengthen": ("question type", r"strengthen"),
    "Must Be True": ("question type", r"must be true|most strongly supported|most supported|inference|guarantees"),
    "Must Be False": ("question type", r"must be false"),
    "Main Conclusion": ("question type", r"main conclusion|find the conclusion|finding the conclusion|conclusion by asking|first sentence conclusion|rebuttal conclusion"),
    "Role": ("question type", r"\brole\b"),
    "Method of Reasoning": ("question type", r"method of reasoning|abstract"),
    "Parallel Reasoning": ("question type", r"parallel"),
    "Principle": ("question type", r"principle|rule behind the verdict"),
    "Paradox": ("question type", r"paradox|curious fact"),
    "Evaluate": ("question type", r"\bevaluate"),
    "Agree/Disagree": ("question type", r"agree|disagree|two speaker|2-speaker"),
    # question features
    "Quantifiers": ("question feature", r"quantif|quantity word|some, most|most, and all"),
    "Explain Curious Fact": ("question feature", r"curious fact"),
    "Famous Flaws": ("question feature", r"famous flaws"),
    "Anti-Causal": ("question feature", r"anti-causal"),
    "Contrapositive Logic": ("question feature", r"contrapositive"),
    "Conditional Diagramming": ("question feature", r"diagram|conditional rephrase|chains"),
    "Missing Link / Idea": ("question feature", r"missing link|missing connection"),
    "First Sentence Conclusion": ("question feature", r"first sentence"),
    "Rebuttals": ("question feature", r"rebuttal"),
    "Analogies": ("question feature", r"analog"),
    "Intermediate Conclusions": ("question feature", r"intermediate conclusion"),
    "Science": ("question feature", r"\bscience"),
    # reasoning types
    "Causation": ("reasoning type", r"causa|cause|causal"),
    "Conditional Logic": ("reasoning type", r"conditional|contrapositive|sufficient|necessary|unless|if-then"),
    "Comparison": ("reasoning type", r"comparison|analog|similar|difference-maker|difference maker"),
    # activities / practice mode (not in the platform taxonomy)
    "Reading Comprehension": ("practice mode", r"reading comprehension|reading center|rc recall|rc training|passage|recall, colour|read, recall"),
    "Timed section / PrepTest": ("practice mode", r"timed section|preptest|practice_test|\bpt ?\d+"),
    "Warm-up": ("practice mode", r"warm-up|warm up"),
    "Onboarding": ("practice mode", r"welcome to your classroom"),
}
QTYPE_NORMALISE = [
    (r"parallel.*flaw|flawed parallel", "Parallel Reasoning"),
    (r"^parallel", "Parallel Reasoning"),
    (r"^principle", "Principle"),
]
REASONING_NORMALISE = {"Conditional Reasoning": "Conditional Logic"}


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def tags_from_text(text):
    t = text.lower()
    return sorted({tag for tag, (_, rx) in RULES.items() if re.search(rx, t)})


def norm_qtype(q):
    for rx, to in QTYPE_NORMALISE:
        if re.search(rx, q, re.I):
            return to
    return q


def load():
    data = json.loads((OUT / "data" / "assignments.generated.json").read_text(encoding="utf8"))
    cat = json.loads((ROOT / "references" / "lsatu-guided-drill-catalog.json").read_text(encoding="utf8"))
    return data, cat


def drill_tags(d):
    tags = {norm_qtype(q) for q in d.get("question_types", [])}
    tags |= set(d.get("question_features", []))
    tags |= {REASONING_NORMALISE.get(r, r) for r in d.get("reasoning_types", [])}
    return sorted(tags)


def sessions_for(slug):
    """date -> (label, text used for tagging). Sources: session folders, Gemini exports, recaps."""
    base = ROOT / "students" / slug
    found = {}
    sdir = base / "sessions"
    if sdir.is_dir():
        for d in sorted(sdir.iterdir()):
            m = re.match(r"(\d{4}-\d\d-\d\d)-(.*)", d.name)
            if not m:
                continue
            text = m.group(2).replace("-", " ")
            for f in ("summary.md", "recap.md"):
                p = d / f
                if p.exists():
                    text += " " + p.read_text(encoding="utf8", errors="ignore")[:4000]
            found[m.group(1)] = (m.group(2).replace("-", " "), text)
    for sub in ("transcript-downloads", "recaps"):
        p = base / sub
        if p.is_dir():
            for f in sorted(p.glob("*.md")):
                m = re.match(r"(\d{4}-\d\d-\d\d)", f.name)
                if not m:
                    continue
                # Gemini exports open with a short summary and "Next steps", then the full
                # transcript. Only the opening describes the session's topics.
                txt = f.read_text(encoding="utf8", errors="ignore")[:2600 if sub == "transcript-downloads" else 4500]
                if m.group(1) in found:
                    found[m.group(1)] = (found[m.group(1)][0], found[m.group(1)][1] + " " + txt)
                else:
                    found[m.group(1)] = ("", txt)
    return found


def session_tags(text):
    """Tag a session only when a topic is said at least twice, to avoid passing mentions."""
    t = text.lower()
    skip = ("Onboarding", "Warm-up", "Timed section / PrepTest", "Comparison", "Evaluate")
    return sorted({tag for tag, (_, rx) in RULES.items() if len(re.findall(rx, t)) >= 2 and tag not in skip})


def d(s):
    return date.fromisoformat(s)


def main():
    data, cat = load()
    drills = {x["title"]: x for x in cat["drills"] if x.get("is_published")}
    catalog = {"drills": [], "activities_bootcamps": []}
    for x in cat["drills"]:
        catalog["drills"].append({"slug": x["slug"], "title": x["title"], "published": x.get("is_published"), "level": x.get("category"),
                                  "questions": x.get("question_count"), "minutes": x.get("estimated_minutes"), "tags": drill_tags(x)})
    (OUT / "data").mkdir(parents=True, exist_ok=True)

    rows = data["rows"]
    for r in rows:
        if r["type"] == "drill" and r["title"] in drills:
            r["tags"] = drill_tags(drills[r["title"]])
            r["tag_source"] = "catalog"
        else:
            text = r["title"] + " " + " ".join(r.get("outline") or [])
            r["tags"] = tags_from_text(text)
            r["tag_source"] = "keyword rules"
    (OUT / "data" / "assignments.tagged.generated.json").write_text(json.dumps({"rows": rows}, indent=1), encoding="utf8")
    (OUT / "data" / "catalog.generated.json").write_text(json.dumps(catalog, indent=1), encoding="utf8")

    # ---- link each assignment to the session before it
    by_student = defaultdict(list)
    for r in rows:
        by_student[r["key"]].append(r)
    sess_cache = {}
    link = {}  # item id -> (session date, label) or None
    session_items = defaultdict(list)  # (key, date) -> rows
    sess_meta = {}
    for key, items in by_student.items():
        sess = sessions_for(key) if (ROOT / "students" / key).is_dir() else {}
        sess_cache[key] = sess
        dates = sorted(sess)
        for r in items:
            if r["type"] == "note" and r["title"].startswith("Welcome"):
                link[r["id"]] = None
                continue
            a = d(r["added"])
            best = None
            for sd in dates:
                dd = d(sd)
                if dd <= a <= dd + timedelta(days=WINDOW_DAYS):
                    best = sd
            link[r["id"]] = best
            if best:
                session_items[(key, best)].append(r)
                sess_meta[(key, best)] = sess[best]

    # ---- by-topic.md
    topic_notes = defaultdict(list)
    topic_other = defaultdict(list)
    for r in rows:
        for t in r["tags"]:
            if r["type"] in ("note", "session_recap"):
                topic_notes[t].append(r)
            elif r["type"] in ("activity", "bootcamp_module"):
                topic_other[t].append(r)
    topic_drills = defaultdict(list)
    for x in catalog["drills"]:
        if x["published"]:
            for t in x["tags"]:
                topic_drills[t].append(x)
    kinds = {t: k for t, (k, _) in RULES.items()}
    all_tags = sorted(set(topic_notes) | set(topic_drills) | set(topic_other), key=lambda t: (kinds.get(t, "question feature"), t))
    lines = ["---", "title: Homework assigning, by topic", "type: reference", "status: generated, first pass", "---", "",
             "# By topic: what was assigned before, and what exists",
             "", "Generated by `system/scripts/build-homework-assigning.py` from LSAT U. Do not hand-edit; fix the tag rules instead.",
             "Notes and activities are tagged by keyword rules on their title and headings, so a tag can be missing or wrong. Drills are tagged from the platform catalog and are exact.", ""]
    for t in all_tags:
        lines += [f"## {t}", f"_{kinds.get(t, 'platform tag')}_", ""]
        ns = sorted(topic_notes.get(t, []), key=lambda r: r["added"], reverse=True)
        if ns:
            lines.append("**Notes assigned before** (newest first)")
            for r in ns[:12]:
                lk = f" · [html]({r['archive']})" if r.get("archive") else ""
                lines.append(f"- {r['added']} · {r['student']} · {r['title']}{lk}")
            if len(ns) > 12:
                lines.append(f"- … {len(ns) - 12} more in the data file")
            lines.append("")
        ot = sorted({(r["type"], r["title"]) for r in topic_other.get(t, [])})
        if ot:
            lines.append("**Activities and bootcamp modules assigned before**")
            for ty, ti in ot[:10]:
                lines.append(f"- {ti} ({ty})")
            lines.append("")
        dr = topic_drills.get(t, [])
        if dr:
            lines.append(f"**Guided drills in the catalog** ({len(dr)})")
            for x in sorted(dr, key=lambda x: x["title"])[:14]:
                lines.append(f"- {x['title']} · `{x['slug']}` · {x['questions']} questions")
            if len(dr) > 14:
                lines.append(f"- … {len(dr) - 14} more")
            lines.append("")
    (OUT / "by-topic.md").write_text("\n".join(lines), encoding="utf8")

    # ---- assignment-log.md (running, session by session)
    lines = ["---", "title: Assignment log", "type: ledger", "status: generated", "---", "", "# Assignment log: what followed each session",
             "", f"Each assignment is linked to the latest session on or before its added date, within {WINDOW_DAYS} days. Items with no session in that window are listed under \"Between sessions\".",
             "Generated; re-run `build-homework-assigning.py` after `lsatu-assignment-export.mjs`. Session topic tags use the same keyword rules and need two mentions.", ""]
    for key in sorted(by_student):
        items = by_student[key]
        name = items[0]["student"]
        lines += [f"## {name} (`{key}`)", ""]
        sess = sess_cache.get(key, {})
        for sd in sorted(sess, reverse=True):
            its = session_items.get((key, sd), [])
            if not its:
                continue
            tg = session_tags(sess[sd][1])
            lines.append(f"### Session {sd}" + (f" · {sess[sd][0]}" if sess[sd][0] else ""))
            if tg:
                lines.append(f"Topics: {', '.join(tg)}")
            for r in sorted(its, key=lambda r: (r["added"], r["type"])):
                due = f" · due {r['due']}" if r["due"] else ""
                lines.append(f"- {r['added']} · {r['type']} · {r['title']}{due} · tags: {', '.join(r['tags']) or 'none'}")
            lines.append("")
        loose = sorted([r for r in items if link.get(r["id"]) is None], key=lambda r: r["added"], reverse=True)
        if loose:
            lines.append("### Between sessions")
            for r in loose:
                lines.append(f"- {r['added']} · {r['type']} · {r['title']} · {r['status']}")
            lines.append("")
    (OUT / "assignment-log.md").write_text("\n".join(lines), encoding="utf8")

    # ---- playbook.md: what followed sessions on each topic (observed counts)
    follow = defaultdict(Counter)
    n_sessions = Counter()
    for (key, sd), its in session_items.items():
        tg = session_tags(sess_meta[(key, sd)][1]) or []
        for t in tg:
            n_sessions[t] += 1
            seen = set()
            for r in its:
                label = f"{r['type']}: {r['title']}" if r["type"] != "drill" else f"drill: {r['title']}"
                if label not in seen:
                    follow[t][label] += 1
                    seen.add(label)
    lines = ["---", "title: Homework assigning playbook", "type: playbook", "status: draft, inferred from past assignments, not yet confirmed by Joshua", "---", "",
             "# Playbook: in this situation, assign this", "",
             "This is what the record shows, not what Joshua has said is the rule. Each line says how many past sessions on a topic were followed by that assignment. Confirm or correct it in the grilling.", "",
             "## How to use it on a new transcript", "",
             "1. Tag the session: question types, question features, reasoning types (see `taxonomy.md`).",
             "2. For each tag, read the topic's section below and in `by-topic.md`: the closest earlier note, the drills, any activity.",
             "3. Check what the student already holds (`students/<slug>/homework/already-assigned/index.md`). No repeats.",
             "4. Propose; never assign before Joshua approves. A topic with no prior: query the second brain (`second-brain-query`), then build from scratch.", ""]
    for t in sorted(follow, key=lambda t: -n_sessions[t]):
        lines += [f"## {t}  ({n_sessions[t]} past sessions)", ""]
        for label, c in follow[t].most_common(8):
            lines.append(f"- {c} of {n_sessions[t]} sessions: {label}")
        lines.append("")
    (OUT / "playbook.md").write_text("\n".join(lines), encoding="utf8")

    # ---- taxonomy.md
    qt = Counter(t for r in rows for t in r["tags"] if kinds.get(t) == "question type")
    lines = ["---", "title: Homework assigning taxonomy", "type: reference", "status: generated", "---", "", "# Tags", "",
             "Question type, question feature and reasoning type are the platform's own fields (`src/lib/questionLoader.ts`, the guided drill catalog). Practice mode is added here for activities and Reading Comprehension.", "",
             "| Tag | Kind | Keyword rule | Items tagged |", "|---|---|---|---|"]
    cnt = Counter(t for r in rows for t in r["tags"])
    for t, (k, rx) in RULES.items():
        lines.append(f"| {t} | {k} | `{rx}` | {cnt.get(t, 0)} |")
    untagged = [r for r in rows if not r["tags"] and r["type"] in ("note", "activity", "bootcamp_module")]
    lines += ["", f"## Untagged notes, activities and modules ({len(untagged)})", "", "These match no rule. Either add a rule or they are off-topic.", ""]
    for r in untagged[:60]:
        lines.append(f"- {r['added']} · {r['student']} · {r['type']} · {r['title']}")
    (OUT / "taxonomy.md").write_text("\n".join(lines), encoding="utf8")

    print(json.dumps({"items": len(rows), "tagged": sum(1 for r in rows if r["tags"]), "untagged_notes_etc": len(untagged),
                      "linked": sum(1 for v in link.values() if v), "sessions_with_items": len(session_items)}, indent=1))


if __name__ == "__main__":
    main()
