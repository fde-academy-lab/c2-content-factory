# Week 4 explorer: build notes, sources and proofs

**INTERNAL.** The notes behind `demos/C2_W04_D01_week_explorer_STUDENT.html`, the one interactive page
for the whole of Week 4 (spine section 11). They say what each scene draws and what each control moves,
where every number comes from, what the build decided where the spine left a choice, what the two
reviews found and what changed, where the sources disagree with themselves, and what the proofs returned.

## How the page is built and checked

| Step | Command or place | What it does |
|---|---|---|
| The house look and the diagram builders | `python3 scripts/build_companion.py content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html` | Fills the page's `<style data-c2kit>` and `<script data-c2kit>` blocks from `scripts/companion/`; T3's two trees are drawn by `C2K.driverTree` |
| Every number | The `W4` block in the page's head | One constants block, each value with its source in a comment: the case file or the spine for case numbers, "derived" for arithmetic on them, "toy" for invented values that the page labels toy where they appear. Drawings and readouts compute from the block; the reveal sentences quote the case's numbers as text, so a changed value is edited there by hand too |
| The browser sweep | `python3 scripts/html_sweep.py content/W04/D1/demos` | Clicks every control in DOM order and fails on a control that changes nothing, a console error or a covered dropdown |
| The day gate | `python3 scripts/verify.py content/W04/D1` | The layout, naming and writing rules, then the sweep |

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
| M1 | Can online hours rise while riders wait as long? | A city of twelve zones with sixty driver dots that drive, idle or sit offline, a picture with no scale | The floor slider, Rs 0 to 400 in steps of 20, moves dots online and into the outer zones and moves online hours, trips, trips per online hour, the idle share, the total top-up, the part paid to driver-weeks accepting under half their requests and the dot counts; the rider-wait toggle shows the wait meter and its minutes | At Rs 300: 118,000 to 146,300 hours, 224,200 to 230,900 trips, 1.90 to 1.58, Rs 1.16 crore of Rs 1.9 crore to driver-weeks accepting under half their requests, wait 4.8 to 4.6, and 1.83 already at Rs 100; trips per online hour = trips / online hours |
| M2 | Which number should the scheme pay for? | A seesaw of the paid number against three guardrails, above the same sixty dots | The select of four paid numbers re-places the dots, tips the seesaw, flips the guardrail chips and moves the dot counts, the idle share, the wait, the top-up per trip and the acceptance share, against guardrail lines printed in the readout | Trips with an acceptance floor puts 40 of 60 dots to driving against 31; which line catches which way of gaming; the definition's lines, with the north star defined |
| M3 | What does one line of a definition change? | The twelve driver-weeks as a table, with a before and after bar | Four selects (numerator, denominator, window, exclusions) recolour the columns, strike excluded rows and move the before, after and change readouts; the window select prints the counts it divides | Per online hour 1.90 to 1.19, per enrolled driver 19.0 to 14.7; the acceptance exclusion compares six drivers with four (the four alone fall 1.98 to 1.89) and, with enrolled drivers, turns the fall into a rise, 19.0 to 20.8; a definition names numerator, denominator, window, exclusions and what it does not reward |
| M4 | Which number moved first? | Acceptance share and bookings per online hour over twelve weeks, the launch marked | The week slider, 1 to 12, draws both lines to that week, rings each turn and moves the week's values and the turn readouts | Acceptance turns in week 7, bookings in week 9, a lead of two weeks; a leading indicator moves before the outcome it leads |
| T1 | What is left when the slide says one thing? | A slide with nine of Monday's numbers under a topic title | Nine checkboxes fade tiles, count the numbers left and rewrite the title when two remain; the warden test, defined in its readout as whether a reader outside the field could act on the title alone, prints its verdict on the current title | Trips per online hour and the top-up carry the claim; acceptance and cancellations show the gaming without its cost, so they go to the appendix; claim, evidence, caveat, action |
| T2 | Which denominator is the slide using? | The same bookings over three denominators as indexed bars | The select draws the chosen reading's bars; a reading not yet chosen stays a dashed outline; the select also moves the slide title and the before, after and change readouts | Rs 314 to Rs 260 per online hour, per driver-week up 3 percent on a toy count that leaves out the 140 joiners, per trip flat at Rs 165; bookings per online hour = trips per online hour x fare |
| T3 | How big is a number nobody has measured? | Two guesstimate trees, UPI payments a day and drivers at the evening peak, each titled as a question | The select moves the focus between the trees; six sliders move the factors, the products and the anchors' lines; the UPI anchor and its ratio print at the reveal | 802 million a day in September 2026 (776 million over 31 days); drivers at peak: to be found, with the case's 656 drivers online before the launch named as a different unit; on these ranges peak requests moves the drivers' estimate most; clarify, map, calculate, validate |
| W1 | Why is lift a ratio of two areas? | A unit square with two bands and their overlap, the observed overlap beside it | Three sliders, P(A), P(B) and the observed share, in steps of 0.01, move the bands, the areas, observed over expected and the range the overlap can take at those bands | Bands widened to 0.70 and 0.50 at a fixed 0.30 overlap give lift 0.86; at 0.80 and 0.70 the overlap is forced to at least 0.50; the tea stall's 1.25; lift = P(A and B) / (P(A) P(B)) |
| W2 | What does confidence throw away? | A hundred carts in the case's proportions, with a legend for bread, milk, both and neither | Two filter buttons and a reset move carts to the right or fade them and move the counts | 34 carts left, 25 with milk, 25 / 34 = 0.74 against milk's 0.71, lift 1.04 as W1's ratio of areas; confidence = P(A and B) / P(A) |
| W3 | Why does the item in every cart look like the best partner? | The square with bread and milk, and two gauges | The milk-share slider, 0.10 to 0.90, moves milk's band, the overlap, confidence, lift and the carts holding both | At 0.71, confidence 0.74 and lift 1.04, with the held-lift assumption stated; confidence follows popularity, lift divides it out |
| W4 | What does a strip slot earn? | A cart page with three slots under a cart holding chips | The rank toggle swaps milk's slot for dip's; three sliders move every slot's rupees and the strip's day and month totals | Rs 3,240 against Rs 17,280 a day, about Rs 4.2 lakh a month for one slot; value = views x click-through x add rate x margin |
| W5 | Where should the support floor sit? | Lift against support for nine pairs on a log scale, filled dots for the case's numbers and open dots drawn inside its band | A guess slider and lock record the prediction and then lock; the floor slider, 0.1 to 5 in steps of 0.1, moves the floor line and the counts | Eight of nine survive 1 percent; ice cream with chocolate sauce, about four carts a day, goes on a watch list; any floor from 0.3 to 2.9 percent keeps the same eight; act above the floor, watch below it |
| Th1 | How can every batch shrink while the average stays flat? | The cohort staircase filling month by month under the dashboard's line, with October as a labelled toy month | Next month adds a column up to October, then starts again from February; the slider resizes the August sale cohort and moves its row, the counted members and October's reading | 38 from June to September while every row falls and the sale cohort sits outside the count; 34 in October as it enters at 2.6 times normal, 36 at normal size; counted from the first month, September would read 36; blend = sum of size x rate / sum of sizes |
| Th2 | What is the flat number made of? | Two months of a coaching centre's batches, stacked by size, opening before batch B joins | Batch B's size, from 0, and batch A's rate move the stacks and the blended share | 250 of 500 is still 50 percent; the weighted average written out |
| Th3 | Which stage owns the loss? | The order flow as bars whose lengths are the counts, opening with the carousel's menu opens left out | The unit toggle and the carousel toggle swap the counts and move every step's rate | 118 percent search to menu view per session; 34 and 61 percent menu view to add-to-cart; the loss at add-to-cart to order on Android; each step divides by the step before in one unit |
| Th4 | Is it novelty or habit? | A launch cohort against an organic cohort over eight weeks, and the blended actives since the launch | The week slider draws both curves to that week; the blend toggle shows the blended line | At week four the launch cohort keeps 24 percent and the organic 36; the blend bottoms at 36,600 in week five and climbs to 42,900 by week eight; judge each cohort at the age where habit shows |
| F1 | What is a series made of? | Trend, season and noise panels on one scale, summed into one series over two labelled years | Three sliders move their panels, the series, its highest and lowest weeks and the trend's rise | The season's peaks and troughs move 25 thousand; on this noise the highest week goes from 255 to 277 thousand and the lowest from 167 to 146; series = trend + season + noise |
| F2 | How wrong on the weeks it never saw? | The 104 weeks with the hidden weeks shaded, and the hidden weeks zoomed with each week's error | The method select and the split slider, 52 to 91, move the forecast, the sticks, the method's description, the MAE, the priced errors and the scoreboard | MAE 21,000, 9,200, 8,900 and 14,800; priced, the vendor Rs 10.9 lakh, the baseline Rs 18.6 lakh and the baseline raised for the costs Rs 10.9 lakh, with the no-festival caveat; MAE = mean of absolute errors on held-out weeks |
| F3 | Where does the house bot put Diwali this year? | The toy series' 2025 festive weeks above two 2026 copies on the same calendar weeks | The Diwali slider, the weeks of 19 October to 9 November 2026, moves the 2026 marker and the festival-aligned copy while the bot stays; the readout says when the slider sits on 2026's own week | The bot two weeks early at the 2026 date; festival-aligned copies the week at the same distance from the festival |
| F4 | Where should the plan sit when being short costs more? | The idle, late and total expected cost against the plan's distance from the forecast, scaled to the tallest curve | Two cost sliders, opening at the case's Rs 5.4 and Rs 25, move the curves, the minimum, the weeks covered, the packer shifts and the expected costs | The 0.82 quantile, a plan that covers about 82 weeks in 100, about 10,300 shipments and 86 shifts above the middle; plan quantile = under-cost / (under-cost + over-cost) |
| S1 | Does the method survive a change of company? | The week's methods on the left and the chosen unit's card on the right | The unit select lights the one or two methods the unit leans on and fills the card; the textarea writes the learner's own line into the map | Each unit leans on one or two methods, which come across unchanged; what changes is the metric, the constraint and the cost of an error |

