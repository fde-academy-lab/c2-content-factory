# Which tool should own each of Marketing's and Finance's recurring numbers, and which would you refuse for Finance?

Chapter 5 set, five items, after chapter 5: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "Tell me honestly which tool you would pick for which job, and which one you would refuse for
> Finance's numbers."
>
> Kavya Nair, senior analyst, Kalpa Retail data team

Kavya asked for a tool-choice note: which of plain Python, SQL and pandas should own each recurring
number, with a reason per tool. Anand Iyer, Kalpa Retail's finance controller, has an analyst who
reruns every number the team sends, line by line, from the warehouse, Kalpa's Postgres database.
Finance's Monday revenue is eight numbers, four segments by two quarters, adding up to
Rs 19,84,00,000.

Chapter 5 sized three routes to those eight numbers on Kalpa's 1,000 orders and 340 customers: SQL
grouping in the warehouse; pandas reading the orders and the customer list, merging and grouping;
and plain Python reading the orders with their segment and adding them up in a dictionary. Each route
returned the same eight rows. SQL moved 8 rows out of the warehouse to produce them, pandas 1,340 and
plain Python 1,000, and Finance's number went to SQL, where Anand's analyst can rerun it. The growth
team's table reconciled with Finance's query in every segment.

**Who needs the answer.** Kavya, and behind her Anand Iyer. A number that lives in two tools drifts
into two numbers, and two numbers for one metric costs a month of argument before anyone acts on
either.

**The questions on the way.**

- How many rows does each route move for Finance's eight numbers when the orders reach 50 lakh?
- Which line of a draft tool-choice note does Kavya send back?
- What does Kavya say to a note that gives Finance's number to pandas because it ran fastest?
- Which new fact would move one of Finance's asks onto pandas?
- Which Monday check would catch a merge that counted one customer's spend twice?

Every number about next year in item 1 and every timing in item 3 is invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. How many rows does each route move for Finance's eight numbers when the orders reach 50 lakh?

Next year Kalpa Retail's warehouse holds 50 lakh orders and 2 lakh customers. Each route still
answers Finance's eight numbers the way chapter 5 wrote it. How many rows does each move out of the
warehouse?

a) 8 each, since every route returns the same eight numbers
b) SQL 8, pandas 52 lakh, plain Python 50 lakh
c) SQL 2 lakh, pandas 52 lakh, plain Python 50 lakh
d) SQL 8, pandas 50 lakh, plain Python 52 lakh

### Q2. Which line of a draft tool-choice note does Kavya send back?

A draft note, four lines:

1. Finance's revenue by segment and quarter: SQL in the warehouse, which Finance reruns.
2. The growth team's customer table: pandas reading the warehouse; the analysts add a column most
   weeks.
3. The head of Retail-Plus's months view: pandas, `pivot_table` with its `aggfunc` written out.
4. An auditor's question about one customer's spend, step by step: a pandas chain, the shortest code.

Which line goes back, and why?

a) Line 1: Finance's number belongs in the notebook the table comes from
b) Line 2: the customer table should be a SQL view that Finance reruns
c) Line 3: a months view is a one-off and belongs in plain Python
d) Line 4: a step-by-step audit of one case reads best as a plain loop

### Q3. What does Kavya say to a note that gives Finance's number to pandas because it ran fastest?

A hurried note reads: "pandas 0.08 seconds, SQL 0.11, plain Python 0.21, on 1,000 orders, so
Finance's number goes to pandas." What does Kavya say?

a) Agreed: pandas was fastest, and speed is what Finance waits on
b) Time each route a hundred times and give the number to the median's winner
c) These timings tie and swap from run to run; size by rows moved
d) SQL should win anyway, since a database always beats a laptop

### Q4. Which new fact would move one of Finance's asks onto pandas?

SQL owns Finance's revenue. Which of these facts would make pandas, reading the query's answer
rather than the orders, the right home for one of Finance's asks?

a) Finance adds a ninth number every Monday, for a new segment
b) Finance wants a new cut, tried five ways this afternoon, then dropped
c) The orders table grows tenfold, so the query takes longer each Monday
d) Finance's new analyst prefers Python to SQL for every rerun

### Q5. Which Monday check would catch a merge that counted one customer's spend twice?

The growth team's table and Finance's query must agree every Monday, and about ten customers join
the list in a typical week. Which check catches a refresh whose merge gave one customer who
ordered two rows, so their spend counts twice?

a) The table's spend by segment against Finance's query, to the rupee
b) The table's row count against last Monday's row count
c) Finance's query run twice, to see it returns the same eight numbers
d) The table's spend against the sum the previous cell printed
