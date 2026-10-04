# Provenance: Week 3, Saturday, the Build 1 close

**INTERNAL.** Where every fact in this day's files came from, what the pack decided where a source left
a call open, and the depth loop's record. Raised to standard v3 in the US setting on 1 October 2026,
over the first wave of 29 September 2026.

## Which sources does the pack rest on?

| What | Source | Status |
|---|---|---|
| The day's date, module and focus | `docs/programme/calendar.md`, line W03/SAT, and the sync blocks in each TRAINER file | Locked calendar, 21 September 2026 |
| The row | `docs/curriculum/W3_Build_1.md`, Saturday 24 October, all fifteen columns, and Monday's row for the week | Tracker v7 |
| The spine, its rubrics, the rule for a failed demo, and the plants | `docs/detailing/W03_build1_spine.md`, approved 29 September 2026; its sub-problem 4 row re-planted on 1 October 2026 (decision `build1-register-from-bookings`) | Approved |
| Kalpa Health in the US | `docs/07_Client_Zero.md` section 1c; decisions `four-domains` and `build1-us-data` in `data/programme/facts.yaml` | Addendum of 30 September 2026 |
| The 300-minute Saturday | `data/programme/facts.yaml`, `campus_day.saturday_minutes` | Locked |
| 35 learners in nine groups, eight of four and one of three | `data/programme/facts.yaml`, `cohort`, and its `groups` conflict with the tracker's fifteen | Stated (handover) |
| Marks per event (mini project 40, mock 30, GD 30) and the Build 1 rubrics, learner-facing, with the graded days | `data/programme/facts.yaml`, `evaluation` and `evaluation.rubrics.W03`, approved 29 September 2026; read by both workbook builders and rendered by the sync into the bank, the run sheet and the presentation deck | Locked |
| The five askers' questions, word for word | `content/W03/D1/briefs/C2_W03_D01_brief_{1..5}_*_STUDENT.md` and the briefing note, merged in #215 | Monday's pack |
| The data files' columns and what each system says one row is | `content/W03/D1/briefs/C2_W03_D01_data_dictionary_STUDENT.md` | Monday's pack |
| The plant table Monday's trainers hold | `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md`, "What is planted in each brief's files" | Monday's pack |
| Terms, roles and the revenue-cycle metrics | `content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, sections 2 to 6 | Monday's dossier |
| Claim, evidence, caveat, action | `content/W01/D4/slides/C2_W01_D04_half1_STUDENT.md`, S5, "The note" | Week 1 Thursday, merged |
| Restate, bound, offer the test | `content/W01/D5/slides/C2_W01_D05_rehearsal_STUDENT.md`, S6 and S7 | Week 1 Friday, merged |
| The names of the Weeks 1 and 2 moves | The decks of `content/W01/D1` to `D5` and `content/W02/D1` to `D5` (each chapter's question), and the "Week 1 or 2 move" column of Monday's briefs | Merged at v3 |
| The week's seven interview questions and their tags | `docs/curriculum/W3_Build_1.md`, the interview angle of each row | Tracker v7 |
| Meera's Week 4 Monday words | `docs/curriculum/W4_Analyst_craft.md`, Monday 26 October, business scenario | Tracker v7 |
| Build 2 opens on Tuesday 10 November in Kalpa Financial Services | `docs/programme/calendar.md`, line W06/D2 | Locked calendar |
| Friday's seven GD rounds, the first tranche of up to three, the freeze and the drawn order | `content/W03/D5/trainer/C2_W03_D05_day_sheet_TRAINER.md`, as merged on 1 October 2026 (first wave); a parallel session is rebuilding it | Friday's pack |
| The presentation format is handed out at Wednesday's close | `content/W03/D3/trainer/C2_W03_D03_day_sheet_TRAINER.md` and `content/W03/D3/checkpoints/C2_W03_D03_headline_claim_STUDENT.md` (first wave) | Wednesday's pack |

## Which real-world facts appear, and where was each checked?

| Fact, as the pack prints it | Where it appears | Source, read on 1 October 2026 |
|---|---|---|
| Quest Diagnostics' diagnostic information services, its laboratory business, had second-quarter 2026 revenues of $2,978 million, up 10.3 percent on 2025; requisition volume rose 13.1 percent and revenue per requisition fell 2.8 percent, both against 2025 | Presentation deck, D11 | Quest Diagnostics, "Quest Diagnostics Reports Second Quarter 2026 Financial Results; Raises Revenue and EPS Guidance for Full Year 2026", 23 July 2026, https://www.prnewswire.com/news-releases/quest-diagnostics-reports-second-quarter-2026-financial-results-raises-revenue-and-eps-guidance-for-full-year-2026-302832675.html (verified 1 Oct 2026, read twice); the three figures sit together in the release's three-months comparison table for the segment; total revenues were $3,043 million, up 10.2 percent, which the first build quoted beside the segment's rows until the rigor review caught the mix |
| Optum India is UnitedHealth Group's largest Global Capability Center, providing healthcare operations, technology, analytics and support services, with hubs in Gurugram, Noida, Bengaluru, Hyderabad, Pune and Chennai | Week close, D5 | UnitedHealth Group careers, India, https://www.unitedhealthgroup.com/careers/in/work.html (verified 1 Oct 2026, read twice) |
| AGS Health provides healthcare billing, coding and analytics to large US healthcare organizations (nearly half of the 20 most prominent US hospitals and 40 percent of the 10 largest health systems, in its words), with more than 15,000 revenue-cycle professionals worldwide and delivery centres in Chennai, Vellore, Tirupati, Hyderabad, Ahmedabad, Jaipur and Bengaluru | Week close, D5 | AGS Health, company page, https://www.agshealth.com/company/ (verified 1 Oct 2026, read twice) |

The segment's revenue growth and its two requisition percentages do not multiply to each other
exactly (1.131 times 0.972 is 1.099, against 10.3 percent), and the release does not show how they
combine, so the deck states the three figures side by side and its note says they do not multiply. The deck's note mentions that Quest runs patient service
centres and laboratories without a count, since the count (about 2,400, in Monday's dossier) was not
re-read today.

## Which numbers does the pack quote, and what recomputes them?

Every number in the TRAINER files comes from `internal/C2_W03_SAT_witness_INTERNAL.py`, which reads the
ten CSV files in `content/W03/D1/data/` the way a group would and compares 53 figures with the spine,
216 further figures with the bank the TRAINER files quote, and 14 dates, ids and yes-or-no findings
exactly. A figure passes only to the last place the table prints it; the shuffled chance checks
(20,000 shuffles, a fixed seed) carry a wider tolerance of their own. Its run on 1 October 2026 ends
`RESULT: PASS (0 disagreements with the spine, the bank and the facts)`. The generator's own witness,
`python3 data/generate_kalpa_health.py --witness`, ends `PASS every plant holds` on the same day.

The STUDENT files quote no number from the data pack beyond what Monday's briefs give learners (Dr
Menon's 5 and 18 percent, the 9 percent lift, KH-ATL-03 as the worst centre, 6,700 patients), the
rubric's marks, Quest's three segment figures and the invented figures listed below.

## Where is each plant used, and does any reach a learner?

| Plant | TRAINER files that name it | STUDENT files |
|---|---|---|
| The headline: the dashboard counts old-system retail tests, a panel as its components | Question bank, run sheet, week-close notes | None |
| The employer contract and panels billed as one claim line | Question bank, run sheet, week-close notes | None |
| The booking-system switch in Chicago and Philadelphia, the old export's repeats and the month-first dates | Question bank, run sheet, week-close notes | None |
| The claim-key formats, the double posts, the unposted employer claim and the denials paying nothing | Question bank, run sheet, week-close notes | None |
| KH-ATL-03's appointments against the walk-ins, on the register drawn from the bookings | Question bank, run sheet, week-close notes | None |
| The offer's targeting by metro and the negative split inside the campaign metros | Question bank, run sheet, week-close notes | None |

Decision `plants-once-found` covers only a regular week's Saturday paper, so no Build 1 STUDENT file
names a plant, hints at its size or reuses a planted value. The presentation deck's examples run on an
invented turnaround quarter, on the lab director's question, which none of the five briefs asks.

## What is invented, and where is each invention labelled?

| Invention | Where | How it is labelled |
|---|---|---|
| The lab director's turnaround quarter: median draw to released result 22 hours in Q2 and 18 in Q3 on 9,400 tests, 14 hours in Q3 timed from arrival at the lab; the courier run; the draw sites' clocks moving by an hour in July; 200 samples timed by hand | Presentation deck, D12 to D16, D23's note, D37, D40; the run sheet's one-breath interview answer | "invented" on each slide that uses it; the run sheet says the trainer models only this invented answer |
| A decisions-log row: 14 blank age bands, kept and labelled unknown, with a reason that restates the issue | Presentation deck, D21 and D22 (D20 shows what each cell holds, with no invented call) | "the invented row"; the question's note says the real files' age bands have no blanks |
| The weak and usable sentences for Build 2, the five demo steps to order, and the replies and reasons in the question slides | Presentation deck, D21, D24, D30, D38; week close, S8 | Generic examples, attached to no Kalpa number |
| The seat labels G1-S1 to G9-S3 and the sample entries in the recalc manifests | Both workbooks and their manifests | Test entries only; the committed workbooks are empty templates |

## Which decisions did this pack take where the sources left the call open?

| Decision | Why | Where it landed |
|---|---|---|
| The rule for a failed demo, set by the orchestrating session on 29 September 2026, is applied in both workbooks as checks: each group's demo outcome is recorded; the group's 34 are required whatever the outcome; a learner in a group whose demo still failed cannot close on full marks for presentation and defence | The rubric's full marks for presentation and defence begin with "the live demo runs cold", and the spine says a failed demo "costs its own marks"; how many marks is the panel's call, so the sheets set no number | Scoring workbook (Groups, Learners, Summary), closure workbook (Demos, Scores, Checks), the bank, the run sheet, the deck's D32 |
| A demo recovered inside its two minutes is left to the panel's judgement within presentation and defence; both workbooks say the rule sets nothing for it | The spine's rule says what a demo that still fails costs and is silent on a recovery; the first build had labelled a recovery as run cold, which the rule never says | Both workbooks, the bank, the run sheet |
| A machine that fails before the demo starts is swapped for a spare and the demo runs in the slot; only if no spare works does it run cold in the room's reserve, before the same panel | The rule covers a group's code; the first wave added the machine case and the requester's delegation covers it | Run sheet, bank, deck D32, both workbooks |
| The grade closure workbook takes the mini project in its two parts, 34 and 6; ABSENT goes in the learner's presentation and defence cell, ABSENT in the group part reads NOT A SCORE, and a seat whose group part differs from a teammate's reads GROUP PART DIFFERS | The rubric gives every member the group's 34, so the part is the group's and the same number on every seat; the first build accepted either error with no flag | Closure workbook, run sheet |
| Each room's scribe checks the commit of its own room's demo machines; the Academic TA prepares every machine before the rooms open | The first build gave the Academic TA every room's check while scribing the leader's room, and both rooms change over at the same minutes | Run sheet |
| The slot is 17 minutes of the group's, 8 to 10 of the panel's and 3 of changeover, with cards at 5 and 1 minute left | The row's 25 to 30 minutes; Friday's pack shows cards at 5 and 1 minute left | Deck S5, run sheet, bank |
| The room rule: each sub-problem's groups together and back to back, which wins over balancing the rooms; sub-problems 1 and 5 before the leader where it splits nothing | The row asks for alternate viewpoints back to back; the leader's questions are a board's; Friday's tranche takes whole clusters only, so under a 2, 2, 2, 2 and 1 allocation Saturday holds three clusters of two, which cannot split three and three without breaking a cluster | Run sheet |
| Four timings: the likely Saturday (two GD rounds, six presentations) as three and three under a 3, 3 and 3 allocation or four and two under 2, 2, 2, 2 and 1; and the heaviest (three GD rounds, nine presentations) in each shape, 3, 3 and 3 at 28-minute slots with the leader signing after the afternoon's quiet-member questions and no slack for a late leader | Monday's allocation is the Programme Head's and Friday's tranche depends on its draw | Run sheet |
| The one-breath interview answer the trainer may model runs on the invented turnaround quarter | An answer built on a group's finding would name a plant to the room | Run sheet |
| The deck's S slides are the ones shown at each expert day's opening; every other slide is a D slide read alone from Wednesday's close | The standard numbers a self-study slide D; Wednesday's pack hands the deck out for the night | Presentation deck |
| Deck question slides are audited by `internal/C2_W03_SAT_deck_options_audit_INTERNAL.py`, which keys them from their answer slides and runs `scripts/distractor_audit.py` on a scratch copy | The audit reads option sets only in exercise folders, which a build Saturday does not have | Proof below |
| The bank's sub-problem 1 answer gives each branch's share of the shortfall against 18 percent, the measure brief 1 asks for: what Q3 would have billed at 18 percent above its own Q2 less what it billed, $93,715 in all, in dollars and in tests performed; Chicago and Philadelphia carry 67.7 percent, and every payer is short with none carrying it alone | Brief 1 reads each branch "by how much of the shortfall against that plan it explains"; the first build gave growth rates only, and its payer answer (Medicaid and self-pay) explains only 42.4 percent | Bank, run sheet, week-close notes, witness |
| The money to chase is valued at what the payers' contracts allow: each payer's allowed amount over billed on the claims it paid (Medicaid 0.28, Medicare 0.34, commercial 0.53, self-pay 1.0), applied to the claims still unpaid; the employer invoice counts in full | Sub-problem 3 exists to separate billed dollars from money owed; the first build's chase figure was in billed dollars and left out patient shares and reversed claims | Bank, run sheet, week-close notes, witness |
| This programme's own arithmetic, marked so in the bank: 712 scheduled slots to separate KH-ATL-03's gap from chance (normal approximation, two-sided 5 percent, 80 percent power, the other centres' 15.1 percent taken as known), with the exact binomial power at 712 (0.77) and the two-sample figure (about 745); each metro's permutation p and a pooled within-metro test for the three campaign metros (shuffles inside each metro; 14.1 percent less, p about 0.007); the offered patients' gap held at each metro's own not-offered rate (9.6 percent less); and New York's p corrected for six metros by Bonferroni (about 0.18) | They answer the caveat challenges the panel will hear; the first build ran the chance check on New York alone, stated "less in every campaign metro" without one, and used a "nothing anywhere" null its own pooled reading rejects | Bank, run sheet, week-close notes, witness |
| The binomial check is worded as a conditional throughout: at the other centres' rate, 15 or more misses in 79 slots happen with probability 0.21 | The shorthand "chance gives the gap with probability 0.21" reads as the chance that chance caused it | Bank, run sheet, week-close notes |
| The week close lists all seven of the week's interview questions, Wednesday's "two systems with different id formats" among them | The row's interview angle goes into the pack as tagged questions; by the week close no group's work can change | Week close, S6 |
| File names are kept | Wednesday's, Thursday's and Friday's packs point at `slides/C2_W03_SAT_presentation_format_STUDENT.md` | Every file |
| On 4 October 2026, after Friday's pack merged, the run sheet follows Friday's rules: a group whose run two did not count at Friday's freeze check has its demo rerun from its frozen commit before the room opens; a GD round Friday could not run goes online to the Principal Advisor straight after round 9, from minute 40; and the room check keeps each GD group's slot at least 30 minutes after its round ends, minute 100 for a moved round | Friday's second review round changed its freeze check and its rule for a round that could not run, and the heaviest timing here had put the third round with the expert while this sheet's own row for an extra round sent it to the Principal Advisor | Run sheet: the start line, the roles table, the room check, the heaviest 2, 2, 2, 2 and 1 timing, the rerun before the room opens, and the row for a round that could not run on Friday |

## Where do the files differ from the spine's wording?

| The spine says | The files hold | What this pack does |
|---|---|---|
| Sixty billed amounts are text "such as $1,050.00" | Sixty text amounts, from "$30.00" to "$350.00"; "$1,050.00" occurs nowhere | The bank quotes "$265.00", which a group reading the claims file finds |
| "1,137 denials, 10.4 percent of retail claims" | The claims file marks 1,175 of 11,355 retail claims denied, 10.348 percent, which rounds to 10.3; 1,137 of them carry a denial posting paying $0.00 and 38 have no posting | The bank and the run sheet give all three counts and print 10.3 percent. On 4 October 2026 the orchestrating session corrected the spine and Monday's day sheet to 1,175 denied claims at 10.3 percent, so the bank's last section and the witness now read 10.3 throughout |
| "a gap chance produces with probability 0.21" (sub-problem 4) | 0.21 is the probability of 15 or more misses in 79 slots at the other centres' rate | The pack words it as that conditional |
| "Outside them the gaps are chance ... New York +23.5 percent, a random draw ... a false positive rather than a lift" (sub-problem 5) | New York's two-sided permutation p is about 0.03 and about 0.18 corrected for six metros; inside the campaign metros no single metro's gap is clear alone (Dallas about 0.21, Atlanta 0.05, Phoenix 0.14), while the three together give p about 0.007 | The pack says New York does not survive the correction and is no evidence of a lift, and rests "offered patients booked less" on the pooled test |
| "The old export also repeats 180 rows from a mid-quarter re-export" | 180 booking ids twice, booked 1 June to 26 September: 145 pairs identical, 30 differing in `updated_at` (one of them in `channel` as well) and 5 only in `channel` | The bank quotes the files and makes no claim about when the re-export ran |

## Which tools and versions produced the files?

Python 3.11.15, pandas 3.0.6, openpyxl 3.1.5, PyYAML 6.0.1 and python-pptx 1.0.2; LibreOffice 24.2.7.2
for the recalculations and the renders, with `fonts-crosextra-carlito` installed in the session so
Calibri text measures as on a trainer's laptop; Node 22.22.0. The decks were built with
`scripts/build_deck.py` and mermaid-cli 11.17.0, installed in the session's scratch space and run with
the container's puppeteer configuration, because `setup.sh` pins version 11 and every built deck was
measured against it; the container's own mermaid-cli is 12.0.0. The workbooks and their recalc
manifests are written by `internal/C2_W03_SAT_build_mini_project_scoring_INTERNAL.py` and
`internal/C2_W03_SAT_build_grade_closure_INTERNAL.py`.

## What did the depth loop ask, find and change?

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every file built from the row, the spine and the dossier, in the row's order? | The first wave's question bank and week-close notes were in the India setting; the witness quoted the old register's no-show numbers and failed five spine figures; the first wave's presentation deck named two plants in a STUDENT file (two metros changing booking systems, the posting system's own key format), used a Week 1 plant's figures as its example, and kept its options in tables the audit cannot read | Every file rebuilt: the witness against the re-planted spine (0 disagreements), the bank and notes in dollars, metros, payers and Q2 to Q3, the deck on invented figures with no plant, its options as lettered lines |
| 2. Domain | The builder | Could a learner who has never worked in a business say who asks, why the number matters, what a wrong number costs and which real company faces the same question, from each file alone? | The presentation deck never said what Kalpa Health is; its vocabulary map gave "payer" and "phlebotomist" no meaning; the week close named Kalpa Health without saying what it does; no real company appeared | S1 now says what Kalpa Health is and how it bills; the map defines payer and phlebotomist; the week close's S1 says what Kalpa Health is; Quest's quarter (D10) and Optum India and AGS Health (week close D5), each checked on 1 October 2026 |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with options, a sizing and the call, and the code last? | The day teaches no code. The one-slide answer arrives on Dr Menon's two minutes of reading, the cold demo on the panel's trust in a number it watched arrive, and the held caveat on the challenge; the run sheet sizes every load in minutes and names what changes the plan | No change |
| Humanizer, file mode | The builder | Which patterns of `.claude/skills/humanizer` remain in each prose file? | Contrast tails ("never out of the questions", "never a feeling", "never a tidied copy", "never defend blindly and never fold"), a "rather than" contrast in the bank's opening, two closers that only restated, and a rule between every section of the TRAINER files | Each rewritten as a plain statement, the restating closers replaced by the section's answer or cut, the rules removed; the tic scanner clean on every file |
| 4. Rigor | A fresh reviewer agent, read-only, once | Does every number recompute from the files, does every key hold under a blind sit, does every rule add up in minutes and marks, and does any STUDENT file name a plant? | No blocker, 8 major and 18 minor. Majors: the bank never gave each branch's share of the shortfall, so its payer answer failed on that measure; the money to chase was in billed dollars; the chance check ran on New York and on no campaign metro; the 9 percent's mechanism was named as a trend where the booking level per head drives it; every question slide's note hinted at its key; one key repeated the slide before it; one question had two defensible options; the likely Saturday's three-and-three plan split a cluster under one allocation. Minors included "two minutes after" for 6 of 280 double posts, loose witness tolerances and unasserted facts, a "nothing anywhere" null, the 712's unstated assumption, the binomial shorthand, an overclaimed answer slide, a clock caveat that could not move the claim, Quest's segment mixed with its total, a source overreach in the week close, 1,721 for 1,720, two workbook gaps, three run sheet contingencies, an interview answer resting on ids that cannot match, facilitation that could hand a finding over, rule 3's count, the machine branches, Friday's tranche workbook and the week close's 15.5 minutes. Out of scope, for the orchestrating session: Friday's day sheet line 120, the reversals' posting minute, September's compressed posting lag | Every finding fixed: the witness gained 81 bank figures and 14 facts, tightened its tolerances and sums quantities; the bank carries the shortfall table, the chase at contract value, the per-metro and pooled chance checks, the level mechanism, the Bonferroni correction, the 712's assumptions and the conditional wording; the deck's notes keep hints off the question slides and its items were rewritten; the run sheet carries both likely plans, the per-room hash checks, the 3, 3 and 3 signing order and the late leader; the closure workbook flags a group part that differs or reads ABSENT; both workbooks leave a recovered demo to the panel; Quest, Optum India and AGS Health re-read on 1 October 2026 |
| 5. Pedagogy and language | A fresh reviewer agent, read-only, once | Can each file be understood alone, does every heading ask a plain question with who needs it and what it costs, does each section close on its answer, and does the language pass the house rules and the humanizer? | No blocker, 5 major and 22 minor. Majors: the run sheet's model interview answer named a plant; the one-slide answer counted three, four and five ways; all four question slides used one device; nine repeated headings in the bank; many Who-needs lines without a decision or a cost. Minors included titles that label instead of answering, an inaccurate panel slide, section promises, the slot's length, tense, undefined terms, process words, restating closers, staged triads, non-house bold, weak negatives, map notes without a watch-for, a garbled clause, the cover strip touching the footer, Quest's numbers, a table-only rubric slide, the week close's timing and no section-closing slides | Every finding fixed except the optional rubric chart (a table stays, since the rubric's words are the content): the answer moved to the invented quarter; five slots counted one way; four devices (choose, spot the cell, order, true or false with its reason); every repeated heading split into a question naming its stake; every Who-needs line names a decision and a cost; five section-closing slides and a closing slide that answers the day's question; terms defined at first use; process words, restating closers and decorative bold removed; the cover's quote shortened so the chapter strip clears the footer |
| Second round, scoped | A fresh reviewer agent, read-only, once | Do the fixes that changed a number, a key or a rule hold, and does every file repeat them the same way? It recomputed every changed figure with its own code and sat the four question slides blind | No blocker and no major; 12 minors. The bank's spare-machine row named a different person from the run sheet; the money-to-chase subtotal said "before any denial" while including the 38 denied claims with no posting; the per-head gap's widening was credited to the campaign metros alone when the other three metros also fell; the run sheet's claim about Friday's draw did not hold once clusters split between rooms; the 3, 3 and 3 late-leader row started closure too early; the short week close added to 12 minutes; "no evidence of a lift" overstated the correction; 10.35 invited rounding up; and four nits (who checks the commit in the deck, one answer-slide reason, one separating question that addressed both groups, the one-breath answer's challenge wording) | All twelve fixed. The widening now reads "the other three metros fell 3.4 percent (New York up 3.0, Chicago down 12.7 and Philadelphia down 2.9)", three figures the witness gained; the subtotal reads "before the 1,137 denials with a posting are worked"; the Programme Head checks that no Saturday GD group has a slot before minute 70; closure in the 3, 3 and 3 late case starts about 40 minutes into the afternoon; the short close skips S4 and S6. No third round, since the brief allows one second round and its fixes were wording plus three witnessed figures |

## How was the pack proved?

Every command below ran on 1 October 2026 on the committed files, after the second round's fixes.

| Command | Last line |
|---|---|
| `python3 scripts/verify.py content/W03/SAT --execute` | `RESULT: PASS (0 failures)`: 16 files named and placed for a build week Saturday; xlsx_recalc 7 verdicts and 12 flips, and 5 verdicts and 9 flips; deck_md_check on 54 and 15 slides; deck_check on 71 rendered slides with 0 overflowing boxes; two WARN lines on marks language in the STUDENT decks, which the approved learner-facing rubrics allow |
| `python3 scripts/sync_programme.py --check` | `every output is current` |
| `python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py` | `RESULT: PASS (0 disagreements with the spine, the bank and the facts)`, 283 lines: 53 spine, 216 bank, 14 facts |
| `python3 content/W03/SAT/internal/C2_W03_SAT_deck_options_audit_INTERNAL.py` | `RESULT: PASS (0 failures)`: four items, keys b, a, d and c, one in each position, no key the longest option |
| `python3 .claude/skills/llm-tic-scrubber/scripts/tic_scan.py content/W03/SAT` | `tic_scan: 10 of 10 files clean` |
| `python3 .claude/skills/training-deck-builder/scripts/meta_scan.py` on both decks | `meta_scan: clean, 1270 text runs checked` |
| Both decks built with `scripts/build_deck.py` and rendered through LibreOffice | 55 and 16 slides, looked at slide by slide on contact sheets; the cover's chapter strip clears the footer |

The headings-only read of the three TRAINER files and the deck's titles runs as a chain of plain
questions and action titles in the day's order.
