import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def quote(value):
    if value is None:
        return 'NULL'
    escaped = str(value).replace('\\', '\\\\').replace("'", "''")
    return "E'" + escaped.replace('\r', '\\r').replace('\n', '\\n') + "'"


def values(records):
    return ',\n'.join('(' + ','.join(quote(v) for v in row) + ')' for row in records)


edits = json.loads((ROOT / 'pdf-choice-proposals.json').read_text(encoding='utf-8'))
snapshot = json.loads((ROOT / 'initial-live-snapshot.json').read_text(encoding='utf-8'))
sources = {r['qid']: r for r in snapshot['sources']['structuredContent']['rows']}
assert len(edits) == len({e['row_id'] for e in edits}) == 2
question_values, choice_values, edit_values = [], [], []
for edit in edits:
    assert edit['table'] == 'lr_answer_choices' and edit['column'] == 'choice_text'
    assert md5(edit['old']) == edit['old_md5']
    assert '\r' not in edit['new']
    edit['new_md5'] = md5(edit['new'])
    source = sources[edit['qid']]
    assert source['id'] == edit['question_id'] and source['correct_choice'] == edit['key']
    assert edit['letter'] != edit['key']
    question_values.append([edit['qid'], source['id'], md5(source['stimulus']), md5(source['prompt']), source['correct_choice']])
    assert sorted(c['letter'] for c in source['choices']) == list('ABCDE')
    for choice in source['choices']:
        if choice['id'] == edit['row_id']:
            assert choice['letter'] == edit['letter'] and choice['text'] == edit['old']
        choice_values.append([edit['qid'], choice['id'], choice['letter'], md5(choice['text']), str(choice['letter'] == source['correct_choice']).lower()])
    edit_values.append([edit['qid'], edit['question_id'], edit['row_id'], edit['letter'], edit['old'], edit['old_md5'], edit['new'], edit['new_md5']])

sql = 'with expected_questions(qid,rid,stimulus_md5,prompt_md5,key) as (values\n' + values(question_values) + '),\n'
sql += 'expected_choices(qid,rid,letter,body_md5,correct) as (values\n' + values(choice_values) + '),\n'
sql += 'expected_edits(qid,qid_uuid,rid,letter,old_text,old_md5,new_text,new_md5) as (values\n' + values(edit_values) + '),\n'
sql += """
locked_questions as materialized(select q.* from lr_questions q where q.qid in(select qid from expected_questions) for update),
locked_choices as materialized(select c.* from lr_answer_choices c where c.question_id in(select id from locked_questions) for update),
eligibility as materialized(select
 not exists(select 1 from expected_questions x where (select count(*) from locked_questions q where q.id::text=x.rid and q.qid=x.qid and md5(q.stimulus)=x.stimulus_md5 and md5(q.prompt)=x.prompt_md5 and q.correct_choice::text=x.key)<>1)
 and not exists(select 1 from expected_choices x where (select count(*) from locked_choices c join locked_questions q on q.id=c.question_id where q.qid=x.qid and c.id::text=x.rid and c.letter::text=x.letter and md5(c.choice_text)=x.body_md5 and c.is_correct=x.correct::boolean)<>1)
 and not exists(select 1 from locked_choices c where not exists(select 1 from expected_choices x where x.rid=c.id::text))
 and not exists(select 1 from expected_edits x where (select count(*) from locked_choices c join locked_questions q on q.id=c.question_id where q.qid=x.qid and q.id::text=x.qid_uuid and c.id::text=x.rid and c.letter::text=x.letter and c.choice_text=x.old_text and md5(c.choice_text)=x.old_md5)<>1) eligible)
"""
(ROOT / 'pdf-preflight.sql').write_bytes((sql + 'select eligible from eligibility;\n').encode('utf-8'))
sql += """,
updated as(update lr_answer_choices t set choice_text=e.new_text from expected_edits e,eligibility g
 where g.eligible and t.id=e.rid::uuid and t.question_id=e.qid_uuid::uuid and t.letter::text=e.letter
 and t.choice_text=e.old_text and md5(t.choice_text)=e.old_md5
 and exists(select 1 from locked_questions q where q.id=t.question_id and q.qid=e.qid)
 returning t.id::text rid,md5(t.choice_text) body_md5),
result as(select (select eligible from eligibility) eligible,(select count(*) from updated) updated_rows,
 (select count(*) from updated u join expected_edits e on e.rid=u.rid and e.new_md5=u.body_md5) verified_rows,
 (select jsonb_agg(to_jsonb(u)) from updated u) receipts)
select *,1/(case when (not eligible and updated_rows=0) or (eligible and updated_rows=2 and verified_rows=2) then 1 else 0 end) atomic_assertion from result;
"""
(ROOT / 'pdf-apply-atomic.sql').write_bytes(sql.encode('utf-8'))

for edit in edits:
    next(c for c in choice_values if c[1] == edit['row_id'])[3] = edit['new_md5']
audit = 'with expected_questions(qid,rid,stimulus_md5,prompt_md5,key) as (values\n' + values(question_values) + '),\n'
audit += 'expected_choices(qid,rid,letter,body_md5,correct) as (values\n' + values(choice_values) + '),\n'
audit += 'expected_edits(qid,qid_uuid,rid,letter,old_text,old_md5,new_text,new_md5) as (values\n' + values(edit_values) + '),\n'
audit += """
question_checks as(select x.qid,
 (select count(*) from lr_questions q where q.qid=x.qid and q.id::text=x.rid and md5(q.stimulus)=x.stimulus_md5 and md5(q.prompt)=x.prompt_md5 and q.correct_choice::text=x.key) matches from expected_questions x),
choice_checks as(select x.qid,x.letter,
 (select count(*) from lr_answer_choices c join lr_questions q on q.id=c.question_id where q.qid=x.qid and c.id::text=x.rid and c.letter::text=x.letter and md5(c.choice_text)=x.body_md5 and c.is_correct=x.correct::boolean) matches from expected_choices x),
edit_checks as(select x.qid,x.rid,x.letter,
 (select count(*) from lr_answer_choices c join lr_questions q on q.id=c.question_id where q.qid=x.qid and q.id::text=x.qid_uuid and c.id::text=x.rid and c.letter::text=x.letter and c.choice_text=x.new_text and md5(c.choice_text)=x.new_md5) matches from expected_edits x)
select jsonb_build_object('expected_rows',2,'matching_rows',(select count(*) from edit_checks where matches=1),
 'edit_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from edit_checks c where matches<>1),'[]'::jsonb),
 'question_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from question_checks c where matches<>1),'[]'::jsonb),
 'choice_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from choice_checks c where matches<>1),'[]'::jsonb),
 'extra_choices',(select count(*) from lr_answer_choices c join lr_questions q on q.id=c.question_id where q.qid in(select qid from expected_questions) and not exists(select 1 from expected_choices x where x.rid=c.id::text))) audit;
"""
(ROOT / 'pdf-read-after-audit.sql').write_bytes(audit.encode('utf-8'))
(ROOT / 'pdf-payload-final.json').write_bytes((json.dumps(edits, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
for name in ['pdf-preflight.sql', 'pdf-apply-atomic.sql', 'pdf-read-after-audit.sql']:
    assert b'\r' not in (ROOT / name).read_bytes()
print('Built PDF two-choice atomic apply, preflight and audit; escaped E literals and LF bytes')
