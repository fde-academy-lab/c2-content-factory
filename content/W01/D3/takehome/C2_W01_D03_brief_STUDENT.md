# Take-home: a second export, and the note to Finance

> "The ERP team found another extract from the migration, Q1 only, a different batch. Same drill:
> which total is right, what you set aside and why, and whether it changes anything we said today."
>
> Anand Iyer, finance controller, Kalpa Retail

About two hours tonight. The file is `data/C2_W01_D03_takehome_STUDENT.csv`. Nobody has profiled it
in class, and its defects are not the ones you met today, so today's counts will not carry over.

## Part 1. The full pass, about seventy minutes

In a fresh notebook, using the day's helper:

1. Read the file and profile every field: present, convertible, distinct. Write one sentence per
   field on what its counts let you trust.
2. Convert amounts with a rejects log. Every row that fails goes into the log with its line, field,
   value and reason, and you read each logged row before deciding anything about it.
3. Apply the identity rule, preferring the copy that validates, and log a reason for every row set
   aside.
4. For every value that converts but is still not an ordinary order, make the three-way decision,
   drop, default or keep and flag, and write the reason. At least one decision tonight has two
   defensible answers; choose one and say what the other would have given.
5. Reconcile twice: rows in equal rows kept plus rows set aside, and rupees as read less the rupees
   set aside equal your clean total. Draw the bridge with `kit.bridge`.

## Part 2. The note to Finance, about twenty minutes

Under 120 words, numbers first: the clean Q1 total and how you know it, the two reconciliations, the
decisions you flagged, and the one decision that moves the total, with the total under each answer.

## Part 3. Read, about twenty minutes

Real Python, Reading and Writing CSV Files, the section on `csv.DictReader` (verified 03 Sep 2026):
https://realpython.com/python-csv/

## What makes this hard to shortcut

- The file is not in any assistant's training data, and its numbers come only from running it.
- The self-check lists the counts a correct pass reaches, so a pasted answer that was never run will
  miss them in ways you can see.
- The note has to name the decision that moves the total and give both totals, which only somebody
  who read the logged rows can do.

## What to bring tomorrow

Your decisions log, your two reconciliations and the note. Thursday opens on Meera's question about
whether the Retail-Plus fall is real, and your note is the evidence that the numbers under it are
clean.
