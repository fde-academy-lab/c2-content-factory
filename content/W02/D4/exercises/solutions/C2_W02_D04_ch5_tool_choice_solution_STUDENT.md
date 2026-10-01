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
produce it. The set asks for the rows moved at a larger scale, the wrong line in a draft note, the
reply to a note that sized by speed, the fact that would give one of Finance's asks to pandas, and
the check that ties the growth team's table to Finance's query.

## Why does each of the five keys hold, from 50 lakh orders to the Monday reconciliation?

### Q1. How many rows does each route move for Finance's eight numbers when the orders reach 50 lakh?

A design item. 50 lakh orders, 2 lakh customers, the same three routes.

The key is b, "SQL 8, pandas 52 lakh, plain Python 50 lakh". SQL sends its answer, 8 rows, however
many orders sit behind it. pandas reads every order and every customer, 50 lakh and 2 lakh, to merge
and group them. Plain Python reads every order with its segment already joined, 50 lakh.

- a, "8 each, since every route returns the same eight numbers": sizes the answer, which ties, in
  place of the work, which does not.
- c, "SQL 2 lakh, pandas 52 lakh, plain Python 50 lakh": SQL groups by segment and quarter, not by
  customer, so it sends 8 rows.
- d, "SQL 8, pandas 50 lakh, plain Python 52 lakh": swaps the two routes; pandas is the one that
  reads the customer list as well.

### Q2. Which line of a draft tool-choice note does Kavya send back?

A design item. Four lines, one wrong.

The key is d, "Line 4: a step-by-step audit of one case reads best as a plain loop". The auditor's
question is asked once and has to be read line by line; a pandas chain is short and hides its middle
steps, while a loop shows each order being added.

- a, "Line 1: Finance's number belongs in the notebook the table comes from": a notebook runs on a
  copy on one machine, and Finance cannot rerun it from the warehouse.
- b, "Line 2: the customer table should be a SQL view that Finance reruns": Finance reruns its
  revenue; the customer table is the growth team's bench, which gains a column most weeks.
- c, "Line 3: a months view is a one-off and belongs in plain Python": the head of Retail-Plus reads
  the view every week, and `pivot_table` builds it in one line.

### Q3. What does Kavya say to a note that gives Finance's number to pandas because it ran fastest?

Invented timings of 0.08, 0.11 and 0.21 seconds on 1,000 orders.

The key is c, "These timings tie and swap from run to run; size by rows moved". On a thousand orders
every route finishes well inside a second, and the ranking changes from one run to the next, so speed
separates nothing. Rows moved and who reruns the number do.

- a, "Agreed: pandas was fastest, and speed is what Finance waits on": Finance waits on a number it
  can rerun, which a notebook on the analyst's machine is not.
- b, "Time each route a hundred times and give the number to the median's winner": a steadier timing
  still answers a question that separates nothing at this size.
- d, "SQL should win anyway, since a database always beats a laptop": SQL wins here on rows moved and
  on who reruns it; "always faster" is false on small data.

### Q4. Which new fact would move one of Finance's asks onto pandas?

A design item. SQL owns Finance's revenue.

The key is b, "Finance wants a new cut, tried five ways this afternoon, then dropped". Iteration on a
question asked once is pandas' work, and pandas reads the query's answer, so the definition still
lives in one place.

- a, "Finance adds a ninth number every Monday, for a new segment": a recurring number Finance reruns
  stays in the warehouse.
- c, "The orders table grows tenfold, so the query takes longer each Monday": growth argues harder for
  SQL, which still sends only its answer.
- d, "Finance's new analyst prefers Python to SQL for every rerun": a preference is not a fact about
  the number; the analyst can run the query from Python.

### Q5. Which Monday check would catch a merge that counted one customer's spend twice?

A design item. About ten customers join the list in a typical week.

The key is a, "The table's spend by segment against Finance's query, to the rupee". The two share no
code, so a customer whose spend is counted twice in the table makes that segment's total disagree
with Finance's query by exactly that customer's spend.

- b, "The table's row count against last Monday's row count": new customers move the count every
  week, so one extra row hides among the sign-ups.
- c, "Finance's query run twice, to see it returns the same eight numbers": checks Finance's side
  against itself and never looks at the table.
- d, "The table's spend against the sum the previous cell printed": the table checked against
  itself.

## Why is option b in item 3, timing each route a hundred times, the wrong answer worth arguing about?

Item 3, option b sounds rigorous: more runs, a median, a fair contest. It measures the wrong thing
more carefully. A sizing column where every option scores the same separates nothing, and timing it
a hundred times does not change that; the columns that separate the routes are rows moved and who has
to rerun the number.

## Where does one metric living in many places come up at work?

LinkedIn's engineering page for its Unified Metrics Platform says that before it, "multiple
stakeholders come up with different ways to calculate the same metric arriving at slightly different
results", and that the platform now "serves as the single source of truth for all business metrics
at Linkedin" (LinkedIn Engineering, Unified Metrics Platform, checked 1 Oct 2026).
