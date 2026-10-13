# Run sheet: the forecast tournament with a house bot

**TRAINER ONLY.** This sheet runs the day's signature activity, which plays out across the three case
chapters, after the four concept chapters have taught the five topics on the chai stall (invented).
The entrants are finance's rule (last year's same weeks plus 4 percent), the vendor's curve and every
group's own one-line rule. The house bot, the seasonal naive at Flipkart, a copy of the same week last
year, is the bar: nothing goes to the staffing plan unless it beats
the bot on the same thirteen hidden weeks, by the same measure, fixed before anyone scores. In round
three the bot itself turns out to be wrong about which week Diwali falls in, and the group that
notices first wins the plan. A trainer who did not write the day can run it from this page alone.

## Who plays which role?

| Role | Who | What they do |
|---|---|---|
| Referee and scorekeeper | The day's trainer | Fixes the rule at the start, keeps the wall scoreboard, says the lines below, plays finance in round three |
| Second scorer | The day's TA | Types each group's rule into notebook 06 and reads its score aloud, plays the vendor's sponsor in round three |
| Entrants | Groups of about four learners | Write one rule in one line, defend it, and vote before each reveal |

## What must be printed or set up before the room sits down?

| Material | File | How many |
|---|---|---|
| The twelve rows | `data/C2_W04_D05_twelve_rows_STUDENT.csv`, printed as a table, or `whiteboards/C2_W04_D05_twelve_rows_STUDENT.png` | One per group |
| The wall scoreboard | Drawn on the board: one row per entrant; columns for the rule in one line, MAE in shipments, weeks too high of 13, the misses priced in Rs lakh | One, on the wall all day |
| Finance's and the vendor's sponsor's role cards | `trainer/C2_W04_D05_role_cards_TRAINER.md` | One copy each, for the trainer and the TA |
| The festival calendar card | `trainer/C2_W04_D05_festival_calendar_card_TRAINER.md`, printed large | One, face down until half two's S4 |
| Sticky notes in two colours | | A pad per group, for the votes on half one's S41, S43, S51, S53 and S55 and half two's S3 |

## How do the minutes run?

| Turn | Minutes | Slides | What the room does |
|---|---|---|---|
| The rule | inside chapter 5 | Half one S5, then S39 and S40 | Hears the two forecasts, says what would make each wrong, hears the rule, names its group's entrant |
| Round one, chapter 5 | 37 | S38 to S48 | Reads the twelve rows by hand, writes its own rule in one line, forecasts Diwali 2025's week with every rule |
| Round two, chapter 6 | 30 | S49 to S59 | Votes on the scoreboard, watches its rule scored on the hidden weeks, prices the misses |
| Lunch | | | The scoreboard stays up |
| Round three, chapter 7 | 33 | Half two S2 to S11 | Votes on the bot's busiest week, turns the calendar card, back-tests 2025, books the plan; the objections follow on S14 |

## What does the trainer say at each turn?

**The rule, said word for word before anyone scores.** "The error measure is fixed now, before
anyone scores: mean absolute error in shipments on the thirteen held-out weeks, then the same errors
priced. Nothing goes to the plan unless it beats the house bot on those weeks."

**Round one.** "Each group writes one rule, in one line, that a planner could run on a spreadsheet:
what does it copy, and what does it add?" Collect the rules on the board before S43 shows the three
rules, so the room sees whose rule matches which, and say which of chapter 2's baselines each copies. Then: "Use your rule on the twelve rows. What does
it say for the week of 20 October 2025, Diwali's week, which shipped 308,900?"

**Round two.** "Thirteen weeks are hidden from everyone, 29 June to 21 September 2026. Every rule
forecasts all thirteen from 22 June. Before the scores: which rule wins?" Take the vote on S51, then
the TA reads each group's score. After S54: "The vendor's curve fits two years within 2 percent. Is
that a good forecast?" Wait for "score it on the weeks it never saw".

**Round three.** Before turning the calendar card, say exactly the question on half two's S3: "Which
week does the bot make 2026's busiest?" Take the vote, then turn the card on S4: the bot's busiest
week is 5 October, a copy of 2025's peak, and the rush comes in the week of 19 October, two weeks
before Diwali's week of 2 November. The first group to place 2026's peak on 19 October wins the plan,
and its line goes first in the afternoon's staffing note. The objections come on half two's S14, in
the staffing note's minutes: the trainer, as finance, and the TA, as the vendor's sponsor, each say
their card's opening line, and one group answers each, 4 minutes in all.

## How does the TA score a group's own rule?

In notebook 06, add one line per group at the bottom of cell 5, after `rules` is built, so that no
cell moves and the numbers below still point at the right cells. Use only the names the notebook
already has (`train`, `last_year`, `h`, `slope`):

```python
rules["group 1"] = (last_year * 1.03).round().astype(int)   # "last year plus 3 percent"
```

Run cells 5 and 7 for the MAE at S51 and S52. After the vendor's reveal on S54, run cell 13 for the
misses priced at S55 and S56; it reads the vendor's numbers itself, and both cells cover every column
of `rules`. Read each group's MAE, then its cost, aloud and write them on the wall. A rule that cannot be written in
one line goes back to its group.

## What does the finished scoreboard read?

| Entrant | MAE, shipments a week | Weeks too high | Misses priced |
|---|---|---|---|
| Festival-aligned | 6,615 | 6 of 13 | Rs 13.5 lakh |
| Finance's rule | 6,615 | 6 of 13 | Rs 13.5 lakh |
| Seasonal naive, the house bot | 9,831 | 2 of 13 | Rs 30.5 lakh |
| Drift | 14,842 | 8 of 13 | Rs 28.0 lakh |
| Naive | 14,923 | 8 of 13 | Rs 28.8 lakh |
| Vendor's curve | 16,400 | 12 of 13 | Rs 11.9 lakh |

Each group's own rule takes its row from the notebook. A rule that copies last year's week and adds
3 to 5 percent lands within a few hundred shipments of the 6,615 row: on festival-free weeks the
simple copies win, and round three settles the festival.

## What do you do when it stalls?

| The stall | The sign | What to say |
|---|---|---|
| A method that is not a rule | "We would use machine learning" | "Write it in one line a planner could run. Until then, the house bot is your entry." |
| Trusting a curve because it fits | A group backs the vendor on its 2 percent | "Score it on the weeks it did not see." The your-turn cell prints 16,400 |
| Hiding random weeks | A group wants a random fifth of the weeks | "What will the plan hold you to?" The latest weeks, at least as far ahead as the plan reaches: ten here |
| Averaging the two forecasts | "13 percent, halfway" | "Both copy the calendar. Where does their average put the peak?" |
| Crowning the cheapest misses | A group sends the vendor because Rs 11.9 lakh is lowest | "Who chose how high it runs, and does it run higher in October?" S57's cards answer it |
| A group finishes early | Its rule is scored and argued | "Price your rule's misses with a late shipment at Rs 40, the top of its range. Does the order change?" |
