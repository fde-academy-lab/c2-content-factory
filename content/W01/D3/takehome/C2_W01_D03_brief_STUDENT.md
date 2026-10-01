# Which Q1 total is right on a second export nobody has profiled?

> "The ERP team found another extract from the migration, Q1 only, a different batch. Same drill:
> which total is right, what you set aside and why, and whether it changes anything we said today."
>
> Anand Iyer, finance controller, Kalpa Retail

An extract is one pull of rows out of the ERP, the enterprise resource planning system Finance books
orders in, and the migration is the Q1 move of the order data from one system to another. Today's
export held 201 rows for 186 orders, and the day's pass set aside 15 copies and landed Q1 on the
books, Finance's own record of Q1, at Rs 1,90,00,000. A profile counts, for every field, the values
present, the values that convert and the distinct values.

**Who needs the answer.** Anand Iyer, the finance controller, needs to know whether this second extract
changes anything the team told him today. A total you have not reconciled, or a decision you made
without writing it down, would put an unexplained figure in front of Finance a second time.

**The questions on the way.**

- What does a full pass find in the second extract?
- What does the note to Finance say, and in what order?
- How does `csv.DictReader` turn each line of a CSV into a record?

About two hours tonight. The file is `data/C2_W01_D03_takehome_STUDENT.csv`, and nobody has profiled it
in class. Three of its five defects are kinds you met today, in new places and new amounts; two are
kinds you have not met, so today's counts will not carry over, and the profile is how you find all
five.

## Part 1. What does a full pass find in the second extract?

About seventy minutes; used at work on every new extract before any figure from it is quoted.

In a fresh notebook, using the day's helper, the `c2kit` module every notebook imports as `kit`:

1. Read the file and profile every field: present, convertible, distinct. Write one sentence per
   field on what its counts let you trust.
2. Apply the identity rule, the rule that decides when two rows are one order, keeping the copy whose
   amount converts (the first when both do), and log a reason for every row set aside.
3. Convert the kept amounts with a rejects log. Every row that fails goes into the log with its line,
   field, value and reason, and you read each logged row before deciding anything about it.
4. For every value that converts but is still not an ordinary order, make the three-way decision,
   drop, default or keep and flag, and write the reason. At least one decision tonight has two
   defensible answers; choose one and say what the other would have given.
5. Reconcile twice: rows in equal rows kept plus rows set aside, and rupees as read less the rupees
   set aside equal your clean total. Draw the bridge, the walk from one total to the other one cause
   at a time, with `kit.bridge`.

## Part 2. What does the note to Finance say, and in what order?

About twenty minutes; used at work whenever a reconciliation goes to the person who signs for the
number.

Under 120 words, numbers first: the clean Q1 total and how you know it, the two reconciliations, the
decisions you flagged, and the one decision that moves the total, with the total under each answer.

## Part 3. How does `csv.DictReader` turn each line of a CSV into a record?

About twenty minutes; used at work every time an analyst reads a CSV in Python.

Real Python, Reading and Writing CSV Files, the section on `csv.DictReader`,
https://realpython.com/python-csv/ (verified 03 Sep 2026).

## What stops a pasted answer from passing?

- The file is not in any assistant's training data, and its numbers come only from running it.
- The self-check lists the counts a correct pass reaches, so a pasted answer that was never run will
  miss them in ways you can see.
- The note has to name the decision that moves the total and give both totals, which only somebody
  who read the logged rows can do.

## What do you bring to Thursday's session?

Your decisions log, your two reconciliations and the note. Thursday opens on the question Meera
Raghavan, Kalpa Retail's CEO, is asking: whether the fall in Retail-Plus, Kalpa's paid membership tier,
is real. Your note is the evidence that the numbers under it are clean.
