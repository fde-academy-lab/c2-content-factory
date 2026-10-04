# Where did Build 1 Friday's pack come from, and what does each of its numbers rest on?

**INTERNAL.** The sources of every file in `content/W03/D5/`, every link with the day it was checked,
the data command and the checks behind each number, where each plant is used, every decision that
departs from the spine, the row or the first wave's pack, what was invented, the depth loop, and the
tool versions. The pack was raised to standard v3 in the US setting on 1 October 2026, on branch
`w03-d5`, from the first wave's pack of 29 September 2026 (pull request #161 and its follow-ups).
That session stopped at the account's usage limit while its second review round ran; a resumed
session on 4 October 2026 ran the round again, fixed its findings, ran the proofs and closed this
record.

---

## Which sources was the pack built from?

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules, the plant rule |
| `.claude/skills/day-pack-builder/references/the-standard.md` and `artifact-manifest.md` | The question ladder, the self-contained rule, the depth loop, and the build-week pack (GD prompts with facilitation notes for the expert days, about 30 minutes a group; no tests, no Kahoot) |
| `docs/detailing/W03_build1_spine.md`, approved 29 September 2026 | Friday's line (GD rounds on prompts that climb in complexity, a thread separate from the projects, the build freeze, two cold demo runs, the first presentations); the rule for a demo that fails; the three rubrics; the plant table and its witness numbers |
| `docs/curriculum/W3_Build_1.md`, Friday's row in its fifteen columns, and Monday's row | The scenario, the thinking trained (structured articulation under time pressure, unprepared by design), the agenda, the trainer notes (fifteen groups at 30 minutes is about 7.5 hours of GD across both expert days; the Principal Advisor takes a share online; the freeze tonight), GD topics at progressive complexity as a separate thread, two cold demo runs logged, the `[F]` interview angle, the one-slide answer (claim, evidence, caveat, action) |
| `docs/programme/calendar.md`, line W03/D5 | Fri 23 Oct, build week, Module 1, no faculty block, rendered through `sync:module:W03/D5`, `sync:day-date:W03/D5` and `sync:faculty-day:W03/D5` |
| `docs/07_Client_Zero.md`, sections 1a, 1b and 1c | Dr Priya Menon as Kalpa Health's COO; the GCC frame and Kavya Nair's review; Kalpa Health as a US diagnostics and revenue-cycle business across six metros, with four kinds of payer and seven denial categories |
| `data/programme/facts.yaml`, as of 1 October 2026 | The campus day (two blocks of 180 minutes); the cohort (35 learners and nine groups, stated); the W03 rubrics, learner-facing, rendered through `sync:rubric:W03/gd` and `sync:rubric:W03/mini-project`; decisions `four-domains`, `build1-us-data`, `build1-register-from-bookings`, `chapter-standard`, `question-ladder`, `self-contained`, `humanizer` and `opus-max`; addendum `health-us-facing` |
| `content/W03/D1/`, merged in #215 and #218 | The five askers' questions as the briefs word them; the briefing note and the data dictionary (each file's grain, the GCC frame, the week's days); Monday's plant table with its witness numbers, including the register drawn from the bookings; the domain dossier and card for US healthcare terms |
| `content/W03/SAT/` on main | The presentation format the first tranche follows, the mini project scoring sheet the first tranche is scored in, and the closure run sheet's expectation of seven Friday GD rounds and two on Saturday morning, with its Plan A, where slots 8 and 9 run from minute 10 and the expert's room presents from minute 40, which sets where a round moved to Saturday goes |
| The Week 1 and Week 2 packs on main (#203, #206 to #210, #217, #219 to #222) | The names of the moves the GD prompts ask for, as those packs teach them |

## Which links were checked, and when?

Every link below was opened on 1 October 2026, except row 11, opened on 4 October 2026. On 4 October
2026 the round 2 reviewer re-read rows 1 and 4 to 9 and found each still says what the pack says.
The STUDENT cards name each source with its date and carry no URL; the checklist carries its one URL
with its date.

| # | Source | URL | Checked | How, and what was read |
|---|---|---|---|---|
| 1 | Quest Diagnostics, Form 10-K for 2025, signed 26 February 2026 | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | checked 1 Oct 2026; re-read 4 Oct 2026 | curl, text searched: QuestHealth.com and consumer-initiated services; about 2,400 patient service centres; patients 12 percent of 2025 consolidated net revenues (the payer table's "% of Consolidated Net Revenues", DIS 98 percent) and "approximately 20 %" of consolidated net accounts receivable at 31 December 2025; rapid response laboratories that "quickly perform an abbreviated menu of routine tests for customers that require rapid turnaround times"; non-routine tests "may be performed less frequently than routine tests"; more than 45 million MyQuest users, scheduling and reminders; "select assets of the outreach laboratory services business of Allina Health" for $230 million on 16 September 2024; "Historically, hospitals were able to negotiate higher reimbursement rates..."; "zero-dollar out-of-pocket costs for members using preferred providers"; "The UnitedHealthcare Preferred Lab Network, which chose us to participate" |
| 2 | Medicare.gov, diagnostic laboratory tests | https://www.medicare.gov/coverage/diagnostic-laboratory-tests | checked 1 Oct 2026 | WebFetch: "You usually pay nothing for Medicare-covered diagnostic laboratory tests." |
| 3 | KFF, "Claims Denials and Appeals in ACA Marketplace Plans in 2024", 24 March 2026 | https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/ | checked 1 Oct 2026 | WebFetch: 19 percent of in-network claims denied in 2024, ranging from 3 to 36 percent by insurer |
| 4 | American Hospital Association, on the Change Healthcare cyberattack | https://www.aha.org/change-healthcare-cyberattack-underscores-urgent-need-strengthen-cyber-preparedness-individual-health-care-organizations-and | checked 1 Oct 2026; re-read 4 Oct 2026 | WebFetch: the attack of 21 February 2024 "encrypted and incapacitated significant portions of Change Healthcare's functionality"; "It annually processes 15 billion health care transactions", including "claims transmittals and payment" |
| 5 | CMS, fact sheet on CHOPD accelerated and advance payments, 9 March 2024 | https://www.cms.gov/newsroom/fact-sheets/change-healthcare-optum-payment-disruption-chopd-accelerated-payments-part-providers-advance | checked 1 Oct 2026; re-read 4 Oct 2026 | WebFetch: up to thirty days of average Medicare claims payments (claims paid 1 August to 31 October 2023, divided by three); "100% recoupment of Medicare claims payments" for 90 days, then a demand for any balance |
| 6 | eCFR, 45 CFR 164.502 | https://www.ecfr.gov/current/title-45/section-164.502 | checked 1 Oct 2026; re-read 4 Oct 2026, title 45 current to 1 October 2026 | Read through the eCFR API renderer (https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-45?part=164&section=164.502, checked 1 Oct 2026), title 45 current to 29 September 2026: 164.502(e)(1)(i) "satisfactory assurance", (e)(2) documented "through a written contract or other written agreement"; 164.502(d)(1) and (2), a disclosure to a business associate to create de-identified information, which falls outside the subpart; 164.502(a)(5)(ii)(A), no sale of protected health information "Except pursuant to and in compliance with § 164.508(a)(4)" (the pass 4 reviewer's copy of the same API text, read on 1 Oct 2026) |
| 7 | eCFR, 45 CFR 164.504 | https://www.ecfr.gov/current/title-45/section-164.504 | checked 1 Oct 2026; re-read 4 Oct 2026 | The same API: 164.504(e)(2)(i), the contract "may not authorize the business associate to use or further disclose the information in a manner that would violate the requirements of this subpart, if done by the covered entity", except for the business associate's own management and administration and data aggregation for the covered entity's health care operations; card 09 paraphrases the rule with that limit |
| 8 | Texas HHSC, Managed Care Uniform Terms and Conditions, version 1.3, section 4.10 | https://www.hhs.texas.gov/sites/default/files/documents/amended-star-health-2.pdf | checked 1 Oct 2026; re-read 4 Oct 2026 | WebFetch saved the PDF and pdftotext read it: 4.10(3)(a) and (b), the information and remote-access sentences; 4.10(4)(a), "Unless otherwise approved in advance by HHSC in writing"; 4.10(5)(c), the prior-approval exception, limited to work "that HHSC has approved in writing and that HHSC has confirmed will not involve the sharing of Confidential Information outside the United States"; Article 1, Confidential Information, item 4, protected health information in any form |
| 9 | AGS Health, company page | https://www.agshealth.com/company/ | checked 1 Oct 2026, twice; re-read 4 Oct 2026 | WebFetch: global headquarters "1015 18th St. NW Suite #1101 Washington DC, 20036"; "AGS Health was established with its first service center in Chennai, India"; "more than 15,000 skilled RCM professionals worldwide"; offices in Chennai, Vellore, Tirupati, Hyderabad, Bengaluru, Ahmedabad and Jaipur, and a near-shore centre in Guadalajara; US hospitals and health systems; coding, claims management and accounts receivable services |
| 10 | GitHub Docs, "Creating a codespace for a repository" | https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository | checked 1 Oct 2026 | WebFetch: branch menu, **Code**, the **Codespaces** tab, "Create a codespace on BRANCH" |
| 11 | Medicare.gov, "Get started with Medicare" | https://www.medicare.gov/basics/get-started-with-medicare | checked 4 Oct 2026 | WebFetch: "Medicare is health insurance for people 65 or older who meet citizenship or residency requirements", and "You may be eligible to get Medicare earlier if you have a disability, End-Stage Renal Disease (ESRD), or ALS"; behind card 02's "the federal insurance that covers most people of that age" and card 09's "the federal insurance for people aged 65 and over and some younger people with disabilities", which follow the dossier's definition |

**Checked and left out.** The HHS frequently asked questions on the Change Healthcare incident,
with its count of about 192.7 million individuals, refused curl and WebFetch with a 403 on 1 October
2026, and the session's egress policy blocked the Wayback Machine, so the card gives no count of
people affected. HHS's guidance that HIPAA sets no border on electronic records stored abroad
could not be read that day for the same reason, so card 10 rests its compliance edge on the Texas
clause alone; the domain dossier carries the HHS guidance, checked on 30 September 2026.

---

## How was the data pack checked, and which numbers come from it?

The pack copies no data. Every learner file that quotes Kalpa Health's figures reads them from
`content/W03/D1/data/`, written by `python3 data/generate_kalpa_health.py --out content/W03/D1/data
--stem C2_W03_D01`. On 1 October 2026, and again on 4 October 2026, that command, pointed at a
scratch folder, wrote ten files byte-identical to the committed ones; `--witness` ended `PASS every
plant holds`; Monday's `content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py` ended
`RESULT: PASS`; and the ten SHA-256 checksums in the cold-run script match the committed files.

`internal/C2_W03_D05_numbers_INTERNAL.py` is the record of every number the pack quotes. On 4
October 2026 it ends `RESULT: PASS (0 failures)` on 234 checks:

| Check | What it proves |
|---|---|
| The cards' data pack figures | 6,700 patients; 1,699 aged 65 and over, 25.4 percent; 1,250 in Dallas, about one in seven of them on Medicaid (14.4 percent on the register, a share card 10 prints only as one in seven); the Whole-body wellness panel at $299 and the Healthy aging panel by name; six laboratories and twelve patient service centres; each found on the card that quotes it |
| Each card's inputs and arithmetic | Every input a card's arithmetic starts from, found on the card; every result the prompts file prints, recomputed from those inputs with halves rounded up and, where a line multiplies a rounded figure, from the figure as printed (card 05's 18.7 percent, card 08's $15.08); card 03's second reading of the busiest day; the working days behind card 09's backlog counted from the calendar; card 03's Poisson check; the facilitation notes' $384 example; and the interview answer's 19 and 24 percent in the day sheet |
| The plant table | Every figure in the day sheet's plant table against the generator's witness and Monday's witness check, and the denial rates recounted from the claims file |
| The plant guard | No STUDENT file in the day folder carries a planted value, a plant's words, the 10.3, 10.35 or 10.348 percent denial rate, or any of the 83 counts of 20 or more in the generator's witness and Monday's witness check standing alone, bar three accepted by name: 30, the round's minutes and the rubric's marks; 64, card 03's New York samples a day; and 38, card 03's Atlanta samples a day and card 06's Atlanta batched share |
| The checksums | The ten files the cold-run script pins are the data pack's |

## Which numbers does each file quote, and where does each come from?

| File | Its numbers | Where they come from |
|---|---|---|
| The ten GD cards, STUDENT | The register, price list and site list figures above; the real facts in the links table; every other figure, marked on its card as an assumption with the head it comes from, or as an illustration | The data pack through the numbers script; the sources table; this pack's own design |
| The GD prompts, TRAINER | Each card's arithmetic, its plausible wrong number and its break-even; that the three-step swap clears all 362,880 draw orders under either of Monday's allocations | The numbers script; the swap simulation run on 4 October 2026 (below) |
| The facilitation notes, TRAINER | The same figures, rounded once more in the strongest discussions (about $14,000, about $720,000, about $15 of margin) | The prompts file |
| The day sheet, TRAINER | The plant table; the block grids; 270 minutes of GD for nine groups and 450 for fifteen; the 33 minutes of slack in block two; the interview answer's numbers | The witness through the numbers script; the roster workbook's verdicts |
| The checklist and the cold-run script, STUDENT | A slot of 25 to 30 minutes; about five minutes as the longest a cold run should take; ten minutes of cost before a challenges log entry; ten checksums | The spine's Saturday line; this pack's thresholds; the data pack |
| The roster and the scoring sheet, TRAINER | Rounds of 30 minutes, an opening of 15, blocks of 180, nine groups, the W03/gd criteria and 35 seats | The row; this pack; `data/programme/facts.yaml` |

The spine's plant table gives the retail denial rate as 10.4 percent, as does Monday's sheet. The
claims file marks 1,175 of the 11,355 retail claims denied, which is 10.348 percent: the witness
prints it to four places as 0.1035, and rounding that a second time gives 10.4. The day sheet says
10.3 percent, with the counts beside it.

---

## Where is each plant used, and who sees it?

| Plant | Where it appears | Audience |
|---|---|---|
| The headline and all five sub-problems, with their witness numbers | The expert's brief in the day sheet, each with the question that tests whether a group found it | TRAINER |
| The five sub-problems' ground | The prompts file keeps card 05 from sub-problems 3 and 5, card 06 from 4, and cards 09 and 10 from 3, since those groups would argue from a week's rehearsal or recognise card 10's Texas Medicaid totals from their own files; the roster flags a clash | TRAINER |

No STUDENT file names a plant. The numbers script's guard searches every STUDENT file in the day
folder for the spine's planted values (among them $180,000, 1,200 screenings, 23.0 and 12.2 percent,
180 repeated rows, 280 double posts, 398 unposted claims, the 18.8, 7.9, 19.0 and 15.1 percent no-show
rates and the 9 percent claim) and for the plants' words (employer, the new booking system, 18
September, month first, re-export, double posts, CLM- keys, KH-ATL-03, walk-in, campaign, at-home,
and Chicago beside Philadelphia), and, since round 2, for every count of 20 or more in the
generator's witness and Monday's witness check standing alone, with three coincidences accepted by
name as the numbers table above records, and finds none. On 4 October 2026 a scratch copy of card 01
with 253 rows, 64 samples and a 10.3 percent rate typed into it failed the guard on all three. Nine
near-misses were removed on the way:

