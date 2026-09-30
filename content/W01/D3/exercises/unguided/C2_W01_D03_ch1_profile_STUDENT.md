# What did the ERP actually send, and does the dashboard's Rs 2.1 crore follow from it?

Chapter 1 set, 4 items, about 12 minutes, after chapter 1. The ERP is the enterprise resource planning system Finance books orders in. Kalpa Retail's dashboard reads an export of orders from it and puts Q1 revenue at Rs 2.1 crore, while the books, Finance's own record of Q1, say Rs 1,90,00,000 to the rupee.

> "How many records did you receive, and how many can you use?"
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand Iyer, the finance controller, decides whether Finance acts at all on the drop the team reported on Tuesday, the fall from Q1 to Q2 measured on the export as delivered. Tonight his analyst ties out every figure: she matches each one to the books line by line, so a rupee's difference is a finding. A wrong count costs the most of the day, since every later number stands on it. A note that calls the dashboard right when it is not makes the analyst discount everything the team sends, and Marketing loses a month.

**The questions on the way.**

- Should the note on the largest Q2 order go to Anand?
- Which plan fits the 45 minutes before the analyst starts?
- How many rows are copies, and how many amounts cannot be read?
- Which route counts the distinct ids of 4 crore rows with 2 GB free?

Both of Anand's figures count booked value, every order at the price charged, whatever its status. Chapter 1 profiled the export before totalling anything: for every field it counted the values present, the values that convert to the type the field needs, and the distinct values. The profile found 201 rows for 186 distinct order ids and one amount that does not convert, and Q1 over the 200 amounts that do convert is Rs 2,09,98,210, so the dashboard's Rs 2.1 crore is honest arithmetic on this file. Kalpa's Business segment is its sales to companies, every order in lakhs.

Every number in the items is invented unless the item says it comes from today's file, and the reasoning is the one you ran on Kalpa's export. An item marked Design asks you to combine two of the day's ideas, or to size the options yourself, before you choose.

**What you post.** One line of 4 letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

### Q1. Should the note on the largest Q2 order go to Anand?

A colleague's note to Anand names Rs 980 as the largest Q2 order in a new export, found by calling `max()` on the amounts as the CSV gave them. The same export's profile shows 21 Business orders, the smallest of them Rs 2,10,000. What do you tell the colleague before the note goes?

a) Send it, since max() looked at every Q2 amount the file holds
b) Send it, adding that Business orders are counted apart
c) Hold it: no largest order sits below every Business order
d) Hold it until the ERP team confirms Rs 980 is the true value

### Q2. Which plan fits the 45 minutes before the analyst starts? (Design)

A new export of 1.2 crore rows and 12 fields lands, and Anand's analyst starts work in 45 minutes. The team's profile reads about 20 lakh values a minute. Which plan fits the 45 minutes?

a) Profile all 12 fields, then read the rows the profile flags
b) Profile order_id and amount, then read the rows they flag
c) Tie out a random sample of 10,000 rows against the books
d) Total every amount, then set the total beside the books

### Q3. How many rows are copies, and how many amounts cannot be read?

An invented export holds 250 rows, 238 distinct order ids and 247 amounts that convert. How many rows could inflate revenue as copies, and how many amounts sit outside every total until someone reads them?

a) 12 copies and 3 unreadable amounts
b) 3 copies and 12 unreadable amounts
c) 15 copies and no unreadable amounts
d) 9 copies and 3 unreadable amounts

### Q4. Which route counts the distinct ids of 4 crore rows with 2 GB free? (Design)

Next quarter's export will hold 4 crore rows. A Python set of order ids takes about 100 bytes an id, and the laptop the team leaves running overnight has 2 GB free. Which route counts the distinct order ids?

a) A set of every id, then its length, as chapter 1 did
b) A Counter over every id, which also keeps how often each appears
c) A set of the first crore ids, with the answer times four
d) Sort the ids on disk, then count each change from the last
