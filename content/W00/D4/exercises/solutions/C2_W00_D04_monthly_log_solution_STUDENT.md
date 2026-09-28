# Solutions: the month's log

Week 0, Thursday. Released once the exercise has closed.

## The idea being tested

Each item asks one idea from the SQL half a question it can only answer if the idea is understood
rather than recognised: which quotes wrap text, which rows a `WHERE` keeps, what an aggregate returns,
how many groups a `GROUP BY` makes, where a filter on groups belongs, and the fixed order in which
clauses are written.

## The answers

Answers: 1b 2c 3a 4c 5d 6b 7a 8b 9c 10a 11d

Item 12 is an order, so it takes four letters: b d c a.

| No. | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Week 2 has ten issues, numbers 9 to 18 | Eight is week 1; eighteen is weeks 1 and 2 together; 38 is the whole month |
| 2 | c | Text sits in single quotes | Double quotes name a column, so Postgres looks for a column called Commerce; bare Commerce is also read as a column; quoting 'dept' compares two pieces of text, which are never equal |
| 3 | a | Issues 12, 26 and 33 are Arts books kept past 14 days | Eleven counts every Arts issue; fourteen is the loan, not a count; nothing about the data makes it 0 |
| 4 | c | Issue 3, Calculus, was kept 20 days, the longest in Maths | 23 is the longest in the whole table, a Commerce book; 19 is the second longest in Maths; 12 is the first Maths row, not the largest |
| 5 | d | Week 3 has issues from Arts, Commerce, Maths and Science, one row each | One would need no `GROUP BY`; three forgets that Commerce first borrowed in week 3; ten counts the rows, not the groups |
| 6 | b | S02 has six issues, more than anyone | S01 and S03 have five each, so they tie for second; S09 has three |
| 7 | a | Algebra and Poetry have 7 each, and Calculus, Chemistry and Physics 5 each | Two counts only the books with 7; eight counts every book; three leaves out the pair tied at 7 |
| 8 | b | A condition on a group's count belongs in `HAVING` | `WHERE` runs before any group exists, so Postgres refuses an aggregate there; `ORDER BY` sorts and never removes; `AND` joins conditions inside a `WHERE` or a `HAVING` and cannot stand on its own |
| 9 | c | Week 4's late books are issues 31, 33 and 37, adding 9, 2 and 5 | Nine is only the Commerce book; fourteen is the loan; 53 is every late day of the month |
| 10 | a | The written order is fixed, and `WHERE` comes before `GROUP BY` | `COUNT(*)` needs nothing inside it; `FROM` is already in its place; numbers never need quotes |
| 11 | d | Science's ten issues add to 135 days, and 135 / 10 is 13.5 | 11.9 is the average of the whole table; 135 is the sum before dividing; 10.0 is the number of issues |
| 12 | b d c a | `FROM`, then `WHERE`, then `GROUP BY`, then `HAVING` | Any other order is a syntax error, as item 10 showed |

## The part worth arguing about

Item 2 is worth a minute. Options a and b both stop with an error, because Postgres reads Commerce as
the name of a column, and the unquoted one is even folded to lower case before it looks. Option d
does not fail at all: it compares the text 'dept' with the text 'Commerce', finds them different on
every row, and returns nothing. A query that runs and returns nothing looks like an answer, which
makes it the more expensive mistake.

## Where this lives in production

A librarian's month, a canteen's takings by counter, and a support team's tickets by category are
the same query: one table, a `WHERE` for the rows that matter, a `GROUP BY` for the breakdown, and a
`HAVING` for the groups worth a meeting. Week 2 builds every Monday report of the programme on this
shape.