| Where | What it was | What it is now |
|---|---|---|
| The cold-run script's docstring | Its example slide number was "$180,000", the employer contract's planted value | "$12,345" |
| Card 10 | The register's 180 Dallas patients on Medicaid, a true count that equals the 180 repeated rows by chance | "one in seven, 14.4 percent of 1,250" after pass 4, which round 2 found multiplies back to exactly 180 |
| Card 10, round 2 | "One in seven, 14.4 percent of 1,250" | "about one in seven of the 1,250", which multiplies back to about 179 |
| Card 05 | The fourteen labs' after-rate of 9.8 percent, which equals the next-worst centre's all-visit no-show rate | 9.9 percent, with the arithmetic recomputed |
| Cards 01 and 03 | "A January campaign" and "the spring campaign", which share sub-problem 5's word | "January's advertising" and "the spring advertising" |
| Card 01 | 150 panels a month, equal to the planted median claim and the employer panel's $150 | 160 panels, with the arithmetic recomputed |
| Card 06 | Chicago's 6,000 results, equal to the employer contract's 6,000 tests | 6,100, with Chicago's routine results at 5,600 |
| Cards 03 and 04 | Dallas's 60 samples a day and the 60 calls behind card 04's estimate, equal to the 60 text amounts | 59 samples and 66 calls, with the arithmetic recomputed |
| The cold-run script's docstring | A thousands-comma example of "1,231,001", the planted Q3 billed total, written while fixing pass 4's comma finding and caught by the widened guard | "12,345,678"; the script's seconds-to-minutes constant is written 60.0 so the guard can stay strict on a standalone 60 |

