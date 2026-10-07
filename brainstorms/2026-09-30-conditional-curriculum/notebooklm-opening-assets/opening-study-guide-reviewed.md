# LSAT Logic Foundations: Conditional Reasoning Study Guide

## 1. Part 1: What a Conditional Is (The Guarantee)

### 1.1 Concept Explanation
A conditional statement is a strict logical rule. It guarantees that when one condition is met, another condition must be met as well. It leaves no room for exceptions.

Consider the statement: "All dogs are mammals." If you know that Luna is a dog, you automatically know she is a mammal. You do not need any additional facts about her. The rule covers every dog, and Luna falls inside that group.

We can reframe the statement as: "If something is a dog, then it is a mammal." In logical notation, this relationship is written with an arrow:

`Dog -> Mammal`

Read the arrow as "if this is true, then that must be true."

The arrow records the logical relationship. By itself, it does not establish physical cause and effect or a sequence in time. A conditional rule does not prove its starting condition actually exists in reality. It only tells you what must follow if that condition occurs. Finally, the rule `Dog -> Mammal` permits mammals that are not dogs. It also does not require the two sets to be different sizes.

### 1.2 Visual Description
*Visual Caption: A visual diagram featuring a large outer box labeled "Mammals" with a smaller box labeled "Dogs" placed entirely inside it, demonstrating that every dog fits completely within the mammal category while leaving space for non-dog mammals outside the smaller box.*

### 1.3 Worked Example
* **Rule:** All dogs are mammals (`Dog -> Mammal`).
* **Given Fact:** Luna is a dog.
* **Step 1:** Check if the given fact meets the starting condition of the rule. Luna is a dog, so the starting condition (`Dog`) is satisfied.
* **Step 2:** Apply the rule's guarantee. Because the starting condition is met, the outcome on the right side of the arrow must follow.
* **Conclusion:** Luna is a mammal.

### 1.4 Independent Practice Task
**Prompt:** All volunteers wear badges. Ari is a volunteer. What does the rule guarantee about Ari?

<details>
<summary>See Solution</summary>

**Solution:** Ari wears a badge.
* **Step 1 (Setup):** Translate the rule into a logical statement: `Volunteer -> Wears a badge`.
* **Step 2 (Application):** The problem states that Ari is a volunteer, which satisfies the starting condition.
* **Step 3 (Conclusion):** Because the rule covers every volunteer without exception, it strictly guarantees that Ari wears a badge.
</details>

### 1.5 Core Takeaway
A conditional tells you what must follow when its condition is met.

---

## 2. Part 2: Why Direction Matters

### 2.1 Concept Explanation
Logical direction is critical on the LSAT. For the forward inference taught here, read from the sufficient condition to the necessary condition. Later lessons will add other valid ways to use the same rule. Reversing the arrow fundamentally changes the claim being made.

Using the rule `Dog -> Mammal`, knowing that Luna is a dog guarantees she is a mammal. However, if you only know that Luna is a mammal, you cannot conclude that she is a dog; she could be a cat or another animal. The rule allows for mammals that are not dogs.

Understanding logical direction directly impacts your performance across various LSAT question types:
* **Must Be True:** You may apply a conditional rule to a matching fact to find what must follow. Later lessons cover additional valid inferences.
* **Flaw:** Arguments often commit errors by reversing a rule and assuming that satisfying the right side proves the left side.
* **Sufficient Assumption:** You must identify the precise missing logical link that connects the premise directionally to the conclusion.

### 2.2 Visual Description
*Visual Caption: A diagram illustrating a strict one-way path with a single arrow pointing exclusively from left to right, showing why knowing the left side gives the right side, while knowing the right side alone does not establish the left.*

### 2.3 Comparison Table

| What we know | What we can conclude | Why |
| :--- | :--- | :--- |
| Luna is a dog. | Luna is a mammal. | The rule covers every dog. |
| Luna is a mammal. | We don't know whether Luna is a dog. | Other mammals are allowed. |

### 2.4 Independent Practice Task
**Prompt:** Every volunteer wears a badge. Ari wears a badge. Does that establish that Ari is a volunteer? Explain your answer using the rule.

<details>
<summary>See Solution</summary>

**Solution:** No. 
* **Reasoning:** The rule (`Volunteer -> Wears a badge`) requires all volunteers to wear badges, but it does not state that *only* volunteers wear badges. Non-volunteers (such as paid staff members) are permitted by the rule to wear badges as well. Knowing Ari wears a badge moves backward against the arrow, which proves nothing about his volunteer status.
</details>

### 2.5 Core Takeaway
Follow the direction the rule gives you. Before accepting a conclusion, check that the rule actually reaches it.

---

## 3. Part 3: Sufficient Means Enough

### 3.1 Concept Explanation
In conditional logic, the term **sufficient** means "enough." 

The sufficient condition always sits on the left side of the arrow. It functions as the trigger for the rule. The moment the sufficient condition is fulfilled, the outcome on the right side is fully guaranteed.

Consider this rule: "If a student earns full credit, that student passes the assignment."
`Earns full credit -> Passes`

