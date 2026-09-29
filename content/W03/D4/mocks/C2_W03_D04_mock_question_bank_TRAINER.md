# Mock R1, the technical half: question bank with model answers

**TRAINER ONLY.** Assessors keep this page. Nothing on it reaches a learner, before or after the mock.

The technical half runs nine minutes: three questions, about three minutes each, one at each level.
Every question is asked in a stakeholder's words from Kalpa Retail, the unit the room worked in for
Weeks 1 and 2, so the half tests the fortnight's method and never Python or SQL syntax on its own.
The viva half, on the group's Kalpa Health work, is a separate file,
`C2_W03_D04_viva_prompts_TRAINER.md`.

## How the bank is cut

| Level | What it asks for | What an understood answer shows |
|---|---|---|
| L1, the move | The method named and applied to a business ask | The learner states the move and its first check without prompting |
| L2, the number | A plausible wrong number on the table, and what produced it | The learner names the mechanism that made the number, the check that catches it and the fix |
| L3, the judgement | A stakeholder pushing back, and a decision to defend | The learner holds a position with a number, names what would change it and proposes the next step |

Ten families cover the fortnight, one per taught day, and each family carries one question per level,
so the bank holds thirty questions. The row's tags are kept: `[S]` staple asked everywhere, `[F]`
frequent in GCC and product screens, `[D]` differentiator. The anchor column names the row whose
interview angle each question descends from, and the trap it reuses from
`docs/detailing/W01_W02_spine.md` where there is one.

| Family | Taught on | The fortnight's move |
|---|---|---|
| T01 | Week 1 Monday | The revenue tree and the typical order |
| T02 | Week 1 Tuesday | The investigation ladder and the fair window |
| T03 | Week 1 Wednesday | Profile, clean, reconcile, with a decisions log |
| T04 | Week 1 Thursday | Real or noise, and the fair comparison |
| T05 | Week 1 Thursday and Friday | The four-part note and holding a caveat |
| T06 | Week 2 Monday | The warehouse query Finance audits |
| T07 | Week 2 Tuesday | Booked against collected, and joins that lie |
| T08 | Week 2 Wednesday | Ranking, ties and change over time |
| T09 | Week 2 Thursday | The customer table in pandas |
| T10 | Week 2 Friday | Excel for the stakeholder, and choosing the tool |

## The eight sets

A learner meets one set. The roster gives each seat its set letter, and within a group the seats
take consecutive letters, so no two members of one group meet the same set. Each set draws its three
questions from three different families, and every set mixes Week 1 and Week 2.

| Set | L1, the move | L2, the number | L3, the judgement |
|---|---|---|---|
| A | T01-L1 | T04-L2 | T07-L3 |
| B | T02-L1 | T05-L2 | T08-L3 |
| C | T03-L1 | T06-L2 | T09-L3 |
| D | T04-L1 | T07-L2 | T10-L3 |
| E | T05-L1 | T08-L2 | T01-L3 |
| F | T06-L1 | T09-L2 | T02-L3 |
| G | T07-L1 | T10-L2 | T03-L3 |
| H | T08-L1 | T01-L2 | T04-L3 |

Six questions sit outside every set as reserves: T09-L1, T10-L1, T02-L2, T03-L2, T05-L3 and T06-L3.
Use a reserve when a learner says they have heard a question from a group-mate or a friend in
another group, when a set's question lands on the learner's own sub-problem so closely that it
duplicates the viva, or when a learner is re-mocked.

**Leakage.** Mocks run all day and learners talk. Eight sets spread the risk, and the follow-up is
what protects the half: a memorised model answer survives the first question and breaks on the
follow-up, which is written to move the case one step. If a learner delivers a model answer
word-perfect, go straight to the follow-up and then to one reserve from the same level.

## The calibration floor

The row names GeeksforGeeks, "Data Analyst Interview Questions and Answers", for calibrating the
technical half, https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ (verified 29 September 2026; the page shows 95 numbered questions and was last updated on
24 July 2026). Its questions are definitional ("what is a join", "what is a p-value"). This bank sits
one step above them, because a GCC screen at the 0 to 3 year band asks for the definition inside a
business case. If a learner cannot answer a question at the case level, ask the definitional form
once, note that you did, and move on.

---

## T01. The revenue tree and the typical order

### T01-L1 `[S]` The move

**Anchor.** Week 1 Monday: "A business says 'grow revenue 15 percent'; how do you turn that into
questions data can answer?" and "How would you increase sales for an online retailer?"

