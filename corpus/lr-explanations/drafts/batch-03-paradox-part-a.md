---
type: draft
subject: LR Paradox batch 03, part A, 19 slots
status: loaded 2026-10-01
created: 2026-10-01
---

# Paradox explanations: batch 03, part A

Source: the bank on current main (`3fb8c77` and later, worktree `../ai-os-projects/lsatu-wt-bankfix-b02`, detached at origin/main) and the post-batch-02 database pull. Batch 03 is the first 40 Paradox and Paradox EXCEPT slots in gap-list order; all 40 are already in the database. This file holds the first 19. PT117-S3-Q2 (part B) has steps and needs notes only; every other slot needs steps and five notes.

Steps use the Paradox labels already in the database (Given that / How can it be that / Evaluate / Goal). `Modelled on` references are picks from `models/Paradox-Method.md`. Tags come from the existing Paradox vocabulary in `lr_answer_choices.tag`; "Helps Explain" marks the four working choices on EXCEPT and "helps least" questions. Quoted question text is inserted from the bank by script, whitespace normalized.

## PT102-S2-Q17 | Paradox | D

**Modelled on:** PT101-S3-Q14 (EXCEPT, one frame for every choice), PT148-S3-Q11 (explain a difference with a difference).

> Nicotine has long been known to cause heart attacks and high blood pressure. Yet a recent study has shown that the incidence of heart attacks and high blood pressure is significantly higher among cigarette smokers who do not chew tobacco than among nonsmokers exposed to an equal amount of nicotine through tobacco chewing.
>
> Which one of the following, if true, helps least to resolve the apparent discrepancy described above?
>
> (A) People who smoke but do not chew tobacco tend to exercise less than those who chew tobacco but do not smoke.
> (B) Chemicals other than nicotine present in chewing tobacco but not present in cigarette smoke mitigate the effects that nicotine has on the cardiovascular system.
> (C) People who chew tobacco but do not smoke tend to have healthier diets than those who smoke but do not chew tobacco.
> (D) Chemicals other than nicotine present in chewing tobacco but not present in cigarette smoke can cause cancer.
> (E) Chemicals other than nicotine present in cigarette smoke but not present in chewing tobacco raise blood pressure.

### Argument Breakdown

**Given that:** Nicotine causes heart attacks and high blood pressure, and the smokers and chewers in the study took in the same amount of nicotine.

**How can it be that:** Smokers who do not chew have significantly more heart attacks and high blood pressure than chewers who do not smoke?

**Evaluate:** Nicotine is equal, so it cannot be the difference. The answer has to be something else that separates the two groups: another ingredient in smoke that hurts the heart, something in chewing tobacco that protects it, or a lifestyle difference like diet or exercise. Run each choice through one frame: "Smokers have more heart trouble than chewers because..."

**Goal:** This is a "helps least" question. Four choices will name a heart-related difference between the groups. The answer will not.

### Choice Notes

**(A) Helps Explain.** Smokers exercise less. Less exercise is bad for the heart, so this is a non-nicotine difference that fits the frame.

**(B) Helps Explain.** Something in chewing tobacco blunts nicotine's effect on the heart. Same nicotine, less damage for chewers.

**(C) Helps Explain.** Chewers eat better. A healthier diet protects the heart, which separates the groups.

**(D) Correct.** Cancer is not heart attacks or blood pressure. A chemical in chewing tobacco that causes cancer says nothing about why chewers have *fewer* heart problems. If anything, it is one more harm for chewers, and it fails the frame.

**(E) Helps Explain.** Something in cigarette smoke, but not in chewing tobacco, raises blood pressure. That gives smokers extra heart risk on top of the shared nicotine.

## PT104-S1-Q7 | Paradox | C

**Modelled on:** PT148-S3-Q11 (difference between groups), PT140-S1-Q20 (part vs whole).

> Because of the recent recession in Country A, most magazines published there have experienced decreases in advertising revenue, so much so that the survival of the most widely read magazines is in grave doubt. At the same time, however, more people in Country A are reading more magazines than ever before, and the number of financially successful magazines in Country A is greater than ever.
>
> Which one of the following, if true, most helps to resolve the apparent discrepancy in the information above?
>
> (A) Most magazines reduce the amount they charge for advertisements during a recession.
> (B) The audience for a successful television show far exceeds the readership of even the most widely read magazine.
> (C) Advertising is the main source of revenue only for the most widely read magazines; other magazines rely on circulation for their revenue.
> (D) Because of the recession, people in Country A have cut back on magazine subscriptions and are reading borrowed magazines.
> (E) More of the new general interest magazines that were launched this year in Country A have survived than survived in previous years.

### Argument Breakdown

**Given that:** Most magazines have lost advertising revenue in the recession, enough to put the most widely read magazines in danger.

**How can it be that:** People are reading more magazines than ever, and more magazines are financially successful than ever?

**Evaluate:** Notice the two groups the stimulus names. The danger is to the *most widely read* magazines. The success is counted across magazines in general. If smaller magazines do not depend much on advertising, an ad slump would hurt the big ones while the rest thrive on more readers. Look for something that separates how the two kinds of magazine make money.

**Goal:** Find a difference in revenue source between the most widely read magazines and the others.

### Choice Notes

**(A) Half Scope.** Cheaper ad rates would explain the fall in ad revenue. They do nothing to explain why more magazines than ever are succeeding.

**(B) Out of Scope.** Television audiences do not tell us anything about magazine revenue or magazine success.

