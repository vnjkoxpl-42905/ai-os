"""Build insert-only SQL batches that load LSAT Lab explanations into LSAT U.

Input: data/received/<pull>.json (from /api/questions/<id>), the audit JSON
(for each slot's Coverage State), and the bank (for question text/type).
Every statement only fills gaps: steps go only into an explanation that has
none, notes only where a letter has none, questions only where the slot has no row.

Usage (from an LSAT U checkout root):
  python <this> --pull data/received/explanations-267.json --audit <audit.json> --out <dir> [--max-kb 40]
"""
import argparse, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import html_to_steps as C

SRC = 'Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.'

def lit(s):
    if s is None: return 'NULL'
    tag = 'lsat'
    while ('$%s$' % tag) in s: tag += 'x'
    return '$%s$%s$%s$' % (tag, s, tag)

def where(pt, sec, qn, alias='q'):
    return f"{alias}.preptest={pt} AND {alias}.section={sec} AND {alias}.question_number={qn}"

def steps_sql(pt, sec, qn, steps, explanation_filter):
    vals = ','.join(f"({i},{lit(s['label'])},{lit(s['body'])})" for i, s in enumerate(steps))
    return (f"INSERT INTO lr_explanation_steps (explanation_id, position, label, body)\n"
            f"SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id "
            f"WHERE {where(pt, sec, qn)} AND e.style IN ('single','standard') {explanation_filter} "
            f"AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) "
            f"ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES {vals}) v(p,l,b)\nON CONFLICT DO NOTHING;")

def notes_sql(pt, sec, qn, notes):
    vals = ','.join(f"({lit(L)},{lit(b)})" for L, b in notes if b)
    if not vals: return ''
    return (f"INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)\n"
            f"SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id "
            f"WHERE {where(pt, sec, qn)} AND e.style='single') e, (VALUES {vals}) v(l,b)\nON CONFLICT DO NOTHING;")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pull', required=True); ap.add_argument('--audit', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--max-kb', type=int, default=40)
    a = ap.parse_args()
    cov = {e['slot']: e['coverage'] for e in json.load(open(a.audit, encoding='utf-8'))['lsatlab_explained_lsatu_not']}
    pull = {f"PT{r['pt']}-S{r['sec']}-Q{r['pos']}": r for r in json.load(open(a.pull, encoding='utf-8'))}
    bank = {}
    for f in glob.glob('public/data/PT*-LR.json'):
        for q in json.load(open(f, encoding='utf-8')):
            bank[f"{q['practiceTest']}-S{q['sectionNumber']}-Q{q['questionNumber']}"] = q
    stmts, manifest = [], []
    for slot, c in sorted(cov.items()):
        r = pull.get(slot)
        if not r: manifest.append({'slot': slot, 'skipped': 'not pulled'}); continue
        pt, sec, qn = map(int, re.findall(r'\d+', slot))
        steps = C.steps(r['gf'])
        answers = sorted(r['answers'], key=lambda x: x['pos'])
        notes = [('ABCDE'[x['pos'] - 1],) + C.note(x['fb']) for x in answers]  # (letter, tag, body)
        if not steps: manifest.append({'slot': slot, 'skipped': 'no breakdown in LSAT Lab'}); continue
        block = [f"-- {slot} ({c})"]
        if c == 'Unloaded':
            b = bank[slot]
            block.append(
                f"INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)\n"
                f"SELECT s.id, {lit(slot)}, {pt}, {sec}, {qn}, {lit(b['questionType'])}, {lit(b['stimulus'])}, {lit(b['questionStem'])}, {lit(b['correctAnswer'])}, true, {lit(SRC)} "
                f"FROM lr_sections s WHERE s.preptest={pt} AND s.section={sec}\nON CONFLICT DO NOTHING;")
            vals = ','.join(f"({lit(L)},{lit(x['text'])},{lit(tag)},{'true' if L == b['correctAnswer'] else 'false'})"
                            for (L, tag, _), x in zip(notes, answers))
            block.append(f"INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)\n"
                         f"SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES {vals}) v(l,t,g,c) WHERE {where(pt, sec, qn)}\nON CONFLICT DO NOTHING;")
        if c in ('Unloaded', 'Unexplained'):
            block.append(f"INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE {where(pt, sec, qn)} ON CONFLICT DO NOTHING;")
            block.append(steps_sql(pt, sec, qn, steps, ''))
            block.append(notes_sql(pt, sec, qn, [(L, body) for L, _, body in notes]))
            block.append(f"UPDATE lr_questions q SET is_explained=true WHERE {where(pt, sec, qn)};")
        else:  # Notes-only: add the breakdown to the explanation that already carries the notes
            block.append(steps_sql(pt, sec, qn, steps, "AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id)"))
        stmts.append('\n'.join(x for x in block if x))
        manifest.append({'slot': slot, 'coverage': c, 'steps': len(steps), 'notes': sum(1 for n in notes if n[2])})
    os.makedirs(a.out, exist_ok=True)
    batches, cur = [], ''
    for s in stmts:
        if cur and len(cur) + len(s) > a.max_kb * 1024: batches.append(cur); cur = ''
        cur += s + '\n\n'
    if cur: batches.append(cur)
    for i, b in enumerate(batches, 1):
        open(os.path.join(a.out, f'batch-{i:02d}.sql'), 'w', encoding='utf-8').write(b)
    json.dump(manifest, open(os.path.join(a.out, 'manifest.json'), 'w'), indent=1)
    print(len(stmts), 'questions in', len(batches), 'batches;', sum(1 for m in manifest if 'skipped' in m), 'skipped')

if __name__ == '__main__':
    main()
