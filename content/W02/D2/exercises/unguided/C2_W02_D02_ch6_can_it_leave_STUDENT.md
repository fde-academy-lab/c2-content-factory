# Which checks must pass before the collected number leaves the team, and what does Anand get when one fails at the end of reporting day?

The chapter 6 set has six items on an invented book and three wrong reports written from it, so none
of its numbers comes from Kalpa's warehouse. Items 1 and 2 close the chapter live; the rest open the
TA-led practice lab or are worked tonight.

> **The client asks.** "Booked revenue is not collected revenue. Show me what we actually collected
> against what we booked, and prove it is not double-counted."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** Kavya Nair, the team's senior analyst, reviews every number before it
leaves the team, Anand forwards it to the CEO, and you sign it. A check that cannot fail puts a PASS
on a wrong number.

**The questions on the way.**

- Which plausibility checks fail report X?
- Which of these checks stops report Y?
- Which pair of checks stops report Z?
- Which two checks would you keep if you could run only two?
- What goes to Anand when the payments check fails late?
- Which source makes a check Kalpa's own tables cannot pass alone?

An item marked Design asks for the best-fit approach, a sizing, the fact that would switch it, or the second route.

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

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. Which plausibility checks fail report X?

Of the three plausibility checks, which ones fail report X?

a) none of the three
b) the gap check alone
c) all three
d) the channel check alone

### Q2. Which of these checks stops report Y?

Report Y's gap of 4,000 is right. Which one of these checks stops it?

a) the gap against the unpaid list's own total
b) booked on the page against booked from orders alone
c) the gap against booked less collected
d) collected at most booked, on every channel the page shows

### Q3. Which pair of checks stops report Z?

Report Z passes the orders and booked checks. Which pair of checks stops it?

a) orders against the table, and a gap that is not negative
b) the gap against booked less collected, and collected at most booked on every channel
c) the gap against the unpaid list, and collected plus posted twice against posted
d) booked against orders alone, and every channel present

### Q4. Which two checks would you keep if you could run only two? (Design)

A new analyst can run only two checks late on reporting day. Which pair stops all three wrong reports, X, Y and Z?

a) orders against the table, and booked against orders alone
b) collected at most booked, and a gap that is not negative
c) the gap against booked less collected, and every channel present on the page
d) booked against orders alone, and the gap against the unpaid list

### Q5. What goes to Anand when the payments check fails late? (Design)

At the end of reporting day, "collected plus posted twice against posted from the payments table alone" fails for the first time. What goes to Anand that day?

a) the whole page, with a footnote that one check failed
b) booked, the open line naming the check, collected held
c) nothing at all, until the platform lead repairs the feed
d) last week's collected figure beside this week's booked

### Q6. Which source makes a check Kalpa's own tables cannot pass alone? (Design)

Every check above reads Kalpa's own tables. Which source would give a check that those tables cannot pass by themselves?

a) a second query written against the same payments table
b) last quarter's signed report, set beside this quarter's
c) the gateway's settlement file of what reached the bank
d) the orders table's own total, recomputed a second time

---

## Where does this skill come back?

It comes back every Monday, and in the escalated case, whose last part asks for the check that
proves the page counts no payment twice. The notebook for this chapter is
`notebooks/C2_W02_D02_06_can_it_leave_STUDENT.ipynb`.
