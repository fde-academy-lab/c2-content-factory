# Kahoot pack: Week 1, Day 4

Eight items. Seven from the day, one returning from Wednesday one level up.

Ungraded. This is a performance indicator the programme reads for attention and retention, and it carries no weight of any kind.

Run it at the close of half two. Each item is twenty seconds except Q3 and Q8, which get thirty.

---

## Q1. Seven order amounts are on screen, sorted. Give the median.

```
1,030   1,145   1,280   1,310   1,865   2,270   2,835
```

- 1,676
- 1,310 ← correct
- 1,865
- 2,835

*Why:* seven values, so the fourth is the middle. Position, not arithmetic.
*Trap:* 1,676 is the mean, for anyone who started adding.

---

## Q2. One order in a column becomes 170 times larger. What moves?

- The mean moves a lot, the median barely ← correct
- Both of them move by roughly the same amount
- The median moves and the mean stays put
- Neither moves, since it is only one order

*Why:* the mean divides a total that just grew enormously. The median only cares which order is standing in the middle position, and that order did not change.

---

## Q3. Which claim do you trust? (30 seconds)

```
segment A:  returned 5 of 12          41.7%
segment B:  returned 500 of 1,200     41.7%
```

- A, because a smaller sample is easier to verify
- Neither, since the two cannot be compared at all
- B, because one order moves A by more than eight points ← correct
- A, because 41.7 is the same in both so it makes no difference

*Why:* one order flips A's rate by 8.3 points and moves B's by less than 0.1. A is not bad, it is unmeasured.
*Trap:* option three is the one careful people pick. They can be compared. B is the number you would act on, and A is the one you would ask for more data on.

---

## Q4. Read the skew off this sorted tail.

```
... 2,855   2,895   2,930   2,990   2,995   480,000
```

- A long left tail, with the mean sitting low
- Roughly even, since only one value is unusual
- You cannot tell without the full column
- A long right tail, so the mean sits high ← correct

*Why:* one value a hundred and sixty times the one below it is a right tail by definition, and the mean is pulled towards it.

---

## Q5. A money column with one enormous order. Which statistic goes to the stakeholder?

- The mean, since it uses all the data
- The median, named as the median ← correct
- The mode, since it is the most typical value
- The range, since it shows the full picture

*Why:* the standing convention wherever a long tail exists, which is why national statistics report median household income rather than mean.
*Trap:* "uses all the data" is true of the mean and is exactly the problem.

---

## Q6. Business returns at 11.1 percent, the best in the file. What must travel with that number?

- The nine orders it was computed on ← correct
- The date it was computed
- The segment's median order value
- The percentage change since last month

*Why:* 11.1 percent on nine orders and 11.1 percent on nine hundred are different claims wearing the same number. One more return takes this one to 22.2 percent.

---

## Q7. This code runs on Kalpa's four segments. What happens?

```python
counts = {"Retail-Core": 0, "Retail-Plus": 0, "Business": 0}
for r in orders:
    counts[r["segment"]] += 1
```

- It runs and silently skips the fourth segment
- ValueError
- TypeError
- KeyError ← correct

*Why:* a dictionary asked for a key it does not hold raises `KeyError`, and prints the missing key for you. Here that is `'Student'`, and it fires on the first order in the file.
*Trap:* option two is what people expect and hope for. Python does not skip quietly, which is the good news.

---

## Q8. Return question from Wednesday, one level up. (30 seconds)

Wednesday you found that fifty orders held only forty-nine distinct order ids, and you decided to keep both rows of the pair and flag it.

Today: your segment counts print as 9, 14, 11 and 10. Somebody asks whether your summary is trustworthy. What is your **first** check?

- Recompute the four medians by hand
- Re-run yesterday's cleaning pass
- Add the four counts, expecting 44 ← correct
- Ask which of the segments they care about

*Why:* the reconciliation habit from Wednesday, applied to a grouping instead of a cleaning pass. Input must equal the sum of the parts. Nine plus fourteen plus eleven plus ten is forty-four, so no order was lost or double-counted, and that is one addition rather than an afternoon.

*Follow-up to ask aloud, not on screen:* the pair you kept is still in there, so one customer's order is counted twice in Retail-Core. Does that break the reconciliation? No. It was a decision, it is in the log, and the count is right for the file as it stands.

---

## Distractor audit

| Check | Result |
|---|---|
| Is any correct answer the longest option? | Q1 no. Q2 no, option 2 is comparable and option 4 is longer. Q3 no, options 2 and 4 are longer. Q4 no, option 4 is longer. Q5 no, options 2, 3 and 4 are all longer. Q6 no, options 3 and 4 are longer. Q7 no, it is the shortest. Q8 no, option 3 is comparable and option 4 longer. |
| Key positions as written | Q1 pos 1, Q2 pos 1, Q3 pos 1, Q4 pos 1, Q5 pos 1, Q6 pos 1, Q7 pos 1, Q8 pos 1 |
| Position spread | **Fails as written.** Shuffle before delivery. |

**Shuffle instruction for whoever loads this into Kahoot.** Every key sits in position one because the correct answer is written first for readability. Randomise the option order on all eight items when you build the quiz. Target roughly two keys in each of the four positions. A learner who notices the first option is always right has stopped reading the question, and the indicator stops measuring anything.

Keep the options themselves intact. The distractors were chosen against specific wrong reasoning: the mean in Q1, "easier to verify" in Q3, "uses all the data" in Q5, and the silent skip in Q7 each correspond to a mistake somebody in the room is actively making.