**(C) Correct.** Only the biggest magazines live on advertising, so the ad slump threatens them. Everyone else lives on circulation, and more people are reading, so more of them succeed. Both halves of the stimulus now fit.

**(D) Deepens Paradox.** If readers cut subscriptions and borrow copies, circulation revenue falls too. That makes the record number of successful magazines even harder to explain.

**(E) Restates Paradox.** New magazines surviving is one more sign of success. It repeats the surprising fact instead of explaining it.

## PT105-S4-Q2 | Paradox EXCEPT | B

**Modelled on:** PT107-S4-Q19 (EXCEPT: is it a reason for joy?), PT113-S2-Q17 (three-and-one split).

> The blues is a modern musical form whose lyrics usually address such topics as frustration, anger, oppression, and restlessness. Yet blues musicians claim to find joy in performing, and the musicians and fans alike say that the blues’ overall effect is an affirmation of life, love, and hope.
>
> Each of the following, if true, helps to resolve the apparent conflict in the passage except:
>
> (A) The sharing of blues music serves to create a cohesive, sympathetic social network.
> (B) Blues musicians who do not draw on their personal tragedies are no more successful than blues musicians who do.
> (C) The irony and wit found in the blues provide a sense of perspective on life’s troubles.
> (D) The realization that other people share one’s plight is helpful in dealing with life’s problems.
> (E) The conversion of personal sorrow into an artistic work can have a cathartic effect on artists and their audiences.

### Argument Breakdown

**Given that:** Blues lyrics are usually about frustration, anger, oppression and restlessness.

**How can it be that:** Musicians find joy in performing the blues, and players and fans say its overall effect affirms life, love and hope?

**Evaluate:** We need ways that singing about trouble can leave people feeling better. Shared experience, humor, perspective and release would all do it. Each working answer should connect the sad material to the positive effect.

**Goal:** Four choices give a way sad songs can produce joy or hope. The answer will not touch joy or hope at all.

### Choice Notes

**(A) Helps Explain.** Sharing the music builds a supportive community. Belonging is a source of joy, even when the songs are about pain.

**(B) Correct.** This compares *success* between two kinds of musicians. It says nothing about why performing sad songs brings joy or hope to anyone, so it does not touch the conflict.

**(C) Helps Explain.** Irony and wit give perspective on troubles. Laughing at hardship is one way sad material turns into affirmation.

**(D) Helps Explain.** Hearing that others share your plight helps you cope. That turns songs about trouble into comfort.

**(E) Helps Explain.** Turning sorrow into art can be cathartic for both performer and audience. Release is a direct route from sad lyrics to a good feeling.

## PT106-S1-Q8 | Paradox | C

**Modelled on:** PT139-S1-Q15 (find the other cause), PT141-S4-Q15 (breadcrumbs).

> Generally speaking, if the same crop is sown in a field for several successive years, growth in the later years is poorer than growth in the earlier years, since nitrogen in the soil becomes depleted. Even though alfalfa is a nitrogen-fixing plant and thus increases the amount of nitrogen in the soil, surprisingly, it too, if planted in the same field year after year, grows less well in the later years than it does in the earlier years.
>
> Which one of the following, if true, most helps to explain the similarity described above between alfalfa and non-nitrogen-fixing plants?
>
> (A) Some kinds of plants grow more rapidly and are more productive when they are grown among other kinds of plants rather than being grown only among plants of their own kind.
> (B) Alfalfa increases the amount of nitrogen in the soil by taking nitrogen from the air and releasing it in a form that is usable by most kinds of plants.
> (C) Certain types of plants, including alfalfa, produce substances that accumulate in the soil and that are toxic to the plants that produce those substances.
> (D) Alfalfa increases nitrogen in the soil in which it grows only if a certain type of soil bacteria is present in the soil.
> (E) Alfalfa is very sensitive to juglone, a compound that is exuded from the leaves of black walnut trees.

### Argument Breakdown

**Given that:** Most crops grow worse in later years because they use up the soil's nitrogen. Alfalfa adds nitrogen to the soil.

**How can it be that:** Alfalfa still grows worse year after year when planted in the same field?

**Evaluate:** Nitrogen cannot be alfalfa's problem, since it makes its own. So something *else* about growing in the same spot must be hurting it. What builds up or runs down when the same plant grows in one field for years? Pests, disease, or something the plant itself leaves behind.

**Goal:** Find a cause of decline other than nitrogen loss that applies to alfalfa.

### Choice Notes

**(A) Too Weak.** "Some kinds of plants" do better among other species. We are not told alfalfa is one of them, and this does not give a mechanism for its year-to-year decline.

**(B) Deepens Paradox.** This explains how alfalfa adds usable nitrogen. It confirms the expectation that alfalfa should not run short, so it makes the decline more puzzling.

**(C) Correct.** Alfalfa produces substances that build up in the soil and poison it. Each year in the same field, more of the toxin is there. That is a reason for decline that has nothing to do with nitrogen.

**(D) Unclear Impact.** Alfalfa adds nitrogen only when certain bacteria are present. The stimulus already says alfalfa increases nitrogen, and we are not told the bacteria are missing, so this does not explain the decline.

**(E) Out of Scope.** No black walnut trees are mentioned. A sensitivity to their leaves cannot explain decline in an ordinary alfalfa field.

## PT106-S3-Q3 | Paradox | E

**Modelled on:** PT154-S1-Q6 (one concrete mechanism), PT141-S4-Q15 (read the details).

