# Day sheet: Week 1 Day 3, Wednesday

**TRAINER ONLY.**

---

## The two-minute orientation

| | |
|---|---|
| **Start from** | Tuesday's functions and conclusion. Today re-runs it on the ERP exports, and the number moves. |
| **Go as far as** | Everyone ships the cleaned dataset, the decisions log, a reconciled count and revenue bridge, and the note to Finance. |
| **Stop before** | Statistics beyond counts and the median, imputation beyond a stated default, pandas. |
| **Comes later** | Thursday asks whether the cleaned gap is real. Week 2 re-expresses this whole pass in SQL and then in pandas. |
| **Cut first** | Writing JSON back out, then the outlier fence. **Never cut the reconciliation or the recompute.** |

---

## The running order

| Block | Duration | What happens |
|---|---|---|
| 1 | 10 min | Anand's two figures. The room lists ways an export could produce either. |
| 2 | 45 min | Files: read the CSV and the JSON feed. Everything is text until converted. |
| 3 | 40 min | Profile: presence, convertibility, distinct counts per field |
| 4 | 50 min | Missing values and the three-way decision. Duplicates and the identity rule. The bulk order kept because it is real. |
| 5 | 35 min | Reconcile: input equals clean plus rejected. Recompute the tree. What changed against Tuesday. |
| 6 | 40 min | Unguided: the full pass, the decisions log, the note to Finance |
| 7 | 20 min | Kahoot and close |

---

## What is planted, and what the room should find

**This section never reaches a learner.**

| Planted | What the room should do | If nobody finds it |
|---|---|---|
| 14 duplicated Q1 rows carrying Rs 20 lakh | Notice 201 rows against 186 distinct ids in the profile, then total the repeats | Ask for the distinct count of `order_id` explicitly. Do not say why. |
| One amount spelled `twelve` | Meet `ValueError` in the conversion, then count how many there are | It fires in block 2 whether they look or not |
| One record with no `status` | Find it in the presence count: 200 of 201 | Ask which field is present on fewer rows than the others |
| A near-duplicate pair sharing `KR-02151` with different dates | Find that a whole-record dedupe leaves it and an id dedupe removes it | This is the judgment of the day. If nobody reaches it, walk it in block 4 rather than losing it. |
| A truncated JSON feed | Meet `JSONDecodeError` and open the file at the named line | It fires in block 2 |
| A vendor export with the header row repeated | Notice the second line is identical to the first | Lowest priority. Cut it before the reconciliation. |

**The Rs 4,80,000 corporate order is planted to survive.** If a learner proposes removing it, do not
correct them. Ask what they would tell the customer, and let the room answer.

---

## The deliberate failures, with their exact text

**Block 2, the truncated feed.**

```
json.decoder.JSONDecodeError: Unterminated string starting at: line 1397 column 15 (char 27679)
```

Before anybody theorises, open the file at that point and read the last sixty characters aloud. The
sentence to leave them with: a truncated file is a complete file that stops early, so you ask for it
again rather than patching it.

**Block 2, the conversion.**

```
ValueError: invalid literal for int() with base 10: 'twelve'
```

Then the move that matters: put it in a `try` and **count** the failures rather than suppressing
them. One is a curiosity; forty would be a different day.

---

## The numbers, so you are never caught out

| | |
|---|---|
| Rows in the export | 201 |
| Distinct order ids | 186 |
| Clean | 184 |
| Rejected | 17 (15 duplicate ids, 1 no status, 1 unconvertible amount) |
| Q1 as exported | Rs 2,09,98,210, which rounds to Anand's 2.1 crore |
| Q1 reconciled | Rs 1,89,98,210, which rounds to Finance's 1.9 crore |
| The gap | Rs 20,00,000 |
| Q2 reconciled | Rs 1,86,98,150 |

| Measure | Tuesday | Wednesday |
|---|---|---|
| Revenue change | down 11.0 percent | down 1.6 percent |
| Orders per customer | down 24.6 percent | down 12.9 percent |
| Retail-Plus | down 49.0 percent | down 33.3 percent |
| Retail-Core | down 5.3 percent | down 2.5 percent |
| Customers | 69 and 69 | 69 and 68 |

The customer count moves from 69 to 68 because a rejected row was somebody's only Q2 order. If a
learner spots that, it is an excellent question: the answer is that rejecting rows changes the
population, which is why the rejects log exists.

---

## Per-block facilitation

**Block 1.** Get five causes out of the room before opening anything, and write them on the board.
Then point out that none of them is "the amounts are wrong". That is the insight of the morning and
it lands better as an observation about their own list than as a statement from you.

**Block 3.** Profile and stop. The urge to fix is strong and the discipline is the lesson. If
somebody starts removing rows during the profile, ask them how many rows they are about to remove,
and let the silence do the work.

**Block 4.** The near-duplicate pair is the block's centre. Put both rows on screen side by side and
ask which one is the order. There is no right answer in the data, which is the point.

**Block 5.** Write `INPUT = CLEAN + REJECTED` on the board before running anything, then fill it.
Build the bridge left to right, saying each number aloud. When it lands on 1.9, say "Anand was
right" out loud; it matters that the room hears the analyst concede.

**Block 6.** The note to Finance is the deliverable, not the code. Ask two learners to read theirs
aloud at the close.

---

## Checkpoint questions

1. After block 3: `order_id` is present 201 times and distinct 186 times. What does that prove, and
   what does it not prove?
2. After block 4: two rows share an id and differ on the date. Which is the order?
3. After block 5: your bridge lands on 1.92 and Finance says 1.90. What do you do?
4. After block 6: which of Tuesday's sentences would you now withdraw?

---

## What the room leaves with

A reconciled number they can defend in four lines, a decisions log an auditor could read, and the
experience of watching their own Tuesday finding get smaller without disappearing. The last one is
the day.
