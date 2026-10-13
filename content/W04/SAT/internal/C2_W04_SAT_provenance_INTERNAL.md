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
the blueprint's pace, 9 easy, 19 medium and 11 hard (28 percent hard), with an untimed stretch page
of five. Ten bank items print (five of them reworded through `data/programme/paper_edits.yaml`),
thirty-two fold into deeper items, one moves to the stretch page, and twenty-nine additions come
from the week's source file. A blind guesser averages 6.4 of 39, and the key's guessing line sits at
10. The levels are the ones the second fix pass set after its blind check (below): 11 hard items is
the honest count, short of the decision's about 60 percent, which would be 23 or 24.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Which number should the plan chase, and which should a scheme pay for? | Q1 to Q7 | 19 | 3 | 2 | 2 |
| 2. Can the number survive the room, and can you size a city from nothing? | Q8 to Q14 | 23.5 | 1 | 5 | 1 |
| 3. Which pairs beat chance, and what is a slot worth? | Q15 to Q21 | 21.5 | 0 | 4 | 3 |
| 4. Where is the tier losing people? | Q22 to Q28 | 23 | 0 | 5 | 2 |
| 5. Which forecast earns the plan's trust? | Q29 to Q33 | 19 | 1 | 2 | 2 |
| 6. What changes when the method moves company? | Q34 to Q39 | 12 | 4 | 1 | 1 |
| Total | 39 | 118 | 9 | 19 | 11 |

The distractor audit passes with key positions a 8, b 6, c 8, d 8 and e 1, counting the single keys
and the letters of the four more-than-one keys, which share no letter across them (Q7 c, d, e; Q9
a, c; Q13 a, c; Q34 a, b, d). Among the 21 single keys, 3 tie for the longest option, 3 are or tie
for the shortest and 15 sit between. The proofs script, `C2_W04_SAT_key_proofs_INTERNAL.py`,
assembles the paper exactly as the builder does, recomputes every key from the five facts files and
the printed exhibits, and fails if any line the second fix pass took out comes back; it ends
"RESULT: PASS (39 items proved)".

## The fate of every bank item

