# Provenance: Week 1, Friday

**INTERNAL.** Where every fact, number and decision in this pack came from. The lab data is
`v3-lab`, **proposed for client zero v2.3** (tracker v7, 21 September 2026) and not yet locked.

## Sources, in the order they bind

| Source | What it gave this pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The day's shape (lab 150, break 10, debrief 40, rehearsal in two rounds 100, timed cases 40, Kahoot and preview 20); the traps as "the week's traps in new places, and a reconciliation skipped under time pressure"; the practice lab as "rerun the step where the learner stalled" |
| `docs/curriculum/W1_Data_analysis_found.md`, Fri 09 Oct row | Kavya's words, the four questions on the table, the method's six steps, the observation rule with no scores on a wall, the client-zero column (v3-lab and its four defect families), the interview angle, the after-class tasks, the Kahoot plan, the references |
| `docs/programme/calendar.md` | Fri 09 Oct, teaching, Module 1, no faculty block |
| `docs/07_Client_Zero.md` v2.2 with the v2.3 note | The stakeholders and their roles; v3-lab named as proposed for v2.3 |
| `.claude/skills/day-pack-builder/references/the-standard.md` and `artifact-manifest.md` | Form; the three devices that keep plants out of learner files; the AI-free lab kept in its own kind |
| `content/W01/D3` and `content/W01/D4` | The week's conventions the lab reruns: the identity rule, the three-way decision, input equals clean plus rejected, the shuffle on the customer, the four-part note |
| `docs/curriculum/Saturday_papers.md`, W1 paper | Saturday's format for the preview; the Kahoot avoids the paper's items |

## The data

```
python3 data/generate_client_zero.py --version v3-lab --out content/W01/D5/data --stem C2_W01_D05
python3 data/generate_client_zero.py --contract
```

`v3-lab` was added to the generator as a new version only, seeded from `SEED + 30` (and `SEED + 31`
for the practice export), with customer ids C-7000 to C-7803 and order ids KR-07001 onward, so no
key from Monday to Thursday recurs. Versions v0 to v3 were written to a scratch folder after the
change and compared byte for byte with the committed day folders: every file identical. The
contract passes with the v3-lab block added.

| File | Rows | Carries |
|---|---|---|
| `C2_W01_D05_lab_orders_STUDENT.csv` | 207 | 197 distinct orders plus 10 repeated rows, one text amount, one empty segment |
| `C2_W01_D05_lab_control_STUDENT.csv` | 2 | Q1 98 orders Rs 60,48,000; Q2 99 orders Rs 43,25,480 |
| `C2_W01_D05_practice_orders_STUDENT.csv` | 79 | 75 distinct orders plus 4 repeated Q1 Retail-Plus rows, one amount "Rs 2,260", one empty customer_id |
| `C2_W01_D05_practice_control_STUDENT.csv` | 2 | Q1 39 orders Rs 23,21,000; Q2 36 orders Rs 23,39,340 |

## The plants, and where each is used

| Plant | Lab file | Used in (TRAINER and INTERNAL only) | Learner files |
|---|---|---|---|
| September batch posted twice, 10 rows in Q2 | KR-07143 and nine Retail-Core orders | Lab key, day sheet, reference notebook, observation sheet | Never named; the debrief shows the mechanism on invented numbers |
| "9,85,000" stored as text | KR-07073 | Same | Never named; the debrief uses an invented "7,50,000" |
| Empty segment | KR-07146 | Same | Never named |
| Business on 6 then 4 orders | 5 corporate customers | Same | Never named; the debrief uses an invented 6 then 3 |

The practice export's defects appear in its solution file, which opens only after the practice lab.

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| The lab export is described to learners as "Kalpa-shaped and re-keyed for the drill, so nothing in it belongs in Monday's note" | The row says only "a fresh two-quarter export" | Any business identity for the export (a region, last year's quarters) would be a client-zero fact beyond the lock, and its totals differ from the Q1 and Q2 figures the week established |
| A control-totals file ships with the lab export | The row lists no control file | The reconciliation needs a figure outside the file to land on; Wednesday's Finance figure plays that role in the week |
| The clean finding is Retail-Core's basket, a branch the week never showed | The row says only that the defect families move | A lab that ends on Tuesday's answer measures memory; a new branch measures the method |
| The lab's 150 minutes are terms 10, clock 120, second look 20 | The row: terms 10, lab 120 | The spine's 150; the row's "inside two hours" kept as the clock |
| The debrief splits across lunch, 20 and 20 | The spine lists debrief 40 after the break | The morning block is 180 minutes, so 150 + 10 + 40 does not fit; the reconciliation (predicted by the row) runs before lunch and the tally chooses the rest |
| The debrief deck uses invented numbers for every mechanism | The row: "each rerun once on the projector" | The deck is a learner file; the projector rerun comes from the TRAINER reference notebook |
| The rehearsal defends Thursday's final note | The row says "the note" | Thursday's note is the one going to Monday's review, which is what the rehearsal rehearses |
| Three decks named lab, debrief, rehearsal, where the standard names half1 and half2 | The standard | A lab day takes its week spine's shape; three decks follow the three moments a trainer switches files |
| No companion page, decision workbook, cheat sheet, take-home, whiteboard or tiered extras | The standard's teaching-day volume | The requester's list for this day names the artifacts; the lab adds no idea, and the practice set carries the row's FIX task |
| The Kahoot carries five items and the return question | The standard's eight | The row's quiz plan and the requester's brief both say five plus the return |
| The practice set is 11 items with a hands-on rerun | The standard: three or four problems | It is four problems, each with two or three lettered items, so the audit can check it |

## Invented

The debrief's numbers (Rs 40,00,000 and Rs 42,40,000; 120 rows and 114 orders; "7,50,000"; 1.40 to
1.75 orders per customer; Rs 2,400 to Rs 2,100; 6 then 3 orders and -45 percent; p = 0.01 and 0.11;
mean Rs 48,900 and median Rs 1,980), the Kahoot's 180, 171 and 9 and its p = 0.04, the three timed
cases' situations (a food-delivery client, a 50,000-row export, a checkout flow on 12 and 1,200
visits; the 42 against 31 on 12 against 1,200 comes from Thursday's row), and the Marketing pushes
beyond the row's own facts. None is a Kalpa fact.

## Links, each checked on 29 September 2026

- Aced (formerly Exponent), top data analyst interview questions, the rehearsal's challenge
  questions; page title "35+ Data Analyst Interview Questions & Answers (2026 Guide)":
  https://www.tryexponent.com/blog/top-data-analyst-interview-questions (verified 29 Sep 2026)
- Seeing Theory, frequentist inference, the student reference:
  https://seeing-theory.brown.edu/frequentist-inference/index.html (verified 29 Sep 2026)

## Tool versions the numbers and outputs came from

Python 3.11 kernel through nbclient; python-pptx 1.0.2; LibreOffice headless for the render check
with fonts-crosextra-carlito installed; mermaid-cli 11.17.0 for the deck diagrams (the session's
global mermaid-cli was 12.0.0, which rejects the `-w` flag `scripts/build_deck.py` passes, so an 11.x
copy was installed in the session's scratch folder and put first on PATH for the build).
