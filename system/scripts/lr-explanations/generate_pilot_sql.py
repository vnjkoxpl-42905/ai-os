"""Validate the approved 20-question LR pilot and emit insert-only SQL.

This script reads local snapshots only. It never connects to the database.
Run from any directory: python system/scripts/lr-explanations/generate_pilot_sql.py
"""

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DRAFT = ROOT / "corpus/lr-explanations/drafts/pilot-2026-09-27.md"
DB = ROOT / "system/scripts/lsatlab-pull/data/db"
BANK = ROOT / "projects/lsatu-wt-glossary/public/data"
OUTPUT = ROOT / "corpus/lr-explanations/work/pilot-inputs/pilot-20-insert-only.sql"
SLOTS = (
    "PT109-S4-Q1", "PT114-S1-Q23", "PT159-S1-Q21", "PT104-S4-Q23",
    "PT109-S3-Q3", "PT108-S3-Q6", "PT156-S4-Q10", "PT110-S2-Q8",
    "PT117-S3-Q8", "PT112-S1-Q3", "PT114-S2-Q21", "PT114-S4-Q12",
    "PT105-S1-Q3", "PT120-S4-Q9", "PT105-S4-Q12", "PT116-S2-Q19",
    "PT128-S3-Q16", "PT105-S1-Q11", "PT115-S2-Q8", "PT104-S4-Q13",
)
UNLOADED = {"PT159-S1-Q21", "PT156-S4-Q10", "PT128-S3-Q16"}
STEPS_ONLY = {"PT108-S3-Q6"}  # Existing choice notes; add breakdown.
NOTES_ONLY = {"PT117-S3-Q8"}  # Existing breakdown; add choice notes.
KNOWN_WORDING_VARIANT = {
    ("PT105-S4-Q12", "E"): (
        "The less willing people are to do without technology the more likely they are to complain about the effects of technology.",
        "The less willing people are to do without technology the more likely they are to complain about the effects of the technology.",
    )
}
QUESTION_TYPE_OVERRIDE = {"PT156-S4-Q10": "Paradox"}  # Bank mislabels this EXCEPT stem.


def records(name):
    return json.loads((DB / f"{name}.json").read_text(encoding="utf-8"))


def norm(value):
    value = unicodedata.normalize("NFKC", value or "").casefold()
    value = value.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", value).strip()


def wording_key(value):
    # The old DB snapshot concatenates speaker paragraphs and contains replacement
    # characters where apostrophes were imported. Compare lexical content here;
    # the emitted SQL still guards the DB snapshot's exact bytes.
    return re.sub(r"[^a-z0-9]+", "", norm(value))