| Bank | Type, the tracker's level | Fate | Where it is tested | Why |
|---|---|---|---|---|
| 1 | Fill in the blank, Easy | Printed | Q1 | As the tracker prints it |
| 2 | Fill in the blank, Medium | Printed | Q2 | As the tracker prints it |
| 3 | Fill in the blank, Easy | Folded | Q19, bank 32 | The call on the case and the charger turns on a lift of 0.97 against a confidence of 0.825, and the reason for option a, the most tempting wrong answer, is that confidence is the measure a popular item fools, so lift is the one that is not fooled. |
| 4 | Fill in the blank, Medium | Folded | Q19, bank 32 | The key reads the lift of 0.97 as case buyers taking a charger about as often as chance alone gives, slightly less, which is what a lift of about 1 means. |
| 5 | Fill in the blank, Easy | Folded | Q24, bank 35 | The honest headline needs each cohort read from the month its members joined, and its reason names the entry moment as what fixes a cohort. |
| 6 | Fill in the blank, Medium | Folded | Q29, bank 41 | The item asks for the seasonal naive by name and keys it as the same month a year earlier, which is the blank bank 6 fills. |
| 7 | Fill in the blank, Easy | Folded | Q33, kalpa-board | The board sentence the item keys gives the error on six months the forecast never saw and says none of them held a Diwali, and two wrong options stretch that error to festive months it was never measured on. |
| 8 | True or false, Easy | Folded | Q5, tf-target | The printed item is bank 8's statement, judged with its reason on Wells Fargo's cross-sell count, so the room has to say what the staff did and not only mark it true. |
| 9 | True or false, Easy | Folded | Q3, tf-leading | The printed item is bank 9's statement, judged with its reason on the Hyderabad dashboard, where the leading number has to be told apart from the north star it feeds. |
| 10 | True or false, Easy | Folded | Q19, bank 32 | Option a is the reading that a confidence above 0.8 is worth promoting, and the key refuses the bundle at a confidence of 0.825, which is bank 10's false statement shown false. |
| 11 | True or false, Medium | Folded | Q20, watch | The printed item judges bank 11's statement with its reason on the two thin pairs the week found, Kalpa's car phone mount and car charger and Instamart's ice cream and chocolate sauce, each at a support of 0.25 percent. |
| 12 | True or false, Hard | Folded | Q24, bank 35 | The set's two blends both read 41 percent while cohorts A and B both fall, which is bank 12's statement worked on numbers. |
| 13 | True or false, Medium | Folded | Q25, funnel-units | Option b divides every step by the sessions that opened the app, the single denominator bank 13 calls false, and its reason says why each step takes the step before as its base. |
| 14 | True or false, Easy | Folded | Q31, m5 | The sponsor's case is a curve that fits two years within 2 percent, and the key says a fit is no forecast, which is bank 14's false statement refused on the M5 scoreboard. |
| 15 | One correct option, Medium | Folded | Q7, kalpa-sheet | The exhibit is the lab's finding behind bank 15's reading, reorders per member up 1.22 times while their booked value per member fell to 0.96, and option a, the reorders north star, is wrong for the reason bank 15 keys. |
| 16 | One correct option, Medium | Folded | Q7, kalpa-sheet | Option a is the head of Retail-Plus's proposal, a number the app raised 1.22 times while booked value per member fell to 0.96 and no placement reached a member, so refusing it as the north star is the proxy test applied, a number a team can hit while the business gets worse. Q4 held this fold until its options stopped turning on the proxy test. |
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
| 29 | More than one correct, Hard | Printed, its stem, options reworded, at Medium | Q34 | The edit and its reason are in data/programme/paper_edits.yaml, status accepted |
| 30 | Scenario set, Medium | Printed, its situation reworded | Q17 | The edit and its reason are in data/programme/paper_edits.yaml, status accepted |
| 31 | Scenario set, Medium | Printed | Q18 | As the tracker prints it |
| 32 | Scenario set, Hard | Printed, its options reworded, at Medium | Q19 | The edit and its reason are in data/programme/paper_edits.yaml, status accepted |
| 33 | Scenario set, Medium | Printed | Q22 | As the tracker prints it |
| 34 | Scenario set, Hard | Printed, at Medium | Q23 | As the tracker prints it |
| 35 | Scenario set, Hard | Printed, its stem and options reworded, at Medium and 3 minutes | Q24 | The edit and its reason are in data/programme/paper_edits.yaml, status accepted |
| 36 | Scenario set, Medium | Folded | Q32, asym | The item asks for each forecast's mean absolute error from its misses summed by direction, the arithmetic of bank 36 on the week's own thirteen weeks. |
| 37 | Scenario set, Hard | Folded | Q33, kalpa-board | The board sentence the item keys is bank 37's answer to Anand on Kalpa's own months, the average miss on months the forecast had not seen. |
| 38 | Scenario set, Medium | Moved to the stretch page | Stretch 5 | A recall check on MAPE's denominator, kept untimed so the timed paper holds about 60 percent hard |
| 39 | Applied maths, Medium | Folded | Q21, margin | The item is bank 39's expected value with the cost line most analysts forget, a discount paid on adds that would have happened anyway. |
| 40 | Applied maths, Hard | Folded | Q18, bank 31 | The set computes a confidence and then a lift from three counts, the arithmetic of bank 40, on a pair whose lift falls below 1 where bank 40's reached 2.5. |
| 41 | Applied maths, Easy | Printed, its stem reworded | Q29 | The edit and its reason are in data/programme/paper_edits.yaml, status accepted |
| 42 | Applied maths, Easy | Folded | Q25, funnel-units | Reading the exhibit needs each step's conversion over the step before, which is what bank 42 asks for, in two units. |
| 43 | Applied maths, Hard | Folded | Q32, asym | The item's reason sets the vendor's mean miss of 16,400 against festival-aligned's 6,615, about 148 percent larger, the comparison bank 43 asks for on the week's own weeks. |

