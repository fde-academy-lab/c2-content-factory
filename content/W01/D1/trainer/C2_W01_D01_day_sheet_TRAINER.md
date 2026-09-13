# Day sheet: Week 1 Day 1, Monday

**TRAINER ONLY.** Nothing on this page reaches a learner.

---

## The two-minute orientation

| | |
|---|---|
| **Start from** | No Kalpa, no Python. The business and the preamble open the day. The tree is the teaching; Python is the calculator. |
| **Go as far as** | Everyone draws the tree unaided, places an initiative on a branch, and computes the five leaves including median order value. |
| **Stop before** | Functions, files, grouping by segment, statistics beyond mean and median. All four arrive later this week and saying so once buys you the room's patience. |
| **Comes later** | Which branch moved, Tuesday. Can we trust the numbers, Wednesday. Is it real and what do we tell Meera, Thursday. Say the arc once, at the start, and do not repeat it. |
| **Cut first** | The recovery drill, down to five minutes. **Never cut the tree or the mean-against-median reveal.** |

---

## The running order

| Block | Duration | What happens |
|---|---|---|
| 1 | 15 min | Meera's ask. The room names what "sales" could mean. Collect four readings on the board before moving. |
| 2 | 40 min | The revenue tree on the board, each branch as a metric with its denominator, marketing's Rs 12 crore placed on its branch |
| 3 | 25 min | Environment: open the Codespace, run the setup cell, restart and recover once |
| 4 | 60 min | Count the leaves in Python: orders, revenue, customers, orders per customer. Loops, accumulators, records as dictionaries. |
| 5 | 30 min | Mean against median, and the order that splits them |
| 6 | 40 min | Unguided: three tree nodes and one sentence on which branch to examine first |
| 7 | 20 min | Kahoot and close |

Durations, never clock times. If a block overruns, block 3 is the one to compress.

---

## What is planted in today's data, and what the room should find

**This section never reaches a learner.** The discovery is the lesson; naming the plant spends it.

| Planted | Where it is | What the room should do | If nobody finds it |
|---|---|---|---|
| One corporate order of Rs 4,80,000 | Row 31, segment `Business` | Notice that the mean is eight times the median, sort the amounts, and find it themselves | Ask "sort the amounts and read me the top five". Do not name the row. |
| One amount stored as the text `"4500"` | Row 8 | Meet `TypeError` when they write the running total, read the trace, find the row | They will meet it whether they look for it or not. It is the block-4 failure. |

**If a learner asks directly whether the data is rigged:** answer with the question back. "What
would you check?" Then let them check it.

---

## The deliberate failures, with their exact text

**Block 4, the accumulator.** Have the room write the sum without `int()`. It stops with:

```
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

Read it aloud as four facts before anybody edits anything: the kind of problem, the operation, what
sat on each side, where it gave up. Then find the row together. The fix is `int()`, and say the cost
out loud: a loud problem has become a silent assumption, and Wednesday gives that assumption a log.

**Block 3, the kernel.** Run the cells deliberately out of order to produce:

```
NameError: name 'orders' is not defined
```

Then Restart Kernel and Run All Cells. The rule to leave them with: if it passes after a restart,
your screen was stale; if it fails, the notebook is wrong.

---

## The numbers, so you are never caught out

| | |
|---|---|
| Orders | 30 |
| Revenue | Rs 5,44,810 |
| Customers | 23 |
| Orders per customer | 1.30 |
| Delivered | 21 orders, Rs 5,20,790 |
| Returned | 5 orders, Rs 14,970 |
| Cancelled | 4 orders, Rs 9,050 |
| Mean order | Rs 18,160 |
| Median order | Rs 2,205 |
| Largest order | Rs 4,80,000, which is 88 percent of revenue |
| Mean without it | Rs 2,235 |

If a learner's numbers disagree, they have a different file or different code. Settle it at the
time, not at the end of the day.

---

## Per-block facilitation

**Block 1.** Do not write the tree yet. Get four readings of the word "sales" out of the room first,
because the tree lands much harder when it arrives as the answer to confusion they just felt.

**Block 2.** Draw the top row and stop. Add the owners only when somebody asks who would have to do
something about a branch. The question to push on: "divided by what?" Ask it every time a branch is
named, until somebody says it before you do.

**Block 3.** This is the block to compress. The only thing that must survive is one deliberate
out-of-order run and the restart that fixes it.

**Block 4.** Type it yourself on the projector, slowly, saying the three parts of the accumulator
aloud. Do not paste. The room mirrors on their own Codespace.

**Block 5.** Ask for the mean first and let somebody read it out. Then ask whether anybody in the
room has ever placed an eighteen-thousand-rupee order at a retailer. The laugh is the teaching
moment; the sort is the proof.

**Block 6.** Circulating matters more here than anywhere else today, because this is the first time
they work alone and the first silence is where week one is won or lost.

---

## Checkpoint questions

Ask these at the block boundaries. Each should take one learner under thirty seconds.

1. After block 2: name one branch and its denominator.
2. After block 4: what does `total = total + x` do that `total + x` does not?
3. After block 5: which number would you put in front of Meera, and why not the other one?
4. After block 6: which branch did you pick, and what would change your mind?

---

## What the room leaves with

The tree drawn from memory, four leaves computed, the median chosen over the mean on purpose, and
one branch named with a cost attached. Anything less than that and Tuesday starts on sand.
