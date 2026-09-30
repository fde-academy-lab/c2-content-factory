# Which answers hold in the chapter 4 set on which branch moved and what each Retail-Plus member spent, and why?

Answers: 1b 2c 3a 4d 5c 6a

Chapter 4 wrote the quarter comparison as named steps in one `WITH` query and read each branch of
each segment's tree as Q2 over Q1. Retail-Plus's customers fell to 0.835 of Q1, its orders per
customer to 0.780 and its revenue per order rose to 1.084, which multiply back to its revenue ratio of
0.706. Spend per member taken with a plain average said Rs 6,437 then Rs 5,439, down 15.5 percent,
because each quarter's average covered only that quarter's buyers; with the zero written in for a
member who bought nothing, the same 107 members spent Rs 5,474 then Rs 3,863, down 29.4 percent. The
set tries the same reading on other segments and invented numbers. Three of the six items are design
items: 1, 2 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. The head of
Retail-Plus sets her retention effort from these lines, and a spend per member that half the fall
has leaked out of tells her the tier is holding.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A branch comparison is only as honest as the groups inside each number. The design items choose how
to write a query an auditor reruns, name the fact that would change that choice, and confirm a
per-member change over a group fixed from the customers table. The other items read which branch
pulled a segment down, predict what two averages return when some members bought nothing, and explain
a sheet on which members spent more while their segment's revenue fell.

## Why is each key right, item by item?

### Q1. Which way should a four-step branch query be written for an analyst who reruns it in a fresh session?

Kind: a design item, the best-fit way with its size in statements and rows written.

The key is b, "Named steps in a WITH query: one statement and no rows written, read top to bottom".
Each step carries a name and a comment and the next step reads it, so the analyst audits in the order
the logic runs, and the whole query reruns as one statement in any session without writing anything.

- a, "Nested subqueries: one statement and no rows written, read from the innermost step outwards":
  it runs the same, and a four-deep nest makes the auditor read backwards from the innermost step.
- c, "Temporary tables: one statement per step and rows written at each step, read in order": four
  statements that pass state between them, so no statement can be read or rerun on its own, and the
  tables vanish with the session.
- d, "Four queries stitched together in a notebook: four statements and every result moved out":
  moves the results out of the warehouse into a notebook, which is what Anand ruled out.

### Q2. Which fact would make temporary tables the better way?

Kind: a design item, the fact that switches the choice.

The key is c, "One step's result is read by many queries over millions of rows within one long
session". Computing a heavy step once and letting many queries read it saves work, and that saving is
a performance choice the platform lead would weigh. On a book of 1,000 orders read once a Monday it
does not arise.

- a, "The analyst wants a comment above every step, and a WITH query has no place to carry one": a
  `WITH` query carries a comment above each step, which is one of its strengths.
- b, "The suite starts running in a brand new session every Monday, with nothing kept from the last
  run": a fresh session is where temporary tables are weakest, since they vanish between sessions.
- d, "The query grows from four steps to seven, too many for a single statement": a `WITH` query holds
  seven named steps as easily as four.

### Q3. Which branch pulled Business's revenue down most, and does its row check itself?

Kind: read the output. Business's branches are 0.972, 0.965 and 1.051 against a revenue ratio of
0.986.

The key is a, "Orders per customer, at 0.965, and the three branches multiply back to 0.986". Orders
per customer fell 3.5 percent and customers 2.8 percent, while revenue per order rose 5.1 percent;
0.972 times 0.965 times 1.051 is 0.986, so the row checks itself.

- b, "Customers who bought, at 0.972, since fewer buyers always hurt revenue the most": the customer
  branch fell less than the frequency branch here, and no branch always hurts most.
- c, "Revenue per order, at 1.051, since it moved furthest from 1 of the three branches": it moved
  furthest, upwards, so it held revenue up rather than pulling it down.
- d, "None of them, since a revenue ratio of 0.986 sits too close to 1 to read any branch": a small
  change in revenue can hide larger moves in its branches that pull against each other, as this row
  shows.