**Ask.** "Meera Raghavan says sales must grow 15 percent next year. Before you open any data, what is
sales made of, and what is the first question you ask her?"

**Model answer, under a minute.** Sales is customers, times orders per customer, times items per
order, times price per item, less discounts. Every branch is a number over a denominator in one
window, so orders per customer is orders divided by distinct customers in the same quarter. Growth
has to come from one or more branches, so the first question to Meera is which branch the plan
assumed would move: more customers, more frequent customers, bigger baskets or higher prices. Then I
ask whether she means booked or collected sales and over which window, because the answer changes
the number I measure against.

**Follow-up.** "Take orders per customer. What exactly is its denominator, and what goes wrong if you
count rows?"

**What the follow-up separates.** A learner who understood says distinct customers in the window,
and that counting order rows as customers makes orders per customer read 1.00, which says nobody
comes back when some do. A learner who memorised the tree recites the four branches and stalls on the
denominator, or says "the number of rows".

**A weak answer sounds like.** "I would look at the sales dashboard and see which products are
selling", or a list of marketing ideas with no tree.

### T01-L2 `[S]` The number

**Anchor.** Week 1 Monday: "Mean or median for order value, and why?" The trap is the mean of
Rs 18,160 sold as the typical order when the median is Rs 2,205.

**Ask.** "On thirty orders the mean is Rs 18,160 and the median is Rs 2,205. Meera wants the typical
order value for her note. Which number goes in, and what do you do before you choose?"

**Model answer, under a minute.** A mean about eight times the median says a few very large orders
are pulling it, so before choosing I sort the orders and read the top of the list. If one order is a
bulk business purchase, the typical order is the median, Rs 2,205, and the bulk order is reported
separately as its own line, because it is real revenue that will not repeat in the same way. I keep
the order in the data and in the total; I only keep it out of the word "typical".

**Follow-up.** "When is the mean the right number to give her?"

**What the follow-up separates.** Understood: when she needs a total, because mean times count
rebuilds revenue, so planning and budgeting use the mean with the bulk order stated. Memorised:
"the median is always better because it ignores outliers".

**A weak answer sounds like.** "Remove the outlier and take the mean again", which deletes real
revenue from the books.

### T01-L3 `[D]` The judgement

**Anchor.** Week 1 Monday: "Marketing wants budget for acquisition; what would you check before
agreeing it is the right branch, and how would you say no?"

**Ask.** "Marketing wants Rs 12 crore for acquisition. Your tree says customers held steady and
orders per customer fell. You are in the room with the marketing lead. What do you say?"

**Model answer, under a minute.** I put the branches side by side for the same two windows: customer
count held, orders per customer fell. The gap is in how often existing customers come back, so money
spent bringing in new customers is aimed at a branch that is not short. I would say that plainly,
with the two numbers, and then offer the marketing lead a way to be right: if new customers come back
more often than existing ones, their cohort's repeat rate will show it, and a small test on a
retention offer tells us within a quarter whether frequency responds to spend.

**Follow-up.** "The marketing lead says new customers become repeat customers later, so acquisition
fixes frequency too. What data answers that, and what if it is too early to tell?"

**What the follow-up separates.** Understood: the repeat rate of last year's new-customer cohort
against existing customers over the same months, and if the cohort is too young, "not yet" with the
date it can be read. Memorised: repeats "the data says frequency" without naming the comparison.

**A weak answer sounds like.** Caving ("it could help, let us try both"), or an assertion with no
number.

---

## T02. The investigation ladder and the fair window

### T02-L1 `[S]` The move

**Anchor.** Week 1 Tuesday: "Sales dropped 15 percent last month; how would you investigate?"

**Ask.** "Meera says sales dropped 15 percent last month. What do you do in the first thirty minutes,
in order?"

**Model answer, under a minute.** First, is the drop real: the same length of window, the same
definition of sales, the month's data complete, no late records or pipeline change. Second, which
branch of the revenue tree moved: customers, orders per customer, basket size or price. Third, which
segment, channel or region carries the movement. Fourth, is it a change in mix or a change in rate
inside the segments. Fifth, one hypothesis for the business, with the evidence that would settle it.
Causes come last because they are the cheapest thing to guess and the most expensive to guess wrong.

**Follow-up.** "What would make you stop at the first rung and never reach the tree?"

**What the follow-up separates.** Understood: a data problem that explains the drop by itself, such
as missing days, a system change or a changed definition, which goes back to the data owner first.
Memorised: repeats the five rungs without an example of the first one failing.

