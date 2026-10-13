# Week 4 explorer: build notes, sources and proofs

**INTERNAL.** The notes behind `demos/C2_W04_D01_week_explorer_STUDENT.html`, the one interactive page
for the whole of Week 4 (spine section 11). They say what each scene draws and what each control moves,
which deck slide calls which scene, where every number comes from, what the build decided where the
spine or the facts files left a choice, what the reviews found and what changed, which of the sources'
contradictions are now settled and by what, and what the proofs returned.

The page was built in three passes and then read against the concept-first rebuild. The first pass, on
12 October 2026, built every scene from the case file and the spine before any day pack existed. The
second (commit 6998f38) moved Monday's and Tuesday's scenes onto Monday's final data. The third moved
Thursday's and Friday's scenes onto their merged day packs (commits c4b8353, b070fea, 1aeaead and
d1f3019, then 23634c7 after the two reviews), after pull requests 232 and 233 had settled the other
days' contradictions in the case file and the spine; pull request 239 then wrote Thursday's corrections
into the case file and the spine, and a second merge of main (756e35f) and one line of Th1's prompt
(3bc59c0) brought the page level with them. The fourth, on 13 October 2026 on branch `w04-week-read`,
followed the five days' concept-first rebuild (decision `concept-first-case-second`): the home map now
carries each day's row subtopics, every scene's controls and reveal wait behind its prediction, and
every scene that taught a retired example or printed a value its deck now reaches later moved onto the
day's own invented example or the day's rebuilt numbers. A trainer who did not write the week then
read the page against the five decks' opening slides and their scene calls, and one fix pass followed,
both on 13 October 2026; the section on the cold read below records each finding and what changed.

## How the page is built and checked

| Step | Command or place | What it does |
|---|---|---|
| The house look and the diagram builders | `python3 scripts/build_companion.py content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html` | Fills the page's `<style data-c2kit>` and `<script data-c2kit>` blocks from `scripts/companion/`; T3's trees are drawn by `C2K.driverTree` |
| Every number | The `W4` block in the page's head | One constants block, each value with its source in a comment: a day's facts file by id, a day's data table, "derived" for arithmetic on them, and "toy" for the few invented values that have no facts id yet (listed below). Drawings, readouts and the reveals rebuilt in the fourth pass compute from the block; the reveals still written as text quote their day's numbers and are listed below |
| The day's topics | `W4_TOPICS`, after the `W4` block | Each day's row subtopics, verbatim and in the row's order from `docs/curriculum/W4_Analyst_craft.md`, which the home map prints on each day's box |
| Friday's rules | The page's script, after `yAt` | Naive, drift, the house bot, finance's rule, festival-aligned, the cushion and the plan, ported from `content/W04/D5/internal/C2_W04_D05_make_data_INTERNAL.py` with weeks counted from 1; the vendor's rows are read from its table, never computed |
| The browser sweep | `python3 scripts/html_sweep.py content/W04/D1/demos` | Clicks every control in DOM order and fails on a control that changes nothing, a console error or a covered dropdown |
| The day gate | `python3 scripts/verify.py content/W04/D1` | The layout, naming and writing rules, then every proof script on the day's folder, the sweep among them |

The six day buttons come first in the DOM, and choosing a day opens that day's section and every
earlier one, so by the time the sweep reaches the scenes the Saturday button has opened all six days.
Choosing a day sets `location.hash` to `mon` to `sat`, and a scene id (`#M1`, `#Th3`) opens its day and
scrolls to it, so a trainer can bookmark either. The page keeps nothing between visits, loads nothing
from the network and needs no install. Printing reveals every scene first and prints one scene per A4
landscape page in its final state.

## The home map

Each day's box carries, under the day's question and its case, the row's subtopics as numbered lines in
the row's own words and order: six on Monday and five on every other day. The legend above the map
says what the bold lines, the numbered lines, the violet finding lines, the amber Kalpa box and the
connecting lines mean. The map is drawn 1,200 by 632 units and printed 646 pixels tall at a laptop's
width, so it fits a 1,366 by 768 screen below the day buttons; a topic line wider than its box would
be squeezed by `textLength`, and none is. Saturday's row names its subtopics as nine interview
anchors, so Saturday's box says so in a third line, and the nine open, verbatim and with their tags,
in a list under the map.

## The scenes, and what each control moves

Every scene has the six parts of spine section 11: a question as its heading, the first answer most
people give, a prediction, a drawing, controls with a printed readout each, and a reveal that prints
the number and then names the formula last. Until a letter is chosen, or W5's guess is locked, every
control except the set select puts itself back and asks for the prediction, outlined in rose, and the
reveal stays shut. Seven scenes carry two sets, chosen by a select at their top that starts the scene
again, prediction and all: the day's invented example first, for the concept chapter that calls the
scene, and the case second, for the case chapter that calls it (W1, W2, W3, W5, F2 and F3), or, in T3,
chapter 8's two questions. Every scene opens before the state its prediction asks about, and the
reveal sets the scene to its set's own state and says so.

