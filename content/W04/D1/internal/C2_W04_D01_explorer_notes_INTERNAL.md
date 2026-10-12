# Week 4 explorer: build notes, sources and proofs

**INTERNAL.** The notes behind `demos/C2_W04_D01_week_explorer_STUDENT.html`, the one interactive page
for the whole of Week 4 (spine section 11). They say what each scene draws and what each control moves,
where every number comes from, what the build decided where the spine left a choice open, where the
sources disagree with themselves, and what the proofs returned.

## How the page is built and checked

| Step | Command or place | What it does |
|---|---|---|
| The house look and the diagram builders | `python3 scripts/build_companion.py content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html` | Fills the page's `<style data-c2kit>` and `<script data-c2kit>` blocks from `scripts/companion/`; T3's two trees are drawn by `C2K.driverTree` |
| Every number | The `W4` block in the page's head | One constants block, each value with its source in a comment: the case file or the spine for case numbers, "derived" for arithmetic on them, "toy" for invented values that the page labels toy where they appear |
| The browser sweep | `python3 scripts/html_sweep.py content/W04/D1/demos` | Clicks every control in DOM order and fails on a control that changes nothing, a console error or a covered dropdown |
| The day gate | `python3 scripts/verify.py content/W04/D1` | The layout, naming and writing rules, then the sweep |

The six day buttons come first in the DOM, and choosing a day opens that day's section and every
earlier one, so by the time the sweep reaches the scenes the Saturday button has opened all six days
and every control is visible. Choosing a day sets `location.hash` to `mon` to `sat`, and a scene id
(`#M1`, `#Th3`) opens its day and scrolls to it, so a trainer can bookmark either. The page keeps
nothing between visits, loads nothing from the network and needs no install.

## The scenes, and what each control moves

Every scene has the six parts of spine section 11: a question as its heading, the first answer most
people give, a prediction made before any control is touched, a drawing, controls with a printed
readout each, and a reveal that prints the number and then names the formula last. Every slider's
readout prints the raw slider value, so one step always moves a printed digit. The reveal also sets the
scene to the case's state, and printing the page reveals every scene first, so each prints in its
final state.