Here, earning full credit is sufficient to guarantee passing. If Maya earns full credit, that fact alone is enough to conclude that she passes. However, saying full credit is "enough" does not mean it is "the only way." A student might earn less than full credit and still pass through other criteria. Sufficient means enough to guarantee the result, not that no other paths exist.

### 3.2 Visual Description
*Visual Caption: An illustration of a light switch labeled "Sufficient Trigger" on the left side, connected by a left-to-right wire to an illuminated light bulb on the right labeled "Necessary Result," showing that flipping the switch guarantees the light turns on.*

### 3.3 Worked Example
* **Rule:** `Earns full credit -> Passes`
* **Scenario:** Maya earned full credit on her assignment.
* **Analysis:** Earning full credit is the sufficient condition on the left. Because Maya met this condition, the trigger is activated.
* **Deduction:** Maya's passing status is completely guaranteed.

### 3.4 Independent Practice Task
**Prompt:** If a person wins the race, that person receives a medal. Which condition is enough to guarantee the other? Then write the arrow.

<details>
<summary>See Solution</summary>

**Solution:** 
* **Sufficient Condition:** Winning the race is enough to guarantee receiving a medal.
* **Logical Arrow:** `Wins -> Receives a medal`
* **Reasoning:** Winning triggers the medal outcome. The rule does not state that winning is the only way to receive a medal, but it is sufficient to guarantee one.
</details>

### 3.5 Core Takeaway
The sufficient condition goes on the left. Meeting it is enough to guarantee the right.

---

## 4. Part 4: Necessary Means Required

### 4.1 Concept Explanation
In conditional logic, the term **necessary** means "required."

The necessary condition always sits on the right side of the arrow. It represents the element that must be present whenever the sufficient condition occurs.

Revisiting the academic rule: `Earns full credit -> Passes`. Under this rule, passing is necessary (required) for having earned full credit. You cannot earn full credit and fail. However, knowing that someone passed does not prove they earned full credit.

Consider an architectural rule: "Entering the archive requires a pass."
`Enters the archive -> Has a pass`

Here, having a pass is required for entry, so it goes on the right side. However, simply possessing a pass does not guarantee that a person actually enters the archive.

### 4.2 Visual Description
*Visual Caption: A visual representation of a secure archive door requiring entry, featuring a mandatory keycard slot positioned on the right side of the doorframe, emphasizing that the keycard is required to gain access.*

### 4.3 Role Comparison Table

| Sufficient | Necessary |
| :--- | :--- |
| Enough to guarantee the other condition. | Required whenever the sufficient condition is met. |
| Goes on the left side of the arrow. | Goes on the right side of the arrow. |
| If I have this, what must follow? | What must I have in order for the left side to be true? |

### 4.4 Independent Practice Task
**Prompt:** Every finalist receives an invitation. Identify the sufficient condition and the necessary condition. Does receiving an invitation establish that someone is a finalist?

<details>
<summary>See Solution</summary>

**Solution:**
* **Sufficient Condition:** Being a finalist (goes on the left).
* **Necessary Condition:** Receiving an invitation (goes on the right).
* **Diagram:** `Finalist -> Receives invitation`
* **Establishes Finalist Status?** No. Receiving an invitation does not establish that someone is a finalist. The rule requires finalists to receive invitations, but it permits non-finalists to receive invitations as well.
</details>

### 4.5 Core Takeaway
Sufficient is enough. Necessary is required. Required means right.

---

## 5. Part 5: Group 1: Find the Sufficient Idea

### 5.1 Concept Explanation
To translate natural language into conditional logic, you must recognize indicator words. Group 1 indicators introduce the **sufficient idea**, placing it on the left side of the arrow.

**Group 1 Indicator Words:** `if`, `when`, `where`, `all`, `the only`, `every`, `any`.

When translating, avoid relying on sentence word order. Instead, apply the golden rule: **"What complete idea is the indicator referring to?"**

For example, consider these two sentences:
1. "If a student revises the essay, the student receives feedback."
2. "A student receives feedback if the student revises the essay."

In both cases, "if" refers to "revises the essay." Therefore, regardless of sentence order, the translation remains identically:
`Revises essay -> Receives feedback`

### 5.2 Sentence Translation Table

| Sentence | What the indicator refers to | Translation |
| :--- | :--- | :--- |
| Every volunteer wears a badge. | Every volunteer. | `Volunteer -> Wears a badge` |
| Any applicant who submits late pays a fee. | Any applicant who submits late. | `Applicant submits late -> Pays a fee` |
| When the alarm sounds, the staff evacuate. | When the alarm sounds. | `Alarm sounds -> Staff evacuate` |
| Where there is smoke, there is fire. | Where there is smoke. | `Smoke -> Fire` |

*Note: You must capture complete ideas. In the applicant example, translating "applicant" alone is incorrect; the rule specifically targets an applicant **who submits late**.*

### 5.3 Read "The Only"
Examine the sentence: "The only people admitted are members."
Ask: "The only *what*?" Answer: "The only *people admitted*." 
Because "the only" modifies "people admitted," that complete idea is the sufficient condition:

