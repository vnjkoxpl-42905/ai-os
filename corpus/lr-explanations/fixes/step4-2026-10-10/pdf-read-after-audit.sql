with expected_questions(qid,rid,stimulus_md5,prompt_md5,key) as (values
(E'PT102-S4-Q2',E'6caf4d41-296d-4280-91a2-bb6213ef9073',E'2f288985bb004609ae8f8702897747cc',E'e42f0982b6b8a25358d0c0eb0eaebf99',E'B'),
(E'PT134-S1-Q12',E'ea6fbe50-50c0-4acf-8e48-1263ba720e2a',E'6f44c5adb015cbda1cc683abb6edf5b8',E'1a1e361558dd1d7237046c300850be6c',E'D')),
expected_choices(qid,rid,letter,body_md5,correct) as (values
(E'PT102-S4-Q2',E'5ce1a0c8-bb73-4d36-903c-767bb60731ce',E'A',E'e80440761dbba8db43a950117b17079e',E'false'),
(E'PT102-S4-Q2',E'd3a85e77-fdf9-4567-b7c6-a6b0833e3996',E'B',E'876be81a64234e6d15c5e1841c277ebf',E'true'),
(E'PT102-S4-Q2',E'4073a63b-1015-469d-a891-27f5756d62ff',E'C',E'8fb66e79d388750bbe1947d7614b389e',E'false'),
(E'PT102-S4-Q2',E'968c03fa-c5ad-4d2a-b139-8cc4563f9ca6',E'D',E'46660dc57d1d3fdc76c4da3507d1484a',E'false'),
(E'PT102-S4-Q2',E'692b2034-a830-4882-9202-cbaaf934f664',E'E',E'bca66754dde1168a4cdc409ca6e8b0f3',E'false'),
(E'PT134-S1-Q12',E'c8ab001a-7c9c-40cc-8f14-e801fe0d76b5',E'A',E'e666b67b05becd4cc8c16a31527378da',E'false'),
(E'PT134-S1-Q12',E'ed1e7656-b5fe-45b7-b041-50a75e641373',E'B',E'e49e70a60e44ea460527b128e1fc590b',E'false'),
(E'PT134-S1-Q12',E'cce72d6d-8eb1-495e-ab0a-c76ffe95c0c7',E'C',E'0733ce801e9e6daf4d9df986a30c2fbd',E'false'),
(E'PT134-S1-Q12',E'613cb0c8-6817-41ef-94fb-6aa705f87736',E'D',E'b1cdc07510782d301ef1198f5a349563',E'true'),
(E'PT134-S1-Q12',E'57611b67-bc3b-4c97-8674-8009b6e761a3',E'E',E'c3c65c57a1838d2030b340c6f252203b',E'false')),
expected_edits(qid,qid_uuid,rid,letter,old_text,old_md5,new_text,new_md5) as (values
(E'PT102-S4-Q2',E'6caf4d41-296d-4280-91a2-bb6213ef9073',E'4073a63b-1015-469d-a891-27f5756d62ff',E'C',E'In order to insure that tax returns are correct, it is necessary to hire professional income-tax advisors to prepare them.',E'e84ec9f1e9b736fdc1b3330f244abdda',E'In order to ensure that tax returns are correct, it is necessary to hire professional income-tax advisors to prepare them.',E'8fb66e79d388750bbe1947d7614b389e'),
(E'PT134-S1-Q12',E'ea6fbe50-50c0-4acf-8e48-1263ba720e2a',E'57611b67-bc3b-4c97-8674-8009b6e761a3',E'E',E'One ought to urge the government only do those things the government is justified in doing.',E'645cd821d5e6a7efd909a243d39dd952',E'One ought to urge the government to do only those things the government is justified in doing.',E'c3c65c57a1838d2030b340c6f252203b')),

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