> Birds startled by potential predators generally try to take cover in nearby vegetation. Yet many birds that feed at bird feeders placed in suburban gardens are killed when, thus startled, they fly away from the vegetation in the gardens and into the windowpanes of nearby houses.
>
> Which one of the following, if true, most helps to explain the anomalous behavior of the birds that fly into windowpanes?
>
> (A) Predator attacks are as likely to occur at bird feeders surrounded by dense vegetation as they are at feeders surrounded by little or no vegetation.
> (B) The bird feeders in some suburban gardens are placed at a considerable distance from the houses.
> (C) Large birds are as likely as small birds to fly into windowpanes.
> (D) Most of the birds startled while feeding at bird feeders placed in suburban gardens are startled by loud noises rather than by predators.
> (E) The windowpanes of many houses clearly reflect surrounding vegetation.

### Argument Breakdown

**Given that:** Startled birds usually fly toward nearby vegetation for cover.

**How can it be that:** Startled birds at suburban feeders fly *away* from the garden's vegetation and into windows?

**Evaluate:** The birds' instinct is to seek vegetation. What if they think they *are* flying toward vegetation? A window that reflects trees and shrubs would look like cover. Then the birds are following their usual instinct, and the glass is the trap.

**Goal:** Find a reason the windows look like a place to hide.

### Choice Notes

**(A) No Impact.** How likely an attack is near dense versus sparse vegetation does not explain where a startled bird flies.

**(B) Deepens Paradox.** If some feeders are far from houses, birds there have even less reason to hit windows. It does nothing for the birds that do.

**(C) No Distinction.** Bird size is not part of the puzzle. Large and small birds alike hitting windows leaves the behavior unexplained.

**(D) Too Weak.** Being startled by noise rather than predators might change a reaction in general, but it does not explain flying *into windows* rather than into the vegetation.

**(E) Correct.** If the windows reflect the surrounding plants, a fleeing bird sees what looks like cover and flies toward it. It is behaving just as the first sentence says birds do.

## PT107-S1-Q10 | Paradox | D

**Modelled on:** PT141-S4-Q15 (breadcrumbs), PT152-S4-Q23 (state the exact gap).

> The symptoms of hepatitis A appear no earlier than 60 days after a person has been infected. In a test of a hepatitis A vaccine, 50 people received the vaccine and 50 people received a harmless placebo. Although some people from each group eventually exhibited symptoms of hepatitis A, the vaccine as used in the test is completely effective in preventing infection with the hepatitis A virus.
>
> Which one of the following, if true, most helps resolve the apparent discrepancy in the information above?
>
> (A) The placebo did not produce any side effects that resembled any of the symptoms of hepatitis A.
> (B) More members of the group that had received the placebo recognized their symptoms as symptoms of hepatitis A than did members of the group that had received the vaccine.
> (C) The people who received the placebo were in better overall physical condition than were the people who received the vaccine.
> (D) The vaccinated people who exhibited symptoms of hepatitis A were infected with the hepatitis A virus before being vaccinated.
> (E) Of the people who developed symptoms of hepatitis A, those who received the vaccine recovered more quickly, on average, than those who did not.

### Argument Breakdown

**Given that:** The vaccine is completely effective at preventing hepatitis A infection.

**How can it be that:** Some vaccinated people in the test later showed symptoms of hepatitis A?

**Evaluate:** The first sentence is a breadcrumb: symptoms appear at least 60 days *after* infection. So a person can show symptoms long after they were infected. If some vaccinated people were already infected before the shot, a perfect vaccine could not prevent an infection that had already happened.

**Goal:** Look for vaccinated people who were infected before vaccination.

### Choice Notes

**(A) Half Scope.** This is about the placebo group. It does not explain why people in the *vaccine* group got symptoms.

**(B) No Impact.** Who recognized their symptoms does not change who had them. Vaccinated people still showed symptoms.

**(C) No Impact.** Overall fitness might affect how sick someone gets, but a completely effective vaccine should prevent infection regardless.

**(D) Correct.** The vaccine prevents infection; it cannot undo one that already happened. With a 60-day delay before symptoms, people infected before the shot would show symptoms afterward. The vaccine is still completely effective.

**(E) Too Weak.** Faster recovery says the vaccinated people were still infected. That is the puzzle, not the explanation.

## PT107-S1-Q25 | Paradox EXCEPT | B

**Modelled on:** PT120-S3-Q15 (EXCEPT: name the routes up front), PT113-S2-Q17 (three-and-one split).

> The indigenous people of Tasmania are clearly related to the indigenous people of Australia, but were separated from them when the land bridge between Australia and Tasmania disappeared approximately 10,000 years ago. Two thousand years after the disappearance of the land bridge, however, there were major differences between the culture and technology of the indigenous Tasmanians and those of the indigenous Australians. The indigenous Tasmanians, unlike their Australian relatives, had no domesticated dogs, fishing nets, polished stone tools, or hunting implements like the boomerang and the spearthrower.
>
> Each of the following, if true, would contribute to an explanation of differences described above except:
>
> (A) After the disappearance of the land bridge the indigenous Tasmanians simply abandoned certain practices and technologies that they had originally shared with their Australian relatives.
> (B) Devices such as the spear-thrower and the boomerang were developed by the indigenous Tasmanians more than 10,000 years ago.
> (C) Technological innovations such as fishing nets, polished stone tools, and so on, were imported to Australia by Polynesian explorers more recently than 10,000 years ago.
> (D) Indigenous people of Australia developed hunting implements like the boomerang and the spearthrower after the disappearance of the land bridge.
> (E) Although the technological and cultural innovations were developed in Australia more than 10,000 years ago, they were developed by groups in northern Australia with whom the indigenous Tasmanians had no contact prior to the disappearance of the land bridge.

