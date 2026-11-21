update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('e97e6dfc-ab09-48ec-98b3-01348735ebe9'::uuid,'f1842f9ce33465600d0a03d938f10187','Phrases like "as so-and-so said" or "as the saying goes" signal that the story just told illustrates the quote that follows.

The rule:
apparent counterexample just given → "as the saying goes" (or similar) is used inappropriately','Principle (when)','Principle (when)'),
('947254e3-8811-4acb-a129-4f94ec3d2649'::uuid,'8e4b430257d06daff918a28bad3a3d56','Every choice tells a short story and then tacks on a saying with one of these phrases. So the work is the same five times: read the story, then ask whether what just happened supports the saying or seems to run against it.

If the story supports the saying, the phrase is doing its job. If the story looks like an exception to the saying, the phrase is misused, and that is the answer the stem wants. Don''t get pulled into whether the saying is wise. We only care whether this story fits it.','Evaluate','Evaluate'),
('90e0aaee-c2b3-4e58-bde4-f30d4f92d8fe'::uuid,'bf92253095feacc69662fc26b46cbb87','Find the story whose events point the opposite way from its saying: things go one way, and the quote that follows claims something the story just contradicted.','Goal','Goal'),
('b59d5d95-c3d2-4ca3-b4d1-1c589562462e'::uuid,'8053318dec48322f9c2fbacc954aff09','Situation: someone in a cold climate buys a coat that is stylish but not warm, to look sophisticated.

Analysis: people are sometimes willing to sacrifice sensual comfort or pleasure for the sake of appearances.','Given','Situation and Analysis'),
('2f36e995-a397-4279-b070-de3509a8a40f'::uuid,'dcbb3403397f21882e727e9c3f5a2d43','This is a case, and the stem wants the general rule it illustrates. So strip out the specifics and keep the moving parts.

Who gets blamed more? Politicians, which in general terms are publicly known people.
Why? Not mainly because they are familiar. The author sets that explanation aside. The reason is that people feel they have more power over politicians.

So the case links two things: feeling power over someone and blaming that someone more. The author also hands us a trap in advance. Familiarity is named only to be rejected, so an answer that makes familiarity the driver of blame is fighting the stimulus.','Evaluate','Evaluate'),
('dd11ceed-c9f5-4468-bfd1-31071f1c4906'::uuid,'67c0a3572b54e663e01f3d25dd16de69','We''re looking for a generalization like: people are more likely to blame a public figure when they feel they have power over that figure.','Goal','Goal'),
('f019c330-3296-42cf-8e9d-4d4155dec75d'::uuid,'7c57f0d792e8ff8f569bc55dfd7742ad','Increased productivity resulting from greater efficiency [from Taylor''s methods] has led to increases in most workers'' standards of living.','Opposing Idea','The gain'),
('8951647c-05a8-4bc8-9168-57a8960370cb'::uuid,'ca3c5ff864702e14054baddcc2017384','At the same time, Taylor''s methods have tended to make these workers'' jobs routine and repetitive.','Evidence','The change'),
('3a20777e-3ecc-4f2f-b685-b8a9e6e6d8f6'::uuid,'7a3ff24a710078b99cb3d430b316ae72','That change has robbed their work of some of the intrinsic worth it possessed when it emphasized creativity and talent.','Conclusion','The loss'),
('56f863a7-167b-4c61-a12f-5bbf77c82d7e'::uuid,'1cde477671d3a063d92f0ea4a055fb93','This isn''t an argument. Nothing here is offered as proof of anything else. It is a description of a tradeoff, and the stem asks for the generalization it fits.

Taylor''s methods did two things at once. They raised efficiency and productivity, and that raised most workers'' standards of living: a material gain. They also made jobs routine and repetitive, which took away some of the work''s intrinsic worth: a loss in what the work itself is like.

So a matching generalization needs both sides: one development, a gain for workers in one respect, a loss for workers in another. Also watch the strength. The stimulus says "most" workers and "some of" the intrinsic worth, and it never says the gain causes the loss. An answer that claims more than that won''t fit cleanly.','Evaluate','Evaluate'),
('00dcf3ce-8256-449f-b0b5-a506f1757323'::uuid,'1d56700f33e001a94e4326ef105dc005','Something like: a change in industry can help workers in one way, such as their standard of living, while making their work worse in another way, such as how satisfying it is.','Goal','Goal'),
('165edab2-960b-43b1-90b6-13e5401a0cf0'::uuid,'d3a8a2b8a68c9c00d44dee2b7580c8a9','A rule can only prove its right side. Here that is one outcome: the government is justified in interfering. So any answer that concludes the government is not justified is out before we check anything else. Showing that the triggers are missing doesn''t prove the opposite outcome; it just means the rule doesn''t apply.

For an answer that concludes interference is justified, check that the facts in the choice establish both triggers:
1. The action would increase the likelihood of physical harm to others.
2. The action is not motivated by a desire to help others.

Watch the qualifiers. "Physical" rules out harm to looks or money. "Others" rules out harm to the person acting.

Goal: a judgment where someone acting for their own reasons does something likely to physically hurt other people, and the conclusion is that the government is justified in stepping in.','Evaluate / Goal','Evaluate / Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;