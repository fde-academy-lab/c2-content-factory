# Run sheet: the forecast tournament with a house bot

**TRAINER ONLY.** This sheet runs the day's signature activity. The entrants are finance's rule (last
year's same weeks plus 4 percent), the vendor's curve and every group's own one-line rule. The house
bot, a copy of the same week last year, is the bar: nothing goes to the staffing plan unless it beats
the bot on the same thirteen hidden weeks, by the same measure, fixed before anyone scores. In round
three the bot itself turns out to be wrong about which week Diwali falls in, and the group that
notices first wins the plan. A trainer who did not write the day can run it from this page alone.

## Who plays which role?

| Role | Who | What they do |
|---|---|---|
| Referee and scorekeeper | The day's trainer | Fixes the rule at the start, keeps the wall scoreboard, says the lines below, plays finance in round three |
| Second scorer | The day's TA | Types each group's rule into notebook 02 and reads its score aloud, plays the vendor's sponsor in round three |
| Entrants | Groups of about four learners | Write one rule in one line, defend it, and vote before each reveal |

## What must be printed or set up before the room sits down?

| Material | File | How many |
|---|---|---|
| The twelve rows | `data/C2_W04_D05_twelve_rows_STUDENT.csv`, printed as a table, or `whiteboards/C2_W04_D05_twelve_rows_STUDENT.png` | One per group |
| The wall scoreboard | Drawn on the board: one row per entrant; columns for the rule in one line, MAE in shipments, weeks too high of 13, the misses priced in Rs lakh | One, on the wall all day |
| Finance's and the vendor's sponsor's role cards | `trainer/C2_W04_D05_role_cards_TRAINER.md` | One copy each, for the trainer and the TA |
| The festival calendar card | `trainer/C2_W04_D05_festival_calendar_card_TRAINER.md`, printed large | One, face down until S29 |
| Sticky notes in two colours | | A pad per group, for the votes on S5, S9, S18, S20, S22 and S28 |

## How do the minutes run?

| Turn | Minutes | Slides | What the room does |
|---|---|---|---|
| The rule | 10 | Cover to S3 | Hears the two forecasts, says what would make each wrong, hears the rule, names its group's entrant |
| Round one | 40 | S4 to S14 | Reads the twelve rows by hand, writes its own rule in one line, forecasts Diwali 2025's week with every rule |
| Round two | 45 | S15 to S26 | Votes on the scoreboard, watches its rule scored on the hidden weeks, prices the misses |
| Break | 10 | | The scoreboard stays up |
| Round three | 75 | S27 to S36 | Votes on the bot's busiest week, turns the calendar card, back-tests 2025, hears the objections, sets the plan |

## What does the trainer say at each turn?

**The rule, said word for word before anyone scores.** "The error measure is fixed now, before
anyone scores: mean absolute error in shipments on the thirteen held-out weeks, then the same errors
priced. Nothing goes to the plan unless it beats the house bot on those weeks."

**Round one.** "Each group writes one rule, in one line, that a planner could run on a spreadsheet:
what does it copy, and what does it add?" Collect the rules on the board before S8 shows the four
rules, so the room sees whose rule matches which. Then: "Use your rule on the twelve rows. What does
it say for the week of 20 October 2025, Diwali's week, which shipped 308,900?"

**Round two.** "Thirteen weeks are hidden from everyone, 29 June to 21 September 2026. Every rule
forecasts all thirteen from 22 June. Before the scores: which rule wins?" Take the vote on S18, then
the TA reads each group's score. After S21: "The vendor's curve fits two years within 2 percent. Is
that a good forecast?" Wait for "score it on the weeks it never saw".

**Round three.** Before turning the calendar card, say exactly: "Which week does the bot put Diwali in
this year?" Take the vote on S28, then turn the card on S29. The first group to place 2026's peak in
the week of 19 October, two weeks before Diwali's week of 2 November, wins the plan, and its line
goes first in the afternoon's staffing note. Then the trainer, as finance, and the TA, as the
vendor's sponsor, object from the role cards, and each group answers one of them.

## How does the TA score a group's own rule?

In notebook 02, after cell 6 has built `rules`, add one line per group in a new cell, using only the
names the notebook already has (`train`, `last_year`, `h`, `slope`):

```python
rules["group 1"] = (last_year * 1.03).round().astype(int)   # "last year plus 3 percent"
```

Then run cell 8 for the MAE and cell 14 for the misses priced; both cover every column of `rules`.
Read each group's MAE and cost aloud and write them on the wall. A rule that cannot be written in
one line goes back to its group.

## What does the finished scoreboard read?

| Entrant | MAE, shipments a week | Weeks too high | Misses priced |
|---|---|---|---|
| Festival-aligned | 6,615 | 6 of 13 | Rs 13.5 lakh |
| Finance's rule | 6,615 | 6 of 13 | Rs 13.5 lakh |
| House bot | 9,831 | 2 of 13 | Rs 30.5 lakh |
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
| Hiding random weeks | A group wants a random fifth of the weeks | "What will the plan hold you to?" The latest weeks, at least as many as it books |
| Averaging the two forecasts | "13 percent, halfway" | "Both copy the calendar. Where does their average put the peak?" |
| Crowning the cheapest misses | A group sends the vendor because Rs 11.9 lakh is lowest | "Who chose how high it runs, and does it run higher in October?" S24's three cards answer it |
| A group finishes early | Its rule is scored and argued | "Price your rule's misses with a late shipment at Rs 40, the top of its range. Does the order change?" |