### Argument Breakdown

**Given that:** Tasmanians and Australians are related and were separated about 10,000 years ago.

**How can it be that:** Two thousand years later, Tasmanians lacked dogs, nets, polished tools and implements like the boomerang that Australians had?

**Evaluate:** There are only a few routes. The Tasmanians lost things they once had. The Australians gained things after the split, by invention or import. Or the Australians had them before the split, but only in groups the Tasmanians never met. Any of these explains the gap.

**Goal:** Four choices fit one of those routes. The answer will make the gap harder to explain.

### Choice Notes

**(A) Helps Explain.** Tasmanians once had these practices and dropped them. That is the "lost it" route.

**(B) Correct.** If Tasmanians developed boomerangs and spear-throwers *before* the split, they should still have had them. This adds to the mystery of why they lacked them later instead of explaining it.

**(C) Helps Explain.** Polynesians brought these innovations to Australia after the bridge disappeared. Tasmania was cut off by then, so Tasmanians never got them.

**(D) Helps Explain.** Australians invented the boomerang and spear-thrower after the split. Tasmanians could not have received them.

**(E) Helps Explain.** The innovations existed before the split, but only among northern groups the Tasmanians never contacted. Separation then kept them out.

## PT107-S3-Q21 | Paradox | D

**Modelled on:** PT143-S1-Q19 (averages, do the numbers), PT120-S4-Q1 (per-item vs total).

> A study of the difference in earnings between men and women in the country of Naota found that the average annual earnings of women who are employed full time is 80 percent of the average annual earnings of men who are employed full time. However, other research consistently shows that, in Naota, the average annual earnings of all employed women is 65 percent of the average annual earnings of all employed men.
>
> Which one of the following, if also established by research, most helps explain the apparent discrepancy between the research results described above?
>
> (A) In Naota, the difference between the average annual earnings of all female workers and the average annual earnings of all male workers has been gradually increasing over the past 30 years.
> (B) In Naota, the average annual earnings of women who work full time in exactly the same occupations and under exactly the same conditions as men is almost the same as the men’s average annual earnings.
> (C) In Naota, a growing proportion of female workers hold full-time managerial, supervisory, or professional positions, and such positions typically pay more than other types of positions pay.
> (D) In Naota, a larger proportion of female workers than male workers are part-time workers, and part-time workers typically earn less than full-time workers earn.
> (E) In ten other countries where the proportion of women in the work force is similar to that of Naota, the average annual earnings of women who work full time ranges from a low of 50 percent to a high of 90 percent of the average annual earnings of men who work full time.

### Argument Breakdown

**Given that:** Among full-time workers, women's average earnings are 80 percent of men's.

**How can it be that:** Among all workers, women's average earnings are only 65 percent of men's?

**Evaluate:** The second figure includes part-time workers; the first does not. Put numbers on it. Say full-time men average $50,000 and full-time women $40,000 (80 percent). If many more women than men work part time at low pay, adding the part-timers drags the women's average down much more than the men's. The gap widens from 80 to 65.

**Goal:** Find a difference between men and women in the group the first study left out: part-time workers.

### Choice Notes

**(A) No Impact.** A gap that has grown over 30 years does not explain why two measurements taken now give different numbers.

**(B) Too Weak.** Women in identical jobs earning about the same as men is about full-time pay. It does not explain why including all workers lowers the ratio.

**(C) Opposite.** More women in well-paid full-time jobs would raise women's averages. That works against a lower all-worker figure.

**(D) Correct.** A larger share of women work part time, and part-timers earn less. Adding them pulls the women's overall average down more than the men's, which turns 80 percent into 65.

**(E) Out of Scope.** Figures from other countries cannot explain the gap between two figures about Naota.

## PT108-S3-Q17 | Paradox EXCEPT | E

**Modelled on:** PT113-S2-Q17 (three-and-one split), PT101-S3-Q14 (one frame for every choice).

> Radial keratotomy (RK), a surgery that is designed to reshape the cornea so that light focuses correctly on the retina, is supposed to make eyeglasses or contact lenses that correct for nearsightedness unnecessary. Yet a study of patients who have undergone RK shows that some of them still need to wear glasses or contact lenses.
>
> Each of the following, if true, would help to resolve the apparent discrepancy in the information above EXCEPT:
>
> (A) As the eye heals from an operation to correct nearsightedness, it may in fact overcorrect, causing the person to be farsighted.
> (B) The more severe a patient’s nearsightedness, the less effective the corneal reshaping of RK will be in correcting the problem.
> (C) Occasionally an RK patient’s eyes may heal differently, causing a difference in the two eyes’ visual acuity that can be overcome only with corrective lenses.
> (D) RK patients who originally suffered from only mild nearsightedness may, if the cornea does not heal evenly, develop an astigmatism that requires corrective lenses.
> (E) Those who choose to undergo RK tend to be as nearsighted before this operation as those who choose not to undergo RK.

### Argument Breakdown

**Given that:** RK is supposed to make glasses and contacts unnecessary for nearsighted people.

**How can it be that:** Some RK patients still need glasses or contacts?

**Evaluate:** Frame: "This patient still needs lenses because..." Working answers describe a way the surgery can fall short or create a new vision problem. The answer will say nothing about what happens to RK patients' eyes.

**Goal:** Four choices give a reason some patients still need lenses. The answer will not.