`Admitted -> Member`

This statement guarantees that everyone admitted is a member; it does not claim that every member is admitted.

### 5.4 Visual Description
*Visual Caption: A visual graphic showing a spotlight focused directly on the left box of a conditional diagram labeled "Sufficient Idea," highlighting how Group 1 indicators point straight to the left side.*

### 5.5 Independent Practice Task
**Prompt:** For each sentence, identify the indicator, ask what it refers to, and write the complete rule arrow:
1. All registered guests receive a wristband.
2. A report is reviewed if it is submitted before noon.
3. The only vehicles permitted inside are electric vehicles.

<details>
<summary>See Solution</summary>

**Solution:**
1. **Indicator:** `All` (refers to "registered guests").
   * **Target Idea:** Registered guest
   * **Translation:** `Registered guest -> Receives wristband`
2. **Indicator:** `If` (refers to "submitted before noon").
   * **Target Idea:** Submitted before noon
   * **Translation:** `Submitted before noon -> Reviewed`
3. **Indicator:** `The only` (refers to "vehicles permitted inside").
   * **Target Idea:** Vehicle permitted inside
   * **Translation:** `Vehicle permitted inside -> Electric vehicle`
</details>

### 5.6 Core Takeaway
Find the indicator's target. For Group 1, that complete idea goes left.

---

## 6. Part 6: Group 2: Find What's Required

### 6.1 Concept Explanation
Group 2 indicators introduce the **necessary idea**. The complete idea introduced by a Group 2 indicator belongs on the right side of the arrow.

**Group 2 Indicator Words:** `only`, `only if`, `only when`, `only where`, `always`, `requires`, `must`.

Always ask: **"What is the indicator referring to?"**

Consider the sentence: "A student enters the archive only if the student has a pass."
Ask: "Only if *what*?" Answer: "Only if the student has a pass." Possessing a pass is required:

`Enters archive -> Has a pass`

### 6.2 "If" vs. "Only If" Comparison Table

| Sentence | Rule Translation | Logical Meaning |
| :--- | :--- | :--- |
| A student enters if the student has a pass. | `Has a pass -> Enters` | Having a pass is **sufficient** (enough) to enter. |
| A student enters only if the student has a pass. | `Enters -> Has a pass` | Having a pass is **necessary** (required) to enter. |

Changing a single word from "if" to "only if" completely reverses what the sentence guarantees.

### 6.3 Indicator Location and Word Comparison
Required elements do not always appear at the end of a sentence. For instance, in "A pass is required for entry," asking "What is required?" yields "A pass." Thus, the required element appears first in the sentence, but still belongs on the right side of the diagram: `Enters -> Has a pass`.

Compare the indicators "only" and "the only":
* **"Only members are admitted."** 
  * Indicator: `Only` (refers to "members"). Being a member is required. 
  * Translation: `Admitted -> Member`
* **"The only people admitted are members."** 
  * Indicator: `The only` (refers to "people admitted"). People admitted is the sufficient condition. 
  * Translation: `Admitted -> Member`

Both sentences express the exact same logical relationship, but their indicators point to different parts of the sentence structure.

### 6.4 Group 2 Sentence Translation Table

| Sentence | Required idea | Translation |
| :--- | :--- | :--- |
| A finalist must attend the interview. | Is required to attend the interview. | `Finalist -> Required to attend interview` |
| Approval requires a signature. | Has a signature. | `Approved -> Has signature` |
| A review occurs only when a complaint is filed. | A complaint is filed. | `Review occurs -> Complaint filed` |
| The service operates only where a station is available. | A station is available. | `Service operates -> Station available` |
| A finalist always receives an invitation. | Receives an invitation. | `Finalist -> Receives invitation` |

### 6.5 Visual Description
*Visual Caption: A diagram displaying a target box positioned on the right side labeled "Necessary/Required Idea" marked with a distinct checkmark, illustrating that Group 2 indicators place their target on the right.*

### 6.6 Independent Practice Task
**Prompt:** Identify what is required, then write the rule for each sentence:
1. Only registered guests receive wristbands.
2. A permit is required for construction.
3. A student graduates only if the student completes the project.

<details>
<summary>See Solution</summary>

**Solution:**
1. **Indicator:** `Only` (refers to "registered guests").
   * **Required Idea:** Registered guest
   * **Translation:** `Receives wristband -> Registered guest`
2. **Indicator:** `Required` (refers to "a permit").
   * **Required Idea:** Has permit
   * **Translation:** `Construction -> Has permit`
3. **Indicator:** `Only if` (refers to "completes the project").
   * **Required Idea:** Completes project
   * **Translation:** `Graduates -> Completes project`
</details>

### 6.7 Core Takeaway
For Group 2, the required idea goes right. Ask what the indicator refers to, then check the meaning of your arrow against the sentence.

### Read “must” in context

In the interview sentence, “must” states an obligation. It tells us what a finalist is required to do. It does not establish that the finalist actually attends. In other sentences, “must” can express logical necessity. Keep the complete meaning when you diagram.
