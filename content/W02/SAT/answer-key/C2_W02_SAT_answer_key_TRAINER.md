# Week 2 recap: answer key

TRAINER ONLY. For the Academic TA leading the discussion, and for peer cross-evaluation.

Each item gives the full-credit answer, then the most common partial answer and why it falls
short. The partial answers matter more than the full ones: they are what the room will have
written, and naming the gap is the discussion.

---

## Section A. The language

**A1.** `WHERE` decides whether to keep one row, judged on that row alone, before any grouping
exists. `HAVING` decides whether to keep a whole group, judged on the group, after the grouping has
happened.

*Common partial:* "`WHERE` is for rows and `HAVING` is for aggregates." True and incomplete. It
states the rule without the reason, so it does not predict anything new. The timing is the answer.

**A2.** `SELECT` runs after `WHERE` and before `ORDER BY`. The alias does not exist when `WHERE` is
evaluated and does exist by the time `ORDER BY` runs.

*Common partial:* "Aliases only work in `ORDER BY`." Memorised rather than understood, and it
fails the moment somebody asks about `GROUP BY` or `HAVING`.

**A3.** Neither is wrong. Without `ORDER BY` the server promises nothing about row order, so
returning different rows is allowed behaviour rather than a bug.

*Common partial:* "The data must have changed." The item says unchanged, and the instinct to
blame the data rather than the guarantee is worth naming out loud.

**A4.** It promises a name for a result, usable for the rest of the statement. It promises nothing
about how the work is done: the planner may run the block once or fold it into the outer query.

*Common partial:* "It runs the query once and stores the result." A reasonable belief and not a
guarantee, and acting on it as a performance strategy is how people are surprised.

---

## Section B. Joins

**B1.** `INNER` keeps only orders that have a payment, so it answers what paying customers did.
`LEFT` keeps every order paid or not, so it answers what was booked and what came in against it.
The 30 unpaid orders are exactly the difference.

*Common partial:* Answering in terms of rows kept and dropped without naming a question. The item
asks for the business question on purpose, because the row arithmetic is the easy half.

**B2.**

```
Rows before: 1,000 orders.
Rows after:  1,450.
Difference:  450 orders carry two payment rows, of which 400 are instalment plans and 50
             are gateway retries. 30 orders carry none.
Therefore:   do not SUM the order amount over this join.
```

*Common partial:* Three lines with no "therefore". The therefore is the line that saves somebody,
and a reconciliation without it is a description rather than a decision.

**B3.** The join multiplied rows rather than corrupting them. Each row pairs a real order with a
real payment; an order with two payment rows appears twice, and an aggregate over the joined table
counts its amount twice. Nothing is wrong with any row and the total is wrong.

*Common partial:* "There are duplicates in the data." There are not. Neither table holds a
duplicate row, and the distinction between duplication in a table and duplication in a join is the
whole item.

**B4.** The 450 are not a random slice. Large invoices get instalment terms, so the duplicated
orders are the ones carrying the revenue: they hold over 80 percent of the book.

*Common partial:* "Because 450 is nearly half of 1,000." Arithmetic on the wrong quantity. The
answer is about value, not count, and a room that only gives the count answer has not understood
why fan-out is dangerous rather than annoying.

**B5.** Keep every order, attach payments, then keep only the rows where the payment side is
empty. An anti-join. An `INNER` join would have removed those rows before you could look at them,
returning nothing and looking like good news.

*Common partial:* Describing the anti-join correctly and omitting the second half. The second half
is the item.

**B6.** Two rows with identical amounts is a repeated charge. Two rows with different amounts is a
split invoice, which is correct. A rule cannot decide it because the separator is a business fact
about what the payments mean, and a rule that deleted every duplicate would delete four hundred
legitimate instalments.

*Common partial:* Getting the test right and not saying why a rule fails. The second half is what
distinguishes an analyst from a script.

---

## Section C. Windows

**C1.** `ROW_NUMBER`: 1, 2, 3, 4. `RANK`: 1, 2, 2, 4. `DENSE_RANK`: 1, 2, 2, 3.

*Common partial:* Swapping `RANK` and `DENSE_RANK`. Worth one line in the discussion: `RANK`
answers how many rows are ahead of me, `DENSE_RANK` answers how many distinct levels are ahead.

**C2.** `RANK`. It can ship more than fifty names, and in this data it ships fifty-one, because
two members tie at position fifty and both are kept.

*Common partial:* Naming `RANK` and saying it ships fifty. Half the item. The business owner asked
specifically not to lose a name, so the extra name is the requested behaviour.

