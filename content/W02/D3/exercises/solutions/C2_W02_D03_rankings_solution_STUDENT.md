# Solution: how many make the list when two members tie?

Answers: 1c 2a 3d 4b 5d 6c 7b

## The idea being tested

The tie rule is a business decision written as a function name. ROW_NUMBER breaks a tie
arbitrarily, RANK shares the position and leaves a gap after it, and DENSE_RANK shares the position
without a gap, so each rule ships a different number of rows whenever a tie sits near the line.
Members P to U are invented for this set; the Retail-Core figures come from the warehouse (v4),
checked 29 Sep 2026.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | RANK gives the four tied members the position of the first of them, 2, and the next member takes the position after all four, 6, so a gap of three opens. | a is ROW_NUMBER. b is DENSE_RANK. d closes the gap by one, which no function does. |
| 2 | a | DENSE_RANK gives the tie one number and the next member the very next number, so U is 3. | b is RANK. c is ROW_NUMBER. d treats P as tied with the four, and P spent more. |
| 3 | d | ROW_NUMBER numbers every row once, and with only spend in the order the database may place tied rows in any order, so a rerun can number them differently. | a is what RANK and DENSE_RANK do. b holds only when the member name is added to the order as a tiebreaker. c assumes an order date the query never read. |
| 4 | b | ROW_NUMBER stops at three rows, RANK keeps P and the whole tie at 2, which is five, and DENSE_RANK also keeps U at 3, which is six. | a treats the cut-off as a row limit. c forgets that U's dense number is 3. d cuts the tie in half, which RANK never does. |
| 5 | d | Two ties above the fiftieth place each give two members one dense number, so the dense numbers run two behind RANK by the line: the 51st and 52nd members, at Rs 2,950 and Rs 2,910, carry dense numbers 49 and 50. | a is false on this data, since the fiftieth member at Rs 2,980 stands alone. b confuses a member row with a month row, and this table has one row per member. c is false, since the two spend Rs 2,950 and Rs 2,910. |
| 6 | c | RANK gives tied members the same position and keeps everyone at the line, and the report states the count so a list of fifty-one reads as a decision rather than a bug. | a sounds like "ranked the same" and ships extra members below the tie whenever a tie sits higher up. b drops one tied member by a coin toss that customer_id only makes repeatable. d ships forty-nine when a tie crosses the line, which is what the segment head forbade. |
| 7 | b | ROW_NUMBER must give two equal spenders different numbers, and with nothing else in the order the database chooses which of them is tenth, so the choice can change between runs with the same data. | a and c need a change in the data, and the stem rules it out. d is false, since RANK gives both tied members position 10 and keeps them both. |

## The part worth arguing about

Item 6, option b. A tiebreaker on customer_id makes ROW_NUMBER repeatable, so Monday's list and
Tuesday's list agree. It is still a coin toss in business terms, because the member with the lower
id stays on and the other one drops off with the same spend. Repeatable and fair are two different
properties, and the segment head asked for fair.

## Where the pattern lives in production

Leaderboards, sales incentive lists, top-N product widgets and campaign targeting lists all carry
this choice, and the one that bites is the silent ROW_NUMBER in a scheduled job: the list changes
between runs, nobody changed the data, and a customer asks why the reward disappeared. The habit
is to count what each rule ships at the line, and to write the rule and the count in the report.