| Id | The question | What is drawn | What each control moves | The reveal |
|---|---|---|---|---|
| M1 | Can online hours rise while riders wait as long? | A city of twelve zones with sixty driver dots that drive, idle or sit offline, a picture with no scale | The floor slider, Rs 0 to 400 in steps of 20, moves dots online and into the outer zones and moves online hours, trips, trips per online hour, the idle share, the total top-up and the dot counts; the rider-wait toggle shows the wait meter and its minutes | At Rs 300: 118,000 to 146,300 hours, 224,200 to 230,900 trips, 1.90 to 1.58, wait 4.8 to 4.6, and 1.83 already at Rs 100; trips per online hour = trips / online hours |
| M2 | Which number should the scheme pay for? | A seesaw of the paid number against three guardrails, above the same sixty dots | The select of four paid numbers, in the order of Monday's S75 with an acceptance floor third, re-places the dots, tips the seesaw, flips the guardrail chips and moves the dot counts, the idle share, the wait, the top-up per trip and the acceptance share, against guardrail lines printed in the readout | Trips with an acceptance floor puts 40 of 60 dots to driving against 31; which line catches which way of gaming; why S75's fourth choice, enrolled drivers, is not drawn; the definition's lines in S80's and S81's words |
| M3 | What does one line of a definition change? | The twelve driver-weeks as a table, with a before and after bar | Four selects (numerator, denominator, window, exclusions) recolour the columns and strike excluded rows; once a prediction is made they move the before, after and change readouts, which until then are outlines | Computed from the rows: per online hour 1.90 to 1.19, per enrolled driver online at peak 19.0 to 14.7; the acceptance exclusion compares six drivers with four (the four alone fall 1.98 to 1.89) and, with enrolled drivers, turns the fall into a rise, 19.0 to 20.8; on the full data, S81's 35.76 to 35.89 |
| M4 | Which number moved first? | Monday's weekly acceptance share and bookings per online hour over twelve peak weeks, the launch marked | The week slider, 1 to 12, draws both lines to that week, rings each turn and moves the week's values and the turn readouts | Both lines turn in week 7, the launch week: acceptance 0.862 to 0.729, and bookings per online hour Rs 310.3 to Rs 271.0 and on to Rs 259.1 by the third week, as Monday's S28 reads them; acceptance leads because it can be read per offer while the launch week runs |
| T1 | What is left when the slide says one thing? | Slide A as Tuesday's S33 shows it, nine tiles under a topic title; with only the claim's two numbers left, the slide rebuilt in S35's four parts | Nine checkboxes fade tiles and count the numbers left; two left make the title the claim, or a title made of the two numbers; the warden test, Tuesday's notice-board check, prints its verdict on the current title | S34's key, b: trips per peak online hour 1.90 to 1.58 and the 61 percent of the Rs 1.9 crore top-up paid to low acceptance; Rs 314 to Rs 260 at the Rs 165 fare; the action's Rs 58 lakh to Rs 92.7 lakh; claim, evidence, caveat, action |
| T2 | Which denominator is the slide using? | The same bookings over three denominators as indexed bars | The select draws the chosen reading's bars; a reading not yet chosen stays a dashed outline | Rs 314 to Rs 260 per online hour; per active driver-week Rs 5,817 to Rs 5,861; per trip flat at Rs 165 |
| T3 | How big is a number nobody has measured? | The chosen question's tree: drivers online at Uber's evening peak in Hyderabad as Tuesday's chapter 8 maps it, six leaves under trips to serve an hour, trips per online driver-hour and the buffer; or UPI payments a day as active users times payments per user | A slider per leaf, each running across the range Tuesday's facts give its guess: people 0.9 to 1.1 crore, weekday trips per 100 people 0.5 to 1.5, the evening share 0.20 to 0.30, trips a busy driver fits in an hour 2 to 3, the idle share 0.22 to 0.38 and the buffer 1.10 to 1.25; active users 25 to 45 crore and payments 1 to 3 a day; each moves the tree, the running results and the estimate, and the check prints at the reveal | Drivers: about 5,700, from 2,900 to 8,600 as weekday trips per 100 people run across their range, with every other leaf's swing in order; 0.60 driver-hours a trip against the case's 0.53 before the launch, about 5,000 at the case's 1.90 trips an hour, a published count to be found. UPI: 802 million a day over September's 30 days, the chain's 700 million about 13 percent below, 776 million over 31 days, about Rs 1,220 a payment |
| W1 | Why is lift a ratio of two areas? | A unit square with two bands and their overlap, the observed overlap beside it | On the canteen, three sliders count orders out of 12; on the case, they move shares of all carts; each moves the bands, the areas, observed over expected and the overlap's possible range, and the overlap slider runs only across that range | Canteen: roti and sabzi 3 / 1.33 = 2.25, and widening B to chaas's 9 orders at the same 3 gives 1.00. Case: 10,064 carts against the 9,656 chance gives, lift 1.04, where the twelve carts read 1.50 |
| W2 | What does confidence throw away? | The twelve orders, or the case's twelve carts, as cards with a legend | Two filter buttons and a reset move the cards and the counts | Canteen: papad to dal rice 3 / 5 = 0.60, dal rice to papad 3 / 6 = 0.50, lift 1.20. Case: bread to milk 4 / 4 = 1.00, lift 1.50 on twelve carts, too few to trust |
| W3 | Why does the item in every order look like the best partner? | The square with the popular item's band, and two gauges | The popular item's share moves its band, the overlap, confidence, lift and the count holding both, with the pair's lift held | Canteen: roti to chaas at chaas's 0.75 reads confidence 0.75 and lift 1.00, and no partner can pass 1.33. Case: bread to milk 0.74 and 1.04, the 50 common items 0.70 to 0.74 and 0.99 to 1.04, no partner past 1.41 |
| W4 | What does a strip slot earn? | A cart page with three slots, each with milk's share of its views, its click-through and its rupees a day | The rank toggle, rank by lift against rank by count, takes milk out of the strip; three sliders, views, the add rate and the margin, run across their stated ranges and move every slot's rupees and the strip's day and month | Rs 17,280 at 6.4 percent against Rs 3,240 at 1.2, Rs 14,040 a day, about Rs 4.2 lakh a month a slot; milk's 1.5 slots' worth recovers about Rs 6.3 lakh a month, Rs 3.9 lakh to Rs 9.3 lakh across the ranges |
| W5 | Where should the support floor sit? | Lift against support for the canteen's thirteen pairs, or the case's nine, with the 1.5 bar and the floor | A guess slider and lock record the prediction; the floor slider moves the floor line and the counts | Canteen: 6 of 13 pairs at a floor of 3 orders; gulab jamun and curd's 6.00 on one order goes on the watch list. Case: 8 of 9 at 1 percent, 4 past the bar; ice cream and chocolate sauce, 4.60 on 0.25 percent, watched; 246 pairs across all carts |
| Th1 | How can every batch shrink while the average stays flat? | Thursday's cohort staircase from the day's sizes and cells, filling month by month under the dashboard's line, October on amber as the day's estimate | Next month adds a column up to October, then starts again; the slider resizes the August cohort from 1 to 3 times a normal 5,000 | 38.2, 38.0, 37.9 and 37.8 from June to September; October about 33 (32.9; 31.9 to 33.8 for a month-two rate of 17 to 24 percent); everyone counted, September 35.9 |
| Th2 | What is the flat number made of? | A neighbourhood gym's members over January and February, stacked by group, Thursday's chapter 3 example | The January joiners in February's count, 0 to 800 in steps of 40, and the older members' February rate move the stacks and the blend | 250 of 500 is still 50 percent while the older members fall from 50 to 40; the weighted average written out |
| Th3 | Which stage owns the loss? | Gold members' September order flow from the day's events table as bars under a header naming the unit | The unit toggle and the carousel toggle swap among four sets of counts | 118 percent per session with the carousel in, 89 among sessions that searched, 101 per member; the unit decides the question each rate answers, and the loss needs the split by platform and date, which the deck makes after its call |
| Th4 | Is it novelty or habit? | A launch-week cohort against a later weekly cohort over eight weeks, and the blended weekly actives, every number a toy | The week slider draws both curves; the blend toggle shows the blended line | At week four 24 against 36 percent; the blend's record of 70,000 in launch week, 48,400 in week three, 69,800 by week eight |
| F1 | What is a series made of? | The chai stall's eight weeks from 30 September 2024 as a trend in cups, each day's share of a weekday and a wobble factor in three thin panels, multiplied into the line beneath | Three sliders, growth 0 to 100 percent a year, a Sunday's share of a weekday 0.1 to 1 and the wobble 0 to 10 cups on a weekday, move their panels, the line and the readouts | Doubling the dip, a Sunday from 0.6 of a weekday to 0.2, drops each Sunday from about 60 to about 20 cups while the weekdays and the trend stay; the trend adds about 1.5 cups in eight weeks under a 4.7-cup wobble; series = trend x season x wobble, as Friday's S10 reads the stall |
| F2 | How wrong on what it never saw? | Stall: the fourteen days of 1 to 14 February 2025 with the hidden days shaded and each day's miss. Case: the 104 weeks with the hidden weeks zoomed | Stall: the last day naive may see, day 7 to 11. Case: the rule select and the split slider, 52 to 91 | Stall: from day 11, misses of -10, +5 and 0, MAE 5.0 cups, a lean of 1.7 short, Rs 150 priced. Case: festival-aligned and finance's rule 6,615, the house bot 9,831, drift 14,842, naive 14,923, the vendor 16,400; the board of each rule's MAE, weeks too high and priced misses at the day's split |
| F3 | Where does a yearly copy put Diwali? | Stall: 13 October to 2 November 2025 against a copy of the same weekday some weeks back. Case: the 2025 festive weeks above the bot's and festival-aligned's 2026 forecasts | Stall: the copy's reach, 50 to 53 weeks back, opening at 50. Case: Diwali's 2026 week, 19 October to 9 November, opening on the case's own week of 2 November; the 2026 forecasts draw only after the prediction | Stall: 52 weeks back puts 2024's Diwali week a week late, 100 cups where 44 sold and 40 where 110 sold, 41.1 a day at worst 71, against 6.5 at worst 13 for 51 weeks back. Case: the bot peaks on 5 October, festival-aligned on 19 October; booking by the bot costs Rs 111.6 lakh if demand follows festival-aligned |
| F4 | Where should the plan sit when being short costs more? The note under the heading says the scene goes beyond Friday's five topics | The average cost of the week of 19 October's misses against the plan's distance above the forecast, with the thirteen misses beneath | Two cost sliders, an idle packer-shift Rs 500 to 800 and a late shipment Rs 15 to 40 | 0.82 of weeks; the 0.82 point 2.6 percent, covering 10 of 13; 446,236 shipments and 3,719 shifts for 19 October; 20,275 shifts, 515 above 19,760; the curve's own low at the 11th sorted week, 2.7 percent, 2.8 on the grid; about Rs 1.4 lakh from 2 to 4 percent against Rs 2.1 lakh at the forecast |
| S1 | Does the method survive a change of company? | The week's methods on the left and the chosen unit's card on the right | The unit select lights the methods the unit leans on and fills the card; the textarea writes the learner's own line | The method stays; the metric, the constraint and the cost of an error change |

