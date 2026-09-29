# Provenance: Week 1, Thursday

INTERNAL. Where every part of the Thursday pack came from, what was invented, and what departs from a
source. Rebuilt on 29 September 2026 to the standard of that date; the older pack of 9 September was
removed whole.

## Sources, in the order they were read

| Source | What it gave the pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, Thursday row, the campus day, the afternoon-and-lab table | The case, the five rungs, the four traps, the escalated case, the second case, the lab set, the 360-minute day |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The bar, the volume per family, the form of each family |
| `docs/curriculum/W1_Data_analysis_found.md`, Thu 08 Oct row, all fifteen columns | Scenario, thinking, agenda, outcomes, trainer notes, plants, exercises, after-class tasks, interview angle, references, Kahoot plan |
| `docs/programme/calendar.md` | W01/D4, Thu 08 Oct 2026, teaching, M1, no faculty block |
| `docs/07_Client_Zero.md` (v2.2 locked), section 7, version v3 | The dataset and its three witnesses; the stakeholder table |
| `content/W01/D1` | The model for form: deck syntax, notebook helper and rhythm, companion build, workbook build, day sheet |

## Data

```bash
python3 data/generate_client_zero.py --version v3 --out content/W01/D4/data --stem C2_W01_D04
python3 data/generate_client_zero.py --version v0 --out <scratch> --stem C2_W01_D04_monday
cp <scratch>/C2_W01_D04_monday_takehome_STUDENT.py content/W01/D4/data/C2_W01_D04_monday_sample_STUDENT.py
python3 data/generate_client_zero.py --version v2 --out <scratch> --stem C2_W01_D04
cp <scratch>/C2_W01_D04_takehome_STUDENT.csv content/W01/D4/data/C2_W01_D04_takehome_STUDENT.csv
```

`python3 data/generate_client_zero.py --contract` passed on 29 September 2026 (v3: Student orders 12
against 12; blended exposure lift +6.1 percent; within Retail-Plus and within Retail-Core -3.0
percent). The v3 files regenerate byte-identical to the ones the 9 September pack carried.

| File | Version | Read by |
|---|---|---|
| `C2_W01_D04_orders_STUDENT.csv` | v3, the 186 cleaned orders | Notebooks 01 to 03, ex1 |
| `C2_W01_D04_exposure_STUDENT.csv` | v3, 160 customers | ex1, ex2 |
| `C2_W01_D04_campaigns_STUDENT.csv` | v3, one campaign | ex1, ex2 |
| `C2_W01_D04_monday_sample_STUDENT.py` | v0, Monday's take-home sample | Practice lab problem 3 (ex3) |
| `C2_W01_D04_takehome_STUDENT.csv` | v2, Wednesday's take-home export | Tonight's take-home |

## Plants, and where each is used

| Plant | Where the room meets it | Kept out of |
|---|---|---|
| Student holds exactly 12 orders (5 then 7, from 2 customers) | Notebook 03, the empty your-turn cell; ex1 part 3 computes it into a variable and never prints it | Every slide, exercise stem, the Kahoot, the companion page and the study notes |
| The Retail-Plus gap is real but modest | Notebook 01 level 4 (135 of 5,000, 0.027); notebook 02 (Rs 24,420, 0.19 percent) | Slides state neither number; the round 2 slides give the sentence with blanks |
| The monsoon sale lifts the blend 6.1 percent while each segment falls 3.0 percent | ex1 part 4 and ex2; the debrief is built on the room's own split | Slides use an invented reversal (big and small spenders) in its place |
| Take-home plants: header row as body line 45, -2,400 on KR-02018, 12/05/2026 on KR-02030, empty status on KR-02052, six duplicated ids | The take-home | Named only in the day sheet; the self-check gives numbers and generic decisions |

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| The shuffle permutes quarter labels on delivered revenue per member | The row says "shuffle the segment labels" | Meera's first question compares two quarters of one segment, so the labels that carry no meaning under chance are the quarters; the take-home keeps a segment comparison |
| The measure is delivered revenue per member | The row leaves the measure open | Monday settled delivered as the money kept, and a member exists in both quarters; on this measure the one-sided share is 0.027, which is the spine's 0.03 without forcing it |
| The morning demonstration runs on Retail-Core, and the room runs Retail-Plus | The spine's round is "a shuffle test on the Retail-Plus gap" | The trainer shows the wobble first and the room finds the plant; the rung is unchanged |
| The p-value counts one direction (a fall at least as large) | None; the row says "at least as extreme" | Meera asked about a drop; the two-direction share (0.050) is taught as depth in notebook 01 and slide D39 |
| Round 3's chance reference is a coin flip per order | The row's shuffle is a label shuffle | Shuffling labels among a fixed set of orders keeps the 5 and 7 split, so it cannot test a count; one coin per order is the same chance-only idea for a count |
| The rupee size of the Retail-Plus fall and the Student count never appear on a slide | The spine lists "40 percent on twelve orders" as the trap | CLAUDE.md forbids naming a plant in a STUDENT file; the trap is staged on the headline 40 percent and the count is the room's |
| Retail-Plus "beats the wobble" is presupposed by round 2's slides and by the Kahoot's return item | The row's plant list | Round 2's rung is the question that result raises, and the return question is the row's own; both follow the room's round 1 run |
| The Kahoot's rate item uses 45 percent on 11 orders against 31 percent on 400 | The row's plan says 40 percent on 12 | The standard's third device: a quiz trap never echoes the planted value |
| The practice lab gives the "four p-value sentences" and "confounder in three vignettes" in new sentences and vignettes | The spine lists the same device names as the row's mid-session drills | The round sets use them in session; the lab needs fresh items |
| Tonight's take-home runs on Wednesday's take-home export (v2) with a discount question | The row's after-class task names the note and a shuffle on Monday's data | v3 has no second sample in the generator; v2's second export carries its own plants, spirals Wednesday's cleaning, and the Monday shuffle became practice problem 3 as the spine asks |
| A decision workbook ships beside the companion | The standard lists it; the prompt did not | D1's model pack carries one, and it gives early finishers the day's four decisions with a defect each |

