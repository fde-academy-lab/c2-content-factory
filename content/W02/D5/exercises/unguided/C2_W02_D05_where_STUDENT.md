# Unguided: where does this belong

Eight asks. For each, say which of the warehouse, pandas or Excel should own it. Use the three
questions: who owns this number, for how long, and who has to read it.

## Q1.

Anand: "The Q2 collected-revenue figure my analyst audits every Monday." Which one appears?

a) The warehouse, as a scheduled query with comments
b) pandas, in a notebook the analyst opens and reads
c) Excel, so the analyst can slice it while checking
d) Plain Python, so each step can be read aloud

## Q2.

The chief of staff: "A pivot I can slice by segment during the meeting." Which one appears?

a) The warehouse, with a query per segment prepared
b) pandas, with the director calling out filters
c) Excel, built on the clean customer table
d) Plain Python, rerun for each slice requested

## Q3.

You: "Joining payments to orders without double-counting." Which one appears?

a) Excel, using a lookup down the whole payment column
b) The warehouse, where the join and its check live
c) pandas, since merge carries a validate argument
d) Whichever of the three the deadline allows

## Q4.

Marketing: "The weekly customer table our analysts build features on." Which one appears?

a) Excel, refreshed by hand every Monday morning
b) The warehouse, since it is the source of truth
c) Plain Python, so the logic stays inspectable
d) pandas, from the warehouse, in a single run

## Q5.

A director in the room: "What if the Retail-Plus fall were half as steep?" Which one appears?

a) Excel, with the assumption in a marked input cell
b) The warehouse, re-queried with a changed filter now
c) pandas, editing the notebook while they watch
d) Nowhere: the question cannot be answered live

## Q6.

You: "Cleaning the duplicate keys out of the exposure feed." Which one appears?

a) Excel, using remove duplicates on the column
b) pandas or the warehouse, wherever the feed lands
c) Excel, since the feed's owner sends a spreadsheet
d) Plain Python, reading the file line by line

## Q7.

The chief of staff: "One number on the front page with its trend." Which one appears?

a) Excel, computing the number from the raw export
b) Excel, showing a number the warehouse computed
c) pandas, exporting a picture of the chart to paste
d) The warehouse, since the number must be correct

## Q8.

Somebody proposes keeping the sheet as the record, since it has been corrected by hand a few
times. Which one appears?

a) Fine, as long as the corrections are documented
b) Fine, since the corrections are genuine fixes
c) Refuse: a corrected sheet cannot be rebuilt
d) Refuse: Excel cannot hold that many rows safely

## Answering

Post one line: the eight letters in order. Then take Q1 and Q2, which are both Anand's world and
get different answers, and write one sentence on what separates them.
