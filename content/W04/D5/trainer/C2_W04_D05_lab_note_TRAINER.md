# TA lab note: the forecasting method on Kalpa's 24 months, then the practice set

**TRAINER ONLY.** For the TA who runs the practice lab after the faculty block (tentative). The lab
re-runs levels L1 to L3 on Kalpa Retail's monthly revenue in notebook 04, sits the Kalpa board set,
then works the practice set. The programme's facts set no length for the lab, so the parts below run
in this order and the practice set is cut from its end when time runs short. Never cut the twelve
rows or the two your-turn cells.

## What does the lab ask, and what is the order of work?

Kalpa Retail's growth plan goes to the board and needs revenue for October 2026 to March 2027,
against a plan line 15 percent above the same months a year earlier, with Diwali inside the window.
Finance's forecast is last year plus 4 percent; marketing's vendor curve promises 22 percent. Anand
Iyer, the finance controller: "Two forecasts, eighteen points apart. Which one do I put in front of
the board, and how wrong could it be?"

| Order | Part | File |
|---|---|---|
| 1 | The twelve rows read by hand on paper: which month is each winter's biggest? | The table below, printed one per group |
| 2 | The 24 months loaded and drawn | Notebook 04, cells 2 to 4 |
| 3 | Naive and drift scored on April to September 2026 | Notebook 04, cell 6 |
| 4 | Your turn: the seasonal copy and the vendor scored on the same six months | Notebook 04, cell 8, empty |
| 5 | Your turn: which month each copy puts Diwali in, and the six months summed | Notebook 04, cell 10, empty |
| 6 | The growth and the plan line | Notebook 04, cell 11 |
| 7 | The Kalpa board set, sat after the notebook | `exercises/unguided/C2_W04_D05_kalpa_board_STUDENT.md` |
| 8 | The practice set | `exercises/practice/C2_W04_D05_lab_set_STUDENT.md` |

## What do the twelve rows hold, and what should the hand count give?

Print this table for each group: October to March of both winters, Rs lakh.

| Month | 2024-25 | 2025-26 |
|---|---|---|
| October | 415.1 | 427.6 |
| November | 286.8 | 297.0 |
| December | 295.8 | 310.5 |
| January | 275.9 | 285.1 |
| February | 267.4 | 275.7 |
| March | 284.6 | 297.0 |

The hand count: October is the biggest month of both winters, about 1.4 times November each year,
and every month of the second winter sits a little above the same month of the first. Diwali fell on
31 October 2024 and 20 October 2025, so both spikes are October's. The question to leave on the board:
Diwali falls on 8 November 2026, so which month should carry this winter's spike?

## Which plants should the your-turn cells find, and what do you do if nobody finds one?

The plants stay on this page until a learner's own cell prints them. After that the room may say
them (decision `w4-finding-once-found`), and the Kalpa board set prints what the lab found.

| Plant | What the full data says | If nobody finds it |
|---|---|---|
| Two October spikes | October 2024 is 1.45 times November 2024, its one neighbour in the data; October 2025 is 1.56 times the mean of September and November 2025 | Ask "which month is each winter's biggest, and by how much over its neighbours?" |
| A growing business | The twelve months to September 2025 sit 3.5 percent below the twelve to September 2026 (Rs 37.40 crore against Rs 38.77 crore) | Point at cell 11's printed growth, 3.7 percent on the first year |
| A fit that is no forecast | The vendor fits its 18 fitted months within 1.8 percent, yet on April to September 2026 it misses by Rs 38.8 lakh a month against the seasonal copy's Rs 11.7 lakh; naive and drift miss by Rs 59.4 and Rs 58.8 lakh | Ask "which rows of the vendor's file are fits, and which are its hold-out forecasts?", then point at the `kind` column, which reads `holdout` for the six hidden months |
| The vendor's 22 percent | Its October 2026 to March 2027 total is Rs 23.09 crore, 22 percent above the same months a year earlier (Rs 18.93 crore); finance's is Rs 19.69 crore, 4 percent above | Ask "sum each column of your table: how far apart are the totals?" |
| The month-aligned trap | The copy of the same month a year earlier puts the spike in October 2026, while Diwali falls on 8 November 2026; the festival-aligned copy moves it to November, Rs 444.7 lakh | Ask "which month is Diwali in this year, and which month did your copy put the spike in?" |

The plan line sums to Rs 21.77 crore, 15 percent above the year before and Rs 2.08 crore (10.6
percent) above festival-aligned. The three lines a group brings back: the board number, Rs 19.69
crore from festival-aligned with the spike in November; its error bar, festival-aligned's own miss on
the six hidden months, Rs 3.5 lakh a month, about Rs 21 lakh if all six miss the same way, which
notebook 04's last code cell prints, with the spike month itself untested; and the gap to the plan
line, Rs 2.08 crore. A group that offers the seasonal copy's Rs 11.7 lakh is asked which forecast
that miss belongs to: the copy without the 4 percent.

## Where do learners stall, and which hint unlocks each place?

| Where | The stall | The one hint |
|---|---|---|
| Which months to hide | Hiding the first six months, or a random six | "What will the plan hold you to?" The last months, as many as the horizon: six here |
| The seasonal copy | Typing `shift(52)` from the morning on monthly data | "How many rows back is the same month last year in this table?" Twelve |
| The vendor's file | Scoring its fitted rows and finding it nearly perfect | "Which rows did the vendor see when it made its forecast?" |
| The festival-aligned copy | Moving every month, or none | "Which two months swap places when Diwali moves from October to November?" |
| Reading the totals | Calling the vendor's Rs 23.09 crore "22 percent growth" | "22 percent above which months, and on what record of months it never saw?" |

## Where do learners stall in the practice set, and which hint unlocks each item?

The practice set's keys are 1b, 2c, 3a, 4d, 5a and 6d. Item 5 is the Parsons problem: the house bot's
scoring cell, `shift(52)` included, arrives scrambled.

| Item | Where learners stall | The one hint |
|---|---|---|
| Q1, three series | Calling Z's wobble a trend | "Does Z climb, or only wobble around the same height?" |
| Q2, the gift shop | Copying the same calendar week, 35 | "Which week of last year sat at the same distance after its festival?" |
| Q3, five misses | Averaging the signed misses to 0 | "Does a miss of 8 too low cancel a miss of 12 too high on the packing floor?" |
| Q4, the vendor's pitch | Asking how the model works first | "Which weeks would you score it on?" |
| Q5, the scrambled cell | Scoring before the hidden weeks exist | "Which line uses a name no earlier line has made?" |
| Q6, the plan share | Dividing the cheap cost by the sum, 0.14 | "Which side of the forecast do you want to be on more often?" |

## What do you send the trainer after the lab?

One line per group, sent to the trainer before Saturday's session: the board number it would send,
its error bar, and the month it puts the spike in. A group that found no plant is named, so
Saturday's discussion can start there.
