import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def rows(value):
    return value.get('structuredContent', value)['rows']


def md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def quote(value):
    if value is None:
        return 'NULL'
    escaped = str(value).replace('\\', '\\\\').replace("'", "''")
    escaped = escaped.replace('\r', '\\r').replace('\n', '\\n')
    return "E'" + escaped + "'"


def values(records):
    return ',\n'.join('(' + ','.join(quote(v) for v in row) + ')' for row in records)


edits = load('payload-approved.json')
assert len(edits) == 16
assert len({(e['table'], e['row_id'], e['column']) for e in edits}) == 16
for edit in edits:
    assert md5(edit['old']) == edit['old_md5']
    assert md5(edit['new']) == edit['new_md5']
    assert '\r' not in edit['new']

sources = {r['qid']: r for r in rows(load('initial-live-snapshot.json')['sources'])}
sources.update({r['qid']: r for r in rows(load('guard-sources-live.json'))})
question_values, choice_values = [], []
for qid in sorted({e['qid'] for e in edits}):
    source = sources[qid]
    question_values.append([qid, source['id'], md5(source['stimulus']), md5(source['prompt']), source['correct_choice']])
    assert sorted(c['letter'] for c in source['choices']) == list('ABCDE')
    for choice in source['choices']:
        choice_values.append([qid, choice['id'], choice['letter'], md5(choice['text']), str(choice['letter'] == source['correct_choice']).lower()])

edit_values = []
for edit in edits:
    edit_values.append([edit['qid'], edit['table'], edit['column'], edit['row_id'], edit.get('explanation_id'), str(edit.get('position', edit.get('letter', ''))), edit.get('label'), edit['old'], edit['old_md5'], edit['new'], edit['new_md5']])

standard = next(r for r in rows(load('q157-styles-live.json')) if r['style'] == 'standard')['notes_d'][0]
sql = 'with expected_questions(qid,rid,stimulus_md5,prompt_md5,key) as (values\n' + values(question_values) + '),\n'
sql += 'expected_choices(qid,rid,letter,body_md5,correct) as (values\n' + values(choice_values) + '),\n'
sql += 'expected_edits(qid,tbl,col,rid,eid,slot,label,old_text,old_md5,new_text,new_md5) as (values\n' + values(edit_values) + '),\n'
sql += """
locked_questions as materialized(select t.* from lr_questions t where t.qid in(select qid from expected_questions) for update),
locked_choices as materialized(select t.* from lr_answer_choices t where t.question_id in(select id from locked_questions) for update),
locked_explanations as materialized(select t.* from lr_explanations t where t.question_id in(select id from locked_questions) for update),
locked_steps as materialized(select t.* from lr_explanation_steps t where t.id::text in(select rid from expected_edits where tbl='lr_explanation_steps') for update),
locked_notes as materialized(select t.* from lr_explanation_choice_notes t where t.id::text in(select rid from expected_edits where tbl='lr_explanation_choice_notes') or t.id::text=STANDARD_ID for update),
actual as (
 select q.qid,'lr_questions'::text tbl,'stimulus'::text col,q.id::text rid,null::text eid,''::text slot,null::text label,q.stimulus body from locked_questions q
 union all select q.qid,'lr_answer_choices','tag',c.id::text,null,c.letter::text,null,c.tag from locked_choices c join locked_questions q on q.id=c.question_id
 union all select q.qid,'lr_answer_choices','choice_text',c.id::text,null,c.letter::text,null,c.choice_text from locked_choices c join locked_questions q on q.id=c.question_id
 union all select q.qid,'lr_explanation_steps','body',s.id::text,e.id::text,s.position::text,s.label,s.body from locked_steps s join locked_explanations e on e.id=s.explanation_id join locked_questions q on q.id=e.question_id
 union all select q.qid,'lr_explanation_choice_notes','body',n.id::text,e.id::text,n.letter::text,null,n.body from locked_notes n join locked_explanations e on e.id=n.explanation_id join locked_questions q on q.id=e.question_id),
eligibility as materialized(select
 not exists(select 1 from expected_questions x where (select count(*) from locked_questions t where t.id::text=x.rid and t.qid=x.qid and md5(t.stimulus)=x.stimulus_md5 and md5(t.prompt)=x.prompt_md5 and t.correct_choice::text=x.key)<>1)
 and not exists(select 1 from expected_choices x where (select count(*) from locked_choices c join locked_questions q on q.id=c.question_id where q.qid=x.qid and c.id::text=x.rid and c.letter::text=x.letter and md5(c.choice_text)=x.body_md5 and c.is_correct=x.correct::boolean)<>1)
 and not exists(select 1 from locked_choices c join locked_questions q on q.id=c.question_id where not exists(select 1 from expected_choices x where x.qid=q.qid and x.rid=c.id::text))
 and not exists(select 1 from expected_edits e where (select count(*) from actual a where a.qid=e.qid and a.tbl=e.tbl and a.col=e.col and a.rid=e.rid and (e.eid is null or a.eid=e.eid) and a.slot=e.slot and (e.label is null or a.label=e.label) and a.body=e.old_text and md5(a.body)=e.old_md5)<>1)
 and (select count(*) from locked_notes n where n.id::text=STANDARD_ID and md5(n.body)=STANDARD_MD5)=1 eligible)
""".replace('STANDARD_ID', quote(standard['id'])).replace('STANDARD_MD5', quote(standard['md5']))
(ROOT / 'preflight.sql').write_bytes((sql + 'select eligible from eligibility;\n').encode('utf-8'))

