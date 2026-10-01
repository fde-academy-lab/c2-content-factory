# Which answers hold in the chapter 5 set on which tool owns which number, and why?

Answers: 1b 2d 3c 4b 5a

Kavya Nair, the senior analyst, asked for a tool-choice note: which of plain Python, SQL and pandas
should own each recurring number, and which tool would be refused for Finance's numbers. Anand
Iyer's analyst in Finance reruns every number the team sends from the warehouse. Finance's Monday
revenue is eight numbers, four segments by two quarters, adding up to Rs 19,84,00,000. On Kalpa's
1,000 orders and 340 customers, each route returned the same eight rows, while SQL moved 8 rows out
of the warehouse, pandas 1,340 and plain Python 1,000, and Finance's number went to SQL. Four of the
five items are design items: 1, 2, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. The note decides
where each number lives, and a number that lives in two places becomes two numbers.

**The questions on the way.**

- Which idea does the chapter 5 set test?
- Why does each of the five keys hold, from 50 lakh orders to the Monday reconciliation?
- Why is option b in item 3, timing each route a hundred times, the wrong answer worth arguing about?
- Where does one metric living in many places come up at work?

## Which idea does the chapter 5 set test?

A tool is chosen by who has to trust and rerun the number, and sized by what each route moves to
produce it. The set asks for the rows moved at a larger scale, the wrong line in a note for next
quarter's asks, the reply to a note that sized by speed, the input that lets pandas try Finance's
new cuts without moving the orders, and the check that ties the growth team's table to Finance's
query.

## Why does each of the five keys hold, from 50 lakh orders to the Monday reconciliation?

### Q1. How many rows does each route move for Finance's eight numbers when the orders reach 50 lakh?

Item 1 is a design item: there are 50 lakh orders and 2 lakh customers, and the three routes are
written as chapter 5 wrote them.

The key is b, "SQL moves 8 rows, pandas 52 lakh and plain Python 50 lakh". SQL sends its answer, 8
rows, however many orders sit behind it. pandas reads every order and every customer, 50 lakh and 2
lakh, to merge and group them. Plain Python reads every order with its segment already joined, 50
lakh.

- a, "Each route moves 8 rows, since every route returns the same eight numbers": It sizes the
  answer, which ties, in place of the work, which does not.
- c, "SQL moves 2 lakh rows, pandas 52 lakh and plain Python 50 lakh": SQL groups by segment and
  quarter, which makes 8 groups however many customers there are, so it sends 8 rows.
- d, "SQL moves 8 rows, pandas 50 lakh and plain Python 52 lakh": It swaps the two routes, and
  pandas is the one that reads the customer list as well.

### Q2. Which line of a draft tool-choice note does Kavya send back?

Item 2 is a design item: two of the four lines give an ask to plain Python, and only one of them
fits what plain Python is for.

The key is d, "Line 4 goes back, since a number another team reruns every morning belongs in SQL".
The stores team reruns its count every day, so the count has to live where the stores team can run
it, as a query in the warehouse that sends only its answer. A script on the analyst's machine moves
every order each morning and leaves the stores team waiting on the analyst. Line 3 keeps plain
Python because one customer's question is asked once and has to be read step by step.

- a, "Line 1 goes back, since Finance's number belongs in the notebook the table comes from": A
  notebook runs on a copy on one machine, and Finance cannot rerun it from the warehouse.
- b, "Line 2 goes back, since the customer table should be a SQL view that Finance reruns": Finance
  reruns its revenue, and the customer table is the growth team's bench, which gains a column most
  weeks.
- c, "Line 3 goes back, since one customer's question reads best as a short pandas chain": A pandas
  chain is short and hides its middle steps, while a loop shows each of her orders being added.

### Q3. What does Kavya say to a note that gives Finance's number to pandas because it ran fastest?

The note's timings, 0.009, 0.012 and 0.021 seconds on 1,000 orders, are invented.