Decision `plants-once-found` covers only a regular week's Saturday paper, so it does not reach Build
1, and no file here relies on it.

---

## Which decisions depart from the spine, the row or the first wave's pack, and why?

| Decision | Why |
|---|---|
| The ten cards are new, and the first wave's ten are deleted | They carried the India setting, and three sat on plants' ground: the corporate contract card priced an employer screening deal beside the planted contract, the home collection card reused the campaign's 9 percent, and the league table card was a no-show table. Cards 03, 04 and 07 keep their first-wave ideas (same-day results, the phone line, the growth budget) in new US form. |
| The cards quote three files by name, the register, the price list and the site list, and two cards carry assumptions near the booking and claims files | Card 04's 15 percent by phone and 23,000 bookings sit near the legacy file's 15.3 percent and about 23,400 a year, and card 10's 800 claims and $35,000 are the files' Texas Medicaid totals doubled; neither is planted ground, and card 10 is kept from the billing groups, which work those files |
| Reading time goes by level: cards 01 to 04 read four minutes and discuss seventeen, cards 05 to 08 five and sixteen, cards 09 and 10 six and fifteen | Pass 5 measured every card past its stated reading time; the cards were cut and the reading time raised by level, so each round stays 30 minutes; the chair's opening covers what each card's last section asks of the group, and the card prints the minutes and the marks, so the reading minutes go to the case. Round 2 counted 488 to 849 words above the rules, each card within about 5 percent of its minutes at 140 words a minute, card 07 the tightest at 5.2 minutes |
| The cards do not name the Week 1 or 2 move they ask for, and their questions set up the situation without naming the analysis | Framing the problem is what the rubric's first criterion scores; the prompts file names the move so the chair can recognise it, and the optional move question was dropped so every group meets the same two questions |
| Card 09 runs on a Monday-to-Friday week | Pass 4 found the backlog counted on six days and the enrolment on five; five days is a US billing office's week, so the backlog is 13 working days, 910 claims and $71,500 |
| Card 08 asks for no Week 2 move | Its payment delay is folded into the margin as a cost of money, so the spare stays open to the billing groups, which own Week 2 Tuesday's move this week |
| Card 09 is set in the real outage of March 2024 | A public case the room can look up is more vivid than an invented outage; Kalpa is placed in it as an illustration and every Kalpa number on the card says so |
| The roster keeps card 05 from sub-problems 3 and 5, card 06 from 4 and cards 09 and 10 from 3, and its example allocation is Monday's Option B with the group of three on question 4 | So that the shipped draw shows no clash and matches Monday's sheet |
| The first wave's swap, within the level or card 08, gains a third step: swap two groups' draw positions where both moves are allowed | Round 2 found the two steps stuck in 7.28 percent of draw orders under Option B and 27.38 percent under Option A; with the third step `internal/C2_W03_D05_swap_check_INTERNAL.py` finds no draw left with a clash |
| A failed call's round, and a late expert's missed rounds, run first in stream B's three free Friday slots, and only then on Saturday after slot 9 | The first wave sent a failed call's round straight to Saturday, which round 2 found could put its group into a presentation slot with no setup time, and asked the trainer for end minutes the roster cannot compute, while stream B stood idle from minute 75 to 165 |
| The freeze is checked in one sweep at the close, run two counts only when nothing but the logs or the slide's wording changed after it, and each group keeps its cold-run log in its repository as `cold_run_log.md` | Round 2 found the TA's check gave no outcome for a commit after run two, which the checklist's own steps produce; the row asks for two cold runs "logged", and a log in the repository is one the TA can read at the close |
| GD scores are entered after the rounds, never shown to a group | The expert enters stream A's in block one's write-up, the Academic TA types stream B's from the Principal Advisor's scores, and both chairs settle gaps in block two's GD-notes slot, which the day sheet's grids already hold |
| A second GD stream online, difficulty climbing with the slot, and a first tranche of up to three presentations in whole clusters | Kept from the first wave (#161), and the Saturday run sheet on main plans on seven Friday rounds and two on Saturday morning |
| The roster workbook gains a builder, and both workbooks store computed values | The first wave left no builder for the roster; stored values let a reader that does not recalculate see the verdicts |
| No deck | The Friday fill names none, and the opening is spoken from the day sheet |
| The day sheet carries `sync:faculty-day:W03/D5` | It renders the calendar's "No IITGN faculty block on this day", so a change reaches the sheet with one sync |
| The first tranche is scored in Saturday's mini project scoring sheet | The Saturday run sheet on main expects Friday's tranche there |
| The retail denial rate reads 10.3 percent | See the numbers section; the spine and Monday's sheet should change to match |
| Card 10 prints the Dallas Medicaid share as about one in seven of the 1,250 | "One in seven, 14.4 percent of 1,250" multiplied back to exactly 180, the repeated rows' count |

## What was invented?

| Invented | Where |
|---|---|
| Every card figure marked as an assumption or an illustration, every stakeholder's line, and Dr Menon's asks, among them card 03's busiest day of about 10 samples above the average and card 10's tests at two thirds of what the plan pays | The ten cards |
| The five levels, the kept-from flags, the three-step swap, each card's positions, its plausible wrong numbers, card 03's second reading of the busiest day and its full-marks tables | The prompts file |
| The opening instruction, each card's added line, the moves table, the intervention lines, the chair's two questions per card, the strongest and weakest discussions, the evidence page, the seat cards, the fairness section, and the rules for a failed link, a failed call and a late expert, with stream B's free slots and Saturday as the last resort | The facilitation notes |
| The opening words, the ladder's answers, the roll call's question, the freeze rule's words, the sweep and the run-two comparison, the draw's steps and the moved round's slot, the table of what goes wrong, the Support TA's floor duty where the TA roster has them on site, and the interview answer in a trainee's voice | The day sheet |
| The table of what each script line means, the usual breaks, the two thresholds, the log's file name and a SQL group's commit line | The checklist |
| The Check rows for an empty slot and a draw position outside 1 to 9, the three swap steps in the Read me, the card 10 flip, and the scoring sheet's reading of a cleared Sat cell | The roster and the scoring sheet |
| The sixteen cold-run cases and the swap check's enumeration | `internal/C2_W03_D05_cold_run_cases_INTERNAL.py` and `internal/C2_W03_D05_swap_check_INTERNAL.py` |

---

## How did the depth loop run?

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every file built from the row, the spine and the dossier, in the day's order? | The first wave's cards, prompts and notes were in the India setting and three cards sat on plants' ground; the day sheet's no-show row quoted the old register | Every file rebuilt as recorded above |
| 2. Domain | The builder | Could a learner who has never worked in a business say, from each card alone, who asks, what a wrong call costs and which real company faces the same question? | Six US terms were used before they were explained: deductible, coinsurance and copay on card 02, in-network on card 05, the allowed share on card 07, payer enrolment on card 09, and MCO and GCC on card 10 | Each term glossed where it first appears; the January belief on card 01 attributed to the marketing head |
| 3. Problem first | The builder | Does each card state the decision before any number, lay its options and their sizes on the page, and leave the call to the group with what would change it named in the prompts? | Every card does; the prompts file gives each card's positions and the fact that would change the call | None needed beyond pass 2's |
| The humanizer's read | The builder, in file mode | Which of the humanizer's patterns remain in the prose? | A saying ("the real question"), a long appositive list, a run-on sentence on card 05, a contradictory "books by coming without booking", a doubled "whatever" on card 09, "slow money" on card 02 | Each rewritten; the contrasts kept are those where both halves carry information |
| 4. Rigor | A fresh reviewer, read-only, on the Opus model, 1 October 2026 | Does every number recount from the files or the card, does every real fact match its source, and does every rule a chair or a TA applies hold in every case? | One blocker and nine majors: AGS Health called Indian against its own page; the Texas approval route misread, since 4.10(5)(c) reaches only work that shares no Confidential Information; card 09 deciding a HIPAA question the rule leaves open; the AHA's list of what Change processes turned into what the attack stopped; card 04 setting lost revenue against a saved cost; Houston's 15 percent read as 50 without its condition; card 03's averages hiding the busiest days; card 10's wrong number inverted; card 09's six-day and five-day weeks mixed; the roster silent past nine groups and on a mistyped draw. Sixteen minors, among them coincidental echoes of planted values (150, 6,000, 60, 180), card 02's dominant option left uncomputed, four cold-run script edge cases, the scoring sheet's -1 learners, Quest's 12 percent being of consolidated revenues, and card 10's "every other payer" | Every finding fixed as the files now read, with the numbers script widened to check each card's inputs and every witness count; not taken: the optional Kodiak figure for card 09, left out to keep the card readable in its time |
| 5. Pedagogy and language | A fresh reviewer, read-only, on the Opus model, 1 October 2026 | Does every heading pass the headings-only read, does every file stand alone, and does the prose pass the humanizer and the house style? | Nine majors: the cards and the chair's added lines handed over the move the first criterion scores; no card readable in its stated time (495 to 918 words above the rules); three conflicting rules for a failed link and one for a late expert; scoring timed three ways; the cold-run check unrunnable as written; the frozen hash possibly not the demoed commit; one generic heading on all ten cards; "payer" never explained; boilerplate beats. Twenty-two minors, among them "post" for mailing, repeated moves on cards 02, 04 and 08, the group of three, broken pointers, undefined terms on the day sheet, sayings and closers, and the interview line printed as an instruction | Every finding fixed as the files now read; the cards now carry 486 to 845 words above their rules, read in four to six minutes by level; not taken as worded: the rules printed on the back of each card, since the chair's opening now carries them, and cards cut to about 400 and 550 words, since raising the reading time kept each card's evidence whole |
| Round 2 | A fresh reviewer, read-only, on the Opus model, 4 October 2026; the first attempt on 1 October stopped with the session | Do the fixes that changed a number, a key or a rule other files repeat agree everywhere, does each rule hold in every case it meets, and is each recomputed figure right? | No blocker: no wrong key, no named plant and no false fact, and all five corrected sources still say what the pack says. Seven majors: the freeze check gave no outcome when a commit followed run two, which the checklist's own steps produce; "with uncommitted changes" fired on files a notebook writes; three accounts of the 1-minute open, the opening leaving out bringing in a quiet member; the swap rule stuck in 7.3 percent of draws; the failed-call rule broke Saturday and asked for end minutes the roster cannot compute; the late-expert rule failed past three missed rounds; two files disagreed on who types the draw. Five minors: card 05's and card 08's printed arithmetic not reproducing their printed results ($186,900, $633.54, $520.41); card 03's listen-for line contradicting its own table; the day sheet's "10.35 percent" rounding twice; gaps in the plant guard (card 10's 14.4 percent of 1,250 multiplying to 180, no guard on 10.3 percent, Monday's counts unsearched, card 10's flag unasserted); this row's date | Every finding fixed: the sweep, the run-two comparison and `cold_run_log.md` in the day sheet and the checklist; git read before the notebook runs; one opening, which names bringing in a quiet member, with the cards' line and the prompts' sentence pointing at it; the third swap step in the prompts, the day sheet and the roster, with a flip proving card 10's flag; stream B's free slots first and Saturday after slot 9 last, the moved group presenting no earlier than the fourth slot of its room; the trainer types the draw; $187,000, $633.36 and $520.26; card 03's listen-for line and its second reading of the busiest day; 10.348 percent; card 10's "about one in seven of the 1,250"; the guard widened to every count of 20 or more in both witness outputs, with 30, 38 and 64 accepted by name |
| The builder's check of round 2's fixes | The builder, 4 October 2026 | Does every file that repeats a changed rule or number now say the same, and do the changed scripts and workbooks still prove themselves? | A search of the pack for every replaced phrase and number found none left outside this record; the numbers script, the recalc of both workbooks, the sixteen cold-run cases and the swap check all pass | None needed |
| The humanizer's read, after round 2 | The builder, in file mode, 4 October 2026 | Which of the humanizer's patterns remain in the prose, round 2's new lines among it? | Label fragments in the prompts file: ten "decision and metric" lines with no verb, ten plausible-wrong-number lines opening on a bare label, and ten full-marks blocks of criterion labels followed by fragments; fragment cells and lead-ins in the day sheet's envelope, its role table and five bold lead-ins; the checklist's dateline and two one-word cells; card 02's positions written as fragments; "a year's delay" for a three-month pilot | Each became a sentence; the full-marks blocks became two-column tables with a sentence per criterion; the pilot's risk reads three months in the prompts and the facilitation notes; the tic scanner finds 17 of 17 files clean |
| The headings-only read | The builder, 4 October 2026 | Read alone and in order, do every file's headings tell its argument as a chain of questions? | Every card, the prompts, the facilitation notes, the checklist, the day sheet and this record pass; the two recalc manifests opened on labels | Both manifests open on the question they prove |

