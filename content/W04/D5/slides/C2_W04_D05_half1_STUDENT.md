# Flipkart Lucknow: festive forecasts 18 points apart

Week 4, Day 5. Half one.

Header: WEEK 4  ·  FRIDAY  ·  FLIPKART, LUCKNOW  ·  ILLUSTRATIVE CASE

---

## S1. Two forecasts for one festive window, 18 points apart
*What has the planner been handed, and what is due Friday?*

| On the ticket | What it says |
|---|---|
| Company, city, surface | Flipkart, the Lucknow fulfilment centre: outbound shipments and packer shifts |
| The history | 104 weeks, the weeks beginning Monday 30 September 2024 to Monday 21 September 2026; an ordinary week in late 2024 ships about 210,000 |
| The festival | Diwali fell on Thursday 31 October 2024 and Monday 20 October 2025, and falls on Sunday 8 November 2026; the three weeks before it run at 1.5, 1.9 and 1.7 times an ordinary week, its own week at 1.4, the week after below ordinary |
| The two forecasts | A vendor's model promises the window 22 percent above last year's; finance's rule is last year's window plus 4 percent |
| The data | `weekly_shipments` (week_start, shipments, packer_shifts_worked, overtime_shifts); `vendor_forecast` (week_start, vendor_shipments, kind: fitted, holdout or forecast); `calendar` (week_start, diwali_week, sale_week); `costs` (item, rs, low, high) |
| The costs, assumed | An idle packer-shift Rs 650 (range Rs 500 to 800); a late shipment Rs 25 (range Rs 15 to 40); a packer packs about 120 shipments a shift |
| The ask, due Friday | Which forecast goes to the plan for the eight weeks beginning 12 October to 30 November 2026, how wrong could it be, and how many packer shifts a week |
| Caveats | The festival moves by weeks each year and the sale weeks move with it; two years hold two festivals; a late shipment costs more than an idle shift; peak weeks are capped by the centre's own capacity |

Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

```notes
LIVE, 5 minutes, on screen as the room sits down. Read the title, then the table top to bottom, then
the label line. Today is a tournament in three rounds: count by hand, score on hidden weeks, then
place the festival and price the plan. Define two words as they appear: a packer-shift is
one packer working one shift, and a forecast is a number for a week nobody has seen yet. Point at
the four tables and their columns; every number today comes from them. Ask the room what would
make each forecast wrong, and write the answers on the board without judging them. Transition:
where today sits in the week.
```

---

## S2. Friday asks how much is coming, and how wrong
*Where does today's ticket sit among the week's five?*

```mermaid
flowchart LR
    C["<b>One number,</b><br/>five tickets"]
    M["<b>Mon · Uber</b><br/>1.9 to 1.6 trips an hour"]
    T["<b>Tue · Uber</b><br/>Rs 314 to Rs 260 an hour"]
    W["<b>Wed · Instamart</b><br/>6.1 to 3.8 percent"]
    H["<b>Thu · Zomato Gold</b><br/>58 to 44 percent"]
    F["<b>Fri · Flipkart</b><br/>how much, how wrong?"]
    S["<b>Sat</b><br/>a new company"]
    K["<b>Kalpa lab</b><br/>24 months"]
    C --> M
    C --> W
    C --> H
    C --> F
    M -.- T
    F --> K
    T --> S
    K --> S
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class C,M,T,W,H known
    class F lit
    class S unknown
    class K kalpa
```

```notes
LIVE, 2 minutes. Read the earlier nodes with their numbers: each was a number the room produced
on its day. Monday's guardrails bound what a forecast may chase, Thursday's cohorts gave the
week a time axis, and today asks what the plan will be held to. The Kalpa node is the lab after
class. Explorer: the home screen, Friday lit. Transition: where today ends.
```

---

## S3. Where today ends: 20,275 shifts, a bar in rupees
*What will the planner carry out of the room?*

```cards
icon: badge-check | eyebrow: The plan | title: 20,275 packer shifts | body: Over the eight weeks, peaking at 3,719 in the week of 19 October, from a forecast that keeps each week's distance from Diwali. | tone: dark
icon: ruler | eyebrow: The error bar | title: 6,615 shipments a week | body: Its miss on thirteen weeks it never saw: Rs 35,832 of idle shifts if high, Rs 1.7 lakh of late shipments if low. | tone: light
icon: scale | eyebrow: The two forecasts | title: Neither carries the plan | body: The vendor loses to a copy of last year on hidden weeks; finance's rule puts the peak two weeks early. | tone: light
```

