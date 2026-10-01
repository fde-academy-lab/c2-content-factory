# Solution: which checks must pass before the number leaves?

Answers: 1a 2b 3c 4d 5b 6c

## What does this set test?

The set tests whether a check can fail at all, which check stops each wrong report, and what leaves
the team on the day checks fail. Items 4, 5 and 6 are design items: the two checks that cover three
wrong reports, which figures leave when checks fail late, and the source outside Kalpa's own
tables.

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
- **Tie-back checks** recompute a figure outside the report and compare it with the report: orders
  against the orders table; booked against the orders table; the gap against booked less collected;
  the gap against the never-paid and paid-short lists; collected plus posted twice against posted
  from the payments table alone.
- An **open line** names a failed check, what it means and when it will close.

The invented book: 10 orders, booked 50,000. Two orders were never paid, worth 4,000, and no order was
paid short, so collected, each payment counted once, is 46,000. One payment of 1,000 was posted twice,
so the payments table holds 47,000 against these orders. Every report carries all three channels.

| Report | Orders on it | Booked | Collected | Gap |
|---|---|---|---|---|
| The true report | 10 | 50,000 | 46,000 | 4,000 |
| X, the quarter's dates in WHERE | 8 | 46,000 | 46,000 | 0 |
| Y, the fan-out draft, its 14 rows read as orders | 14 | 50,000 | 61,000 | minus 11,000 |
| Z, posted read as collected | 10 | 50,000 | 47,000 | 3,000 |

## Why does each key hold, item by item?

### Q1. Which plausibility checks fail report X?

Of the three plausibility checks, which ones fail report X?

The key is a, "none of the three". X is consistent with itself: collected 46,000 is at most booked 46,000, the gap of 0 is not negative, and all three channels are on it. Only a check against the tables sees the two missing orders.

- b, "the gap check alone": 0 is not negative, so the gap check passes.
- c, "all three": nothing on X contradicts itself, so none of the three can fail.
- d, "the channel check alone": every report carries all three channels, so the channel check passes.

### Q2. Which one of these checks does report Y pass?

Report Y summed each order's amount on every payment row for collected, as chapter 2's draft did. Which one of these checks does it pass?

The key is b, "booked on the page against booked from orders alone". Y's booked is 50,000, the orders table's own figure: the fan-out reached its collected and its row count and never its booked, which is why the booked check alone cannot be trusted to catch a fan-out.

- a, "the gap against the never-paid and paid-short lists": Y's gap of minus 11,000 is far from the lists' 4,000.
- c, "collected at most booked, on every channel the page shows": 61,000 exceeds 50,000.
- d, "orders on the page against orders in the table": 14 rows read as orders against 10 in the table.

### Q3. Which pair of checks stops report Z?

Report Z passes the orders and booked checks. Which pair of checks stops it?

The key is c, "the gap against the two lists, and collected plus posted twice against posted". Z's gap of 3,000 misses the lists' 4,000, and its collected 47,000 plus 1,000 posted twice is 48,000 against 47,000 in payments.

- a, "orders against the table, and a gap that is not negative": Z has all ten orders and a gap above zero.
- b, "the gap against booked less collected, and collected at most booked on every channel": 50,000 less 47,000 is 3,000, and 47,000 is at most 50,000.
- d, "booked against orders alone, and every channel present": Z's booked is right and every channel is there.

### Q4. Which two checks would you keep if you could run only two? (Design)

A new analyst can run only two checks late on reporting day. Which pair stops all three wrong reports, X, Y and Z?

The key is d, "booked against orders alone, and the gap against the two lists". Booked against orders stops X (46,000 against 50,000); the gap against the lists stops Y (minus 11,000) and Z (3,000), each against 4,000. Together they cover all three, though Y passes the booked check.

- a, "orders against the table, and booked against orders alone": Z passes both, with ten orders and the right booked.
- b, "collected at most booked, and a gap that is not negative": X passes both, with 46,000 against 46,000 and a gap of 0.
- c, "the gap against booked less collected, and every channel present on the page": all three reports pass both, since each gap is its own booked less its own collected.

### Q5. Which figures leave for Anand when checks fail late? (Design)

Late on reporting day the suite runs on a new week's page, from a book of its own. Orders on the page match the table, and the gap equals the page's booked less its collected. Booked fails, 62,000 against 60,000 from the orders table; the gap against the two lists fails, 4,000 against 5,500; and collected plus posted twice fails, 58,500 against 55,000 in payments. Which figures leave for Anand that day?

The key is b, "booked from orders alone, with the open line; collected and the gap held". The page's booked is wrong, 62,000 against 60,000, and booked recomputed from the orders table alone is right by construction, so that figure leaves, with the open line naming the three failed checks. Collected, plus the 500 the page shows as posted twice, overshoots what the payments table holds by 3,500, so it is held, and the gap, 1,500 short of the two lists, is held with it. The platform lead hears that day, since the posted check is the feed's.

- a, "booked, collected and the gap, with an open line naming each failed check": an open line explains a held figure and never licenses one, so this puts the page's wrong booked and two unreconciled figures on the CEO's page.
- c, "booked and the gap, since the gap's own arithmetic passed; collected held": the gap's own arithmetic only says it equals the page's booked less its collected, so it carries both their errors, and the gap fails its tie-back to the two lists by 1,500.
- d, "nothing at all, until every check on the page passes again": withholds booked from the orders table, which ties to that table alone and is right whatever the page did.

### Q6. Which source makes a check Kalpa's own tables cannot pass alone? (Design)

Every check above reads Kalpa's own tables. Which source would give a check that those tables cannot pass by themselves?

The key is c, "the gateway's settlement file of what reached the bank". A settlement file comes from the gateway and the bank, so a difference against the payments table is evidence nobody at Kalpa wrote.

- a, "a second query written against the same payments table": reads the same table again.
- b, "last quarter's signed report, set beside this quarter's": compares two of Kalpa's own reports.
- d, "the orders table's own total, recomputed a second time": recomputes Kalpa's own record.

## Which item is worth arguing about?

Item 5's option c feels careful: the gap's own arithmetic passed, so why hold it? The gap is booked
less collected, so it inherits every error in collected; a check that the gap equals its own
subtraction passes whatever collected says. Only the tie-back to the two lists tests the gap against
something collected did not produce.

## Where does this pattern live in production?

Wirecard's auditor, EY, refused to sign off on its 2019 accounts in June 2020, saying it was unable to
confirm that the money existed, and people with first-hand knowledge told the Financial Times that
from 2016 to 2018 the auditor had not checked directly with Singapore's OCBC Bank, relying instead on
documents from Wirecard and its trustee (BBC News, 18 June 2020; the FT, republished by the Irish
Times, 26 June 2020; both checked 1 Oct 2026). No check outside the company confirmed the cash.
