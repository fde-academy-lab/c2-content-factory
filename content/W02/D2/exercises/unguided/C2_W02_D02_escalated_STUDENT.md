# Which Q2 orders and channels make the gap, and how do you prove the collected figure counts no payment twice?

You work the escalated case alone, on Kalpa's warehouse. Today the tentative faculty block takes the
afternoon's last 120 minutes, so the case runs in two sittings: parts 1 and 2 straight after
chapter 6, in 20 minutes, and parts 3 to 5 in the TA-led practice lab, in about 30.
The notebook is `notebooks/C2_W02_D02_ex1_escalated_case_STUDENT.ipynb`: eight lettered choices in
five parts, a check after each part and empty cells where you read what you found.

> **The client asks.** "Booked revenue is not collected revenue. Some orders are paid in two
> instalments, some are refunded, some were never paid at all. Show me, order by order, what we
> actually collected against what we booked in Q2. If there is a gap, I want to know which orders and
> which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

The data platform lead added the payments table to the team's access and said, in passing, that the
payments feed "sometimes double-posts when the gateway retries".

## What do you need to know before you start?

**Who needs the answer.** Anand signs the page and sends it on to the CEO's Monday numbers, the
collections team rings every order on the unpaid list, and the platform lead receives the repeated
postings. A page that drops an order or keeps a repeat fails each of them.

- **Booked** is Monday's figure: 462 Q2 orders and Rs 9,84,00,000. **Collected** is the cash that
  arrived, each payment counted once. **Posted** is every payment row the feed holds against an order,
  repeats included.
- The **gap** is booked less collected. The **surplus** of a retried instalment is what was posted
  beyond one payment of it.
- The chapters built each move on invented tables first; this case asks you to choose each move again
  on Kalpa's Q2 alone, with a check after each choice.
- Q2 runs from 1 July to 30 September. The warehouse's tables are `orders` (one row per order) and
  `payments` (one row per payment event, with an instalment number).

## What are the five parts?

| Part | The question you answer | What you hand in | When |
|---|---|---|---|
| 1 | What did Q2 book, by channel, from orders alone? | Orders and booked by channel, the baseline every later figure reconciles to | Now, with part 2 |
| 2 | What did Q2 collect at order grain, and does the count close? | The reconciliation lines written before the query runs, then collected by channel | Now, 20 minutes with part 1 |
| 3 | Which Q2 orders were never paid? | The unpaid list, largest first, with its total against the gap | The lab |
| 4 | Which payments did the gateway post twice? | The double-paid list, retries only, with its surplus against posted less collected | The lab |
| 5 | What does the page say, and which check proves it? | One line per channel, the check that proves collected holds no payment twice, and the sentence to Anand | The lab |

## What are the rules for the case?

- Work alone, from the warehouse. Nothing needs cleaning, and every query runs on `orders` and
  `payments`.
- Write the reconciliation lines in part 2 before you run the query: rows in, rows out, and what the
  difference is made of.
- Each check tells you whether your pick holds, without showing you the answer. When one fails,
  change your pick and leave the check as it is.
- Every figure on your page ties back to one table alone, and the sentence to Anand carries its
  definition of collected.

## What do you post in the cohort channel?

Post one line of eight letters in the order of the notebook's markers, then your sentence to Anand
below it.

```
Post exactly this shape: xxxxxxxx
```
