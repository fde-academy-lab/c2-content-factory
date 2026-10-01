# Which answers hold in the chapter 4 set on which branch moved and what each Retail-Plus member spent, and why?

Answers: 1a 2c 3a 4d 5c 6d

Chapter 4 wrote the quarter comparison as named steps in one `WITH` query and read each branch of
each segment's tree as Q2 over Q1. Retail-Plus, Kalpa's paid membership tier, saw its customers fall
to 0.835 of Q1, its orders per customer to 0.780 and its revenue per order rise to 1.084, which
multiply back to its revenue ratio of 0.706. Spend per member taken with a plain average said Rs 6,437
then Rs 5,439, down 15.5 percent, because each quarter's average covered only that quarter's buyers;
with the zero written in for a member who bought nothing, the same 107 members spent Rs 5,474 then
Rs 3,863, down 29.4 percent. The set tries the same reading on other segments and invented numbers.
Three of the six items are design items: 1, 2 and 6.

**Who needs the answer.** You do, when you check your six letters after the lab or tonight. The head
of Retail-Plus sets her retention effort from these lines, and a spend per member that half the fall
has leaked out of tells her the tier is holding.

**The questions on the way.**

- Which idea does the chapter 4 set test: who is inside each number, and how a query is written for the analyst?
- Why does each of the six keys hold, from the renamed column to the route that never averages?
- Why is option a in item 6, the tier's 120 members, worth arguing about?
- Where does GitLab's data team say to prefer named steps to subqueries?

## Which idea does the chapter 4 set test: who is inside each number, and how a query is written for the analyst?

The set tests whether each number names the group inside it, and whether a query is written for the
person who reruns it. The design items count the edits a renamed column costs each way of writing the
comparison, count how often a shared step is computed under named steps and under a temporary table,
and reach the fix's spend per member by a route that never averages. The other items read which
branch pulled a segment down, predict what two averages return when some members bought nothing, and
explain a sheet on which customers spent more while their segment's revenue fell.

## Why does each of the six keys hold, from the renamed column to the route that never averages?

### Q1. Which way of writing the comparison needs fewer edits when a column is renamed?

Kind: a design item, the best-fit way sized in the places a rename forces the analyst to edit,
counted from the two versions printed in the stem.

The key is a, "Named steps: 1 place against the nested version's 4, and each one reruns whole in a
fresh session". Version A names `c.segment` in each subquery's SELECT and again in its GROUP BY, four
places; version B names it once, in `book`, and the later steps read the step's own column. Both are
single statements that write nothing, so both rerun whole; the rename is what separates them.

- b, "Nested subqueries: 2 places, one per subquery, against named steps' 4, so nested is easier to
  keep": counts one place per subquery, where each subquery names the column twice, and counts the
  later steps' `segment`, which reads `book`'s column and not the customers table's.
- c, "Named steps: 4 places, since every later step names the segment, against the nested version's
  2": the later steps name `book`'s column, which `c.tier AS segment` keeps as it is.
- d, "Temporary tables: 1 place, in the first table, and nothing to rebuild when the analyst opens a
  fresh session": a temporary table vanishes when its session ends, so every Monday's fresh session
  has to build it again before the comparison can read it.

### Q2. How many times is a shared step computed each Monday, and when does a temporary table fit?

Kind: a design item, the fact that switches the choice, worked out as a count. The scale is invented:
2 crore orders and twelve queries in one session, each starting from the same step.

The key is c, "12 times with named steps and once with a temporary table, so the temporary table fits
a step this large". Postgres computes a `WITH` step once for each run of the statement that holds it,
so twelve queries carrying the step compute it twelve times; a temporary table is built once in the
session and read by all twelve. On Kalpa's 1,000 orders read once a Monday the difference never
arises, which is why named steps fit the suite today.

- a, "Once with named steps, since Postgres computes a WITH step only once, and 12 times with temporary
  tables": a `WITH` step is computed once per statement, not once per session, and the temporary table
  is the one built once.
- b, "12 times either way, since a temporary table is rebuilt for every query that reads it": a
  temporary table stays built for the rest of its session, so the queries after the first read rows
  already written.
- d, "Once either way, so named steps still fit, and they write nothing into the warehouse": writing
  nothing is true, and each of the twelve statements still computes its own copy of the step.