## The additions

Twenty-nine items come from the source file, seven of them Tuesday's, which decision
`papers-to-build` leaves to the content team and the key lists as waiting for the tracker.

| Q | Addition and its label | Type | Level | Minutes | Day |
|---|---|---|---|---|---|
| Q3 | tf-leading, "Judge the statement" | True or false | Easy | 2.5 | Mon |
| Q4 | twelve-rows, "Read six drivers" | One correct option | Hard | 4 | Mon |
| Q5 | tf-target, "Judge the statement on a case" | True or false | Easy | 2.5 | Mon |
| Q6 | wells-silent, "Size the 2013 change" | One correct option | Medium | 3.5 | Mon |
| Q7 | kalpa-sheet, "Mark the definition sheet" | More than one correct | Hard | 3.5 | Mon |
| Q8 | slide-order, "Build the slide" | Order the steps | Medium | 3.5 | Tue |
| Q9 | keep-two, "Keep two elements" | More than one correct | Hard | 2.5 | Tue |
| Q10 | concede, "Judge the defence" | True or false | Medium | 3.5 | Tue |
| Q11 | memo, "Judge the memo" | True or false | Easy | 2.5 | Tue |
| Q12 | estimate-order, "Order the estimate" | Order the steps | Medium | 4 | Tue |
| Q13 | four-checks, "Check four sources" | More than one correct | Medium | 4 | Tue |
| Q14 | metro, "Read the metro counts" | One correct option | Medium | 3.5 | Tue |
| Q15 | ctr-slot, "Read the strip by slot" | One correct option | Hard | 3.5 | Wed |
| Q16 | heavy, "Award the strip's slots" | One correct option | Medium | 4 | Wed |
| Q20 | watch, "Judge two high-lift pairs" | True or false | Hard | 3 | Wed |
| Q21 | margin, "Price the bundle slot" | One correct option | Hard | 3.5 | Wed |
| Q25 | funnel-units, "Read the flow two ways" | One correct option | Hard | 4 | Thu |
| Q26 | android, "Find the fix and its cost" | One correct option | Hard | 4 | Thu |
| Q27 | swiggy, "Read the weaned cohort" | One correct option | Medium | 3.5 | Thu |
| Q28 | kalpa-window, "Answer the app team" | One correct option | Medium | 3.5 | Thu |
| Q30 | calendar, "Set October and November" | Applied maths | Hard | 4 | Fri |
| Q31 | m5, "Answer the sponsor" | One correct option | Medium | 4 | Fri |
| Q32 | asym, "Price the misses" | One correct option | Hard | 4 | Fri |
| Q33 | kalpa-board, "Choose the board sentence" | One correct option | Medium | 4 | Fri |
| Q35 | brief-logistics, "Match: Kalpa Logistics" | Match the following | Easy | 1.5 | Sat |
| Q36 | brief-health, "Match: Kalpa Health" | Match the following | Easy | 1.5 | Sat |
| Q37 | brief-connect, "Match: Kalpa Connect" | Match the following | Easy | 1.5 | Sat |
| Q38 | brief-finance, "Match: Kalpa Financial Services" | Match the following | Easy | 1.5 | Sat |
| Q39 | amazon, "Set the plan share" | One correct option | Hard | 3.5 | Sat |

## The edits laid on the bank

All five sit in `data/programme/paper_edits.yaml` under W4 with status accepted, since the requester
accepted the paper's edits on 13 October 2026 and asked the same day for the paper to be edited;
each carries its reason, and none moves a key.

