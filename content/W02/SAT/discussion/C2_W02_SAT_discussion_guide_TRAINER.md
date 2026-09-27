# Week 2 Saturday: the discussion guide

**TRAINER ONLY.** Led by the Academic TA, after the paper and the break. The paper and its key are
in `paper/` and `answer-key/`; the key file carries every item's key, tag, level, day and interview
anchor.

This is the heaviest paper of the first month, because SQL carries the most interview weight of any
analyst skill. The discussion is where that weight turns into answers a learner can say aloud.

---

## The shape of the four hours

| Block | Duration | What happens |
|---|---|---|
| The paper | 120 min | Pen and paper, AI-free, no notes: 58 objective items. |
| Break | 20 min | Papers stay face down on the desks. |
| Marking | 15 min | Papers swapped and marked against the key, read out by you. |
| Most-missed first | 20 min | The items the room lost most, each one repaired aloud. |
| The interview anchors | 40 min | Ten questions asked aloud as interview questions, with random call-outs. |
| Doubts and the bridge | 25 min | Open doubts, then Monday: Build 1 opens in Kalpa Health. |

---

## Marking, 15 minutes

1. Papers swap along the row, so nobody marks their own.
2. Read the key out section by section from the key file: the letters in runs of five, the words
   and numbers one at a time, and each ordering item's sequence slowly, twice.
3. The marker writes a tick or a cross beside every item, then the count of ticks as Items right on
   the front page, and hands the paper back.
4. The key file's marking rule decides the edge cases: every correct letter and no other on a
   more-than-one item, the number on an applied maths item, the whole sequence on an ordering item.
   There is no partial credit, because the programme has set no rule for it.

Say once, at the start, that the marker is deciding nothing, and that reading somebody else's
answer against the key is the exercise.

## Most-missed first, 20 minutes

Read out the candidate list and ask for hands on the paper each person marked: "a cross on item
24?" Write the counts on the board and take the four highest, in order. An item outside the list
that carries more crosses wins its place.

| Item | What it tests | The trap most papers fall into | The repair, said aloud |
|---|---|---|---|
| 24 and 53 | The join that multiplied money | Checking the rows, which all look fine | Compare the row count before and after the join first: fifty retried payments turn Rs 20 lakh collected into a sum of Rs 21 lakh. |
| 28 | A window that changes between runs | Blaming the cache or the database | The `ORDER BY` inside the window has ties, so the row order is ambiguous and the running total can differ; name a tiebreaker. |
| 35 | What a full outer join adds | Ticking the orders with two payments | Only rows with no partner on the other side are new: orders with no payment and payments with no order. |
| 36 | When GROUP BY runs out | Ticking total revenue per segment | A rank within a segment, the previous month beside this one, and a running total with every row kept all need a window; a total per segment does not. |
| 46, 47 and 54 | Ties in a top-N | Assuming a top-N always returns N rows | `DENSE_RANK() <= 3` returns five members here, `RANK() <= 50` ships 51 rows on a tie at fifty, and only `ROW_NUMBER` returns exactly N, by breaking the tie arbitrarily. |
| 51 | Where a fix belongs | Correcting the total in the pivot | The fix belongs in the merge: de-duplicate the exposure table on a stated rule and validate the keys, so the pivot is right without anyone typing over it. |
| 57 | Logical order | Writing the clauses in the order they are typed | FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, which is why an alias works in ORDER BY and fails in WHERE. |

## The interview anchors, 40 minutes

Ask each anchor aloud as an interviewer would: name the person, then the question, then wait. Give
sixty seconds. Ask the room for the one sentence that would make the answer stronger, and read the
answer below only if nobody gets there. The items after each anchor descend from it.

### 1. [S] WHERE against HAVING, one sentence each.

*Items 1, 11 and 33.*

`WHERE` decides whether to keep one row, judged on that row alone, before any grouping exists.
`HAVING` decides whether to keep a whole group, judged on the group, after the grouping has
happened. Listen for the answer that says only "rows against aggregates": true, and it predicts
nothing new, because the timing is the answer.

### 2. [S] INNER against LEFT join: what does each drop or keep?

*Items 4, 12, 21 and 35.*

An inner join keeps only the rows that find a partner, so an order with no payment disappears. A
left join keeps every row of the left table and fills the missing side with nulls, so the unpaid
order stays, which is exactly how Anand's unpaid orders are found: left join, then keep the rows
where the payment's key is null. Both can multiply rows, because each keeps every matching pair.

### 3. [S] RANK, DENSE_RANK and ROW_NUMBER on a tie.

*Items 14, 25, 26, 44 to 47 and 54.*