The key is c, "She says hundredths of a second decide nothing on a weekly number, and sizes by rows
moved". On Kalpa's 1,000 orders all three routes finish in hundredths of a second; timed over and
over, SQL finished first on every run, by about a hundredth of a second. A hundredth of a second on
a number Finance reads once a week decides nothing, so speed cannot choose between the routes. Rows
moved can, 8 for SQL against 1,340 for pandas and 1,000 for plain Python, and that gap grows with the
business.

- a, "She agrees, since pandas was fastest and speed is what Finance waits on": Finance waits on a
  number it can rerun, which a notebook on the analyst's machine is not.
- b, "She asks for each route to be timed a hundred times, with the number going to the median's
  winner": A steadier timing measures the same gap of hundredths of a second, which still decides
  nothing.
- d, "She says SQL should win anyway, since a database always beats a laptop": SQL does own the
  number, because Anand's analyst reruns it and it moves 8 rows. The reason this reply gives is
  speed, and a hundredth of a second decides nothing on a weekly number.

### Q4. Which input should pandas read for Finance's five new cuts, and how many rows does it move?

Item 4 is a design item: the cuts are tried in an afternoon, which is pandas' work, and the orders
run to 50 lakh, so the input has to carry every dimension the cuts need without moving the orders.

The key is b, "It should read one query grouped by segment, quarter, channel and city, at most 144
rows". The five cuts between them use segment, channel, city and quarter, so one answer at that
grain serves all five: 4 segments by 2 quarters by 3 channels by 6 cities is at most 144 rows, and
each cut is a sum of those rows in pandas. The revenue's definition stays in the warehouse's query,
and the rows sent stay at 144 however many orders sit behind them; on today's orders the query
returns 134, since not every combination has an order.

- a, "It should read every order with its segment and city, 50 lakh rows, so any cut can be tried":
  It moves every order to make at most 144 sums, and it writes a second definition of revenue in the
  notebook.
- c, "It should read Finance's Monday answer, the eight rows of segment by quarter, already
  computed": Eight rows carry no channel or city, so only the cut by segment can be made from them.
- d, "It should read the growth team's customer table, 2 lakh rows, already in memory": The table
  holds each customer's spend over both quarters with no channel or quarter, so the three cuts that
  need a channel or a quarter cannot be made from it.

### Q5. Which Monday check would catch a merge that counted one customer's spend twice?

Item 5 is a design item: about ten customers join the list in a typical week, so the check has to
tell one doubled customer from the sign-ups.

The key is a, "Compare the table's spend by segment with Finance's query, to the rupee". The two
share no code, so a customer whose spend is counted twice in the table makes that segment's total
disagree with Finance's query by exactly that customer's spend.

- b, "Compare the table's row count with last Monday's row count": New customers move the count
  every week, so one extra row hides among the sign-ups.
- c, "Run Finance's query twice, to see that it returns the same eight numbers": It checks Finance's
  side against itself and never looks at the table.
- d, "Compare the table's spend with the sum the previous cell printed": It checks the table against
  itself.

## Why is option b in item 3, timing each route a hundred times, the wrong answer worth arguing about?

Item 3, option b sounds rigorous, since a median of a hundred runs is steadier than one run. On
Kalpa's orders it would even give the number to SQL, which finished first on every run, and it would
give it for a gap of about a hundredth of a second, which changes nothing for a number Finance reads
once a week. SQL owns Finance's number because Anand's analyst reruns it from the warehouse and
because it moves 8 rows where pandas moves 1,340, a gap that grows with the orders.

## Where does one metric living in many places come up at work?

LinkedIn's engineering page for its Unified Metrics Platform says that before it, "multiple
stakeholders come up with different ways to calculate the same metric arriving at slightly different
results", and that the platform now "serves as the single source of truth for all business metrics
at Linkedin" (LinkedIn Engineering, Unified Metrics Platform, checked 1 Oct 2026).
