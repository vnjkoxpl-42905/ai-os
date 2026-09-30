# Facts, Rules, and What Follows

Conditional reasoning uses general rules to work out what must follow from the information given.

First, understand each statement. Then decide whether you are **applying a rule to a case** or **linking rules to make a new rule**. Those moves produce different kinds of conclusions.

In an inference question, accept all the given statements as true. Your job is to prove what else must be true, without adding a fact or a connection the statements never supplied.


## 01 | Facts establish information about a case

**Definition:** A fact tells us something is true about a particular case or group. A fact given in the question is treated as true. A fact you infer must be proved from the given information.

**Concrete example:** “Mira is trained.” That tells us something about Mira. It does not tell us whether other people are trained, whether Mira has a badge, or how training relates to badges.

A fact can be negative: **“Niko does not have a badge.”** It can describe a group: **“Some staff members are trained.”** That last statement establishes at least one trained staff member, without establishing that every staff member is trained.

<!-- FACT-SCOPE -->

**Try it:** Some reports are missing pages. Does at least one report with missing pages exist? Must every report be missing pages?

**Worked answer:** At least one report is missing pages. The statement establishes that such a report exists, but does not establish that every report is missing pages. Other reports could be complete.

Both facts and rules are accepted as true when they are given. Sort them by their role: a case fact establishes that a condition is true of someone or something; a conditional rule connects that condition to another.

“Requires approval” and “has received approval” are different facts. A requirement can be established without establishing that it was fulfilled. Keep the complete claim when you read or shorten it.

## 02 | Rules connect conditions

**Definition:** A conditional rule tells us what must be true if a condition is met. It applies to every case that meets that condition. A rule connects conditions; it does not identify a particular case that meets them.

**Concrete example:** “Everyone who is trained has a badge.” This connects being trained with having a badge. It says that every trained person actually has a badge.

<!-- RULE-PARTS -->

Let **T** mean “is trained” and **B** mean “has a badge.” We can write the rule as **T → B**. The arrow points from the starting condition to the required result. If T is true of someone, B must be true of that same person.

Being trained is **sufficient** to establish that someone has a badge: it is enough to trigger this rule. Having a badge is **necessary** for being trained under this rule: a trained person cannot lack a badge.

That does not mean training is the only way to get a badge. It also does not establish that anyone is trained. The rule could hold even if no one met its starting condition.

### Rules can connect different kinds of claims

A rule can tell us what someone **should** do or what they **may** do. That is different from telling us what they actually did.

Suppose **every damaged item should be inspected**. If this item is damaged, it should be inspected. We cannot conclude it has been inspected. But “has not been inspected” is not the same as “it is not true that it should be inspected.” An inspection could be overdue.

Suppose **a visitor may enter the archive only if the visitor has a badge**. A badge is necessary for permission to enter. The rule is **May enter → Has a badge**. Without a badge, the visitor does not have permission to enter under this rule. Having a badge alone does not establish permission; another requirement might still apply.

<!-- MODALITY -->

The rule concerns permission. It does not prove that someone physically cannot enter without permission. Keep the same kind of claim throughout your reasoning: a requirement stays a requirement, advice stays advice, and permission stays permission.

**Try it:** Every damaged item should be inspected. This damaged item has not been inspected. Does that violate the rule? What can you conclude about what should happen?

**Worked answer:** The item should be inspected. Its not having been inspected does not contradict the claim about what should happen. The rule does not state that every required inspection actually occurs.

## 03 | Apply a rule to the same case

**Definition:** Applying a rule means finding an established fact that satisfies the rule's starting condition, then concluding the required result for **the same case**.

### Apply the rule forward

**Given fact:** Mira is trained.

**Rule:** Everyone who is trained has a badge.

**Match:** “Mira is trained” satisfies the rule's condition, “is trained.”

**Therefore:** Mira has a badge.

**Why:** The rule covers every trained person, including Mira. We have proved a new fact about Mira. We have not made a claim about everyone who has a badge.

<!-- APPLY-SEQUENCE -->

**Try it:** Every file marked confidential requires restricted storage. This file is marked confidential. What follows? Does the rule alone establish that a confidential file exists?

**Worked answer:** This file requires restricted storage. The fact establishes that this particular file is confidential. The rule alone establishes a requirement for any confidential file, without establishing that any such file exists.

### When the fact denies the result

A different fact calls for a different move. Suppose **Niko does not have a badge**, and the same rule says **everyone who is trained has a badge**.

If Niko were trained, the rule would require Niko to have a badge. That would contradict the given fact. So **Niko is not trained**.

**Given fact:** Niko does not have a badge.

**Rule:** Trained → Has a badge.

**Match:** The fact denies the required result. Restate the rule as **No badge → Not trained**.

**Therefore:** Niko is not trained.

**Why:** Training cannot be present while the rule's required result is absent. This is the **contrapositive**: reverse the arrow and negate both complete conditions.

The contrapositive states the same rule. It does not deny the original rule, and it is not the unsupported reversal **Has a badge → Trained**.

Keep qualifiers inside the conditions. For **Damaged → Should be inspected**, the contrapositive starts with “it is not true that it should be inspected” and concludes “not damaged.” Whether the item has actually been inspected is a different claim.