**A weak answer sounds like.** "It is probably seasonality or a competitor", with no check of whether
the drop is real.

### T02-L2 `[F]` The number (reserve)

**Anchor.** Week 1 Tuesday: "What has to match before a quarter-on-quarter comparison is fair?" The
trap is quarters of unequal length compared as totals.

**Ask.** "Q1 ran 90 days and Q2 ran 92. Q2 revenue is 3 percent higher than Q1. The head of
Retail-Plus calls it growth. What do you check?"

**Model answer, under a minute.** Two extra days are about 2.2 percent more calendar, so most of the
3 percent is the calendar. On a per-day basis Q2 is about 0.8 percent above Q1, which is close to
flat. I would give the per-day comparison, and then check the other things that have to match: the
same stores open, the same definition of revenue and the same data completeness in both quarters.

**Follow-up.** "One store was closed for a week in Q1 for renovation. What changes?"

**What the follow-up separates.** Understood: compare like for like, stores open in both windows for
the same days, and report the renovated store separately. Memorised: repeats "per day" without
seeing that a closure is the same problem at store level.

**A weak answer sounds like.** "Revenue grew 3 percent quarter on quarter."

### T02-L3 `[D]` The judgement

**Anchor.** Week 1 Tuesday: "Marketing insists the answer is acquisition and your data says
frequency; how do you make the case in the room?" and the trap of an average of segment averages.

**Ask.** "Average order value rose in every one of the four segments from Q1 to Q2, and the company's
average order value fell. Marketing says your numbers must be wrong. What happened, and how do you
make the case in the room?"

**Model answer, under a minute.** Nothing is wrong: the mix moved. More of Q2's orders came from the
segment with the lowest order value, so the company average fell even though each segment's rose. I
would show one table with each segment's share of orders and its average in both quarters, and split
the change into a rate effect, which is positive, and a mix effect, which is negative and larger. The
business question then becomes why the low-value segment grew its share, which is a better question
than whether the analyst made an error.

**Follow-up.** "Which one number would you put on the slide for Meera?"

**What the follow-up separates.** Understood: the mix effect in rupees or points, with the segment
whose share grew named. Memorised: says "Simpson's paradox" and stops, with no number and no
decision.

**A weak answer sounds like.** "There must be a data error; I would recheck the query."

---

## T03. Profile, clean, reconcile, with a decisions log

### T03-L1 `[S]` The move

**Anchor.** Week 1 Wednesday: "Finance and your dashboard disagree; what do you do?"

**Ask.** "Anand Iyer says Q1 revenue is Rs 1.9 crore and your dashboard says Rs 2.1 crore. He wants to
know which is right before anyone acts. What do you do?"

**Model answer, under a minute.** I do not pick one. First I match definitions: booked or collected,
gross or net of returns and cancellations, the same window. Then I profile the export before touching
it: row counts, distinct ids, types, missing values, the largest amounts. Then I build the bridge from
2.1 to 1.9 line by line: duplicates from the migration, cancelled orders, amounts stored as text,
anything else, each in rupees. Every cleaning act goes into the decisions log, and the check is that
input rows equal clean rows plus rejected rows, so Anand's analyst can audit every rupee.

**Follow-up.** "Your row counts reconcile and the rupees still do not. Where do you look?"

**What the follow-up separates.** Understood: the amounts themselves, meaning values coerced to zero,
text amounts, a duplicate pair with different amounts, or a bulk order treated differently in the two
systems. Memorised: says "check for duplicates" again, which the counts already ruled out.

**A weak answer sounds like.** "Finance is the source of truth, so I would use their number."

### T03-L2 `[F]` The number (reserve)

**Anchor.** Week 1 Wednesday: "How do you find duplicates, and what makes two records the same?" The
trap is a whole-record dedupe that reports zero duplicates.

**Ask.** "You dedupe the migrated orders on the whole record and find zero duplicates. Anand's team
swears there are duplicates. How can both be true?"

**Model answer, under a minute.** A re-export changes some field, usually a timestamp or a status, so
two copies of one order are rarely identical on every column. The identity rule has to be the
business key, the order id, and where there is none, customer, date and amount together. Then I
decide which copy to keep, usually the one with the latest update, and log the rule, the count and
the rupees removed.

**Follow-up.** "Two rows share an order id and carry different amounts. Which do you keep?"

