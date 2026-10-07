# Facts, Rules, and What Follows

Conditional reasoning uses rules to work out what must follow from the information given.

Treat the given statements as true. Your job is to find what else must be true.

Before you combine statements, identify what each one says. A **fact** describes a case. A **rule** tells you what must follow if its condition is met.

A **conclusion** is what the statements prove. It can follow from a fact and a rule, or from a valid chain of rules.


## 01 | Facts state what is true

A fact tells you what is true in a particular case. **“Application J was submitted after the deadline”** tells us something about Application J. It does not tell us when other applications were submitted.

A fact can also describe more than one case. **“Some applications were submitted after the deadline”** establishes that at least one late application exists. It does not establish that every application was late.

For now, keep those claims separate from anything you might infer. “J was late” is given. Whether J requires special approval is a different claim. We need a rule connecting lateness to that requirement before we can prove it.

<!-- FACT-SCOPE -->

**Try it:** Some reports are missing pages. Does at least one report with missing pages exist? Must every report be missing pages?

**Worked answer:** At least one report is missing pages. The statement establishes that such a report exists, but does not establish that every report is missing pages. Other reports could be complete.

Keep the whole description. “Requires special approval” is different from “has received special approval.” Each could be a fact about an application, but a requirement does not establish that it has been fulfilled.


## 02 | Rules state a requirement

A rule tells you what must follow if its condition is met. Consider this policy: **Every application submitted after the deadline requires special approval.**

The rule has two complete parts. **Submitted after the deadline** is the condition. **Requires special approval** is the required result. The rule connects them in that order.

<!-- RULE-PARTS -->

Let **L** mean “submitted after the deadline” and **R** mean “requires special approval.” Then we can write the same rule as **L → R**. The arrow points from the condition to the required result. If L is true, R must be true.

Being late is **sufficient** to establish the approval requirement. That means lateness is enough to trigger this rule. Requiring approval is **necessary** for a late application. That means a late application cannot lack that requirement.

Those words describe this connection. They do not say that approval is the only requirement, or that lateness is the only reason approval could be required.

The rule alone does not establish that any application was late. It tells us what is required of any late application, even if no applications were submitted late.

### Keep the kind of claim intact

A rule can tell us what someone **should** do or what they **may** do. That is different from telling us what they actually did.

Suppose **every damaged item should be inspected**. If this item is damaged, it should be inspected. We cannot conclude it has been inspected. But “has not been inspected” is not the same as “it is not true that it should be inspected.” An inspection could be overdue.

Suppose **a visitor may enter the archive only if the visitor has a badge**. A badge is necessary for permission to enter. The rule is **May enter → Has a badge**. Without a badge, the visitor does not have permission to enter under this rule. Having a badge alone does not establish permission; another requirement might still apply.

<!-- MODALITY -->

The rule concerns permission. It does not prove that someone physically cannot enter without permission. Keep the same kind of claim throughout your reasoning: a requirement stays a requirement, advice stays advice, and permission stays permission.

**Try it:** Every damaged item should be inspected. This damaged item has not been inspected. Does that violate the rule? What can you conclude about what should happen?

**Worked answer:** The item should be inspected. Its not having been inspected does not contradict the claim about what should happen. The rule does not state that every required inspection actually occurs.

## 03 | Apply one rule to a fact

Now combine a rule with a fact that meets its condition.

**Rule:** Every application submitted after the deadline requires special approval.

**Fact:** Application J was submitted after the deadline.

**Conclusion:** Application J requires special approval.

The fact supplies the condition. The rule supplies the connection to the result. Together, they prove the conclusion.

**Try it:** Every file marked confidential requires restricted storage. This file is marked confidential. What follows? Does the rule alone establish that a confidential file exists?

**Worked answer:** This file requires restricted storage. The fact establishes that this particular file is confidential. The rule alone establishes a requirement for any confidential file, without establishing that any such file exists.

There are two ways to use the application policy. A late application must require approval. An application that does **not** require approval cannot have been late. If it had been late, the policy would require approval, contradicting the fact we were given.

