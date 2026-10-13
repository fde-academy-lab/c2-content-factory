# Provenance: Week 4, Saturday

INTERNAL. One session built this pack on 13 October 2026 on the branch `w04-sat`, working in one
long turn with nobody answering questions, so every choice the spine left open is recorded here as a
decision with its reason.

## What decided this pack

| Source | What it settled |
|---|---|
| The orchestrator's brief for the W04 SAT session, 13 October 2026 | The seven deliverables, the rules that stop invention, the finish line, and three notes: Thursday's numbers only from Thursday's facts file, every Delhi Metro and Aced fact only from Thursday's corrections table, and Friday's hold-out errors from Friday's facts file |
| `docs/detailing/W04_analyst_craft_spine.md`, section 10 | The 300-minute Saturday in seven blocks, the six parts and their questions, the bank items each part tests, the additions each part wants, the eight briefs and their seeds, item 41, and the plant rule |
| `docs/detailing/W04_case_file.md`, "Saturday: the method moves company" | The facts each drill brief may use, and the R2 list of facts the Saturday may cite |
| `docs/curriculum/W4_Analyst_craft.md`, the Saturday row and the five day rows | The nine interview anchors, the drill rule, the bridge, and Tuesday's anchors |
| `docs/curriculum/source.xlsx`, the Saturday papers tab, paper W4 (43 items, 89 minutes) | Every bank stem and key, unchanged, and what the paper must test |
| `data/programme/facts.yaml` | `campus_day.saturday_minutes` 300; `saturday_papers.paper_minutes` W04 120; decisions `saturday-w4-shape`, `saturday-interview-grade`, `saturday-real-cases`, `plants-once-found`, `w4-finding-once-found`, `papers-to-build` and `teaching-approach`; module M2 for Week 4 |
| The five Week 4 facts files, `content/W04/D{1..5}/internal/C2_W04_D0{d}_facts_INTERNAL.yaml` | Every synthetic number on the paper, read by id in the key proofs |
| The five lab notes, `content/W04/D{1,3,4,5}/trainer/*_lab_note_TRAINER.md`, and Tuesday's lab | The Kalpa findings the paper may name, each confirmed against the note's plant table before printing |
| The five interview transcripts in each day's `extras` folder | The mock round's questions, follow-ups and AI-company variants, quoted as each transcript prints them |
| `docs/07_Client_Zero.md` v2.2, sections 1a, 1c and the Build 2 seeds | Kalpa's four other units and their people, Rohan Desai's twenty-to-one cost, Kalpa Health's US setting and six metro areas |
| `docs/curriculum/W5_ML_core_ME1.md` and `docs/programme/calendar.md` | The bridge's Week 5 days, its Monday ask and Rohan's Tuesday question |
| The W01 and W02 Saturday packs | The source file's form, the discussion guide's form, and the folding practice |

## The paper

`scripts/build_saturday_paper.py W04 --docx` renders 39 timed items in six parts at 118 minutes by
the blueprint's pace, 8 easy, 8 medium and 23 hard (59 percent hard), with an untimed stretch page of
five. Ten bank items print (five of them reworded through `data/programme/paper_edits.yaml`),
thirty-two fold into deeper items, one moves to the stretch page, and twenty-nine additions come
from the week's source file. A blind guesser averages 6.4 of 39, and the key's guessing line sits at
10. The levels are the ones the fix pass set after the two cold reads (below).

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Which number should the plan chase, and which should a scheme pay for? | Q1 to Q7 | 19 | 2 | 2 | 3 |
| 2. Can the number survive the room, and can you size a city from nothing? | Q8 to Q14 | 23 | 1 | 0 | 6 |
| 3. Which pairs beat chance, and what is a slot worth? | Q15 to Q21 | 21.5 | 0 | 3 | 4 |
| 4. Where is the tier losing people? | Q22 to Q28 | 22.5 | 0 | 2 | 5 |
| 5. Which forecast earns the plan's trust? | Q29 to Q33 | 20 | 1 | 0 | 4 |
| 6. What changes when the method moves company? | Q34 to Q39 | 12 | 4 | 1 | 1 |
| Total | 39 | 118 | 8 | 8 | 23 |

The distractor audit passes with key positions a 10, b 5, c 9, d 6 and e 1; the four more-than-one
items share no letter across their keys (Q7 c, d, e; Q9 a, c; Q13 a, c; Q34 a, b, d). The proofs
script, `C2_W04_SAT_key_proofs_INTERNAL.py`, assembles the paper exactly as the builder does and
recomputes every key from the five facts files and the printed exhibits; it ends "RESULT: PASS (39
items proved)".

