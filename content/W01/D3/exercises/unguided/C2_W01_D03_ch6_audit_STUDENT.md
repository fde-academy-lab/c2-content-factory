# Chapter 6 set: the log the analyst audits

4 items, about 12 minutes, after chapter 6. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask you to combine two of the day's ideas or to size the options yourself before you choose.

Post one line, 4 letters in item order, no spaces:

```
Post exactly this shape: xxxx
```

---

### Q1

A pass reports 500 rows in, 470 kept and 30 set aside, and its Q1 comes out Rs 2,100 below the books' Rs 3,20,00,000. What do you do next?

a) Ship it, since the rows reconcile and Rs 2,100 is a rounding error
b) Add a Rs 2,100 adjustment line, labelled, so the rupees tie
c) Find the set-aside row whose value its kept twin lacks
d) Ask Finance whether its books carry Rs 2,100 too much

### Q2 (Design)

Put the pass in order for Anand's analyst: 1 apply the identity rule, keeping the copy whose amount converts; 2 reconcile rupees to the books; 3 convert the kept amounts and log any that fail; 4 reconcile rows, in equals kept plus set aside plus rejected. Which order holds?

a) 1, 3, 4, 2
b) 3, 1, 4, 2
c) 1, 4, 3, 2
d) 3, 4, 1, 2

### Q3 (Design)

Anand's analyst has 20 minutes tonight and reads a line in about 30 seconds. Your pass set aside 24 rows, flagged 4, made 5 decisions and ties 2 control totals, on a raw file of 900 rows and a clean file of 876. Which hand-over fits her 20 minutes?

a) The clean file, to read against the raw one, line by line
b) A full diff of the raw and clean files, a line per raw row
c) The clean file, with one line saying 24 rows were set aside
d) The set-aside, flags and decisions logs, with both totals

### Q4 (Design)

The analyst asks how she can know the log is complete without trusting the code that wrote it. Which test gives her that?

a) Count the log's lines and compare them with the rows removed
b) Rebuild the clean file from the raw export and the log alone
c) Read every line of the log and check that each has a reason
d) Rerun the pass and compare the new log with the old, line by line