## Invented, and labelled so wherever it appears

- The ten cards (Q1 3,400, 2,900, 4,100, 2,500, 3,800; Q2 2,200, 3,100, 1,900, 2,700, 2,400).
- The twenty no-change segments in notebook 01 (seeds 100 to 119, values Rs 1,500 to Rs 4,500).
- The Rs 20 gap at 100 to 20,000 orders (notebook 02) and the Rs 5 gap at 100 to 10 lakh orders (morning S22).
- The retention offer at Rs 500 per member per quarter, and the 30 percent margin in notebook 02's depth.
- The one-order swing table, the 400-order segment, and the 42 percent on 12 simulation in notebook 03.
- The big and small spenders in the afternoon debrief (Rs 5,000 and Rs 4,800; Rs 1,000 and Rs 960; 20 and 80 percent).
- Every number on the companion page and in the decision workbook.
- The numbers in the round 2 and round 3 sets, the lab's vignettes and problem 4, and Kahoot items 1, 3 and 7.

## Links, each checked on the day it entered

| Link | Checked | Used in |
|---|---|---|
| Seeing Theory, frequentist inference: https://seeing-theory.brown.edu/frequentist-inference/index.html | Checked 29 Sep 2026, HTTP 200, title "Seeing Theory - Frequentist Inference" | Take-home, study notes |
| StatQuest video index: https://statquest.org/video_index.html | Checked 29 Sep 2026, HTTP 200, both named videos listed | Study notes |

The row's trainer resources (Khan Academy, Exponent, GeeksforGeeks) are not carried into any pack file.

## Citations in the study notes, each checked on 29 Sep 2026

| Citation | How it was checked |
|---|---|
| Fisher, The Design of Experiments, 1935, as an original reference for the permutation test | Crossref lists contemporary reviews dated December 1935; the Wikipedia article "Permutation test" lists it under original references |
| Wasserstein and Lazar, "The ASA Statement on p-Values: Context, Process, and Purpose", The American Statistician 70, 2016, principle 2 | Crossref record for DOI 10.1080/00031305.2016.1154108; the principle's wording read verbatim from the ASA's own PDF of the statement |
| Simpson, "The Interpretation of Interaction in Contingency Tables", JRSS Series B 13, 1951 | Crossref record for DOI 10.1111/j.2517-6161.1951.tb00088.x |
| Bickel, Hammel and O'Connell, "Sex Bias in Graduate Admissions: Data from Berkeley", Science 187, 1975 | Crossref record and abstract for DOI 10.1126/science.187.4175.398; the notes' sentence follows the abstract ("about as many units appear to favor women as to favor men") |

## Tools the numbers and outputs came from

Python 3.11.15; nbclient 0.11.0 and nbformat 5.11.1 through `scripts/nb_make.py`; pandas is not used
(Week 1 stays in plain Python). Every share comes from `random.seed(2026)`, except the invented
segments in notebook 01 (their own seeds) and the invented Rs 20 orders (seed 11). Decks built with
`scripts/build_deck.py` and rendered through LibreOffice with Carlito installed; mermaid-cli 11.17.0
was used from a session-local install, because the container's mermaid-cli 12 rejects the `-w` flag
the deck builder passes. The companion page's live numbers come from a seeded mulberry32 generator in
the browser, so they differ slightly from Python's (the walk's 1,000 shuffles give 0.029 there against
0.021 in notebook 01), and every such number on the page is labelled as computed on the page.
