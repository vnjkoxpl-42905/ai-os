with expected(qid,kind,eid,slot,rid,new_md5,old_md5,new_label,old_label) as (values
('PT158-S4-Q22','step','bc99369b-8d3d-451e-9228-15efe84d9372','0','b297870f-c027-4cf8-9986-89f93ab41452','316838a5754ec0971575d78450cbc5db','f75b2a78ab1e07e8cc15ff4a9fefcd1b','Conclusion','Conclusion'),
('PT158-S4-Q22','step','bc99369b-8d3d-451e-9228-15efe84d9372','1','99121926-d49a-415e-a029-61f6329177ef','7e8e52c93db0fa7bb9eee0567d10d28b','c40c3da66fcd9ab270095c4d082bde2e','Evidence','Evidence'),
('PT158-S4-Q22','step','bc99369b-8d3d-451e-9228-15efe84d9372','2','92039a68-223d-42f3-9bd9-b5a531bf5340','c7e5cedf5bdf158421ceaf0e324d9cda','b8fd0f832774cb291edef382e9b6527a','Evaluate','Evaluate'),
('PT158-S4-Q22','step','bc99369b-8d3d-451e-9228-15efe84d9372','3','7d3ea25e-dd71-4ada-937c-ae04e2252a50','e4e923dd4d3df36c25c5f79d27d642bc','6989e6cd9e24ea1fb8402f28a2d73a12','Goal','Goal'),
('PT158-S4-Q22','note','bc99369b-8d3d-451e-9228-15efe84d9372','A','3f5c68c4-8737-490f-b41b-1ca69027a118','9da74a3631e9a303fc4cdbc2750de8d1','330acba2ebb0026ac2fedbd196b159b8',NULL,NULL),
('PT158-S4-Q22','note','bc99369b-8d3d-451e-9228-15efe84d9372','B','01678eae-d0c8-4317-8851-790c8b1813a1','e735db93e60238591faf11365600f8e1','8937dce02c5175a15c8df8778147276a',NULL,NULL),
('PT158-S4-Q22','note','bc99369b-8d3d-451e-9228-15efe84d9372','C','2ab8be91-6574-4c5d-b0dc-d80bbe02a89e','e6256f7421d9fabe829d97903f0562eb','2248ec965f8296519e03e95a18623099',NULL,NULL),
('PT158-S4-Q22','note','bc99369b-8d3d-451e-9228-15efe84d9372','D','28029a1b-b551-46c4-93ea-97824d1d5775','e46d66965a73d1a64f576064761e85d6','03a4e6b88539482818e6bf001ad355e7',NULL,NULL),
('PT158-S4-Q22','note','bc99369b-8d3d-451e-9228-15efe84d9372','E','6ed8926a-96f2-4261-831b-8f6ed4b064c7','828c3868082534e3ae04df7ad35d7ca3','0e1454af91135c77ef9d9f2b485ae253',NULL,NULL),
('PT158-S4-Q24','step','571e3119-bcb6-4ccd-b487-3f2b10167cc0','0','168cd86b-f30d-4918-b872-9377446e405c','1be0859891be628719afad3615e4b7e9','1be0859891be628719afad3615e4b7e9','Conclusion','Conclusion'),
('PT158-S4-Q24','step','571e3119-bcb6-4ccd-b487-3f2b10167cc0','1','c6f428a8-8d04-4dbf-b508-bb7e55130399','81ca5a272b99d34b1815d7d63f9d3204','81ca5a272b99d34b1815d7d63f9d3204','Evidence','Evidence'),
('PT158-S4-Q24','step','571e3119-bcb6-4ccd-b487-3f2b10167cc0','2','d1c38a19-c55c-4bbc-99be-1c6bb16adb74','c614cbced4e73699976320d904814ac0','73bc0ca4f66db6db2dd7ea9ccdfe67d3','Evaluate','Evaluate'),
('PT158-S4-Q24','step','571e3119-bcb6-4ccd-b487-3f2b10167cc0','3','28c5b825-0584-4296-ba19-94bc4225d797','2f97665e6f4213d68057d33eee4e3085','7666df51fff25e6864f078fbf63a1115','Goal','Goal'),
('PT158-S4-Q24','note','571e3119-bcb6-4ccd-b487-3f2b10167cc0','A','3ae82b06-98b5-4ef7-a819-629993fad1a7','b17620d7b23a7d058e2ca9f49e0513b4','5af648f434b6219795f28991e1a31c2c',NULL,NULL),
('PT158-S4-Q24','note','571e3119-bcb6-4ccd-b487-3f2b10167cc0','B','3ca3bfff-6aa0-45d5-b8e4-5dc7bf7e6f7c','1110a5df9a0d8699a141aac21f90449e','d2ebffa10d06ff747295f550270fd9ac',NULL,NULL),
('PT158-S4-Q24','note','571e3119-bcb6-4ccd-b487-3f2b10167cc0','C','bf754625-bf1f-488f-afde-ff800c3dcbac','59b7997437862f354db7563c617fc56b','478ceedf22c11020fa1af3cf6f47b1a3',NULL,NULL),
('PT158-S4-Q24','note','571e3119-bcb6-4ccd-b487-3f2b10167cc0','D','a289da90-b50c-4d22-b9cf-e6c42994d2b3','2ac38f6325aeb2a50c537c1e56fda49f','d5d9767edd4731efc07bd761f0d3d35d',NULL,NULL),
('PT158-S4-Q24','note','571e3119-bcb6-4ccd-b487-3f2b10167cc0','E','88958a04-d640-4eb8-8590-63e0d3cf36b2','a3110b7dad82244654f99778ef073c3f','898c1d9690b391f1bf5fafe53d2a759c',NULL,NULL)), actual as (
 select 'step'::text kind, explanation_id::text eid, position::text slot,id::text rid,md5(body) body_md5,coalesce(label,'') label from lr_explanation_steps
 union all select 'note',explanation_id::text,letter::text,id::text,md5(body),null::text from lr_explanation_choice_notes
), checked as (
 select e.*,count(a.rid)::integer matches,
 count(a.rid) filter(where a.body_md5=e.new_md5 and (e.rid is null or a.rid=e.rid) and (e.kind='note' or a.label=e.new_label))::integer final_matches,
 count(a.rid) filter(where a.body_md5=e.old_md5 and (e.rid is null or a.rid=e.rid) and (e.kind='note' or a.label=e.old_label))::integer old_matches,
 jsonb_agg(jsonb_build_object('rid',a.rid,'md5',a.body_md5,'label',a.label)) filter(where a.rid is not null) actual
 from expected e left join actual a on a.kind=e.kind and a.eid=e.eid and a.slot=e.slot
 group by e.qid,e.kind,e.eid,e.slot,e.rid,e.new_md5,e.old_md5,e.new_label,e.old_label
), extras as (
 select a.kind,a.eid,a.slot,count(*) count from actual a
 where a.eid in (select distinct eid from expected) and not exists(select 1 from expected e where e.eid=a.eid and e.kind=a.kind and e.slot=a.slot)
 group by a.kind,a.eid,a.slot
)
select jsonb_build_object('batch','e24','expected_rows',(select count(*) from checked),'final_rows',(select count(*) from checked where matches=1 and final_matches=1),'old_rows',(select count(*) from checked where matches=1 and old_matches=1),'missing',(select count(*) from checked where matches=0),'duplicate_slots',(select count(*) from checked where matches>1),'mismatches',coalesce((select jsonb_agg(jsonb_build_object('qid',qid,'kind',kind,'slot',slot,'expected_id',rid,'expected_md5',new_md5,'matches',matches,'old_matches',old_matches,'actual',actual)) from checked where matches<>1 or final_matches<>1),'[]'::jsonb),'extra_slots',coalesce((select jsonb_agg(to_jsonb(extras)) from extras),'[]'::jsonb)) audit;
