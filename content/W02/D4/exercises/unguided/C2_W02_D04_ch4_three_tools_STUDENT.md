# Of the 130 customers the sale reached, how many bought, and do plain Python, SQL and pandas agree?

Chapter 4 set, five items, after chapter 4: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "You did the tree in plain Python in Week 1, in SQL on Monday. Do it a third way now, and tell me
> honestly which tool you would pick for which job."
>
> Kavya Nair, senior analyst, Kalpa Retail data team

The marketing lead's November budget case has a second line after the reach: the share of reached
customers who bought, meaning reached customers with at least one order between April and September
2026, over all the customers reached. It says who bought at some point; whether they bought because
of the sale is a separate test. A customer's segment is one of Kalpa Retail's four: Retail-Core,
Retail-Plus, Student or Business.

Chapter 4 asked the question in plain Python, SQL and pandas, and the three agreed once each read a
customer's segment from the customer list, where every customer has one: 107 of the 130 reached
customers bought, 82 percent, made up of 56 of 70 in Retail-Core and 51 of 60 in Retail-Plus. A set
difference, with no grouping at all, found the same 107. Kavya's rule when two tools disagree is to
look for the rows one of them dropped before looking at the code.

**Who needs the answer.** The marketing lead, through Kavya. A share that leaves out the reached
customers who never bought makes the sale look perfect, and the budget asked for on it repeats a
campaign on numbers nobody earned.

**The questions on the way.**

- What does a default `groupby` report for five invented reached customers?
- What do SQL's `GROUP BY` and pandas' `groupby` each do with a customer whose segment is missing?
- What is the first check on a dashboard that says 96 percent of 1,250 reached customers bought?
- Which pairing does Kavya sign once the share goes to Finance's quarterly audit?
- Which line gives the share who bought with no group that could drop anyone?

Every customer and number in items 1, 3 and 5 is invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. What does a default `groupby` report for five invented reached customers?

Five invented reached customers. C and E never ordered, so their segment, read from their orders,
is missing:

```python
reach = pd.DataFrame({"customer_id": ["A", "B", "C", "D", "E"],
                      "segment": ["Retail-Core", "Retail-Plus", None, "Retail-Plus", None],
                      "bought": [1, 1, 0, 0, 0]})
out = reach.groupby("segment")["bought"].agg(["size", "sum"])
```

Adding up `out`, how many customers does it count, and what share of them bought?

a) 5 customers, 40 percent
b) 3 customers, 67 percent
c) 5 customers, 67 percent
d) 3 customers, 40 percent

### Q2. What do SQL's `GROUP BY` and pandas' `groupby` each do with a customer whose segment is missing?

An interviewer asks what each tool does, by default, with rows whose grouping key is missing. Which
answer is right?

a) SQL keeps one `NULL` group; pandas drops it unless `dropna=False`
b) Both drop the rows, since a group needs a value to be named by
c) SQL drops the `NULL` rows; pandas keeps them in a group named NaN
d) Both keep one group for it, `NULL` in SQL and NaN in pandas

### Q3. What is the first check on a dashboard that says 96 percent of 1,250 reached customers bought?

A campaign dashboard says 96 percent of 1,250 reached customers bought. The campaign platform's feed
for the same campaign names 1,480 customers. What does the first check find?

a) A rerun of the dashboard's query on the same data surfaces the gap
b) 1,200 bought of 1,250, recomputed by hand, which confirms 96 percent
c) The 50 of the 1,250 who did not buy are the ones missing from the feed
d) 230 of 1,480 reached are missing; if none bought, it is 81 percent

### Q4. Which pairing does Kavya sign once the share goes to Finance's quarterly audit?

The share who bought was answered in pandas, on the table already in memory, and checked in SQL.
Next quarter the same number goes into Finance's audit pack, which Anand Iyer's analyst reruns from
the warehouse. Which pairing does Kavya sign?

a) pandas answers on the table in memory, and SQL, sending 2 rows, checks it
b) SQL answers where the auditor reruns it; pandas sets check it
c) Plain Python answers, line by line for the auditor, and SQL checks it
d) pandas answers, and the notebook goes to the auditor to rerun it

### Q5. Which line gives the share who bought with no group that could drop anyone?

An invented campaign reached 800 customers; 5,000 customers ordered in the period; 610 customers are
in both groups. In Python, `reached` and `buyers` are sets of customer ids. Which line gives the
share of the reached customers who bought?

a) `len(reached & buyers) / len(buyers)`, which is 12 percent
b) `len(reached - buyers) / len(reached)`, which is 24 percent
c) `len(reached & buyers) / len(reached)`, which is 76 percent
d) `len(buyers - reached) / len(buyers)`, which is 88 percent
