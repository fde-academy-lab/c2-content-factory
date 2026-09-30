# Which answers hold in the chapter 6 set on the log Anand's analyst audits, and why?

Answers: 1c 2a 3d 4b

Anand Iyer's analyst checks the team's logs tonight against the books, Finance's own record of Q1, so every decision the pass made on Kalpa Retail's export has to be one she can audit, and the clean file has to be one she can rebuild from the raw export and the log alone.

Three of the four items are design items: 2, 3 and 4.

### Q1. What do you do next with a pass Rs 2,100 below the books?

A pass reports 500 rows in, 470 kept and 30 set aside, and its Q1 comes out Rs 2,100 below the books' Rs 3,20,00,000.

The key is c, "Find the set-aside row whose value its kept twin lacks". Rows prove no row vanished and say nothing about which rows stayed. The missing rupees sit in a set-aside row whose twin, the kept copy of the same order, cannot be summed.

- a, "Ship it, since the rows reconcile and Rs 2,100 is a rounding error": a gap of any size is an order missing from a file called reconciled.
- b, "Add a Rs 2,100 adjustment line, labelled, so the rupees tie": an adjustment closes the gap without a cause.
- d, "Ask Finance whether its books carry Rs 2,100 too much": the books are the reference until a row proves otherwise.

### Q2 (Design). In what order does the pass run for Anand's analyst?

Four steps to order: 1 apply the identity rule, which decides when two rows are one order, keeping the copy whose amount converts; 2 reconcile rupees to the books; 3 convert the kept amounts and log any that fail; 4 reconcile rows, in equals kept plus set aside plus rejected.

The key is a, "1, 3, 4, 2". The rule has to see which copy converts, so it runs first and keeps a readable copy. Conversion then runs on what was kept, the rows equation needs the rejects count, and the rupee tie comes last, against the books.

- b, "3, 1, 4, 2": step 3 converts the kept amounts, and nothing is kept before the rule runs.
- c, "1, 4, 3, 2": the rows equation counts the rejected rows, which exist only after conversion.
- d, "3, 4, 1, 2": converts and reconciles before anything is kept.

### Q3 (Design). Which hand-over fits the analyst's 20 minutes?

The analyst has 20 minutes and reads a line in about 30 seconds; the pass set aside 24 rows, flagged 4, made 5 decisions and ties 2 control totals, a count and a sum compared at both ends, on a raw file of 900 rows and a clean file of 876.

The key is d, "The set-aside, flags and decisions logs, with both totals". 24 + 4 + 5 + 2 is 35 lines, about 17 and a half minutes, and it ties both totals and lets her replay the pass. The clean file against the raw is 1,776 lines, about 15 hours, and a full diff 900 lines, 7 and a half hours, and neither says why.

- a, "The clean file, to read against the raw one, line by line": about 15 hours, with no reasons.
- b, "A full diff of the raw and clean files, a line per raw row": 7 and a half hours, showing what went with no reason beside it.
- c, "The clean file, with one line saying 24 rows were set aside": one line, which ties the rows and nothing else.

### Q4 (Design). Which test shows the log is complete without trusting the code that wrote it?

The analyst asks how she can know the log is complete without trusting the code that wrote it.

The key is b, "Replay the log on the raw export and compare with the clean file". The replay shares no code with the pass: if the raw export less the logged lines equals the clean file, nothing left without a line.

- a, "Count the log's lines and compare them with the rows removed": counts can match while the rows differ.
- c, "Read every line of the log and check that each has a reason": proves that each line has a reason and says nothing about a removal with no line.
- d, "Rerun the pass and compare the new log with the old, line by line": the same code repeats the same mistakes.