| Id | The question | What is drawn | What each control moves | The reveal |
|---|---|---|---|---|
| M1 | Can online hours rise while riders wait as long? | A city of twelve zones with sixty driver dots that drive, idle or sit offline | The floor slider, Rs 0 to 400 in steps of 20, moves dots online and into the outer zones and moves online hours, trips, trips per online hour, the idle share, the top-up paid to driver-weeks accepting under half their requests and the dot counts; the rider-wait toggle shows the wait meter and its minutes | At Rs 300: 118,000 to 146,300 hours, 224,200 to 230,900 trips, 1.90 to 1.58, Rs 1.16 crore to driver-weeks accepting under half their requests, wait 4.8 to 4.6; trips per online hour = trips / online hours |
| M2 | Which number should the scheme pay for? | A seesaw of the paid number against three guardrails, above the same sixty dots | The select of four paid numbers re-places the dots, tips the seesaw, flips the guardrail chips and moves the dot counts, the idle share, the wait and the top-up per trip | Trips with an acceptance floor puts 40 of 60 dots to driving against 31; the definition's lines |
| M3 | What does one line of a definition change? | The twelve driver-weeks as a table, with a before and after bar | Four selects (numerator, denominator, window, exclusions) recolour the columns, strike excluded rows and move the before, after and change readouts | Per online hour 1.90 to 1.19, per enrolled driver 19.0 to 14.7; a definition names numerator, denominator, window, exclusions and what it does not reward |
| M4 | Which number moved first? | Acceptance share and bookings per online hour over twelve weeks, the launch marked | The week slider, 1 to 12, draws both lines to that week and moves the week's values and the turn readouts | Acceptance turns in week 7, bookings in week 9, a lead of two weeks; a leading indicator moves before the north star |
| T1 | What is left when the slide says one thing? | A slide with nine of Monday's numbers under a topic title | Nine checkboxes fade tiles, count the numbers left and rewrite the title when two remain; the warden test, defined in its readout as whether a reader outside the field could act on the title alone, prints its verdict on the current title | Trips per online hour and the top-up carry the claim; claim, evidence, caveat, action |
| T2 | Which denominator is the slide using? | The same bookings over three denominators as indexed bars | The select draws the chosen reading's bars, outlined; a reading not yet chosen stays a dashed outline, so the drawing never answers the prediction; the select also moves the slide title and the before, after and change readouts | Rs 314 to Rs 260 per online hour, per driver-week up 3 percent, per trip flat at Rs 165; bookings per online hour = trips per online hour x fare |
| T3 | How big is a number nobody has measured? | Two guesstimate trees, UPI payments a day and drivers at the evening peak | The select moves the focus between the trees; six sliders move the factors, the products, the drivers' ratio and the anchors' lines; the UPI anchor and ratio print at the reveal | 802 million a day in September 2026 (776 million over 31 days); drivers at peak: to be found, the case's own 813 a peak hour; clarify, map, calculate, validate |
| W1 | Why is lift a ratio of two areas? | A unit square with two bands and their overlap, the observed overlap beside it | Three sliders, P(A), P(B) and the observed share, in steps of 0.01, move the bands, the areas, observed over expected and the range the overlap can take at those bands | Bands widened to 0.70 and 0.50 at a fixed 0.30 overlap give lift 0.86; at 0.80 and 0.70 the overlap is forced to at least 0.50; the tea stall's 1.25; lift = P(A and B) / (P(A) P(B)) |
| W2 | What does confidence throw away? | A hundred carts in the case's proportions | Two filter buttons and a reset move carts to the right or fade them and move the counts | 34 carts left, 25 with milk, 25 / 34 = 0.74 against milk's 0.71; confidence = P(A and B) / P(A) |
| W3 | Why does the item in every cart look like the best partner? | The square with bread and milk, and two gauges | The milk-share slider, 0.10 to 0.90, moves milk's band, the overlap, confidence and lift | At 0.71, confidence 0.74 and lift 1.04; confidence follows popularity, lift divides it out |
| W4 | What does a strip slot earn? | A cart page with three slots under a cart holding chips | The rank toggle re-ranks the items into the slots; three sliders move every slot's rupees and the strip's day and month totals | Rs 3,240 against Rs 17,280 a day, about Rs 4.2 lakh a month; value = views x click-through x add rate x margin |
| W5 | Where should the support floor sit? | Lift against support for nine pairs on a log scale, with the action regions | A guess slider and lock record the prediction; the floor slider, 0.1 to 5 in steps of 0.1, moves the floor line and the counts | Eight of nine survive 1 percent, ice cream with chocolate sauce falls off at 0.25 percent; act above the floor, watch below it |
| Th1 | How can every batch shrink while the average stays flat? | The cohort staircase filling month by month under the dashboard's line | Next month adds a row and extends every older row; the size slider resizes the newest cohort and moves its row and the counted members | The dashboard holds at 38 from June to September while every row falls; blend = sum of size x rate / sum of sizes |
| Th2 | What is the flat number made of? | Two months of a coaching centre's batches, stacked by size, opening before batch B joins | Batch B's size, from 0, and batch A's rate move the stacks and the blended share | 250 of 500 is still 50 percent; the weighted average written out |
| Th3 | Which stage owns the loss? | The order flow as bars whose lengths are the counts, opening with the carousel's menu opens left out | The unit toggle and the carousel toggle swap the counts and move every step's rate | 118 percent search to menu view per session; 34 and 61 percent menu view to add-to-cart; each step divides by the step before in one unit |
| Th4 | Is it novelty or habit? | A launch cohort against an organic cohort over eight weeks, and the blended actives | The week slider draws both curves to that week; the blend toggle shows the blended line | At week four the launch cohort keeps 24 percent and the organic 36; the blend bottoms at 36,600 in week five and climbs to 42,900 by week eight; judge a cohort at the age where habit shows |
| F1 | What is a series made of? | Trend, season and noise panels summed into one series | Three sliders move their panels, the series, its highest and lowest weeks and the trend's rise | Doubling the season doubles the swing around the trend; series = trend + season + noise |
| F2 | How wrong on the weeks it never saw? | The 104 weeks with the hidden weeks shaded, and the hidden weeks zoomed with each week's error | The method select and the split slider, 52 to 91, move the forecast, the sticks, the MAE, the priced errors and the scoreboard | MAE 21,000, 9,200, 8,900 and 14,800, and the errors priced; MAE = mean of absolute errors on held-out weeks |
| F3 | Where does the house bot put Diwali this year? | The 2025 festive weeks above two 2026 copies on the same calendar weeks | The Diwali slider, the weeks of 19 October to 9 November 2026, moves the 2026 marker and the festival-aligned copy while the bot stays | The bot two weeks early at the 2026 date; festival-aligned copies the week at the same distance from the festival |
| F4 | Where should the plan sit when being short costs more? | The idle, late and total expected cost against the plan's distance from the forecast | Two cost sliders, inside the case's ranges, move the curves, the minimum, the quantile, the packer shifts and the expected costs | The 0.82 quantile, about 10,300 shipments and 86 shifts above the middle; plan quantile = under-cost / (under-cost + over-cost) |
| S1 | Does the method survive a change of company? | The week's methods on the left and the chosen unit's card on the right | The unit select lights the methods the unit uses and fills the card; the textarea writes the learner's own line into the map | What stays is the method; what changes is the metric, the constraint and the cost of an error |