### Choice Notes

**(A) Helps Explain.** The eye overcorrects while healing and becomes farsighted. That patient now needs lenses for a new problem.

**(B) Helps Explain.** RK works less well on severe nearsightedness. Severely nearsighted patients may be left needing lenses.

**(C) Helps Explain.** Uneven healing leaves the two eyes different, which only lenses can fix.

**(D) Helps Explain.** Uneven healing can cause astigmatism that requires lenses, even in patients who started with mild nearsightedness.

**(E) Correct.** This compares RK patients with people who skipped surgery, before surgery. Being equally nearsighted beforehand says nothing about why some patients need lenses afterward.

## PT109-S3-Q1 | Paradox | B

**Modelled on:** PT148-S3-Q11 (difference between groups), PT154-S1-Q6 (one concrete mechanism).

> North American eastern white cedars grow both on cliff faces and in forests. Cedars growing on exposed cliff faces receive very few nutrients, and rarely grow bigger than one-tenth the height of cedars growing in forests, where they benefit from moisture and good soil. Yet few eastern white cedars found in forests are as old as four hundred years, while many on cliff faces are more than five hundred years old.
>
> Which one of the following, if true, most helps to explain the difference in the ages of the cedars on cliff faces and those in forests?
>
> (A) The conditions on cliff faces are similar to those in most other places where there are few tall trees.
> (B) In areas where eastern white cedars grow, forest fires are relatively frequent, but fires cannot reach cliff faces.
> (C) Trees that are older than a few hundred years start to lose the protective outer layer of their bark.
> (D) The roots of cedars on cliff faces lodge in cracks in the cliff, and once the roots are so large that they fill a crack, the tree is unable to grow any taller.
> (E) Eastern white cedar wood is too soft to be used for firewood or modern buildings, but it is occasionally used to make furniture.

### Argument Breakdown

**Given that:** Forest cedars get water and good soil and grow ten times taller than cliff cedars.

**How can it be that:** Cliff cedars often live past 500 years while few forest cedars reach 400?

**Evaluate:** Better growing conditions do not guarantee a longer life. Something must cut forest trees' lives short or protect cliff trees. Ask what kills trees: fire, logging, disease, storms. We need one that hits the forest but not the cliff.

**Goal:** Find a threat in the forest that cliff cedars escape.

### Choice Notes

**(A) No Impact.** Cliffs resembling other sparse places tells us nothing about why trees there live longer than forest trees.

**(B) Correct.** Fires are frequent where these cedars grow, and they reach forests but not cliff faces. Forest cedars burn before they get old; cliff cedars survive.

**(C) Applies to Both.** Losing bark after a few hundred years would happen to old cedars wherever they grow. It does not separate cliff from forest.

**(D) Half Scope.** This explains why cliff cedars stay short. The puzzle is why they live longer, and height limits say nothing about age.

**(E) Too Weak.** Occasional furniture use might lead to some cutting, but the choice does not say forest cedars are cut more than cliff cedars. It does not explain the age gap.

## PT110-S2-Q5 | Paradox | B

**Modelled on:** PT148-S3-Q11 (explain a difference with a difference), PT144-S3-Q5 (match the definitions).

> Many elementary schools have recently offered computer-assisted educational programs. Students’ reactions after several years have been decidedly mixed. Whereas students have found computers very useful in studying arithmetic, they have found them of little help in studying science, and of no help at all with their reading and writing skills.
>
> Which one of the following, if true, most helps to explain the students’ mixed reactions?
>
> (A) Students in these schools began reading and doing arithmetic before learning to use computers.
> (B) Of the disciplines and skills mentioned, the exactness of arithmetic makes it most suitable to computer-assisted education.
> (C) Many elementary school teachers are reluctant to use computer technology in their classrooms.
> (D) Young students are more likely to maintain interest in training programs that use the newest computers and video graphics than in those that do not.
> (E) The elementary schools have offered more computer-assisted programs in reading and writing than in arithmetic and science.

### Argument Breakdown

**Given that:** Schools offered computer-assisted programs to students.

**How can it be that:** Students found them very useful for arithmetic, of little help in science, and no help in reading and writing?

**Evaluate:** The same computers produced different results by subject. So the answer has to be something about the subjects. What does arithmetic have that computers suit and reading and writing lack? Clear right-or-wrong answers that a program can check.

**Goal:** Find a feature of arithmetic that makes it better suited to computers than the other subjects.

### Choice Notes

**(A) No Impact.** Students started both reading and arithmetic before computers. That applies to two of the subjects alike, so it cannot explain the split.

**(B) Correct.** Arithmetic's exactness makes it the best fit for computer-assisted learning. That gives a subject-level difference that matches the ranking: arithmetic most useful, the others less.

**(C) Applies to Both.** Teacher reluctance would affect every subject. It does not explain why one subject did well and the others did not.

**(D) No Distinction.** Interest in the newest computers applies to all programs equally.

**(E) Deepens Paradox.** More programs in reading and writing should have made computers *more* helpful there, not less.

## PT111-S3-Q12 | Paradox EXCEPT | E

**Modelled on:** PT120-S3-Q15 (EXCEPT: name the routes), PT126-S4-Q5 (groups not fair to compare).