**The tournament's rule.** Nothing goes to the plan unless it beats the house bot, a copy of the same week last year, on the same thirteen hidden weeks, by the same measure: the average miss in shipments, then priced in rupees.

```notes
LIVE, 3 minutes. Show the finished answer once, then earn it. The rule is fixed now, before anyone
scores: mean absolute error in shipments on the thirteen held-out weeks, then the same misses
priced. Groups enter their own hand rule in round one. Transition: chapter 1, counting by hand.
```

---

## SECTION 1: What shape do the weeks have?
*What shape do the 104 weeks have, and what would three simple rules say for one week before any code opens?*

```notes
LIVE, 1 minute. Chapter 1 of 3, level L1, round one of the tournament. Twelve printed weeks per
table; no laptop opens in this chapter. Transition: the questions.
```

---

## S4. Four questions, climbed by hand
*Who needs the answer, and which questions lead to it?*

**Who needs the answer.** The FC planner, who books shifts weeks ahead and cannot add one on the day: a rule that puts the busiest week in the wrong place books packers for a quiet week.

```timeline
label: Shape | title: Where is the peak? | body: Which week of the season ships the most, in each year?
label: Rules | title: What do rules copy? | body: Naive, same week last year, drift and festival-aligned, each in one line.
label: One week | title: Which lands closest? | body: Three rules for Diwali 2025's own week.
label: The trap | title: Which week moves? | body: Where a copy of last year puts the peak. | tone: dark
```

```notes
LIVE, 2 minutes. Read the four questions. Each gets a number before the next is asked.
Transition: the first question, voted before anything is shown.
```

---

## S5. Which week of the festive season ships most?
*Two festivals, six weeks each: where does the peak sit, before you see a bar?*

```cards
icon: calendar | eyebrow: a | title: Diwali's own week | body: The festival is the moment people shop. | tone: light
icon: calendar | eyebrow: b | title: The week before Diwali's week | body: The last full week before the festival. | tone: light
icon: calendar | eyebrow: c | title: Two weeks before Diwali's week | body: Early enough for parcels to arrive. | tone: light
icon: calendar | eyebrow: d | title: The week after Diwali's week | body: Gifts bought late, shipped late. | tone: light
```

```notes
LIVE, 3 minutes. Each group holds up a letter. Two minutes for neighbours to argue, then vote again.
Keep both counts on the board. Transition: the twelve weeks.
```

---

## S6. Answer: two weeks before Diwali, in both years
*What did the twelve weeks around two Diwalis ship?*

