# Facts, Rules, and What Follows

A rule tells you what follows **if a condition is met**. A fact tells you what is true in a particular case. Put them together, and you can prove something new.

Suppose a program has this policy: **Every application submitted after the deadline requires special approval.** One application was submitted after the deadline. That application requires special approval. We have a rule, a fact that fits its starting condition, and a conclusion the rule guarantees.

Change the fact, and the conclusion can change. An application that requires special approval need not have been late. It could require approval for another reason. The policy gives one route to that requirement, not the only route.

<!-- FACT-LAB -->

## 01 | Start with the fact you actually have

The rule applies to every late application. The fact identifies one of those applications. We can now apply the rule to that particular case.

**Rule:** Every application submitted after the deadline requires special approval.

**Fact:** This application was submitted after the deadline.

**What follows:** This application requires special approval.

The rule alone does not tell us that any applications were submitted late. We needed the fact to establish that we had a case to which the rule applies. A conditional rule can be true even if nothing meets its starting condition.

Now give the two complete ideas short names. Let **L** mean “submitted after the deadline” and **R** mean “requires special approval.” The notation saves space; it should not change the meaning.

`L -> R` means: if L is true, R must be true.

**Try it:** Every file marked confidential requires restricted storage. This file is marked confidential. What follows? Does the rule alone establish that a confidential file exists?

**Worked answer:** This file requires restricted storage. The fact establishes that this particular file is confidential. The rule alone establishes a requirement for any confidential file, without establishing that any such file exists.

## 02 | Use the rule forward, or use its contrapositive

There are two ways to use the application policy. A late application must require approval. An application that does **not** require approval cannot have been late. If it had been late, the policy would require approval, contradicting the fact we were given.

<!-- TWO-MOVES -->

**Forward:** Submitted late -> Requires approval.

**Contrapositive:** Does not require approval -> Was not submitted late.

The contrapositive states the same rule from its other end. Reverse the direction **and negate both complete ideas**. Simply reversing the arrow would say that requiring approval proves lateness. The original policy never said that.

Simply negating both ideas without reversing would also add something: “not late -> does not require approval.” An on-time application could require approval for a different reason. That situation does not break the policy.

The only combination the original rule rules out is **late, but does not require approval**. The other three combinations can fit the rule.

<!-- CASE-GRID -->

**Try it:** Every confidential file requires restricted storage. This file does not require restricted storage. What follows? What if all you know is that it does require restricted storage?

**Worked answer:** If it does not require restricted storage, it is not confidential. That is the contrapositive. If it does require restricted storage, its confidentiality remains unknown. A nonconfidential file could require restricted storage for another reason.

## 03 | Link rules when the whole middle idea matches

Add a second policy: **Every application that requires special approval needs a supervisor's signature.** The first rule gets us to “requires special approval.” The second starts at that exact idea. We can carry the application through both rules.

**First rule:** Submitted late -> Requires special approval.

**Second rule:** Requires special approval -> Needs a supervisor's signature.

**Combined rule:** Submitted late -> Needs a supervisor's signature.

In letters, the pattern is `L -> R` and `R -> S`, so `L -> S`. If a particular application was late, both requirements follow for that application. Without a fact establishing a late application, we still have a combined rule rather than proof that a late application exists.

You can also work backward through the combined rule. If an application does **not** need a supervisor's signature, it cannot require special approval under the second policy. If it does not require special approval, it cannot have been late under the first policy.

**Backward chain:** Does not need signature -> Does not require approval -> Was not late.

<!-- CHAIN-LAB -->

### Matching a word is not enough

“Requires special approval” and “has received special approval” both mention approval. They describe different conditions. A requirement can exist before anyone fulfills it. You cannot link a rule ending in the first phrase to a rule starting in the second unless another statement connects them.

This is why you should diagram **complete ideas**, not isolated words. Keep words such as “requires,” “has,” “should,” and “may” inside the condition they qualify.

