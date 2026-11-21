import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def quote(value):
    if value is None:
        return 'NULL'
    escaped = str(value).replace('\\', '\\\\').replace("'", "''")
    return "E'" + escaped.replace('\r', '\\r').replace('\n', '\\n') + "'"


def values(records):
    return ',\n'.join('(' + ','.join(quote(v) for v in row) + ')' for row in records)


review = json.loads((ROOT / 'reviewer-pt132.json').read_text(encoding='utf-8'))
assert review.get('verdict') == 'APPROVE'
edits = json.loads((ROOT / 'pt132-proposals.json').read_text(encoding='utf-8'))
snapshot = json.loads((ROOT / 'pt132-live-snapshot.json').read_text(encoding='utf-8'))['structuredContent']['rows']
assert len(snapshot) == 1 and len(edits) == 7
source = snapshot[0]
assert source['qid'] == 'PT132-S2-Q3' and source['correct_choice'] == 'B'
assert source['question_type'] == 'Strengthen' and source['style'] == 'single'
by_id = {e['row_id']: e for e in edits}
assert len(by_id) == 7
body_values = []
for kind, key, slot in [('step', 'steps', 'position'), ('note', 'notes', 'letter')]:
    for row in source[key]:
        edit = by_id.get(row['id'])
        assert md5(row['body']) == row['md5']
        if edit:
            assert edit['old'] == row['body'] and edit['old_md5'] == row['md5']
            assert md5(edit['new']) == edit['new_md5']
            assert edit['explanation_id'] == source['explanation_id']
            assert edit[slot] == row[slot]
            assert '\r' not in edit['new']
        body_values.append([kind, row['id'], str(row[slot]), row.get('label'), row['body'], row['md5'], edit['new'] if edit else row['body'], edit['new_md5'] if edit else row['md5'], str(edit is not None).lower()])
assert len(body_values) == 9
choice_values = [[c['id'], c['letter'], md5(c['choice_text']), str(c['is_correct']).lower()] for c in source['choices']]
assert sorted(c[1] for c in choice_values) == list('ABCDE')
question_values = [[source['question_id'], source['qid'], md5(source['stimulus']), md5(source['prompt']), source['correct_choice'], source['question_type'], source['explanation_id'], source['style']]]
sql = 'with question_expected(rid,qid,stimulus_md5,prompt_md5,key,qtype,eid,style) as (values\n' + values(question_values) + '),\n'
sql += 'choice_expected(rid,letter,body_md5,correct) as (values\n' + values(choice_values) + '),\n'
sql += 'body_expected(kind,rid,slot,label,old_text,old_md5,new_text,new_md5,target) as (values\n' + values(body_values) + '),\n'
sql += """
locked_question as materialized(select q.* from lr_questions q where q.qid=E'PT132-S2-Q3' for update),
locked_explanation as materialized(select e.* from lr_explanations e where e.question_id in(select id from locked_question) for update),
locked_choices as materialized(select c.* from lr_answer_choices c where c.question_id in(select id from locked_question) for update),
locked_steps as materialized(select s.* from lr_explanation_steps s where s.explanation_id in(select id from locked_explanation) for update),
locked_notes as materialized(select n.* from lr_explanation_choice_notes n where n.explanation_id in(select id from locked_explanation) for update),
actual_bodies as (
 select 'step'::text kind,s.id::text rid,s.position::text slot,s.label,s.body from locked_steps s
 union all select 'note',n.id::text,n.letter::text,null::text,n.body from locked_notes n),
eligibility as materialized(select
 (select count(*) from locked_question)=1 and (select count(*) from locked_explanation)=1
 and (select count(*) from locked_choices)=5 and (select count(*) from actual_bodies)=9
 and (select count(*) from locked_question q join locked_explanation e on e.question_id=q.id join question_expected x on x.rid=q.id::text where q.qid=x.qid and md5(q.stimulus)=x.stimulus_md5 and md5(q.prompt)=x.prompt_md5 and q.correct_choice::text=x.key and q.question_type=x.qtype and e.id::text=x.eid and e.style=x.style)=1
 and not exists(select 1 from choice_expected x where (select count(*) from locked_choices c where c.id::text=x.rid and c.letter::text=x.letter and md5(c.choice_text)=x.body_md5 and c.is_correct=x.correct::boolean)<>1)
 and not exists(select 1 from body_expected x where (select count(*) from actual_bodies a where a.kind=x.kind and a.rid=x.rid and a.slot=x.slot and (x.label is null or a.label=x.label) and a.body=x.old_text and md5(a.body)=x.old_md5)<>1) eligible)
"""
(ROOT / 'pt132-preflight.sql').write_bytes((sql + 'select eligible from eligibility;\n').encode('utf-8'))
sql += """,
us as(update lr_explanation_steps t set body=x.new_text from body_expected x,question_expected q,eligibility g
 where g.eligible and x.target::boolean and x.kind=E'step' and t.id=x.rid::uuid and t.explanation_id=q.eid::uuid
 and t.position::text=x.slot and t.label=x.label and t.body=x.old_text and md5(t.body)=x.old_md5
 returning t.id::text rid,md5(t.body) body_md5),
un as(update lr_explanation_choice_notes t set body=x.new_text from body_expected x,question_expected q,eligibility g
 where g.eligible and x.target::boolean and x.kind=E'note' and t.id=x.rid::uuid and t.explanation_id=q.eid::uuid
 and t.letter::text=x.slot and t.body=x.old_text and md5(t.body)=x.old_md5
 returning t.id::text rid,md5(t.body) body_md5),
writes as(select * from us union all select * from un),
result as(select (select eligible from eligibility) eligible,(select count(*) from us) updated_steps,(select count(*) from un) updated_notes,
 (select count(*) from writes) updated_rows,(select count(*) from writes w join body_expected x on x.rid=w.rid and x.new_md5=w.body_md5) verified_rows,
 (select jsonb_agg(to_jsonb(w)) from writes w) receipts)
select *,1/(case when (not eligible and updated_rows=0) or (eligible and updated_rows=7 and verified_rows=7 and updated_steps=4 and updated_notes=3) then 1 else 0 end) atomic_assertion from result;
"""
(ROOT / 'pt132-apply-atomic.sql').write_bytes(sql.encode('utf-8'))