## Which deck slide calls which scene

Every day's deck names its scenes in the slide's notes fence (spine section 11). Read from the five
rebuilt decks on 13 October 2026; Saturday's deck reopens the home screen.

| Day | Slide, and the scene it calls |
|---|---|
| Mon | half1 S2's and S4's notes, the home screen; S10's notes (SECTION 1) point to M1 as chapter 7's, and S67 (SECTION 8) runs it; S17's notes (SECTION 2) point to M2 as chapter 9's, and S75 and S80 (SECTION 9) run it; S28 (SECTION 3), on the case's weekly data, M4; S33's notes (SECTION 4) point to M3 as chapter 9's, and S81 (SECTION 9) runs it |
| Tue | half1 S2, the home screen with T1 to T3 named; SECTION 4's opener, S33, S34 and S35 T1; S39 and S40 T2; half2 SECTION 8's opener, S74 and S76 T3, on its drivers question |
| Wed | half1 S2, the home screen; on the canteen set, S13 (SECTION 2) W2, S19 (SECTION 3) W1, S24 (SECTION 4) W3 and S33 (SECTION 6) W5; on the case set, S41 (SECTION 7) W2, S47 (SECTION 8) W1 and S49 (SECTION 8) W3; half2 S63 (SECTION 10) W5 on the case set and S66 (SECTION 10) W4 |
| Thu | half1 S2, the home screen; SECTION 3's opener Th2; SECTION 6's opener and S47 Th1; SECTION 7's opener and S58 Th3; half2 S78 and S80 (SECTION 9) Th4 |
| Fri | half1 S2, the home screen; S4 and S8 (SECTION 1) F1; on the stall set, S19 (SECTION 2) F3 and S24 (SECTION 3) F2; on the case set, S46 (SECTION 5) F3, S50 (SECTION 6) F2 and half2 S3 (SECTION 7) F3; the fallback deck's S11 F4 |