![Twelve weeks around two Diwalis, Diwali's own week in red](../whiteboards/C2_W04_D05_twelve_rows_STUDENT.png)

The busiest week is two weeks before Diwali's week both times: 401,000 shipments in the week of 14 October 2024 and 418,200 in the week of 6 October 2025. Diwali's own week ships 296,900 and 308,900, and the week after is the lowest.

```notes
LIVE, 5 minutes. Count aloud left to right, StatQuest style. Parcels leave the centre before the
festival so they arrive in time, which is why the peak comes early. If most of the room voted a,
ask what a customer does on Diwali itself. Transition: what a weekly series is made of.
```

---

## S7. A weekly series carries four shapes at once
*What do you read off a series before any rule is chosen?*

![Four shapes on invented numbers: trend, season, cycle and noise](../whiteboards/C2_W04_D05_four_patterns_STUDENT.png)

Read them in this order: the slow climb (trend), the yearly peak (season), the repeat inside a month (here, payday weeks) and what is left over (noise). A planner books against the first three and buys a cushion for the fourth. The numbers are invented so each shape stands alone.

```notes
LIVE, 3 minutes. 3Blue1Brown's move: the picture first, the names after. The real series has all
four: a growth of about 4 percent a year, the festival, the week holding the 1st of a month and a
wobble of a few percent. Explorer: scene F1, the season slider. Transition: four rules.
```

---

## S8. Four rules, each a single line of copying
*What does each simple forecasting rule copy from the past?*

| Rule | What it copies | On a canteen's tea (invented) |
|---|---|---|
| Naive | The last value | 50, 52, 49 and 51 cups on four days, so tomorrow is 51 |
| Same week last year | The same point one cycle back, here 52 weeks | Sundays sell about 80, so next Sunday is 80 |
| Drift | The straight line through the first and last values | The average change added on |
| Festival-aligned | The week at the same distance from last year's Diwali, plus the year's growth | No canteen version: it exists because the festival moves |

```notes
LIVE, 4 minutes. Read each rule as one sentence a shift supervisor could repeat. Same week last
year is the house bot of the tournament. Festival-aligned adds the 4 percent a year the centre
grew. Transition: the three rules on one real week.
```

---

## S9. Which rule lands closest on Diwali 2025's week?
*From the week of 13 October 2025, which rule best forecasts the week of 20 October?*

```cards
icon: list | eyebrow: a | title: Naive | body: Repeat the week of 13 October 2025. | tone: light
icon: list | eyebrow: b | title: Same week last year | body: Copy the week of 21 October 2024, 52 weeks back. | tone: light
icon: list | eyebrow: c | title: Festival-aligned | body: Copy Diwali 2024's own week, 28 October, and add 4 percent. | tone: light
icon: list | eyebrow: d | title: All three within 10,000 | body: One week ahead, every rule is close. | tone: light
```

```notes
LIVE, 3 minutes. Groups work each rule on the twelve printed rows before voting. The actual that
week was 308,900; do not show it until the vote. Transition: the answer.
```

---

## S10. Answer: festival-aligned, within 124 shipments
*What did each rule forecast for the week of 20 October 2025, and by how much did it miss?*

| Rule | The week it copies | Forecast | Miss |
|---|---|---|---|
| Naive | 13 October 2025 | 369,000 | 60,100 too high |
| Same week last year | 21 October 2024 | 356,200 | 47,300 too high |
| Festival-aligned | 28 October 2024, plus 4 percent | 308,776 | 124 too low |

308,900 shipped. The week 52 weeks back looks like "the same week", but in 2024 it was the week before Diwali, and the week before Diwali ships more than Diwali's own week.

```notes
LIVE, 4 minutes. Do the festival-aligned arithmetic aloud: 296,900 times 1.04 is 308,776. Ask
which group's own rule came closest. Transition: the trap hidden in the copy.
```

---

## S11. The copy of last year lands 2025's peak late
*Where does a same-week-last-year copy put the peak when Diwali moves?*

![Two years by date and by weeks from Diwali](../whiteboards/C2_W04_D05_festival_plot_STUDENT.png)

**The plausible wrong number.** The copy books 401,000 for the week of 13 October 2025, its biggest week, while 369,000 shipped; the real peak, 418,200 on 6 October, gets 312,900. **The decision it misleads:** the most packers booked a week after the rush. **The check:** line the years up by weeks from Diwali, as on the right. **The fix:** festival-aligned.

```notes
LIVE, 5 minutes. Diwali's week came one week earlier in 2025, so every calendar copy is a week out.
Veritasium's move: the reveal follows the vote of S9. Transition: where Diwali falls in 2026.
```

---

## S12. In 2026 Diwali's week moves two weeks later
*Where does Diwali fall in 2026, against the two years the rules copy?*

![Diwali's week in 2024, 2025 and 2026](../whiteboards/C2_W04_D05_festival_calendar_open_STUDENT.png)

Diwali 2026 falls on Sunday 8 November, so its week begins 2 November, 54 weeks after Diwali 2025's week and two weeks later in the calendar. Hold one question for round three: where will a copy of last year put this year's rush?

```notes
LIVE, 3 minutes. Count the Mondays on the strip with the room. Do not answer where the copy lands:
round three asks it on S28, and the festival calendar card answers it on S29. Explorer: scene F3,
the Diwali slider. Transition: the real company.
```

---

## S13. Flipkart books its festive capacity weeks ahead
*Which real decisions does a festive forecast feed?*

| | |
|---|---|
| What Flipkart said (6 October 2026) | Ekart added 14 million cubic feet of warehousing space ahead of The Big Billion Days, and more than 2.5 lakh direct and indirect jobs were created for the festive season (F6, checked 12 October 2026) |
| When it was decided | Before the sale opened on 9 October 2026, so the space and the people rested on a forecast made weeks earlier |
| What a senior analyst checks | Whether the forecast behind the booking beat a simple copy of last year, and whether it put the festival in the right week |

```notes
LIVE, 2 minutes. These are Flipkart's own published numbers; everything else today is this class's
synthetic data. Read them as decisions already in motion. Transition: chapter 1's answers.
```

---

## S14. Chapter 1: the peak sits two weeks before Diwali
*What did counting twelve weeks by hand settle, and what does it leave open?*

```mermaid
flowchart LR
    A["<b>The shape</b><br/>peak two weeks<br/>before Diwali"] --> B["<b>Four rules</b><br/>one line each"]
    B --> C["<b>One week</b><br/>aligned copy<br/>misses by 124"]
    C --> D["<b>Hidden weeks</b><br/>which rule<br/>wins?"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class A,B,C known
    class D unknown
```

One week cannot crown a rule. **Say it to a shift supervisor:** the computer copied last year's dates, and the festival moved, so its busiest week came at the wrong time. On Walmart's M5 data the same-period copy scored 0.847 against 1.752 for the naive, lower being better (F2, checked 12 October 2026).

```notes
LIVE, 2 minutes. Read the map left to right; the dashed box is chapter 2. Transition: chapter 2,
the hold-out.
```

---

## SECTION 2: Which rule wins on hidden weeks?
*How does each rule score on the thirteen weeks it never saw, which way is each wrong, and what does each direction cost?*

```notes
LIVE, 1 minute. Chapter 2 of 3, levels L2 and L3, round two of the tournament. Notebook 02 runs
alongside. Transition: the questions.
```

---

## S15. Five questions before the scoreboard
*Who needs the score, and which questions lead to it?*

**Who needs the answer.** The regional operations head, who must say yes or no to the vendor's plus 22 percent before a single shift is booked.

```timeline
label: Hide | title: Which weeks? | body: The last thirteen, forecast from one week.
label: Count | title: How is a miss counted? | body: The average miss in shipments.
label: Score | title: Which rule wins? | body: Four rules on the hidden weeks.
label: Fit | title: What does a fit say? | body: The vendor on weeks it never saw.
label: Price | title: What do misses cost? | body: Rs 25 short, Rs 5.42 spare. | tone: dark
```

```notes
LIVE, 1 minute. Read the five questions. Transition: the weeks we hide.
```

---

## S16. Hide the last thirteen weeks, forecast from 22 June
*Which weeks does the test hide, and from which week is every forecast made?*

![104 weeks with the hold-out shaded](../whiteboards/C2_W04_D05_actual_series_STUDENT.png)

The plan covers eight weeks, so the test hides more: the thirteen weeks from 29 June to 21 September 2026. Every rule forecasts all thirteen from the week of 22 June, as a planner standing there would have. Forecasting: Principles and Practice puts it this way: the test set should be at least as large as the forecast horizon (FPP3, section 5.8, checked 12 October 2026).

```notes
LIVE, 4 minutes. The 91 weeks before are the training weeks. Point at the August sale inside the
hidden weeks: a copy of last year knows about it, naive does not. Explorer: scene F2, the split
slider. Transition: how a miss is counted.
```

---

## S17. MAE: the average miss, counted in shipments
*How is one number made from thirteen misses, and why shipments?*

```stats
value: 8.3 | label: MAE on three invented weeks | note: misses of 10, 5 and 10 shipments, one of them too low: (10 + 5 + 10) / 3
value: shipments | label: the unit | note: a miss is priced per shipment, so the score stays in shipments
value: fixed first | label: the rule | note: the measure is chosen before anyone sees a score
```

Mean absolute error drops each miss's sign and averages. A percentage error would hide the size of a miss: the same percent is twice the shipments in a peak week. The sign comes back on S22.

```notes
LIVE, 3 minutes. Work the toy aloud. Mention MAPE as the percent version and why the plan does not
use it: the costs are per shipment. Transition: the vote.
```

---

## S18. Which rule scores lowest on hidden weeks?
*Before the scoreboard runs, which rule misses least on thirteen weeks it never saw?*

```cards
icon: list | eyebrow: a | title: Naive | body: Repeat the week of 22 June. | tone: light
icon: list | eyebrow: b | title: Drift | body: The line from the first week through 22 June. | tone: light
icon: list | eyebrow: c | title: The house bot | body: Copy the same week of 2025. | tone: light
icon: list | eyebrow: d | title: Festival-aligned | body: The bot plus 4 percent here, tied with finance's rule. | tone: light
```

```notes
LIVE, 3 minutes. Brilliant's move: the room answers before the scoreboard. Note the tie in d is
announced, not hidden: the next slide says why. Transition: the answer.
```

---

## S19. Answer: festival-aligned and finance tie, 6,615
*How did each rule score on the thirteen hidden weeks?*

![Each rule against the actual on the hidden weeks, with its MAE](../whiteboards/C2_W04_D05_baselines_panel_STUDENT.png)

Festival-aligned and finance's rule miss by 6,615 shipments a week, the house bot by 9,831, drift by 14,842 and naive by 14,923. The tie is honest: no hidden week lies within five weeks of a Diwali, so both rules copy the same week of 2025 and add the same 4 percent. They part only in the festive weeks, which this test does not hold.

```notes
LIVE, 5 minutes. Tufte's small multiples: one rule per panel on the same axes. The bot beats naive
because it carries the August sale; it loses to the 4 percent rules because a growing series
makes last year too low. Transition: the vendor.
```

---

## S20. Does a curve that fits history beat the bot?
*The vendor's curve sits within 2 percent of every week it was fitted to. Will it beat the house bot on the hidden weeks?*

```cards
icon: list | eyebrow: a | title: Yes, by a wide margin | body: A model that close to history has learned the series. | tone: light
icon: list | eyebrow: b | title: Yes, narrowly | body: It knows the season the bot copies. | tone: light
icon: list | eyebrow: c | title: No, it loses to the bot | body: A fit is drawn through weeks it has seen. | tone: light
icon: list | eyebrow: d | title: It ties festival-aligned | body: Both end near 6,615. | tone: light
```

```notes
LIVE, 3 minutes. In notebook 02 every learner scores the vendor in an empty cell first; vote after
the cell runs, before this slide's answer. Transition: the answer.
```

---

## S21. Answer: no, it misses by 16,400 a week
*What does the vendor's fit say about its forecast?*

![The vendor's misses: fitted weeks within 2 percent, hidden weeks too high](../whiteboards/C2_W04_D05_fit_vs_forecast_STUDENT.png)

**The plausible wrong number:** "within 1.4 percent of every week, so its plus 22 can be trusted." **The decision it misleads:** a plan 22 percent above last year. **The check:** its error on weeks it never saw, 16,400 a week, 67 percent worse than the house bot. **The fix:** nothing goes to the plan unless it beats the bot there.

```notes
LIVE, 5 minutes. Read the left of the chart, then the right. A fit is drawn through weeks the model
has seen; a forecast is made for weeks it has not. Transition: which way each rule is wrong.
```

---

## S22. Whose misses cost least, once priced?
*A late shipment costs Rs 25 and a spare one Rs 5.42. Whose thirteen misses cost the least?*

```cards
icon: list | eyebrow: a | title: Festival-aligned | body: The lowest MAE, 6,615. | tone: light
icon: list | eyebrow: b | title: The vendor | body: The highest MAE, 16,400. | tone: light
icon: list | eyebrow: c | title: The house bot | body: MAE 9,831. | tone: light
icon: list | eyebrow: d | title: Naive | body: MAE 14,923. | tone: light
```

```notes
LIVE, 3 minutes. The idle cost is Rs 650 / 120 = Rs 5.42 for each shipment of spare capacity.
Ask which way each rule's misses run before anyone votes. Transition: the answer.
```

---

## S23. Answer: the vendor's, at Rs 11.9 lakh
*What do the same misses cost in rupees, and why does the order change?*

![MAE beside the same misses priced in rupees](../whiteboards/C2_W04_D05_scoreboard_STUDENT.png)

The vendor errs high on 12 of 13 weeks, and spare capacity is the cheap kind of miss: Rs 11.9 lakh against Rs 13.5 lakh for festival-aligned. The house bot errs low on 11 of 13 weeks and costs Rs 30.5 lakh, more than naive's Rs 28.8 lakh, with a lower MAE. Priced, a forecast that errs high can cost less than one that misses less.

```notes
LIVE, 4 minutes. Let the result stand; it is true of this data. The room should leave with the
reason: being short costs 4.6 times being long. Transition: why the vendor still does not win.
```

---

## S24. Cheap misses do not win the vendor the plan
*If its misses cost least, why does the vendor's curve still lose the plan?*

```cards
icon: ruler | eyebrow: Unsized | title: Its lean was never chosen | body: Nobody set how high it runs, so nobody knows how high it will run in October. | tone: light
icon: trending-up | eyebrow: Growing | title: It climbs with the weeks ahead | body: 3.6 percent too high in the first six hidden weeks, 11.5 percent in the last six. | tone: light
icon: calendar-x | eyebrow: Untested | title: No festival in the test | body: In the festive weeks it copies 2025's calendar, the wrong weeks. | tone: light
icon: badge-check | eyebrow: The fix | title: Lean high on purpose | body: Raise festival-aligned by an amount the two costs set, which chapter 3 sizes. | tone: dark
```

```notes
LIVE, 3 minutes. The plan's case rests on two things this hold-out cannot test: the festival's
placement and the size of the cushion. Chapter 3 tests the first on 2025's festival and sizes the
second from the costs. Transition: the same score a second way.
```

---

## S25. Second route: 85,996 missed, over 13 weeks
*Does the scoreboard's 6,615 survive a count by hand from the printed misses?*

```stats
value: 40,748 | label: shipments too high | note: festival-aligned above the actual, summed over its 6 high weeks
value: 45,248 | label: shipments too low | note: below the actual, summed over the other 7
value: 6,615 | label: per week | note: (40,748 + 45,248) / 13 = 85,996 / 13
```

The same 6,615 from a table anyone can add up. The split also says the forecast leans neither way here: 6 weeks high, 7 low.

```notes
LIVE, 2 minutes. Notebook 02 prints the thirteen misses; the last cell adds them. Transition:
chapter 2's answers.
```

---

## S26. Chapter 2: fit is not forecast; price the miss
*What did the hidden weeks settle, and what can they not test?*

```mermaid
flowchart LR
    A["<b>Hidden weeks</b><br/>13, from<br/>22 June"] --> B["<b>Score</b><br/>aligned 6,615<br/>bot 9,831<br/>vendor 16,400"]
    B --> C["<b>Price</b><br/>vendor:<br/>Rs 11.9 lakh<br/>bot:<br/>Rs 30.5 lakh"]
    C --> D["<b>Festival weeks</b><br/>not in<br/>the test"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class A,B,C known
    class D unknown
```

On 1,045 monthly series, the methods that best fitted the past did not necessarily forecast better, and a seasonal copy beat half the machine-learning methods (Makridakis and others, PLOS ONE, 2018, F1, checked 12 October 2026). **Say it in one line:** score on weeks the model never saw, in the unit you pay in, against a copy of last year.

```notes
LIVE, 2 minutes. Ten minutes' break follows. Transition: chapter 3, the festival.
```

---

## SECTION 3: Which forecast books the shifts?
*Which forecast goes to the plan, how many packer shifts a week, and what does being wrong cost in each direction?*

```notes
LIVE, 1 minute. Chapter 3 of 3, levels L3 to L5, round three of the tournament. Notebook 03 runs
alongside. Transition: the questions.
```

---

## S27. Five questions between the scores and a plan
*Who needs the plan, and which questions lead to it?*

**Who needs the answer.** The regional operations head, who answers for late parcels in the festival's busiest weeks: a plan with the peak in the wrong week pays for idle packers and late shipments in the same month.

```timeline
label: Place | title: Where is this year's peak? | body: Which week each forecast makes the busiest.
label: Evidence | title: Did placement matter before? | body: 2025's festival, forecast a month ahead.
label: Windows | title: Plus what, against what? | body: The 22 and the 4 against two windows.
label: Level | title: How far above? | body: The cushion two costs justify.
label: Plan | title: How many shifts? | body: Eight weeks, priced. | tone: dark
```

```notes
LIVE, 1 minute. Read the five questions. Transition: round three's reveal.
```

---

## S28. Which week does the bot make 2026's busiest?
*Copying 2025 week for week, which week of 2026 does the house bot book the most packers for?*

```cards
icon: calendar | eyebrow: a | title: 5 October 2026 | body: The week 2025's peak lands on, copied 52 weeks on. | tone: light
icon: calendar | eyebrow: b | title: 19 October 2026 | body: Two weeks before Diwali's week. | tone: light
icon: calendar | eyebrow: c | title: 26 October 2026 | body: One week before Diwali's week. | tone: light
icon: calendar | eyebrow: d | title: 2 November 2026 | body: Diwali's own week. | tone: light
```

```notes
LIVE, 3 minutes. Round three's twist: the house bot itself is wrong about which week Diwali falls
in, and the group that notices wins the plan. Vote, argue, vote again. Explorer: scene F3.
Transition: the answer.
```

---

## S29. Answer: 5 October, two weeks before the peak
*Where does each forecast put this year's busiest week?*

![Four forecasts for 28 September to 30 November 2026](../whiteboards/C2_W04_D05_window_2026_STUDENT.png)

The house bot, finance's rule and the vendor all book their biggest week on 5 October (418,200, 434,928 and 497,900), because each copies 2025's calendar weeks. Festival-aligned books it on 19 October at 434,928, two weeks before Diwali's week of 2 November: finance's number, in the right week.

```notes
LIVE, 5 minutes. Point at finance's 5 October and festival-aligned's 19 October: the same 418,200
times 1.04, two weeks apart. The vendor's model never knew the festival moved. Transition: did
the placement matter last year?
```

---

## S30. On 2025's festival the bot was a week late
*Forecast from 22 September 2025, how did the copy of 2024 do on 2025's festival?*

![2025's festival against the copy of 2024 and the festival-aligned copy](../whiteboards/C2_W04_D05_backtest_2025_STUDENT.png)

The house bot missed 2025's eight festive weeks by 58,250 a week: Rs 79.8 lakh, Rs 69.6 lakh of it late shipments in the weeks the rush came early. Festival-aligned missed by 4,034 a week, Rs 4.6 lakh. One festival is thin evidence, so it settles placement and leaves the size of the error open.

```notes
LIVE, 5 minutes. This back-test is the only festival the data can test the rules on. The vendor
has no festive forecast to score, only its fit. Transition: what plus 22 and plus 4 measure.
```

---

## S31. Plus 22 and plus 4 measure different windows
*How does each forecast compare with last year's eight weeks, counted two ways?*

| 12 Oct to 30 Nov 2026 | Eight weeks | Against 13 Oct to 1 Dec 2025 | Against 29 Sep to 17 Nov 2025 |
|---|---|---|---|
| House bot | 1,983,300 | level | 13.0 percent below |
| Finance's rule | 2,062,632 | 4.0 percent above | 9.5 percent below |
| Vendor | 2,419,500 | 22.0 percent above | 6.1 percent above |
| Festival-aligned | 2,370,680 | 19.5 percent above | 4.0 percent above |

Last year's same calendar weeks shipped 1,983,300; the same weeks counted from Diwali shipped 2,279,500. Finance's plus 4 is plus 4 only on the calendar weeks: it sits 308,048 shipments below festival-aligned, on the costly side. The vendor's plus 22 sits 2.1 percent above festival-aligned, with its peak on the wrong week.

```notes
LIVE, 6 minutes. The calendar window holds only the tail of 2025's festival, because 2025's peak
came before 13 October; 2026's peak falls inside the window. That is why an honest forecast reads
plus 19.5 against it. Transition: how far above the forecast to plan.
```

---

## S32. Being short costs 4.6 times being long
*How far above the forecast should the plan sit, and why above?*

![Expected cost of a week's plan against its level](../whiteboards/C2_W04_D05_cost_curve_STUDENT.png)

A shipment of spare capacity costs Rs 650 / 120 = Rs 5.42; a shipment short costs Rs 25. The cheapest plan covers demand in 25 / (25 + 5.42), about 0.82, of weeks. Festival-aligned's hidden-week misses put that at 2.6 percent above the forecast: demand beat the forecast by more in 18 percent of the hidden weeks.

```notes
LIVE, 6 minutes. Read the two cost curves, then the total; its lowest point sits right of zero.
If the late cost rises toward Rs 40, the line moves further right. Explorer: scene F4.
Transition: the plan in shifts.
```

---

## S33. The plan: 20,275 packer shifts in eight weeks
*How many packer shifts does each week need, and how wrong could the plan be?*

| Week of | Forecast | Plan, plus 2.6 percent | Packer shifts |
|---|---|---|---|
| 12 Oct | 344,448 | 353,404 | 2,946 |
| 19 Oct | 434,928 | 446,236 | 3,719 |
| 26 Oct | 383,760 | 393,738 | 3,282 |
| 2 Nov | 321,256 | 329,609 | 2,747 |
| 9 Nov | 196,144 | 201,244 | 1,678 |
| 16 Nov | 237,016 | 243,178 | 2,027 |
| 23 Nov | 225,992 | 231,868 | 1,933 |
| 30 Nov | 227,136 | 233,042 | 1,943 |

Shifts are the plan over 120, rounded up: 20,275 in all. **The error bar:** 6,615 shipments a week on the hidden weeks, Rs 35,832 of idle shifts if high or Rs 1.7 lakh of late shipments if low; 4,034 a week on 2025's festival.

```notes
LIVE, 6 minutes. Walk the first two rows aloud: 344,448 times 1.026 is 353,404, over 120 and rounded
up is 2,946 shifts. A packer-shift is one packer for one shift; how shifts become people depends on the roster,
which the ticket does not give. Transition: what the other plans would cost.
```

---

## S34. Every other plan costs at least Rs 82.2 lakh
*If demand follows the festival-aligned forecast, what does each other plan cost?*

| Plan for the eight weeks | Spare shipments | Shipments short | Cost |
|---|---|---|---|
| House bot | 48,672 | 436,052 | Rs 111.6 lakh |
| Finance's rule | 87,360 | 395,408 | Rs 103.6 lakh |
| Vendor | 310,364 | 261,544 | Rs 82.2 lakh |
| The plan, festival-aligned plus 2.6 percent | 61,639 | 0 | Rs 3.3 lakh |

A scenario, never a measurement: each plan is priced against festival-aligned's weeks. The cushion's Rs 3.3 lakh is what the insurance costs if demand lands exactly on the forecast.

```notes
LIVE, 4 minutes. The bot's and finance's costs are mostly late shipments in the weeks of 19
October to 2 November. Transition: what the data cannot tell us.
```

---

## S35. What two years of weeks cannot tell us
*Which doubts sit on the plan, and which fact would settle each?*

| The doubt | What would settle it |
|---|---|
| The festival moves, and the sale moves with it | Tested on one festival only: the 2025 back-test |
| Two years hold two festivals | Only a third year; no check inside the data closes it |
| The hidden weeks hold no festive week | The 2025 festival's 4,034 a week, one festival |
| Capacity caps the peak | Overtime reached 1,638 shifts in the week of 6 October 2025 against 5 in an ordinary week, so peak demand may have run above what shipped |
| Growth of 4 percent a year | Two years' evidence; a third could move it |
| The 2025 festival coincided with GST cuts | October 2025 two-wheeler retail ran 31,49,846 against 12,87,735 in September, part of it credited to the cuts (FADA, F5, checked 12 October 2026) |

```notes
LIVE, 5 minutes. One doubt at a time, each with the fact that would settle it. The FADA figure is
a national series; it shows a festive month confounded by a tax change, a warning for any model
trained on national data. Transition: the two role cards.
```

---

## S36. Close: beat the bot, place the festival, price it
*What do finance and the vendor's sponsor hear, and what does the morning leave on the board?*

```cards
icon: calculator | eyebrow: To finance | title: Right growth, wrong weeks | body: Your 4 percent is the growth two years show. Copied by calendar, it books the peak on 5 October and sits 308,048 shipments short. | tone: light
icon: trending-up | eyebrow: To the vendor's sponsor | title: A fit, never a forecast | body: Within 1.4 percent on history, and 16,400 a week off on thirteen weeks it never saw. | tone: light
icon: badge-check | eyebrow: The rule | title: Beat the bot, then place the festival | body: Score on hidden weeks in shipments and rupees; copy by distance from Diwali; plan at the 0.82 share. | tone: dark
```

```notes
LIVE, 3 minutes. Each stakeholder is partly right: concede the true part first. The afternoon
writes the staffing note from these three cards. Transition: lunch, then half two.
```