The day decks name the scene each slide calls in the slide's notes fence (spine section 11); the decks
were not built when the page was, so the slide-to-scene list belongs to the week read.

## Where the numbers come from

The five day facts files did not exist when the page was built (the build workflow had the explorer
after the five drafting sessions; this session ran on the day the spine was approved), so every case
number comes straight from `docs/detailing/W04_case_file.md` and `docs/detailing/W04_analyst_craft_spine.md`
as approved on 12 October 2026. When the facts files land, the week read swaps the `W4` block's values
for the facts files' values by id; every scene computes from that block, so nothing else changes.

| Day | Case numbers, with their place in the sources | Derived on the page | Toy, labelled toy on the page |
|---|---|---|---|
| Mon | The ticket table: 118,000 and 146,300 hours, 224,200 and 230,900 trips, 0.86 and 0.73, 0.04 and 0.09, 0.22 and 0.38, 4.8 and 4.6 minutes, 0.11 and 0.10, Rs 1.9 crore; L5's Rs 1.16 crore; the floor of Rs 300; the twelve rows' table | Rs 82 of top-up per trip (Rs 1.9 crore over 230,900) | The response curve between Rs 0 and Rs 300; the dots' behaviour under the three other paid numbers and their wait and top-up per trip; the twelve weekly values of M4, built to average 0.86, 0.73, Rs 314 and Rs 260 |
| Tue | Rs 314, Rs 260 and Rs 165 (ticket); 24.07 billion and 802 million a day (T3, NPCI through Outlook Money, checked 12 October 2026) | 776 million over 31 days; 813 drivers online in an average peak hour (146,300 hours over 180 peak hours: 5 weekdays, two windows of three hours, six weeks); per driver-week up 3 percent | The 6,000 driver-weeks behind the per driver-week reading; every factor in the two guesstimate trees, which the learner sets |
| Wed | 71 percent milk, 34 percent bread, 0.74 and 1.04 for bread to milk, 0.73 and 1.03 for eggs, 5.0 percent and 3.4 for chips with cold drink, 0.25 percent and 4.6 for ice cream with chocolate sauce, the 0.96 to 1.08 band, 1.2 and 6.4 percent click-through, 60,000 views, 0.5 add rate, Rs 9 margin, 40,000 carts | The hundred carts (25, 9, 46, 20) in the case's proportions; each pair's support from share times confidence; Rs 17,280, Rs 3,240, Rs 14,040 and Rs 4.2 lakh | The tea stall (R1); bread, dip and namkeen beside chips; the other milk pairs' positions inside the case's band |
| Thu | Month-one retention 58, 56, 55, 53, 52, 50, 49 and 31; 5,000 a normal month and 2.6 times for August; 38 percent flat; 118, 34 and 61 percent; 58 to 44, 57 and 52 for the checkout | The blend from the cells and the sizes | The cells after month one, built so the dashboard reads 38 from June to September; the coaching batches (R1); the funnel's counts; the AI app's two cohorts |
| Fri | The 104 weeks' dates; Diwali on 31 October 2024, 20 October 2025 and 8 November 2026 (F5, `facts.yaml`); 120 shipments a shift; Rs 650 and Rs 25 with their ranges; the MAE table; 4 percent a year of drift; the festive shape | Rs 5.4 a shipment; the 0.82 quantile; 10,300 shipments and 86 shifts; Rs 0.88 and Rs 1.35 lakh a week; the priced errors | The 104 weekly values, built to the case's shape and solved so the last 13 weeks score 21,000, 9,200, 8,900 and 14,800; the vendor's curve at 1.10 times last year's week; the trend, season and noise of F1 |
| Sat | Rohan Desai's "twenty times more one way than the other" (`docs/07_Client_Zero.md`, stakeholder table); Kalpa Health's six US metro areas billed in dollars (decision `build1-us-data`); the brief lines of spine section 10 and the case file's Saturday table | None | None: the four company cards carry no figure and say they are hypothetical |