| Bank | Edit | Why |
|---|---|---|
| 29 | A stem setting Rohan Desai's ask and its twenty-to-one cost; option a names the definition written down before any number is read, option b a guardrail the measured cannot move, and option c the rupee amount each kind of wrong nudge costs | The tracker's stem carried no scenario, and its options b and c ran 21 and 31 characters against 60 for option a; a first wording of c read as the practice of pricing both errors, which carries over; and the blind check of 13 October 2026 found option a's list of a definition's parts printed Q2's answer, window |
| 30 | A situation of 1,000 round, illustrative consumer baskets with Business orders left out | Wednesday's lab found that Kalpa's 1,000 orders hold 812 consumer baskets once the 188 Business orders go, so "1,000 baskets" read as the lab's base trap |
| 32 | Option a names the case as well, at 106 characters | The key was the longest option by 9 characters |
| 35 | A stem that also asks what June's blend reads without cohort C, and four options crossing two halves, the headline (the existing cohorts' fall hidden by the new cohort, or the new members blamed on C's June against A's May) and the size (37.8 percent weighted, or 40.5 unweighted), each half printed twice | The key was the longest option by one character, an earlier c printed Q22's answer, and the blind second read found the key could be pieced together from a first clause two options shared and the item one idea once Q22 and Q23 are done |
| 41 | A stem set in 2025, when Diwali stayed in October | The tracker's stem names this October as the Diwali month, and Diwali falls on 8 November 2026; the spine's proposed stem keyed last year's Diwali month as the seasonal naive, which Friday's same-month definition refuses once the festival changes month |

## Decisions taken where the spine left a choice open

