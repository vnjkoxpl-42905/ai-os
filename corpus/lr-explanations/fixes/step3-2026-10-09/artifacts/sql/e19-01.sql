update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('00e40578-bc91-4a71-8b9f-67df69fbcf56'::uuid,'6ebd0e6dcdb28bb6af21f515460594da','On a Role question, find the conclusion first, then ask what the named claim does for it.

The conclusion carries the opinion word: the medical establishment should "announce only conclusive results". The next sentence opens with "After all," and that phrase hands us a reason for the claim right before it. So the fire drill sentence is support for the conclusion.

Now look at what kind of support it is. Fire drills have nothing to do with food studies. The physician pulls in a situation from a different area of life because it works the same way: people hear a signal over and over, the signal rarely means anything, and they stop reacting. Constant tentative warnings are the fire drills. A health warning that finally matters is the real alarm. That is an analogy.','Evaluate','Evaluate'),
('88d2713b-fc3b-4661-bf77-db6938b0e762'::uuid,'85a4009d9a50141df4c269260ff5696e','We''re asked about the last sentence. Prediction: it''s an analogy offered as support for the main conclusion, the claim that the medical establishment should announce only conclusive results.

Any answer that calls it an example of the health warnings themselves, an objection, or decoration is out before we read the details.','Goal','Goal'),
('47320945-1608-4997-8a8d-2553ef76b2c0'::uuid,'0ea35382176ad5a255d74089f0c0e2f4','Among 100 first-graders who got handwriting lessons, those whose composition skills had improved the most were the ones who had learned to write letters the most automatically.

Notice the mismatch: the composition half is about improvement, while the handwriting half is about how automatic the kids ended up.','Evidence','Evidence'),
('cf84d2b1-9d6f-44a8-b234-abc41fd3c429'::uuid,'4de4c24d06fc48a08c438fe20146ba7d','This is a study that hands us a correlation, and the author reads a cause into it.

CURIOUS FACT: Why were the kids with the biggest composition gains the same kids who wrote letters most automatically?

AUTHOR''S EXPLANATION: Handwriting lessons made writing automatic for some kids. Once forming letters stopped taking effort, those kids had attention left over for what they were writing, so their composition improved.

Now argue with it. How could we explain the same data without the author''s story? Maybe some kids were simply stronger students from the start. They could already write letters automatically before the lessons, and they also picked up composition faster, with no help from automatic handwriting. The evidence doesn''t rule that out, because it never tells us whether automaticity changed during the lessons.','Evaluate','Evaluate'),
('7c43a239-ae68-4b6e-8e8c-c8baf632e8ec'::uuid,'03bb0458011b26fc7f9e793f4cf0a51d','Strengthen answers for a curious fact usually do one of two things: make the author''s explanation more plausible, or rule out an alternate explanation.

The best target here: show that the kids who gained the most automaticity during the lessons also gained the most in composition. Change tracking change is what we''d expect if automatic handwriting frees up attention, and it shrinks the room for the stronger-students-from-the-start story.','Goal','Goal'),
('dfe89858-b232-4a53-b9da-12973ec59c10'::uuid,'7438b726b97146fe8aab2d9540a350eb','The conclusion follows a process of elimination. Medications with an unpleasant taste are "generally produced only in tablet, capsule, or soft-gel form." M can''t be a tablet, because its waxy ingredient can''t take the heat. M can''t be a soft-gel, because the company "does not have soft-gel manufacturing technology" and makes everything itself. Capsule is what''s left.

But look at who the first rule covers: only medications with an unpleasant taste. Nothing tells us M tastes bad. If M tastes fine, the rule never applies, and M could come in a liquid, a powder, or anything else. The elimination only works if M is in the group the rule covers.
PT → (T or C or SG)
~T
~SG
missing: PT','Evaluate','Evaluate'),
('75c4f679-6d2a-401c-938d-59a4bf0c3e64'::uuid,'44707bda1a062188817b66cfae608ca5','In ancient Greek courts, witnesses were not cross-examined, and the jury, "selected from the citizenry," "received no guidance on points of law".
So it was extremely important for litigants to make a good impression on the jurors.','Evidence','Evidence'),
('bac48c6b-a834-48b0-82d2-9d1b65a21402'::uuid,'1e41c824566089cf373502c4545dd4fd','The evidence tells us litigants worked hard to impress jurors. The conclusion jumps to something else: that their speeches show what ordinary citizens thought was moral.

How could we argue against that? Maybe litigants impressed jurors some other way: with charm, flattery, appeals to class, or clever storytelling. Then the speeches would tell us what jurors found appealing, not what they believed about right and wrong. Maybe litigants presented an ideal moral code nobody actually held.

For the speeches to be a good record of common morality, two links have to hold. Litigants tried to impress jurors by appealing to the jurors'' moral views. And the jurors'' views were the citizens'' views, which the argument already gives us since jurors came from the citizenry.','Evaluate','Evaluate'),
('cd7154ad-a0b5-4f67-9603-8a0fefeafae1'::uuid,'987a453d513f544924cc64609b2e2e88','The burrowing activities of sand termites cause fairy circles to form.','Conclusion','Conclusion'),
('0a2eb3e4-5b21-4a54-bfd2-088618899396'::uuid,'69fd9b19ab190c746074e99b31f6cf20','Sand termite colonies were found in every fairy circle the scientists investigated.','Evidence','Evidence'),
('d5c60ec9-d4f0-449d-8a11-fcd64e106be4'::uuid,'3da465a30547baf2630a70fa1777dd4e','This is a correlation (termites are always there) turned into a cause (termites make the circles).

How else could we explain termites showing up in every circle? Maybe the arrow runs the other way: something else kills the grass, and termites move into the bare patches afterward. Or something else entirely, such as the soil or the climate, creates the circles, and termites just happen to live in the same ground.

So we want evidence that the circles form the way burrowing would make them form, or evidence that knocks out a rival cause.','Evaluate','Evaluate'),
('5668f31e-b8b2-47c6-aaa7-dbda3d15aafe'::uuid,'5ddc58d37485002f56bfe18887724188','Best target: something about how plants die in the circles that matches termites burrowing underground, especially while the circles are forming. Ruling out a rival such as termites arriving after the circles already exist would also work.','Goal','Goal'),
('93de37eb-e49a-4b6a-803a-4eebe4cbbcdd'::uuid,'b441311953adfaf8948f63cdb853170b','Start with who made the poles. If Homo sapiens weren''t in Europe until 200,000 years ago, then the 400,000-year-old poles belonged to the humanlike precursors. The argument needs that part, and it gets it from the second premise.

The weak part is what the poles were for. The conclusion says the find disproves the belief that the precursors were only "gatherers and scavengers and did not hunt." That only works if the poles and flint were used to hunt.

How could we argue they weren''t? Maybe the sharpened poles were for fending off predators. Maybe the horses died on their own, and the precursors used the flint and poles to cut up and carry away the carcasses. Either way, the find fits a group of scavengers just fine.','Evaluate','Evaluate'),
('5123f2ed-a700-4c1f-ac1d-9590b1d55582'::uuid,'cafc3fa46074deabe45df4af67e9b36e','Look for an answer that shows the poles were used for hunting, or one that rules out the non-hunting uses, such as defense or handling scavenged meat.','Goal','Goal'),
('5255bdef-38f2-4903-8b12-a8ead7021a4d'::uuid,'27fbaa7298362c107251c4eb0d7ccfc1','Profit is what you take in minus what you spend. The evidence says organic and conventional orchards cost the same to run and produce the same amount. So the only difference left is taste, and the conclusion bets that better taste means more profit.

How could we argue against that? Maybe buyers don''t care about taste. If people buy apples by price or by looks, better tasting apples sell no better and earn no more. Then equal costs and equal output mean equal profit.

The argument needs better taste to turn into more money: higher prices, more sales, or both.','Evaluate','Evaluate'),
('957258e0-ab27-4290-af10-9ffb6680eb9e'::uuid,'b7f8f928328a21f2b5632bb6edda1150','Look for an answer showing that better taste brings in more revenue, for example that apple demand or apple prices depend on flavor.','Goal','Goal'),
('1316bb8b-f740-422a-9ab1-94498a72113c'::uuid,'84470016873c69b4ab8364767e3ca902','First-born children in the study consistently showed "less cognitive plasticity than did their siblings." Cognitive plasticity is the willingness to accept new ideas.
It is "reasonable to think" that people open to new ideas will be adventurous in other ways.','Evidence','Evidence'),
('fba4670a-559d-475c-83e6-f8f64bafea7e'::uuid,'39cfba36a361a2ba1f310ab596c114e5','The study only measured one thing: openness to new ideas. The conclusion is about something else: being adventurous. The psychologist bridges the two with a premise that is just "reasonable to think".

How could we argue against it? Plenty of people are open to new ideas and still avoid risk in everything else. Being adventurous probably depends on many things, and openness to ideas might be a small part of it, or no part at all. If so, the study''s result tells us nothing about who is more adventurous.','Evaluate','Evaluate'),
('b8a4b25a-b08c-4102-bb24-0a50fdc9a581'::uuid,'5dd620579662a2d12d7f31681e87f0c5','Look for evidence that people with more cognitive plasticity really are more adventurous, for example that openness to new ideas goes along with risk-taking. That turns the psychologist''s guess into something with support.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;