## The fate of every bank item

| Bank | Type, the tracker's level | Fate | Where it is tested | Why |
|---|---|---|---|---|
| 1 | Fill in the blank, Easy | Printed | Q1 | As the tracker prints it |
| 2 | Fill in the blank, Medium | Printed | Q2 | As the tracker prints it |
| 3 | Fill in the blank, Easy | Folded | Q19, bank 32 | The call on the case and the charger turns on a lift of 0.97 against a confidence of 0.825, and the reason for option a, the most tempting wrong answer, is that confidence is the measure a popular item fools, so lift is the one that is not fooled. |
| 4 | Fill in the blank, Medium | Folded | Q19, bank 32 | The key reads the lift of 0.97 as case buyers taking a charger about as often as chance alone gives, slightly less, which is what a lift of about 1 means. |
| 5 | Fill in the blank, Easy | Folded | Q24, bank 35 | The honest headline needs each cohort read from the month its members joined, and its reason names the entry moment as what fixes a cohort. |
| 6 | Fill in the blank, Medium | Folded | Q29, bank 41 | The item asks for the seasonal naive by name and keys it as the same month a year earlier, which is the blank bank 6 fills. |
| 7 | Fill in the blank, Easy | Folded | Q33, kalpa-board | The board sentence the item keys gives the error on months the forecast never saw, and its wrong option a is a fit to months it did see. |
| 8 | True or false, Easy | Folded | Q5, tf-target | The printed item is bank 8's statement, judged with its reason on Wells Fargo's cross-sell count, so the room has to say what the staff did and not only mark it true. |
| 9 | True or false, Easy | Folded | Q3, tf-leading | The printed item is bank 9's statement, judged with its reason on the Hyderabad dashboard, where the leading number has to be told apart from the north star it feeds. |
| 10 | True or false, Easy | Folded | Q19, bank 32 | Option a is the reading that a confidence above 0.8 is worth promoting, and the key refuses the bundle at a confidence of 0.825, which is bank 10's false statement shown false. |
| 11 | True or false, Medium | Folded | Q20, watch | The printed item judges bank 11's statement with its reason on the two thin pairs the week found, Kalpa's car phone mount and car charger and Instamart's ice cream and chocolate sauce, each at a support of 0.25 percent. |
| 12 | True or false, Hard | Folded | Q24, bank 35 | The set's two blends both read 41 percent while cohorts A and B both fall, which is bank 12's statement worked on numbers. |
| 13 | True or false, Medium | Folded | Q25, funnel-units | Option c divides every step by the sessions that opened the app, the single denominator bank 13 calls false, and its reason says why each step takes the step before as its base. |
| 14 | True or false, Easy | Folded | Q31, m5 | The sponsor's case is a curve that fits two years within 2 percent, and the key says a fit is no forecast, which is bank 14's false statement refused on the M5 scoreboard. |
| 15 | One correct option, Medium | Folded | Q7, kalpa-sheet | The exhibit is the lab's finding behind bank 15's reading, reorders per member up 1.22 times while their booked value per member fell to 0.96, and option a, the reorders north star, is wrong for the reason bank 15 keys. |
| 16 | One correct option, Medium | Folded | Q4, twelve-rows | The city team's note is a number hit while the outcome got worse, hours up and trips per hour down, so applying the proxy test is the item's whole judgement. |
| 17 | One correct option, Medium | Folded | Q7, kalpa-sheet | Option d is bank 17's guardrail, revenue per active customer, which catches frequency bought with low-value orders. |
| 18 | One correct option, Easy | Folded | Q19, bank 32 | The set's situation is bank 18's on round counts, a charger in 85 percent of baskets and a case at a confidence of 0.825 toward it, and the call is the reading bank 18 keys. |
| 19 | One correct option, Medium | Folded | Q21, margin | Turning a pair into a recommendation needs an expected value in rupees, and the item computes it, incremental margin less the discount paid on every add. |
| 20 | One correct option, Medium | Folded | Q24, bank 35 | The headline item's reason is the one bank 20 keys, that a cohort view fixes the entry moment so a changing mix cannot hide a decline. |
| 21 | One correct option, Hard | Folded | Q25, funnel-units | Each step is computed over the step before, in sessions and in members, which is bank 21's arithmetic, and option a is bank 21's reading that the lowest step is the loss. |
| 22 | One correct option, Hard | Folded | Q28, kalpa-window | The reply the item keys is bank 22's evidence on Kalpa's own counts, the stage's conversion by date, with the fall inside the auto-reorder window. |
| 23 | One correct option, Medium | Folded | Q31, m5 | The key is bank 23's honest test, scoring the curve against the seasonal naive on weeks it never saw. |
| 24 | One correct option, Easy | Folded | Q32, asym | The plan follows from what each miss costs the decision, which is what bank 24 says good enough is about. |
| 25 | More than one correct, Medium | Folded | Q7, kalpa-sheet | Options b and e set a lagging number against a leading one, last quarter's audited revenue against add-to-cart events this week, bank 25's options c and a. |
| 26 | More than one correct, Medium | Folded | Q18, bank 31 | The set computes a confidence and a lift from one pair's counts with bank 26's definitions b and c, the pair's support of 165 in 1,000 is its option a on the exhibit, and a confidence of 0.825 beside a lift of 0.97 is the counterexample to its option d. |
| 27 | More than one correct, Hard | Folded | Q25, funnel-units | The exhibit carries all three of bank 27's false losses at once, a step members can skip, a session base set beside a member base, and the temptation to divide every step by the opening count. |
| 28 | More than one correct, Medium | Folded | Q31, m5 | The scoreboard sets machine-learning entries against the naive and the seasonal naive, two of the honest baselines bank 28 keys, and the key refuses a vendor's curve as its own baseline. |
| 29 | More than one correct, Hard | Printed, its stem, options reworded, at Medium | Q34 | The edit and its reason are in data/programme/paper_edits.yaml, status proposed |
| 30 | Scenario set, Medium | Printed, its situation reworded | Q17 | The edit and its reason are in data/programme/paper_edits.yaml, status proposed |
| 31 | Scenario set, Medium | Printed | Q18 | As the tracker prints it |
| 32 | Scenario set, Hard | Printed, its options reworded, at Medium | Q19 | The edit and its reason are in data/programme/paper_edits.yaml, status proposed |
| 33 | Scenario set, Medium | Printed | Q22 | As the tracker prints it |
| 34 | Scenario set, Hard | Printed, at Medium | Q23 | As the tracker prints it |
| 35 | Scenario set, Hard | Printed, its options reworded | Q24 | The edit and its reason are in data/programme/paper_edits.yaml, status proposed |
| 36 | Scenario set, Medium | Folded | Q32, asym | The item asks for each forecast's mean absolute error from its misses summed by direction, the arithmetic of bank 36 on the week's own thirteen weeks. |
| 37 | Scenario set, Hard | Folded | Q33, kalpa-board | The board sentence the item keys is bank 37's answer to Anand on Kalpa's own months, the average miss on months the forecast had not seen. |
| 38 | Scenario set, Medium | Moved to the stretch page | Stretch 5 | A recall check on MAPE's denominator, kept untimed so the timed paper holds about 60 percent hard |
| 39 | Applied maths, Medium | Folded | Q21, margin | The item is bank 39's expected value with the cost line most analysts forget, a discount paid on adds that would have happened anyway. |
| 40 | Applied maths, Hard | Folded | Q18, bank 31 | The set computes a confidence and then a lift from three counts, the arithmetic of bank 40, on a pair whose lift falls below 1 where bank 40's reached 2.5. |
| 41 | Applied maths, Easy | Printed, its stem reworded | Q29 | The edit and its reason are in data/programme/paper_edits.yaml, status proposed |
| 42 | Applied maths, Easy | Folded | Q25, funnel-units | Reading the exhibit needs each step's conversion over the step before, which is what bank 42 asks for, in two units. |
| 43 | Applied maths, Hard | Folded | Q32, asym | The item's reason sets the vendor's mean miss of 16,400 against festival-aligned's 6,615, about 148 percent larger, the comparison bank 43 asks for on the week's own weeks. |

