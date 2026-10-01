# Which fifty Retail-Plus members go on the protect list, and when the chief of staff types an id, does the sheet answer for that member?

Chapter 3 set, six items, after chapter 3: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "... the top-fifty protect list with a lookup so I can find any member by id ..."
>
> Meera's chief of staff, Kalpa Retail

Retail-Plus is Kalpa Retail's paid membership tier. The protect list is the fifty Retail-Plus members
with the highest revenue between April and September 2026, taken from the customer table, which
holds one row per customer who ordered in those months; the head of Retail-Plus sends each of them a
retention offer. On the table, member ids sit in column A, rows 2 to 301, and revenue in column E. A
lookup takes an id and returns a value from the same row. `VLOOKUP(id, table, column, range_lookup)`
gives an exact match when range_lookup is FALSE, and #N/A when the id is missing; left out or TRUE, it
gives an approximate match, which expects the first column to be sorted. `INDEX(E:E, MATCH(id, A:A,
0))` is an exact match, and `IFERROR(x, "not in the table")` shows those words where x would be an
error. `XLOOKUP(id, A:A, E:E, "not in the table")`
is exact by default and takes the not-found words as its fourth argument; Microsoft says it is not
available in Excel 2016 and Excel 2019, and LibreOffice 24.2 shows #NAME? for it. COUNTIF counts the
rows holding a value, and SUMIFS adds the values on the rows that meet a condition.

**Who needs the answer.** The head of Retail-Plus spends a retention offer on each of the fifty, and
the chief of staff reads a member's line aloud when a director names one. A lookup that answers with
the wrong member's row tells a director that someone who has stopped buying is one of the best, and
spends an offer on the wrong person.

**The questions on the way.**

- What went wrong when C-0195 came back as Rs 16,740 at rank 15?
- Which formula returns a member's revenue or the words "not in the table", and nothing else?
- Which lookup ships to an office where two laptops run Excel 2019?
- Which match type fits a discount tier, and which fits a member id?
- Which three ids test a lookup before a director uses it?
- Which check can disagree with the lookup when the lookup is wrong?

Item 4's tiers are invented; the other items use the customer table's own ids and numbers.

Post one line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What went wrong when C-0195 came back as Rs 16,740 at rank 15?

C-0195 is a Retail-Plus member in Delhi who placed no orders between April and September, so the
customer table has no row for C-0195. The chief of staff types the id, the cell holds
`=VLOOKUP("C-0195", A2:F301, 5)`, and the sheet shows Rs 16,740 and rank 15 on the protect list.
What went wrong?

a) The member's orders were summed across both quarters instead of Q2 alone
b) The ids are text, so the lookup compared them in the wrong order
c) The list was ranked before the segment filter was applied to it
d) An approximate match returned the nearest id below the one asked for

### Q2. Which formula returns a member's revenue or the words "not in the table", and nothing else?

Revenue sits in column E and ids in column A of the customer table, rows 2 to 301, and the chief of
staff types an id into cell H1. Which formula returns that member's revenue when the id is in the
table, and the words "not in the table" when it is not?

a) `=VLOOKUP(H1,A:E,5)`
b) `=IFERROR(INDEX(E:E,MATCH(H1,A:A,0)),"not in the table")`
c) `=INDEX(E:E,MATCH(H1,A:A,1))`
d) `=IFERROR(VLOOKUP(H1,$A$2:$E$301,5,TRUE),"not in the table")`

### Q3. Which lookup ships to an office where two laptops run Excel 2019?

The protect list goes to the CEO's office. Two of its laptops run Excel 2019 and the rest run
Microsoft 365, and any of them may open the file in Monday's meeting. There a director names an id,
the chief of staff types it and reads the cell aloud, so the cell has to answer in words the room can
hear: a revenue figure, or "not in the table". Which lookup ships?

a) XLOOKUP with its fourth argument, since it is exact by default and names a missing id
b) VLOOKUP with FALSE, since #N/A is an honest answer for an id the table lacks
c) IFERROR around INDEX and MATCH with 0, which every version computes
d) VLOOKUP with its fourth argument left out, since every version of Excel has it

### Q4. Which match type fits a discount tier, and which fits a member id?

An invented price list sets discount tiers that start at Rs 0, Rs 1,000, Rs 2,500 and Rs 5,000,
sorted from lowest, and an order of Rs 2,700 needs its tier. The same sheet also looks members up by
id for the chief of staff. Which match type fits each lookup?

a) Exact for the tier, and approximate for the member id
b) Approximate for the tier, and exact for the member id
c) Approximate for both, since both columns are sorted
d) Exact for both, since an approximate match is never safe

### Q5. Which three ids test a lookup before a director uses it?

The chief of staff will type ids into the lookup in Monday's meeting, on a list the room will see
sorted by revenue. Which three ids do you test it with first?

a) One known to be present, one known to be missing, and the first once re-sorted
b) The top member, a member from the middle of the list, and the last id in the table
c) Three ids from the top of the list, so that the largest revenues are proved first
d) One typed in lower case, one with a trailing space, and one pasted from the export

### Q6. Which check can disagree with the lookup when the lookup is wrong?

A second route shares none of the lookup's steps, so it can fail when the lookup is wrong. Which of
these is one?

a) An XLOOKUP beside the INDEX and MATCH, compared with it cell by cell
b) The lookup's answer compared with the rank column on the very row it returned
c) A COUNTIF of the id, which must read zero where the lookup says not found
d) Conditional formatting that colours the lookup's cell red whenever it shows #N/A
