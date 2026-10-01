"""Validate batch 02 Flaw drafts and emit guarded insert-only SQL, one transaction per slot. No database writes.

Handles four slot states:
  unloaded     question absent: insert question + choices (bank text) + explanation
  unexplained  question present, no single/standard explanation: insert explanation
  notes-only   explanation has steps but no notes: insert five notes
  partial      explanation has steps and some notes: insert only the missing letters
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from project_paths import project_path
import json
import re
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[3]
DRAFTS = [ROOT / f"corpus/lr-explanations/drafts/batch-02-flaw-part-{p}.md" for p in "ab"]
DB = ROOT / "system/scripts/lsatlab-pull/data/db"
BANK = project_path("lsatu-wt-glossary", "public", "data")
OUT = ROOT / "corpus/lr-explanations/work/batch-02-inputs"
Q = "$batch02$"
TYPE_FIX = {"PT147-S4-Q16": "Parallel Flaw", "PT156-S4-Q24": "Parallel Flaw"}
TEXT_FIX = {("PT127-S1-Q4", "questionStem"): ("�", "’")}


def lit(s):
    if Q in s:
        raise ValueError("delimiter in text")
    return f"{Q}{s}{Q}"


def norm_text(s):
    """Collapse hard line wraps inside paragraphs; keep blank-line paragraph breaks."""
    paras = re.split(r"\n\s*\n", s.strip())
    return "\n\n".join(re.sub(r"\s*\n\s*", " ", p).strip() for p in paras)


def records(name):
    return json.loads((DB / f"{name}.json").read_text(encoding="utf-8"))


def parse_drafts():
    slots = {}
    for path in DRAFTS:
        text = path.read_text(encoding="utf-8")
        for sec in text.split("\n## ")[1:]:
            head = sec.split("\n", 1)[0]
            slot, qtype, key = [x.strip() for x in head.split("|")]
            steps, notes = [], {}
            bd = sec.split("### Argument Breakdown", 1)
            if len(bd) == 2:
                part = bd[1].split("### Choice Notes", 1)[0]
                for m in re.finditer(r"^\*\*(.+?):\*\* (.+?)(?=\n\n\*\*|\Z)", part.strip(), re.S | re.M):
                    steps.append((m.group(1).strip(), m.group(2).strip()))
            cn = sec.split("### Choice Notes", 1)[1]
            for m in re.finditer(r"^\*\*\(([A-E])\) (.+?)\.\*\* (.+?)(?=\n\n\*\*\(|\Z)", cn.strip(), re.S | re.M):
                notes[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
            slots[slot] = dict(type=qtype, key=key, steps=steps, notes=notes)
    return slots


def main():
    drafts = parse_drafts()
    bank = {}
    for f in BANK.glob("PT*-S*-LR.json"):
        for b in json.loads(f.read_text(encoding="utf-8")):
            bank[f"{b['practiceTest']}-S{b['sectionNumber']}-Q{b['questionNumber']}"] = b
    qs = {q["qid"]: q for q in records("lr_questions")}
    exq = defaultdict(list)
    for e in records("lr_explanations"):
        if e["style"] in ("single", "standard"):
            exq[e["question_id"]].append(e)
    st = defaultdict(list)
    for s in records("lr_explanation_steps"):
        st[s["explanation_id"]].append(s)
    nt = defaultdict(dict)
    for n in records("lr_explanation_choice_notes"):
        nt[n["explanation_id"]][n["letter"]] = n["body"]

    errors, manifest = [], []
    OUT.mkdir(parents=True, exist_ok=True)
    for slot, d in drafts.items():
        b = bank[slot]
        if d["key"] != b["correctAnswer"]:
            errors.append(f"{slot}: key mismatch")
        q = qs.get(slot)
        sql = [f"-- {slot}. Approved 2026-10-01.", "BEGIN;"]
        if q is None:
            state = "unloaded"
            if len(d["steps"]) < 3 or sorted(d["notes"]) != list("ABCDE"):
                errors.append(f"{slot}: unloaded slot needs steps and five notes")
            pt, sec, num = int(b["practiceTest"][2:]), b["sectionNumber"], b["questionNumber"]
            stim = norm_text(b["stimulus"])
            stem = norm_text(b["questionStem"])
            fix = TEXT_FIX.get((slot, "questionStem"))
            if fix:
                stem = stem.replace(*fix)
            if "�" in stim + stem + "".join(b["answerChoices"].values()):
                errors.append(f"{slot}: damaged character in bank text")
            qtype = TYPE_FIX.get(slot, "Flaw")
            sql.append(f"DO $guard$ BEGIN IF EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={lit(slot)}) THEN RAISE EXCEPTION 'Unloaded slot now exists: {slot}'; END IF; END $guard$;")
            sql.append(f"DO $guard$ BEGIN IF (SELECT COUNT(*) FROM lr_sections s WHERE s.preptest={pt} AND s.section={sec}) <> 1 THEN RAISE EXCEPTION 'Section unavailable: {slot}'; END IF; END $guard$;")
            sql.append(f"INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note) SELECT s.id, {lit(slot)}, {pt}, {sec}, {num}, {lit(qtype)}, {lit(stim)}, {lit(stem)}, {lit(b['correctAnswer'])}, true, {lit('Batch 02 approved 2026-10-01; question text from local bank.')} FROM lr_sections s WHERE s.preptest={pt} AND s.section={sec} AND NOT EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={lit(slot)}) ON CONFLICT DO NOTHING;")
            for L in "ABCDE":
                tag = d["notes"][L][0]
                sql.append(f"INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct) SELECT q.id, {lit(L)}, {lit(norm_text(b['answerChoices'][L]))}, {lit(tag)}, {'true' if L == b['correctAnswer'] else 'false'} FROM lr_questions q WHERE q.qid={lit(slot)} AND NOT EXISTS (SELECT 1 FROM lr_answer_choices c WHERE c.question_id=q.id AND c.letter={lit(L)}) ON CONFLICT DO NOTHING;")
            target = "e.style='single'"
            new_expl = True
        else:
            exps = exq[q["id"]]
            sql.append(f"DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={lit(slot)} AND q.stimulus={lit(q['stimulus'])} AND q.prompt={lit(q['prompt'])} AND q.correct_choice={lit(q['correct_choice'])}) THEN RAISE EXCEPTION 'Question changed: {slot}'; END IF; END $guard$;")
            if q["correct_choice"] != d["key"]:
                errors.append(f"{slot}: DB key differs")
            if not exps:
                state, new_expl, target = "unexplained", True, "e.style='single'"
                sql.append(f"DO $guard$ BEGIN IF (SELECT COUNT(*) FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={lit(slot)} AND e.style IN ('single','standard')) <> 0 THEN RAISE EXCEPTION 'Explanation row changed: {slot}'; END IF; END $guard$;")
            else:
                if len(exps) != 1:
                    errors.append(f"{slot}: {len(exps)} explanation rows")
                    continue
                e = exps[0]
                have = sorted(nt[e["id"]])
                state = "partial" if have else "notes-only"
                new_expl, target = False, f"e.id={lit(e['id'])}"
                missing = [L for L in "ABCDE" if L not in have]
                if sorted(d["notes"]) != missing or d["steps"]:
                    errors.append(f"{slot}: draft letters {sorted(d['notes'])} vs missing {missing}")
                sql.append(f"DO $guard$ BEGIN IF (SELECT COUNT(*) FROM lr_explanation_steps s WHERE s.explanation_id={lit(e['id'])}) <> {len(st[e['id']])} OR (SELECT COUNT(*) FROM lr_explanation_choice_notes n WHERE n.explanation_id={lit(e['id'])}) <> {len(have)} THEN RAISE EXCEPTION 'Explanation changed: {slot}'; END IF; END $guard$;")
        if new_expl:
            sql.append(f"INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.qid={lit(slot)} AND NOT EXISTS (SELECT 1 FROM lr_explanations e WHERE e.question_id=q.id AND e.style IN ('single','standard')) ON CONFLICT DO NOTHING;")
            vals = ", ".join(f"({i}, {lit(l)}, {lit(bd)})" for i, (l, bd) in enumerate(d["steps"]))
            sql.append(f"INSERT INTO lr_explanation_steps (explanation_id, position, label, body) SELECT e.id, v.position, v.label, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES {vals}) v(position,label,body) WHERE q.qid={lit(slot)} AND {target} AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ON CONFLICT DO NOTHING;")
        nvals = ", ".join(f"({lit(L)}, {lit(d['notes'][L][1])})" for L in sorted(d["notes"]))
        sql.append(f"INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body) SELECT e.id, v.letter, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES {nvals}) v(letter,body) WHERE q.qid={lit(slot)} AND {target} AND NOT EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id AND n.letter=v.letter) ON CONFLICT DO NOTHING;")
        sql.append("COMMIT;")
        fname = f"batch02-{slot.lower()}.sql"
        (OUT / fname).write_text("\n".join(sql) + "\n", encoding="utf-8")
        manifest.append(dict(slot=slot, file=fname, state=state, steps=len(d["steps"]), notes=len(d["notes"])))
    (OUT / "batch02-sql-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    if errors:
        print("ERRORS:\n" + "\n".join(errors))
        sys.exit(1)
    from collections import Counter
    print(f"{len(manifest)} slots", Counter(m["state"] for m in manifest), "steps", sum(m["steps"] for m in manifest), "notes", sum(m["notes"] for m in manifest))


if __name__ == "__main__":
    main()
