# Provenance: Week 1 Day 1

**INTERNAL.** What this pack is built from, what was verified and when, and every decision that
departs from a source.

---

## The sources

Built on 29 September 2026 from, in this order: `docs/detailing/W01_W02_spine.md`, approved by the
requester on 29 September 2026, which sets the day's case, its five rungs, its traps, the campus day
and the afternoon-and-lab table; `.claude/skills/day-pack-builder/references/the-standard.md`, which
sets the form and the volume; the Monday 5 October 2026 row of
`docs/curriculum/W1_Data_analysis_found.md`, read in column order, for everything the spine leaves
unchanged (the scenario, the data version, the plants, the interview anchors, the references and the
Kahoot plan); the day's line in `docs/programme/calendar.md`; and `docs/07_Client_Zero.md` at v2.2,
locked 13 September 2026, with the Global Capability Centre addendum of 28 September 2026.

## The data

Every file in `data/` is written by `data/generate_client_zero.py`, version `v0`; nothing is
hand-edited, and a regeneration on 29 September 2026 produced byte-identical files.

```
python3 data/generate_client_zero.py --version v0 --out content/W01/D1/data --stem C2_W01_D01
```

| Planted | Where it is used |
|---|---|
| One Business order of Rs 4,80,000, KR-01031 | Round 3's trap (the mean of Rs 18,160 against the median of Rs 2,205), found by the learner's own sort in an empty cell; the second case, where it carries store's 91.6 percent |
| One amount stored as the text "4500", KR-01008 | Round 2, met as a TypeError in two minutes and fixed with `int()`; the record is found in an empty cell |
| The take-home's second sample: two Business orders (Rs 3,12,000 and Rs 2,05,000) and the text "1990" | The take-home; named only in the day sheet |

The plants appear by value only in `trainer/` and here.

## Rebuilt on 29 September 2026 to the approved spine

The pilot of 28 September was rejected for its content: staged Python errors, code-reading
exercises and a 230-minute day. Its form was kept. Every family was rebuilt around one case climbed
in five rungs, a trap per rung, and the 360-minute day.

| Family | The pilot | Now |
|---|---|---|
| Decks | A half-one and a half-two deck built around a NameError, a TypeError and code-reading drills | A morning deck of the ask and three rounds, and an afternoon deck of the two cases, the debrief of wrong answers, the interview drill and the close |
| Notebooks | Four chapter notebooks and a hands-on twin | One notebook per round climbing four levels with its trap, plus the escalated case and the second case, each a TODO twin with an executed solution |
| Companion | A revenue-tree page | A branch simulator: every assumption the traps turn on is a control, and the number and the decision move with it |
| Workbook | Four tabs on the tree | One tab per taught decision, one planted formula defect each |
| Exercises | Three lettered sets on concept, code and operation | One scenario set per round, the two case briefs, and the practice lab set, every stem a Kalpa business question |
| Reading | Notes and a sheet on the old chapters | Notes carrying the three rounds as worked cases, the sheet with the traps, the board work in order, Tuesday's pre-read |

## Decisions that depart from a source

1. **The rungs map onto the rounds two to one at the start.** The spine names five rungs and the
   day has three morning rounds and two afternoon cases. Round 1 carries rungs one and two (four
   readings of sales, and the tree as metrics), rounds 2 and 3 carry the leaves and the typical
   order, and the escalated case carries the fifth rung, which branch Meera opens first. The second
   case is the spine's second case.
2. **Each round's trap is assigned from the spine's Monday list.** The cancelled-orders trap sits in
   round 1, the rows-as-customers trap in round 2, the mean in round 3 and the two 10 percent lifts in
   the escalated case. The second case carries its own trap, store's 91.6 percent, which the spine
   does not list; it follows from the spine's question ("whether one channel changes the
   recommendation") on this file.
