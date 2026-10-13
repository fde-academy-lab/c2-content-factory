# Week 4 explorer: build notes, sources and proofs

**INTERNAL.** The notes behind `demos/C2_W04_D01_week_explorer_STUDENT.html`, the one interactive page
for the whole of Week 4 (spine section 11). They say what each scene draws and what each control moves,
which deck slide calls which scene, where every number comes from, what the build decided where the
spine or the facts files left a choice, what the reviews found and what changed, which of the sources'
contradictions are now settled and by what, and what the proofs returned.

The page was built in three passes. The first, on 12 October 2026, built every scene from the case file
and the spine before any day pack existed. The second (commit 6998f38) moved Monday's and Tuesday's
scenes onto Monday's final data. The third, recorded here, moved Thursday's and Friday's scenes onto
their merged day packs (commits c4b8353, b070fea, 1aeaead and d1f3019, then 23634c7 after the two
reviews), after pull requests 232 and 233 had settled the other days' contradictions in the case file
and the spine. Pull request 239 then wrote Thursday's corrections into the case file and the spine,
and a second merge of main (756e35f) and one line of Th1's prompt (3bc59c0) brought the page level
with them.

## How the page is built and checked

| Step | Command or place | What it does |
|---|---|---|
| The house look and the diagram builders | `python3 scripts/build_companion.py content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html` | Fills the page's `<style data-c2kit>` and `<script data-c2kit>` blocks from `scripts/companion/`; T3's two trees are drawn by `C2K.driverTree` |
| Every number | The `W4` block in the page's head | One constants block, each value with its source in a comment: the case file or the spine for Monday to Wednesday's case numbers, Monday's data for M4 and T2, Thursday's and Friday's facts files by id and Friday's two data tables for Th1 to F4, "derived" for arithmetic on them, and "toy" for invented values that the page labels toy where they appear. Drawings and readouts compute from the block; the reveal sentences quote the day's numbers as text, so a changed value is edited there by hand too |
| Friday's rules | The page's script, after `F1N` | Naive, drift, the house bot, finance's rule, festival-aligned, the cushion and the plan, ported from `content/W04/D5/internal/C2_W04_D05_make_data_INTERNAL.py` with weeks counted from 1; the vendor's rows are read from its table, never computed |
| The browser sweep | `python3 scripts/html_sweep.py content/W04/D1/demos` | Clicks every control in DOM order and fails on a control that changes nothing, a console error or a covered dropdown |
| The day gate | `python3 scripts/verify.py content/W04/D1` | The layout, naming and writing rules, then every proof script on the day's folder, the sweep among them |

The six day buttons come first in the DOM, and choosing a day opens that day's section and every
earlier one, so by the time the sweep reaches the scenes the Saturday button has opened all six days
and every control is visible. Choosing a day sets `location.hash` to `mon` to `sat`, and a scene id
(`#M1`, `#Th3`) opens its day and scrolls to it, so a trainer can bookmark either. The page keeps
nothing between visits, loads nothing from the network and needs no install. Printing reveals every
scene first and prints one scene per A4 landscape page in its final state.

## The scenes, and what each control moves

Every scene has the six parts of spine section 11: a question as its heading, the first answer most
people give, a prediction made before any control is touched, a drawing, controls with a printed
readout each, and a reveal that prints the number and then names the formula last. Every scene opens
before the state its prediction asks about, and the reveal sets the scene to the case's state.

