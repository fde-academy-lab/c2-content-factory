# Where did Build 1 Friday's pack come from, and what does each of its numbers rest on?

**INTERNAL.** The sources of every file in `content/W03/D5/`, every link with the day it was checked,
the data command and the checks behind each number, where each plant is used, every decision that
departs from the spine, the row or the first wave's pack, what was invented, the depth loop, and the
tool versions. The pack was raised to standard v3 in the US setting on 1 October 2026, on branch
`w03-d5`, from the first wave's pack of 29 September 2026 (pull request #161 and its follow-ups).

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
| `content/W03/SAT/` on main | The presentation format the first tranche follows, the mini project scoring sheet the first tranche is scored in, and the closure run sheet's expectation of seven Friday GD rounds and two on Saturday morning |
| The Week 1 and Week 2 packs on main (#203, #206 to #210, #217, #219 to #222) | The names of the moves the GD prompts ask for, as those packs teach them |

## Which links were checked, and when?

Every link below was opened on 1 October 2026. The STUDENT cards name each source with that date and
carry no URL; the checklist carries its one URL with its date.

| # | Source | URL | Checked | How, and what was read |
|---|---|---|---|---|
| 1 | Quest Diagnostics, Form 10-K for 2025, signed 26 February 2026 | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | checked 1 Oct 2026 | curl, text searched: QuestHealth.com and consumer-initiated services; about 2,400 patient service centres; patients 12 percent of 2025 diagnostic net revenues and 20 percent of net receivables at 31 December 2025; rapid response laboratories, "24 hours a day, 365 days a year"; more than 45 million MyQuest users, scheduling and reminders; Allina Health's outreach business for $230 million on 16 September 2024 (OhioHealth's for $200 million on 13 October 2024 and University Hospitals' for $183 million on 30 December 2024, used only in TRAINER notes); "Historically, hospitals were able to negotiate higher reimbursement rates..."; "high value, lower cost providers", "zero-dollar out-of-pocket costs for members using preferred providers", "The UnitedHealthcare Preferred Lab Network, which chose us to participate" |
| 2 | Medicare.gov, diagnostic laboratory tests | https://www.medicare.gov/coverage/diagnostic-laboratory-tests | checked 1 Oct 2026 | WebFetch: "You usually pay nothing for Medicare-covered diagnostic laboratory tests." |
| 3 | KFF, "Claims Denials and Appeals in ACA Marketplace Plans in 2024", 24 March 2026 | https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/ | checked 1 Oct 2026 | WebFetch: 19 percent of in-network claims denied in 2024, ranging from 3 to 36 percent by insurer |
| 4 | American Hospital Association, on the Change Healthcare cyberattack | https://www.aha.org/change-healthcare-cyberattack-underscores-urgent-need-strengthen-cyber-preparedness-individual-health-care-organizations-and | checked 1 Oct 2026 | WebFetch: the attack of 21 February 2024 "encrypted and incapacitated significant portions of Change Healthcare's functionality"; "annually processes 15 billion health care transactions"; disrupted "claims transmittals and payment" |
| 5 | CMS, fact sheet on CHOPD accelerated and advance payments, 9 March 2024 | https://www.cms.gov/newsroom/fact-sheets/change-healthcare-optum-payment-disruption-chopd-accelerated-payments-part-providers-advance | checked 1 Oct 2026 | WebFetch: up to thirty days of average Medicare claims payments (claims paid 1 August to 31 October 2023, divided by three); "100% recoupment of Medicare claims payments" for 90 days, then a demand for any balance |
| 6 | eCFR, 45 CFR 164.502 | https://www.ecfr.gov/current/title-45/section-164.502 | checked 1 Oct 2026 | Read through the eCFR API renderer (https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-45?part=164&section=164.502, checked 1 Oct 2026), title 45 current to 29 September 2026: 164.502(e)(1)(i) "satisfactory assurance", (e)(2) documented "through a written contract or other written agreement" |
| 7 | eCFR, 45 CFR 164.504 | https://www.ecfr.gov/current/title-45/section-164.504 | checked 1 Oct 2026 | The same API: 164.504(e)(2)(i), the contract "may not authorize the business associate to use or further disclose the information in a manner that would violate the requirements of this subpart, if done by the covered entity" |
| 8 | Texas HHSC, Managed Care Uniform Terms and Conditions, version 1.3, section 4.10 | https://www.hhs.texas.gov/sites/default/files/documents/amended-star-health-2.pdf | checked 1 Oct 2026 | WebFetch saved the PDF and pdftotext read it: 4.10(3)(a) and (b), the information and remote-access sentences; 4.10(4)(a), "Unless otherwise approved in advance by HHSC in writing" |
| 9 | AGS Health, company page | https://www.agshealth.com/company/ | checked 1 Oct 2026 | WebFetch: "more than 15,000 skilled RCM professionals worldwide"; delivery centres in Chennai, Vellore, Tirupati, Hyderabad, Bengaluru, Ahmedabad and Jaipur; US hospitals and health systems; coding, claims management and accounts receivable services |
| 10 | GitHub Docs, "Creating a codespace for a repository" | https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository | checked 1 Oct 2026 | WebFetch: branch menu, **Code**, the **Codespaces** tab, "Create a codespace on BRANCH" |

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
--stem C2_W03_D01`. On 1 October 2026 that command, pointed at a scratch folder, wrote ten files
byte-identical to the committed ones; `--witness` ended `PASS every plant holds`; Monday's
`content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py` ended `RESULT: PASS`; and the ten
SHA-256 checksums in the cold-run script match the committed files.

`internal/C2_W03_D05_numbers_INTERNAL.py` is the record of every number the pack quotes. It ends
`RESULT: PASS (0 failures)` on 164 checks:

| Check | What it proves |
|---|---|
| The cards' data pack figures | 6,700 patients; 1,699 aged 65 and over, 25.4 percent; 1,250 in Dallas, 180 of them on Medicaid, 14.4 percent; the Whole-body wellness panel at $299 and the Healthy aging panel by name; six laboratories and twelve patient service centres; each found on the card that quotes it |
| Each card's arithmetic | Every result the prompts file prints, recomputed from the card's own exhibit with halves rounded up, and the interview answer's 19 and 24 percent in the day sheet |
| The plant table | Every figure in the day sheet's plant table against the generator's witness and Monday's witness check, and the denial rates recounted from the claims file |
| The plant guard | No STUDENT file in the day folder carries a planted value or a plant's words |
| The checksums | The ten files the cold-run script pins are the data pack's |

## Which numbers does each file quote, and where does each come from?

| File | Its numbers | Where they come from |
|---|---|---|
| The ten GD cards, STUDENT | The register, price list and site list figures above; the real facts in the links table; every other figure, marked on its card as an assumption with the head it comes from, or as an illustration | The data pack through the numbers script; the sources table; this pack's own design |
| The GD prompts, TRAINER | Each card's arithmetic, its plausible wrong number and its break-even | The numbers script |
| The facilitation notes, TRAINER | The same figures, rounded once more in the strongest discussions (about $14,000, about $720,000) | The prompts file |
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
| The five sub-problems' ground | The prompts file keeps card 05 from sub-problems 3 and 5, card 06 from 4 and card 09 from 3, since those groups would argue from a week's rehearsal; the roster flags a clash | TRAINER |

No STUDENT file names a plant. The numbers script's guard searches every STUDENT file in the day
folder for the spine's planted values (among them $180,000, 1,200 screenings, 23.0 and 12.2 percent,
180 repeated rows, 280 double posts, 398 unposted claims, the 18.8, 7.9, 19.0 and 15.1 percent no-show
rates and the 9 percent claim) and for the plants' words (employer, the new booking system, 18
September, month first, re-export, double posts, CLM- keys, KH-ATL-03, walk-in, campaign, at-home,
and Chicago beside Philadelphia), and finds none. Four near-misses were removed on the way:

| Where | What it was | What it is now |
|---|---|---|
| The cold-run script's docstring | Its example slide number was "$180,000", the employer contract's planted value | "$12,345" |
| Card 10 | The register's 180 Dallas patients on Medicaid, a true count that equals the 180 repeated rows by chance | "one in seven, 14.4 percent of 1,250" |
| Card 05 | The fourteen labs' after-rate of 9.8 percent, which equals the next-worst centre's all-visit no-show rate | 9.9 percent, with the arithmetic recomputed |
| Cards 01 and 03 | "A January campaign" and "the spring campaign", which share sub-problem 5's word | "January's advertising" and "the spring advertising" |

Decision `plants-once-found` covers only a regular week's Saturday paper, so it does not reach Build
1, and no file here relies on it.

---

## Which decisions depart from the spine, the row or the first wave's pack, and why?

| Decision | Why |
|---|---|
| The ten cards are new, and the first wave's ten are deleted | They carried the India setting, and three sat on plants' ground: the corporate contract card priced an employer screening deal beside the planted contract, the home collection card reused the campaign's 9 percent, and the league table card was a no-show table. Cards 03, 04 and 07 keep their first-wave ideas (same-day results, the phone line, the growth budget) in new US form. |
| The cards quote only the register, the price list and the site list | No booking, claim, posting, visit or campaign figure reaches a card, so no card can echo or confirm a plant |
| Cards 07 to 10 read for four minutes and discuss for seventeen | Their exhibits run to about 700 to 900 words; the round stays 30 minutes |
| The cards do not name the Week 1 or 2 move they ask for | Framing the problem is what the rubric's first criterion scores; the prompts file names the move, and the chair may ask for it after the discussion |
| Card 09 is set in the real outage of March 2024 | A public case the room can look up is more vivid than an invented outage; Kalpa is placed in it as an illustration and every Kalpa number on the card says so |
| The roster keeps card 05 from sub-problems 3 and 5, card 06 from 4 and card 09 from 3, and its example allocation is reordered | So that the shipped draw shows no clash; the first wave's rule of a swap within the level or card 08 holds |
| A second GD stream online, difficulty climbing with the slot, and a first tranche of up to three presentations in whole clusters | Kept from the first wave (#161), and the Saturday run sheet on main plans on seven Friday rounds and two on Saturday morning |
| The roster workbook gains a builder, and both workbooks store computed values | The first wave left no builder for the roster; stored values let a reader that does not recalculate see the verdicts |
| No deck | The Friday fill names none, and the opening is spoken from the day sheet |
| The day sheet carries `sync:faculty-day:W03/D5` | It renders the calendar's "No IITGN faculty block on this day", so a change reaches the sheet with one sync |
| The first tranche is scored in Saturday's mini project scoring sheet | The Saturday run sheet on main expects Friday's tranche there |
| The retail denial rate reads 10.3 percent | See the numbers section; the spine and Monday's sheet should change to match |

## What was invented?

| Invented | Where |
|---|---|
| Every card figure marked as an assumption or an illustration, every stakeholder's line, and Dr Menon's asks | The ten cards |
| The five levels, the kept-from flags, each card's positions, its plausible wrong numbers and its full-marks blocks | The prompts file |
| The opening instruction, each card's added line, the moves table, the intervention lines, the panel's two questions per card, the strongest and weakest discussions, the evidence page and the fairness section | The facilitation notes |
| The opening words, the roll call's question, the freeze rule's words and checks, the draw's steps, the table of what goes wrong and the interview answer in a trainee's voice | The day sheet |
| The table of what each script line means, the usual breaks, and the two thresholds | The checklist |
| The example allocation on the roster's Inputs sheet | The roster |

---

## How did the depth loop run?

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every file built from the row, the spine and the dossier, in the day's order? | The first wave's cards, prompts and notes were in the India setting and three cards sat on plants' ground; the day sheet's no-show row quoted the old register | Every file rebuilt as recorded above |
| 2. Domain | The builder | Could a learner who has never worked in a business say, from each card alone, who asks, what a wrong call costs and which real company faces the same question? | Six US terms were used before they were explained: deductible, coinsurance and copay on card 02, in-network on card 05, the allowed share on card 07, payer enrolment on card 09, and MCO and GCC on card 10 | Each term glossed where it first appears; the January belief on card 01 attributed to the marketing head |
| 3. Problem first | The builder | Does each card state the decision before any number, lay its options and their sizes on the page, and leave the call to the group with what would change it named in the prompts? | Every card does; the prompts file gives each card's positions and the fact that would change the call | None needed beyond pass 2's |
| The humanizer's read | The builder, in file mode | Which of the humanizer's patterns remain in the prose? | A saying ("the real question"), a long appositive list, a run-on sentence on card 05, a contradictory "books by coming without booking", a doubled "whatever" on card 09, "slow money" on card 02 | Each rewritten; the contrasts kept are those where both halves carry information |
| 4. Rigor | A fresh reviewer, read-only | See below | See below | See below |
| 5. Pedagogy and language | A fresh reviewer, read-only | See below | See below | See below |

---

## What could this record not establish?

- Whether the Programme Head runs nine groups, as facts.yaml states, or the tracker's fifteen; the
  roster's flips show both.
- Whether the HHS figures on the Change Healthcare breach have moved since the dossier's check on
  30 September 2026; the card does not quote them.

## Which tools and versions produced the numbers and files?

Python 3.11.15; openpyxl 3.1.5; PyYAML 6.0.1; pandas 3.0.6 (for the cold-run test notebook);
nbformat 5.11.1, nbconvert 7.17.1 and jupyter_core 5.9.1 (for the cold-run script's tests);
LibreOffice 24.2.7.2 (for both workbooks' stored values and for `scripts/xlsx_recalc.py`); poppler's
pdftotext (for the Texas terms); git 2.43.0. The generator, the witness checks and the numbers
script use the standard library only.