**What the follow-up separates.** Understood: neither by default; check the status and the update
time, keep the later one if the history explains the change, and otherwise put both in the rejects
log and ask Finance. Memorised: "keep the first".

**A weak answer sounds like.** "I would run drop_duplicates."

### T03-L3 `[D]` The judgement

**Anchor.** Week 1 Wednesday: "An auditor asks why you dropped 14 rows; walk them through it."

**Ask.** "An auditor from Anand's team asks why your clean file has 14 fewer rows than the export.
Walk them through it."

**Model answer, under a minute.** I open the decisions log. Each rule has a line: what it caught, how
many rows, how many rupees, and why. For example, so many rows were migration duplicates removed on
the order id keeping the latest update, and so many had amounts that could not be read and are held
in the rejects file with the original value. Input equals clean plus the 14 rejected, and the revenue
bridge shows the rupees each rule moved. Nothing was dropped silently, and the large business order
was kept because it is real revenue.

**Follow-up.** "Which of the 14 would you defend least, and why?"

**What the follow-up separates.** Understood: names a real judgement call, such as a row rejected
because the amount was ambiguous, and says what evidence would bring it back. Memorised: "all 14 were
clearly bad data".

**A weak answer sounds like.** "They were outliers and bad data, so I removed them."

---

## T04. Real or noise, and the fair comparison

### T04-L1 `[S]` The move

**Anchor.** Week 1 Thursday: "What does p = 0.03 mean, and not mean?" The trap is reading p = 0.03 as
a 3 percent chance of being wrong.

**Ask.** "Your test on the Retail-Plus gap gives p = 0.03. Meera asks what that means. Tell her, and
tell her what it does not mean."

**Model answer, under a minute.** If there were no real difference between the groups, a gap at least
this large would turn up by chance about three times in a hundred. So the gap is hard to explain as
luck. It does not mean there is a 3 percent chance we are wrong, it does not mean a 97 percent chance
the effect is real, and it says nothing about whether the gap is large enough to act on. That second
question is about rupees, and I answer it separately.

**Follow-up.** "Explain where the 0.03 came from without using the word probability."

**What the follow-up separates.** Understood: shuffle the group labels thousands of times, compute the
gap each time, and count how often a shuffled gap was as large as the real one: about 3 in every 100
shuffles. Memorised: repeats the definition.

**A weak answer sounds like.** "There is a 97 percent chance the result is correct."

### T04-L2 `[F]` The number

**Anchor.** Week 1 Thursday: "42 percent on 12 users against 31 percent on 1,200; which do you trust?"
The trap is a headline rate on twelve orders.

**Ask.** "A new checkout page converts 42 percent of 12 visitors. The old page converts 31 percent of
1,200. The product head wants to switch. What do you tell them?"

**Model answer, under a minute.** On 12 visitors one person moves the rate by about 8 points, and a
rough margin of one over the square root of the count is about 29 points, so 42 percent is inside the
noise of 31. On 1,200 the margin is about 3 points, so 31 is solid. I would trust 31, say the new page
is not yet shown to be better, and ask for enough traffic to settle it before switching.

**Follow-up.** "How many visitors would you want on the new page?"

**What the follow-up separates.** Understood: to read a gap of about 5 points, a margin of 5 points,
so about 400 visitors, since one over the square root of 400 is 0.05. Memorised: "a larger sample"
with no number.

**A weak answer sounds like.** "42 is higher than 31, so the new page is better."

### T04-L3 `[D]` The judgement

**Anchor.** Week 1 Thursday: "Revenue rose after a discount; did the campaign work, and what would you
need to know?" The trap is the aggregate trusted while every segment fell.

**Ask.** "Revenue rose after the monsoon discount. The marketing lead says it worked. When you split
by segment, every segment's revenue per customer fell. What do you say?"

**Model answer, under a minute.** The total rose because the mix changed, more customers from a
segment that spends more, while inside every segment customers spent less. So the discount did not
lift any segment, and the rise came from who showed up. To say whether the discount caused anything I
need what would have happened without it: the trend before, the same season last year, or customers
who were not offered it. My answer to Meera is that the lift is not shown, with the segment table and
the cost of the discount beside it.

**Follow-up.** "The marketing lead says the board sees the total, and the total went up. How do you
hold the line?"

**What the follow-up separates.** Understood: holds the segment result, names the decision at stake,
more discount money, and proposes a test with a held-out group so the next campaign answers the
question. Memorised: "correlation is not causation" with no split and no test.

