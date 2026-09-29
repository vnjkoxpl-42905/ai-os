# Some, Most, and All

A quantity statement tells us whether a claim holds for at least one member of a group, for more than half, or for every member. **Some**, **most**, and **all** give us different guarantees. Before we combine quantity statements, we need to know what each one proves and what it leaves open.

We need to know two things about each statement: what it guarantees, and what it still leaves open. Once that is clear, we can combine statements without asking an arrow to do more than it can.

## Some guarantees at least one

Imagine a shelf with eight books. I tell you that **some of the books are hardcover**. How many hardcover books must there be?

At least **one**. There could be one, four, or all eight. “Some” rules out zero. It does not rule out “most” or “all.”

![Eight books showing that one hardcover book and eight hardcover books both satisfy some.](./assets/some-books.svg)

This is easy to miss because in ordinary conversation “some” often suggests “some, but not all.” On the LSAT, that extra phrase is not part of the statement. If all eight books are hardcover, it is still true that some are hardcover.

**Try it:** If some books on the shelf are hardcover, could seven be hardcover? Could none be hardcover?

<details><summary>Check your answer</summary>

Seven could be hardcover. None could not. “Some” guarantees at least one and tells us nothing more about the count.

</details>

There is one more feature of “some” that matters later. If some books are hardcover, then some hardcover things are books. Both sentences describe the same overlap.

```text
Books  ←some→  Hardcover
```

The double arrow means we may read a **some** statement in either direction. It does not turn the sentence into an **all** statement.

## Most guarantees more than half

Now I tell you that **most of the eight books are hardcover**. We need at least **five** hardcover books. Four would be exactly half, and half is not most. Five, six, seven, or eight could satisfy the sentence.

![Eight books showing that five hardcover books and eight hardcover books both satisfy most.](./assets/most-books.svg)

Notice that all eight could still be hardcover. “Most” does not tell us that an exception exists.

**Try it:** If most of the eight books are hardcover, must some of them be hardcover? Must any be paperback?

<details><summary>Check your answer</summary>

At least five are hardcover, so **some are hardcover**. No paperback book is required. All eight could be hardcover.

</details>

Here is where the direction of the statement matters. From “most books are hardcover,” we know that **some hardcover things are books**. We cannot say that **most hardcover things are books**. The original sentence counts the books on this shelf. The reversed sentence would count every hardcover thing, including things outside that group.

```text
Books  ─most→  Hardcover
Hardcover  ←some→  Books
```

The first arrow gives the majority claim. The second line is the overlap that the majority guarantees. When we read a most statement backward, the word becomes **some**.

## All leaves no exception

If **all eight books are hardcover**, every book on the shelf is hardcover. One paperback on that shelf would make the statement false.

![Eight books showing that all eight must be hardcover to satisfy all.](./assets/all-books.svg)

An all statement gives us a rule: **if it is a book on this shelf, then it is hardcover**.

```text
Book on this shelf  →  Hardcover
Not hardcover       →  Not a book on this shelf
```

The second line is the contrapositive. Both lines go with the same rule. We cannot turn the first line around and conclude that every hardcover thing is a book on this shelf.

**Try it:** You pick up a paperback. What does the rule tell you? What if you pick up a hardcover notebook?

<details><summary>Check your answer</summary>

The paperback cannot be one of these books. The hardcover notebook tells us nothing about whether it is one of these books. Being hardcover is required of the books, but it is not enough to identify one.

</details>

There is a small qualification. “All A are B” gives a rule about A. By itself, it does not tell us that any A exist. When we already know the group exists, all also guarantees most and some.

## Put the three statements side by side

The same shelf can help us see the whole range.

![For eight existing books: some permits one through eight hardcover, most permits five through eight, and all requires eight.](./assets/book-quantity-ranges.svg)

Read the implications in one direction:

```text
ALL  →  MOST  →  SOME       (when the group exists)
```

If all eight books are hardcover, then most are, and some are. If only “some” is given, all eight **could** be hardcover, but we cannot conclude that they **are**. Keep the distinction between a possible situation and a required one.

## Carry a claim through an all rule

Now we can combine statements. Suppose **some library books are mysteries** and **all mysteries are fiction**. We have at least one book that is a mystery. The all rule applies to every mystery, including that one. So **some library books are fiction**.

```text
Library books  ←some→  Mysteries  →  Fiction
Library books  ←some→  Fiction
```

The all arrow points **away from** the mystery group we reached. That is why the chain works. If the second sentence said only “most mysteries are fiction,” the mystery books we found could be among the exceptions.

The same reasoning preserves the first quantity word:

| First statement | Rule | What follows |
|---|---|---|
| Some library books are mysteries. | All mysteries are fiction. | Some library books are fiction. |
| Most library books are mysteries. | All mysteries are fiction. | Most library books are fiction. |
| All library books are mysteries. | All mysteries are fiction. | All library books are fiction. |

**Try it:** “Most library books are mysteries. All fiction is mystery.” Can we conclude that most library books are fiction?

<details><summary>Check your answer</summary>

No. The all arrow goes from fiction to mystery. We cannot start at mystery and travel backward to fiction.

</details>

## Two majorities of the same group must meet

Suppose a club has ten members. **Most members study law**, and **most members work part time**. Each “most” needs at least six of the ten members. Those two sets cannot fit inside the club without sharing at least two people.

![Ten club members. Six study law, six work part time, and at least two do both.](./assets/club-majority-overlap.svg)

So **some law students work part time**. We can also say **some part-time workers study law**. These are the same people, described from opposite sides of a some statement.

```text
Club members  ─most→  Law students
Club members  ─most→  Part-time workers
Law students  ←some→  Part-time workers
```

The two most arrows begin with the **same group**. That shared starting point is what forces the overlap. The conclusion is **some**, not most. We know the two groups meet; we do not know what fraction of either group lies in the overlap.

**Try it:** If most club members study law and most club members work part time, could the two groups of members be completely separate?

<details><summary>Check your answer</summary>

No. Two separate majorities would require more members than the club has. At least one member must have both traits.

</details>

## A second way two most statements can work

Here is a different comparison. **Most debate team members are seniors**, but **most seniors are not on the debate team**. The seniors on the team are more than half of the team and less than half of the seniors. The same overlap takes up a larger share of the team than of the senior class. Therefore, **there are more seniors than debate team members**.

![An example in which six of ten debate team members are seniors, while six of twenty seniors are on the team.](./assets/group-size-comparison.svg)

The numbers in the picture are one possible case. The conclusion follows from the two majority claims, not from those particular numbers.

## Similar chains can leave a gap

Two some statements need not describe the same person or thing:

```text
Some volunteers speak Spanish.
Some Spanish speakers are trained.
```

The trained Spanish speakers could all be people who do not volunteer. We cannot conclude that any volunteers are trained.

Replacing the second “some” with “most” does not fix the gap. The Spanish-speaking volunteers could sit in the untrained minority. Even two most statements chained through different starting groups do not automatically produce a new majority claim.

Before drawing a conclusion, ask: **Am I carrying a known group through an all rule? Or do two majorities count the same group?** If neither is true, check whether the groups could miss each other.

## The moves to keep

| What you have | What you may conclude |
|---|---|
| Some A are B | Some B are A |
| Most A are B | Some A are B, and some B are A |
| All A are B | A → B, and not B → not A |
| Some/most/all A are B; all B are C | The same first quantity of A are C |
| Most A are B; most A are C | Some B are C |

These are the useful moves. The arrows show exactly where each one is allowed to go.

## Short drill: diagram, combine, decide

Here are five statements about one volunteer program. **Volunteer**, **Spanish speaker**, **trained person**, **weekend worker**, and **student** name groups of people. Treat each sentence as true.

1. Some volunteers speak Spanish.
2. All Spanish speakers are trained.
3. Most volunteers work weekends.
4. Most volunteers are students.
5. Most weekend workers are trained.

First, diagram each statement. Then answer these without looking below:

1. Which two statements prove that **some volunteers are trained**?
2. Which two statements prove that **some students work weekends**?
3. Do statements 3 and 5 prove that **most volunteers are trained**? Explain the gap or draw a counterexample.
4. Can you write either valid **some** conclusion in the reverse order?

<details><summary>Show the diagrams and worked answers</summary>

```text
1. Volunteers       ←some→  Spanish speakers
2. Spanish speakers →       Trained people
3. Volunteers       ─most→  Weekend workers
4. Volunteers       ─most→  Students
5. Weekend workers  ─most→  Trained people
```

**1. Statements 1 and 2.** At least one volunteer speaks Spanish. Every Spanish speaker is trained. That volunteer is trained, so **some volunteers are trained**.

**2. Statements 3 and 4.** Both majorities count the volunteers. The weekend workers and students must share at least one volunteer. So **some students work weekends**.

**3. No.** Statement 3 says most volunteers work weekends. Statement 5 counts all weekend workers, a different group. The volunteers who work weekends could be among the untrained weekend workers. Nothing requires most volunteers to be trained.

**4. Yes.** A some statement describes an overlap in either direction: **some trained people are volunteers**, and **some weekend workers are students**.

</details>