On a tie, `RANK` gives the tied rows the same rank and skips the next ones (1, 2, 2, 4),
`DENSE_RANK` gives the same rank without a gap (1, 2, 2, 3), and `ROW_NUMBER` gives every row its
own number and breaks the tie arbitrarily. The strong answer adds the business consequence: a top-50
report by `RANK` can ship 51 names, and one by `ROW_NUMBER` can hand two analysts two different
lists from the same data unless a tiebreaker is named.

### 4. [S] groupby in the split-apply-combine sentence.

*Items 16, 29 and 56.*

`groupby` splits the rows by a key, applies a computation to each group, and combines the results
into one row per group: 1,000 orders belonging to 400 customers become a 400-row table, with a mean
frequency of 2.5 orders per customer.

### 5. [F] Your LEFT join grew the row count and revenue doubled; name the cause and the check.

*Items 13, 22 to 24, 34, 40 to 43 and 53.*

The cause is a key that is not unique on the right side: some orders have more than one payment
row, so each of those orders appears once per payment and its amount is counted again. Neither
table has to hold a duplicate row for this to happen. The check is the row count before and after
the join, then a count of payment rows per order. Push until somebody says the duplication happened
**in the join**, then ask what that means for every row-level check: all of them pass.

### 6. [F] Top-3 per segment: GROUP BY or a window, and why?

*Items 7, 27 and 36.*

A window. `GROUP BY` collapses each segment to one row, so the members inside it are gone; a window
function ranks each member within its segment and keeps every row, and the top three are the rows
with rank three or less, with the tie rule chosen on purpose.

### 7. [F] Which merge argument raises on duplicate keys, and which error?

*Items 8, 30, 38 and 49.*

`validate`, set to the relationship the merge must have, such as `'one_to_one'` or
`'many_to_one'`. When the keys break it, pandas raises `MergeError: Merge keys are not unique in
right dataset; not a one-to-one merge`, before any number is produced. That is the point: the
error arrives at the merge, instead of a wrong total arriving at the leadership deck.

### 8. [F] A pivot's total disagrees with the warehouse; where do you look first?

*Items 17 and 48 to 51.*

Upstream of the pivot, at the merge that built its table: compare the row counts, and look for
repeated keys. In the paper's third set, 60 customers appear twice in the exposure table, so the
merged table holds 1,060 rows and the pivot sums their revenue twice, which is the same failure
Thursday's `MergeError` caught on the loaded feed. The pivot did nothing wrong with the file it was
handed; the fix is in the merge.

### 9. [D] Same question, three tools: how do you choose, and defend one choice?

*Items 20, 31, 32 and 58.*

The number travels in one direction: the warehouse computes the source of truth, pandas carries the
analyst's iteration, and Excel presents it and lets a director explore. A KPI Finance will check
belongs in the warehouse, because it runs the same way every Monday and anyone can audit the query.
Defend one choice with a reason about who depends on the number, never with a preference for a tool.

### 10. [D] Kalpa Health asks 'where does our growth come from'; say what stays the same in your method and what changes.

*No paper item; this anchor is the bridge.*

What stays the same are habits: count before you total, name the denominator, say what one row
means, reconcile against the owner's books, and ask who owns the number. What changes is the entity
model, the vocabulary and the stakeholders. The failure to listen for is somebody reaching for
Retail's revenue tree in a diagnostics business without first asking what a sale is there.

---

## Running random call-outs without losing the room

| Do | Do not |
|---|---|
| Name the person, then the question, then wait | Ask the question to the room and take the first hand |
| Give sixty seconds, and let the silence run | Rescue somebody at fifteen seconds |
| Take a wrong answer, write it on the board, and ask the room to repair it | Correct it yourself |
| Come back to the same person later with an easier one | Leave somebody who struggled sitting with it |

Call on somebody whose paper you have not read, so the call is genuinely cold, and when an answer is
wrong, take the next answer from somebody else before correcting it, so the room does the work.

---

## Doubts and the bridge into Build 1, 25 minutes

Take open doubts first. Then close on Monday: Build 1 opens in Kalpa Health with the Programme
Head's online introduction, an unfamiliar unit, unfamiliar data and unfamiliar stakeholders, and a
group of four rather than a room. Anchor 10 is the question the whole build week asks. End on the
sentence, and put it on the board:

```
The method transfers. The domain does not.
```

---

## After the session

Collect the marked papers. Using the key file's items-by-tag list, count the crosses per tag for
each learner and enter that row in the ground team's tracker: one row per learner per week, the
count of items right and the misses by tag. The misses by day point at the day each gap came from.

Write a short note for the build team beside the tally. Any item where more than half the papers
gave the same wrong answer points at the teaching rather than the learners, and belongs in a
follow-up issue. Name the two or three learners who answered anchor 10 with habits rather than
techniques: they are the ones to watch in Build 1. The paper is ungraded, never a ranking, and never
read out by name.