**A weak answer sounds like.** "Revenue went up, so the campaign worked", or a slogan with no numbers.

---

## T05. The four-part note and holding a caveat

### T05-L1 `[S]` The move

**Anchor.** Week 1 Thursday: "Explain a finding to a non-technical stakeholder."

**Ask.** "Meera has two minutes. How do you put a finding in front of her?"

**Model answer, under a minute.** One sentence each for four parts. The claim: what is true, with the
number. The evidence: the comparison that shows it, with its denominator and window. The caveat: the
one thing that could make it wrong and how big that risk is. The action: what she should do on
Monday and what it costs. For example: orders per customer fell from Q1 to Q2 while the customer
count held; the fall shows in three of four segments over matched windows; one segment is small
enough that its fall may be noise; so hold the acquisition budget and fund a retention test.

**Follow-up.** "Your caveat, for your own example: how would Meera know if it came true?"

**What the follow-up separates.** Understood: names the check and when it can be read, such as the
small segment's next month compared with its own trend. Memorised: a generic caveat such as "the data
may have errors".

**A weak answer sounds like.** The analysis told in the order it was done, from loading the data.

### T05-L2 `[F]` The number

**Anchor.** Week 1 Thursday: "Why is a rate without a denominator meaningless?" (Week 1 Tuesday) and
the four-part note.

**Ask.** "A colleague's claim for Meera reads: 'Retail-Plus is slipping: orders down 12 percent.' What
is missing before it goes to her?"

**Model answer, under a minute.** The denominator and the window. Orders down 12 percent could mean
fewer members or the same members ordering less, and those lead to different actions, so I want
orders per member. It needs the two windows, matched in length. It needs to say whether 12 percent is
larger than the tier's normal movement. And it needs the action. A version for Meera: orders per
Retail-Plus member fell 12 percent from Q1 to Q2 over matched windows, larger than any quarter this
year; the member count held; so the tier's problem is frequency, and the retention offer goes there
first.

**Follow-up.** "The member count fell 12 percent too. Rewrite the sentence."

**What the follow-up separates.** Understood: orders per member held, so the tier is losing members,
which is an acquisition or renewal problem, and the action changes. Memorised: keeps "slipping"
without recomputing.

**A weak answer sounds like.** "Add a chart to make it clearer."

### T05-L3 `[D]` The judgement (reserve)

**Anchor.** Week 1 Thursday: "The CEO wants a yes or no and the honest answer is 'not yet'; what do
you say, and how do you hold the line when marketing pushes?"

**Ask.** "Meera asks: should I fund the Student segment, yes or no? The honest answer is not yet.
What do you say?"

**Model answer, under a minute.** I say not yet, then what would make it yes and when we will know.
I give what we do know, the segment's size and its trend, with the gap that is still inside the noise.
I name the cost of each wrong call, funding a segment that does not respond or missing one that
would. And I offer the decision she can make today: a small, time-boxed test with a held-out group,
read in six weeks.

**Follow-up.** "The marketing lead says analysts never commit to anything. Answer them."

**What the follow-up separates.** Understood: commits to a decision rule, "if the test group's orders
per customer beat the held-out group by this much, we fund it", which is a commitment. Memorised:
repeats "we need more data".

**A weak answer sounds like.** A yes to please the room, or a lecture on statistics with no decision.

---

## T06. The warehouse query Finance audits

### T06-L1 `[S]` The move

**Anchor.** Week 2 Monday: "WHERE against HAVING, one sentence each" and "Explain the logical order
in which a SQL query executes."

**Ask.** "Anand wants every segment with more than 500 customers in Q2, counting completed orders only.
Where does each condition go in the query, and why there?"

**Model answer, under a minute.** Completed orders only is a filter on rows, so it goes in WHERE and
runs before the grouping. More than 500 customers is a filter on a group's count, which exists only
after grouping, so it goes in HAVING. The query runs FROM, then WHERE, then GROUP BY, then HAVING,
then SELECT, then ORDER BY and LIMIT, which is why the order of the conditions follows the order of
the business question.

**Follow-up.** "Why can you not use the alias you named in SELECT inside WHERE?"

**What the follow-up separates.** Understood: SELECT runs after WHERE, so the alias does not exist
yet. Memorised: "it is a SQL rule".

**A weak answer sounds like.** "HAVING is like WHERE but for groups", with no reason and no order.

### T06-L2 `[F]` The number

**Anchor.** Week 2 Monday: "Why would you compute a KPI in the warehouse rather than in a notebook?"
The trap is orders per customer returning 1 because Postgres divides integers.