<!-- TWO-MOVES -->

**Forward:** Submitted late → Requires approval.

**Contrapositive:** Does not require approval → Was not submitted late.

The contrapositive states the same rule from its other end. Reverse the direction **and negate both complete ideas**. Simply reversing the arrow would say that requiring approval proves lateness. The original policy never said that.

Keep any qualifier inside the condition when you negate it. For “damaged → should be inspected,” the contrapositive begins with “it is not true that it should be inspected,” and concludes “not damaged.” Whether the item has actually been inspected is a separate claim.

Simply negating both ideas without reversing would also add something: “not late → does not require approval.” An on-time application could require approval for a different reason. That situation does not break the policy.

The only combination the original rule rules out is **late, but does not require approval**. The other three combinations can fit the rule.

<!-- FACT-LAB -->

<!-- CASE-GRID -->

<!-- POP-QUIZ-1 -->

**Try it:** Every confidential file requires restricted storage. This file does not require restricted storage. What follows? What if all you know is that it does require restricted storage?

**Worked answer:** If it does not require restricted storage, it is not confidential. That is the contrapositive. If it does require restricted storage, its confidentiality remains unknown. A nonconfidential file could require restricted storage for another reason.

## 04 | Negate the whole requirement

Some conditions contain more than one part. Suppose **a document may be released only if it has been reviewed AND authorized**. Permission requires both parts. If either part is missing, the combined requirement is not satisfied.

**Rule:** May be released → Reviewed AND authorized.

**Contrapositive:** Not reviewed OR not authorized → May not be released.

To negate “reviewed AND authorized,” you only need at least one failure. You do not need both parts to fail. “Not both” does not mean “neither.”

Now suppose **a visitor may enter only if the visitor has a badge OR an invitation**. This requirement allows either route, including both. To fail the entire requirement, the visitor must have neither.

**Rule:** May enter → Has badge OR has invitation.

**Contrapositive:** No badge AND no invitation → May not enter.

<!-- NEGATION -->

Negating a compound condition changes **AND to OR**, or **OR to AND**, while negating each part. For the original AND requirement, one missing part is enough. For the original OR requirement, both routes must be missing.

**Try it:** A document may be released only if it has been reviewed and authorized. It has been reviewed but not authorized. What follows? Does the contrapositive require us to conclude it was not reviewed?

**Worked answer:** The document may not be released. Missing authorization is enough to fail the combined requirement. We do not conclude that review is missing too; the fact says review occurred.

## 05 | Connect rules at a matching middle

Add a second policy: **Every application that requires special approval needs a supervisor's signature.** The first rule gets us to “requires special approval.” The second starts at that exact idea. We can carry the application through both rules.

**First rule:** Submitted late → Requires special approval.

**Second rule:** Requires special approval → Needs a supervisor's signature.

**Combined rule:** Submitted late → Needs a supervisor's signature.

In letters, the pattern is L → R and R → S, so L → S. If a particular application was late, both requirements follow for that application. Without a fact establishing a late application, we still have a combined rule rather than proof that a late application exists.

You can also work backward through the combined rule. If an application does **not** need a supervisor's signature, it cannot require special approval under the second policy. If it does not require special approval, it cannot have been late under the first policy.

**Backward chain:** Does not need signature → Does not require approval → Was not late.

<!-- CHAIN-LAB -->

### Matching a word is not enough

“Requires special approval” and “has received special approval” both mention approval. They describe different conditions. A requirement can exist before anyone fulfills it. You cannot link a rule ending in the first phrase to a rule starting in the second unless another statement connects them.

This is why you should diagram **complete ideas**, not isolated words. Keep words such as “requires,” “has,” “should,” and “may” inside the condition they qualify.

**Try it:** Every late application requires special approval. Every application that has received special approval has a supervisor's signature. Does a late application necessarily have a supervisor's signature? Explain the missing connection.

