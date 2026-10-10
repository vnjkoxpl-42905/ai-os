insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('5dab36d2-be42-4dac-b4c3-9a1758a48326'::uuid,2,'Evaluate','On Main Conclusion questions, listen for the conclusion early. It usually shows up in the first sentence or right after a pivot that pushes back on someone else''s view.

Here the first sentence does both. "Contrary to recent speculations" tells us other people expect a hardware store, and the author is about to disagree. Then comes the author''s own claim: no hardware store will be opening in the plaza.

Test it by asking, "Why should I believe that?" The next two sentences answer. Anyone opening a store there would already be publicizing it, and there has been no publicity. So nobody is opening a store there. Both sentences point back at the first one, which makes the first sentence the main conclusion and the other two its evidence.

The speculation itself is not the author''s view. It is the position the author argues against.'),
('5dab36d2-be42-4dac-b4c3-9a1758a48326'::uuid,3,'Goal','Find the answer that restates the author''s claim with the opener stripped off: a hardware store will not be opening in the shopping plaza. Expect trap answers that restate the speculation, the conditional premise, or the no-publicity premise.'),
('c97829cb-ce32-4ed7-b348-87a1a99191f7'::uuid,3,'Evaluate','The conclusion here sits in the middle sentence, and the word "For" is what gives it away. "For" means "because": the last sentence is the reason for the sentence before it. Why should we believe that expanding your mind lets you inspire curiosity? Because it makes you impossible to fully comprehend, so you stay a mystery to others.

So what is the first sentence doing? It is called "a given." Nothing argues for it, and it is not a reason for the middle sentence either. It explains why anyone would care about inspiring curiosity. That makes it background, not the conclusion.

Now the hard part: the conclusion is a conditional, so direction matters. The author says expanding your mind is enough to inspire curiosity:

Expands mind → Inspires others'' curiosity

The author does not say it is the only way. An answer that flips this into a requirement, or that changes whose curiosity we are talking about, is a different claim.'),
('c97829cb-ce32-4ed7-b348-87a1a99191f7'::uuid,4,'Goal','Look for an answer that says: if you constantly broaden your abilities and extend your intellectual reach, you will be able to inspire the perpetual curiosity of others. Check the direction (broadening is the trigger, curiosity is the result) and check that the curiosity belongs to other people.'),
('737e7000-49dd-46b2-b774-be961f17f175'::uuid,2,'Evaluate','On Main Conclusion questions, check the first sentence first. It is often the claim, with the reasons following it.

The manager opens with an opinion: there is no good reason to suppose promoting creativity is a proper goal of employee training. Ask, "Why should I believe that?" The rest of the paragraph answers. Reason one: many jobs need little or no creativity, and in those jobs creativity is more likely to disrupt than to innovate. Reason two, flagged by "Furthermore": even if creativity were in demand, there is no evidence it can be taught.

"Furthermore" stacks a second reason on the first. Both point back at the opening sentence, so that sentence is the main conclusion.

Notice how careful the conclusion is. The manager does not say training should never promote creativity. The claim is only that there is no good reason to think it should.'),
('737e7000-49dd-46b2-b774-be961f17f175'::uuid,3,'Goal','Look for an answer that matches the first sentence, including its caution: there is no good reason to suppose employee training programs should promote creativity. Expect traps that restate one of the two reasons, or that state them more strongly than the manager did.'),
('1da55640-b0da-40a2-bb51-02ea734fb642'::uuid,4,'Evaluate','On Main Conclusion questions, listen for the moment the author''s own voice arrives. Here the first two sentences belong to the many people the anthropologist is answering: chimpanzees should have something like language, because traits evolve gradually and something like human language must exist in the species humans evolved from.

Then the pivot: "This general line of argument may be reasonable, but". The anthropologist grants the gradual-evolution reasoning and rejects only one step of it, the jump to chimpanzees. The claim after "but" is the author''s position.

Check it with "Why should I believe that?" The answer follows the word "because": humans did not evolve from chimpanzees. Chimps are relatives through a common ancestor, and language might have started after that ancestor died out. So even if something like language must exist in species humans evolved from, chimpanzees are not one of those species, and nothing follows about them.

Notice how limited the conclusion is. The author does not say chimpanzees lack language. The claim is that this argument does not show they have it.'),
('1da55640-b0da-40a2-bb51-02ea734fb642'::uuid,5,'Goal','Look for an answer that says the gradual-evolution reasoning does not tell us whether chimpanzees have anything like human language. The right answer may be abstract and describe the reasoning instead of quoting it. Reject any answer that says chimpanzees lack language, since the author only says it does not follow that they have it.'),
('886b6f2d-ba7b-4892-89b4-5c2d44327e59'::uuid,4,'Goal','A correct answer will say that conducting all financial business from home by computer or telephone may benefit banks more than it benefits customers. Keep the comparison and the hedge.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;