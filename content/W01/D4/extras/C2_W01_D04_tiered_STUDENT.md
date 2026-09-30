# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you actually are.

---

## Stretch: when pooling and flipping part ways

You finished the take-home and the flips felt easy. Then this one is for you.

**The situation.** Kavya reads your Retail-Plus test and asks one more question.

> "On our file the flips and the pooled shuffle landed close, 0.029 against 0.027 counting falls.
> Would they on a tier where heavy buyers stay heavy? Most membership data looks like that, and a
> test that gets it wrong can miss a real fall."

**What to build.** An invented tier of 30 members, each keeping a spending level of their own across
both quarters, with every member's Q2 set Rs 400 lower on average:

```python
maker = random.Random(21)
levels = [maker.randint(2000, 7700) for _ in range(30)]      # each member's own level
q1 = [lv + maker.randint(-600, 600) for lv in levels]
q2 = [lv - 400 + maker.randint(-600, 600) for lv in levels]
```

Run both chance references on it, 5,000 times each with seed 2026, using `flip_gaps` and
`shuffle_gaps` from notebook 1's setup. Read each share counting falls and counting a move that
large either way, and measure how well a member's Q1 predicts their Q2 with
`statistics.correlation(q1, q2)`.

| Column | What goes in it |
|---|---|
| The flips' two shares | Your numbers |
| The pooled shuffle's two shares | Your numbers |
| How well Q1 predicts Q2, here and on Kalpa's file (0.04) | Two numbers |
| Why the two routes part here and land close on Kalpa's file | One sentence in business terms |
| Which you would report, and why | One sentence |

**The hard part, and the point.** Pooling treats the 60 totals as 60 different people, so the gaps
between members count as chance. Where heavy buyers stay heavy those gaps are large: pooling
overstates how often chance makes the fall and can miss a real one. On Kalpa's file a member's Q1
barely predicts their Q2, so the two routes land close there, and the design still picks the flips.
The skill is letting the design of the data choose the chance reference before any share comes
back.

**Check your build.** The tier's real fall comes out at about Rs 314 a member, and counting falls,
the flips give about 0.004 and the pooled shuffle about 0.24.

---

## Recover: the three sentences, until they are automatic

Today felt fast, and the p-value sentence still comes out wrong under pressure. Then do this, and
nothing else, tonight.

**Step 1.** Write the three sentences on a card, from the cheat sheet:

- "If nothing had changed, a gap this large turns up in about ___ of every 100 flips, and a gap that
  large either way in about ___."
- "It is worth Rs ___ a quarter, ___ percent of the company."
- "The rate stands on ___ orders from ___ customers; under thirty customers, it is a lead."

**Step 2.** Open notebook 1 and rerun sections 2 and 3 only. Fill the first sentence twice, once for
Retail-Core and once for Retail-Plus, and read both aloud.

**Step 3.** Open the chapter 1 set in `exercises/unguided/` and redo every item without looking at the
solution. If any answer changes from your first attempt, read that item's row in the solution file and
say the reason aloud.

**Step 4.** Say the note's four parts aloud from memory: claim, evidence, caveat, action. Saturday's
paper asks for them.