**Ask.** "Your Monday query returns orders per customer of exactly 1 for every segment. The head of
Retail-Plus reads it as nobody coming back. What happened?"

**Model answer, under a minute.** Both counts are integers, and Postgres divides integers as integers,
so 1.4 becomes 1. Casting one side to numeric gives the real ratio. I would also check the
denominator is COUNT of distinct customers, because COUNT of rows counts orders, and orders over
orders is 1 for a different reason. Before the number went out I should have compared it with the
Week 1 figure for the same window, which was well above 1.

**Follow-up.** "How do you stop this reaching Anand next Monday?"

**What the follow-up separates.** Understood: a check query that compares the KPI with a known value
or a sensible range and fails loudly. Memorised: "cast to float" and nothing about the check.

**A weak answer sounds like.** "Customers are not returning."

### T06-L3 `[D]` The judgement (reserve)

**Anchor.** Week 2 Monday: "A stakeholder's analyst must audit your query; what changes in how you
write it, and what would you refuse to compute in a notebook?"

**Ask.** "Anand's analyst will audit your KPI query line by line. What changes in how you write it, and
what would you refuse to compute in a notebook?"

**Model answer, under a minute.** I write it as named steps, one CTE per business step, so each step
can be run and checked on its own. Every filter and window is explicit, every LIMIT has an ORDER BY
with a tie-break, and a reconciliation query beside it proves the total against Finance's number. I
would refuse to compute Finance's KPI in a notebook, because a notebook copy drifts from the
warehouse and then there are two versions of one number.

**Follow-up.** "Two learners ran your top-10 query and got different lists. Why?"

**What the follow-up separates.** Understood: LIMIT without ORDER BY, or ties at the cut, returns
whatever rows come first. Memorised: "the data changed".

**A weak answer sounds like.** "I would add comments."

---

## T07. Booked against collected, and joins that lie

### T07-L1 `[S]` The move

**Anchor.** Week 2 Tuesday: "INNER against LEFT join: what does each drop or keep?" and "How do you
find orders with no payment?"

**Ask.** "Anand wants booked against collected, order by order. INNER join or LEFT join from orders to
payments, and what does the wrong one hide?"

**Model answer, under a minute.** LEFT from orders to payments, because it keeps every order and shows
the unpaid ones with an empty payment. An INNER join drops unpaid orders, so every row on screen looks
paid and booked appears to equal collected. The unpaid list is the orders where the payment side is
empty, the anti-join, and that list is usually what Anand wanted in the first place.

**Follow-up.** "You add WHERE payment status equals success. What happens to your LEFT join?"

**What the follow-up separates.** Understood: the filter removes the rows with an empty payment, so it
behaves as an INNER join; the condition moves into the ON clause. Memorised: "LEFT keeps everything".

**A weak answer sounds like.** "LEFT keeps all the rows from both tables."

### T07-L2 `[F]` The number

**Anchor.** Week 2 Tuesday: "Revenue doubled after a join and every row looks fine; where do you
look?" The trap is a join fan-out that doubles collected revenue.

**Ask.** "After you join payments to orders, collected revenue is almost double what Finance reports,
and every row looks right. Where do you look?"

**Model answer, under a minute.** At the grain. Some orders have more than one payment row, retries or
split payments, so the join repeats the order for each and the sum counts the order amount twice. I
count rows and distinct order ids before and after the join; if rows grew, the join fanned out. The
fix is to bring payments to one row per order first, summed, and then join.

**Follow-up.** "What single check, run every time, would have caught it?"

**What the follow-up separates.** Understood: the row count after the join equals the order count, or
the order id stays unique after the join. Memorised: "remove duplicates after the join", which hides
the cause.

**A weak answer sounds like.** "Finance must be missing some payments."

### T07-L3 `[D]` The judgement

**Anchor.** Week 2 Tuesday: "Design the validation you run before a joined number reaches Finance, and
say what you do when it fails at 5 pm on reporting day."

**Ask.** "Design the checks you run before a joined number reaches Anand. Then it is an hour before his
reporting deadline and one check fails. What do you do?"

**Model answer, under a minute.** Row counts before and after, key uniqueness on each side, the total
amount before and after, the unmatched rows on each side counted and listed, and a bridge from booked
to collected. If one fails near the deadline I do not ship the wrong number. I tell Anand straight away
what failed and how big it is, and give him either last week's reconciled number or today's with the
gap stated in rupees, and the time the fixed number will reach him.

