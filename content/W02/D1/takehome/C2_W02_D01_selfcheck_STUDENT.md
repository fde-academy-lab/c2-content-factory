# Self-check: the take-home, before class does

Check each number alone. If yours differs, the first place to look is in the column beside it.

## Part 1, the checkpoints

| Checkpoint | The number you should reach | If yours differs, look at |
|---|---|---|
| Cities in the result | 6 | the JOIN between the two steps, which should be on city |
| Retail-Plus revenue across the six cities, Q1 | Rs 5,85,770 | the segment filter, which belongs in each step's WHERE |
| Retail-Plus revenue across the six cities, Q2 | Rs 4,13,380 | the quarter filter in the second step |
| Retail-Plus orders across the six cities, Q1 and Q2 | 215 and 140 | whether you counted rows or customers |
| The first row, ordered by the change in rupees | the city whose revenue fell by Rs 92,710 | the direction of your ORDER BY |
| Its orders per buyer, Q1 then Q2 | 2.86 then 1.63 | integer division |
| City-quarters under 30 orders | 6 of the 12 | whether HAVING tests the count of orders |
| The only city whose Retail-Plus revenue rose | up 53.4 percent | the sign of your change column |

## Part 1, the reasoning to check

- Your sentence names the branch behind your largest-fall city. Before you send it, put that city's
  buyers, orders per buyer and revenue per order side by side for both quarters, and check that the
  branch you named is the one that moved furthest.
- Do the same for the city with the second-largest fall, and name its branch from its own numbers
  rather than from the first city's.
- Your threshold sentence quotes the count of thin city-quarters from your own `HAVING` query and
  says what that count allows you to claim about a city split.

## Parts 2 to 4, the checks

- Both of your queries run unchanged on the warehouse, and each has a comment line that names the
  question, the reading of revenue and the denominator.
- Your run order reads FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT.
- Your SQLBolt line names one exercise and says what would change.