## What the build decided where the spine left a choice

| Choice | What the page does | Why |
|---|---|---|
| Which day sections show | A day button opens its own section and every earlier one, and dashes nothing below | The map lights every earlier node, and the sweep reaches every control only if the last day button opens all six days |
| The prediction form | Lettered choices in twenty scenes, with the key on A four times, B five, C six and D five, and never the longest option; a guess slider with a lock button in W5, where the prediction is a count | The spine allows a choice or a slider guess; a count reads best as a guess; a key that sits on one letter or is always the longest lets a learner answer without thinking |
| The reveal | Sets the scene to the case's state as it prints the number, and names the formula last | The reveal prints the case's number, so the picture should show it |
| Motion | CSS transitions and one CSS animation (the driving dots), switched off under reduced motion; nothing animates by timer | Motion explains the mechanism without changing the page between the sweep's before and after reads |
| Thursday's dashboard | Counts a member from the second month after signup, so the August cohort enters only in October | The case's flat 38 percent through September is out of reach under the spine's definition (see the next section); the case's own words, "month-two retention", support this reading |
| Monday's twelve rows | The case file's table as printed, so M3's hand count is 1.90 to 1.19 | The table is the only set of rows the sources fix; the case file's own hand count disagrees with it (see the next section) |
| S1's map | The week's five methods on the left, the unit's card on the right | The home map's nodes become the methods that stay, and the card shows what changes |
| Th1's prediction | Asks what holds the dashboard's 38 up in September (the sale cohort sits outside the count until its second month), where the spine asks what the blend will do | The Thursday ticket prints the flat 38 for June to September, so the spine's question is answered before it is asked; the reveal still lands the spine's number and formula |
| Opening states | Every scene opens before the state its prediction asks about: T2 draws a reading once it is chosen, T3 holds the measured 802 million for the reveal and opens its UPI tree at 50 million a day, Th2 opens before batch B joins, Th3 opens with the carousel's opens left out, and no caption prints the number a prediction asks for | A drawing that shows the answer first turns the prediction into reading |
| Light theme only | The house companion look, tuned for a projector | The house pages are light; a dark theme would need every drawing's colours as variables, which the house library does not carry yet |

## Where the sources disagree with themselves

These need the orchestrator, because the case file says no session changes a target alone.

1. **Monday's twelve rows.** The case file's table sums to 60 and 74 hours and 114 and 88 trips, a hand count of 1.90 to 1.19 trips per online hour, while the same section states the hand count as 114 to 110 trips and 1.90 to 1.49. Reaching 110 trips with drivers E and F at 3 and 2 needs drivers A to D to complete 105 trips in 44 hours, about 2.4 an hour against about 2.0 before, which breaks the table's "about the same" for them. The page uses the table; when the Monday facts file lands, M3 takes its `twelve_rows` and the M3 reveal's numbers. The table's 1.19 also sits 0.03 from the Kalpa plant 1.22, inside the 0.05 margin the spine sets for the twelve rows, and the table's hours rise 23 percent against the plant's 22.
2. **Thursday's flat 38 percent.** Under the spine's definition (members who signed up before the month, so a cohort counts from its first month), September's blend must fall below August's: every older cohort falls with age, and the August cohort enters at 31 percent, below the blend, at 2.6 times a normal size. With normal cohorts of 5,000 the drop is about two points. The page reads the dashboard as counting members from their second month, which holds 38 from June to September with every row falling and puts the sale cohort's weight into October. Either the spine's definition or the September target needs to change.
3. **Friday's hold-out dates.** "The last thirteen weeks, beginning 22 June to 21 September 2026" is fourteen weeks; the last thirteen begin on 29 June. The page uses 29 June, which keeps the 91 training weeks the case states.
4. **Tuesday's per driver-week reading on the twelve rows.** With the same six drivers in both weeks and a flat fare, bookings per driver-week move with trips, which fall on the rows, so the rows cannot show per driver-week rising. The page shows the three readings on the city's totals with a toy count of driver-weeks held equal, where per driver-week rises 3 percent with total bookings.
5. **Friday's calendar table.** It has 112 weeks, to the week of 16 November 2026, while the festive window to staff runs to the week of 30 November.
6. **Friday's errors priced.** On the page's toy weeks, which score the case's MAE table exactly, the vendor's errors, 12 of 13 too high, price at Rs 10.9 lakh against the festival-aligned baseline's Rs 18.6 lakh, and the baseline raised by F4's 10,300 shipments prices at Rs 10.9 lakh, level with the vendor. F2's reveal says so, with the case's own L4 caveat that the hold-out holds no festive week, so the case's argument for the baseline rests on the festive window the hold-out cannot test. A facts file that prices the hold-out will likely find the same, and the Friday deck should be ready for a learner who spots it.

