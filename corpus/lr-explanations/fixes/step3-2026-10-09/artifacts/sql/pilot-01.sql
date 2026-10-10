update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('46e6d3c1-5e7f-4f40-939c-ab4d239521b5'::uuid,'He''s currently proposing a new city ordinance prohibiting "bait-and-switch", but four years ago he owned an appliance store that was famous for its use of bait-and-switch.','Smith is now proposing an ordinance that bans the "bait-and-switch" sales tactic. But four years ago, Smith owned an appliance store that was famous for its use of bait-and-switch.','Evidence','Evidence'),
('b8076a74-666d-40bb-83ae-1b88584557ef'::uuid,'Whenever we''re doing Flaw and we see a Rebuttal style argument, we consider the 2 of the 10 Famous Flaws that deal with rebuttals: Ad Hominem - This refers to when an author dismisses an argument because the source of the argument has a biased interest or conflicting past behavior. Unproven vs. Proven False - This refers to when an author argues that "because there''s no evidence for X, or because someone''s attempt to prove X failed, that shows that X is false". This looks to be an example of Ad Hominem. The author isn''t saying that Smith''s claim is false, so it couldn''t be Unproven vs. Proven False. She''s just dismissing his view, saying "it doesn''t even merit consideration". And why? Because of Smith''s conflicting past behavior. We should never reject someone''s suggestion that we do Y just because that person used to say/do the opposite of Y. People and circumstances can change. Maybe there was someone who was really into cryptocurrency when it first came out but now is against it because of how bad its energy demands are for the environment. We can''t say, "Don''t listen to that crypto-critic. After all, he was way into Bitcoin when it first came out."','Whenever a Flaw argument rejects someone''s proposal, ask what the rejection is based on. Is it the proposal itself, or the person who made it?

The council president never says a word about the ordinance. Would it work? Would it protect shoppers? Is bait-and-switch harmful? None of that comes up. The only reason given is Smith''s past: Smith''s store was famous for the very tactic the ordinance would ban.

That is the Ad Hominem flaw: dismissing a position because of its source rather than its content. Smith''s history might make Smith look like a hypocrite, but hypocrisy doesn''t make an idea bad. Given that Smith once used bait-and-switch, how could we still argue the ordinance deserves a hearing? Easily. People change. Smith may have watched customers get burned and now wants the tactic gone. Someone who knows a tactic from the inside may even be well placed to write a rule against it.

Notice what the president does not say. The president never claims the ordinance is false or mistaken, only that it "does not even merit consideration." So answers about proving a claim false miss the target. The objection is to refusing to look at the ordinance at all.','Evaluate','Evaluate'),
('bb7e7ca7-6bf8-4c7c-b7da-9337f46059bf'::uuid,'Great works of art evoke passionate responses in those who view them. (GW → PR) The work of abstract painter Ezekiel Reilly elicits intensely emotional responses in those who view them. (PR)','Great works of art evoke passionate responses in those who view them.
GW → PR

The work of abstract painter Ezekiel Reilly elicits intensely emotional responses in those who view it.
Reilly''s art: PR','Evidence','Evidence'),
('5ccb5709-390f-4679-a7b8-88c20b32ce20'::uuid,'His art is great. (GW)','Reilly''s art is great.
Reilly''s art: GW','Conclusion','Conclusion'),
('756f3aef-e1fe-4ef6-b6d7-8d935db47e25'::uuid,'In order to draw this conclusion, we must assume that any work of art which elicits a passionate response is a great work. This is an illegal reversal of the first premise. (PR → GW)','The first premise is a conditional. If a work is great, then it evokes passionate responses. That makes a passionate response necessary for greatness: every great work has one.

The evidence tells us Reilly''s work has the passionate response. Then the conclusion jumps to greatness. That runs the arrow backward:

Premise: GW → PR
Author''s move: PR, so GW

In order to draw this conclusion, we must assume that any work of art which elicits a passionate response is a great work. That is an illegal reversal of the first premise. The rule tells us what follows from being great. It says nothing about what follows from stirring up strong feelings.

Think of a painting viewers find offensive, or a clumsy portrait that makes people furious. Both provoke intense reactions without being great art. A passionate response is a requirement for greatness, not proof of it.','Evaluate','Evaluate'),
('56f41c0f-785b-49e6-9cc6-3a251b6c033c'::uuid,'The companies only list voice mail''s advantages. If answering machines do something valuable that voice mail can''t, some people will keep them, and they won''t become obsolete.','The companies predict that answering machines will become obsolete, meaning hardly anyone will keep using them. Their reason is a list of voice mail''s strengths: more convenient, more flexible, less expensive.

Given that voice mail beats answering machines on all three, how could we argue answering machines will still survive? The list only covers what voice mail is good at. It never asks whether answering machines do something voice mail can''t. If they offer one valuable feature voice mail lacks, some customers will keep their machines for that feature alone, and the machines won''t become obsolete.

Notice how strong the conclusion is: "obsolete." To weaken it, we don''t have to show answering machines will win. We only need a reason a meaningful number of people would keep using them.','Evaluate','Evaluate'),
('773dcb3b-ca9e-4a32-a0e4-b56b8ebab524'::uuid,'Find an advantage answering machines have over voice mail.','Look for an advantage answering machines have that voice mail does not offer, something useful enough that people would keep their machines for it. Answers that add more voice mail strengths, or more answering machine weaknesses, help the companies instead.','Goal','Goal'),
('718bd96e-cea7-49a0-b1b6-9a55ffe0fb3b'::uuid,'Pause and infer. Technology brings more food, but the centralization it needs makes collapse deadlier. So technology doesn''t remove the dangers of collapse. If anything, the route to more food makes them worse.','Pause and infer before reading the choices. Line up the two relationships:

Better technology → more food, but only a negligible increase without centralization
More centralization → a greater share of people perish if the society collapses

So the technology route to more food runs through centralization, and centralization makes collapse deadlier. That is why the author concludes the effort will "merely exacerbate the disasters associated with societal collapse."

What does that tell us about technology and collapse? If better technology could prevent every problem that comes with a collapse, the author couldn''t say the technology-driven plan only makes those disasters worse. So at least one collapse problem, the higher death toll, is something technology does not fix.

On Most Strongly Supported questions, a weakly worded answer like "not every" is easy to prove. It needs only one exception, and the stimulus hands us one.','Evaluate','Evaluate'),
('7c2f4e9a-fca0-4474-a21b-87372a6535a2'::uuid,'Technology won''t prevent every problem that comes with a centralized society''s collapse.','Technology won''t prevent every problem that comes with a centralized society''s collapse. Look for a modestly worded answer along those lines. Be wary of answers that claim a trend over time, an "only" relationship, or anything about population growth the passage never addresses.','Goal','Goal'),
('e29f83ec-ca14-4f4a-92d1-f1a4fdfcbbc6'::uuid,'An Egyptian cup dating from 2000 B.C. depicts a brewery and contains residue of alcoholic beer — older than the Babylonian fermentation evidence from 1500 B.C.','An Egyptian cup dating from 2000 B.C. depicts what appears to be a brewery, and its chemical residue shows it held alcoholic beer. That is older than the Babylonian wine-making evidence from 1500 B.C., which had been thought to be the first.','Evidence','Evidence'),
('df1b22a1-32f7-4e82-bcfd-fd61bec76946'::uuid,'"First known" and "first ever" are different. The Egyptian cup is the earliest *archaeological evidence* of alcoholic beverage production we have found, but other societies — including the Egyptians themselves earlier or some entirely different civilization — could have produced alcohol earlier without leaving evidence behind, or with evidence we have not yet found.','"First known" and "first ever" are different claims. The cup is the earliest evidence of alcohol we have found. That puts Egypt ahead of Babylon on the evidence so far, but the conclusion says the Egyptians were the first society to produce alcoholic beverages at all.

Given the 2000 B.C. cup, how could we argue the Egyptians were not first? Another society could have brewed or fermented something earlier and left no trace, or left one nobody has dug up yet. The argument even shows how this happens: the Babylonians were thought to be first until this cup turned up. The next discovery could do the same to the Egyptians.

Whenever a conclusion says something was the first, the only, or never happened, check whether the evidence covers everything or just what has been found so far.','Evaluate','Evaluate'),
('688ff509-a7ab-4c06-b061-692fbc4d62ad'::uuid,'Political candidates’ speeches are loaded with promises and with expressions of good intention.
But one must not forget that the politicians’ purpose in giving these speeches is to get themselves elected.
Conclusion
Clearly, then, these speeches are selfishly motivated and the promises made in them are unreliable.
Evaluate
This is an ad hominem attack. Just because politicians are motivated to win election does not mean that their promises are unreliable.','Political candidates'' speeches are loaded with promises and with expressions of good intention.

But one must not forget that the politicians'' purpose in giving these speeches is to get themselves elected.','Evidence','Evidence')
) v(id,ob,nb,ol,nl) where t.id=v.id and t.body=v.ob returning t.id;