The day decks name the scene each slide calls in the slide's notes fence (spine section 11); the decks
were not built when the page was, so the slide-to-scene list belongs to the week read.

## Where the numbers come from

The five day facts files did not exist when the page was built (this session ran on the day the spine
was approved), so every case number comes straight from `docs/detailing/W04_case_file.md` and
`docs/detailing/W04_analyst_craft_spine.md` as approved on 12 October 2026. When the facts files land,
the week read swaps the `W4` block's values for the facts files' values by id and edits the reveal
sentences that quote them.

| Day | Case numbers, with their place in the sources | Derived on the page | Toy, labelled toy on the page |
|---|---|---|---|
| Mon | The ticket table: 118,000 and 146,300 hours, 224,200 and 230,900 trips, 0.86 and 0.73, 0.04 and 0.09, 0.22 and 0.38, 4.8 and 4.6 minutes, 0.11 and 0.10, Rs 1.9 crore; L5's Rs 1.16 crore; the floor of Rs 300; the twelve rows' table | Rs 82 of top-up per trip (Rs 1.9 crore over 230,900); the four drivers' 1.98 to 1.89 and the enrolled base's 19.0 to 20.8 from the rows | The response curve between and above the case's two floors; the dots' behaviour, wait, top-up and acceptance under the three other paid numbers; the guardrail lines of 0.80 acceptance and Rs 40 a trip; the twelve weekly values of M4, set around the case's six-week figures |
| Tue | Rs 314, Rs 260 and Rs 165 (ticket); 24.07 billion and 802 million a day (T3, NPCI through Outlook Money, checked 12 October 2026) | 776 million over 31 days; 656 drivers online in an average peak hour before the launch (118,000 hours over 180 peak hours: 5 weekdays, two windows of three hours, six weeks); per driver-week up 3 percent | The 6,000 driver-weeks behind the per driver-week reading; every factor in the two guesstimate trees, which the learner sets |
| Wed | 71 percent milk, 34 percent bread, 0.74 and 1.04 for bread to milk, 0.73 and 1.03 for eggs, 5.0 percent and 3.4 for chips with cold drink, 0.25 percent and 4.6 for ice cream with chocolate sauce, the milk band of lifts near one (the case file's 0.96 to 1.08, used to place pairs and no longer printed), 1.2 and 6.4 percent click-through, 60,000 views, 0.5 add rate, Rs 9 margin, 40,000 carts | The hundred carts (25, 9, 46, 20) in the case's proportions; each pair's support from share times confidence; Rs 17,280, Rs 3,240, Rs 14,040 and Rs 4.2 lakh | The tea stall (R1); peanuts, dip and namkeen beside chips; milk's 0.75 and 1.06 beside chips, inside the band; the other milk pairs at lifts 1.03 to 1.07 |
| Thu | Month-one retention 58, 56, 55, 53, 52, 50, 49 and 31; 5,000 a normal month and 2.6 times for August; 38 percent flat; 118, 34 and 61 percent; 58 to 44, 57 and 52 for the checkout | The blend from the cells and the sizes, and September's 36 under the first-month count | The cells after month one, built to hold within 0.15 of 38.0 from June to September; the sale cohort's month-two 24 percent and the October month; the coaching batches (R1); the funnel's counts; the AI app's two cohorts |
| Fri | The 104 weeks' dates; Diwali on 31 October 2024, 20 October 2025 and 8 November 2026 (F5, `facts.yaml`); 120 shipments a shift; Rs 650 and Rs 25 with their ranges; the MAE table; 4 percent a year of drift; the festive shape | Rs 5.4 a shipment; the 0.82 quantile; 10,300 shipments and 86 shifts; Rs 0.88 and Rs 1.35 lakh a week; the priced errors, the raised baseline's among them | The 104 weekly values, built to the case's shape and solved so the last 13 weeks score 21,000, 9,200, 8,900 and 14,800; the vendor's curve at 1.10 times last year's week; the trend, season and noise of F1 |
| Sat | Rohan Desai's "twenty times more one way than the other" (`docs/07_Client_Zero.md`, stakeholder table); Kalpa Health's six US metro areas billed in dollars (decision `build1-us-data`); the brief lines of spine section 10 and the case file's Saturday table | None | None: the four company cards carry no figure and say they are hypothetical |

Finance's rule of thumb scores 9,600 in the case's MAE table and drift alone 11,500; the page draws the
four methods spine section 11 names and leaves those two to the Friday notebook.

## What the build decided where the spine left a choice

| Choice | What the page does | Why |
|---|---|---|
| Which day sections show | A day button opens its own section and every earlier one, and dashes nothing below | The map lights every earlier node, and the sweep reaches every control only if the last day button opens all six days |
| The prediction form | Lettered choices in twenty scenes, with the key on A four times, B five, C six and D five, and never the longest option; a guess slider with a lock button in W5, where the prediction is a count | The spine allows a choice or a slider guess; a key that sits on one letter or is always the longest lets a learner answer without thinking |
| Opening states | Every scene opens before the state its prediction asks about: T2 draws a reading once it is chosen, T3 holds the measured 802 million for the reveal and opens its UPI tree at 50 million a day, Th2 opens before batch B joins, Th3 opens with the carousel's opens left out, F4 opens at the case's costs, and no caption or myth line prints the answer a prediction asks for | A drawing that shows the answer first turns the prediction into reading |
| Thursday's dashboard | Counts a member from the second month after signup, says so in Th1's caption, and adds October as a labelled toy month where the sale cohort enters the count | Under the spine's first-month definition the case's flat 38 through September cannot hold (see the source list); the case's own words, "month-two retention", support this reading, and the toy October shows the cohort's size at work, the mechanism spine section 11 asks Th1 to show |
| Th1's prediction | Where October's reading lands when the sale cohort enters the count, with options 24, 34, 36 and 38 | The ticket prints the flat 38 for June to September, so the spine's "what will the blend do" is answered before it is asked unless it moves to the month the cohort is counted |
| Monday's twelve rows | The case file's table as printed, so M3's hand count is 1.90 to 1.19 | The table is the only set of rows the sources fix; the case file's own hand count disagrees with it (see the source list) |
| S1's map | The week's five methods on the left, the unit's card on the right | The home map's nodes become the methods that stay, and the card shows what changes |
| Motion | CSS transitions and one CSS animation (the driving dots), switched off under reduced motion; nothing animates by timer | Motion explains the mechanism without changing the page between the sweep's before and after reads |
| Toggle labels | Every toggle keeps its label and carries its state in `aria-pressed`, which the pressed style shows | The WAI-ARIA authoring practice for toggle buttons keeps the label fixed while the state changes; the map's toggle now follows the same rule |
| Light theme only | The house companion look, tuned for a projector | The house pages are light; a dark theme would need every drawing's colours as variables, which the house library does not carry yet |

## What the two reviews found and what changed

Two fresh reviewers, who wrote findings and edited nothing, walked the page while it was being fixed:
a fresh graduate meeting each scene cold (43 rows at commit fcf106f: none blocking, 25 slowing, 16
cosmetic, 2 scenes that simply work, plus 12 findings fixed during the walk, two of which blocked
learning) and a rigor and numbers pass (32 number findings, 19 of them in the sources, 6 arithmetic, 9
against the spec, 13 plant placements judged and 4 style points). Their reports sit in the session's
scratchpad as `walk_fresh_graduate.md` and `review_rigor.md`.

| Where | What the reviews found | What changed |
|---|---|---|
| W1 | The reveal's bands of 0.80 and 0.70 with an overlap of 0.30 cannot happen | Bands of 0.70 and 0.50 (lift 0.86); the readout prints the range the overlap can take |
| T2, W2, T3, Th2, Th3, W3, S1 | A drawing, caption, myth line or header printed the answer before the prediction | Each now opens before its answer (see the opening states above) |
| Th1 | The reading was unstated, the unrounded blend drifted 0.8 points, the slider never moved the dashboard and the steps stopped at September | Reading stated, cells flattened to within 0.15 of 38.0, October added as a toy month, slider resizes the sale cohort |
| F2 | The vendor priced cheapest with nothing reconciling it, the vendor's rule was unstated, the methods were undefined | The raised baseline priced in prose and as a scoreboard row, each method described as it is scored, the split's meaning printed |
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
| The reveal sentences do not follow the constants block (rigor) | The head comment now says so; generating reveal numbers from the block is a later engineering task |
| W1's readout labels its expected area P(A) x P(B) before the reveal (rigor) | The two areas are the scene's drawing |
| F2 prices an idle shipment at Rs 5.417 and F4 at Rs 5.4 (rigor) | No printed figure changes |
| M1 asks about Rs 250 while the case's floor is Rs 300 (walk) | Spine section 11 fixes the Rs 250 question; the reveal now quotes the 1.83 at Rs 100 |
| Toggles should flip their labels (walk) | See toggle labels above |

## Where the sources disagree with themselves

These need the orchestrator, because the case file says no session changes a target alone. The page
works around each one as stated; nothing here changed a source file.

1. **Monday's twelve rows.** The case file's table sums to 60 and 74 hours and 114 and 88 trips, a hand count of 1.90 to 1.19 trips per online hour, while the same section states 114 to 110 trips and 1.90 to 1.49, and spine section 5 says two drivers' hours doubled where E and F rise 1.6 and 1.4 times. Reaching 110 trips needs drivers A to D at about 2.4 an hour against 2.0 before. The rows also break spine section 4's margins: 1.90 before equals the city's 1.90, hours rise 23 percent against the city's 24 and the Kalpa plant's 22, and acceptance runs 0.86 to 0.74 against the city's 0.86 to 0.73.
2. **Monday's Rs 1.16 crore.** The case file computes it from "61 percent of the top-up paid to driver-weeks with acceptance under 0.5" and then calls it "paid to idle hours"; a driver-week holds busy and idle hours. The page says driver-weeks.
3. **Tuesday's per driver-week reading.** The case file says it rises "because hours rose", and hours do not enter it; with Monday's 140 drivers who joined after the launch it falls about 9 percent if every driver is active weekly. The page holds a toy 6,000 driver-weeks and says it leaves the joiners out. The case file's 1.58 x Rs 165 is Rs 261; Rs 260 needs the unrounded 1.578, which the page uses.
4. **Wednesday's ticket.** Milk on 44 percent of slot impressions at 1.2 percent and the rest at 6.4 percent blend to 4.1 percent, against the stated 3.8; one of the four numbers has to change. The page does not print the blend. The twelve rows' bread to milk confidence of 0.75 sits 0.01 from the case's own 0.74, against the case file's own margin, and the case's milk band (confidence 0.68 to 0.78, lift 0.96 to 1.08) overlaps Kalpa's charger band (0.78 to 0.86 and 0.93 to 1.02); the page no longer prints the band.
5. **Thursday's flat 38 percent.** Under the spine's definition (members who signed up before the month, counted from their first month) September cannot read 38: with the January to July cohorts at 38 and the August cohort entering at 31 percent with 13,000 members, September is at most 36.1. The case's sale cohort also enters below the blend, so it cannot prop the blend up the way the row's Kalpa plant and the Th2 toy describe. The page counts from the second month and says so; the definition, and the sale cohort's role, need settling before the Thursday pack is built, or learners will carry a reading into the lab that does not reproduce Kalpa's 41.
6. **Thursday's other numbers.** The twelve rows hold at most 5 of 12 in September (41.7 percent, 0.7 from the Kalpa plant 41); 60,000 members against eight months of 5,000 and 13,000 for August is 53,000 (at 60,000 a normal month is about 5,875 and August 2.2 times); the ticket's 58 to 44 names no unit on the day whose lesson is the unit; and the Android release on 14 September with a 14-point fall sits inside Kalpa's planted window of 10 to 30 September, one point from its 15-point fall.
7. **Friday's hold-out and vendor.** "The last thirteen weeks, beginning 22 June to 21 September 2026" is fourteen weeks; the page uses 29 June, which keeps 91 training weeks. The spine and `vendor_forecast` fit the vendor to all 104 weeks while the case's table scores it on 13 held out; a forecast scored on the hold-out has to be made from data to the week of 22 June.
8. **Friday's calendar.** It has 112 weeks, to the week of 16 November 2026, while the festive window to staff runs to the week of 30 November, which needs 114.
9. **Friday's errors priced.** On the page's toy weeks, which score the case's MAE table exactly, the vendor's errors, 12 of 13 too high, price at Rs 10.9 lakh against the baseline's Rs 18.6 lakh, and the baseline raised by 10,300 shipments prices at Rs 10.9 lakh, level with the vendor. The hold-out holds no festive week, so the case's argument for the baseline rests on a window the hold-out cannot test, and the 8,900 behind F4's plan comes from weeks with no festival. The Friday deck should be ready for a learner who spots it.
10. **Friday's wording and plant equalities.** "A late shipment costs five times an idle shift" compares Rs 25 with Rs 5.4 a shipment, 4.6 times, with Rs 650 a shift. The plan quantile 0.82 equals Wednesday's Kalpa 0.82, the 4 percent drift and the festive multiples sit inside Kalpa's ranges, and "within 2 percent" and "at least 30 percent above" copy the Kalpa vendor plant; mirroring is the design, and the exact equalities are avoidable.
11. **Spine section 1's map.** "Five tickets, five companies" counts Uber twice, and K1 "Kalpa Retail: the auto-reorder window" names the three-week window the row keeps for trainers; the page says four companies and "reorders per member", and every deck's slide two inherits the spine's wording until it changes.

## The proofs

### The browser sweep

The sweep's last lines on the final page, with the pre-installed Chromium at `/opt/pw-browsers`
(`setup.sh` was not needed):

```
      C2_W04_D01_week_explorer_STUDENT.html: 187 controls clicked, 0 inert, 0 not visible in the opening state, 0 console errors
RESULT: PASS (0 failures)
```

`python3 scripts/verify.py content/W04/D1` returned `PASS  2 files, every stem C2_W04_D01_ and every
folder valid for a teaching day`, the same sweep result and `RESULT: PASS (0 failures)`; the two files
are the page and these notes, since the Monday sessions' files were not on this branch. The page is
plain ASCII with no URL, no external file, no storage call and no network request.

### The plant grep

A script reads the page three ways (rendered with every day open, rendered with every scene revealed,
and the `W4` constants block) and searches for every Kalpa value the spine and the case file plant
(sections 5, 7, 8 and 9 of the spine, the case file's Kalpa transfers and the row's PLANTED lines).
Values moved off planted numbers during the build: the launch cohort's curve (22 and 15 percent and a
blended 41,900 became 24 and 16 percent and 42,900), the chips and milk pair (0.97 became 1.06), the
other milk pairs drawn in the band (0.99 and 1.01 became 1.03 to 1.07), the support axis (its 0.3 and
30 percent labels are gone), the milk band's printed 0.96 to 1.08, a constants comment that listed
festive multiples between 1.4 and 1.9, and M3's "down 4 percent", now the exact 4.5. The Friday ticket
gives the vendor and finance as eighteen points apart and the page never prints the vendor's 22.