## Where the numbers come from

| Day | The day's numbers, with their place in the sources | Derived on the page | Toy, with no facts id yet |
|---|---|---|---|
| Mon | The ticket table: 118,000 and 146,300 hours, 224,200 and 230,900 trips, 0.86 and 0.73, 0.04 and 0.09, 0.22 and 0.38, 4.8 and 4.6 minutes, 0.11 and 0.10, Rs 1.9 crore; the floor of Rs 300; the twelve rows' table; M4's twelve weekly ratios, Monday's facts (`acceptance_2026_MM_DD`, `rs_per_hour_2026_MM_DD`); the north star's 35.76 and 35.89 (`north_star_before`, `north_star_after`) | Rs 82 of top-up per trip; every value in M3's readout and reveal, computed from the rows; M4's turns | M1's response curve between and above the case's two floors, and its 1.83 at Rs 100; M2's dots, wait, top-up and acceptance under the three other paid numbers, and its guardrail lines of 0.80 and Rs 40 |
| Tue | Tuesday's facts: slide A's nine tiles (`cluttered_slides.A_dashboard`, each tile with its ids), `fare_avg_rs`, `rs_per_hour_before` and `rs_per_hour_after`, `saving_low_lakh` and `saving_high_lakh`; Monday's 6,360 and 6,500 active driver-weeks; Tuesday's facts for T3, each leaf with its low and high ends: `hyd_people`, `weekday_ride_share`, `evening_share`, `peak_window_hours`, `trips_per_busy_hour`, `idle_share`, `buffer`, `india_people`, `upi_active_users`, `upi_payments_per_day`, and `upi_month_total`, `upi_month_value_lakh_crore` and `september_days` | T3's running results, swings and checks, which reproduce `requests_per_evening_hour`, `trips_per_online_hour_chain`, `drivers_before_buffer`, `drivers_at_peak_central`, the twelve `swing_*` values, `driver_hours_per_trip_before`, `chain_over_case_per_trip`, `drivers_at_case_tph`, `upi_per_day`, `upi_month_over_31`, `upi_estimate_gap_pct` and `upi_value_per_payment_rs`; Rs 5,817 and Rs 5,861 a driver-week | None |
| Wed | Wednesday's facts by id: the canteen's twelve orders (`toy_canteen_*`: the items' counts, the three pairs of 3, the thirteen pairs with their orders and lifts, the floor of 3, the 1.5 bar and the month's floor of 8); the case's 40,000 carts, milk 71 and bread 34 percent, bread and milk's 10,064, 9,656, 0.74 and 1.04, the 50 common items' bands, the twelve carts (`twelve_rows`), 60,000 views and their range, 1.2 and 6.4 percent click-through, milk's shares of the three slots, the add rate and the margin with their ranges, the nine pairs, the 246 pairs and 4 strong, ice cream with chocolate sauce on 100 carts against 22 | Lift, confidence, the expected overlaps and the counts at any setting; each slot's rupees and the strip's day and month; the floors that keep the same pairs | None; W4's four options are Wednesday's S65 cards |
| Thu | Thursday's facts: the cohort sizes, `m1_*`, the triangle's cells, the dashboard's 38.2 to 37.8 (`dashboard_jun` to `dashboard_sep`), `everyone_sep` 35.9, `oct_sale_m2_assumed` 20.5 with 17 to 24 and `oct_dashboard_estimate` 32.9, the September funnel (`sep_sessions_*`, `sep_members_*`), `sep_menu_sessions_no_search` 38,932, `search_to_menu_searched_sep` 89 percent, the release's figures; the gym (`toy_gym_dashboard`, the same numbers as `toy_blend`) | The dashboard and October's blend from the cells and sizes; the funnel's counts with the carousel left out (39,766, 31,748 and 20,477 sessions; 43,470, 24,183, 21,501 and 17,124 members), recounted on 13 October 2026 from `data/C2_W04_D04_events_STUDENT.csv.gz` to the digit | Th4's other weeks, the 100,000 launch cohort and the weekly 20,000; its week-four 24 and 36 are `toy_ai_cohorts` |
| Fri | Friday's data: the 104 weeks of `weekly_shipments` and the vendor's 114 rows; Friday's facts: the weeks and Diwali dates, `training_weeks`, `holdout_weeks`, `per_shift`, the costs and ranges, `growth_factor`, the alignment band, `aligned_nogrowth_mae` 10,575, and the stall (`toy_stall_*`, `toy_ch1_left_spread`, `toy_ch3_*`, `toy_ch2_window_*`) with its daily record from `data/C2_W04_D05_chai_stall_daily_STUDENT.csv` | Every rule's forecast, MAE and priced miss at any split; F4's cushion, plan and cost curve; the map's 19,760-shift plan (`base_shifts_total`); the stall's copies at any reach and naive from any day | F1's wobble, a seeded draw on the stall's 4.7-cup spread |
| Sat | Rohan Desai's "twenty times more one way than the other" (`docs/07_Client_Zero.md`); Kalpa Health's six US metro areas billed in dollars; the brief lines of spine section 10 | None | None |