> Despite the fact that antilock brakes are designed to make driving safer, research suggests that people who drive cars equipped with antilock brakes have more accidents than those who drive cars not equipped with antilock brakes.
>
> Each of the following, if true, would help resolve the apparent discrepancy described above except:
>
> (A) Most cars equipped with antilock brakes are, on average, driven more carelessly than cars not equipped with antilock brakes.
> (B) Antilock brakes malfunction more often than regular brakes.
> (C) Antilock brakes require expensive specialized maintenance to be even as effective as unmaintained regular brakes.
> (D) Most people who drive cars equipped with antilock brakes do not know how to use those brakes properly.
> (E) Antilock brakes were designed for safety in congested urban driving, but accidents of the most serious nature take place on highways.

### Argument Breakdown

**Given that:** Antilock brakes are designed to make driving safer.

**How can it be that:** Drivers of cars with antilock brakes have more accidents?

**Evaluate:** Two routes. Either the brakes fail to deliver their safety in practice (malfunction, poor maintenance, misuse), or the drivers differ (more careless). Either would let the design be safe while the cars still crash more.

**Goal:** Four choices give one of those routes. The answer will not explain *more* accidents.

### Choice Notes

**(A) Helps Explain.** Antilock cars are driven more carelessly. The drivers, not the brakes, account for the extra accidents.

**(B) Helps Explain.** Antilock brakes fail more often than regular brakes. Brakes that fail cause accidents.

**(C) Helps Explain.** Without expensive maintenance, antilock brakes are worse than regular brakes. Many owners will skip that maintenance.

**(D) Helps Explain.** Most drivers do not know how to use antilock brakes properly, so they do not get the safety benefit.

**(E) Correct.** This says where the brakes were meant to help and where the worst accidents happen. Highways affect cars with either kind of brake, and "most serious" is about severity, not number. It does not explain why antilock cars have *more* accidents.

## PT111-S4-Q12 | Paradox | C

**Modelled on:** PT126-S4-Q5 (compare with the untreated group), PT101-S2-Q18 (low baseline).

> Most doctors recommend that pregnant women eat a nutritious diet to promote the health of their babies. However, most babies who are born to women who ate nutritious diets while pregnant still develop at least one medical problem in their first year.
>
> Which one of the following, if true, does most to resolve the apparent discrepancy in the information above?
>
> (A) Women who regularly eat a nutritious diet while pregnant tend to eat a nutritious diet while breast-feeding.
> (B) Most of the babies born to women who did not eat nutritious diets while pregnant develop no serious medical problems later in childhood.
> (C) Babies of women who did not eat nutritious diets while pregnant tend to have more medical problems in their first year than do other babies.
> (D) Medical problems that develop in the first year of life tend to be more serious than those that develop later in childhood.
> (E) Many of the physicians who initially recommended that pregnant women consume nutritious diets have only recently reaffirmed their recommendation.

### Argument Breakdown

**Given that:** Doctors recommend nutritious diets during pregnancy to promote babies' health.

**How can it be that:** Most babies of mothers who ate nutritious diets still have a medical problem in their first year?

**Evaluate:** The recommendation does not promise a problem-free first year. It only claims the diet *helps*. Ask, "Compared to what?" If babies of mothers who did not eat well have even more problems, then the diet does help.

**Goal:** Find a comparison showing babies of well-fed mothers do better than the others.

### Choice Notes

**(A) No Impact.** Diet while breast-feeding does not explain why the recommended pregnancy diet seems not to work.

**(B) Deepens Paradox.** If babies of poorly fed mothers have no serious problems later in childhood, diet looks even less important.

**(C) Correct.** Babies of mothers without a nutritious diet have more first-year problems. Most babies have some problem either way, but the diet lowers the number. The recommendation is still sound.

**(D) No Impact.** How serious first-year problems are compared with later ones does not show the diet helps.

**(E) No Impact.** Doctors repeating their advice is not evidence that the advice works.

## PT112-S1-Q13 | Paradox | C

**Modelled on:** PT141-S4-Q15 (breadcrumbs), PT152-S4-Q23 (state the exact gap).

> When astronomers observed the comet Schwassman-Wachmann 3 becoming 1,000 times brighter in September 1995, they correctly hypothesized that its increased brightness was a result of the comet's breaking up—when comets break up, they emit large amounts of gas and dust, becoming visibly brighter as a result. However, their observations did not reveal comet Schwassman-Wachmann 3 actually breaking into pieces until November 1995, even though telescopes were trained on it throughout the entire period.
>
> Which one of the following, if true, most helps to resolve the apparent conflict in the statements above?
>
> (A) Comets often do not emit gas and dust until several weeks after they have begun to break up.
> (B) The reason comets become brighter when they break up is that the gas and dust that they emit refract light.
> (C) Gas and dust can be released by cracks in a comet even if the comet is not broken all the way through.
> (D) The amount of gas and dust emitted steadily increased during the period from September through November.
> (E) The comet passed close to the sun during this period and the gravitational strain caused it to break up.

### Argument Breakdown

**Given that:** The comet brightened in September because it was breaking up, since breaking up releases bright gas and dust.

**How can it be that:** Astronomers watching all along did not see it break into pieces until November?

**Evaluate:** "Breaking up" and "breaking into pieces" may not be the same moment. If a comet can crack and leak gas before it actually splits apart, the brightening and the visible split can be two months apart.

**Goal:** Find a way gas and dust could be released before the comet split into pieces.

### Choice Notes

**(A) Opposite.** If gas and dust come weeks *after* breakup begins, the comet should have split before it brightened. That runs the timeline the wrong way.

**(B) No Impact.** Why gas and dust brighten a comet does not explain the gap between brightening and the visible split.

**(C) Correct.** Cracks can release gas and dust without the comet breaking all the way through. The comet began cracking in September, brightened, and split into pieces in November.

