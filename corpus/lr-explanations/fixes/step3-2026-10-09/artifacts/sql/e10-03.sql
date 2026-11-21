insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('cbdecbe8-ae3b-4bf8-8309-586d3c924c8c'::uuid,1,'Evaluate','Both sentences are conditionals, and they share one idea: the increase in rush-hour traffic flow. When two rules share a term, try to chain them.

The increase is the result in the first rule and the trigger in the second:
no investment → no increase in rush-hour flow → predicament not resolved

Read it forward: without the computer modeling investment, there''s no increase, and without the increase, the predicament stays unresolved. Or read the contrapositive: resolving the predicament required the increase, and the increase required the investment.

Each link is a requirement. The investment was needed; nothing says it was enough. So the safe inferences are about what could not have happened without something, not about what was guaranteed to happen.'),
('cbdecbe8-ae3b-4bf8-8309-586d3c924c8c'::uuid,2,'Goal','Look for the two ends of the chain joined together. Something like: if the city had not invested in computer modeling technology, the financial predicament would not have been resolved. The contrapositive version (resolving the predicament required the investment) would work just as well.'),
('ac2194b1-6d03-4995-b8f9-556aa1f12fa4'::uuid,1,'Evaluate','Each sentence picks up where the last one ended: sewage leads to overnutrified water, overnutrified water leads to algae, and algae can lead to a fish kill. When causes and effects line up end to end like this, connect the first cause to the last effect.

Watch the word "sometimes" on the last link. The algae don''t always feed toxic microorganisms. So the chain doesn''t prove that sewage always kills the fish. It proves that it can.'),
('ac2194b1-6d03-4995-b8f9-556aa1f12fa4'::uuid,2,'Goal','Look for a softly worded answer that joins the start of the chain to the end: overnutrifying an estuary with sewage can lead to most of its fish dying. An answer that says this "will" happen goes past the "sometimes".'),
('ef68a7e2-3ce5-47c5-9918-a96762181a53'::uuid,1,'Evaluate','We have one rule and one fact. The rule works on a variety''s suitability. The fact is about one variety: some nurseries call every Stark Sweet Melody tree "miniature."

Can we fire the rule? Only if we know whether Stark Sweet Melody is suitable for a tub or pot, and we''re never told. So we can''t say anyone is mislabeling outright.

What we can do is put the inference in conditional form. Suppose Stark Sweet Melody is not suitable. Then none of its trees can be correctly labeled "miniature." But some nurseries label them "miniature." So those nurseries are mislabeling.

Also notice what the rule doesn''t give us. Suitability is required for a correct "miniature" label, but it isn''t enough. Even a suitable variety might not be miniature.'),
('ef68a7e2-3ce5-47c5-9918-a96762181a53'::uuid,2,'Goal','Look for an answer that keeps the unknown as a condition: "If Stark Sweet Melody is not suitable for a tub or pot, then some nurseries are mislabeling it." It might be phrased with "unless," which means "if not."'),
('4e360875-0755-4a5a-850a-ef5d076a133c'::uuid,2,'Goal','Look for an answer built on the "at most one exception" idea: if there are two or more new courses, at least one has a prerequisite. Another safe version: any new course that didn''t come from Dean Wilson''s proposal has a prerequisite. Reject answers that assume a proposal gets approved, or that stretch the prerequisite rule past upper-level courses.'),
('92043ea4-ffbd-42ba-b249-6faaf3768e45'::uuid,2,'Goal','Look for the fix stated as a capability: thin television sets can now have screens that are both large and bright. The "However" and "Moreover" tell us the report is building toward exactly that. Reject answers about what people want, what''s wrong with the new screens, or how thickness changes brightness.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;