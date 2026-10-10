update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('b13f2d7f-892c-438a-a4db-4433f79e009e'::uuid,'be6d8383a6695a6e0ad133cc9202a95a','Go claim by claim through Paula''s argument and ask of each one: does Ashley push back?

1. Earthlike planets are common, so there probably are intelligent beings on other planets. Ashley never touches this. Calling the search a waste doesn''t mean nothing is out there. It can just mean we''re listening for the wrong signal.

2. Alien scientists would understand math and physics the way we do, so they would inevitably develop technologies such as radio communication. Ashley rejects this directly. Our science, mathematics, and technology are "unique outgrowths" of our physiology, cognitive makeup, and environment. Different beings, different outgrowths. The legal and political systems comparison is there to make Paula''s "inevitably" sound as odd as expecting aliens to have our courts and juries.

3. We can expect our radio telescopes to detect signs of such beings. Ashley rejects this too: the search is "a waste of time and money."

So the friction sits in claims 2 and 3, and they share one core question: would intelligent aliens end up with radio? Paula says inevitably. Ashley says there''s no reason to expect it.

Underneath, Paula treats math and physics as something any intelligent mind would arrive at. Ashley treats them as a product of being human.','Evaluate','Evaluate'),
('d03bb8ee-aa3f-48a6-bbe2-12ed75b7372a'::uuid,'725626240c027adec99de8fb27a5d15d','Look for an answer about whether intelligent aliens would have developed radio communication, or, nearly the same thing, whether radio telescopes are a sensible way to look for them. Paula has to land on yes and Ashley on no.

Be careful with answers about intelligent life alone. Ashley never says whether aliens exist, so an answer about existence gives us an Agree position from Paula and nothing from Ashley.','Goal','Goal'),
('48e638a9-3a7e-490f-b2af-8569e906daf9'::uuid,'4bb6ba9ee22d1a012843172a1e94151f','Archaeologists can study the artifacts left by ancient cultures to determine whether they were nomadic or sedentary.

Does Kendall push back on this? Yes, at least partly. Kendall says what artifacts a people make is determined largely by the materials available to them. If materials drive what gets made, the artifacts may tell us more about the local supply of stone and wood than about whether the people moved around. That makes the artifact test much less reliable.','Robin''s 1st Claim','Robin''s 1st Claim'),
('24ec064d-ffc5-4f19-b19f-d7442d3655c0'::uuid,'3985510ed1ddcfe30e9c3382a7fd8025','If artifacts were made to last, rather than to be quickly discarded, then the culture was likely sedentary.

Does Kendall deny this exact claim? Not cleanly. Kendall''s point lands hardest on the flip side. Picture a settled village with nothing around it but reeds and soft wood. Everything it makes falls apart within a few years. Robin''s test would call that village nomadic, and Kendall''s point explains why that would be a mistake: the flimsy artifacts reflect the materials, not a life on the move.

So Kendall might accept "made to last, so probably sedentary" while rejecting "not durable, so probably nomadic."','Robin''s 2nd Claim','Robin''s 2nd Claim'),
('eb15399b-1322-4d8c-88f7-888ae61f1933'::uuid,'189655fed1636dee9a9a7abcbb23ae0a','Robin is committed to more than the durable half. The first claim says artifacts can determine whether a culture was nomadic or sedentary, so Robin''s test has to sort both ways: lasting artifacts point to sedentary, throwaway artifacts point to nomadic.

Kendall''s response targets that second half. Look for an answer about whether non-durable artifacts give us good reason to call a culture nomadic. Robin says yes. Kendall says no, because the available materials may explain the flimsiness.','Goal','Goal'),
('dfb3414b-7299-447e-929f-c89a5f9aa85b'::uuid,'a0cce756d582481a87367b7d748ab388','A few months into a high-salt diet, 75% of the rats in the colony had high or extremely high blood pressure; only 25% had normal blood pressure.','Evidence','Evidence'),
('ebb4113c-41f0-41e3-8cd2-3520cf6cbd26'::uuid,'1ce47db39da0058b2ccb3f0e1d489af6','The study has a result but no starting point. It measured blood pressure a few months into the diet, and that''s all we get.

So ask: what if most of these rats already had high blood pressure before the study began? Then 75% at the end tells us nothing about salt. The diet didn''t move the numbers. It just sat on top of them.

Now flip it. If almost every rat started out normal and 75% ended up high, the diet looks much more like the culprit.

Whenever an argument draws a link from an after-measurement alone, the missing piece is the before-measurement, or a comparison group that never got the treatment.','Evaluate','Evaluate'),
('2e41c9fa-3934-4afd-8862-c33846c4a63a'::uuid,'ca830a23f2d74e1ba57c9e2ee01f8d43','Look for a question about the rats'' blood pressure before the diet started.

Test each choice by imagining two different answers to it. If one answer would help the conclusion and the other would hurt it, the question is relevant. If every possible answer leaves the conclusion where it was, move on.','Goal','Goal'),
('bfbb2fa9-f17a-41dd-ae12-f53af0c9af03'::uuid,'28c0a6de536d01b1be5a3adc5d5c5b42','If we''re the other lawyer and we''re arguing,
*there IS some reason not to try this herb juice*
what would we say?
  We could start with, "Wait. Some doctors said the herbs are potentially harmful? That sounds like a reason not to try it."
  And the herbalist will say, "Oh, don''t listen to them. Doctors don''t want herbs to work. They want a monopoly over medical therapies, so they talk down anything that isn''t theirs."
  We need a response. We could say, "Sure, doctors might have a motive. But a motive doesn''t make the warning false. What if the herbs actually are harmful? Do you have evidence they''re safe?"
  If we know our Famous Flaws, we''ll recognize this as a classic Ad Hominem. That''s when the author dismisses a claim because of who is making it, usually by pointing to (1) an ulterior motive or vested interest, or (2) hypocrisy or conflicting past behavior.
  Here, the herbalist disqualifies the doctors'' warning just because doctors supposedly have an interest in herbal treatments looking bad. The warning itself never gets answered.','Evaluate','Evaluate'),
('1c0d8000-8f52-451a-8497-28414f832400'::uuid,'52bb1c2ae7a618e8df751171a28af913','Look for an answer saying the herbalist dismisses the doctors'' claim by attacking the doctors'' motives instead of addressing whether the herbs are harmful.
  Or, there might be an answer saying, "even if the herb juice isn''t harmful, there still might be some *other* reason not to try it" (its price, its taste, or the time it takes away from a treatment that works).','Goal','Goal'),
('bdf0a819-b92d-4f0e-9717-bb131e5adfae'::uuid,'e8d4ddf38d804d0ec92d7385775f3848','The argument gives us two facts that share a middle term:

creativity → theta waves increase
music → theta waves increase

Then it concludes that music produces creativity. But the first fact only says creativity comes with more theta waves. It doesn''t say more theta waves bring creativity. That would be the reversal:

theta waves increase → creativity

So how could we argue against the conclusion? Suppose music raises theta waves and that''s all it does. Nothing in the evidence rules out theta waves rising with no creativity at all. Then music could raise theta waves without producing creativity.','Evaluate','Evaluate'),
('1e6e5a48-b204-4ff2-b652-3f7d6b427983'::uuid,'a1648b9ec77c3fca851ad692f7d1ccc9','Find an answer pointing out that theta waves can increase without a state of profound creativity. In other words, the argument treats something that accompanies creativity as if it were enough to produce creativity.','Goal','Goal'),
('0ffd2b3d-74c4-41d5-8bda-ee53fe3518d0'::uuid,'1aae6036fd45f0d5d09858fc925c25d8','The figures our computer program provides are remarkably consistent from week to week.','Evidence','Evidence'),
('274cdce0-e580-4603-ada2-7483a127bd9e'::uuid,'6a839c6ab7c188b9d36f9313030ed680','We can be confident of its accuracy.','Conclusion','Conclusion'),
('508136f4-1fb5-4f54-a32a-ff670e870566'::uuid,'d5411b60bd964e793c13d942b8bc7d19','Beck moves from consistent to accurate:

consistent → accurate

How could we argue the other side? Picture a bathroom scale that always reads five pounds too heavy. Your weight hasn''t changed, so you get the same number every morning. Perfectly consistent, and wrong every time.

The program could be like that scale. If it makes the same mistake every week, its figures would be consistent and inaccurate. Consistency tells us the program is stable, not that it''s right.','Evaluate','Evaluate'),
('243e6ec7-ea2e-4f77-b29b-db10400a82d9'::uuid,'e73aeb52b502f22022138afddf824510','Look at the timing. The consent forms are filled out before the test. The resentment the ethicists describe comes after: when a subject learns they got a placebo, or that the medicine didn''t work.

How could we argue that many subjects still resent it? Accepting a risk isn''t the same as being fine with how it turns out. You can agree to a coin flip and still be upset when you lose. These subjects are suffering from the diseases being treated and hoping the medicine helps. Signing a form that says "I understand I might get a placebo" fits perfectly well with resentment when the placebo arrives.

So the columnist assumes the attitude on the form is the attitude after the outcome.','Evaluate','Evaluate')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;