**(D) Too Weak.** A steady increase in gas and dust does not say why the pieces were not visible until November.

**(E) Half Scope.** This explains why the comet broke up. It does not explain the delay between the brightening and the visible split.

## PT112-S3-Q1 | Paradox | D

**Modelled on:** PT139-S1-Q15 (plan backfired), PT154-S1-Q6 (one concrete mechanism).

> Scientists agree that ingesting lead harms young children. More lead paint remains in older apartment buildings than newer ones because the use of lead paint was common until only two decades ago. Yet these same scientists also agree that laws requiring the removal of lead paint from older apartment buildings will actually increase the amount of lead that children living in older apartment buildings ingest.
>
> Which one of the following, if true, most helps to resolve the apparent discrepancy in the scientists' beliefs?
>
> (A) Lead-free paints contain substances that make them as harmful to children as lead paint is.
> (B) The money required to finance the removal of lead paint from apartment walls could be spent in ways more likely to improve the health of children.
> (C) Other sources of lead in older apartment buildings are responsible for most of the lead that children living in these buildings ingest.
> (D) Removing lead paint from walls disperses a great deal of lead dust, which is more easily ingested by children than is paint on walls.
> (E) Many other environmental hazards pose greater threats to the health of children than does lead paint.

### Argument Breakdown

**Given that:** Lead harms children, and old apartment buildings have more lead paint.

**How can it be that:** Scientists think laws requiring removal of that paint will *increase* how much lead those children ingest?

**Evaluate:** The removal itself must create a new route for lead. Paint sealed on a wall is hard to swallow. Scraping or sanding it off makes dust and chips that spread through the apartment.

**Goal:** Find a way the removal process puts more lead within children's reach.

### Choice Notes

**(A) Out of Scope.** Lead-free paint being harmful in other ways does not explain more *lead* being ingested.

**(B) No Impact.** Better uses for the money say nothing about lead levels after removal.

**(C) Too Weak.** Other sources supplying most of the lead might make removal pointless, but not harmful. It does not explain an *increase*.

**(D) Correct.** Removing the paint spreads lead dust, which children swallow more easily than paint on a wall. The law causes the very exposure it aims to prevent.

**(E) Out of Scope.** Other hazards being worse does not explain how removing lead paint increases lead intake.

## PT113-S3-Q11 | Paradox | E

