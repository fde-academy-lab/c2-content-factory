# Solution: which checks must pass before the number leaves?

Answers: 1a 2b 3c 4d 5b 6c

## What does this set test?

The set tests whether a check can fail at all, which check stops each wrong report, and what leaves
the team on the day a check fails. Items 4, 5 and 6 are design items: the two checks
that cover three wrong reports, the reporting-day rule, and the source outside Kalpa's own tables.

## What did the set give you to work from?

> **The client asks.** "Booked revenue is not collected revenue. Show me what we actually collected
> against what we booked, and prove it is not double-counted."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Kavya Nair, the team's senior analyst, reviews every number before it
leaves the team, Anand forwards it to the CEO, and you sign it. A check that cannot fail puts a PASS
on a wrong number.

- **Plausibility checks** read the report alone: collected is at most booked, the gap is not
  negative, every channel is present.
- **Tie-back checks** recompute a figure from one source table alone and compare it with the report:
  orders against the orders table; booked against the orders table; the gap against booked less
  collected; the gap against the unpaid list's total; collected plus posted twice against posted from
  the payments table alone.

The invented book: 10 orders, booked 50,000. Two orders were never paid, worth 4,000, so collected,
each payment counted once, is 46,000. One payment of 1,000 was posted twice, so the payments table
holds 47,000 against these orders.

| Report | Orders on it | Booked | Collected | Gap |
|---|---|---|---|---|
| The true report | 10 | 50,000 | 46,000 | 4,000 |
| X, written with a plain JOIN | 8 | 46,000 | 46,000 | 0 |
| Y, the fan-out draft, 14 rows | 14 | 65,000 | 61,000 | 4,000 |
| Z, posted read as collected | 10 | 50,000 | 47,000 | 3,000 |

## Why does each key hold, item by item?

### Q1. Which plausibility checks fail report X?

Of the three plausibility checks, which ones fail report X?

The key is a, "none of the three". X is consistent with itself: collected 46,000 is at most booked 46,000, the gap of 0 is not negative, and the channels of its eight orders are all present.

- b, "the gap check alone": 0 is not negative.
- c, "all three": nothing on X contradicts itself; only a check against the tables can see the two missing orders.
- d, "the channel check alone": nothing on X contradicts itself; only a check against the tables can see the two missing orders.

### Q2. Which of these checks stops report Y?

Report Y's gap of 4,000 is right. Which one of these checks stops it?

The key is b, "booked on the page against booked from orders alone". Y repeats the multi-row orders, so its booked reads 65,000 against 50,000 in the orders table.

- a, "the gap against the unpaid list's own total": Y's gap equals the unpaid list's 4,000.
- c, "the gap against booked less collected": 65,000 less 61,000 is 4,000, so it passes.
- d, "collected at most booked, on every channel the page shows": 61,000 is at most 65,000.

### Q3. Which pair of checks stops report Z?

Report Z passes the orders and booked checks. Which pair of checks stops it?

The key is c, "the gap against the unpaid list, and collected plus posted twice against posted". Z's gap of 3,000 misses the unpaid list's 4,000, and its collected 47,000 plus 1,000 posted twice is 48,000 against 47,000 in payments.

- a, "orders against the table, and a gap that is not negative": Z has all ten orders and a gap above zero.
- b, "the gap against booked less collected, and collected at most booked on every channel": 50,000 less 47,000 is 3,000, and 47,000 is at most 50,000.
- d, "booked against orders alone, and every channel present": Z's booked is right and every channel is there.

### Q4. Which two checks would you keep if you could run only two? (Design)

A new analyst can run only two checks late on reporting day. Which pair stops all three wrong reports, X, Y and Z?

The key is d, "booked against orders alone, and the gap against the unpaid list". Booked against orders stops X (46,000) and Y (65,000); the gap against the unpaid list stops Z (3,000 against 4,000). Together they cover all three.

- a, "orders against the table, and booked against orders alone": Z passes both, with ten orders and the right booked.
- b, "collected at most booked, and a gap that is not negative": all three reports pass both.
- c, "the gap against booked less collected, and every channel present on the page": all three reports pass both.

### Q5. What goes to Anand when the payments check fails late? (Design)

At the end of reporting day, "collected plus posted twice against posted from the payments table alone" fails for the first time. What goes to Anand that day?

The key is b, "booked, the open line naming the check, collected held". Booked ties to the orders table alone and leaves; collected, which this check guards, is held; the open line names the failed check, what it means and when it closes, and the platform lead hears that day.

- a, "the whole page, with a footnote that one check failed": puts an unreconciled figure on the CEO's page with a footnote nobody reads.
- c, "nothing at all, until the platform lead repairs the feed": withholds booked, which is reconciled.
- d, "last week's collected figure beside this week's booked": mixes two weeks on one page.

### Q6. Which source makes a check Kalpa's own tables cannot pass alone? (Design)

Every check above reads Kalpa's own tables. Which source would give a check that those tables cannot pass by themselves?

The key is c, "the gateway's settlement file of what reached the bank". A settlement file comes from the gateway and the bank, so a difference against the payments table is evidence nobody at Kalpa wrote.

- a, "a second query written against the same payments table": reads the same table again.
- b, "last quarter's signed report, set beside this quarter's": compares two of Kalpa's own reports.
- d, "the orders table's own total, recomputed a second time": recomputes Kalpa's own record.

## Which item is worth arguing about?

Item 5's option a, the footnote, feels honest, and it is how a wrong figure reaches a leadership page
with a PASS stamp beside it. The rule separates what is reconciled from what is not, so the reader
never has to judge a footnote: booked goes out that day, collected waits, and the open line says when
it will follow.

## Where does this pattern live in production?

Wirecard's auditor, EY, refused to sign off on its 2019 accounts in June 2020, saying it was unable to
confirm that the money existed, and people with first-hand knowledge told the Financial Times that
from 2016 to 2018 the auditor had not checked directly with Singapore's OCBC Bank (BBC News, 18 June
2020; the FT, republished by the Irish Times, 26 June 2020; both checked 1 Oct 2026). A check that
reads a company's own records back to it cannot fail.