## The proofs

### The browser sweep

The sweep's last lines on the final page, with the pre-installed Chromium at `/opt/pw-browsers` (`setup.sh` was not needed):

```
      C2_W04_D01_week_explorer_STUDENT.html: 187 controls clicked, 0 inert, 0 not visible in the opening state, 0 console errors
RESULT: PASS (0 failures)
```

`python3 scripts/verify.py content/W04/D1` returned `PASS  2 files, every stem C2_W04_D01_ and every folder valid for a teaching day`, the same sweep result and `RESULT: PASS (0 failures)`; the two files are the page and these notes, since the Monday sessions' files were not on this branch. The page is 238,655 bytes of plain ASCII with no URL, no external file, no storage call and no network request.

### The plant grep

A script reads the page three ways (rendered with every day open, rendered with every scene revealed, and the `W4` constants block) and searches for every Kalpa value the spine and the case file plant (sections 5, 7, 8 and 9 of the spine, the case file's Kalpa transfers and the row's PLANTED lines). Four coincidences were moved off the planted values: the launch cohort's curve (it printed 22 and 15 percent and a blended 41,900; it now prints 24 and 16 percent and 42,900), the chips and milk pair (0.97 lift and 8.3 percent support, now 0.99 and 8.4), the support axis (its 0.3 and 30 percent labels are gone; 0.1, 1 and 10 percent remain), and a constants comment that listed festive multiples between 1.4 and 1.9. The Friday ticket gives the vendor and finance as eighteen points apart and the page never prints the vendor's 22.

The 31 hits that remain are the case's own numbers or false matches:

| The hit | Where | Why it stays |
|---|---|---|
| 6.4 and 1.2 percent, matched as "4 percent" and "2 percent" through their decimals | W4's strip, caption and reveal | The case's two click-through rates |
| "at least 2 percent of carts", confidence 0.68 to 0.78 | W3's reveal | The case file's own sentence for the milk band (its line 394) |
| Lift 0.96 to 1.08 | W3's reveal, W5's caption, a constants comment | The case's milk band; its 0.96 equals Kalpa's Monday 0.96 by the case file's own choice |
| 0.82 | F4's readout and reveal, the Friday node on the map | Spine section 11 fixes F4's reveal at about 0.82, which is the case's 25 over 25 plus 5.4 |
| About 4 percent a year | A constants comment | The Friday case's drift; the page prints it as "times 1.04 for the year's drift" |
| 30% | An axis tick on Th1's retention chart | A tick on a scale, unrelated to Kalpa's vendor error |
| "more than 5 percent below its before average" | M4's caption | M4's own rule for when a toy line turns |

### The writing checks

| Check | Scope | Result |
|---|---|---|
| The style sweep inside `verify.py` (dashes, banned words, the contrast construction it rejects, clock times, the rupee glyph, invisible Unicode, names, faculty sessions, undated links) | The page and these notes | Pass |
| `tic_scan.py` from the llm-tic-scrubber skill | The page's static prose, 488 runs; the page rendered with every scene revealed, 1,447 runs; these notes, 122 runs | Clean on all three |
| The house-rule words and glyphs, searched again on the rendered text | Every scene revealed | None found |
| The humanizer skill's read, in file mode on prose only | Every reveal paragraph | Six sentences that carried an aphorism now carry a number (W5, Th1, Th2, Th4, F2 and S1) |

### The two reviews and what changed

Two fresh reviewers, who write findings and never edit, walked the page: a fresh graduate meeting each scene cold, and a rigor and numbers pass. Their findings and what changed follow in this section once both reports are in.

### Screenshots

The final screenshots of each day's last scene, revealed, are listed here once the reviews' fixes are in.
