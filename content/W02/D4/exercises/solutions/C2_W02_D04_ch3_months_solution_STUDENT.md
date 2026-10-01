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
- Why does each of the five keys hold, from two invented members to the fact that moves the view?
- Why is option b in item 2, filling the empty months, the wrong answer worth arguing about?
- Where does keeping how often apart from how much come up at work?

## Which idea does the chapter 3 set test?

A reshape puts one number in each cell, and the number is whatever the call was told to put there.
The set asks what a cell holds when nobody says, how to read a view against its source, which shape
answers a trend, what the index makes a row, and which fact would move the view into the warehouse.

## Why does each of the five keys hold, from two invented members to the fact that moves the view?

### Q1. What does a one-line pivot put in April's column for two invented members?

M1 ordered twice in April, Rs 1,000 and Rs 3,000; M2 once, Rs 4,000.

The key is b, "Rs 6,000". With no `aggfunc`, `pivot_table` puts the mean of each member's orders in
the cell: Rs 2,000 for M1 and Rs 4,000 for M2. The column adds up to Rs 6,000 where April's orders
were worth Rs 8,000, and M1's second order has vanished into an average.

- a, "Rs 8,000": April's true total, which the cell holds only with `aggfunc="sum"`.
- c, "Rs 3,000": the mean of the two cells, an average taken twice.
- d, "Rs 2,667": the mean of April's three orders, which no cell holds.

### Q2. What goes back to an analyst whose months view adds up to less than its orders?

The view's columns add up to Rs 3,10,000 and Rs 2,90,000; its orders total Rs 8,40,000.

The key is d, "Its cells are not totals: Rs 6,00,000 against Rs 8,40,000; name the aggfunc". A view
of spend has to hold its source's total. Rs 6,00,000 against Rs 8,40,000 says the cells are
something other than sums, and the default mean is the usual cause, so the analyst says which
`aggfunc` the view used before anyone reads a fall off it.

- a, "Ship it, since the fall of 6.5 percent comes from the view's own columns": a fall read from
  averages is the fall of a typical order, and the head of the tier asked about spend.
- b, "Rebuild it with `fill_value=0`, since the empty months pulled the sums down": an empty cell adds
  nothing to a sum whether it is blank or 0, so the fill cannot close a Rs 2,40,000 gap.
- c, "Rs 2,40,000 of orders is missing, so the index must have dropped members": the gap is real, and
  a dropped member is one cause; the cheaper test comes first, since one `aggfunc` explains a short
  total with every member present.

### Q3. Which shape should carry the tier's twelve-month trend next year, sized on its rows and empty cells?

A design item. 150 members, about 540 member-months with orders, 12 months, one line on one slide.

The key is c, "The long table: 540 rows, none empty, one total a month by `groupby`". A
trend is one number per month, and grouping the long table by month gives it from 540 rows with
nothing empty.

- a, "The wide table: 1,800 cells, 1,260 of them empty, read along each member's row": 150 members
  by 12 months is 1,800 cells, 1,260 of them empty, and it is read along a member's row, which is a
  comparison; the trend needs its columns summed first.
- b, "A query per month: 12 columns written by hand, and a 13th month is an edit": every new month is
  an edit and a place for a typo.
- d, "The pivot indexed by order: a row per order and 12 columns, nearly all empty": each row is an
  order, the wrong thing for any member or tier question.

### Q4. What shape is the tier's pivot with months as the index and members as the columns?

355 orders, 107 members, six months, months on the index.

The key is a, "6 by 107". The index decides what one row is, here a month, and the columns are the
107 members who ordered. The orders are folded into the cells.

- b, "107 by 6": the member view, with `index` and `columns` the other way round.
- c, "355 by 6": the view indexed by order, one row per order.
- d, "6 by 355": treats each order as a column, which no argument in the call asks for.

### Q5. Which fact would move the months view from pandas into the warehouse?

A design item. The view lives in pandas, long and wide together.

The key is b, "Finance asks to rerun the view every Monday beside its revenue query". Once Finance
reruns it every week, the view belongs where the data lives and where Finance can run it, as a query
with a table of months, which grows by itself when October arrives.

- a, "The head of Retail-Plus asks for October once its orders arrive": pandas adds a month with no
  edit, while a query with hand-written columns would need one.
- c, "The tier grows from 120 members to 400, so the wide table gets longer": more rows suit pandas
  as well as SQL at this size.
- d, "Members place several orders a month, so each cell needs a sum": they already do, and
  `aggfunc="sum"` handles it in pandas.

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