<!-- TWO-MOVES -->

### Four facts, one unchanged rule

The rule is **Trained → Has a badge**. Read what each fact actually matches before choosing a conclusion.

### Fact 1: The person is trained

**Match:** The original starting condition is met.

**What follows:** The person has a badge.

**Why:** Every trained person has a badge under this rule. Apply it to this person.

### Fact 2: The person has no badge

**Match:** The required result is absent. This meets the contrapositive's starting condition.

**What follows:** The person is not trained.

**Why:** A trained person without a badge would contradict the rule.

### Fact 3: The person has a badge

**Match:** We have only the original result. The rule does not say that everyone with a badge is trained.

**What follows:** Whether this person is trained remains unknown.

**Why:** An untrained visitor with a badge fits the rule. A trained person with a badge also fits it.

### Fact 4: The person is not trained

**Match:** The original starting condition is absent. The rule only guarantees badges for trained people.

**What follows:** Whether this person has a badge remains unknown.

**Why:** An untrained person could have a badge or lack one. Both situations fit the rule.

The forbidden combination is **trained, but no badge**. All other combinations can fit the rule. A rule rules out that combination; a fact tells us which condition we actually have.

Now explore those same moves with a different rule: **Every late application requires special approval.** First identify the supplied fact. Then see whether it triggers the original rule, triggers its contrapositive, or leaves the other condition open.

<!-- FACT-LAB -->

<!-- CASE-GRID -->

<!-- POP-QUIZ-1 -->

**Try it:** Every confidential file requires restricted storage. This file does not require restricted storage. What follows? What if all you know is that it does require restricted storage?

**Worked answer:** If it does not require restricted storage, it is not confidential. That is the contrapositive. If it does require restricted storage, its confidentiality remains unknown. A nonconfidential file could require restricted storage for another reason.

You do not have to write every contrapositive automatically. If the fact clearly meets the original starting condition, apply that rule. If the fact denies its result, or a connection is difficult to see, a contrapositive can make the supported move clear.

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

## 05 | Link rules to produce a new rule

**Definition:** Linking rules means matching the result of one rule to the starting condition of another, so that together they establish a **new conditional rule**.

### Link the rules without adding a case

**First rule:** Every late application requires special approval.

**Second rule:** Every application requiring special approval needs a supervisor's signature.

**Match:** “Requires special approval” is the result of the first rule and the starting condition of the second. The whole idea matches.

**New rule:** Submitted late → Requires special approval → Needs a supervisor's signature.

**Therefore:** Every late application needs a supervisor's signature.

**Why:** Consider any application that is late. The first rule requires approval; that satisfies the second rule's condition, which requires a signature. This proves the general connection **Late → Needs signature**. It does not establish that any application was late.

### Add a fact and use the whole chain

**Given fact:** Application J was submitted late.

**Rules:** Submitted late → Requires special approval → Needs a supervisor's signature.

**Therefore:** Application J requires special approval and needs a supervisor's signature.

The rules-only conclusion was a new **if-then rule**. Adding J's fact lets us apply it and conclude something about **J**. Do not silently add a case when the information gives you only rules.

<!-- TWO-OUTPUTS -->

You can also use the chain's contrapositive: **Does not need signature → Does not require approval → Was not late**. A fact denying the final result can be carried backward through both connections.

<!-- CHAIN-LAB -->

### The whole middle idea must match

“Requires special approval” and “has received special approval” are not the same condition. A requirement can remain unfulfilled. A rule ending in the first phrase cannot be linked to one starting in the second unless another statement connects them. Shared words are not enough; match the complete claim, including qualifiers and negation.

**Try it:** Every late application requires special approval. Every application that has received special approval has a supervisor's signature. Does a late application necessarily have a supervisor's signature? Explain the missing connection.

**Worked answer:** No. A late application requires approval, but it may not have received it. The second rule applies to applications that have received approval. Nothing says the late application's requirement has been fulfilled.

### A contrapositive can uncover the match

Suppose these two rules are given:

**Rule 1:** Trained → Has a badge.

**Rule 2:** Not trained → Requires supervision.

“Trained” and “not trained” are opposite ideas in the same position: both are starting conditions. They do not look like a chain yet. Take the contrapositive of the first rule:

**Restated rule 1:** No badge → Not trained.

Now “not trained” is the result of that restatement and the starting condition of rule 2. We can link them:

**New chain:** No badge → Not trained → Requires supervision.

**New conditional:** Anyone without a badge requires supervision.

Again, that is a general rule. It does not prove that someone lacks a badge. If a separate fact says Niko lacks a badge, then we can apply the chain and conclude that Niko requires supervision.

<!-- HIDDEN-CHAIN -->

When opposite ideas sit in the same position, try a contrapositive to expose a match. When the match is already visible, use it directly. The point is to find a supported connection, not to produce extra diagrams for their own sake.

## 06 | Shared beginnings do not create a chain

Use only the rules given in this new example. Rules from earlier examples do not carry over.

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

Use only the information given in each problem. For each problem, write what follows and name the move. If a proposed conclusion is not guaranteed, explain a situation that would make it false while keeping the given statements true.

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