| Id | The question | What is drawn | What each control moves | The reveal |
|---|---|---|---|---|
| M1 | Can online hours rise while riders wait as long? | A city of twelve zones with sixty driver dots that drive, idle or sit offline, a picture with no scale | The floor slider, Rs 0 to 400 in steps of 20, moves dots online and into the outer zones and moves online hours, trips, trips per online hour, the idle share, the total top-up, the part paid to driver-weeks accepting under half their offers and the dot counts; the rider-wait toggle shows the wait meter and its minutes | At Rs 300: 118,000 to 146,300 hours, 224,200 to 230,900 trips, 1.90 to 1.58, Rs 1.16 crore of Rs 1.9 crore to driver-weeks accepting under half their offers, wait 4.8 to 4.6, and 1.83 already at Rs 100; trips per online hour = trips / online hours |
| M2 | Which number should the scheme pay for? | A seesaw of the paid number against three guardrails, above the same sixty dots | The select of four paid numbers re-places the dots, tips the seesaw, flips the guardrail chips and moves the dot counts, the idle share, the wait, the top-up per trip and the acceptance share, against guardrail lines printed in the readout | Trips with an acceptance floor puts 40 of 60 dots to driving against 31; which line catches which way of gaming; the definition's lines, with the north star defined |
| M3 | What does one line of a definition change? | The twelve driver-weeks as a table, with a before and after bar | Four selects (numerator, denominator, window, exclusions) recolour the columns, strike excluded rows and move the before, after and change readouts; the window select prints the counts it divides | Per online hour 1.90 to 1.19, per enrolled driver 19.0 to 14.7; the acceptance exclusion compares six drivers with four (the four alone fall 1.98 to 1.89) and, with enrolled drivers, turns the fall into a rise, 19.0 to 20.8; a definition names numerator, denominator, window, exclusions and what it does not reward |
| M4 | Which number moved first? | Monday's weekly acceptance share and bookings per online hour over twelve peak weeks, the launch marked | The week slider, 1 to 12, draws both lines to that week, rings each turn and moves the week's values and the turn readouts | Both lines turn in week 7, the launch week; acceptance leads because it can be read per offer while the launch week runs; a leading input is a number you can read, and act on, before the outcome is reported |
| T1 | What is left when the slide says one thing? | A slide with nine of Monday's numbers under a topic title | Nine checkboxes fade tiles, count the numbers left and rewrite the title when two remain; the warden test, defined in its readout as whether a reader outside the field could act on the title alone, prints its verdict on the current title | Trips per online hour and the top-up carry the claim; acceptance and cancellations show the gaming without its cost, so they go to the appendix; claim, evidence, caveat, action |
| T2 | Which denominator is the slide using? | The same bookings over three denominators as indexed bars | The select draws the chosen reading's bars; a reading not yet chosen stays a dashed outline; the select also moves the slide title and the before, after and change readouts | Rs 314 to Rs 260 per online hour; per active driver-week Rs 5,817 to Rs 5,861 on Monday's 6,360 and 6,500 driver-weeks; per trip flat at Rs 165; bookings per online hour = trips per online hour x fare |
| T3 | How big is a number nobody has measured? | Two guesstimate trees, UPI payments a day and drivers at the evening peak, each titled as a question | The select moves the focus between the trees; six sliders move the factors, the products and the anchors' lines; the UPI anchor and its ratio print at the reveal | 802 million a day in September 2026 (776 million over 31 days); drivers at peak: to be found, with the case's 656 drivers online before the launch named as a different unit; on these ranges peak requests moves the drivers' estimate most; clarify, map, calculate, validate |
| W1 | Why is lift a ratio of two areas? | A unit square with two bands and their overlap, the observed overlap beside it | Three sliders, P(A), P(B) and the observed share, in steps of 0.01, move the bands, the areas, observed over expected and the range the overlap can take at those bands | Bands widened to 0.70 and 0.50 at a fixed 0.30 overlap give lift 0.86; at 0.80 and 0.70 the overlap is forced to at least 0.50; the tea stall's 1.25; lift = P(A and B) / (P(A) P(B)) |
| W2 | What does confidence throw away? | A hundred carts in the case's proportions, with a legend for bread, milk, both and neither | Two filter buttons and a reset move carts to the right or fade them and move the counts | 34 carts left, 25 with milk, 25 / 34 = 0.74 against milk's 0.71, lift 1.04 as W1's ratio of areas; confidence = P(A and B) / P(A) |
| W3 | Why does the item in every cart look like the best partner? | The square with bread and milk, and two gauges | The milk-share slider, 0.10 to 0.90, moves milk's band, the overlap, confidence, lift and the carts holding both | At 0.71, confidence 0.74 and lift 1.04, with the held-lift assumption stated; confidence follows popularity, lift divides it out |
| W4 | What does a strip slot earn? | A cart page with three slots under a cart holding chips | The rank toggle swaps milk's slot for dip's; three sliders move every slot's rupees and the strip's day and month totals | Rs 3,240 against Rs 17,280 a day, about Rs 4.2 lakh a month for one slot, which Wednesday's S32 multiplies by milk's 1.5 slots; value = views x click-through x add rate x margin |
| W5 | Where should the support floor sit? | Lift against support for nine pairs on a log scale, filled dots for the case's numbers and open dots drawn inside its band | A guess slider and lock record the prediction and then lock; the floor slider, 0.1 to 5 in steps of 0.1, moves the floor line and the counts | Eight of nine survive 1 percent; ice cream with chocolate sauce, about four carts a day, goes on a watch list; any floor from 0.3 to 2.9 percent keeps the same eight; act above the floor, watch below it |
| Th1 | How can every batch shrink while the average stays flat? | Thursday's cohort staircase, the day's sizes and cells, filling month by month under the dashboard's line, with October on amber as the day's estimate | Next month adds a column up to October, then starts again from February; the slider resizes the August cohort from 1 to 3 times a normal 5,000 and moves its row, the counted members, October's reading and its range | 38.2, 38.0, 37.9 and 37.8 from June to September while every row falls and the August cohort sits outside the count; October about 33 (32.9; 31.9 to 33.8 for a month-two rate of 17 to 24 percent), about 35 at a normal size; everyone who joined before September reads 35.9; blend = sum of size x rate / sum of sizes |
| Th2 | What is the flat number made of? | Two months of a coaching centre's batches, stacked by size, opening before batch B joins | Batch B's size, from 0 in steps of 40 so every count is a whole person, and batch A's rate move the stacks and the blended share | 250 of 500 is still 50 percent; the Gold dashboard's gentler prop, one cohort of about 5,000 entering at about 38.5 a month; the weighted average written out |
| Th3 | Which stage owns the loss? | Gold members' September order flow from the day's events table, as bars whose lengths are the counts, under a header naming the unit, opening with the carousel's menu opens left out | The unit toggle and the carousel toggle swap among four sets of counts and move the header, every step's rate and the carousel line | 118 percent per session with the carousel in, 89 among sessions that searched, 101 per member; 34 and 61 percent; the loss inside the checkout, checkout start to order per session 72.5 to 55 percent for members on Android; each step divides by the step before in one unit |
| Th4 | Is it novelty or habit? | A launch-week cohort against a later weekly cohort over eight weeks, and the blended weekly actives since the launch, every number a toy | The week slider draws both curves to that week; the blend toggle shows the blended line, its value and the launch week's record | At week four 24 against 36 percent; the blend sets its record of 70,000 in launch week, dips to 48,400 in week three and is back at 69,800 by week eight; read each cohort by weeks since signup, at week four or later |
| F1 | What is a series made of? | Trend, season and noise panels on one scale, summed into one series over two labelled years, a toy | Three sliders move their panels, the series, its highest and lowest weeks and the trend's rise | The season's peaks and troughs move 25 thousand; on this noise the highest week goes from 255 to 277 thousand and the lowest from 167 to 146; the centre's own shapes and the cycle the toy leaves out; series = trend + season + noise |
| F2 | How wrong on the weeks it never saw? | Friday's 104 weeks with the hidden weeks shaded, the vendor's fit dashed when it is chosen, and the hidden weeks zoomed with each week's miss on one scale for every rule | The rule select (six rules) and the split slider, 52 to 91, move the forecast, the sticks, the rule's description, the MAE and the priced misses; the vendor scores only at the day's split; the board under the reveal stays at the day's split | 6,615 for festival-aligned and finance's rule, 9,831 for the house bot, 14,842 for drift, 14,923 for naive and 16,400 for the vendor; priced, Rs 13.5, 30.5, 28.0, 28.8 and 11.9 lakh; each raised to its own 0.82 point, Rs 8.8 lakh for festival-aligned, finance's rule and the house bot, Rs 10.0 for the vendor and Rs 17.7 for naive and drift; MAE = mean of absolute misses on held-out weeks |
| F3 | Where does the house bot put Diwali this year? | Friday's 2025 festive weeks above the house bot's and festival-aligned's 2026 forecasts on the same calendar weeks, on one scale with a legend | The Diwali slider, the weeks of 19 October to 9 November 2026, moves the marker, festival-aligned's copy, its eight-week total against both 2025 windows and the readouts, and says when it sits on a what-if; at the last stop the week outside the alignment band is ringed and explained; the bot stays | The bot peaks on 5 October at 418,200 and festival-aligned on 19 October at 434,928; the eight weeks against both 2025 windows, as a table of four forecasts; the bot's Rs 111.6 lakh scenario; copy the week at the same distance from the festival, then add the growth |
| F4 | Where should the plan sit when being short costs more? | The average cost of the week of 19 October's misses against the plan's distance above the forecast, with festival-aligned's thirteen hidden-week misses tried as its demand and drawn as dots beneath, violet where the plan covers them | Two cost sliders, an idle packer-shift from Rs 500 to 800 and a late shipment from Rs 15 to 40, move the curves, the plan's point, the ringed lowest point of the curve, the dots it covers, the shifts and the costs | 82 weeks in 100; the 0.82 point of the misses, 2.6 percent, covering 10 of 13, beside the curve's lowest point at 2.8; 446,236 shipments and 3,719 shifts for 19 October against 3,625; 20,275 shifts over eight weeks, 515 above 19,760; the 4.1 percent reading and Rs 1.4 lakh anywhere from 2 to 4 percent; plan quantile = under-cost / (under-cost + over-cost) |
| S1 | Does the method survive a change of company? | The week's methods on the left and the chosen unit's card on the right | The unit select lights the one or two methods the unit leans on and fills the card; the textarea writes the learner's own line into the map | Each unit leans on one or two methods, which come across unchanged; what changes is the metric, the constraint and the cost of an error |

