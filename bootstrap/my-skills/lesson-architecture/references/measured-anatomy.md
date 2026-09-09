# Measured anatomy of the reference material

Two independent sites teaching the same concept, read side by side on
30 August 2026. What matches across both is structural. What differs is
incidental and can be chosen freely.

Sources: `mysqltutorial.org/mysql-basics/mysql-order-by/`,
`pgtutorial.com/postgresql-tutorial/postgresql-order-by/`,
`mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/`,
`pgtutorial.com/`.

---

## The same lesson, both sites

| Slot | Site A | Site B |
|---|---|---|
| Title | "MySQL ORDER BY" | "PostgreSQL ORDER BY: Sorting Rows in a Query" |
| Reading time printed | 5 minutes | 3 minutes |
| Promise line | "in this tutorial, you will learn how to sort the rows in a result set" | "you will learn how to use the ORDER BY clause to sort rows in ascending or descending orders" |
| Broken default stated first | The order of rows is unspecified | The statement returns rows in an unspecified order by default |
| Skeleton with placeholders | Yes, then each option decomposed into its own one-line block | Yes, then a numbered first-second-third decomposition |
| The machine | Diagram: evaluation runs FROM, then SELECT, then ORDER BY | Numbered list of the same three, plus the alias consequence spelled out |
| World | Shared eight-table database loaded once for the whole site | A seven-row table created inline for this lesson |
| Example count | Six | Six |
| Real output printed | Every example | Every example |
| Runnable link per example | "Try It Out" | "Try it", carrying the query encoded in the URL |
| Gotcha section | Null ordering, placed last | Null ordering, placed last |
| Rules block | Four bullets | Four bullets |
| Quiz | Absent | Separate page, linked |
| Prev and next | Yes, named | Yes, named |
| Family visible | Sidebar, roughly 84 units in 12 groups | Sidebar, 101 units in 20 sections |
| Per-unit feedback | Was this tutorial helpful, yes or no | Same |

### What this tells you

Everything in the left column of that table is structure and transfers. The
choice between a shared database and an inline table is free. The choice
between a diagram and a numbered list for the machine is free. The presence of
a quiz is free. The nine slots and their order are not free; both sites landed
on the same sequence independently.

---

## The two ladders

Neither ladder introduces two ideas on one rung, and both end on the gotcha.

**Site A:** one column ascending, the same column descending, two columns with
opposite directions, sorting by a computed expression, the same expression
named with an alias, sorting by a custom rank using a position function, then
null ordering.

**Site B:** one column, the same column descending, two columns, a computed
expression, the same expression named with an alias, sorting by a date, then
null ordering with the two explicit null placement options.

The shared shape: **single, then multiple, then computed, then named, then a
different data type, then the edge case.** That ladder generalises well beyond
sorting. For any operation, teach it on one thing, then on several, then on
something derived, then give the derived thing a name, then change the type of
thing, then break it.

---

## The world, measured

Site A's world is a scale-model car retailer. Eight entities: customers,
products, product lines, orders, order line items, payments, employees,
offices. Each gets a one-line purpose. A relationship diagram is provided as a
downloadable page with the instruction to print it and keep it on the desk.

Site B's lesson world is a seven-row, five-column inventory of phones. Every
column carries a witness:

| Column | Witness planted | Which lesson needs it |
|---|---|---|
| price | Two rows tied at 999.99 | The multi-column sort, which otherwise looks identical to the single-column sort |
| color | Two rows missing a value | The two null-placement options, which otherwise produce identical output |
| quantity | Inverted against price | Sorting by price times quantity, which otherwise reproduces the price order |
| updated_date | Three rows sharing one date | Date sorting with ties, showing stability is not guaranteed |
| name | Two families with shared prefixes | The alphabetical tiebreak inside a price tie |

Seven rows carry five distinct teaching points. That density is the target.

---

## The map, measured

Site B's homepage is the strongest single artifact of the four. It is a
complete syllabus readable in three minutes.

- 20 numbered sections, 101 units
- Mean 5.05 units per section, range 2 to 12
- Every section has a one-sentence capability promise, most beginning "In this
  section, you will learn how to"
- Every unit has a verb-first one-liner
- Section names are tasks: "Filtering rows in a table", "Joining tables",
  "Grouping rows", "Enhancing table structure"

The ordering is capability-first rather than logically complete. Section 1
teaches create, insert, select and drop, so the learner does a full cycle
immediately. Proper design, keys and constraints arrive in section 3, after the
learner has already felt the absence of them. A reference manual would have
reversed those two.

Site A's grouping is the same idea in a sidebar. Its bulge is instructive:
28 of roughly 84 units sit under "Querying data", which is an honest signal
about where the real weight of the subject sits. Do not flatten sections toward
equal size; let the bulge show where the course actually lives.

---

## Translating the nine slots into slides

One unit becomes four to eight slides. This is the mapping that has worked.

| Slot | Slides |
|---|---|
| Title and promise | Folded into the section map slide, current section marked |
| Broken default | One slide: what happens today without this, with a real number |
| Skeleton | One slide: the shape with placeholders, parts numbered down the side |
| The machine | One slide: the diagram, with the one consequence stated in the lead line |
| World | Not repeated per unit. One world slide near the front of the deck |
| Ladder | Two to four slides, one rung each, real output shown on every one |
| Gotcha | One slide, the failure shown rather than described |
| Rules | One slide, four bullets, each a complete sentence |

The ladder is where slide count is won or lost. Three rungs on one slide is the
compression failure that makes a deck useless a month later. One rung per slide
with its output visible is the version a learner can revise from.

---

## What was deliberately not copied

- The flat, voiceless register. Search-landing pages need no hook because
  arrival implies intent. A scheduled session does, so the cold open on the
  failure stays
- Full per-page self-containment. It causes repetition in a linear deck.
  Self-contain the unit, connect the slides
- Byte-sizing by term. It works because the subject has separable clauses.
  Judgement subjects are entangled, so size units by decision instead