### Q4. What do two averages return on five invented members' Q2 spend?

Kind: predict the output, on invented numbers. Three members spent Rs 800, Rs 1,200 and Rs 500, and
two spent nothing in Q2.

The key is d, "Rs 833 and Rs 500". `avg` averages only the filled-in values, Rs 2,500 over three
members, which is Rs 833. With `coalesce` the two empty values become Rs 0, and Rs 2,500 over all five
members is Rs 500.

- a, "Rs 500 and Rs 500": assumes `avg` counts an empty value as zero, and it leaves it out.
- b, "Rs 833 and Rs 833": assumes `coalesce` changes nothing, and it writes in two zeros.
- c, "Rs 500 and Rs 833": swaps the two.

### Q5. What explains a sheet that says Retail-Core members spent more each while Retail-Core's revenue fell?

Kind: spot the plausible wrong output. The sheet says Rs 3,658 then Rs 3,815, up 4.3 percent, while
Retail-Core's revenue fell 1.8 percent.

The key is c, "Each average covers only that quarter's 102 or 96 buyers, two different groups".
`avg` skips the members with no order in a quarter, so Q1's average is over 102 members and Q2's over
96, and the 29 or 35 members who bought only in the other quarter drop out of each. Over the same 131
members, with zeros written in, Retail-Core spent Rs 2,848 then Rs 2,796 each, down 1.8 percent, the
same change as its revenue.

- a, "Retail-Core's revenue per order rose 1.2 percent, and that lift reaches every member's spend":
  the branch did rise 1.2 percent, and the customer branch fell 5.9 percent, so revenue per order
  cannot turn a fall in revenue into a rise per member of a fixed group.
- b, "The averages round to whole rupees, and the rounding moved the two apart": rounding moves an
  average by less than a rupee, and the gap is Rs 157.
- d, "Members who joined in Q2 spent more than the rest and pulled Q2's average up": when a member
  joined does not enter either average; which members bought in each quarter does.

### Q6. What does Retail-Plus spend per member come to over the tier's 120 members?

Kind: a design item, the independent second route, computed. Retail-Plus booked Rs 5,85,770 in Q1 and
Rs 4,13,380 in Q2, and the tier has 120 members.

The key is a, "Rs 4,881 then Rs 3,445, down 29.4 percent". Rs 5,85,770 over 120 is Rs 4,881 and
Rs 4,13,380 over 120 is Rs 3,445. The group is fixed from the customers table, so nobody's buying
pattern can change who is inside it, and the change is the tier's revenue change, down 29.4 percent,
the same as the fixed 107 gave in the chapter. Any group held the same in both quarters gives the same
change.

- b, "Rs 5,474 then Rs 3,863, down 29.4 percent": the chapter's numbers over the 107 members who
  bought in the half-year; the change agrees, and the levels are over a different group from the one
  the route names.
- c, "Rs 6,437 then Rs 5,439, down 15.5 percent": revenue over each quarter's own buyers, 91 and then
  76, the plain average that leaves out whoever stopped.
- d, "Rs 1,723 then Rs 1,216, down 29.4 percent": divides by all 340 members on the book, most of whom
  belong to other segments, so it is no longer spend per Retail-Plus member.

## Which wrong answer is worth arguing about?

Item 6, option b. It carries the right change, and some will argue that 107 is the better group,
since the 13 members who bought nothing all half-year may have lapsed. That is a fair question for
the head of Retail-Plus, and it changes the level, never the change: any fixed group moves by 29.4
percent. The argument worth having is which level she quotes, and the answer is whichever group the
sheet names beside the number.

## Where does this show up at work?

GitLab's data team writes in its SQL style guide that it prefers CTEs over sub-queries because "CTEs
make SQL more readable ...", and asks that each CTE "perform a single, logical unit of work". The same
guide asks that calculations carry a brief description of what is going on, which is the comment
above each named step an auditor reads first.
