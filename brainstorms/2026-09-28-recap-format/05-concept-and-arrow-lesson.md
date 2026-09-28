# Some, Most, and All: What the Arrows Let You Infer

The words *some*, *most*, and *all* tell you how much of a group fits a description. First learn the amount each word guarantees. Then learn which conclusions you can carry forward, reverse, or combine.

## First, learn the ranges

Imagine **10 cookies**. We are asking how many of them are chocolate.

![A chart showing the possible number of chocolate cookies out of ten: some allows one through ten, most allows six through ten, and all requires ten.](./assets/quantity-ranges.svg)

| Sentence | What it guarantees | What it still allows |
|---|---|---|
| **Some cookies are chocolate.** | At least 1 of 10 is chocolate. | Anywhere from 1 to 10 could be chocolate. |
| **Most cookies are chocolate.** | More than half are chocolate: at least 6 of 10. | Anywhere from 6 to 10 could be chocolate. |
| **All cookies are chocolate.** | Exactly 10 of 10 are chocolate. | No non-chocolate cookie is possible. |

“Some” often suggests “some, but not all” in ordinary conversation. That suggestion is not part of the LSAT claim. **Some can include most or all.** “Most” can include all too.

These are ranges of *possible* counts. They are not all counts you have *proved*. If you are told “some,” you have proved at least one. You have **not** proved most or all.

![Three rows of cookies illustrating one valid example each: one chocolate cookie for some, six for most, and ten for all.](./assets/cookie-examples.svg)

The cookie rows are examples. The range chart shows every count each word permits.

## Which statement is strong enough to prove another?

![A one-way diagram in which all guarantees most, and most guarantees some.](./assets/quantity-implications.svg)

If a group has at least one member, **all → most → some**. Every stronger statement proves the weaker ones. The reverse does not follow:

- “Some cookies are chocolate” could describe all 10, but it does not prove all 10 are chocolate.
- “Most cookies are chocolate” could describe all 10, but it does not prove all 10 are chocolate.
- “Some cookies are chocolate” does not prove that most are chocolate. One chocolate cookie would make “some” true and “most” false.

**Possible is not guaranteed.** That is the distinction to keep in mind whenever you move between these words.

## The arrows work differently

Let **A** be one group and **B** another. An arrow describes what the sentence lets you say about their relationship. These are quantity arrows, except for the ordinary conditional arrow under “all.”

![The three quantity arrow patterns: some works in both directions as some; most gives some in reverse; all gives a one-way conditional arrow and its contrapositive.](./assets/quantity-arrows.svg)

### Some: the overlap works in both directions

If **some A are B**, at least one thing belongs to both groups. That same thing proves **some B are A**. You can turn the sentence around without changing “some.”

```text
Some A are B  ⇔  Some B are A
```

This is a two-way **some** relationship. It does **not** mean every A is B or every B is A.

### Most: keep the majority in its original direction

If **most A are B**, more than half of A are B. Because at least one A is B, **some B are A**. That is the safe conclusion when you look back from B.

```text
Most A are B  →  Some B are A
```

You cannot reverse it as **most B are A**. The sentence measured a majority of A; it did not tell you what fraction of B is A. You also cannot assume that some A are *not* B, because all A could be B.

### All: use the conditional arrow

If **all A are B**, every A is B:

```text
A → B
not B → not A    (contrapositive)
```

The contrapositive is valid because something outside B cannot be inside A if every A is inside B. The reverse, **B → A**, is not valid. B may contain things that are not A.

If at least one A exists, “all A are B” also gives you **some A are B** and **some B are A**. Without that existence, an all-rule alone does not establish that any A exists.

## When arrows can be joined

The middle group has to connect the claims in a way that covers the members you are carrying forward.

| Given | What follows | Why |
|---|---|---|
| All A are B. All B are C. | **All A are C.** | Every A enters B, and every B enters C. |
| Some A are B. All B are C. | **Some A are C.** | The A that are B are covered by the all-rule. |
| Most A are B. All B are C. | **Most A are C.** | The majority of A inside B are all covered by the rule. |
| Most A are B. Most A are C. | **Some B are C.** | Two majorities of the same A group must overlap. |

For the last row, picture 10 members of A. More than 5 are B, and more than 5 are C. Those two sets cannot be separate within only 10 members. At least one member is both B and C.

![Two majorities measured against the same ten members of A must overlap.](./assets/shared-majority.svg)

## When the arrows do not join

**Some A are B + most B are C** does not guarantee that any A are C. The A inside B could all be among the B that are not C.

**Most A are B + most B are C** does not guarantee that any A are C. The two “most” claims count different groups, and the A inside B could sit outside C.

**All A are B + some B are C** does not guarantee that any A are C. The B that are C could be B that are not A.

When a connection feels tempting, ask: **Can the members identified by the first sentence all be outside the part described by the second?** If yes, the conclusion is not guaranteed.

## Check yourself

**1.** Some A are B. Could all A be B? Does the premise prove that all A are B?

**Answer:** Yes, all A *could* be B. No, the premise does not prove it.

**2.** Most A are B. What can you safely say about B that are A?

**Answer:** Some B are A. You cannot say most B are A without another premise.

**3.** Most A are B, and most A are C. Why must some B be C?

**Answer:** Both majorities are taken from the same A group. Each occupies more than half of it, so they must overlap.