## The additions

Twenty-nine items come from the source file, seven of them Tuesday's, which decision
`papers-to-build` leaves to the content team and the key lists as waiting for the tracker.

| Q | Addition and its label | Type | Level | Minutes | Day |
|---|---|---|---|---|---|
| Q3 | tf-leading, "Judge the statement" | True or false | Easy | 2.5 | Mon |
| Q4 | twelve-rows, "Read six drivers" | One correct option | Hard | 4 | Mon |
| Q5 | tf-target, "Judge the statement on a case" | True or false | Medium | 2.5 | Mon |
| Q6 | wells-silent, "Size the silent change" | One correct option | Hard | 3.5 | Mon |
| Q7 | kalpa-sheet, "Mark the definition sheet" | More than one correct | Hard | 3.5 | Mon |
| Q8 | slide-order, "Build the slide" | Order the steps | Hard | 3.5 | Tue |
| Q9 | keep-two, "Keep two elements" | More than one correct | Hard | 2.5 | Tue |
| Q10 | concede, "Judge the defence" | True or false | Hard | 3.5 | Tue |
| Q11 | memo, "Judge the memo" | True or false | Easy | 2.5 | Tue |
| Q12 | estimate-order, "Order the estimate" | Order the steps | Hard | 3.5 | Tue |
| Q13 | four-checks, "Check four sources" | More than one correct | Hard | 4 | Tue |
| Q14 | metro, "Read the metro counts" | One correct option | Hard | 3.5 | Tue |
| Q15 | ctr-slot, "Read the strip by slot" | One correct option | Hard | 3.5 | Wed |
| Q16 | heavy, "Allow for heavy buyers" | One correct option | Hard | 4 | Wed |
| Q20 | watch, "Judge two thin pairs" | True or false | Hard | 3 | Wed |
| Q21 | margin, "Price the bundle slot" | One correct option | Hard | 3.5 | Wed |
| Q25 | funnel-units, "Read the flow two ways" | One correct option | Hard | 4 | Thu |
| Q26 | android, "Find the fix and its cost" | One correct option | Hard | 4 | Thu |
| Q27 | swiggy, "Ask for the denominator" | One correct option | Hard | 3.5 | Thu |
| Q28 | kalpa-window, "Answer the app team" | One correct option | Hard | 3.5 | Thu |
| Q30 | calendar, "Move the spike" | Applied maths | Hard | 4 | Fri |
| Q31 | m5, "Answer the sponsor" | One correct option | Hard | 4 | Fri |
| Q32 | asym, "Price the misses" | One correct option | Hard | 5 | Fri |
| Q33 | kalpa-board, "Choose the board sentence" | One correct option | Hard | 4 | Fri |
| Q35 | brief-logistics, "Match: Kalpa Logistics" | Match the following | Easy | 1.5 | Sat |
| Q36 | brief-health, "Match: Kalpa Health" | Match the following | Easy | 1.5 | Sat |
| Q37 | brief-connect, "Match: Kalpa Connect" | Match the following | Easy | 1.5 | Sat |
| Q38 | brief-finance, "Match: Kalpa Financial Services" | Match the following | Easy | 1.5 | Sat |
| Q39 | amazon, "Set the plan share" | One correct option | Hard | 3.5 | Sat |

