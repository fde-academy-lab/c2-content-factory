# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you actually are, not the
one that sounds better.

---

## Stretch: the split, written once

You finished the take-home early and the afternoon's mix against rate felt like arithmetic you did
by hand. Then this one is for you.

**The situation.** Anand Iyer comes back after the afternoon.

> "Your split of revenue per order into mix and rate convinced me for one quarter. Next quarter
> somebody else will run it, on a different file, at the end of a long day. Give me the split as
> something that cannot be done differently twice." (Anand Iyer)

**What to build.** One function, `mix_and_rate(before_rows, after_rows, key)`, that returns a
dictionary with four entries: the overall rate before, the overall rate after, the part of the
change explained by the mix of groups, and the part explained by the rates within groups.

| Step | What it must do |
|---|---|
| 1 | Group both sets of rows by `key` with your own accumulator, and count the groups in each |
| 2 | Compute each group's share of orders and its revenue per order, before and after |
| 3 | Compute what the overall rate would have been with the after mix and the before rates |
| 4 | Return the mix part and the rate part, and check that they add up to the whole change |
| 5 | Refuse, with a clear message, when a group exists on one side only |

**The check it must pass.** On the class file, with `key="segment"`, it reproduces the afternoon's
split of the Rs 33,231 rise: Rs 22,902 of mix and Rs 10,330 of rate, within a rupee.

**The hard part, and the point.** Step 5. A group that exists on one side only has no before rate
or no after rate, and the split has no honest answer for it. Decide what the function does, write
the reason in its docstring, and then run it on the take-home file with `key="channel"` and say in
one line what the split tells the regional operations head.

**A tell that you have done it well:** the function prints nothing, returns its answer whenever an
honest answer exists, and a colleague could read the docstring and know what happens to a missing group without
opening the code.

---

## Recovery: one segment, one step at a time

The session moved fast, the accumulator did not land, and you would rather rebuild it than pretend.
Then this one is for you, and doing it tonight costs you nothing tomorrow.

**Work in a fresh cell in round 2's notebook. One step at a time, running after each.**

1. Print the first three records on their own. Point at the quarter and the segment in each.
2. Make an empty dictionary, `counts = {}`, and print it. It prints `{}`.
3. Take the first record only. Put its quarter into `counts` with the value 1, and print `counts`.
4. Now write the loop over every record that adds 1 to its quarter's count, creating the entry the
   first time a quarter is seen. Print `counts`. It should say 114 for Q1 and 86 for Q2.
5. Change the key to the pair `(order["quarter"], order["segment"])`. Before you run it, write down
   how many keys you expect. Run it and count them.
6. Wrap steps 4 and 5 in a function, `count_by(rows, field)`, that ends in `return counts`. Call it,
   store the result, and print the stored result. Then change `return` to `print` once, run it
   again, and print the stored result: it says `None`.
7. On three invented orders of Rs 1,000, Rs 1,200 and Rs 40,000, write the median, the minimum, the
   maximum and the range by hand, then check each with code.

**What you should end up believing.** Grouping is one move: a dictionary, a key, and an update per
record. A function is worth writing when it hands its answer back, and the `None` you saw in step 6
is what every table built on a printing function is full of.

**If step 7 surprised you,** look at the gap between the mean and the median of those three invented
orders, and say in one sentence which of the two you would put in a note to Meera.
