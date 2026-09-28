# Provenance: Week 1 Day 1

**INTERNAL.** What this pack is built from, what was verified and when, and every decision that
departs from a source.

---

## The sources

Built from `docs/curriculum/W1_Data_analysis_found.md`, the Monday 5 October 2026 row, read in
column order, and from `docs/07_Client_Zero.md` at v2.2, locked 13 September 2026, with the Global
Capability Centre addendum of 28 September 2026, which sets the frame: the cohort as trainee
engineers in the GCC's data and AI team, and the three recurring beats of the client's ask, Kavya's
review and the interview question.

## The data

Every file in `data/` is written by `data/generate_client_zero.py`, version `v0`; nothing is
hand-edited.

```
python3 data/generate_client_zero.py --version v0 --out content/W01/D1/data --stem C2_W01_D01
```

| Planted | Where it is used |
|---|---|
| One Business order of Rs 4,80,000, KR-01031 | The mean against the median in half two, chapter 2, and notebook 4 |
| One amount stored as the text "4500", KR-01008 | The TypeError in half one, chapter 4, and notebook 2 |

Both appear only in `trainer/` and here. The take-home's second sample carries its own two Business
orders and one text amount, also named only in the day sheet.

## Rebuilt on 28 September 2026 to the programme's new standard

Every learner artifact was rebuilt; the old pack is in the history. What changed, and why:

| Artifact | Before | Now |
|---|---|---|
| Decks | Two decks of placeholder slides in the old palette | 28 and 27 numbered slides in the orientation deck's system, a cover and four chapters each, speaker notes on every slide |
| Notebooks | One demo notebook of 34 cells and a hands-on on the second sample | Four teaching notebooks, one per chapter pair, 20 to 28 cells, 5 or 6 rendered diagrams and 5 to 11 checks each, and a hands-on twin on delivered orders with its executed solution |
| Companion | A 10 KB toggle page | A guided walk, a branch calculator, four experiment cards with sequence popups, a paste-your-numbers workbench, a decision tree and a glossary |
| Workbook | None | The day's decision tool, four tabs and an Export tab, proven by xlsx_recalc |
| Exercises | Two lettered sets and a guided file | Three sets layered by concept, code and operating layer, each with a full solution table |
| Notes, sheet, board, pre-read | The old tree and the plants named | The new tree, the plants unnamed, links re-verified |

## Decisions that depart from a source

1. **No learner file names a plant, which changes four things the approved spine or the row
   implied.** The planted records are found in empty your-turn cells, so the executed notebooks carry
   no saved output naming them. The mean against the median is shown on five invented orders in the
   decks, the notebooks, the companion and the board work; the approved spine had put a bulk-order
   switch on the thirty real orders, which would have named the record on a page any learner can
   open. The Kahoot's comparison trap uses "3500" where the row's plan wrote "4500", so the trap
   survives without echoing the plant. The old pack named both plants in its study notes, cheat
   sheet, board work, exercise set and demo; none of those lines survive.
2. **The unguided exercise runs on delivered orders.** The row asks for customers, orders per
   customer and the median unguided, on the same file the demo taught. On booked orders the demo's
   code answers it, so the definition changes and the numbers become new: 19, 1.11 and Rs 2,060.
3. **Anand Iyer is the finance controller.** The W01 D1 row calls him the CFO; `docs/07` and the
   W01 D3 row say finance controller, and the pack follows `docs/07`. The row's word is a tracker
   typo to correct.
4. **The teaching notebooks are four, not one.** The notebook-builder sizing puts a notebook at 16
   to 25 cells; the day's content at the depth asked for runs to about a hundred, so it is split by
   chapter pair.
5. **The decision workbook is new to this day.** The day-pack manifest asks for one on every
   teaching day; the old pack had none.

## Invented, and recorded as invented

1. Kalpa Retail sells to consumers and to businesses: consumer orders sit in the locked Rs 800 to
   Rs 3,000 band, and the Business segment buys in bulk from Rs 2 lakh upward. The row's "one
   business customer can move an average" needs this, and the locked file says the band describes
   the ordinary population rather than the whole file.
2. The Week 1 extract is Kalpa Retail India for one window, 1 July to 26 September 2026.
3. Marketing's Rs 12 crore is the acquisition line of the growth plan, not one quarter's spend.
4. The five orders of Rs 1,900 to Rs 2,600 and the Rs 90,000 bulk order, the four records in
   experiment D, and the canteen sentence on half two S21 are invented to isolate one mechanism
   each, and each place they appear says so.

## Sources, with the date each was checked

| Link | Role | Checked |
|---|---|---|
| https://www.hackingthecaseinterview.com/pages/profitability-case-interview | The profitability case, trainer preparation and the notes' reading path | checked 28 Sep 2026, returned 200 |
| https://www.roadtooffer.com/blog/driver-tree | Driver trees, trainer preparation | checked 28 Sep 2026, returned 200 |
| https://mconsultingprep.com/profitability-case-framework | The framework's revenue variants, the take-home reading | checked 28 Sep 2026, returned 200; variants 1 and 2 are the revenue side |
| https://automatetheboringstuff.com/3e/ | Chapters 2 and 3, if-else and loops, the notes' reading path | checked 28 Sep 2026, returned 200; chapter titles read from the contents |
| https://www.census.gov/library/publications/2025/demo/p60-286.html | Median household income, $83,730 in 2024, the notes' field case | checked 28 Sep 2026; published 9 September 2025 |
| https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning | Codespaces with Jupyter, trainer preparation | checked 28 Sep 2026, returned 200 |
| https://www.youtube.com/watch?v=daefaLgNkw0 | Corey Schafer, Dictionaries, a row-supplied student reference | verified 03 Sep 2026 on the row; the re-check on 28 Sep 2026 returned 429, so it is kept out of the new notes |
| https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode | Mean, median and mode, a row-supplied student reference | verified 03 Sep 2026 on the row; the re-check on 28 Sep 2026 met a bot challenge, so it is kept out of the new notes |

Every error text in the pack was produced by running the code on the day's file under Python 3.11
with IPython 9.17.1, including the full Jupyter traceback quoted on half one S25 and in notebook 2.

## Re-dated on 27 September 2026

Tracker v7 of 21 September 2026 moved this row one week later, to Monday 5 October 2026, with no
change to its fifteen columns; the day sheet's module and date lines render from the calendar.
