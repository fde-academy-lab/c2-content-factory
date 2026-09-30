# Which extra fits you tonight: the stretch on flips against pooling, or the recovery drill on the three sentences?

Both are optional and neither is graded. Pick the one that matches where you are after today's six
chapters on Meera Raghavan's three questions (is the Retail-Plus fall real, is Student's 40 percent
worth budget, and did the monsoon sale work?).

---

## Stretch: on a tier where heavy buyers stay heavy, do flipping each member's pair and pooling the totals still agree?

This one is for you if you finished the take-home and the flips felt easy.

**Who needs the answer.** Kavya Nair, the team's senior analyst, reads your Retail-Plus test and
asks one more question before it goes to Meera.

> "On our file the flips and the pooled shuffle landed close, 0.029 against 0.027 counting falls.
> Would they on a tier where heavy buyers stay heavy? Most membership data looks like that, and a
> test that gets it wrong can miss a real fall."

**The questions on the way.**

1. What do the two chance references do?
2. What do you build, and what do you fill in?
3. Why do the two routes part here, and which would you report?
4. Did your build land on the right numbers?

### What do the two chance references do?

The flip test is for the same members measured twice: a coin per member decides which of its two
quarters counts as Q1, so each member is compared only with themselves. The pooled shuffle is for
two groups of different customers: it throws all the quarterly totals into one pile and deals them
back into two groups at random, so the gaps between members count as chance. On Kalpa's Retail-Plus
file, 22 members measured in Q1 and Q2, the flips gave 0.029 counting falls and the pooled shuffle
0.027, because a member's Q1 barely predicts their Q2 there (a correlation of 0.04).

### What do you build, and what do you fill in?

An invented tier of 30 members, each keeping a spending level of their own across both quarters,
with every member's Q2 set Rs 400 lower on average. Paste this into a new notebook cell and run it:

```python
import random, statistics

def mean(values):
    return sum(values) / len(values)

def flip_gaps(q1, q2, times, seed):
    """The same members measured twice: a coin per member decides which quarter is Q1."""
    random.seed(seed)
    diffs = [a - b for a, b in zip(q1, q2)]
    return [mean([d if random.random() < 0.5 else -d for d in diffs]) for _ in range(times)]

def shuffle_gaps(q1, q2, times, seed):
    """Different customers: pool every total and deal them into two groups at random."""
    random.seed(seed)
    pool = q1 + q2
    gaps = []
    for _ in range(times):
        random.shuffle(pool)
        gaps.append(mean(pool[:len(q1)]) - mean(pool[len(q1):]))
    return gaps

maker = random.Random(21)
levels = [maker.randint(2000, 7700) for _ in range(30)]      # each member's own level
q1 = [lv + maker.randint(-600, 600) for lv in levels]
q2 = [lv - 400 + maker.randint(-600, 600) for lv in levels]
real = mean(q1) - mean(q2)
```

Run both chance references on it, 5,000 times each with seed 2026. Count the share of gaps at least
as large as `real` (falls only) and the share at least that large either way, and measure how well a
member's Q1 predicts their Q2 with `statistics.correlation(q1, q2)`.

| Column | What goes in it |
|---|---|
| The flips' two shares | Your numbers |
| The pooled shuffle's two shares | Your numbers |
| How well Q1 predicts Q2, here and on Kalpa's file (0.04) | Two numbers |
| Why the two routes part here and land close on Kalpa's file | One sentence in business terms |
| Which you would report, and why | One sentence |

### Why do the two routes part here, and which would you report?

Pooling treats the 60 totals as 60 different people, so the gaps between members count as chance.
Where heavy buyers stay heavy those gaps are large, and pooling overstates how often chance makes
the fall, which is how it can miss a real one. On Kalpa's file a member's Q1 barely predicts their
Q2, so the two routes land close there, and the design still picks the flips. The skill is letting
the way the data was collected choose the chance reference before any share comes back, so the flips'
share is the one to report.

### Did your build land on the right numbers?

The tier's real fall comes out at about Rs 314 a member. Counting falls, the flips give about 0.004
and the pooled shuffle about 0.24; either way, about 0.007 and 0.49. A member's Q1 predicts their Q2
at a correlation of about 0.95. The flips call the fall rare, and pooling calls it the usual wobble.

---

## Recover: can you say the three sentences of today's note, correctly, without looking?

This one is for you if today felt fast and the p-value sentence still comes out wrong under
pressure. Do this and nothing else tonight.

**Who needs the answer.** Meera reads the note in two minutes on Monday, and each of its lines rests
on one of these three sentences said correctly.

**The questions on the way.**

1. Which three sentences go on the card?
2. Can you fill the first sentence for both segments?
3. Do your chapter 1 answers hold on a second try?
4. Can you say the note's four parts aloud?

### Which three sentences go on the card?

Write them on a card:

- "If nothing had changed, a gap this large turns up in about ___ of every 100 flips, and a gap that
  large either way in about ___."
- "It is worth Rs ___ a quarter, ___ percent of the company."
- "The rate stands on ___ orders from ___ customers; under thirty customers, it is a lead."

The first says how often chance alone makes the gap, the second how much it is worth, and the third
how much a rate can be trusted.

### Can you fill the first sentence for both segments?

Open today's chapter 1 notebook, `notebooks/C2_W01_D04_01_real_or_wobble_STUDENT.ipynb`, and rerun
only the two sections that ask "What does the usual wobble look like on Retail-Core?" and "How often
does chance alone make a fall as large as Retail-Plus's?". Fill the first sentence twice, once for
each segment, and read both aloud.

### Do your chapter 1 answers hold on a second try?

Open the chapter 1 set, `exercises/unguided/C2_W01_D04_ch1_real_or_wobble_STUDENT.md`, and redo
every item without looking at the solution. If any answer changes from your first attempt, read that
item's section in the solution file and say the reason aloud.

### Can you say the note's four parts aloud?

Say them from memory: claim, evidence, caveat, action. Saturday's paper asks for them.