| Decision | What the pack does | Why |
|---|---|---|
| Folding against printing | 32 bank items fold into deeper items and print as their judgement, with the fold and its reason in the key | The bank fills 89 minutes at 11 hard of 43; printing it whole left 31 minutes for additions and no way to reach about 60 percent hard, and the spine's own table of additions runs to about 70 minutes. Weeks 1 and 2 folded the same way |
| Item 41 | The 2025 stem in place of the spine's proposal, and the calendar trap as the new Q30 | The spine's proposal would key a festival-month copy as the seasonal naive, which Friday's pack defines as the same month a year earlier |
| Part 2's count | Seven items against the spine's "about eight" | Flipkart's decimal slip, UPI's per-day count and DMart's average store fold into one more-than-one item, Q13, so the slip is judged beside two sound checks |
| The households in Q13 | Five lakh households, two million people at four to a household, set against an estimate of the city's UPI users | Tuesday's learner deck (S45) prints eight million households and the spine's draft nine, each more households than the city holds people, which a reader refuses on sight; the second fix pass kept the deck's lesson on units and moved the catch to households set against people |
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
| The second fix pass's layouts | Q6, Q10, Q24, Q26, Q27, Q31, Q32, Q33 and Q39 cross two halves, right and wrong on each, so each half of the key prints exactly as often as its rival half | The brief of 13 October 2026 asked for a two-by-two where a key could be pieced together; exercise-builder's bar forbids an option set whose options share the key's parts, and the brief wins as the requester's instruction, since in a two-by-two every option shares as much with its neighbours as the key does |
| Q4's two halves | The sum against the mean of ratios, and the six drivers against the city's own 1.58 | Tuesday's claim title, "the guarantee is paying for online hours that carry no trips", which Q8 has to offer, would answer any diagnosis or pay half of Q4, so Q4 now turns on halves Part 2 cannot touch; Monday's deck (S11) teaches both. Bank 16 moves its fold to Q7, whose option a is the number a team can hit while the business gets worse |
| Q8's lines | The stem prints Tuesday's four slots in order, from S7 of Tuesday's first deck; all seven lines carry a slot label, two claims, two pieces of evidence, one caveat and two actions | Printing the slots fixes the order, so the item turns on the denominator the scheme pays for and on the action that answers the caveat; a label that refutes itself, a topic title or a headline slot the template lacks, is gone. The builder now prints a seventh option letter, so (g) prints in place in the markdown and the Word paper |
| The answer sheet's ordering spaces | One space per letter of an ordering item's key, four for Q8 and four for Q12 | The blind check found seven spaces for Q8 and six for Q12 where each stem asks for four letters, and all-or-nothing marking fails a candidate who fills every space; `scripts/build_saturday_paper.py` now sizes the spaces by the key, so Week 2's Q8, six lines with a five-letter key, takes five spaces at its next Word rebuild |
| Q9 and Q12 | Q9 sets rider requests beside the wait and Rs 82 a completed trip beside Rs 2,836 an extra trip; Q12 adds a sixth step that moves the right comparison the wrong way, to about 6,450 | Each was one judgement by the blind read's count; each now carries a second, a near-miss a hurried analyst writes, so both stay Hard |
| Q13 | Medium; the stem prints the three sources' own words, option b keeps the 63 million against the stem's 6.3, and option d sets 5 lakh households against an estimate of UPI users | Five one-step checks under all-or-nothing marking are no deeper than one; the spine's eight or nine million households refuses itself on sight, households above people, so the households catch now turns on households against people, the unit Tuesday's deck (S45) teaches |
| Q24 | A stem and an option edit on bank 35, adding June's blend without cohort C, 37.8 percent weighted against 40.5 unweighted, the age claim taken out of the key, and the item printed at Medium | The situation never gives the cohorts' ages, and an older cohort A that still beats C's first month would make C weaker, so the key now says C retains above both existing cohorts in June instead; the blind check read the item medium, since Q22 and Q23 compute both blends just before it |
| Exhibit 5E and Part 5's opening | The "Puts the spike in" column and "none of them a Diwali month" are gone; the hidden-weeks sentence leaves Part 5's opening, and Exhibit 5D keeps only "hidden weeks" in its title | The column printed Q30's month and half of Q33, the caption Q33's limit, and the opening the half of Q31 that asks where a curve is scored |
| Words elsewhere | Every part's "what it shows" line names the part's question in plain words; Part 2's and Part 6's openings name no recommendation and no cost that changes; Exhibit 6A names each day's question; the labels of Q16, Q20, Q27 and Q30 say what the reader does; the match table's spare a names a wrong method in place of Q39's key | Each line told a reader which option to pick: "a check in the right unit" (Q12), "on weeks it never saw" (Q31), "the cost of an error that changed" (Q34, Q39), "Allow for heavy buyers" (Q16), "Move the spike" (Q30), and "a copy aligned to the festival, planned toward the costlier side", Q39's key in brief |
| The stretch page | Stretch 1 drops "well above the single weeks Exhibit 1B prints for E and F" and keeps the idle tail's averages; Stretch 2 sizes a test of one suggestion on invented rates, 5 to 8 percent; Stretch 4 asks whether reading the plan's place from the weeks that chose the forecast is circular | The clause pointed at Q4's sample half; Stretch 2's 6.25 percent was Instamart's pair, 100 of the 1,600 ice-cream carts, so it told a reader the pair goes to a test, Q20's half, and its first wording named the pair; Stretch 4 said the plan sits above the forecast and later where forecasts are scored, Q32's and Q31's halves. The answers keep Friday's 2.6 and 4.1 percent, and the key keeps Wednesday's 1,105 and 4,014 beside the invented 1,056 and 3,777 |
| Levels | 11 hard, 19 medium and 9 easy | An item stays Hard where the blind check of 13 October 2026 read it hard (Q4, Q9, Q15, Q26 and Q30), or where its medium read rested on a cue or leak this pass removed and the interviewer's cold read had read it hard (Q20, Q25, Q32 and Q39); Q7 and Q21, which the check did not sit and the interviewer read hard, stay Hard, Q7 with its lines' descriptions gone. Every other item the check read medium prints at Medium, whatever an earlier read said, and Q5, whose key restates Exhibit 1C's row, prints at Easy. No label was raised to reach a count; the decision's about 60 percent would be 23 or 24 |
| Q32's cost half | The options cross the error, the mean absolute error against misses netted before the sign is dropped, with the cost, festival-aligned taken as cheapest because its error is smallest against the vendor cheapest only because it errs on the cheap side, each forecast first set at its plan share | The blind check found options b and c refuting themselves with signed numbers and Q39 printing Q32's 0.82; with every option agreeing the vendor costs least, the cost half tested nothing, so it now turns on pricing the misses, Rs 11.9 lakh for the vendor against Rs 13.5 lakh for festival-aligned, and no option prints the 0.82 point, which would hand Q39 its share |
| Q39's share | About 0.35 against about 0.65, with no formula printed beside either | The options printed the formula, the late cost over both costs, which with Q32's 0.82 let a reader work the share backwards; the share is now worked from Exhibit 5D's Rs 5.42 and the stem's Rs 10 |
| Cues inside the changed items | Q6's stem drops "kept beside the definition"; Q10's concession names the fact granted, the rains ending inside the window; Q13's option c is shortened; Q15's slot-3 options pick the slot where milk clicks least, a reason that follows from their own diagnosis; Q16's stem drops the support floor, and its option d keeps the per-cart lift for one pair; Q20's key names the missing test; Exhibits 4A and 4C no longer explain the carousel; Exhibit 5C drops the 35.8 percent that named the bar; Exhibit 5D drops the line on where forecasts are scored; Q27's stem names the ten who joined and the five kept | Each was a cue the blind check named: a stem phrase pointing at the key, an option refuting itself, a key that was the longest option, a caption doing the item's step, or a second item settling the first |
| Lines answering items outside the changed set | Q7's lines b, d and e name their element without saying what it does; Q6's guardrail half no longer says what a guardrail catches; Q34's option a and match row d no longer list a definition's window; match row f drops "valued in margin"; the match table asks for "the method" in place of "the week's method" | Each gave a word-bank answer or settled an item the check did not sit: Q1's guardrails, Q2's window, Q3's leading input that moves first and Q21's margin; the match table's header endorsed a spare, the average of each row's own rate, as one of the week's methods. The word guardrail stays where an item needs it, without its definition |
| Q19's options | Left as the tracker prints them, with bank 32's accepted edit | The blind check noted that option a's "more than 80 percent" and option c's "below 1" bracket Q17's and Q18's answers; neither prints the three and two decimals those items ask for, and option c is the tracker's key, which has to state the lift's verdict |
| The Word paper's line on reading code | Printed only on a paper that carries code in an exhibit or a stem | The blind check found the Rules table telling the room to read Python 3 and PostgreSQL on a paper with no code; Weeks 1 and 2 carry code and keep the line |
| The key's slips | Q20's reason drops the 60,000 cart-page views a day that Q21's invented 30,000 contradicted, and its reason on option b is rewritten; Q30's line says the item is right only with all four numbers and November, which replaces the general rule's single number; the fold of bank 13 names option b, the option that divides by the opening sessions | The blind check found the first two and the general rule sitting oddly beside Q30's own line; the third slip was found while closing them |