3. **The row's environment block (25 minutes) becomes two minutes inside round 1.** Week 0 set up
   the Codespace; the 360-minute day has no environment slot, and the standard says a runtime error
   gets two minutes when it happens.
4. **The Kahoot has eight items and no return question.** The standard asks for the return question
   from the day before; the row says there is none on Day 1, and the spine keeps the Kahoot plans as
   the rows have them. The row's six items are kept, and two are added for the rows-as-customers and
   the two-lifts traps.
5. **The plant rule, applied to the afternoon.** A learner file never prints the Business order's
   amount, id, customer or position, the words "bulk order" or "corporate order", or the text amount's
   record. Aggregates that include the order (the mean, the median, store's share, booked revenue)
   are the trap numbers and are printed. Numbers computed without it appear only in afternoon files,
   after round 3's sort has found it, and they are introduced as "the order your round 3 sort put at
   the top". The Kahoot's comparison trap uses "3500" where the row wrote "4500".
6. **Anand Iyer is the finance controller.** The row calls him the CFO; `docs/07` says finance
   controller, and the pack follows `docs/07`.
7. **Seven interview questions are added to the row's five.** They are this pack's case-style
   follow-ups, as the spine asks, and their tags are this pack's calibration on the row's scale.

## Invented, and recorded as invented

1. Kalpa Retail sells to consumers and to businesses: consumer orders sit in the locked Rs 800 to
   Rs 3,000 band and the Business segment buys in bulk, as the generator's docstring sets it.
2. The Week 1 extract is Kalpa Retail India for one window, 1 July to 26 September 2026.
3. Marketing's Rs 12 crore is the acquisition line of the growth plan, not one quarter's spend.
4. The payback consequence in round 3 ("about eight times as many orders") is arithmetic on the
   mean against the median; no customer acquisition cost is stated anywhere, because none exists
   in the sources.
5. Every record labelled invented in the notebooks, the companion, the workbook, the exercises and
   the practice set is invented to isolate one mechanism, and each place says so.

## Sources, with the date each was checked

Each link was requested on 29 September 2026 and returned HTTP 200, except where noted.

| Link | Role | Checked |
|---|---|---|
| https://www.hackingthecaseinterview.com/pages/profitability-case-interview | The profitability case and the revenue tree, trainer preparation and the notes | 29 Sep 2026, 200 behind a bot challenge page |
| https://www.roadtooffer.com/blog/driver-tree | Driver trees, trainer preparation | 29 Sep 2026, 200 |
| https://mconsultingprep.com/profitability-case-framework | The framework's revenue variants, the take-home reading | 29 Sep 2026, 200, title "6 Variants of Profitability Framework" |
| https://automatetheboringstuff.com/3e/ | Loops and dictionaries, the notes' reading path | 29 Sep 2026, 200 |
| https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning | Codespaces with Jupyter, trainer preparation | 29 Sep 2026, 200 |
| https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 | Corey Schafer, the beginner playlist | 29 Sep 2026, 200; the oEmbed title reads "Python Programming Beginner Tutorials" |
| https://www.youtube.com/watch?v=daefaLgNkw0 | Corey Schafer, Dictionaries | 29 Sep 2026; the page returned 429, and the oEmbed endpoint returned "Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs" |
| https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode | Mean, median and mode | 29 Sep 2026, 200 |
| https://britinstitute.uk/blog/data-analyst-case-study-interview-questions | The sales-drop case, Tuesday's pre-read | 29 Sep 2026, 200 |

## Tools the numbers and outputs came from

Python 3.11.15, IPython 9.17.1 and nbclient 0.11.0 for every notebook output and error text;
python-pptx for the decks; mermaid-cli 11.17.0 for every rendered diagram, run from a session-local
install because the installed mermaid-cli 12.0.0 rejects the `-w` flag that `scripts/build_deck.py`
and `scripts/build_cheatsheet.py` pass; LibreOffice for the workbook recalculation and the deck
render check, with the Carlito font installed.
