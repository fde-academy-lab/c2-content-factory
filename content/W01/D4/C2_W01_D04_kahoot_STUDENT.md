# Kahoot pack: Week 1, Day 4

Eight items. Seven from the day, one returning from Wednesday one level up.

Ungraded. This is a performance indicator the programme reads for attention and retention, and it carries no weight of any kind.

Run it at the close of half two. Each item is twenty seconds except Q3 and Q8, which get thirty.

---

## Q1. Seven values are on screen, sorted. Give the median.

```
1,800   3,000   4,500   6,750   9,900   12,900   17,400
```

- **6,750** ← correct
- 8,036
- 9,900
- 4,500

*Why:* seven values, so the fourth is the middle. Position, not arithmetic.
*Trap:* 8,036 is the mean, for anyone who started adding.

---

## Q2. One record in a column becomes 100 times larger. What moves?

- **The mean moves a lot and the median barely moves** ← correct
- Both move by roughly the same amount
- The median moves and the mean stays put
- Neither moves, since it is only one record

*Why:* the mean divides a total that just grew enormously. The median only cares which record is standing in the middle position, and that record did not change.

---

## Q3. Which claim do you trust? (30 seconds)

```
segment A:  accepted 42 percent, on 12 records
segment B:  accepted 31 percent, on 1,200 records
```

- **B, because one record moves A by more than eight points** ← correct
- A, because 42 is higher than 31
- A, because a smaller sample is easier to verify
- Neither, since the two cannot be compared at all

*Why:* one record flips A's rate by 8.3 points and moves B's by less than 0.1. A is not bad, it is unmeasured.
*Trap:* the last option is the one careful people pick. They can be compared. B is the number you would act on, and A is the one you would ask for more data on.

---

## Q4. Read the skew off this sorted tail.

```
... 13,000   13,600   14,200   14,800   15,600   17,400   480,000
```

- **A long right tail, so the mean sits above almost every record** ← correct
- A long left tail
- Roughly even, since only one value is unusual
- You cannot tell without the full column

*Why:* one value twenty-seven times the one below it is a right tail by definition, and the mean is pulled towards it.

---

## Q5. A money column with a few enormous values. Which statistic goes to the stakeholder?

- **The median, named as the median** ← correct
- The mean, since it uses all the data
- The mode, since it is the most typical value
- The range, since it shows the full picture

*Why:* the standing convention wherever a long tail exists, which is why national statistics report median household income rather than mean.
*Trap:* "uses all the data" is true of the mean and is exactly the problem.

---

## Q6. Every rate you report must carry what beside it?

- **The count it was computed on** ← correct
- The date it was computed
- The name of the person who computed it
- The percentage change since last month

*Why:* 58.3 percent on twelve records and 58.3 percent on twelve hundred are different claims wearing the same number.

---

## Q7. This code runs on a file with four segments. What happens?

```python
counts = {"segment_a": 0, "segment_b": 0, "segment_c": 0}
for r in records:
    counts[r["segment"]] += 1
```

- **KeyError** ← correct
- It runs and silently skips the fourth segment
- ValueError
- TypeError

*Why:* a dictionary asked for a key it does not hold raises `KeyError`, and prints the missing key for you.
*Trap:* option two is what people expect and hope for. Python does not skip quietly here, which is the good news.

---

## Q8. Return question from Wednesday, one level up. (30 seconds)

Wednesday you learned that two records sharing an id and disagreeing need an identity rule and a named decision-maker.

Today: your cleaned file has 47 records. Your segment counts print as 20, 9, 6 and 12. Somebody asks whether your summary is trustworthy. What is your **first** check?

- **Add the four counts and confirm they total 47** ← correct
- Recompute the medians by hand
- Re-run the cleaning pass from Wednesday
- Ask which segment they care about

*Why:* the reconciliation habit from Wednesday, applied to a grouping instead of a cleaning pass. Input must equal the sum of the parts. Twenty plus nine plus six plus twelve is forty-seven, so no record was lost or double-counted, and that is one addition rather than an afternoon.

---

## Distractor audit

| Check | Result |
|---|---|
| Is any correct answer the longest option? | Q1 no, Q2 no (option 1 and 2 are close, option 2 is longer), Q3 no (option 3 is longer), Q4 no (option 4 is longer), Q5 no (options 2, 3, 4 all longer), Q6 no (option 4 longer), Q7 no (shortest), Q8 no (option 4 is comparable, option 2 longer) |
| Key positions | Q1 pos 1, Q2 pos 1, Q3 pos 1, Q4 pos 1, Q5 pos 1, Q6 pos 1, Q7 pos 1, Q8 pos 1 |
| Position spread | **Fails as written.** Shuffle before delivery. |

**Shuffle instruction for whoever loads this into Kahoot.** Every key above sits in position one because the correct answer is written first for readability. Randomise the option order on all eight items when you build the quiz. Target roughly two keys in each of the four positions. A learner who notices the first option is always right has stopped reading the question, and the indicator stops measuring anything.

Keep the options themselves intact. The distractors were chosen against specific wrong reasoning: the mean in Q1, the higher percentage in Q3, "uses all the data" in Q5, and the silent skip in Q7 each correspond to a mistake somebody in the room is actively making.
