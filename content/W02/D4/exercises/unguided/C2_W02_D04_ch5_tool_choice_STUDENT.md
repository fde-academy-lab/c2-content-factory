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
and plain Python reading the orders with their segment and adding them up in a dictionary. Each
route returned the same eight rows, and Finance's number went to SQL, where Anand's analyst can
rerun it. The growth team's table reconciled with Finance's query in every segment.

**Who needs the answer.** Kavya, and behind her Anand Iyer. A number that lives in two tools drifts
into two numbers, and two numbers for one metric costs a month of argument before anyone acts on
either.

**The questions on the way.**

- How many rows does each route move for Finance's eight numbers when the orders reach 50 lakh?
- Which line of a draft tool-choice note does Kavya send back?
- What does Kavya say to a note that gives Finance's number to pandas because it ran fastest?
- Which input should pandas read for Finance's five new cuts, and how many rows does it move?
- Which Monday check would catch a merge that counted one customer's spend twice?

Every number about next year in items 1 and 4 and every timing in item 3 is invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. How many rows does each route move for Finance's eight numbers when the orders reach 50 lakh?

Next year Kalpa Retail's warehouse holds 50 lakh orders and 2 lakh customers. Each route still
answers Finance's eight numbers the way chapter 5 wrote it. How many rows does each move out of the
warehouse?

a) Each route moves 8 rows, since every route returns the same eight numbers.
b) SQL moves 8 rows, pandas 52 lakh and plain Python 50 lakh.
c) SQL moves 2 lakh rows, pandas 52 lakh and plain Python 50 lakh.
d) SQL moves 8 rows, pandas 50 lakh and plain Python 52 lakh.

### Q2. Which line of a draft tool-choice note does Kavya send back?

A teammate's draft note gives an owner to each of four asks the team expects next quarter:

1. Finance's revenue by segment and quarter goes to SQL in the warehouse, where Finance reruns it.
2. The growth team's customer table goes to pandas reading the warehouse, since the analysts add a
   column most weeks.
3. A customer's question about why her spend reads what it does goes to plain Python, each of her
   orders added with its step printed.
4. The stores team's orders by channel, which the stores team reruns every morning, go to plain
   Python, in a script anyone can read line by line.

Which line goes back, and why?

a) Line 1 goes back, since Finance's number belongs in the notebook the table comes from.
b) Line 2 goes back, since the customer table should be a SQL view that Finance reruns.
c) Line 3 goes back, since one customer's question reads best as a short pandas chain.
d) Line 4 goes back, since a number another team reruns every morning belongs in SQL.

### Q3. What does Kavya say to a note that gives Finance's number to pandas because it ran fastest?

A hurried note reads: "pandas 0.009 seconds, SQL 0.012, plain Python 0.021, on 1,000 orders, so
Finance's number goes to pandas." What does Kavya say?

a) She agrees, since pandas was fastest and speed is what Finance waits on.
b) She asks for each route to be timed a hundred times, with the number going to the median's winner.
c) She says hundredths of a second decide nothing on a weekly number, and sizes by rows moved.
d) She says SQL should win anyway, since a database always beats a laptop.

### Q4. Which input should pandas read for Finance's five new cuts, and how many rows does it move?

Next year the warehouse holds 50 lakh orders and 2 lakh customers. This afternoon Finance wants its
revenue cut five ways in pandas before it picks one: by segment, by channel, by city, by segment and
channel, and by city and quarter. Kalpa has 4 segments, 3 channels and 6 cities, and the orders
cover 2 quarters. Which input should pandas read?

a) It should read every order with its segment and city, 50 lakh rows, so any cut can be tried.
b) It should read one query grouped by segment, quarter, channel and city, at most 144 rows.
c) It should read Finance's Monday answer, the eight rows of segment by quarter, already computed.
d) It should read the growth team's customer table, 2 lakh rows, already in memory.

### Q5. Which Monday check would catch a merge that counted one customer's spend twice?

The growth team's table and Finance's query must agree every Monday, and about ten customers join
the list in a typical week. Which check catches a refresh whose merge gave one customer who
ordered two rows, so their spend counts twice?

a) Compare the table's spend by segment with Finance's query, to the rupee.
b) Compare the table's row count with last Monday's row count.
c) Run Finance's query twice, to see that it returns the same eight numbers.
d) Compare the table's spend with the sum the previous cell printed.