**C3.** It is not reproducible. Nothing in the data separates tied rows, so nothing in the plan has
to keep them in a fixed order, and two people running the same query can hand out different names.

*Common partial:* Repeating the fairness argument in different words. The item explicitly excludes
it, and the reproducibility argument is the one that convinces an engineer.

**C4.** There is no previous row, so `lag` has nothing to return. It is correct because a member
with one month of data is neither falling nor steady: you cannot tell. In a two-LAG flag the NULL
fails the comparison and the member drops out, which is the honest outcome.

*Common partial:* "It returns NULL." True and not an answer to the question asked, which is why
that is right and what it does to the flag.

**C5.** The window's `ORDER BY` could tie, so the row order within a tie was undefined and the
accumulation differed. It is worse than an incorrect number because nobody can reproduce the
argument about it: the next run may show something else again.

*Common partial:* "You need `ORDER BY`." The query had one. The point is that it was not unique.

---

## Section D. pandas

**D1.** Splitting and combining. The applying is left to you, which is the only part that was ever
about your question.

**D2.** `validate=`, raising `pandas.errors.MergeError`. Full credit mentions that the message
names the offending keys.

*Common partial:* Naming the argument and not the error, or naming a `ValueError`. Worth
correcting precisely, because the error name is what a candidate is asked for in a screen.

**D3.** That the right-hand table has duplicate keys, so a merge on it can fan out. It has told
you nothing about the left.

*Common partial:* Answering "the data is dirty". Which table and which side is the item.

**D4.** Widening creates a cell for every combination, including the ones with no data, and
melting turns every cell into a row. The gaps that had no row in the original long frame now do.

*Common partial:* "It should be the same." A reasonable expectation and wrong, and being surprised
by it once is better than being surprised by it in production.

---

## Section E. The last mile

**E1.** Rows divided by distinct keys. You are looking for 1.00. Anything above one and the file is
not one row per that key, whatever its name says.

**E2.** Nothing. It summed the column it was given across the rows it was given. The problem was
upstream and arrived in the file.

*Common partial:* Blaming the pivot or the tool. The item is designed to catch that reflex, and
the whole lesson of the day is that every check on the pivot passes.

**E3.** The approximate-match argument. It is worse than an error because it returns a real
member's real data: a complete-looking row nobody questions, where `#N/A` is ugly and truthful.

**E4.** A denominator, a period and a comparison. When one is missing the reader supplies it from
whatever was on the previous slide, and that becomes what the number means when they repeat it.

**E5.** Something below the input is a typed number rather than a formula. A result cell holding a
typed value is indistinguishable from a computed one until exactly this moment.

---

## Section F. The judgment

**F1.** Who owns this number, for how long, and who has to be able to read it. None is about syntax
because the tools all compute the same answer; what differs is ownership, lifetime and audience.

*Common partial:* Answering with tool capabilities, which is the habit the whole week works
against.

**F2.** A notebook has no audit trail a controller can read, no guarantee it ran against current
data, and a cell edited at 4 pm looks identical to one nobody touched.

*Common partial:* Any answer mentioning speed or library limits. The objection is procedural and
reaching for a technical one is a tell worth naming gently.

**F3.** Whatever is in Excel must be rebuildable from the warehouse in one run. What breaks it
first is a deadline and a correction made in the sheet that exists nowhere else.

*Common partial:* Naming the condition and blaming carelessness. Deadlines break it, not
character.

**F4.** Something close to: last week's figures came from a 200-row extract, so the levels were a
sample's levels; the shape held, and Retail-Plus frequency is still the branch that moved; every
number from now on comes from the warehouse and each one has a query behind it.

*Common partial:* An apology. Nothing was done wrong, and an answer that opens by apologising has
misread the situation. Worth discussing directly, because the instinct is common and it is
expensive in a client room.

---

## Section G. The transfer

**G1.** There is no single right answer. A strong one names habits rather than techniques:

- Take the row count before any total, and explain the difference rather than checking it.
- Name the denominator for every number, in writing, before anybody asks.
- Say what one row of a file means before pivoting it or sending it.
- Ask who owns a number, for how long, and who must read it, before choosing where it lives.
- State what is a sample and what is the book.

What changes: the entity model, the vocabulary, who the stakeholders are, what a good number even
looks like in that unit. A health business does not have orders and channels, and reaching for
Retail's tree in Health is the failure this item is testing for.

The refusal to assume is the part that separates answers. Strong ones refuse to assume the shape
of the data, the meaning of a segment, or that the stakeholder's question is the question that
matters. Weak ones refuse to assume nothing and describe the method confidently.