## The numbers the pack derives

Every one is recomputed by the proofs script from the facts files or the printed exhibit.

| Number | Where | How |
|---|---|---|
| 1.19 trips per online hour and the mean of ratios 1.31; falls of 37 and 31 percent | Q4 | 88 trips over 74 hours; the average of the six drivers' own rates; 1.90 less 1.19 over 1.90, and 1.90 less 1.31 over 1.90 |
| About 36 percent; 57 percent as the trap | Q6 | 0.04 over 0.11; 0.04 over the other 0.07 |
| 0.8 percent | Q8, lines c and g | Rs 5,861 over Rs 5,817, from Monday's bookings per driver-week |
| Rs 2,836 an extra trip; Rs 82 a completed trip as the trap | Q9 | Rs 1.9 crore over 6,700 extra peak trips; Rs 1.9 crore over all 230,900 |
| 4,960 and 5,700 drivers; 5,000 checked; 3,900 and 6,450 as the traps | Q12 | 8,333 trips an hour over 1.68, times 1.15; 8,333 over the case's 1.90, times 1.15; one trap divides 8,333 trips by 2.13 requests per online driver-hour, the other multiplies 5,704 by 0.595 over 0.526 where it should divide |
| 802 million a day and Rs 146 crore a store, Rs 152 crore a store-year; 5 lakh households | Q13 and its key | 24.07 billion over 30 days; Rs 66,968 crore over the average of 415 and 500 stores; over about 439 store-years with 58 of 85 openings in the last quarter; two million people over four |
| 6 and 27 percent | Q14 | 60 lakh against 64.06 lakh and 82.45 lakh |
| 4.76, 2.85 and 1.35 clicks per 100 impressions; the strip's 3.8 | Q15 | Milk's share times the gap in each slot; half the impressions at 1.2 and half at 6.4 |
| Lifts 3.39 and 1.70 per cart | Q16 | 0.05 over 0.12 times 0.123; 0.075 over 0.22 times 0.20 |
| 0.825 and 0.97 | Q17, Q18 | 165 over 200; 0.825 over 0.85 |
| Rs 1,500 a day | Q21 | 375 new adds at Rs 10, less 750 adds at Rs 3 |
| 41 and 41 percent | Q22, Q23 | 1,640 over 4,000; 2,460 over 6,000 |
| About 37.8 percent, and 40.5 as the trap | Q24 | June without cohort C, 460 and 1,050 retained of 4,000; the unweighted mean of 46 and 35 |
| About 31 trips and 39 peak online hours a driver a week | Stretch 1 | Monday's `idle_trips_after` 33,440 and `idle_hours_after` 42,000 over the 180 idle-tail drivers and six weeks, 30.96 and 38.89 |
| 1,056 and 3,777 carts a half on invented rates of 5 and 8 percent | Stretch 2 | Wednesday's formula, the squared sum of the two z values for 5 percent two-sided and 80 percent power times the two rates' variances over the squared gap, which gives Wednesday's `trial_n_full` 1,105 and `trial_n_half` 4,014 for 6.25 to 9.45 percent |
| 71 to 70 and 65 to 64 percent; 80 percent on every platform | Exhibit 4D | Thursday's events table, per session, 1 August to 13 September against 14 to 30 September: checkout start to order for iOS members 0.713 to 0.700 and for non-members on Android 0.650 to 0.637, and add-to-cart to checkout start 0.800 in every member and platform segment. Thursday's facts file carries only the Android members' rates, so these were recomputed from the table at the orchestrator's review |
| 118, 34 and 61 percent | Q25 | Each step over the step before, per session and per member |
| 3,198 orders over 17 days, 1,317 a week, Rs 4.0 to 6.6 lakh; 1,223 against iOS | Q26 and its key | 14 points of 22,841 carts; 7 of 17 days; at Rs 300 and Rs 500; 13 points with iOS members as the comparator |
| 40 and 80 percent | Q27 | 4 of 10 and 4 of 5 |
| About 9 expected checkouts against 7; 3 fewer, 30 percent and 19 points as the traps | Q28 | 10 of 12 applied to 11 carts; 10 less 7; 3 over 10; 83 less 64 percent |
| Rs 444.7 lakh; Rs 308.9 lakh for October | Q30 and its key line | Rs 427.6 lakh times 1.04; Rs 297.0 lakh times 1.04 on the printed figure, Rs 308.8 lakh on Friday's unrounded revenue |
| MAE 6,615, 9,831 and 16,400; netted 346, 8,708 and 16,108; Rs 13.5, 30.5 and 11.9 lakh, so the smallest error is not the cheapest; Rs 8.8 and 10.0 lakh at the 0.82 point | Q32 | Friday's hold-out section: the high and low misses added and divided by 13, then netted against each other; each priced at Rs 5.42 and Rs 25; 25 over 25 plus 5.42 |
| Rs 2.08 crore under the plan line | Q33 | Rs 21.77 crore less Rs 19.69 crore |
| 0.65, and 0.35 as the trap | Q39 | 10 over 10 plus 650 over 120; 650 over 120 over the same sum |
| 0.81 | The drill's brief 4 | 30 over 30 plus 4,200 over 600 |