**Modelled on:** PT148-S1-Q12 (plan didn't work, three shapes), PT140-S1-Q20 (keep the locked-in gain).

> Several thousand years ago, people in what is now North America began to grow corn, which grows faster and produces more food per unit of land than do the grains these people had grown previously. Corn is less nutritious than those other grains, however, and soon after these people established corn as their staple grain crop, they began having nutrition-related health problems. Yet the people continued to grow corn as their staple grain, although they could have returned to growing the more nutritious grains.
>
> Which one of the following, if true, most helps to explain why the people mentioned continued to grow corn as their staple grain crop?
>
> (A) The variety of corn that the people relied on as their staple grain produced more food than did the ancestors of that variety.
> (B) Modern varieties of corn are more nutritious than were the varieties grown by people in North America several thousand years ago.
> (C) The people did not domesticate large animals for meat or milk, either of which could supply nutrients not provided by corn.
> (D) Some of the grain crops that could have been planted instead of corn required less fertile soil in order to flourish than corn required.
> (E) The people discovered some years after adopting corn as their staple grain that a diet that supplemented corn with certain readily available nongrain foods significantly improved their health.

### Argument Breakdown

**Given that:** Corn is less nutritious than the old grains, and it caused nutrition-related health problems.

**How can it be that:** People kept growing corn as their staple even though they could have gone back to the old grains?

**Evaluate:** Corn still has its advantage: it grows faster and yields more food per acre. If people found a way to fix the nutrition problem without giving up corn, they would keep the extra food and solve the health issue. That beats switching back.

**Goal:** Find a way to solve corn's nutrition problem while keeping corn.

### Choice Notes

**(A) Irrelevant Comparison.** Comparing this corn to its ancestors does not explain why people preferred it to the other grains despite the health problems.

**(B) Out of Scope.** Modern corn being more nutritious has nothing to do with people thousands of years ago.

**(C) Deepens Paradox.** Without meat or milk, people had no other way to make up for corn's poor nutrition. That makes sticking with corn harder to explain.

**(D) Deepens Paradox.** If some alternatives grew in poorer soil, switching back would have been even easier.

**(E) Correct.** People learned that adding readily available nongrain foods fixed their health. They could keep corn's higher yield and solve the nutrition problem at the same time.

## PT114-S2-Q2 | Paradox | D

**Modelled on:** PT154-S1-Q6 (one concrete mechanism), PT120-S1-Q6 (the answer can undercut the first expectation).

> One way kidney stones can form is when urine produced in the kidneys is overly concentrated with calcium or oxalate. Reducing dietary calcium has been thought, therefore, to decrease the likelihood that calcium will concentrate and form additional stones. Oddly enough, for many people the chances of recurrence are decreased by increasing calcium intake.
>
> Which one of the following, if true, most helps to resolve the apparent discrepancy described above?
>
> (A) Laboratory studies on animals with kidney stones reveal that they rarely get additional stones once calcium supplements are added to the diet.
> (B) Increasing dietary oxalate while reducing dietary calcium does not reduce the chances of kidney stone recurrence.
> (C) Kidney stone development is sometimes the result of an inherited disorder that can result in excessive production of calcium and oxalate.
> (D) Increasing calcium intake increases the amount of calcium eliminated through the intestines, which decreases the amount to be filtered by the kidneys.
> (E) Some kidney stones are composed of uric acid rather than a combination of calcium and oxalate.

### Argument Breakdown

**Given that:** Kidney stones can form when urine has too much calcium, so cutting dietary calcium was expected to prevent new stones.

**How can it be that:** For many people, eating *more* calcium lowers the chance of new stones?

**Evaluate:** The expectation assumes more calcium in the diet means more calcium in the urine. What if extra calcium leaves the body another way, before reaching the kidneys? Then eating more could put *less* through the kidneys.

**Goal:** Find a path by which extra dietary calcium reduces the calcium the kidneys handle.

### Choice Notes

**(A) Restates Paradox.** Animals on calcium supplements rarely get new stones. That repeats the surprising result without saying why it happens.

**(B) Unclear Impact.** Adding oxalate while cutting calcium is a different change from adding calcium. It does not explain why more calcium helps.

**(C) No Impact.** An inherited cause of stones does not explain why extra calcium lowers recurrence.

**(D) Correct.** More dietary calcium means more calcium leaves through the intestines and less is left for the kidneys to filter. The urine is less concentrated, so fewer stones form.

**(E) Out of Scope.** Stones made of uric acid are not the calcium-oxalate stones the stimulus is about.

## PT115-S2-Q3 | Paradox | A

**Modelled on:** PT152-S4-Q23 (state the exact gap), PT154-S1-Q6 (one concrete mechanism).

> Letter to the editor: Allowing everyone to voice personal views can have the effect of inhibiting some from voicing their concerns. Thus, allowing unrestricted free speech really inhibits free speech.
>
> Which one of the following, if true, does most to justify the apparently contradictory conclusion above?
>
> (A) When free speech is unrestricted, many people will be shocked by the power of the views of others and thereby become afraid to voice their own concerns.
> (B) When there is unrestricted free speech, there will be a greater number of diverse views expressed, but the views expressed will be potentially offensive to many people.
> (C) Since unrestricted free speech can be offensive, free speech should be restricted when the pain that it causes is great.
> (D) Claiming that unrestricted free speech inhibits free speech is like claiming that increasing someone's salary makes the person poorer.
> (E) When free speech is unrestricted, people offended by the views of others are likely to voice their disagreement, leading toward a resolution of conflict.

### Argument Breakdown

**Given that:** Unrestricted free speech lets everyone voice their views.

**How can it be that:** Unrestricted free speech inhibits free speech?

**Evaluate:** The first sentence gives the hint: letting everyone speak can stop *some* people from speaking. We need a mechanism. If some views are so forceful or intimidating that other people go quiet, total freedom produces less actual speech from them.

**Goal:** Find how unrestricted speech makes some people stop speaking.

### Choice Notes

**(A) Correct.** People shocked by others' powerful views become afraid to voice their own. Unrestricted speech has silenced them, which is exactly the claim.

**(B) Too Weak.** More views, some offensive. Being offended is not the same as being silenced, so this does not show speech is inhibited.

**(C) Out of Scope.** This recommends restricting speech. A recommendation does not explain how unrestricted speech inhibits speech.

**(D) Opposite.** The salary comparison suggests the claim is absurd. That undermines the conclusion we are supposed to justify.

**(E) Opposite.** Offended people speak up in reply. That is more speech, not less.

## PT115-S4-Q5 | Paradox | C

**Modelled on:** PT126-S4-Q5 (another route to the same result), PT140-S1-Q20 (rule out inside the stimulus).

> Lactose, a sugar found in milk, aids in the absorption of calcium, which in turn is required for bone repair. In addition to there being shortages of milk in tropical areas, inhabitants of these areas lose the ability to absorb lactose, unlike people from nontropical areas. Yet inhabitants of tropical areas have no more problems with bone repair than do people who inhabit nontropical areas.
>
> Which one of the following, if true, most helps to resolve the apparent paradox described above?
>
> (A) People living in tropical areas periodically take tablets containing lactose when there are shortages of milk.
> (B) Milk consumption has fallen in both tropical and nontropical areas.
> (C) The abundant sunlight in tropical areas causes the human body to produce vitamin D naturally, which aids in the absorption of calcium.
> (D) Consumption of dairy products other than milk has risen slightly in tropical areas.
> (E) The extent to which people living in tropical areas lose the ability to absorb lactose depends on a genetic predisposition.

### Argument Breakdown

**Given that:** Lactose helps calcium absorption, which bone repair needs. People in tropical areas have little milk and lose the ability to absorb lactose.

**How can it be that:** They have no more trouble with bone repair than people elsewhere?

**Evaluate:** Lactose is one way to absorb calcium. If tropical people have another way, they would not need it. Think about what the tropics have plenty of.

**Goal:** Find another source of help absorbing calcium that tropical people have.

### Choice Notes

**(A) No Impact.** Lactose tablets do not help people who have lost the ability to absorb lactose.

**(B) Applies to Both.** Lower milk consumption everywhere does not separate tropical from nontropical people.

**(C) Correct.** Abundant sunlight makes the body produce vitamin D, which helps absorb calcium. Tropical people get calcium absorption another way.

**(D) Too Weak.** A slight rise in other dairy products does not fix calcium absorption for people who cannot absorb lactose, and "slightly" could not close the gap.

**(E) No Impact.** Genetics deciding how much the ability is lost does not explain how bone repair stays normal.

