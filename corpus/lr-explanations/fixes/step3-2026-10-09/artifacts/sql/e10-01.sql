update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('62e9e508-cfd4-498b-a0cc-3bea52e84382'::uuid,'cbb56c31fa5f623abd7a7180d8e2bd25','1. The increase in rush-hour traffic flow "would not have occurred had the city not invested in computer modeling technology."
no investment → no increase in rush-hour flow
increase in rush-hour flow → investment (contrapositive)

2. The financial predicament "would not have been resolved if the traffic flow across the bridge during rush hour had not been increased."
no increase in rush-hour flow → predicament not resolved
predicament resolved → increase in rush-hour flow (contrapositive)','Explanation','Statements'),
('5412f9a3-8035-4b00-b2bf-04a8aa800dbf'::uuid,'73a94846e5b91c6f0b06e32df4b8eb6d','Coastal estuaries are easily polluted by nutrient-rich sewage.

When that pollution overnutrifies the water, algae proliferate.
sewage overnutrifies water → algae proliferate

The abundant algae "sometimes" feed microorganisms that are toxic to fish, killing most of the fish.
abundant algae → (sometimes) toxic microorganisms thrive → most fish die','Given','Given'),
('07a04192-5610-42df-931d-1efaaee6898d'::uuid,'37301ab4471d0431449e9cc80739fbc5','Some nurseries label any Stark Sweet Melody nectarine trees "miniature." Others do not.

Rule: if a variety of fruit tree is not suitable for growing in a tub or a pot, no tree of that variety can be correctly labeled miniature.
variety not suitable for tub or pot → no tree of it is correctly labeled "miniature"
correctly labeled "miniature" → variety suitable for tub or pot (contrapositive)','Explanation','Statements'),
('50a4f069-39d5-4963-bca5-2e241e4ba078'::uuid,'a3300b0adc4111bf7655e60818df56ea','  - One should not do anything that has the potential to produce serious harm to one''s society.
  - The public actions, or inactions, of celebrities and of people who are widely respected are widely emulated.
  - Some celebrities do not vote.
  - Serious harm befalls a society in which many people refrain from voting.','Given','Given'),
('d46ae81c-0089-4b1b-a04c-f4f4110fc495'::uuid,'55b9bc7236552fa3bb49cc5e58a55630','Look for ideas that show up in more than one statement and chain them.

Public inactions of widely respected people are widely emulated. Not voting is an inaction. So if a widely respected person publicly refrains from voting, many people may refrain too. Many people refraining brings serious harm. That gives us a chain:
widely respected person publicly doesn''t vote → many people don''t vote → serious harm to society

Now the first statement applies. Publicly not voting has the potential to produce serious harm, so one should not do it.

Notice what the chain does not need: the third statement. "Some celebrities do not vote" doesn''t say they do it publicly, so it doesn''t fire anything. It''s there to tempt you into an answer about celebrities who don''t vote.','Evaluate','Evaluate'),
('7c4b65b6-6626-4bf5-abff-c35b8341a81b'::uuid,'5aa2d57e51b78471b701639f9328937e','Look for a "should not" principle about people whose actions are emulated: widely respected people (or celebrities) should not publicly refrain from voting. Be wary of answers that tell society what to require, tell people whom to respect or emulate, or tell anyone they must vote. The stimulus only says what one should not do.','Goal','Goal'),
('6909eea9-13b1-407d-acb8-597c73c737a2'::uuid,'7fcbb73330f980b9804d42d596775020','1. No new course will be approved unless the committee or Dean Wilson has already received a proposal for it.
new course approved → proposal received by committee or by Dean Wilson

2. Dean Wilson has received only one new course proposal.

3. All new course proposals the committee has received are for upper-level courses.
committee proposal → upper-level

4. Beginning next year, all upper-level courses will have prerequisites.
upper-level → prerequisite','Given','Given'),
('e5034862-ccee-462e-a917-35aeaee2425b'::uuid,'419ee3cbbc71701b7ae919f9d518210b','Statements 3 and 4 chain together:
committee proposal → upper-level → prerequisite

Now combine that with statement 1. Every new course next year came from one of two places. If it came from the committee, it has a prerequisite. If it came from Dean Wilson, we know nothing about it, but statement 2 says the dean has only one proposal.

So the dean''s pile can supply at most one new course. Every other new course must come from the committee, and so must have a prerequisite. Put plainly: at most one new course next year can lack a prerequisite.

Also notice what''s missing. Receiving a proposal is required for approval, but nothing says any proposal will be approved. And the prerequisite rule covers upper-level courses only, not every course.','Evaluate','Evaluate'),
('0d45798d-2be6-440a-9948-b9e95fcd763f'::uuid,'d2f36bdcd4e947363f471b1562dfe931','"Moral excellence can be achieved only by repeatedly overcoming inclinations to do the wrong thing."
moral excellence → repeatedly overcame inclinations to do wrong

Overcoming these inclinations is often difficult, even for a morally virtuous person.

"the only way to become a morally virtuous person is through the achievement of moral excellence."
morally virtuous → moral excellence','Given','Given'),
('0646e18d-1d86-4c60-ae80-2d65c5eeb4ef'::uuid,'46fbf1703ec3adc5ff8aa7d39450ebfb','Two requirement rules share a term: moral excellence. It''s the result of the virtue rule and the trigger of the excellence rule, so they chain:
morally virtuous → moral excellence → repeatedly overcame inclinations to do wrong

So every morally virtuous person has repeatedly overcome inclinations to do the wrong thing. Now take one more small step. You can''t overcome an inclination you never had. So every morally virtuous person has had inclinations to do wrong.

The arrows only run one way. Moral excellence is required for virtue, not enough for it. Overcoming inclinations is required for excellence, not enough for it.','Evaluate','Evaluate'),
('8c07262c-c721-42c3-81b4-9d63b4592b86'::uuid,'d85f7e04da740717b27a19e60bd6d774','Expect the end of the chain, said about virtuous people: every morally virtuous person has repeatedly overcome, and so has had, inclinations to do wrong. Watch for answers that run an arrow backward or negate both sides.','Goal','Goal'),
('8ff6050d-272c-4107-b9f4-b1ad274ce116'::uuid,'a61efa8edac5459be071ce3cacf84857','The report sets up a problem and then a fix. The problem: in a set a few inches thick, a noncompound screen gets dimmer as it gets larger, so thin, large and bright don''t go together. The fix: compound screens are made of small, bright tiles, and you can add as many tiles as you want without losing brightness or adding thickness.

Put those together. Keep adding tiles and the screen gets as large as you like, stays bright, and the set stays a few inches thick. So thin sets with screens that are both bright and very large are now possible.','Evaluate','Evaluate'),
('994af839-0cfb-4afe-a4f6-d898ea77c2e1'::uuid,'eaa1cd8ac1d19c4bf4b91abd3a5f8700','Rule (if):
based on info from a reliable source → reasonable to maintain

Fact (some): some beliefs are
1. based on info from a reliable source, and
2. not self-evident, and
3. not grounded in observable evidence','Statements','Statements'),
('7ffd282a-12bf-4803-81b1-20487a2d66ae'::uuid,'06779a368c97fa69a334d3782d4e40b7','We have one conditional and one fact. With a conditional on Must Be True, ask two questions:
1. Is there another conditional to chain it with?
2. Does any fact trigger it (or its contrapositive)?

There''s no second conditional, so #1 is out. For #2, the "some" beliefs in the second sentence are based on information from a reliable source. That triggers the rule, so those beliefs are reasonable to maintain.

Now that group has four traits at once: reliable source, reasonable, not self-evident, and not grounded in observable evidence. The question is most likely testing whether we can attach "reasonable" to the other traits in that group.

Two limits to keep in mind. A "some" fact is about one group, so it can''t become a rule about all beliefs. And the rule only says a reliable source is enough for reasonableness, not that it''s the only route.','Evaluate','Evaluate'),
('99fa7637-eddf-47b6-bba2-a652c22a630f'::uuid,'15cd0176cdd4d465c919e6e9601f5efe','Look for a "some" statement that pairs reasonable with one or both of the other traits: some reasonable beliefs are not self-evident, some reasonable beliefs are not grounded in observable evidence, or some reasonable beliefs are neither.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;