## Which deck slide calls which scene

Every day's deck names its scenes in the slide's notes fence (spine section 11). Read from the five
merged decks; Saturday's pack is not built yet, and the spine has its deck reopen the home screen.

| Day | Slide, and the scene it calls |
|---|---|
| Mon | half1 S2 the home screen; S8 and S16 M1; S25 and S30 M2; S32 M3; S31 M4 |
| Tue | half1 section 1, S8, S9 and S10 T1; S14 and S15 T2; half2 section 4, S38 and S40 T3 |
| Wed | half1 S2 the home screen; S18 W1; S11 W2; S20 W3; S32 W4; S29 W5 |
| Thu | half1 S2 the home screen, Thursday lit; section 1 and S12 Th2; sections 1 and 2, S18 and S22 Th1; section 3 and S30 Th3; half2 section 5 and S44 Th4 |
| Fri | half1 S2 the home screen, Friday lit; S7 F1; S16 F2; S12 and S28 F3; S32 F4; half2 S1a F1, S1b F2, S1c F3 and F4 |

## Where the numbers come from

| Day | The day's numbers, with their place in the sources | Derived on the page | Toy, labelled toy on the page |
|---|---|---|---|
| Mon | The ticket table: 118,000 and 146,300 hours, 224,200 and 230,900 trips, 0.86 and 0.73, 0.04 and 0.09, 0.22 and 0.38, 4.8 and 4.6 minutes, 0.11 and 0.10, Rs 1.9 crore; L5's Rs 1.16 crore; the floor of Rs 300; the twelve rows' table; M4's twelve weekly ratios, Monday's facts file (`acceptance_2026_MM_DD`, `rs_per_hour_2026_MM_DD`) | Rs 82 of top-up per trip (Rs 1.9 crore over 230,900); the four drivers' 1.98 to 1.89 and the enrolled base's 19.0 to 20.8 from the rows | The response curve between and above the case's two floors; the dots' behaviour, wait, top-up and acceptance under the three other paid numbers; the guardrail lines of 0.80 acceptance and Rs 40 a trip |
| Tue | Rs 314, Rs 260 and Rs 165 (ticket); Monday's 6,360 and 6,500 active driver-weeks; 24.07 billion and 802 million a day (T3, NPCI through Outlook Money, checked 12 October 2026) | 776 million over 31 days; 656 drivers online in an average peak hour before the launch (118,000 hours over 180 peak hours: 5 weekdays, two windows of three hours, six weeks); Rs 5,817 and Rs 5,861 a driver-week | Every factor in the two guesstimate trees, which the learner sets |
| Wed | 71 percent milk, 34 percent bread, 0.74 and 1.04 for bread to milk, 0.73 and 1.03 for eggs, 5.0 percent and 3.4 for chips with cold drink, 0.25 percent and 4.6 for ice cream with chocolate sauce, the milk band of lifts near one (the case file's 0.96 to 1.08, used to place pairs and no longer printed), 1.2 and 6.4 percent click-through, 60,000 views, 0.5 add rate, Rs 9 margin, 40,000 carts | The hundred carts (25, 9, 46, 20) in the case's proportions; each pair's support from share times confidence; Rs 17,280, Rs 3,240, Rs 14,040 and Rs 4.2 lakh | The tea stall (R1); peanuts, dip and namkeen beside chips; milk's 0.75 and 1.06 beside chips, inside the band; the other milk pairs at lifts 1.03 to 1.07 |
| Thu | Thursday's facts: `cohort_size_jan` to `cohort_size_sep` (4,854 to 13,000 and 5,089), `cohort_mean_jan_jul` 5,000, `aug_times_normal` 2.6, `m1_jan` to `m1_aug`, the triangle's cells `tri_jan_m2` to `tri_jul_m2`, the dashboard's 38.2, 38.0, 37.9 and 37.8 (`dashboard_jun` to `dashboard_sep`), `everyone_sep` 35.9, `oct_sale_m2_assumed` 20.5 with its range of 17 to 24 and `oct_dashboard_estimate` 32.9, the September funnel per session and per member (`sep_sessions_*`, `sep_members_*`), `sep_menu_sessions_no_search` 38,932, `search_to_menu_searched_sep` 89 percent, the release's 58 to 44, 57 to 56 and 52 to 51, and checkout start to order 72.5 to 55 | The dashboard and October's blend from the cells and the sizes, with each older cohort sliding another 0.3 points in October as the generator's `october()` does; the funnel's counts with the carousel left out from menu view on (39,766, 31,748 and 20,477 sessions; 43,470, 24,183, 21,501 and 17,124 members), counted from the day's events table by the rule behind `search_to_menu_searched_sep` | The coaching batches (`toy_blend`); the AI app's two cohorts, whose week-four 24 and 36 are the day's `toy_ai_cohorts` and whose other weeks, the 100,000 launch cohort and the weekly 20,000 are this page's |
| Fri | Friday's data: the 104 weeks of `weekly_shipments` and the vendor's 114 rows of `vendor_forecast` (fitted to week 91, its hold-out forecast for weeks 92 to 104, its forecast for weeks 105 to 114); Friday's facts: the weeks and Diwali dates, `training_weeks` 91, `holdout_weeks` 13, `per_shift` 120, the costs and their ranges, `growth_factor` 1.04, the alignment band of five weeks before Diwali's week to four after, and the facts the reveals quote (the hold-out's MAEs, high weeks and priced misses, the vendor's 1.4 percent fit and its 3.6 and 11.5 percent drift, each rule's own cushion and its price, `own_cushion_*` and `own_raised_cost_*`, the plan's cushion and shifts, the curve's lowest point, `curve_min_pct`, the 4.1 percent reading with its Rs 1.4 and Rs 2.1 lakh, the window totals, the back-test's 4,034, the scenario's Rs 111.6 and Rs 3.3 lakh) | Every rule's forecast, MAE and priced miss at any split; each rule's own cushion; the cushion at any pair of costs; the plan's shifts; the eight weeks against both 2025 windows; the cost curve and its readouts | The trend, season and noise of F1 |
| Sat | Rohan Desai's "twenty times more one way than the other" (`docs/07_Client_Zero.md`, stakeholder table); Kalpa Health's six US metro areas billed in dollars (decision `build1-us-data`); the brief lines of spine section 10 and the case file's Saturday table | None | None: the four company cards carry no figure and say they are hypothetical |

At the case's state every Thursday and Friday readout reproduces its facts file to the printed digit:
a scratch script ports the same rules onto the CSVs in Python and the page's readouts were read back
in a headless browser at each scene's revealed state and at the sliders' ends.

## What the build decided where the spine or the facts files left a choice

| Choice | What the page does | Why |
|---|---|---|
| Which day sections show | A day button opens its own section and every earlier one, and dashes nothing below | The map lights every earlier node, and the sweep reaches every control only if the last day button opens all six days |
| The prediction form | Lettered choices in twenty scenes, with the key on A five times, B four, C six and D five; a guess slider with a lock button in W5, where the prediction is a count | The spine allows a choice or a slider guess; a key that sits on one letter or is always the longest lets a learner answer without thinking. Since the second pass M4's key, A, is its longest option, which that pass's scene owns (see the open items) |
| Opening states | Every scene opens before the state its prediction asks about: T2 draws a reading once it is chosen, T3 holds the measured 802 million for the reveal and opens its UPI tree at 50 million a day, Th2 opens before batch B joins, Th3 opens with the carousel's opens left out, F4 opens at the case's costs, and no caption or myth line prints the answer a prediction asks for | A drawing that shows the answer first turns the prediction into reading |
| Th1's October | An estimate on amber, each older cohort sliding another 0.3 points from September and the August cohort entering at 20.5 percent, with the readout giving the 17 to 24 range; the size slider keeps the 20.5 | The day estimates October this way (`oct_dashboard_estimate`, half1 S25) and names the assumption as one; the spine asks Th1's slider for the new cohort's size, so the rate stays the day's |
| Th1's prediction | Where October's reading lands, with options 21, 33, 36 and 38 and the key on 33 | The ticket prints the flat 38 for June to September, so the question moves to the month the August cohort is counted, as the first pass decided; the key follows the day's 32.9 |
| Th1's everyone-count | The reveal gives September's 35.9 alone | June's 40.9 is the same quantity and value as Kalpa's planted August blend, 40.9 (36 of 88), and September's 35.9 carries the point |
| Th3's carousel left out | From menu view on, the counts keep only member sessions that included a search; per member, what members did in those sessions | The day's fix counts menu views among sessions that searched (89 percent, half1 S30); carrying the same rule down the funnel keeps every step a share of the step before |
| Th4's blend | Later weekly cohorts of 20,000, so the blend sets its record in launch week, dips and is back near it, 69,800 against 70,000, by week eight | The day's transcript and S44 say weekly actives are still near the launch-week record two months on; under a launch spike and a steady weekly inflow the blend has to dip before it returns, so the page shows the dip and the return |
| F2's rules | Six rules in the select and the scoreboard, made as Friday's generator makes them, each from the split week | The day scores six (half1 S19 and S21); spine section 11 names four, and finance's rule and drift sit in the day's own table |
| F2's vendor | Scored only at the day's split, the week of 22 June 2026; elsewhere the page says it has no forecast | The vendor's hold-out rows are one forecast from that week (correction 1 in Friday's facts header); a fitted value is never scored |
| F2's other splits | Every other rule is forecast from the chosen week with the day's 4 percent, and the readout says the 4 percent was measured on weeks after an early split | The day's own back-test keeps the 4 percent and says it was measured later (half1 S30) |
| F2's board | Stays at the day's split, the week of 22 June 2026, and prices every rule twice: as it forecast, and raised to its own 0.82 point on the hidden weeks | The day prices each forecast at its own 0.82 point (half two S6; the facts' `own_cushion_*` and `own_raised_cost_*`), which shows festival-aligned and the house bot level at Rs 8.8 lakh on weeks with no festival; a board that moved with the split disagreed with the reveal's sentences |
| The reveal's check line | Every reveal adds that the controls now show the case's own state | The reveal sets each scene to the case's state, and a learner who missed the jump took the drawing for their own setting (the third pass's walk) |
| Th2's batch B | Steps of 40 members | At 52.5 percent, 40 members is 21 people, so every count on the readout is a whole person and the percent beside it agrees with it |
| F3's windows | The readout states festival-aligned's eight weeks against both 2025 windows at the slider's Diwali, and the reveal's table states all four forecasts at the case's Diwali | The facts' `window_2026` block and half1 S31; the table stays at the case's position so it never disagrees with the reveal's prose |
| F3's last stop | With Diwali on 9 November, the week of 28 September sits six weeks before it, outside the band, so the rule copies the calendar week of 2025, a festival week; the page rings that point and says so | The generator's rule does the same at that position, and the day never runs it there; the window to staff starts on 12 October, so its totals are untouched |
| The vendor's 22 percent | Printed on the Friday ticket and in F3's table | The first pass kept the vendor's 22 off the page because Kalpa's lab mirrors it; the merged Friday ticket (S1) and its window table (S31) print it, and the task asks for both windows, so the page follows the day |
| F4's curve | The day's empirical curve: the thirteen hidden-week misses tried as the week of 19 October's demand, with the plan read 0.82 of the way along the sorted misses, and the curve's own lowest point ringed on notebook 03's grid of 0.2 percent steps | The bell curve on an MAE of 8,900 behind the first pass's 10,300 shipments has no place in the merged day, whose S32 and S33 read the 2.6 percent off the thirteen weeks; the spine asks for the sum with its minimum marked, and away from the case's costs the two points part (at Rs 500 and Rs 40, +5.0 against +5.4) |
| F4's idle slider | Set in rupees an idle packer-shift, Rs 500 to 800 in steps of 10, with the cost of a spare shipment printed beside it | The case states the idle cost and its range per shift, and Rs 650 / 120 = Rs 5.42 is not on a grid a slider of rupees a shipment can step through |
| S1's map | The week's five methods on the left, the unit's card on the right | The home map's nodes become the methods that stay, and the card shows what changes |
| Motion | CSS transitions and one CSS animation (the driving dots), switched off under reduced motion; nothing animates by timer | Motion explains the mechanism without changing the page between the sweep's before and after reads |
| Toggle labels | Every toggle keeps its label and carries its state in `aria-pressed`, which the pressed style shows | The WAI-ARIA authoring practice for toggle buttons keeps the label fixed while the state changes; the map's toggle follows the same rule |
| Light theme only | The house companion look, tuned for a projector | The house pages are light; a dark theme would need every drawing's colours as variables, which the house library does not carry yet |

## What the first pass's two reviews found and what changed

Two fresh reviewers, who wrote findings and edited nothing, walked the page while it was being fixed:
a fresh graduate meeting each scene cold (43 rows at commit fcf106f: none blocking, 25 slowing, 16
cosmetic, 2 scenes that simply work, plus 12 findings fixed during the walk, two of which blocked
learning) and a rigor and numbers pass (32 number findings, 19 of them in the sources, 6 arithmetic, 9
against the spec, 13 plant placements judged and 4 style points). Their reports sat in that session's
scratchpad as `walk_fresh_graduate.md` and `review_rigor.md`.

| Where | What the reviews found | What changed |
|---|---|---|
| W1 | The reveal's bands of 0.80 and 0.70 with an overlap of 0.30 cannot happen | Bands of 0.70 and 0.50 (lift 0.86); the readout prints the range the overlap can take |
| T2, W2, T3, Th2, Th3, W3, S1 | A drawing, caption, myth line or header printed the answer before the prediction | Each now opens before its answer (see the opening states above) |
| Th1 | The reading was unstated, the unrounded blend drifted 0.8 points, the slider never moved the dashboard and the steps stopped at September | Reading stated, October added, slider resizes the August cohort; the third pass replaced the flattened toy cells with the day's |
| F2 | The vendor priced cheapest with nothing reconciling it, the vendor's rule was unstated, the methods were undefined | The raised baseline priced in prose and as a scoreboard row, each rule described as it is scored, the split's meaning printed |
| M3 | The four drivers "1.90 to 1.89" compared six drivers with four | The reveal gives 1.98 to 1.89 for the four, and names the shrinking-base rise |
| M1, M2, M4 | The top-up's base, the guardrails' lines, the ring's meaning, the dots' scale, the north star and the mean of weekly ratios were unclear or loose | Each is now stated on the page |
| W4, W5 | A partner at chance earned a full slot; milk's toy lifts sat in Kalpa's band; dots, regions and the floor were unexplained | Peanuts replace bread, milk's toy lifts move to 1.03 to 1.07, a legend, plain region labels and a floor sized from W4 |
| T3 | The drivers' check compared different units and the reveal named the wrong biggest factor | The check reads "to be found" with the unit stated; peak requests named on these ranges |
| F1, F3, F4 | Overstated reveal arithmetic, an unlabelled toy panel, a clipped legend, no plain words for the quantile, no festive caveat | Each fixed |
| The map | "Five companies" counts Uber twice; two links did not hold; Monday's Kalpa node named a trainer-only window | Four companies; links rewritten; "reorders per member" |
| Whole page | Readouts repeated the raw slider value | Dropped |

Declined, with the reason:

| Finding | Why it stays |
|---|---|
| Lighting a later day prints the earlier days' findings on the map (walk) | Spine section 1 asks for it; the map never prints the chosen day's own finding, so nothing is spoiled in class, and a learner who opens a later day first has chosen to read ahead |
| T3 asks where the published number lands, where the spine says "within what range the product will land" (rigor) | The options are ranges and the learner builds a product to back a choice; the reveal names the anchor as the spine does |
| Th3 has no platform split, so the drawing cannot show the Android loss (walk) | Spine section 11 fixes Th3's drawing and its two toggles; the reveal names the stage, and the split belongs to the Thursday notebook |
| The reveal sentences do not follow the constants block (rigor) | The head comment says so; generating reveal numbers from the block is a later engineering task |
| W1's readout labels its expected area P(A) x P(B) before the reveal (rigor) | The two areas are the scene's drawing |
| M1 asks about Rs 250 while the case's floor is Rs 300 (walk) | Spine section 11 fixes the Rs 250 question; the reveal quotes the 1.83 at Rs 100 |
| Toggles should flip their labels (walk) | See toggle labels above |

## What the third pass's two reviews found and what changed

Two fresh reviewers, who wrote findings and edited nothing, read the eight rebuilt scenes at commit
d1f3019. The rigor and numbers pass ported every Friday rule into Python and the page's own script into
Node, recounted Th1 from `member_months` and Th3 from the events table, and swept every slider: 16
findings, none wrong, 3 misleading, 5 loose and 8 cosmetic. The fresh graduate walked Th1 to F4 cold
with 109 screenshots and made every prediction right from the screen: 40 findings, none blocking, 18
slowing and 22 cosmetic. Their reports sit in this session's scratchpad as `review_rigor_pass2.md` and
`walk_fresh_graduate_pass2.md`; commit 23634c7 carries the fixes.

| Where | What the reviews found | What changed |
|---|---|---|
| F2 | The board set festival-aligned raised to its own 0.82 point beside every other rule unraised, and it moved with the split while the reveal's sentences stayed at 22 June (rigor 2, 9 and 10) | The board stays at 22 June and prices every rule raised to its own point: Rs 8.8 lakh for festival-aligned, finance's rule and the house bot, Rs 10.0 for the vendor, Rs 17.7 for naive and drift |
| F2 | The house bot and festival-aligned were undefined when the prediction was asked, and option C's qualifier pointed at the key (walk 20, rigor 14) | The prompt defines each rule, and the options are the bare names |
| F2 | The zoom rescaled for the vendor alone, the vendor's fit hid under the actual line, and the axis ends carried no year (walk 27, 28 and 30) | One scale for every rule at a split; the fit drawn dashed on top with its 1.4 percent; years on the axis ends |
| F2 | "The vendor's model was run once", and "the growth the two years show" (rigor 4 and 5) | The vendor forecast the hidden weeks once, from 22 June; the 4 percent is the training weeks' growth |
| F3 | At the last stop a second hump appeared on 28 September, a calendar copy of 2025's sale week from outside the band (rigor 1) | The point is ringed and a readout line explains it |
| F3 | The slider opened on a what-if that read as the case, with no scale and no legend (walk 33 and 34) | The output says what-if or the case's own week; gridlines at 200k and 400k and a legend |
| F3 | The 3,625 shifts are the unraised count the day uses as a wrong option, and the 4 percent away from Diwali went unsaid (rigor 8 and 12) | Labelled as at the forecast itself, before F4's cushion; the 4 percent named |
| F4 | The plan marker left the curve's minimum when the costs moved; "2 to 3 percent" narrowed the day's spread; the misses' scaling, the dots' colours and the 4,034 were unexplained (rigor 6 and 7; walk 36, 37 and 40) | The curve's lowest point is ringed on the day's grid; the reveal takes notebook 03's 4.1 percent and its Rs 1.4 lakh anywhere from 2 to 4 percent; the caption explains all three |
| Friday ticket | "Rs 25 costs more than Rs 650" read wrongly, the capacity caveat was missing, and FC was not expanded (rigor 3 and 15; walk 21 and 22) | Costs said per shipment, the caveat added, and the fulfilment centre's planner named |
| Th1 | The cells argued for "holds at 38", the assumption's link to the discount was unsaid, the 37.5 was not on screen, and the shading, "batch" and "October has not happened" puzzled (walk 3 to 7) | The prompt ties the 20.5 to the fall after month one and the discount; the reveal names the 37.5; the caption explains shading and batches and says October's month has not closed |
| Th2 | Count and percent disagreed at some sizes, and the rate printed as 0.40 (walk 9 and 10) | Batch B steps by 40, and the rate prints as a percent |
| Th3 | The chart named no unit, the funnel's pooling went unsaid, a session count sat under member rates, and the reveal's 72.5 to 55 had no unit (walk 12, 13 and 15; rigor 13) | A header names the unit; the caption says the funnel pools every platform and the month; the member line drops the session count; "per session" |
| Th4 | "The AI app" came before it was introduced, nothing tied it to Gold's sale cohort, the lower panel's weeks were unexplained, the labels touched at week two, and "load and spend" was vague (walk 16 to 19) | The myth names the AI writing assistant; the reveal ties the launch cohort to the sale-week members; the lower title says it plots the weeks above; labels kept 17 px apart; the servers' load and the inference spend |
| F1 | The trend slider read as a level, the thin panels had no negative tick, and the formula dropped the level (walk 23 to 25) | Thousand shipments added each week; -50 ticks; "here on a level of 200 thousand a week" |
| Every scene | The reveal moved the controls without saying so (walk 1) | The check line says the controls now show the case's own state |
| F2, Th3 | Readout lines opened on a label (rigor 16) | Every rule's description and the carousel line are full sentences |
| F2 | The page rounded an exact half up where the generator's Python rounds it to even (rigor 11) | The page rounds half to even; no printed number moved |

Declined, with the reason:

| Finding | Why it stays |
|---|---|
| Every chart label prints at 5 to 6 px at a 390 px phone width, and M3's table scrolls sideways there (walk 2, and outside the eight scenes) | The page is built for the projector and a laptop, where labels print at 13 px or more; a phone layout for all 21 scenes is its own task, listed in the open items |
| Th3 has no platform or date split (walk 12) | As the first pass decided, spine section 11 fixes Th3's toggles; the caption now says no step here shows the loss, and the reveal names it |
| "Month-two retention" names a blend of every age from two up (walk 8) | It is the dashboard's own name in the day's ticket, defined in the same sentence |
| Th2's bars sit low at batch B = 0 (walk 11) | A fixed scale lets the eye see the column grow as B joins |
| Th3's toggle reads "Count per member" over "Counting per session" (walk 14) | Toggles name the action and keep their label, as the first pass decided |
| F1's series line touches the "trend" label at noise 20 (walk 26) | The label's halo keeps it readable |
| Sums above Rs 100 lakh print in lakh (walk 31) | The day prints them in lakh too, as half one S35's Rs 111.6 lakh does |
| F4 prints 82 in 100 before deriving it (walk 38) | The formula comes last by design, and the reveal derives it |
| F4's y-axis rescales with the costs (walk 39) | The plan line and the ring carry the answer, and an axis fixed at Rs 16 lakh would flatten the curve at the case's costs |
| F2's "hidden weeks" label sits outside the shaded block (walk 30, in part) | It names the block from outside it, so it never covers a week |

## The sources' contradictions, and what settled each

The first pass found eleven places where the case file or the spine disagreed with itself and worked
around each on the page. Pull requests 232 and 233 settled Monday's, Tuesday's, Wednesday's and
Friday's in the case file and the spine, and the merged day packs settled Thursday's and carried the
rest into their data; pull request 239 then wrote Thursday's corrections into the case file and the
spine.

| | The contradiction | What settled it | What the page does now |
|---|---|---|---|
| 1 | Monday's twelve rows summed to 114 and 88 trips while the case file said 114 to 110 and 1.90 to 1.49, and "two drivers' hours doubled" | Pull request 232: the case file and the spine's L1 read 114 to 88 and 1.90 to 1.19, E's and F's hours "rose by about half", and the margin rule lets the shared starting 1.90 match | M3 prints 1.90 to 1.19, as before |
| 2 | Monday's Rs 1.16 crore was called "paid to idle hours" | Pull request 233: paid to driver-weeks that accepted under half their offers | M1 says so |
| 3 | Tuesday's per driver-week reading "rose because hours rose" | Pull requests 232 and 233: Rs 5,817 to Rs 5,861 on 6,360 and 6,500 active driver-weeks, bookings up 3 percent against driver-weeks up 2.2 | T2 reads Monday's driver-weeks since the second pass; its formula keeps the unrounded 1.578, so 1.578 x Rs 165 = Rs 260 |
| 4 | Wednesday's milk on 44 percent of impressions blended to 4.1 percent against the stated 3.8; the twelve rows' bread to milk confidence sat 0.01 from the full data's 0.74; the milk band overlapped Kalpa's charger band | Pull request 233 and Wednesday's facts header: milk on half the slot impressions; the twelve rows' bread to milk now 1.00 with lift 1.50; the band stays a notebook check | The page prints neither the share, the blend, the twelve rows nor the band |
| 5 | Thursday's flat 38 could not hold under the spine's first-month definition | Thursday's facts, `definitions` and the first correction: the dashboard counts members two or more months past their signup month, the reading the first pass took | Th1 draws the day's cells under that definition |
| 6 | Thursday's twelve rows held 5 of 12 in September, 0.7 from Kalpa's 41; 60,000 members against 53,000; the 58 to 44 named no unit; the release's 14-point fall sat a point from Kalpa's planted 15 | Thursday's corrections, written into the case file and the spine by pull request 239: the twelve rows read 0 of 5 for the August members' month one and 2 of 12 for everyone in September; 53,089 members; the 58 to 44 counts sessions; Kalpa's planted fall in the window is now 83.3 to 63.6 percent, 19.7 points; 8,027 of the August cohort's 13,000 joined on the sale (`aug_sale_members`) | The ticket prints 53,089 and the August cohort's 13,000; Th1's prompt says the cohort was grown by a discounted sale week, where it had called all 13,000 bought on a discount; the page prints no twelve-row count |
| 7 | Friday's hold-out of "22 June to 21 September" was fourteen weeks, and the vendor was fitted to the weeks it was scored on | Pull request 233 and Friday's corrections 1 and 6: thirteen weeks from 29 June, every forecast from 22 June, the vendor's hold-out rows a forecast from that week | F2 reads the vendor's own rows and scores it only from 22 June |
| 8 | Friday's calendar stopped at 16 November, short of the 30 November window | Pull request 233: 114 weeks | The page's weeks run to 114, the vendor's forecast rows among them |
| 9 | On the first pass's toy weeks the vendor's errors priced level with a raised baseline, with no festive week in the hold-out | Friday's pack prices every rule and lets the vendor's cheaper misses stand (S23), names why it still loses the plan (S24) and tests placement on the 2025 festival (S30: 4,034 against 58,250 a week) | F2 and F3 follow the day |
| 10 | "A late shipment costs five times an idle shift"; the plan quantile and other Friday numbers equalled Kalpa's plants | Pull request 233: 4.6 times a spare shipment; the plant-margin rule applies to Kalpa planted values of the same quantity | F4 prints 4.6 times; the 0.82 stays beside Wednesday's Kalpa confidence 0.82, a different quantity |
| 11 | Spine section 1's map counted five companies and named a trainer-only window | Pull request 233: four companies, and Kalpa's node names reorders per member | The map already said so |

Still open, for the orchestrator or the next pass:

- M4's key, A, is its longest option, against the page's own rule. The second pass set it, and this
  pass left Monday's and Tuesday's scenes alone as the task asked; lengthening option D, "It never
  turns.", would clear it.
- W5 prints the Wednesday case's thin pair, ice cream with chocolate sauce, at 0.25 percent of carts,
  the same quantity and value as Kalpa's planted thin pair (`kalpa_thin_support`, 0.25 percent).
  Wednesday's own pack prints the same number, so a change belongs to Wednesday first.
- Th3's 64 percent, checkout start to order per session, prints beside Kalpa's planted cart to
  checkout in the window, 63.6. The steps differ and Thursday's own S28 prints the 64, so it stays.
- At a 390 px phone width every chart label prints at 5 to 6 px, and M3's table scrolls the page
  sideways by 117 px. A phone layout means reshaping all 21 drawings, which belongs to a pass of its
  own.
- The case file, since pull request 239, says 8,027 of the August cohort's 13,000 "joined that
  week", and the facts' `aug_sale_members` says the same; Thursday's self-check and fallback deck
  say the sale week brought 9,108, the 8,027 who joined on the sale's discount and 1,081 who did not
  (`sale_week_organic_members`). The page prints neither count, so the fix belongs to the case file's
  one sentence and the facts' `how` line.

## The proofs

### The browser sweep

The sweep's last lines on the final page, with the pre-installed Chromium at `/opt/pw-browsers`:

```
      C2_W04_D01_week_explorer_STUDENT.html: 187 controls clicked, 0 inert, 0 not visible in the opening state, 0 console errors
RESULT: PASS (0 failures)
```

`python3 scripts/verify.py content/W04/D1` returned `RESULT: PASS (0 failures)` over the 59 files of
Monday's merged folder, with the same sweep result. The page is plain ASCII at 259 KB, under the
spine's 400 KB, with no URL, no external file, no storage call and no network request.

### The plant grep

A scratch script reads the page with every scene revealed and the `W4` constants block, and searches
for every planted Kalpa value in its printed forms: the `plants` blocks of Monday's and Thursday's
facts files, the PLANT entries of Wednesday's `kalpa_lab`, and the Friday Kalpa plants of the case
file's list, with their values from Friday's `kalpa` block. Eighteen hits remain, each the case's own
number or a different quantity:

| The hit | Where | Why it stays |
|---|---|---|
| 0.82, six times | The Friday node, F2's board, F4's readouts, reveal and formula | Friday's plan quantile (`plan_quantile`), set beside Wednesday's Kalpa confidence 0.82, a different quantity |
| 0.84 | M2's readout | M2's toy acceptance under the acceptance floor, beside Kalpa's charger share of 84.5 percent |
| 0.25 percent | W5's reveal | Wednesday's case number (see the open items) |
| 64 percent, twice | Th3's readout and drawing | The day's checkout start to order per session (see the open items) |
| 31 percent | The Thursday ticket | The August cohort's month one, beside Kalpa's 30.9 percent of sessions skipping search |
| 7.8 percent | F4's reveal | Festival-aligned's largest hidden-week miss, beside Kalpa's checkout per session |
| 24 percent, four times | T1's options, Th1's readout and reveal, Th4's reveal | Monday's 24 percent rise in hours, the day's 17 to 24 range, and the day's AI toy, beside Kalpa's checkout per member of 24.5 |
| 22 percent and 22.0 percent | The Friday ticket and F3's table | The Friday case's vendor promise (`vendor_promise_pct`), which Kalpa's lab mirrors by design |

### The writing checks

| Check | Scope | Result |
|---|---|---|
| The style sweep inside `verify.py` (dashes, banned words, the contrast construction it rejects, clock times, the rupee glyph, invisible Unicode, names, faculty sessions, undated links) | The page and these notes | Pass |
| `tic_scan.py` from the llm-tic-scrubber skill | The Thursday and Friday sections rendered with every scene revealed, outputs and readout labels included, 367 runs after the reviews' fixes; these notes, 295 runs | Clean |
| The humanizer skill's read, in file mode on prose only | The rebuilt tickets, captions, readout lines and reveals | Two staged lines rewritten: F2's "Priced, the order changes." now carries its reason, and F3's scenario names what it rests on |
| Characters | The page and these notes | Plain ASCII, with none of the contrast construction the style sweep rejects |

### Screenshots

Taken with the pre-installed Chromium after the last fix, in this session's scratchpad under
`final_pass3/`: Th1 to Th4 and F1 to F4 in their revealed states, and the sliders' ends
(`f2_split52_vendor.png`, `f3_diwali108.png`, `f3_diwali111.png`, `f4_rs500_rs40.png`,
`f4_rs800_rs15.png`, `th4_week2.png`, `th3_member_left_out.png`), every run with no console error.
Each was looked at, and so were the earlier rounds under `shots/` and its siblings. Th3's bars were narrowed before drawing so the day's longer
counts clear the rate labels, and Th4's curve label was shortened to fit; the screenshots then showed
F3's festival-aligned label crossing its own line, F4's long readouts squeezing their labels to a word
a line, and F4's plan label crossing the forecast line at the high costs, and each was moved or split.