### Q3. Which branch pulled Business's revenue down most, and does its row check itself?

Kind: read the output. Business's branches are 0.972, 0.965 and 1.051 against a revenue ratio of
0.986.

The key is a, "Orders per customer, at 0.965, and the three branches multiply back to its 0.986". Orders
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

### Q5. What explains a sheet that says Retail-Core customers spent more each while Retail-Core's revenue fell?

Kind: spot the plausible wrong output. The sheet says Rs 3,658 then Rs 3,815, up 4.3 percent, while
Retail-Core's revenue fell 1.8 percent.

The key is c, "Each average covers only that quarter's 102 or 96 buyers, two different groups".
`avg` skips the customers with no order in a quarter, so Q1's average is over 102 customers and Q2's
over 96, and the 29 or 35 customers who bought only in the other quarter drop out of each. Over the
same 131 customers, with zeros written in, Retail-Core spent Rs 2,848 then Rs 2,796 each, down 1.8
percent, the same change as its revenue.

- a, "Retail-Core's revenue per order rose 1.2 percent, and that lift reaches every customer's
  spend": the branch did rise 1.2 percent, and the customer branch fell 5.9 percent, so revenue per
  order cannot turn a fall in revenue into a rise per customer of a fixed group.
- b, "The averages round to whole rupees, and the rounding moved the two apart": rounding moves an
  average by less than a rupee, and the gap is Rs 157.
- d, "Customers who joined in Q2 spent more than the rest and pulled Q2's average up": when a
  customer joined does not enter either average; which customers bought in each quarter does.

### Q6. Which route that never averages could confirm Retail-Plus spend per member?

Kind: a design item, the independent second route, computed in two steps. The tier holds 120 members
and 13 of them bought nothing in either quarter, so 107 bought; Retail-Plus booked Rs 5,85,770 in Q1
and Rs 4,13,380 in Q2.

The key is d, "Each quarter's revenue over 120 less the 13 who bought nothing: Rs 5,474 then
Rs 3,863". 120 less 13 is 107, and Rs 5,85,770 over 107 is Rs 5,474 and Rs 4,13,380 over 107 is
Rs 3,863. The count comes from the customers table and a count of its own, never from the fix's step,
so a step that held the wrong members would print levels this route does not reach; today they agree
to the rupee.

- a, "Each quarter's revenue over the tier's 120 members: Rs 4,881 then Rs 3,445": revenue per tier
  member, a fair measure of a different group, since it counts the 13 who bought nothing; its change is
  the same 29.4 percent, and its levels cannot confirm the fix's.
- b, "Each quarter's rupees in the fix's step over the step's own 107 rows: Rs 5,474 then Rs 3,863":
  the right numbers today, and the fix's own average written as a division, since its rupees and its
  rows both come from the step. Whatever members the step held, this route prints what the fix prints:
  built over all 120 members, both would read Rs 4,881.
- c, "Each quarter's revenue over that quarter's own 91 and 76 buyers: Rs 6,437 then Rs 5,439": the
  plain average again, each quarter over its own buyers, which leaves out whoever stopped.

## Why is option a in item 6, the tier's 120 members, worth arguing about?

It carries the right change, 29.4 percent, and some will argue that the tier's 120 is the better base,
since the head of Retail-Plus runs the whole tier, the 13 who bought nothing included. That is a fair
question for her, and it changes the level, never the change: any group held the same in both quarters
moves by 29.4 percent. The item asks for spend per member as the sheet defines it, over the members
who bought, and a second route has to reach that level; the 120-member figure is revenue per tier
member, and the sheet can carry it under its own name.

## Where does GitLab's data team say to prefer named steps to subqueries?

GitLab's data team writes in its SQL style guide that it prefers CTEs over sub-queries because "CTEs
make SQL more readable ...", and asks that each CTE "perform a single, logical unit of work". The same
guide asks that calculations carry a brief description of what is going on, which is the comment
above each named step an auditor reads first. It also says not to use `USING` in joins, because it
gives inaccurate results in Snowflake, the warehouse GitLab runs; on Postgres, `JOIN ... USING` is
exact, which is why Kalpa's lookup line keeps it.