## The edits laid on the bank

All five sit in `data/programme/paper_edits.yaml` under W4 with status proposed, each with its reason,
and none moves a key.

| Bank | Edit | Why |
|---|---|---|
| 29 | A stem setting Rohan Desai's ask and its twenty-to-one cost; option b names a guardrail the measured cannot move, and option c the rupee amount each kind of wrong nudge costs | The tracker's stem carried no scenario, and its options b and c ran 21 and 31 characters against 60 for option a; a first wording of c read as the practice of pricing both errors, which carries over |
| 30 | A situation of 1,000 round, illustrative consumer baskets with Business orders left out | Wednesday's lab found that Kalpa's 1,000 orders hold 812 consumer baskets once the 188 Business orders go, so "1,000 baskets" read as the lab's base trap |
| 32 | Option a names the case as well, at 106 characters | The key was the longest option by 9 characters |
| 35 | Option c says retention held steady from May to June, with no number; option d names the decline and blames the new cohort by setting two ages side by side | The key was the longest option by one character, an earlier c printed Q22's answer, and the tracker's d fell at a glance |
| 41 | A stem set in 2025, when Diwali stayed in October | The tracker's stem names this October as the Diwali month, and Diwali falls on 8 November 2026; the spine's proposed stem keyed last year's Diwali month as the seasonal naive, which Friday's same-month definition refuses once the festival changes month |

## Decisions taken where the spine left a choice open