## Cold reads, the fix passes and the blind check

Two readers read the pack cold on 13 October 2026, findings only, and one fix pass answered both;
`C2_W04_SAT_cold_reads_INTERNAL.md` holds every finding with what the pass did. The learner, sitting
the paper against the clock from the STUDENT file alone, scored 39 of 39 in 103 minutes and found 22
things: 1 blocker (Q7's exhibit read two ways), 8 should fix and 13 notes; the pass fixed 18 and left
4 with their reasons. The hiring interviewer found 46: 2 blockers (Q11 credited Amazon's letter with a
lesson it does not draw, and Q8's order was arguable), 29 should fix and 15 notes, checked 31 real
facts with 29 confirmed and 2 differing, and read 15 of the 23 hard items as medium; the pass fixed
or relabelled 41 and left 5 with their reasons.

A blind second read then sat the fifteen items that pass rewrote, agreed with every key and found
every number right, and read eleven of the fifteen as medium, most because the paper handed their
answers over. The second fix pass, the same day, acted on every one of its findings and on the leaks
of the same kind it found itself. A blind check by a fresh agent then sat the nineteen items that pass
changed, from the STUDENT paper alone: all 19 answers matched the key, no key was wrong, and it read 5
of the 19 as hard and 14 as medium. It named the answer sheet's spaces for Q8 and Q12, six places
where another item, a caption or the stretch page settled a changed item, four answers printed
outside the changed set, the cues inside each item, three keys with a refinement a strong candidate
could raise, a stray rule and two slips in the key. The pass fixed every one but Q19's range and
direction, which print no decimals, and relabelled by the rule in the levels row; the cold-reads
file's last sections take them finding by finding. The paper rebuilt after it proves on all 39 keys,
passes the distractor audit and holds 11 hard items of 39.

## Open points for the orchestrating session

- The edits in `data/programme/paper_edits.yaml` carry status accepted, from the requester's
  acceptance of the paper's edits on 13 October 2026 and the ask of the same day that the paper be
  edited; the 29 additions, the 32 folds and the one move to the stretch page wait for the tracker's
  owner, as the key lists them.
- Friday's facts file notes M5 as "1,972 teams, 35.8 percent of them"; the key prints 1,972 of the
  5,507 teams, 35.8 percent, the guide prints the 1,972 of 5,507, the paper no longer prints either,
  and Friday's learner files print only the 35.8 percent.
- Monday's synthetic idle tail averages about 39 peak online hours a driver a week against the 14
  and 16 of drivers E and F in the twelve rows, which a learner noticed on the stretch page. Main's
  Monday deck (S9) and sheet, from #246, now say E and F keep shorter weeks than the tail's average,
  so the gap is explained where the room meets it; a merge of main into this branch, tried on 13
  October 2026, is clean, and the proofs, verify and both checks pass on it.
- Q20, Q25, Q32 and Q39 print at Hard on the levels row's rule after the blind check read them
  medium for cues this pass removed, and no second sitting has read them, since the skill allows one
  sitting a paper; the room's rates in the item-analysis workbook are the first test of them, and of
  11 hard items against the decision's about 60 percent.
- Interview Query, the Saturday row's student link, could not be reached on 13 October 2026, so no
  file in the pack carries it.