**Follow-up.** "Anand says send it anyway, the board pack is due. What do you send?"

**What the follow-up separates.** Understood: sends it with the caveat in rupees written on the number
itself, and logs the decision. Memorised: "fix it quickly".

**A weak answer sounds like.** "I would fix the bug fast and send it."

---

## T08. Ranking, ties and change over time

### T08-L1 `[S]` The move

**Anchor.** Week 2 Wednesday: "Top-3 per group: GROUP BY or a window, and why?"

**Ask.** "Marketing wants the top three members by spend in each segment. GROUP BY or a window
function, and why?"

**Model answer, under a minute.** A window. GROUP BY collapses each segment to one row, so it can give
the top spend but loses the members behind it. A window ranks members inside each segment, partitioned
by segment and ordered by spend, and keeps every row, so I filter to rank three or better in an outer
query.

**Follow-up.** "Two members tie for third place. How many rows does marketing get?"

**What the follow-up separates.** Understood: depends on the function, RANK gives four, ROW_NUMBER
gives three with an arbitrary pick unless a tie-break is added, and marketing decides the rule.
Memorised: "three".

**A weak answer sounds like.** "ORDER BY spend and LIMIT 3", which gives three for the whole company.

### T08-L2 `[F]` The number

**Anchor.** Week 2 Wednesday: "How would you find customers whose spend fell two months in a row?" The
trap is LAG without PARTITION reading another customer's month.

**Ask.** "Your falling-spend list, built with LAG, flags a customer whose spend rose every month. What
went wrong?"

**Model answer, under a minute.** LAG without PARTITION BY customer reads the previous row of the whole
table, which at the start of each customer's months belongs to someone else. So the first month of a
customer is compared with another customer's last month. The fix is to partition by customer and order
by month, and to fill missing months first, because a skipped month otherwise vanishes from the
comparison.

**Follow-up.** "A customer bought in January and March and nothing in February. Did their spend fall?"

**What the follow-up separates.** Understood: with February filled as zero, yes, it fell; without the
fill, LAG compares March with January; marketing decides whether a gap month counts. Memorised: "sort
by customer".

**A weak answer sounds like.** "The data must have duplicates."

### T08-L3 `[D]` The judgement

**Anchor.** Week 2 Wednesday: "The business says 'ties rank the same'; which function, and how many
rows might the top-N report ship?"

**Ask.** "Marketing says ties rank the same, and wants the top 50 members. Which function, how many rows
might you ship, and what do you tell them?"

**Model answer, under a minute.** RANK, since ties share a rank. The top 50 by RANK can ship more than
50 rows when members tie at the cut, and DENSE_RANK can ship many more. I would say it in the report's
first line: 51 members, because two tie at 50th. If a budget covers exactly 50, that is a business
tie-break, such as tenure or most recent order, and marketing picks it.

**Follow-up.** "The voucher budget covers exactly 50. What do you do?"

**What the follow-up separates.** Understood: asks for the tie-break rule and writes it into the
query, so the list is repeatable. Memorised: "use ROW_NUMBER", which picks one tied member arbitrarily.

**A weak answer sounds like.** "Just take the first 50."

---

## T09. The customer table in pandas

### T09-L1 `[S]` The move (reserve)

**Anchor.** Week 2 Thursday: "groupby in the split-apply-combine sentence."

**Ask.** "The growth team wants one row per customer with spend, order count and last order date. Say
how you build it in one sentence, then the check you run."

**Model answer, under a minute.** Split the orders by customer, apply a sum, a count and a maximum
date to each group, and combine the results into one row per customer. The check is that the result
has exactly as many rows as there are distinct customers in the orders, and that total spend matches
the orders' total.

**Follow-up.** "Customers with no segment have vanished from your table. Why?"

**What the follow-up separates.** Understood: groupby drops missing keys by default, so dropna=False,
or fill the segment first. Memorised: restates split-apply-combine.

**A weak answer sounds like.** The definition, with no check.

### T09-L2 `[F]` The number

**Anchor.** Week 2 Thursday: "Which merge argument raises on duplicate keys, and which error?" The trap
is a merge that doubles a customer's spend.

**Ask.** "After you merge the campaign exposure table onto the customer table, one customer's spend has
doubled. Which argument would have stopped it, and what is the fix?"