The reveals still written as text are M1, M2, T2, Th1, Th2, Th3, Th4, S1 and the case sets of F2 and
F3, each quoting its day's numbers; on 13 October 2026 every number on the page, in both sets of
every scene, opened and revealed, was matched against the five facts files, and the ones that match no
id are the derived and toy values in the table above.

## What the build decided where the spine or the facts files left a choice

| Choice | What the page does | Why |
|---|---|---|
| Which day sections show | A day button opens its own section and every earlier one | The map lights every earlier node, and the sweep reaches every control only if the last day button opens all six days |
| The prediction gate | Until a prediction is made, a control puts itself back, re-draws, outlines the prediction in rose and asks for it; the reveal stays shut; the set select never waits | The task of 13 October 2026 asked every reveal to wait behind its prediction; a learner who drags a slider first has read the answer off the drawing |
| Two sets in one scene | W1, W2, W3, W5, F2 and F3 open on the day's invented example and switch to the case, and the select names the chapters each set serves | Their decks call them from a concept chapter, where the case's numbers come later, and again from a case chapter; one scene per chapter would double the page's scenes |
| The prediction form | Lettered choices in twenty-six scene sets, with the key on A seven times, B nine, C six and D four; a guess slider with a lock in W5's two sets | No key sits on one letter, and none is its scene's longest option except T1's, whose four choices are Tuesday's S34 word for word, where the deck's own key is the longest (checked 13 October 2026) |
| Option letters | Where a scene repeats a deck vote, its letters and key are the slide's: T1 and Tuesday's S34, M2 and Monday's S75, W2's canteen and Wednesday's S12, W4 and Wednesday's half2 S65, Th2 and Thursday's S21, F2's case and Friday's S51, F3's case and Friday's half2 S3 | A trainer reads the room's letter straight into the scene |
| M2's fourth choice | The share of offers accepted stands where S75 offers enrolled drivers, and the reveal says why the dots cannot draw enrolled drivers | A fourth toy behaviour would add invented numbers with no facts id |
| Opening states | Every scene set opens before the state its prediction asks about: F3's stall opens 50 weeks back, a week short of the aligned copy whose 6.5 and 13 the deck reaches after the calendar copy's miss; T3's UPI tree opens on the worked chain with the published figure held for the reveal; F2's stall opens from day 7; M3 holds its before and after values, and F3's case its 2026 forecasts, until the prediction | A drawing that shows the answer first turns the prediction into reading |
| T3's questions | Chapter 8's drivers chain first, the deck's own leaves and ranges, and the UPI drill second, labelled for after the pairs drill | The deck's S74 asks for a slider per leaf and S76 for the trips-per-person slider end to end; the first pass's drivers tree and its 656 drivers online, counted over 180 weekday peak hours, contradicted Tuesday's 252 peak hours and left the tree |
| The reveal's check line | Says the controls now show the invented example's own state, the case's own state, or, where the final state is the asked one, that state (F1, T3) | A learner who missed the jump took the drawing for their own setting (the third pass's walk) |
| Th1's October | An estimate on amber, each older cohort sliding another 0.3 points and the August cohort entering at 20.5 percent, with the 17 to 24 range | The day estimates October this way and names the assumption as one |
| Th1's everyone-count | The reveal gives September's 35.9 alone | June's 40.9 is the same quantity and value as Kalpa's planted August blend |
| Th3's carousel left out | From menu view on, the counts keep only member sessions that included a search | The day's fix counts menu views among sessions that searched (89 percent) |
| Th4's blend | Later weekly cohorts of 20,000, so the blend sets its record in launch week, dips and is back near it by week eight | The day's transcript says weekly actives are still near the launch-week record two months on |
| F2's case | Six rules, the vendor scored only from 22 June 2026, every other rule from any split with the day's 4 percent, and the board at the day's split, priced once | The fix pass took out the column that raised each rule to its own 0.82 point, since Friday's main decks leave the plan quantile to the fallback session |
| F3's case | Opens on the case's Diwali week of 2 November with half2 S3's question; the readout states festival-aligned's eight weeks against both 2025 windows; at the last stop the week outside the alignment band is ringed and explained | The fix pass moved the question onto S3's vote and took the two windows' table out of the reveal, since half2 S5 asks the room to predict it |
| F4 | Marked on its jump button and under its heading as beyond Friday's five topics, the fallback session's plan quantile; the map's Friday finding is half2 S7's plan of 19,760 packer shifts | Friday's half2 S7 and S8 leave the quantile beyond the row |
| F4's numbers | The caption and the reveal are written from the block at the case's costs; the back-test line quotes festival-aligned with no growth, 10,575 a week, and the looseness reads the cost curve's own low at the 11th sorted week | Friday's half2 S5 quotes the 10,575 a planner in September 2025 could have had, and notebook 07 now names the curve's 2.7 percent where the first build had a 4.1 percent reading |
| F4's idle slider | Set in rupees an idle packer-shift, Rs 500 to 800 in steps of 10 | The case states the idle cost per shift, and Rs 5.42 a shipment is not on a grid a slider of rupees a shipment can step through |
| S1's map | The week's five methods on the left, the unit's card on the right | The home map's nodes become the methods that stay, and the card shows what changes |
| Motion | CSS transitions and one CSS animation, switched off under reduced motion | Motion explains the mechanism without changing the page between the sweep's reads |
| Toggle labels | Every toggle keeps its label and carries its state in `aria-pressed` | The WAI-ARIA authoring practice for toggle buttons |
| Light theme only | The house companion look, tuned for a projector | The house library carries no dark theme for drawings yet |