**Worked answer:** No. A late application requires approval, but it may not have received it. The second rule applies to applications that have received approval. Nothing says the late application's requirement has been fulfilled.

## 06 | Shared beginnings do not create a chain

Compare a different pair of rules: **Every late application requires special approval. Every late application needs a supervisor's signature.** Both rules start at “late.” Neither starts where the other ends.

<!-- SHARED-TRIGGER -->

<!-- POP-QUIZ-2 -->

If a fact tells us an application was late, we can apply **both** rules to it. That application requires approval and needs a signature. But we cannot conclude that every application requiring approval needs a signature. An on-time application might require approval for another reason without needing a signature.

Likewise, two rules that end at the same idea do not connect their starting conditions. If confidential files require restricted storage and medical files require restricted storage, a confidential file need not be a medical file. Restricted storage could cover both types separately.

Before joining two arrows, find the destination of the first and the starting condition of the second. They must match, including any negation or qualifier. If they do not match, keep the rules separate or see whether a valid contrapositive produces a match.

**Try it:** Every member of a review panel has training. Every member of that panel has a security badge. Must everyone with training have a security badge? What follows if Dana is a panel member?

**Worked answer:** Training alone does not guarantee a badge. A trained person could be outside the panel. Because Dana is a panel member, both rules apply to Dana: Dana has training and a security badge.

## 07 | Choose the move and test the claim

Start by separating **facts about a case** from **rules about cases**. Then choose the move the information supports.

| What you have | The move | What to check |
| --- | --- | --- |
| A fact meeting a rule's starting condition | Apply the rule forward | Does the whole fact match the whole condition? |
| A fact denying a rule's required result | Use the contrapositive | Did you reverse and negate both complete ideas? |
| Two rules with a matching middle condition | Link the rules | Are direction, negation, and qualifiers identical? |
| Only the required result, or only the absence of the starting condition | Leave the other side open | Could another explanation fit the rule? |

When an inference seems tempting, try to build a case in which the statements are true and the proposed conclusion is false. If you can, the conclusion is not guaranteed. The counterexamples above work this way: an on-time application can still require approval; a requirement can remain unfulfilled; a trained person can be outside the panel.

Keep the scope of the fact too. **Some applications were submitted late. Every late application requires special approval. Therefore, some applications require special approval.** We cannot change “some” to “all.” The rule covers every late case, but the fact establishes only at least one. Other applications could be on time and require no special approval.

## 08 | Mix the moves

For each problem, write what follows and name the move. If a proposed conclusion is not guaranteed, explain a situation that would make it false while keeping the given statements true.

**Practice 1:** Every confidential file requires restricted storage. File K does not require restricted storage. What follows?

**Worked answer:** File K is not confidential. Use the contrapositive: does not require restricted storage → not confidential.

**Practice 2:** Every late application requires special approval. Every application requiring special approval needs a supervisor's signature. Application J was late. What follows?

**Worked answer:** Application J requires special approval and needs a supervisor's signature. Apply the first rule to the fact, then carry its result through the second rule.

**Practice 3:** Every panel member has training. Every panel member has a security badge. Lee has training. Must Lee have a badge?

**Worked answer:** No. Lee could be a trained person outside the panel who has no badge. The two rules share a starting condition. Training alone does not establish that Lee meets it.

**Practice 4:** A document may be released only if it has been reviewed and authorized. Document M has not been reviewed. What follows? Must it also lack authorization?

**Worked answer:** Document M may not be released. One missing requirement is enough. Whether it has authorization remains open; it could have authorization but lack review.

## 09 | Take this into your assigned work

Do the **conditional-diagramming drills first**, then move to the **LSAT questions**. In the drills, write the complete conditions before shortening them. Check your arrow and its contrapositive. When two rules appear, look for an exact match before combining them.

In the LSAT questions, separate the facts from the rules before choosing an answer. Your job is to identify what the statements guarantee. If an answer reverses the rule, drops a qualifier, or turns a requirement into an accomplished action, test it with a counterexample.

Keep this question nearby: **What do I actually have, and which move does it support?**
