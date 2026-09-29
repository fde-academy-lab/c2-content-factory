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

- Your largest-fall city fell mostly through frequency. If your sentence says it lost buyers, compare
  its buyers in the two quarters before you send it.
- The city with the second-largest fall moved the other way on frequency: its orders per buyer rose
  slightly. Say which branch carries its fall.
- Six of the twelve city-quarters hold fewer than 30 orders, so a city split read as a finding
  overstates what the book can show. Say which threshold you used and what it allows you to claim.

## Parts 2 to 4, the checks

- Both of your queries run unchanged on the warehouse, and each has a comment line that names the
  question, the reading of revenue and the denominator.
- Your run order reads FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT.
- Your SQLBolt line names one exercise and says what would change.
