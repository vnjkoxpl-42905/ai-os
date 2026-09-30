"""Validate 40 Flaw drafts and emit guarded insert-only SQL. No database writes."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from project_paths import project_path, VAULT_ROOT
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DRAFTS = [ROOT / f"corpus/lr-explanations/drafts/batch-01-flaw-part-{p}.md" for p in "ab"]
DB = ROOT / "system/scripts/lsatlab-pull/data/db"
BANK = project_path("lsatu-wt-glossary", "public", "data")
OUTPUT = ROOT / "corpus/lr-explanations/work/batch-01-inputs"
NOTES_ONLY = {"PT102-S3-Q14", "PT119-S2-Q24"}
# These source disagreements are independently known and must remain visible.
# SQL guards the database's exact existing bytes; no question or choice text is changed.
KNOWN_DB_VARIANTS = {
    ("PT101-S3-Q2", "stimulus"),  # time/times, liveliness/loveliness
    ("PT101-S3-Q2", "choice B"),  # its/is the cause
    ("PT105-S2-Q15", "stimulus"),  # school of official/school official
    ("PT106-S3-Q5", "stimulus"),  # bank has shared-passage header
}


def records(name):
    return json.loads((DB / f"{name}.json").read_text(encoding="utf-8"))


def lexical(text):
    text = unicodedata.normalize("NFKC", text or "").casefold()
    return re.sub(r"[^a-z0-9]+", "", text)


def sql(value):
    if isinstance(value, int):
        return str(value)
    if "$batch01$" in value:
        raise ValueError("SQL delimiter in authored text")
    return f"$batch01${value}$batch01$"


def parse_drafts():
    parsed, order = {}, []
    for path in DRAFTS:
        source = path.read_text(encoding="utf-8")
        hits = list(re.finditer(r"(?m)^## (?:\d+\. )?(PT\d+-S\d+-Q\d+) (?:·|\|) .*? (?:Answer |\| )([A-E])(?: · Notes only)?$", source))
        if len(hits) != 20:
            raise ValueError(f"Expected 20 headings in {path}, found {len(hits)}")
        for i, hit in enumerate(hits):
            slot = hit.group(1)
            if slot in parsed:
                raise ValueError(f"Duplicate slot: {slot}")
            chunk = source[hit.end():hits[i + 1].start() if i + 1 < len(hits) else len(source)]
            quoted = "\n".join(re.findall(r"(?m)^> ?(.*)$", chunk.split("###", 1)[0]))
            parts = [p.replace("\n", " ").strip() for p in re.split(r"\n\s*\n", quoted) if p.strip()]
            if len(parts) < 3:
                raise ValueError(f"Missing quoted question text: {slot}")
            breakdown = chunk.split("### Argument Breakdown", 1)[1].split("### Choice Notes", 1)[0] if "### Argument Breakdown" in chunk else ""
            step_hits = list(re.finditer(r"(?m)^\*\*([^*\n]+)\*\*\s*", breakdown))
            steps = [(m.group(1).strip().rstrip(":"), breakdown[m.end():step_hits[j + 1].start() if j + 1 < len(step_hits) else len(breakdown)].strip()) for j, m in enumerate(step_hits)]
            if "### Choice Notes" not in chunk:
                raise ValueError(f"Missing choice notes: {slot}")
            notes_part = chunk.split("### Choice Notes", 1)[1]
            note_hits = list(re.finditer(r"(?m)^\*\*\(([A-E])\) ([^*\n]+)\*\*\s*", notes_part))
            notes = [(m.group(1), m.group(2).strip().rstrip("."), notes_part[m.end():note_hits[j + 1].start() if j + 1 < len(note_hits) else len(notes_part)].strip()) for j, m in enumerate(note_hits)]
            if any(not body for _, body in steps) or any(not body for _, _, body in notes):
                raise ValueError(f"Empty authored body: {slot}")
            parsed[slot] = dict(answer=hit.group(2), stimulus="\n\n".join(parts[:-2]), stem=parts[-2],
                                choices=parts[-1], steps=steps, notes=notes)
            order.append(slot)
    if len(order) != 40 or (order[0], order[19], order[20], order[-1]) != (
        "PT101-S3-Q2", "PT108-S2-Q18", "PT109-S3-Q5", "PT119-S3-Q2"
    ):
        raise ValueError("Unexpected 40-slot order")
    return parsed, order


def main():
    draft, slots = parse_drafts()
    questions = {q["qid"]: q for q in records("lr_questions")}
    choices, explanations, steps, notes = (defaultdict(dict), defaultdict(list), defaultdict(list), defaultdict(list))
    for row in records("lr_answer_choices"):
        choices[row["question_id"]][row["letter"]] = row
    for row in records("lr_explanations"):
        if row["style"] in ("single", "standard"):
            explanations[row["question_id"]].append(row)
    for table, destination in (("lr_explanation_steps", steps), ("lr_explanation_choice_notes", notes)):
        for row in records(table):
            destination[row["explanation_id"]].append(row)

    errors = []
    for slot in slots:
        pt, section, number = map(int, re.fullmatch(r"PT(\d+)-S(\d+)-Q(\d+)", slot).groups())
        bank_file = BANK / f"PT{pt}-S{section}-LR.json"
        found = [b for b in json.loads(bank_file.read_text(encoding="utf-8")) if b["questionNumber"] == number]
        if len(found) != 1:
            errors.append(f"{slot}: bank match count {len(found)}")
            continue
        b, d, q = found[0], draft[slot], questions.get(slot)
        if not q:
            errors.append(f"{slot}: missing database question")
            continue
        for name, draft_text, bank_text, db_text in (("stimulus", d["stimulus"], b["stimulus"], q["stimulus"]),
                                                      ("stem", d["stem"], b["questionStem"], q["prompt"])):
            if lexical(draft_text) != lexical(bank_text):
                errors.append(f"{slot}: draft {name} differs from bank")
            if lexical(db_text) != lexical(bank_text) and (slot, name) not in KNOWN_DB_VARIANTS:
                errors.append(f"{slot}: database {name} differs from bank")
        if d["answer"] != b["correctAnswer"] or q["correct_choice"] != b["correctAnswer"]:
            errors.append(f"{slot}: answer key disagreement")
        draft_choices = dict(re.findall(r"\(([A-E])\)\s*(.*?)(?=\s*\([A-E]\)|$)", d["choices"]))
        if set(draft_choices) != set("ABCDE") or set(choices[q["id"]]) != set("ABCDE"):
            errors.append(f"{slot}: incomplete choices")
        else:
            for letter, bank_text in b["answerChoices"].items():
                if lexical(draft_choices[letter]) != lexical(bank_text):
                    errors.append(f"{slot}: draft choice {letter} differs from bank")
                if lexical(choices[q["id"]][letter]["choice_text"]) != lexical(bank_text) and (slot, f"choice {letter}") not in KNOWN_DB_VARIANTS:
                    errors.append(f"{slot}: database choice {letter} differs from bank")
        if [x[0] for x in d["notes"]] != list("ABCDE"):
            errors.append(f"{slot}: expected A-E notes in order")
        if slot in NOTES_ONLY and d["steps"]:
            errors.append(f"{slot}: notes-only slot has draft steps")
        if slot not in NOTES_ONLY and len(d["steps"]) < 2:
            errors.append(f"{slot}: missing draft breakdown")
        es = explanations[q["id"]]
        prior_steps = sum(len(steps[e["id"]]) for e in es)
        prior_notes = sum(len(notes[e["id"]]) for e in es)
        if slot in NOTES_ONLY and (prior_steps == 0 or prior_notes != 0):
            errors.append(f"{slot}: expected prior steps only, found {prior_steps}/{prior_notes}")
        if slot not in NOTES_ONLY and (prior_steps or prior_notes):
            errors.append(f"{slot}: unexpected prior content {prior_steps}/{prior_notes}")
    if errors:
        raise SystemExit("Preflight failed; no SQL emitted:\n" + "\n".join(errors))

    OUTPUT.mkdir(parents=True, exist_ok=True)
    combined, manifest = ["-- Draft only. Execute after user approval.", "BEGIN;", ""], []
    for slot in slots:
        d, q = draft[slot], questions[slot]
        es = explanations[q["id"]]
        old_steps = sum(len(steps[e["id"]]) for e in es)
        old_notes = sum(len(notes[e["id"]]) for e in es)
        lines = [f"-- {slot}",
                 f"DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={sql(slot)} AND q.stimulus={sql(q['stimulus'])} AND q.prompt={sql(q['prompt'])} AND q.correct_choice={sql(q['correct_choice'])}) THEN RAISE EXCEPTION 'Question changed: {slot}'; END IF; END $guard$;"]
        lines.append(f"DO $guard$ BEGIN IF (SELECT COUNT(*) FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={sql(slot)} AND e.style IN ('single','standard')) <> {len(es)} THEN RAISE EXCEPTION 'Explanation row changed: {slot}'; END IF; END $guard$;")
        for letter in "ABCDE":
            lines.append(f"DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid={sql(slot)} AND c.letter={sql(letter)} AND c.choice_text={sql(choices[q['id']][letter]['choice_text'])}) THEN RAISE EXCEPTION 'Choice changed: {slot} {letter}'; END IF; END $guard$;")
        lines.append("DO $guard$ BEGIN IF "
                     f"(SELECT COUNT(*) FROM lr_explanation_steps s JOIN lr_explanations e ON e.id=s.explanation_id JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={sql(slot)} AND e.style IN ('single','standard')) <> {old_steps} OR "
                     f"(SELECT COUNT(*) FROM lr_explanation_choice_notes n JOIN lr_explanations e ON e.id=n.explanation_id JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={sql(slot)} AND e.style IN ('single','standard')) <> {old_notes} "
                     f"THEN RAISE EXCEPTION 'Explanation changed: {slot}'; END IF; END $guard$;")
        if slot in NOTES_ONLY:
            targets = [e for e in es if steps[e["id"]]]
            if len(targets) != 1:
                raise ValueError(f"Ambiguous existing explanation: {slot}")
            selector = f"e.id={sql(targets[0]['id'])}"
            lines.append(f"DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={sql(slot)} AND e.id={sql(targets[0]['id'])} AND e.style={sql(targets[0]['style'])}) THEN RAISE EXCEPTION 'Target explanation changed: {slot}'; END IF; END $guard$;")
            prior = steps[targets[0]["id"]]
            expected = ", ".join(
                f"({sql(step['id'])}, {sql(step['position'])}, {sql(step['label'])}, {sql(step['body'])})"
                for step in prior
            )
            lines.append(
                "DO $guard$ BEGIN IF "
                f"(SELECT COUNT(*) FROM lr_explanation_steps s WHERE s.explanation_id={sql(targets[0]['id'])} "
                f"AND (s.id::text,s.position,s.label,s.body) IN (VALUES {expected})) <> {len(prior)} "
                f"THEN RAISE EXCEPTION 'Existing step changed: {slot}'; END IF; END $guard$;"
            )
        else:
            if es:
                raise ValueError(f"Unexpected prior explanation: {slot}")
            lines.append(f"INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.qid={sql(slot)} AND NOT EXISTS (SELECT 1 FROM lr_explanations e WHERE e.question_id=q.id AND e.style IN ('single','standard')) ON CONFLICT DO NOTHING;")
            selector = "e.style='single'"
        if d["steps"]:
            values = ", ".join(f"({i}, {sql(label)}, {sql(body)})" for i, (label, body) in enumerate(d["steps"]))
            lines.append("INSERT INTO lr_explanation_steps (explanation_id, position, label, body) "
                         f"SELECT e.id, v.position, v.label, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES {values}) v(position,label,body) "
                         f"WHERE q.qid={sql(slot)} AND {selector} AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ON CONFLICT DO NOTHING;")
        values = ", ".join(f"({sql(letter)}, {sql(body)})" for letter, _tag, body in d["notes"])
        lines.append("INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body) "
                     f"SELECT e.id, v.letter, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES {values}) v(letter,body) "
                     f"WHERE q.qid={sql(slot)} AND {selector} AND NOT EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) ON CONFLICT DO NOTHING;")
        filename = f"batch01-{slot.lower()}.sql"
        per_slot = "\n".join(["-- One slot. Draft only.", "BEGIN;", *lines, "COMMIT;", ""])
        byte_count = len(per_slot.encode("utf-8"))
        if byte_count > 12_000:
            raise ValueError(f"{slot}: {byte_count} bytes exceeds 12 KB")
        (OUTPUT / filename).write_text(per_slot, encoding="utf-8")
        combined.extend(lines + [""])
        manifest.append({"slot": slot, "file": filename, "bytes": byte_count,
                         "steps": len(d["steps"]), "notes": len(d["notes"]), "prior_steps_retained": old_steps})
    combined.extend(["COMMIT;", ""])
    (OUTPUT / "batch01-40-insert-only.sql").write_text("\n".join(combined), encoding="utf-8")
    (OUTPUT / "batch01-sql-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Validated {len(slots)} slots, {sum(len(draft[s]['steps']) for s in slots)} steps, {sum(len(draft[s]['notes']) for s in slots)} notes. SQL at {OUTPUT}")


if __name__ == "__main__":
    main()