## What the first pass's two reviews found and what changed

Two fresh reviewers, who wrote findings and edited nothing, walked the page while it was being fixed:
a fresh graduate meeting each scene cold (43 rows at commit fcf106f) and a rigor and numbers pass (32
number findings). Their reports sat in that session's scratchpad as `walk_fresh_graduate.md` and
`review_rigor.md`.

| Where | What the reviews found | What changed |
|---|---|---|
| W1 | The reveal's bands of 0.80 and 0.70 with an overlap of 0.30 cannot happen | Bands of 0.70 and 0.50; the readout prints the range the overlap can take |
| T2, W2, T3, Th2, Th3, W3, S1 | A drawing, caption, myth line or header printed the answer before the prediction | Each opened before its answer |
| Th1 | The reading was unstated, the blend drifted, the slider never moved the dashboard | Reading stated, October added, the slider resizes the August cohort |
| F2 | The vendor priced cheapest with nothing reconciling it | The raised baseline priced in prose and on the board |
| M3 | The four drivers "1.90 to 1.89" compared six drivers with four | 1.98 to 1.89 for the four, and the shrinking-base rise named |
| M1, M2, M4 | The top-up's base, the guardrails' lines, the ring's meaning, the dots' scale and the north star were loose | Each stated on the page |
| W4, W5 | A partner at chance earned a full slot; milk's toy lifts sat in Kalpa's band | The fourth pass replaced both scenes' toys with Wednesday's facts |
| T3 | The drivers' check compared different units | The fourth pass rebuilt the tree on Tuesday's chain and its like-for-like check |
| F1, F3, F4 | Overstated reveal arithmetic, an unlabelled toy panel, a clipped legend | Each fixed; F1 and F3's stall sets now carry Friday's own example |
| The map | "Five companies" counted Uber twice | Four companies |

Declined, with the reason: lighting a later day prints the earlier days' findings on the map, as spine
section 1 asks; M1 asks about Rs 250 while the case's floor is Rs 300, as spine section 11 fixes; toggles
keep their labels.

## What the third pass's two reviews found and what changed

Two fresh reviewers read the eight rebuilt Thursday and Friday scenes at commit d1f3019: the rigor pass
(16 findings, none wrong) and the fresh graduate (40 findings, none blocking); their reports sat in that
session's scratchpad as `review_rigor_pass2.md` and `walk_fresh_graduate_pass2.md`, and commit 23634c7
carries the fixes: F2's board at the day's split with every rule raised to its own point, the rules
defined in the prompt, one scale for every rule, the vendor's fit drawn dashed; F3's ringed last stop and
its what-if wording; F4's ringed lowest point; Th1's caption and prompt; Th3's unit header; Th4's labels;
and the check line on every reveal. Declined: phone-width labels, Th3's platform split, the dashboard's
own name for month-two retention, Th2's fixed scale, Th3's toggle wording, sums above Rs 100 lakh in
lakh, F4's 82 in 100 before its derivation, F4's rescaling axis and F2's label outside its block.

## What the fourth pass changed, scene by scene

| Scene | What changed | Why |
|---|---|---|
| The home map | Each day's box carries its row subtopics, numbered, verbatim and in order; a legend says what each line means | The task of 13 October 2026, step 1 |
| Every scene | Controls and the reveal wait behind the prediction | Step 2 |
| W1, W2, W3, W5 | The tea stall retired; each opens on the hostel canteen's twelve lunch orders, Wednesday's chapters 1 to 6, and switches to the case for chapters 7, 8 and 10 | Wednesday's toy changed in the rebuild, and the deck calls these scenes from both kinds of chapter |
| W4 | Rebuilt on Wednesday's strip: milk's share of each slot's views, the add rate and the margin across their ranges; the toy partners gone | The deck's S65 and S66 price the strip this way |
| Th2 | The coaching centre's batches retired; the neighbourhood gym of Thursday's chapter 3 | Thursday's toy changed in the rebuild |
| F1 | The toy weekly series retired; the chai stall's own parts | Friday's chapters 1 to 4 teach on the stall |
| F2, F3 | A stall set first, Friday's chapters 3 and 2, then the case for chapters 6, and 5 and 7; titles now "How wrong on what it never saw?" and "Where does a yearly copy put Diwali?" | The deck calls them from both kinds of chapter |
| F4 | 4,034 replaced by the no-growth 10,575; the 4.1 percent reading replaced by the curve's 2.7; caption and reveal written from the block | Friday's sources list named both lines for this file |
| T3 | Rebuilt on Tuesday's chapter 8 chain, with the UPI drill as a second question | Its tree, ranges and check contradicted the rebuilt day |
| M4 | The reveal reads the weekly ratios S28 reads, Rs 310.3, 271.0 and 259.1 | Its "about Rs 314 to Rs 271" set a six-week average beside a single week |

