# Guided: ten cards, then five thousand

Built with the trainer. The cards come first and they are not a warm-up. Everything in the code is
the card move repeated.

---

## Step 1. Ten cards, on the table, before any code

Take ten playing cards. Write `PLUS` on six and `CORE` on four.

1. Deal them into two piles by their labels. Compute whatever number the room picks, and the gap
   between the piles. **Write the gap on your page.**
2. Now say the sentence out loud: *suppose the labels mean nothing at all.*
3. Collect the cards, shuffle, and deal ten again into piles of six and four, **ignoring the
   labels**. Recompute the gap and write it down.
4. Do step 3 nine more times.
5. Count how many of your ten chance gaps are at least as large as the real one.

```
that count, over ten  =  the p-value
```

That is the definition. There is nothing else in it.

---

## Step 2. The same move in code, ten times

```python
def shuffled_gap(rng):
    m = members[:]
    rng.shuffle(m)
    a = [r for c in m[:n_plus] for r in by_customer[c]]
    b = [r for c in m[n_plus:] for r in by_customer[c]]
    return fall(b) - fall(a)
```

**The unit you shuffle is the customer, not the order.** A customer's orders belong together, and
splitting them across both labels builds a world that could not exist.

Run ten and print them beside the real gap.

---

## Step 3. Five thousand, and the number that comes out

```python
extreme = sum(1 for _ in range(5000) if abs(shuffled_gap(rng)) >= abs(observed))
```

For Retail-Plus against Retail-Core the answer is **zero of five thousand**.

---

## Step 4. Write it correctly, which is harder than computing it

You did not test every possible world. You made five thousand, so the smallest number you can
honestly report is one in five thousand.

```
p < 0.0002
```

**Never `p = 0`.** Say why out loud before you move on: the number you write is the resolution of
your own simulation.

---

## Step 5. Say the sentence three ways and keep the right one

Write all three on your page.

1. "There is a 0.02 percent chance the finding is wrong."
2. "There is a 0.02 percent chance that chance caused it."
3. "Chance alone produced a gap this large in none of 5,000 shuffles."

Cross out the first two. The third is the only one that describes what you computed.

---

## Step 6. Three calls, not one

| Call | Answered by | For Retail-Plus |
|---|---|---|
| Could chance have done this? | The p-value | No |
| Is it big? | The size of the effect | Yes, about a third |
| Is it worth acting on? | The cost against the gain | Yes, 22 paid-tier members |

Only the first came from the shuffle. Say that out loud too, because it is the sentence that stops a
p-value being used as a decision.

---

## Step 7. Now run the same code on Student and watch it disagree

Twelve orders, five in Q1 and seven in Q2. Under a coin flip per order, how often does chance give
seven or more in the second?

The answer is about **1,914 of 5,000**, so `p = 0.383`.

Write both results side by side on your page. Same method, opposite verdicts. That pair is the day.

---

## Step 8. The campaign, and the three-row table

Compute revenue per customer for the exposed and unexposed groups: first blended, then within
Retail-Plus, then within Retail-Core.

Put the three rows on screen in that order and stop after each one. The reveal is the order.