audit = 'with question_expected(rid,qid,stimulus_md5,prompt_md5,key,qtype,eid,style) as (values\n' + values(question_values) + '),\n'
audit += 'choice_expected(rid,letter,body_md5,correct) as (values\n' + values(choice_values) + '),\n'
audit += 'body_expected(kind,rid,slot,label,old_text,old_md5,new_text,new_md5,target) as (values\n' + values(body_values) + '),\n'
audit += """
question_check as(select count(*) matches from lr_questions q join question_expected x on q.id::text=x.rid join lr_explanations e on e.question_id=q.id where q.qid=x.qid and md5(q.stimulus)=x.stimulus_md5 and md5(q.prompt)=x.prompt_md5 and q.correct_choice::text=x.key and q.question_type=x.qtype and e.id::text=x.eid and e.style=x.style),
choice_checks as(select x.rid,x.letter,(select count(*) from lr_answer_choices c,question_expected q where c.id::text=x.rid and c.question_id=q.rid::uuid and c.letter::text=x.letter and md5(c.choice_text)=x.body_md5 and c.is_correct=x.correct::boolean) matches from choice_expected x),
actual_bodies as(select 'step'::text kind,s.id::text rid,s.position::text slot,s.label,s.body from lr_explanation_steps s,question_expected q where s.explanation_id=q.eid::uuid
 union all select 'note',n.id::text,n.letter::text,null::text,n.body from lr_explanation_choice_notes n,question_expected q where n.explanation_id=q.eid::uuid),
body_checks as(select x.kind,x.rid,x.slot,x.target,(select count(*) from actual_bodies a where a.kind=x.kind and a.rid=x.rid and a.slot=x.slot and (x.label is null or a.label=x.label) and a.body=x.new_text and md5(a.body)=x.new_md5) matches from body_expected x)
select jsonb_build_object('expected_edited_rows',7,'matching_edited_rows',(select count(*) from body_checks where target::boolean and matches=1),
 'preserved_notes',(select count(*) from body_checks where not target::boolean and matches=1),
 'body_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from body_checks c where matches<>1),'[]'::jsonb),
 'choice_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from choice_checks c where matches<>1),'[]'::jsonb),
 'question_snapshot_matches',(select matches from question_check),
 'explanation_count',(select count(*) from lr_explanations e,question_expected q where e.question_id=q.rid::uuid),
 'choice_count',(select count(*) from lr_answer_choices c,question_expected q where c.question_id=q.rid::uuid),
 'body_count',(select count(*) from actual_bodies)) audit;
"""
(ROOT / 'pt132-read-after-audit.sql').write_bytes(audit.encode('utf-8'))
for name in ['pt132-preflight.sql', 'pt132-apply-atomic.sql', 'pt132-read-after-audit.sql']:
    assert b'\r' not in (ROOT / name).read_bytes()
print('Built approved PT132 seven-body atomic SQL, full source guards, preserved D/E audit, escaped E literals')
