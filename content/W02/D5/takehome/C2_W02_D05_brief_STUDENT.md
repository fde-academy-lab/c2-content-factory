# Can you rebuild Monday's three deliverables from a fresh export, and say why every number that moved, moved?

The take-home, due before Build 1 opens on Monday. About ninety minutes in Excel, with no notebook
needed.

> "The data team reran both exports overnight. Rebuild Monday's three things from the new files before
> I open the deck, and tell me which numbers moved and why. If you cannot tell me why, I cannot use it."
>
> Meera's chief of staff, Kalpa Retail

Meera Raghavan, Kalpa Retail's CEO, runs Monday's growth review, and her chief of staff asked for three
things that open without a login: the revenue tree by segment for both quarters, the protect list of
the fifty Retail-Plus members with the highest revenue with a lookup by member id, and one front-page
number with its trend. Retail-Plus is Kalpa's paid membership tier; the other segments are
Retail-Core, Business and Student. Revenue is booked order value in rupees; Q1 runs from April to June
2026 and Q2 from July to September 2026. The warehouse, the database that holds one row per order and
is the source of truth, still books Rs 10,00,00,000 in Q1 and Rs 9,84,00,000 in Q2.

The fresh exports are in `data/`: `C2_W02_D05_takehome_customer_table_STUDENT.csv`, one row per
customer who ordered in the half-year with that customer's orders and revenue added up, and
`C2_W02_D05_takehome_raw_export_STUDENT.csv`, one row per payment with the order's amount repeated on
every row of that order. They have the same columns as Friday's files and a different set of
customers. Friday's rules hold: count each order once before any total, rank inside the segment the
ask names, look up with an exact match that says when an id is missing, print every number with its
period, its comparison and its base, put every assumption in a yellow input cell, and ship a part
only when the checks behind it pass.

**Who needs the answer.** The chief of staff opens the deck on Monday, and the directors decide from
it which branch of the business the growth plan funds. A number that moved for a reason nobody can
name is a number the chief of staff cannot defend in the room, so it does not go in.

**The questions on the way.**

- Does your rebuilt tree tie to the warehouse, and which of its cells moved from Friday?
- Does the protect list's source tie, and what does your release do if it does not?
- Which numbers moved, and what in the fresh sample moved each one?
- What do you tell the chief of staff in three sentences?
- What is the team's operating rule, in your own words?

## What do you ship?

1. **Your own workbook, built on the fresh exports.** The two exports pasted in as values on their
   own tabs; the tree for both quarters, the protect list with its lookup and its foot, and the card
   with its trend, every number a formula; the list size and the card's scope in yellow cells; and a
   Checks tab whose release sentence says what ships and what is held. The deck pack in `demos/` is
   the reference to compare with after you finish, never the template.
2. **The change log.** A table with one row for every number on the three deliverables that moved
   between Friday's files and the fresh ones: the tree's cells, the list's cut-off and total, the
   lookup test, the card sentence. Columns: the number, Friday's value from your own work, the fresh
   value, and one sentence on why it moved. "A different sample" is a reason only when you can say
   what in the sample changed.
3. **A screenshot of your Checks tab,** with the note you would send the data platform lead, who owns
   the warehouse, if the release holds anything.
4. **Three sentences to the chief of staff:** what ties to the warehouse, what moved that matters for
   the growth review, and what is held and why.
5. **The operating rule in three lines,** one per tool, in your own words: what the warehouse owns,
   what pandas owns, and what the workbook owns.

## Which two things do you do on the way?

- Test the lookup with an id you know is missing from the fresh customer table before you test it
  with one that is there. Find a missing id yourself, from the files, and say in the log how you
  found it.
- Read Microsoft's SUBTOTAL page,
  https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939 (verified 29 September 2026),
  and write, as the log's last line, the one situation in which `SUBTOTAL(9)` and `SUBTOTAL(109)`
  give different totals, and which one your foot uses.

## Why can an assistant not do this for you?

The change log needs Friday's values from the work you did today and the fresh values from files
nobody has explained to you. The screenshot is of your own Checks tab, and a missing id is found in the
data, with the log saying how. Check yourself against `C2_W02_D05_selfcheck_STUDENT.md` before
Monday, and reread this week's two notes to Meera and Anand Iyer, Kalpa Retail's finance controller,
before Build 1 opens.
