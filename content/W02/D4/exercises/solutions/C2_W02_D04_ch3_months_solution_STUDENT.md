# Which answers hold in the chapter 3 set on Retail-Plus's months, and why?

Answers: 1b 2d 3c 4a 5b

The head of Retail-Plus, Kalpa Retail's paid membership tier, takes one number to the growth review
and uses each member's months to decide whom to protect. A long table holds one row per member per
month with orders; a wide table, built with `pivot_table`, holds one row per member and one column
per month; `melt` folds wide back into long. Chapter 3 found 107 members buying in 266
member-months, and the tier taking Rs 5,85,770 in Q1 (April to June 2026) and Rs 4,13,380 in Q2
(July to September), a fall of 29.4 percent, which a query that never pivots confirmed. Two of the
five items are design items: 3 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. A months view
whose cells mean something other than a total sends a smaller fall to the review, and a view whose
rows are the wrong thing cannot say who is drifting.

**The questions on the way.**

- Which idea does the chapter 3 set test?
- Why does each of the five keys hold, from two invented members to the two asks of one day?
- Why is option b in item 2, filling the empty months, the wrong answer worth arguing about?
- Where does keeping how often apart from how much come up at work?

## Which idea does the chapter 3 set test?

A reshape puts one number in each cell, and the number is whatever the call was told to put there.
The set asks what a cell holds when nobody says, how to read a view against its source, which shape
answers a trend, what the index makes a row, and how one day's two asks split between pandas and the
warehouse when one of them is rerun every week and the other is tried three ways once.

## Why does each of the five keys hold, from two invented members to the two asks of one day?

### Q1. What does a one-line pivot put in April's column for two invented members?

M1 ordered twice in April, Rs 1,000 and Rs 3,000, and M2 once, Rs 4,000.

The key is b, "It gives Rs 6,000". With no `aggfunc`, `pivot_table` puts the mean of each member's
orders in the cell: Rs 2,000 for M1 and Rs 4,000 for M2. The column adds up to Rs 6,000 where
April's orders were worth Rs 8,000, and M1's second order has vanished into an average.

- a, "It gives Rs 8,000": It is April's true total, which the cell holds only with `aggfunc="sum"`.
- c, "It gives Rs 3,000": It is the mean of the two cells, an average taken twice.
- d, "It gives Rs 2,667": It is the mean of April's three orders, which no cell holds.

### Q2. What goes back to an analyst whose months view adds up to less than its orders?

The view's columns add up to Rs 3,10,000 and Rs 2,90,000, and its orders total Rs 8,40,000.

The key is d, "The cells add up to Rs 6,00,000 of Rs 8,40,000, so name the aggfunc". A view of
spend has to hold its source's total. Rs 6,00,000 against Rs 8,40,000 says the cells are something
other than sums, and the default mean is the usual cause, so the analyst says which `aggfunc` the
view used before anyone reads a fall off it.

- a, "Ship it, since the fall of 6.5 percent comes from the view's own columns": A fall read from
  averages is the fall of a typical order, and the head of the tier asked about spend.
- b, "Rebuild it with `fill_value=0`, since the empty months pulled the sums down": An empty cell
  adds nothing to a sum whether it is blank or 0, so the fill cannot close a Rs 2,40,000 gap.
- c, "Rs 2,40,000 of orders is missing, so the index must have dropped members": The gap is real,
  and a dropped member is one cause. The cheaper test comes first, since one `aggfunc` explains a
  short total with every member present.

### Q3. Which shape should carry the tier's twelve-month trend next year, sized on its rows and empty cells?

Item 3 is a design item: next year 150 members order in about 540 member-months across 12 months,
and the head wants one line on one slide.

The key is c, "The long table fits, at 540 rows by 3 columns, 1,620 cells, none empty, one total a
month by `groupby`". A trend is one number per month, and grouping the long table by month gives it
from 540 rows with nothing empty.

- a, "The wide table fits, at 150 rows by 13 columns, 1,950 cells, 1,260 of them empty, read along
  each member's row": The member and twelve months make 13 columns, so 150 rows hold 1,950 cells, and 1,260 of the
  1,800 month cells are empty. It is read along a member's row, which is a comparison, and the trend
  needs its columns summed first.
- b, "A query per month fits, with 12 columns written by hand, so a 13th month is an edit": Every
  new month is an edit and a place for a typo.
- d, "The pivot indexed by order fits, with a row per order and 12 columns, nearly all of them
  empty": Each of its rows is an order, the wrong thing for any member or tier question.

### Q4. What shape is the tier's pivot with months as the index and members as the columns?

The tier has 355 orders from 107 members over six months, and the call puts the months on the
index.

The key is a, "It returns 6 rows by 107 columns". The index decides what one row is, here a month,
and the columns are the 107 members who ordered. The orders are folded into the cells.

- b, "It returns 107 rows by 6 columns": It is the member view, with `index` and `columns` the other
  way round.
- c, "It returns 355 rows by 6 columns": It is the view indexed by order, one row per order.
- d, "It returns 6 rows by 355 columns": It treats each order as a column, which no argument in the
  call asks for.

### Q5. Which plan answers Finance's weekly months and the head's afternoon question together?

Item 5 is a design item: one ask is rerun every Monday by someone outside the team, and the other is
tried three ways once, so the two asks pull toward different homes.

The key is b, "Finance gets one query grouped by month, and the head's three tries run in pandas on
the tables". Anand Iyer's analyst reruns Finance's months from the warehouse, so they belong there,
as one query grouped by month that gains October by itself. The head's three rankings are an
afternoon's iteration on the long and wide tables chapter 3 already built, which is pandas' work.

- a, "Both stay in pandas, and the notebook with its long and wide tables goes to Finance each
  Monday": Finance's analyst cannot rerun a notebook from the warehouse, and every Monday's copy is
  a second version of a number Finance quotes.
- c, "Finance gets a query per month, typed by hand, and the head's three tries run in pandas": The
  home is right for both asks, and a column typed for each month makes October an edit and a place
  for a typo, in a query Finance reruns every week.
- d, "Both move to the warehouse, as Finance's query and a new query for each of the head's tries":
  Three queries written and dropped in one afternoon are slower to change than three lines on tables
  already in memory, and nobody reruns them after the review.

## Why is option b in item 2, filling the empty months, the wrong answer worth arguing about?

Item 2, option b sounds like a fix because `fill_value=0` sits beside `aggfunc` in the chapter's
corrected call. The two do different jobs. `fill_value` writes 0 in a month with no orders, which
changes how the view reads and never changes a sum; `aggfunc` decides what the filled cells hold. A
total that falls short of its source is an `aggfunc` question first.

## Where does keeping how often apart from how much come up at work?

Costco, whose business rests on paid memberships, reports the two parts separately. On the call for
its fourth quarter of fiscal 2026 its chief financial officer said "traffic or shopping frequency
increased 3.3% worldwide" and "our average transaction or ticket was up 5.9% worldwide" (Costco's
earnings call and the supplemental information it filed with the SEC, both 24 Sep 2026, checked 1
Oct 2026). A months view that averages each cell hides the first of those two numbers inside the
second.