**Try it:** Every late application requires special approval. Every application that has received special approval has a supervisor's signature. Does a late application necessarily have a supervisor's signature? Explain the missing connection.

**Worked answer:** No. A late application requires approval, but it may not have received it. The second rule applies to applications that have received approval. Nothing says the late application's requirement has been fulfilled.

## 04 | A shared starting point does not create a chain

Compare a different pair of rules: **Every late application requires special approval. Every late application needs a supervisor's signature.** Both rules start at “late.” Neither starts where the other ends.

<!-- SHARED-TRIGGER -->

If a fact tells us an application was late, we can apply **both** rules to it. That application requires approval and needs a signature. But we cannot conclude that every application requiring approval needs a signature. An on-time application might require approval for another reason without needing a signature.

Likewise, two rules that end at the same idea do not connect their starting conditions. If confidential files require restricted storage and medical files require restricted storage, a confidential file need not be a medical file. Restricted storage could cover both types separately.

Before joining two arrows, find the destination of the first and the starting condition of the second. They must match, including any negation or qualifier. If they do not match, keep the rules separate or see whether a valid contrapositive produces a match.

**Try it:** Every member of a review panel has training. Every member of that panel has a security badge. Must everyone with training have a security badge? What follows if Dana is a panel member?

**Worked answer:** Training alone does not guarantee a badge. A trained person could be outside the panel. Because Dana is a panel member, both rules apply to Dana: Dana has training and a security badge.

## 05 | Keep the kind of claim intact

A rule can tell us what someone **should** do or what they **may** do. That is different from telling us what they actually did.

Suppose **every damaged item should be inspected**. If this item is damaged, it should be inspected. We cannot conclude it has been inspected. If an item should not be inspected, then it is not damaged under that rule. But “has not been inspected” is not the same as “should not be inspected.” An inspection could be overdue.

Suppose **a visitor may enter the archive only if the visitor has a badge**. A badge is necessary for permission to enter. The rule is **May enter -> Has a badge**. Without a badge, the visitor does not have permission to enter under this rule. Having a badge alone does not establish permission; another requirement might still apply.

<!-- MODALITY -->

The rule concerns permission. It does not prove that someone physically cannot enter without permission. Keep the same kind of claim throughout your reasoning: a requirement stays a requirement, advice stays advice, and permission stays permission.

**Try it:** Every damaged item should be inspected. This damaged item has not been inspected. Does that violate the rule? What can you conclude about what should happen?

**Worked answer:** The item should be inspected. Its not having been inspected does not contradict the claim about what should happen. The rule does not state that every required inspection actually occurs.

## 06 | Negate the whole condition

Some conditions contain more than one part. Suppose **a document may be released only if it has been reviewed AND authorized**. Permission requires both parts. If either part is missing, the combined requirement is not satisfied.

**Rule:** May be released -> Reviewed AND authorized.

**Contrapositive:** Not reviewed OR not authorized -> May not be released.

To negate “reviewed AND authorized,” you only need at least one failure. You do not need both parts to fail. “Not both” does not mean “neither.”

Now suppose **a visitor may enter only if the visitor has a badge OR an invitation**. This requirement allows either route, including both. To fail the entire requirement, the visitor must have neither.

**Rule:** May enter -> Has badge OR has invitation.

**Contrapositive:** No badge AND no invitation -> May not enter.

<!-- NEGATION -->

Negating a compound condition changes **AND to OR**, or **OR to AND**, while negating each part. For the original AND requirement, one missing part is enough. For the original OR requirement, both routes must be missing.

**Try it:** A document may be released only if it has been reviewed and authorized. It has been reviewed but not authorized. What follows? Does the contrapositive require us to conclude it was not reviewed?

**Worked answer:** The document may not be released. Missing authorization is enough to fail the combined requirement. We do not conclude that review is missing too; the fact says review occurred.

## 07 | Decide what the information lets you do

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

**Worked answer:** File K is not confidential. Use the contrapositive: does not require restricted storage -> not confidential.

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