def sql(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    delimiter = "$pilot$"
    if delimiter in value:
        raise ValueError("SQL delimiter appears in source text")
    return f"{delimiter}{value}{delimiter}"


def draft_choices(text):
    return dict(re.findall(r"\(([A-E])\)\s*(.*?)(?=\s*·\s*\([A-E]\)|$)", text))


def parse_draft():
    source = DRAFT.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^## (\d+)\. (PT\d+-S\d+-Q\d+) · .*? · Answer ([A-E])$", source))
    if len(matches) != 20 or tuple(m.group(2) for m in matches) != SLOTS:
        raise ValueError("Pilot headings do not match the approved 20 slots in order")
    parsed = {}
    for i, match in enumerate(matches):
        chunk = source[match.end(): matches[i + 1].start() if i + 1 < len(matches) else len(source)]
        quoted = re.findall(r"(?m)^> ?(.*)$", chunk.split("###", 1)[0])
        paragraphs = re.split(r"\n\s*\n", "\n".join(quoted))
        paragraphs = [p.replace("\n", " ").strip() for p in paragraphs if p.strip()]
        if len(paragraphs) < 3:
            raise ValueError(f"Missing quoted question text: {match.group(2)}")
        steps = []
        notes = []
        if "### Argument Breakdown" in chunk:
            part = chunk.split("### Argument Breakdown", 1)[1].split("### Choice Notes", 1)[0]
            for item in re.finditer(r"(?m)^\*\*([^*\n]+)\*\*\s*$", part):
                following = re.search(r"(?m)^\*\*[^*\n]+\*\*\s*$", part[item.end():])
                end = item.end() + following.start() if following else len(part)
                body = part[item.end():end].strip().removesuffix("\n---").strip()
                if not body:
                    raise ValueError(f"Empty step: {match.group(2)}")
                steps.append((item.group(1).strip(), body))
        if "### Choice Notes" in chunk:
            part = chunk.split("### Choice Notes", 1)[1]
            hits = list(re.finditer(r"(?m)^\*\*\(([A-E])\) ([^*\n]+)\*\*\s*$", part))
            for j, hit in enumerate(hits):
                body = part[hit.end():hits[j + 1].start() if j + 1 < len(hits) else len(part)].strip().removesuffix("\n---").strip()
                if not body:
                    raise ValueError(f"Empty choice note: {match.group(2)} {hit.group(1)}")
                notes.append((hit.group(1), hit.group(2).strip().rstrip("."), body))
        parsed[match.group(2)] = dict(answer=match.group(3), stimulus="\n\n".join(paragraphs[:-2]),
                                      prompt=paragraphs[-2], choices=paragraphs[-1], steps=steps, notes=notes)
    return parsed


def main():
    draft = parse_draft()
    questions = {q["qid"]: q for q in records("lr_questions")}
    choices = defaultdict(dict)
    for choice in records("lr_answer_choices"):
        choices[choice["question_id"]][choice["letter"]] = choice
    explanations = defaultdict(list)
    for explanation in records("lr_explanations"):
        if explanation["style"] in ("single", "standard"):
            explanations[explanation["question_id"]].append(explanation)
    steps = defaultdict(list)
    for step in records("lr_explanation_steps"):
        steps[step["explanation_id"]].append(step)
    notes = defaultdict(list)
    for note in records("lr_explanation_choice_notes"):
        notes[note["explanation_id"]].append(note)

    errors = []
    bank = {}
    for slot in SLOTS:
        pt, section, number = map(int, re.fullmatch(r"PT(\d+)-S(\d+)-Q(\d+)", slot).groups())
        bank_file = BANK / f"PT{pt}-S{section}-LR.json"
        bank_matches = [b for b in json.loads(bank_file.read_text(encoding="utf-8")) if b["questionNumber"] == number]
        if len(bank_matches) != 1:
            errors.append(f"{slot}: bank match count {len(bank_matches)}")
            continue
        b = bank[slot] = bank_matches[0]
        d = draft[slot]
        if wording_key(d["stimulus"]) != wording_key(b["stimulus"]):
            errors.append(f"{slot}: pilot stimulus differs from bank")
        if wording_key(d["prompt"]) != wording_key(b["questionStem"]):
            errors.append(f"{slot}: pilot stem differs from bank")
        if d["answer"] != b["correctAnswer"]:
            errors.append(f"{slot}: pilot answer differs from bank")
        rendered_choices = draft_choices(d["choices"])
        if set(rendered_choices) != set("ABCDE"):
            errors.append(f"{slot}: pilot answer choices are incomplete")
        else:
            for letter, bank_text in b["answerChoices"].items():
                if wording_key(rendered_choices[letter]) != wording_key(bank_text):
                    errors.append(f"{slot}: pilot choice {letter} differs from bank")
        if slot not in STEPS_ONLY and [x[0] for x in d["notes"]] != list("ABCDE"):
            errors.append(f"{slot}: expected five choice notes")
        if slot not in NOTES_ONLY and len(d["steps"]) < 2:
            errors.append(f"{slot}: expected at least two breakdown steps")
        if slot in UNLOADED:
            if slot in questions:
                errors.append(f"{slot}: expected unloaded but question exists")
        else:
            q = questions.get(slot)
            if not q:
                errors.append(f"{slot}: expected existing question")
                continue
            if wording_key(q["stimulus"]) != wording_key(b["stimulus"]) or wording_key(q["prompt"]) != wording_key(b["questionStem"]):
                errors.append(f"{slot}: database question differs from bank")
            if q["correct_choice"] != b["correctAnswer"]:
                errors.append(f"{slot}: database answer differs from bank")
            if set(choices[q["id"]]) != set("ABCDE"):
                errors.append(f"{slot}: database answer choices incomplete")
            else:
                for letter, bank_text in b["answerChoices"].items():
                    db_text = choices[q["id"]][letter]["choice_text"]
                    if wording_key(db_text) != wording_key(bank_text) and (bank_text, db_text) != KNOWN_WORDING_VARIANT.get((slot, letter)):
                        errors.append(f"{slot}: database choice {letter} differs from bank")
            es = explanations[q["id"]]
            step_count = sum(len(steps[e["id"]]) for e in es)
            note_count = sum(len(notes[e["id"]]) for e in es)
            wanted = (0, 5) if slot in STEPS_ONLY else (1, 0) if slot in NOTES_ONLY else (0, 0)
            if slot in NOTES_ONLY:
                good = step_count > 0 and note_count == 0
            else:
                good = (step_count, note_count) == wanted
            if not good:
                errors.append(f"{slot}: existing step/note counts {step_count}/{note_count}, expected {wanted}")
    if errors:
        raise SystemExit("Preflight failed; no SQL emitted:\n" + "\n".join(errors))

    lines = ["-- Approved 20-slot pilot. Generated from pilot-2026-09-27.md and local snapshots.",
             "-- Execute only after reviewing the entire file. Any drift aborts the transaction.",
             "BEGIN;", ""]
    manifest = []
    for slot in SLOTS:
        slot_start = len(lines)
        pt, section, number = map(int, re.fullmatch(r"PT(\d+)-S(\d+)-Q(\d+)", slot).groups())
        d, b = draft[slot], bank[slot]
        q = questions.get(slot)
        lines.append(f"-- {slot}")
        if q:
            lines.append(f"DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={sql(slot)} AND q.stimulus={sql(q['stimulus'])} AND q.prompt={sql(q['prompt'])} AND q.correct_choice={sql(q['correct_choice'])}) THEN RAISE EXCEPTION 'Question changed: {slot}'; END IF; END $guard$;")
            for letter, existing_choice in choices[q["id"]].items():
                lines.append(f"DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid={sql(slot)} AND c.letter={sql(letter)} AND c.choice_text={sql(existing_choice['choice_text'])}) THEN RAISE EXCEPTION 'Choice changed: {slot} {letter}'; END IF; END $guard$;")
            existing = explanations[q["id"]]
            expected_steps = sum(len(steps[e["id"]]) for e in existing)
            expected_notes = sum(len(notes[e["id"]]) for e in existing)
            lines.append(
                "DO $guard$ BEGIN IF "
                f"(SELECT COUNT(*) FROM lr_explanation_steps s JOIN lr_explanations e ON e.id=s.explanation_id JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={sql(slot)} AND e.style IN ('single','standard')) <> {expected_steps} "
                "OR "
                f"(SELECT COUNT(*) FROM lr_explanation_choice_notes n JOIN lr_explanations e ON e.id=n.explanation_id JOIN lr_questions q ON q.id=e.question_id WHERE q.qid={sql(slot)} AND e.style IN ('single','standard')) <> {expected_notes} "
                f"THEN RAISE EXCEPTION 'Explanation changed: {slot}'; END IF; END $guard$;"
            )
        else:
            lines.append(f"DO $guard$ BEGIN IF EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={sql(slot)}) THEN RAISE EXCEPTION 'Unloaded slot now exists: {slot}'; END IF; END $guard$;")
            lines.append(f"DO $guard$ BEGIN IF (SELECT COUNT(*) FROM lr_sections s WHERE s.preptest={pt} AND s.section={section}) <> 1 THEN RAISE EXCEPTION 'Section unavailable: {slot}'; END IF; END $guard$;")
            lines.append("INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note) "
                         f"SELECT s.id, {sql(slot)}, {pt}, {section}, {number}, {sql(QUESTION_TYPE_OVERRIDE.get(slot, b['questionType']))}, {sql(b['stimulus'])}, {sql(b['questionStem'])}, {sql(b['correctAnswer'])}, true, {sql('Pilot approved 2026-09-28; question text from local bank snapshot.')} "
                         f"FROM lr_sections s WHERE s.preptest={pt} AND s.section={section} AND NOT EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid={sql(slot)}) ON CONFLICT DO NOTHING;")
            for letter, choice_text in b["answerChoices"].items():
                lines.append("INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct) "
                             f"SELECT q.id, {sql(letter)}, {sql(choice_text)}, {sql(next((tag for key, tag, _ in d['notes'] if key == letter), ''))}, {sql(letter == b['correctAnswer'])} "
                             f"FROM lr_questions q WHERE q.qid={sql(slot)} AND NOT EXISTS (SELECT 1 FROM lr_answer_choices c WHERE c.question_id=q.id AND c.letter={sql(letter)}) ON CONFLICT DO NOTHING;")
        # Existing content can be under either single or standard; the snapshot guard below
        # rejects drift before any insert. For new questions, create the single row.
        if slot not in STEPS_ONLY and slot not in NOTES_ONLY:
            lines.append(f"INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.qid={sql(slot)} AND NOT EXISTS (SELECT 1 FROM lr_explanations e WHERE e.question_id=q.id AND e.style IN ('single','standard')) ON CONFLICT DO NOTHING;")
        if slot in STEPS_ONLY or slot in NOTES_ONLY:
            existing = explanations[q["id"]]
            target = next((e for e in existing if (notes[e["id"]] if slot in STEPS_ONLY else steps[e["id"]])), None)
            if target is None:
                raise ValueError(f"No target explanation for {slot}")
            target_selector = f"e.id={sql(target['id'])}"
        else:
            target_selector = "e.style='single'"
        if d["steps"]:
            values = ", ".join(f"({pos}, {sql(label)}, {sql(body)})" for pos, (label, body) in enumerate(d["steps"]))
            lines.append("INSERT INTO lr_explanation_steps (explanation_id, position, label, body) "
                         f"SELECT e.id, v.position, v.label, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES {values}) v(position,label,body) "
                         f"WHERE q.qid={sql(slot)} AND {target_selector} AND NOT EXISTS "
                         "(SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ON CONFLICT DO NOTHING;")
        if d["notes"]:
            values = ", ".join(f"({sql(letter)}, {sql(body)})" for letter, _tag, body in d["notes"])
            lines.append("INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body) "
                         f"SELECT e.id, v.letter, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES {values}) v(letter,body) "
                         f"WHERE q.qid={sql(slot)} AND {target_selector} AND NOT EXISTS "
                         "(SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) ON CONFLICT DO NOTHING;")
        lines.append("")
        slot_sql = "\n".join(["-- Approved pilot, one slot per transaction.", "BEGIN;", *lines[slot_start:], "COMMIT;", ""])
        filename = f"pilot-{slot.lower()}.sql"
        byte_count = len(slot_sql.encode("utf-8"))
        if byte_count > 12_000:
            raise ValueError(f"{slot}: {byte_count} bytes exceeds 12 KB per-slot limit")
        (OUTPUT.parent / filename).write_text(slot_sql, encoding="utf-8")
        manifest.append({"slot": slot, "file": filename, "bytes": byte_count,
                         "steps": len(d["steps"]), "notes": len(d["notes"])})
    lines.extend(["COMMIT;", ""])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    (OUTPUT.parent / "pilot-sql-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("Known nonsemantic wording variant: PT105-S4-Q12(E) bank omits the second 'the'; SQL leaves the existing DB choice untouched.")
    print(f"Validated {len(SLOTS)} slots; {sum(len(draft[s]['steps']) for s in SLOTS)} steps and {sum(len(draft[s]['notes']) for s in SLOTS)} notes. Wrote 20 per-slot transactions and manifest to {OUTPUT.parent}")


if __name__ == "__main__":
    main()