| Decision | What the pack does | Why |
|---|---|---|
| Folding against printing | 32 bank items fold into deeper items and print as their judgement, with the fold and its reason in the key | The bank fills 89 minutes at 11 hard of 43; printing it whole left 31 minutes for additions and no way to reach about 60 percent hard, and the spine's own table of additions runs to about 70 minutes. Weeks 1 and 2 folded the same way |
| Item 41 | The 2025 stem in place of the spine's proposal, and the calendar trap as the new Q30 | The spine's proposal would key a festival-month copy as the seasonal naive, which Friday's pack defines as the same month a year earlier |
| Part 2's count | Seven items against the spine's "about eight" | Flipkart's decimal slip, UPI's per-day count and DMart's average store fold into one more-than-one item, Q13, so the slip is judged beside two sound checks |
| The households in Q13 | Eight million households at four to a household | Tuesday's learner deck (S45) prints eight million; the spine's draft said nine |
| Delhi Metro's unit | Trips against DMRC's line-use count, with the record day set apart | Thursday's corrections table replaces the case file's "journeys and boardings are different units" |
| Set 3 of the bank (36 to 38) | 36 folds into Q32 and 37 into Q33, which run on the week's own weeks and months; 38, a recall check on MAPE's denominator, moves to the stretch page | The set's round numbers repeat what Q32 and Q33 test on Lucknow's and Kalpa's numbers |
| Part 6's items | Bank 29 reworded, a match table of four Kalpa briefs and one Amazon item | The spine asks for three or four items on the briefs, one a match table; the match table's four rows are the four Kalpa briefs' first questions |
| Kalpa plants on the paper | Monday's 1.22, 0.96 and none delivered; Wednesday's 84.5 percent, the screen protector at 0.82 and 0.97, the earphones and case at 3.1, and the car pair at 4.0 on 2 baskets; Thursday's flat 41 and the window's 7 of 11; Friday's October spikes, the vendor's Rs 38.8 lakh and the festival-aligned Rs 444.7 lakh | Each sits in its day's lab note plant table (decision `w4-finding-once-found` counts the lab as class); Tuesday's lab has no plant |
| The discussion's 60 minutes | Most-missed 25, ten anchors at three minutes each 30, ratings 5 | The spine gives the block 60 minutes; the row's nine anchors plus Tuesday's "two minutes with a non-technical stakeholder", since Part 2 has no anchor in the Saturday row |
| The drill's 30 minutes | Eight tables of four or five, 8 minutes to prepare, 2 minutes a table aloud, 4 for the map | One brief per table answers all eight inside the block |
| The drill's company briefs | Rapido in Bengaluru, Blinkit in Gurugram, Swiggy One in Bengaluru and an Amazon India centre in a tier 2 city | The spine's choices (Ola or Rapido, Blinkit or Zepto, Swiggy One, Amazon India); each is labelled illustrative, and its only real facts are the case file's allowed ones, re-checked |
| Rapido's facts | None printed | The check confirmed Karnataka's January 2026 ruling but not what Rapido runs in Bengaluru now |
| Blinkit's per-store figure | Not printed | Eternal's Rs 11 lakh a store a day is a steady-state assumption and the quarter's actual was Rs 8.27 lakh, so the brief uses neither |
| The mock round | One question and one follow-up each way from the five transcripts and their AI-company variants, on the spine's seven-line card | The spine's block; the card quotes each question as its transcript prints it |
| The bridge | Week 5's five day questions from the calendar, Marketing's ask and Kavya's condition from the Monday row, Rohan's question from the Tuesday row, the setup line from the Saturday row | No Week 5 spine exists yet, so the bridge names no Week 5 case company, no Week 5 finding and no exam day, whose slot is open in `facts.yaml` |
| The fix pass on the two cold reads | Fourteen of the fifteen items the interviewer read as medium were hardened with the read's own rewrite, a distractor that shares the key's numbers and differs in its judgment or a stem that no longer names the method; Q34 moved to Medium, Q9 to Hard, and Q3, Q11 and Q35 to Q38 to Easy; Q15 stays Hard | Relabelling all fifteen would have left 9 hard items of 39, against the decision's 60 percent, while the read's rewrites cost a sentence each; the cold-reads file records every finding with what the pass did |
| Q13's fifth check | September's UPI average set against Diwali day, sound in unit and wrong in period, beside the households trap | The interviewer asked for a period trap, and the spine names the households trap, so both stay |
| No Saturday deck | The pack ships no deck | The brief lists none, and the Saturday layout verify reads allows only paper, answer-key, discussion and internal; the spine's line that the Saturday deck reopens the explorer's home screen is left to the explorer, which merges separately |

## The numbers the pack derives

Every one is recomputed by the proofs script from the facts files or the printed exhibit.

