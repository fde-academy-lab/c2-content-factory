# Can Anand's analyst audit every decision tonight and rebuild the clean file from the log alone?

Chapter 6 set, 4 items, about 12 minutes, after chapter 6. Anand Iyer is Kalpa Retail's finance controller. The clean file is the export of orders from the ERP, the enterprise resource planning system Finance books orders in, after the day's pass, one row per order with every defect decided in writing, and the log is the set of files in which the pass records what it removed, flagged and decided, and why.

> "Send the reconciliation and the log before the day closes. My analyst checks it tonight."
>
> Anand Iyer, finance controller, Kalpa Retail

Chapter 5 proved today's Q1 with a bridge, a walk from one total to another, one cause to a step: Rs 2,09,98,210 as exported, less Rs 19,67,560 of copies of corporate orders and Rs 30,650 of copies of consumer orders, lands on the books, Finance's own record of Q1, at Rs 1,90,00,000. The identity rule is the rule that decides when two rows are one order. The pass writes four logs. The set-aside log holds every row the pass removed, with its reason and the line of its twin, the row of the same order that stayed; the rejects log holds every value that would not convert; the flags log holds every record kept with a question on it; and the decisions log holds each rule with the rows and rupees it moved. Control totals are a count and a sum computed at both ends of a transfer and compared, here rows and rupees.

**Who needs the answer.** Anand's analyst checks the logs tonight, and an auditor may ask next quarter why any row went. A log she cannot follow costs a week of questions, and a log that fails her tie-out, which matches every figure to the books line by line, costs the team her trust in everything else it sends.

**The questions on the way.**

- What do you do next with a pass Rs 2,100 below the books?
- In what order does the pass run for Anand's analyst?
- Which hand-over fits the analyst's 20 minutes?
- Which test shows the log is complete without trusting the code that wrote it?

Every number in the items is invented unless the item says it comes from today's file, and the reasoning is the one you ran on Kalpa's export. An item marked Design asks you to combine two of the day's ideas, or to size the options yourself, before you choose.

**What you post.** One line of 4 letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

### Q1. What do you do next with a pass Rs 2,100 below the books?

A pass reports 500 rows in, 470 kept and 30 set aside, and its Q1 comes out Rs 2,100 below the books' Rs 3,20,00,000. What do you do next?

a) Ship it, since the rows reconcile and Rs 2,100 is a rounding error
b) Add a Rs 2,100 adjustment line, labelled, so the rupees tie
c) Find the set-aside row whose value its kept twin lacks
d) Ask Finance whether its books carry Rs 2,100 too much

### Q2. In what order does the pass run for Anand's analyst? (Design)

Put the pass in order for Anand's analyst: 1 apply the identity rule, keeping the copy whose amount converts; 2 reconcile rupees to the books; 3 convert the kept amounts and log any that fail; 4 reconcile rows, in equals kept plus set aside plus rejected. Which order holds?

a) 1, 3, 4, 2
b) 3, 1, 4, 2
c) 1, 4, 3, 2
d) 3, 4, 1, 2

### Q3. Which hand-over fits the analyst's 20 minutes? (Design)

Anand's analyst has 20 minutes tonight and reads a line in about 30 seconds. Your pass set aside 24 rows, flagged 4, made 5 decisions and ties 2 control totals, on a raw file of 900 rows and a clean file of 876. Which hand-over fits her 20 minutes?

a) The clean file, to read against the raw one, line by line
b) A full diff of the raw and clean files, a line per raw row
c) The clean file, with one line saying 24 rows were set aside
d) The set-aside, flags and decisions logs, with both totals

### Q4. Which test shows the log is complete without trusting the code that wrote it? (Design)

The analyst asks how she can know the log is complete without trusting the code that wrote it. Which test gives her that?

a) Count the log's lines and compare them with the rows removed
b) Replay the log on the raw export and compare with the clean file
c) Read every line of the log and check that each has a reason
d) Rerun the pass and compare the new log with the old, line by line