updates = []
for i, edit in enumerate(edits):
    if edit['table'] == 'lr_questions':
        ownership = 't.qid=' + quote(edit['qid'])
    elif edit['table'] == 'lr_answer_choices':
        ownership = 'exists(select 1 from locked_questions q where q.id=t.question_id and q.qid=' + quote(edit['qid']) + ')'
    else:
        ownership = 't.explanation_id=' + quote(edit['explanation_id']) + '::uuid and exists(select 1 from locked_explanations x join locked_questions q on q.id=x.question_id where x.id=t.explanation_id and q.qid=' + quote(edit['qid']) + ')'
    if edit['table'] == 'lr_explanation_steps':
        ownership += ' and t.position=' + str(edit['position']) + ' and t.label=' + quote(edit['label'])
    if edit['table'] in ('lr_answer_choices', 'lr_explanation_choice_notes'):
        ownership += ' and t.letter::text=' + quote(edit['letter'])
    updates.append('u' + str(i) + ' as (update ' + edit['table'] + ' t set ' + edit['column'] + '=' + quote(edit['new']) + ' from eligibility g where g.eligible and t.id=' + quote(edit['row_id']) + '::uuid and ' + ownership + ' and t.' + edit['column'] + '=' + quote(edit['old']) + ' and md5(t.' + edit['column'] + ')=' + quote(edit['old_md5']) + ' returning t.id::text rid,' + quote(edit['table']) + '::text tbl,md5(t.' + edit['column'] + ') body_md5)')
sql += ',' + ',\n'.join(updates)
sql += ',writes as (' + ' union all '.join('select * from u' + str(i) for i in range(len(edits))) + '),'
sql += """
result as(select (select eligible from eligibility) eligible,(select count(*) from writes) updated_rows,
 (select count(*) from writes w join expected_edits e on e.rid=w.rid and e.tbl=w.tbl and e.new_md5=w.body_md5) verified_rows,
 (select jsonb_agg(to_jsonb(w)) from writes w) receipts)
select *,1/(case when (not eligible and updated_rows=0) or (eligible and updated_rows=16 and verified_rows=16) then 1 else 0 end) atomic_assertion from result;
"""
(ROOT / 'apply-atomic.sql').write_bytes(sql.encode('utf-8'))

new_questions = [row.copy() for row in question_values]
new_choices = [row.copy() for row in choice_values]
for edit in edits:
    if edit['table'] == 'lr_questions':
        next(row for row in new_questions if row[1] == edit['row_id'])[2] = edit['new_md5']
    if edit['table'] == 'lr_answer_choices' and edit['column'] == 'choice_text':
        next(row for row in new_choices if row[1] == edit['row_id'])[3] = edit['new_md5']

