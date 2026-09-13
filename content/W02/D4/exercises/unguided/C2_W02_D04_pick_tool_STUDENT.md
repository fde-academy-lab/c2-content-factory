# Unguided: pick the tool

Five asks. For each, choose the tool and be ready to defend it with the three questions: who owns
this number, for how long, and who has to be able to read it.

## Q1.

Anand: "The Monday revenue figures, every Monday, that my analyst audits line by line." Which one
appears?

a) pandas, in a notebook the analyst can open and read
b) SQL in the warehouse, on a schedule, with comments
c) Plain Python, since it can be explained line by line
d) Excel, since the analyst already works in a spreadsheet

## Q2.

You, to yourself: "I want to try six versions of a customer score this afternoon and keep one."
Which one appears?

a) SQL, since the warehouse is the source of truth
b) Plain Python, which makes each version explicit
c) pandas in a notebook, iterating fast on a frame
d) Excel, where six columns sit side by side

## Q3.

A trainer, to a room that has never seen a loop: "Show them how a total is built." Which one
appears?

a) Plain Python, so every step is visible
b) pandas, since one line is easier to remember
c) SQL, since it says what rather than how
d) Excel, since a spreadsheet is familiar

## Q4.

Marketing: "The customer table, refreshed every Monday, that our analysts will build on." Which
one appears?

a) SQL, so it is owned by the warehouse
b) Plain Python, so the logic is inspectable
c) Excel, since their analysts open spreadsheets
d) pandas, from the warehouse, in one run

## Q5.

Somebody proposes that Finance's quarter-end number be produced by a notebook an analyst runs.
Which one appears?

a) Fine, since the notebook reads from the warehouse anyway
b) Fine, provided the notebook is committed to the repository
c) Refuse: a notebook has no audit trail a controller can read
d) Refuse: pandas cannot handle numbers of that size accurately

## Answering

Post one line: the five letters in order. Then take Q4 and write one sentence on why your answer
differs from your answer to Q1, given that both are weekly and both come from the warehouse.