## What the cold read found and what the fix pass changed

One fresh reader, a trainer who did not write the week, opened the page at 1,366 by 768 with the five
rows and the five decks' opening slides beside it, lit every day, walked all 21 scenes in both sets, and
wrote findings without editing; the report sat in this session's scratchpad as `cold_read_trainer.md`.
The topics were visible on every weekday and on no Saturday line, and no console error appeared. The
decks lie outside this branch's files, so a call the page cannot fix is named in the last column.

| Finding | What the reader saw | What the page now does | What a deck still needs |
|---|---|---|---|
| 1, blocker | T1's nine numbers, letters, key and rebuilt title differed from Tuesday's S33 to S35 | T1 draws slide A's nine tiles from Tuesday's facts, asks S34's question with its four pairs and key b, and rebuilds the slide in S35's four parts under S35's title | Nothing |
| 2 | Monday's S10, S17 and S33 point concept chapters at case scenes under wrong chapter labels, and M3 printed S62's 1.19 before any prediction | M3 holds its values until a prediction, and its question no longer states the fall | The notes at S10, S17 and S33 drop their pointers or name the chapters that run the scenes: M1 at S67 in chapter 8, M2 at S75 and S80 in chapter 9, and M3 at S81 in chapter 9, on chapter 7's six drivers |
| 3 | M3 offered no denominator matching S81's and printed only the six drivers | M3's denominator reads "enrolled drivers online at least one peak hour", and its reveal adds S81's 35.76 to 35.89 on the full data, so the scene stays with S81's call | Nothing |
| 4 | M2's letters, key and north star differed from S75 and S80 | M2 takes S75's first three choices in order with key c and S80's north star word for word; its fourth choice stays, as the decisions above record | Nothing |
| 5 | M1 printed S79's Rs 1.16 crore after a prediction at S67 | The readout line, the reveal's sentence and the constant behind them are gone | Nothing |
| 6 | Thursday's SECTION 3 note names a coaching centre, and Th2's A and B were swapped against S21 | Th2's choices follow S21's order and words | The opener's note, line 523 of Thursday's half1 deck, names the neighbourhood gym |
| 7 | Th1, called at S47, prints S49's and S53's numbers and the October estimate | Nothing, since the scene's answer is the blend and its estimate | The note at S47 calls Th1 at S53 or later |
| 8 | Th3, called at S58, shows S59's 61 percent per member and stated S63's finding | The reveal no longer states S60's 61 per member or S63's checkout break | The note at S58 moves the call after S63 |
| 9 | F1 added its parts where Friday's S10 multiplies them, and S4 calls F1 where every other day's concept map calls the home screen | F1 multiplies a trend in cups, each day's share of a weekday and a wobble factor | The note at Friday's S4 opens the home screen |
| 10 | F2's case vote differed from S51's letters, its select printed S54's 16,400, and its reveal held S56's priced order and a 0.82 column | F2's case asks S51's question with its letters and key d; the 0.82 column and the cushion sentence are gone | The note at Friday's S50 opens F2's case set after S56 |
| 11 | F3's case printed half2 S4's answer before any prediction, and its reveal held half2 S6's table | F3's case asks half2 S3's question with its letters, draws the 2026 forecasts only after the prediction, and its reveal no longer holds the two windows | Friday's half1 S46 note drops its F3 call, and half2 S3's note opens F3 after the vote |
| 12 | The map's Friday finding and F2's and F3's reveals carried the fallback's 0.82 plan | The finding reads half2 S7's 19,760-shift plan, F4 says it goes beyond the five topics, and no other scene cites F4 | Nothing |
| 13 | Option letters differed where a scene repeats a slide's vote | Letters and keys follow the slide in W2's canteen set, W4, Th2, F2's case and M2's first three choices | Nothing |
| 14 | Calls sit on answer slides: W1 at S19 and S47, W2 at S13 and S41, W3 at S24 and S49, M4 at S28, F3's stall at S19, and T2 at S40 | Nothing | Each call moves to the prediction slide before it |
| 15 | Notes describe scenes wrongly: Wednesday's S33 names W5 for S34's sort, half2 S66 describes W4 by ranks, and Friday's S19 names a festival marker | W4's toggle reads "Rank by lift: take milk out of the strip", so S66's words fit | Wednesday's S33 call moves to S34, and Friday's S19 note names the copy's reach |
| 16 | Saturday's box carried no topics, and no Saturday file calls S1 | Saturday's nine interview anchors open under the map | A Saturday file calls S1 beside the transfer briefs |
| 17 | Scenes run taller than the screen, the map's topic lines print at about 11.7 pixels, W1's overlap slider snapped back and printed "1 orders", and the Monday ticket said "weekday peak window" | W1's overlap slider runs only across what the bands allow and says "1 order"; the Monday ticket says "a whole peak window, two a day of three hours each", as Monday's deck does; the heights and the line size stay | Nothing |