---

## What could this record not establish?

- Whether the Programme Head runs nine groups, as facts.yaml states, or the tracker's fifteen; the
  roster's flips show both.
- Whether the HHS figures on the Change Healthcare breach have moved since the dossier's check on
  30 September 2026; the card does not quote them.
- Whether the Support TA is on site on Friday; no source in the repository gives the TA roster, so
  the day sheet assigns them the floor only where the roster has them on site.
- Whether 4.10's clause reaches Kalpa as a provider under the plan's contract; card 10 gives it as
  Kalpa's lawyers' reading, and no contract between a lab and a Texas Medicaid plan was read.
- Who hosts the Principal Advisor's online round on Saturday morning, and a round moved after it,
  since Saturday's run sheet has the Academic TA scribing the leader's room from minute 10; the
  change requests below ask the Saturday sheet to name them.
- Whether groups keep their cold-run log in their repositories as the checklist asks; the freeze
  sweep reads the run-two line there, and a group without one has its demo rerun on Saturday.

## Which tools and versions produced the numbers and files?

Python 3.11.15; openpyxl 3.1.5; PyYAML 6.0.1; pandas 3.0.6 (for the cold-run test notebook);
nbformat 5.11.1, nbconvert 7.17.1 and jupyter_core 5.9.1 (for the cold-run script's tests);
LibreOffice 24.2.7.2 (for both workbooks' stored values and for `scripts/xlsx_recalc.py`); poppler's
pdftotext 24.02.0 (for the Texas terms); git 2.43.0; mermaid-cli 11.17.0, installed in the session's
scratch folder because the container's `mmdc` reports 12.0.0, with Playwright's Chromium build 1243,
to render the five mermaid fences. The generator, the witness checks, the numbers script and the
cold-run case harness use the standard library only; the swap check adds openpyxl. The versions
were read again on 4 October 2026 and had not changed.

## Which proofs ran on 4 October 2026, and what did they print?

| Proof | Command | What it printed |
|---|---|---|
| The gate | `python3 scripts/verify.py content/W03/D5 --execute` | `PASS  25 files, every stem C2_W03_D05_ and every folder valid for a build day`; eleven WARN lines for marks language, one on each card and one on the checklist, which carry the W03 rubrics the requester ruled learners may see; the roster at 11 verdicts and 5 flips and the scoring sheet at 4 and 4; `RESULT: PASS (0 failures)` |
| The sync | `python3 scripts/sync_programme.py --check` | `every output is current` |
| The numbers | `python3 content/W03/D5/internal/C2_W03_D05_numbers_INTERNAL.py` | `RESULT: PASS (0 failures)` on 234 checks |
| The data | the generator into a scratch folder, `--witness`, and Monday's witness check | ten files byte-identical to the committed ones; `PASS every plant holds`; `RESULT: PASS (0 drifts from the spine and the day sheet)` |
| The workbooks | `python3 scripts/xlsx_recalc.py` on both manifests, and both builders rerun in a scratch tree | the verdicts and flips above; the rerun manifests byte-identical and the workbooks identical cell for cell, in formulas and in stored values |
| The cold-run script | `python3 content/W03/D5/internal/C2_W03_D05_cold_run_cases_INTERNAL.py` | sixteen cases PASS and `RESULT: PASS (0 failures)`; the script as it stood at 00aa2bf fails one, the notebook that writes a file |
| The swap rule | `python3 content/W03/D5/internal/C2_W03_D05_swap_check_INTERNAL.py` | 362,880 draw orders under each of Monday's allocations, a clash in 88.1 percent of them under Option A and 72.9 under Option B, and none left after the three steps |
| The plant guard's teeth | the numbers script on a scratch copy of card 01 with 253 rows, 64 samples and a 10.3 percent rate typed in | `FAIL  plant guard` naming all three |
| The distractor audit | `python3 scripts/distractor_audit.py content/W03/D5` | no option sets found, since a build day's pack carries no question set with options |
| The tic scanner | `python3 .claude/skills/llm-tic-scrubber/scripts/tic_scan.py content/W03/D5` | 17 of 17 files clean |
| The diagrams | mermaid-cli 11.17.0 on the five mermaid fences in the checklist, the prompts, the facilitation notes and the day sheet | all five render, and each was looked at |
| The reads | the headings-only read and the humanizer's read of every file | as the depth loop records |

The pack ships no deck, so no slide was built or rendered, and no notebook, so `--execute` found
nothing to run cold; the cold-run script is proved by its sixteen cases instead.

## Which changes does this pack ask of shared files?

| File | The change | Why |
|---|---|---|
| `docs/detailing/W03_build1_spine.md`, sub-problem 3's row, and Monday's day sheet's plant table | "1,137 denials, 10.4 percent" to "1,175 denied claims, 10.348 percent", with 1,137 kept as the denial postings | 1,175 of 11,355 is 10.348 percent; the witness prints 0.1035 and a second rounding gives 10.4. Thursday's pack asks the same |
| `data/generate_kalpa_health.py --witness` | Print the denied-claim count and its base beside `denial_rate_overall` | So no reader rounds the four-place rate a second time |
| `content/W03/SAT/trainer/C2_W03_SAT_closure_run_sheet_TRAINER.md` | Rerun the demo from the frozen commit "for any group whose run two did not count at Friday's freeze check", in place of "for any group with no second rehearsal cold run logged on Friday" | Friday's check now counts run two only when nothing but the logs or the slide's wording changed after it |
| The same run sheet | Say that a GD round Friday could not run takes the slot straight after slot 9 in the Principal Advisor's room, and that its group presents no earlier than the fourth slot of its room | Friday's facilitation notes and day sheet send such a round there |
| The same run sheet | Name who hosts the Principal Advisor's online round on Saturday morning | The sheet has the Academic TA scribing the leader's room from minute 10, the minute slot 9 starts |
| `scripts/verify.py` | Read the week's evaluation block before warning about marks language in a STUDENT file | The W03 rubrics are locked and learner-facing, so the eleven warnings on this pack are expected every run |
| `scripts/skills_index.py` | A flag that prints the index without rewriting `docs/skills-catalog.md` | A day session runs it as step 1 of skill selection and must not touch `docs/` |
