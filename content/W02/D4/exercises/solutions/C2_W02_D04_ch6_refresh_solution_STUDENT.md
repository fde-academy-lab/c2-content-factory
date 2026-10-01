# Which answers hold in the chapter 6 set on the Monday refresh, and why?

Answers: 1b 2c 3d 4a 5a

The growth team sends a win-back code to every customer the Monday table flags as lapsed: no order in
the 60 days before the table's as-of date, the last date the data covers. Recency is the days from a
customer's last order to that date, and the warehouse's last order is dated 28 September 2026.
Chapter 6 made the table rebuild itself in one function that counts recency to the data's own last
date, carries it as `as_of`, and refuses to write a table that fails any of four guards: one row per
customer, 340 rows, spend of Rs 19,84,00,000, and a smallest recency of 0. The honest win-back list
holds 111 customers. Two of the five items are design items: 3 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. A refresh runs
with nobody watching, so the guards are the only reviewer it has, and each one has to fire on the
failure it is there for.

**The questions on the way.**

- Which idea does the chapter 6 set test?
- Why does each of the five keys hold, from a customer's 20 May order to the cost of the wrong list?
- Why is option a in item 2, "none fires", the wrong answer worth arguing about?
- Where did a daily refresh drop rows with nobody noticing?

## Which idea does the chapter 6 set test?

A job that runs unattended needs two properties: it gives the same answer whenever it runs on the
same data, and it refuses to ship a table that breaks what the business relies on. The set asks for
an honest recency on new dates, which guard reads a suspicious run, how the refresh should run when
its reader changes, which guard catches which break, and what the wall-clock count costs.

## Why does each of the five keys hold, from a customer's 20 May order to the cost of the wrong list?

### Q1. What recency does each refresh give a customer whose last order was 20 May?

An invented store: data ends 30 June, the run is on 13 July, the line is 45 days.

The key is b, "41 days, not lapsed on a 45-day line". The honest refresh counts to the data's last
date, 30 June: 11 days left in May and 30 in June make 41, under the line.

- a, "54 days, lapsed on a 45-day line": counted to the run day, 13 July, so the customer gets a
  win-back code the data never justified.
- c, "13 days, the gap between the data's end and the run": the gap between the two dates, which is
  how much staler the wall-clock count makes every customer, not anyone's recency.
- d, "41 days now, and lapsed by the run day, 13 days later": by the run day the data has not moved,
  so the customer is as recent as on 30 June.

### Q2. Which guard fires on a run whose smallest recency is 7 days?

The run reports 340 rows, the warehouse's spend, `as_of` 28 September and a smallest recency of 7.

The key is c, "The recency guard: recency was counted to a day after 28 September". The as-of date is
the date of the last order, so at least one customer ordered on it, and counted to that date their
recency is 0. A smallest recency of 7 says the days were counted to 5 October, a week the data never
saw.

- a, "None, since rows, spend and the as-of date all agree with the warehouse": three guards pass,
  and the fourth fails.
- b, "The spend guard, as recency counted wrongly moves spend between customers": recency is a count
  of days and never touches spend.
- d, "The recency guard, since nobody can buy in a quarter's last 7 days": the right guard for a
  wrong reason; customers buy on every day, and one bought on 28 September.

### Q3. How should the refresh run once its only reader is a dashboard that queries the warehouse?

A design item. The CSV stops being read; a dashboard reads the warehouse.

The key is d, "A SQL view the dashboard reads, with the four checks as the warehouse's own tests".
Chapter 6 chose the pandas function because the growth team read its output; once the only reader
queries the warehouse, the table belongs there, and the guards move with it so a broken table still
never reaches a viewer.

- a, "The pandas function with guards, writing a CSV the dashboard imports weekly": a second copy for
  a reader that already queries the source.
- b, "A by-hand rerun of the notebooks before the dashboard's first viewer arrives": a check that
  depends on someone noticing.
- c, "A function that prints PASS or FAIL beside each check and writes the table anyway": the table
  ships with its failure printed beside it.

### Q4. Which guard is the only one to fire on each of three broken tables?

Three broken copies, four guards.

The key is a, "count, recency, spend". Dropping the 39 who never ordered leaves 301 rows, which only
the count guard sees, since their spend is 0 and they have no recency. Counting to 19 October makes
the smallest recency 21, which only the recency guard sees. Adding one order's amount twice moves
spend off the warehouse's total, which only the spend guard sees.

- b, "key, recency, spend": dropping rows leaves every remaining key unique.
- c, "count, spend, recency": the wrong date changes recency, never spend, and a doubled amount
  changes spend, never recency.
- d, "count, recency, key": a doubled amount changes a number in a row and adds no row.

### Q5. What do the wall-clock refreshes cost in win-back codes nobody needed?

A design item. 166 and 187 counted to the run days, 111 honest, an invented Rs 150 a code.

The key is a, "Rs 8,250 on 19 October, Rs 11,400 on 2 November". The codes nobody needed are the
customers on the wrong list and not on the honest one: 55 on 19 October and 76 on 2 November, at Rs
150 each, with no new data loaded.

- b, "Rs 24,900 on 19 October, the whole list's codes": prices every code, the 111 that were needed
  among them.
- c, "Rs 8,250 each Monday, since a sent list is fixed": the wall-clock list grows every Monday with
  no new data, and so does the cost.
- d, "Rs 16,650 on 19 October, the honest list's codes": prices the codes that were needed.

## Why is option a in item 2, "none fires", the wrong answer worth arguing about?

Item 2, option a is how a refresh gets waved through: three of the four numbers agree with the
warehouse, and the fourth looks like a statistic about customers. The smallest recency is a property
of the date the count ran to. Somebody always bought on the data's last day, so anything above 0 says
the count ran past the data, whatever the other three guards say.

## Where did a daily refresh drop rows with nobody noticing?

Public Health England's statement of 4 October 2020 said "15,841 cases between 25 September and 2
October were not included in the reported daily COVID-19 cases". The Register reported the cause:
results "automatically fetched in CSV format" from commercial laboratories were stored in the older
.XLS format, "that limited the number of rows to 65,536 per spreadsheet" (The Register, 5 October
2020; both checked 1 Oct 2026). A count of rows in against rows out, run every day, would have
stopped the first short run.