## The sources' contradictions, and what settled each

The first pass found eleven places where the case file or the spine disagreed with itself. Pull
requests 232, 233 and 239 settled them in the case file and the spine, and the merged day packs carried
them into their data: Monday's twelve rows read 114 to 88 and 1.90 to 1.19; the Rs 1.16 crore is paid to
driver-weeks accepting under half their offers; Tuesday's per driver-week reading rose on bookings up 3
percent against driver-weeks up 2.2; Wednesday's milk sits on half the slot impressions; Thursday's
dashboard counts members from their month two, its twelve rows and its 53,089 members were corrected,
and Kalpa's planted fall now reads 83.3 to 63.6 percent; Friday's hold-out is thirteen weeks from 29
June with every forecast made from 22 June, its calendar runs 114 weeks, a late shipment costs 4.6 times
a spare one, and the 2025 back-test tests placement (S5 of Friday's half2: 58,250 for the bot against
10,575 for festival-aligned with no growth); the map counts four companies. The orchestrator kept W5's
0.25 percent and Th3's 64 percent beside Kalpa's planted values of other quantities, and the phone-width
labels, on 13 October 2026.

## The proofs

### The browser sweep

The sweep's last lines on the page of 13 October 2026, with the pre-installed Chromium at
`/opt/pw-browsers`:

```
      C2_W04_D01_week_explorer_STUDENT.html: 190 controls clicked, 0 inert, 6 not visible in the opening state, 0 console errors
RESULT: PASS (0 failures)
```

The six controls not visible in the opening state are the second set's own controls (F2's rule select,
T3's UPI sliders and the like), which the sweep reaches by switching the set. A headless walk opened
every set of every scene, tried the reveal before predicting (it stayed shut in all 28), predicted,
revealed and read the text back, with no console error; the fix pass ran the same walk again with the
same result. The page is plain ASCII at about 331 KB, under
the spine's 400 KB, with no URL, no external file, no storage call and no network request.

### The plant grep

A scratch script opens the page, reveals every scene in every set, and searches the rendered text, the
drawings' labels and the `W4` block for each planted Kalpa value in the forms a reader would see: the
`plants` blocks of Monday's and Thursday's facts files, the PLANT entries of Wednesday's `kalpa_lab`
(bands included) and every value of Friday's `kalpa` block, matched at one decimal of a percent, and for
shares of 0.1 or more also at a whole percent and at two decimals. Every hit but W5's is a different
quantity, mostly on another day, and none reveals what a lab room is meant to find:

| The hit | Where | Why it stays |
|---|---|---|
| 0.82, sixteen times | F4 | Friday's plan quantile in the scene marked beyond the five topics, beside Wednesday's Kalpa charger confidence |
| 0.84 | M2's toy acceptance | Beside Kalpa's charger share of 84.5 percent |
| 0.85, twice | M3's twelve rows | Drivers B's and F's acceptance before the launch, beside the top of Kalpa's charger confidence band |
| 0.24 | W1's and W3's case sets, and a comment in the block | Chance's 0.34 x 0.71 for bread and milk, beside Kalpa's checkout per member of 24.5 percent |
| 24 percent | M1, M3, T1, Th1, Th4 | Monday's rise in hours, slide A's +24 percent tile, the day's 17 to 24 range and the AI toy |
| 0.25 percent | W5's case set | Wednesday's case number and the same quantity as Kalpa's thin pair, kept by the requester on 13 October 2026 |
| 64 percent | Th3 | Thursday's checkout start to order, kept on 13 October 2026 |
| 31 percent | The Thursday ticket | The August cohort's month one, beside Kalpa's 30.9 percent skipping search |
| 7.8 percent | F4's reveal | Festival-aligned's largest hidden-week miss, beside Kalpa's checkout per session |
| 1.2 and 3.8 percent | Wednesday's ticket, W4 and F1 | Click-through, and F1's wobble axis at 1.2, beside Monday's Kalpa ratio of 1.22 and Friday's Kalpa mean error of 3.8 percent |
| 1.4 and 1.6 | F2, F4, M1 | The vendor's 1.4 percent fit and Rs 1.4 lakh; the city's 1.9 to 1.6 trips an hour; beside Kalpa's October ratios of 1.45 and 1.56 |
| 0.2 percent | F4 | The cost curve's grid step, matched by rounding Kalpa's 0.25 percent |

### The writing checks

| Check | Scope | Result |
|---|---|---|
| The style sweep inside `verify.py` | The page and these notes | Pass |
| `tic_scan.py` from the llm-tic-scrubber skill | The twelve rebuilt scenes rendered with every set revealed, 1,192 runs; after the fix pass, the thirteen changed scenes' seventeen sets opened and revealed, 3,068 runs | Clean |
| The humanizer skill's read, in file mode on prose only | The rebuilt prompts, captions, readouts and reveals | No banned word, no dash, no contrast construction; generated sentences read aloud and kept |
| Characters | The page and these notes | Plain ASCII |

### Screenshots

Taken with the pre-installed Chromium on 13 October 2026, in this session's scratchpad under `shots/`:
every set of every rebuilt scene in its revealed state, and the map at 1,366 by 768. Each was looked at;
F1's scale labels crossed its panel titles and F2's naive label sat on the line, and both were redrawn.
The fix pass looked again at T1 in all three title states, M3 and F3's case before a prediction, every
changed scene revealed, and the map with Saturday lit and its anchors open; F3's waiting line crossed
the Diwali marker and now sits on a halo.