| Number | Where | How |
|---|---|---|
| 1.19 trips per online hour and the mean of ratios 1.31 | Q4 | 88 trips over 74 hours; the average of the six drivers' own rates |
| About 36 percent | Q6 | 0.04 over 0.11 |
| Rs 2,836 an extra trip | Q9 | Rs 1.9 crore over 6,700 extra peak trips |
| 4,960 and 5,700 drivers; 3,900 as the trap | Q12 | 8,333 trips an hour over 1.68, times 1.15; the trap divides 8,333 trips by 2.13 requests per online driver-hour |
| 802 million a day and Rs 146 crore a store, Rs 152 crore a store-year | Q13 and its key | 24.07 billion over 30 days; Rs 66,968 crore over the average of 415 and 500 stores; over about 439 store-years with 58 of 85 openings in the last quarter |
| 6 and 27 percent | Q14 | 60 lakh against 64.06 lakh and 82.45 lakh |
| 4.76, 2.85 and 1.35 clicks per 100 impressions; the strip's 3.8 | Q15 | Milk's share times the gap in each slot; half the impressions at 1.2 and half at 6.4 |
| Lifts 3.39 and 1.70 per cart | Q16 | 0.05 over 0.12 times 0.123; 0.075 over 0.22 times 0.20 |
| 0.825 and 0.97 | Q17, Q18 | 165 over 200; 0.825 over 0.85 |
| Rs 1,500 a day | Q21 | 375 new adds at Rs 10, less 750 adds at Rs 3 |
| 41 and 41 percent | Q22, Q23 | 1,640 over 4,000; 2,460 over 6,000 |
| 118, 34 and 61 percent | Q25 | Each step over the step before, per session and per member |
| 3,198 orders over 17 days, 1,317 a week, Rs 4.0 to 6.6 lakh; 1,223 against iOS | Q26 and its key | 14 points of 22,841 carts; 7 of 17 days; at Rs 300 and Rs 500; 13 points with iOS members as the comparator |
| 40 and 80 percent | Q27 | 4 of 10 and 4 of 5 |
| About 9 expected checkouts against 7 | Q28 | 10 of 12 applied to 11 carts |
| Rs 444.7 lakh; about Rs 309 lakh for October | Q30 and its key | Rs 427.6 lakh times 1.04; Rs 297.0 lakh times 1.04 on the printed figure |
| MAE 6,615, 9,831 and 16,400; Rs 13.5, 30.5 and 11.9 lakh; Rs 8.8 and 10.0 lakh at the 0.82 point | Q32 | Friday's hold-out section; 25 over 25 plus 5.42 |
| Rs 2.08 crore under the plan line | Q33 | Rs 21.77 crore less Rs 19.69 crore |
| 0.65 | Q39 | 10 over 10 plus 650 over 120 |
| 0.81 | The drill's brief 4 | 30 over 30 plus 4,200 over 600 |

## Cold reads and the fix pass

Two readers read the pack cold on 13 October 2026, findings only, and one fix pass answered both;
`C2_W04_SAT_cold_reads_INTERNAL.md` holds every finding with what the pass did. The learner, sitting
the paper against the clock from the STUDENT file alone, scored 39 of 39 in 103 minutes and found 22
things: 1 blocker (Q7's exhibit read two ways), 8 should fix and 13 notes; the pass fixed 18 and left
4 with their reasons. The hiring interviewer found 46: 2 blockers (Q11 credited Amazon's letter with a
lesson it does not draw, and Q8's order was arguable), 29 should fix and 15 notes, checked 31 real
facts with 29 confirmed and 2 differing, and read 15 of the 23 hard items as medium; the pass fixed
or relabelled 41 and left 5 with their reasons. The paper rebuilt after the pass proves on all 39
keys, passes the distractor audit and holds 23 hard items of 39. No second read checked the hardened
items.

## Open points for the orchestrating session

- The tracker's owner accepts or rejects the 29 additions, the 32 folds, the one move to the stretch
  page and the five edits in `data/programme/paper_edits.yaml`, all proposed.
- Friday's facts file notes M5 as "1,972 teams, 35.8 percent of them"; the paper and the guide print
  1,972 of the 5,507 teams, 35.8 percent, and Friday's learner files print only the 35.8 percent.
- Monday's synthetic idle tail averages about 39 peak online hours a driver a week against the 14
  and 16 of drivers E and F in the twelve rows, which a learner noticed on the stretch page.
- The hardened items rest on the two reads' rewrites with no second read; the room's rates in the
  item-analysis workbook are the first test of them.
- Interview Query, the Saturday row's student link, could not be reached on 13 October 2026, so no
  file in the pack carries it.