The 26 hits that remain are the case's own numbers or false matches:

| The hit | Where | Why it stays |
|---|---|---|
| 6.4 and 1.2 percent, matched as "4 percent" and "2 percent" through their decimals | W4's strip, caption and reveal | The case's two click-through rates |
| "at least 2 percent of carts" | W3's reveal | The case file's own sentence for the milk band (its line 394) |
| 0.82 | F4's reveal and formula, the Friday node on the map | Spine section 11 fixes F4's reveal at about 0.82, the case's 25 over 25 plus 5.4 |
| About 4 percent a year | A constants comment | The Friday case's drift; the page prints it as "times 1.04 for the year's drift" |
| 30% | An axis tick on Th1's chart | A tick on a scale |
| "more than 5 percent below its before average" | M4's caption | M4's own rule for when a toy line turns |

### The writing checks

| Check | Scope | Result |
|---|---|---|
| The style sweep inside `verify.py` (dashes, banned words, the contrast construction it rejects, clock times, the rupee glyph, invisible Unicode, names, faculty sessions, undated links) | The page and these notes | Pass |
| `tic_scan.py` from the llm-tic-scrubber skill | The page rendered with every scene revealed, 1,467 runs; these notes | Clean |
| The house-rule words and glyphs, searched again on the rendered text | Every scene revealed | None found |
| The humanizer skill's read, in file mode on prose only | Every reveal paragraph | Sentences that carried an aphorism now carry a number (W5, Th1, Th2, Th4, F2 and S1) |

### Screenshots

Taken after the last fix with the pre-installed Chromium, each scene revealed, in the session's
scratchpad under `final_shots/`: each day's last scene (`M4.png`, `T3.png`, `W5.png`, `Th4.png`,
`F4.png`, `S1.png`), all 21 scenes under `final_shots/all/`, and the map at load, with each day lit and
with the connections shown under `final_shots/map/`.