audit = 'with expected_questions(qid,rid,stimulus_md5,prompt_md5,key) as (values\n' + values(new_questions) + '),\n'
audit += 'expected_choices(qid,rid,letter,body_md5,correct) as (values\n' + values(new_choices) + '),\n'
audit += 'expected_edits(qid,tbl,col,rid,eid,slot,label,old_text,old_md5,new_text,new_md5) as (values\n' + values(edit_values) + '),\n'
audit += """
actual as (
 select q.qid,'lr_questions'::text tbl,'stimulus'::text col,q.id::text rid,null::text eid,''::text slot,null::text label,q.stimulus body from lr_questions q where q.qid in(select qid from expected_questions)
 union all select q.qid,'lr_answer_choices','tag',c.id::text,null,c.letter::text,null,c.tag from lr_answer_choices c join lr_questions q on q.id=c.question_id where c.id::text in(select rid from expected_edits)
 union all select q.qid,'lr_answer_choices','choice_text',c.id::text,null,c.letter::text,null,c.choice_text from lr_answer_choices c join lr_questions q on q.id=c.question_id where c.id::text in(select rid from expected_edits)
 union all select q.qid,'lr_explanation_steps','body',s.id::text,e.id::text,s.position::text,s.label,s.body from lr_explanation_steps s join lr_explanations e on e.id=s.explanation_id join lr_questions q on q.id=e.question_id where s.id::text in(select rid from expected_edits)
 union all select q.qid,'lr_explanation_choice_notes','body',n.id::text,e.id::text,n.letter::text,null,n.body from lr_explanation_choice_notes n join lr_explanations e on e.id=n.explanation_id join lr_questions q on q.id=e.question_id where n.id::text in(select rid from expected_edits)),
checked as (select e.qid,e.tbl,e.col,e.rid,
 (select count(*) from actual a where a.qid=e.qid and a.tbl=e.tbl and a.col=e.col and a.rid=e.rid and (e.eid is null or a.eid=e.eid) and a.slot=e.slot and (e.label is null or a.label=e.label) and a.body=e.new_text and md5(a.body)=e.new_md5) matches from expected_edits e),
question_checks as (select x.qid,
 (select count(*) from lr_questions t where t.id::text=x.rid and t.qid=x.qid and md5(t.stimulus)=x.stimulus_md5 and md5(t.prompt)=x.prompt_md5 and t.correct_choice::text=x.key) matches from expected_questions x),
choice_checks as (select x.qid,x.letter,
 (select count(*) from lr_answer_choices c join lr_questions q on q.id=c.question_id where q.qid=x.qid and c.id::text=x.rid and c.letter::text=x.letter and md5(c.choice_text)=x.body_md5 and c.is_correct=x.correct::boolean) matches from expected_choices x)
select jsonb_build_object('expected_rows',16,'matching_rows',(select count(*) from checked where matches=1),
 'mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from checked c where matches<>1),'[]'::jsonb),
 'question_snapshot_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from question_checks c where matches<>1),'[]'::jsonb),
 'choice_snapshot_mismatches',coalesce((select jsonb_agg(to_jsonb(c)) from choice_checks c where matches<>1),'[]'::jsonb),
 'extra_choice_rows',(select count(*) from lr_answer_choices c join lr_questions q on q.id=c.question_id where q.qid in(select qid from expected_questions) and not exists(select 1 from expected_choices x where x.rid=c.id::text)),
 'standard_preserved',(select count(*) from lr_explanation_choice_notes n join lr_explanations e on e.id=n.explanation_id join lr_questions q on q.id=e.question_id where n.id::text=STANDARD_ID and md5(n.body)=STANDARD_MD5 and q.qid=E'PT157-S3-Q25' and e.style=E'standard')) audit;
""".replace('STANDARD_ID', quote(standard['id'])).replace('STANDARD_MD5', quote(standard['md5']))
(ROOT / 'read-after-audit.sql').write_bytes(audit.encode('utf-8'))
assert all(b'\r' not in (ROOT / name).read_bytes() for name in ['apply-atomic.sql', 'preflight.sql', 'read-after-audit.sql'])
print('Built 16-edit atomic SQL, preflight and read-after audit; content newlines escaped in E literals')