**Model answer, under a minute.** validate, set to one_to_one or many_to_one, makes the merge raise a
MergeError when the key is duplicated on the side that should be unique. Here the exposure table has
the customer twice, so the customer's row was repeated. The fix is to bring exposure to one row per
customer first, deciding what two exposures mean, and then merge.

**Follow-up.** "Why not drop duplicates after the merge?"

**What the follow-up separates.** Understood: it hides which side was duplicated and can remove
genuine rows. Memorised: "that also works".

**A weak answer sounds like.** "I would check the shape of the result."

### T09-L3 `[D]` The judgement

**Anchor.** Week 2 Thursday: "Same question, three tools: how do you choose, and defend one choice?"
The trap is recency measured from today instead of the data's last date.

**Ask.** "The customer table refreshes every Monday. A colleague computes recency as days from today's
date to each customer's last order. What goes wrong, and what do you choose?"

**Model answer, under a minute.** Recency from today ages every customer with the calendar, so an
extract that arrives late, or a table read a week later, makes the whole base look more lapsed than
it is. I pin an as-of date to the data, the last order date in the extract or the extract date, and
print it on the table, so two people reading it on different days see the same recency.

**Follow-up.** "Marketing sends the win-back offer to anyone over 90 days. How many customers move if
the extract is a week stale and you use today?"

**What the follow-up separates.** Understood: everyone between 83 and 90 days crosses the line and gets
an offer they should not; the learner says how to count them. Memorised: "use the max date".

**A weak answer sounds like.** "Today's date is fine since we refresh weekly."

---

## T10. Excel for the stakeholder, and choosing the tool

### T10-L1 `[S]` The move (reserve)

**Anchor.** Week 2 Friday: "SQL, pandas or Excel: how do you choose?"

**Ask.** "SQL, pandas or Excel: how do you choose, for one of Meera's asks?"

**Model answer, under a minute.** The warehouse, in SQL, for a number Finance relies on every week,
because it runs close to the data and one version exists. pandas for a multi-step analysis or a
reshape I have to reproduce top to bottom. Excel for the stakeholder who wants to change assumptions
and watch the answer move, fed from an exported, cleaned table and never used to edit the source.

**Follow-up.** "Meera's chief of staff wants to edit the numbers themselves. What do you give them?"

**What the follow-up separates.** Understood: input cells for assumptions, formulas protected, the
data exported read-only. Memorised: "Excel because they know Excel".

**A weak answer sounds like.** "Whatever tool I am most comfortable in."

### T10-L2 `[F]` The number

**Anchor.** Week 2 Friday: "Your pivot shows a different total from the warehouse; where do you look
first?" The trap is a pivot double-counting the double-paid orders.

**Ask.** "Your pivot shows collected revenue Rs 3 lakh above the warehouse figure for the same quarter.
Where do you look first?"

**Model answer, under a minute.** First at what the pivot was built on. If it sits on the raw export,
the double-paid orders are in it twice, and a gap of a round sum points there. Then the filters: the
same window, rows hidden by a filter that a SUM still counts, and amounts typed as text that the pivot
skipped or counted differently. I rebuild the pivot on the cleaned table and check it lands on the
warehouse number.

**Follow-up.** "The gap equals the total of the double-paid orders exactly. What do you change so it
cannot happen again?"

**What the follow-up separates.** Understood: the pivot's source becomes the cleaned, reconciled table,
and the front page carries the reconciliation line. Memorised: "delete the duplicates in Excel".

**A weak answer sounds like.** "Excel must be calculating wrongly."

### T10-L3 `[D]` The judgement

**Anchor.** Week 2 Friday: "Two directors change assumptions in the room and the sheet recalculates
differently for each; what did you get right and what do you fix?" and "How do you present one number
so it is not misread?"

**Ask.** "Two directors change assumptions in the meeting and each gets a different answer from your
sheet. What did you get right, and what do you fix?"

**Model answer, under a minute.** I got the right thing half built: the sheet recalculates, so the
assumptions are live. What needs fixing is that the assumptions are scattered, so two people edited
different cells. I would put every assumption in one labelled block, show two scenario columns side
by side so both directors see both answers, and keep the source data locked. The front page shows one
number with its unit, denominator, period and the comparison it is read against.

**Follow-up.** "Show me the front-page number for revenue per customer in one line."

**What the follow-up separates.** Understood: states value, unit, denominator, period and comparison,
such as Rs 4,850 per active customer in Q2 against Rs 5,100 in Q1. Memorised: "a big number in bold".

**A weak answer sounds like.** "Lock the sheet so nobody can change it."
