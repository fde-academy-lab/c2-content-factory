# Which answers hold in the chapter 6 set on the Monday refresh, and why?

Answers: 1b 2c 3d 4a 5b

The growth team sends a win-back code to every customer the Monday table flags as lapsed: no order in
the 60 days before the table's as-of date, the last date the data covers. Recency is the days from a
customer's last order to that date, the days from the as-of date to the run day are the data's age,
and the warehouse's last order is dated 28 September 2026. Chapter 6 made the table rebuild itself
in one function that counts recency to the last order it read, carries that date as `as_of`, and
refuses to write a table that fails any of four guards: one row per customer, 340 rows, spend of
Rs 19,84,00,000, and a smallest recency of 0. The honest win-back list holds 111 customers. Two of
the five items are design items: 3 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. A refresh runs
with nobody watching, so the guards are the only reviewer it has, and each one has to fire on the
failure it is there for.

**The questions on the way.**

- Which idea does the chapter 6 set test?
- Why does each of the five keys hold, from a customer's 20 May order to the data that stopped
  arriving?
- Why is option a in item 2, "no guard fires", the wrong answer worth arguing about?
- Where did a daily refresh drop rows with nobody noticing?

## Which idea does the chapter 6 set test?

A job that runs unattended needs two properties: it gives the same answer whenever it runs on the
same data, and it refuses to ship a table that breaks what the business relies on. The set asks for
an honest recency on new dates, what a suspicious smallest recency says, how the refresh builds a
past Monday's table for an auditor, which guard catches which break, and which new guard catches
data that has stopped arriving.

## Why does each of the five keys hold, from a customer's 20 May order to the data that stopped arriving?

### Q1. What recency does the honest refresh write for a customer whose last order was 20 May?

An invented store's data ends on 30 June, its refresh runs on 13 July, and its line is 45 days.

The key is b, "It writes 41 days, so the customer is not lapsed on a 45-day line". The honest
refresh counts to the data's last date, 30 June: 11 days left in May and 30 in June make 41, under
the line. The 13 days from 30 June to the run day are the data's age, which the refresh reports
beside the table, so the store knows its list is 13 days old before anything is sent.

- a, "It writes 54 days, so the customer is lapsed on a 45-day line": It counts to the run day,
  13 July, so the customer gets a win-back code the data never justified.
- c, "It writes 13 days, the gap between the data's end and the run": Those 13 days are the data's
  age on the run day. They say how old the data is and nothing about when this customer last
  ordered.
- d, "It writes 41 days, and the customer turns lapsed by the run day, 13 days later": The data
  shows no order from this customer between 20 May and 30 June, its last day, and it holds nothing
  at all for the 13 days after that, since none of them is loaded. Whether the customer ordered in
  those days is unknown, so the recency stays 41 days to the as-of date, and the 13 days are
  reported as the data's age.

### Q2. What does a smallest recency of 7 days say about this Monday's run?

The run reports 340 rows, the warehouse's spend, an `as_of` of 28 September and a smallest recency
of 7.

The key is c, "The recency guard fires, since the days were counted to 5 October, a week past the
data". The as-of date is the date of the last order, so at least one customer ordered on it, and
counted to that date their recency is 0. A smallest recency of 7 says the days were counted to
5 October, a week the data never saw, so the run stops before any code goes out.

- a, "No guard fires, since rows, spend and the as-of date all agree with the warehouse": Three
  guards pass, and the fourth fails, since the `as_of` column says 28 September while the days were
  counted to another date.
- b, "No guard fires, since a 7 only says nobody happened to order in the data's last week": The
  as-of date is the last order's own date, so somebody ordered on it, and a smallest recency of 7
  cannot come from the customers.
- d, "The recency guard fires, since the days were counted to 21 September, a week before the
  data's end": Counted to an earlier date, the customers who ordered after it get a negative
  recency, so the smallest would read minus 7.

### Q3. How should the refresh build the table as it would have stood on 31 August?

Item 3 is a design item: the auditor wants a past Monday's table, so the refresh needs an input it
never needed before, a cut-off date, and everything that reads the orders has to take it, the spend
guard's total among them.

