# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you actually are, not the
one that sounds better.

---

## Stretch: the branch that pays for itself

You finished the take-home early and the arithmetic felt easy. Then this one is for you.

**The situation.** Meera comes back with a second question.

> "You told me which branch to look at. Now tell me which branch is worth the money. If I spend
> Rs 1 crore, which branch gives me the most revenue back, and how sure are you?"

**What to build.** One table, five rows, one per branch. For each branch:

| Column | What goes in it |
|---|---|
| Branch | The name |
| What Rs 1 crore buys | Your own assumption, written as an assumption |
| The revenue that produces | The arithmetic, shown |
| What has to be true | The condition your number depends on |
| How you would find out | A check somebody could run this week |

**The hard part, and the point.** Every row needs an assumption you invented, clearly labelled as
invented. The skill is not the arithmetic. It is writing a number you are willing to defend while
saying out loud which part of it you made up.

**A tell that you have done it well:** at least one row should conclude that the branch is not
worth Rs 1 crore, with a reason.

---

## Recovery: thirty orders, one loop at a time

The session moved fast, the loop did not land, and you would rather rebuild it than pretend. Then
this one is for you, and doing it tonight costs you nothing tomorrow.

**Work in a fresh cell in today's notebook. One step at a time, running after each.**

1. Print the first record on its own. Look at it until the seven field names are familiar.
2. Print just the amount of the first record: `ORDERS[0]["amount"]`.
3. Print the amount of the second record. Then the third. By hand, three times.
4. Now write the loop that prints every amount. Nothing else, just the print.
5. Add a variable `total = 0` above the loop and `print(total)` below it. Run it. It prints zero,
   because nothing adds to it yet.
6. Add the one line inside the loop that adds to `total`. Run it.
7. When it breaks, read the message out loud before you change anything. The message names the row.

**What you should end up believing.** A loop is three decisions: where it starts, what it does each
time, and what survives after it finishes. Everything else this week is a variation on those three.

**If step 7 did not break for you,** you skipped the file's one text amount, which means you already
wrote `int()`. Go back and take it out on purpose so you see the error once. Meeting it tonight
alone is cheaper than meeting it on Wednesday in front of Finance.