The key is d, "Cut the orders and the spend guard's total at 31 August, and count recency to the
last order kept". The 848 orders placed before 31 August are worth Rs 17,19,59,570, and the last of
them is dated 28 August, which becomes the table's as-of date, so the smallest recency is 0. The
spend guard compares the table with the warehouse's total over the same orders, Rs 17,19,59,570, so
all four guards pass on a table of 340 customers, 47 of whom had not yet ordered, with a win-back
list of 103.

- a, "Read every order as now, and count recency to 31 August, the day it would have run": It keeps
  September's 152 orders, worth Rs 2,64,40,430, in every customer's numbers, and the 118 customers
  whose last order fell in September get a negative recency, so the recency guard stops it at minus
  28.
- b, "Cut the orders and the spend guard's total at 31 August, and count recency to 31 August": 31
  August is the day the refresh would have run, and the last order before it is dated 28 August, so
  the smallest recency is 3 and the recency guard stops the run. It is chapter 6's run-day count,
  moved back to August.
- c, "Cut the orders at 31 August, count recency to the last order kept, and keep the guards as they
  are": The table is right, and its spend of Rs 17,19,59,570 meets a guard still holding the
  warehouse's full Rs 19,84,00,000, so the spend guard stops a right table.

### Q4. Which guard is the only one to fire on each of three broken tables?

Each of the three broken copies breaks one thing, and each of the four guards checks one thing.

The key is a, "Count fires on copy 1, recency on copy 2 and spend on copy 3". Dropping the 39 who
never ordered leaves 301 rows, which only the count guard sees, since their spend is 0 and they have
no recency. Counting to 19 October makes the smallest recency 21, which only the recency guard sees.
Adding one order's amount twice moves spend off the warehouse's total, which only the spend guard
sees.

- b, "Key fires on copy 1, recency on copy 2 and spend on copy 3": Dropping rows leaves every
  remaining key unique.
- c, "Count fires on copy 1, spend on copy 2 and recency on copy 3": The wrong date changes recency
  and leaves spend alone, and a doubled amount changes spend and leaves recency alone.
- d, "Count fires on copy 1, recency on copy 2 and key on copy 3": A doubled amount changes a number
  in a row and adds no row.

### Q5. Which fifth guard stops a run on stale data and still lets a normal Monday through?

Item 5 is a design item: the four guards cannot see data that has stopped arriving, so a new guard
has to read the calendar, with a tolerance that a normal Monday passes.

The key is b, "The as-of date is no more than seven days before the run day". Comparing the as-of
date with the run day is the one job the wall clock keeps, and the gap is the data's age. On a
normal Monday the orders end the day before, an age of 1 day, which passes; after two weeks of
failed loads the age is 15 days, which stops the run before any code goes out and says how old the
data is.

- a, "The as-of date is the run day itself": On a normal Monday the orders end on Sunday, so this
  guard stops every run, and a guard that fires every week is soon switched off.
- c, "The win-back list holds no more customers than last Monday's list": With no new orders loaded,
  this Monday's list repeats last Monday's, so it passes, and it would stop an honest week in which
  more customers lapse.
- d, "The spend still equals the warehouse's total when rechecked before the send": The warehouse is
  the stale source, so the table still equals its total. Two of the four guards compare the table
  with the warehouse, which is stale too, and two check the table's own shape, the recency guard
  passing because the as-of date comes from the same orders, so none of them can see a load that
  stopped.

## Why is option a in item 2, "no guard fires", the wrong answer worth arguing about?

Item 2, option a is how a refresh gets waved through: three of the four numbers agree with the
warehouse, and the fourth looks like a statistic about customers. The smallest recency is a property
of the date the count ran to. Somebody always bought on the data's last day, so anything above 0
says the count ran past the data, whatever the other three guards say.

## Where did a daily refresh drop rows with nobody noticing?

Public Health England's statement of 4 October 2020 said "15,841 cases between 25 September and 2
October were not included in the reported daily COVID-19 cases". The Register reported the cause:
results "automatically fetched in CSV format" from commercial laboratories were stored in the older
.XLS format, "that limited the number of rows to 65,536 per spreadsheet" (The Register, 5 October
2020; both checked 1 Oct 2026). A count of rows in against rows out, run every day, would have
stopped the first short run.
