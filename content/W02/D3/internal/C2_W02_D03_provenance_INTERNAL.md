# Provenance: Week 2, Wednesday

**INTERNAL.** What this pack is built from, what was verified and when, and every decision that
departs from a source.

---

## The sources

The pack is built from the Wednesday 14 October 2026 row of `docs/curriculum/W2_Data_manipulation.md`
(tracker v7), read in column order from the business scenario through the thinking, the agenda, the
trainer notes, the client-zero column, the exercises, the after-class tasks, the interview angle,
the resources and the Kahoot plan, and including the violet column for the IITGN faculty session
W2-3, which is tentative. The week's approved spine, `docs/detailing/W01_W02_spine.md`, approved by
the requester on 29 September 2026, sets the case, the five rungs, the four traps and the faculty-day
shape, and it wins over the row where they differ. The lock came from `data/programme/facts.yaml`
(the campus day of 29 September 2026, and the faculty block's tentative status and its placement
after the day's applied core), the W02/D3 line of `docs/programme/calendar.md` (Wed 14 Oct, a
teaching day, Module 1, faculty block W2-3 tentative) and `docs/07_Client_Zero.md` at v2.2, locked
13 September 2026, for the stakeholders and the v4 row of the dataset ladder. The form follows
`.claude/skills/day-pack-builder/references/the-standard.md`, whose model pack is `content/W01/D1`.

---

## The data

The warehouse is the v4 file that Monday's pack ships, `content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`,
written by `data/generate_client_zero.py` and loaded into the database `kalpa` by the Codespace's
own script. Nothing in it is hand-edited.

```
python3 data/generate_client_zero.py --version v4 --out content/W02/D1/data --stem C2_W02_D01
bash .devcontainer/load_warehouse.sh
```

The take-home's second sample is written by `content/W02/D3/internal/C2_W02_D03_takehome_data_INTERNAL.py`,
which imports the generator, sets its seed to 20261014 and reruns `build_v4`, then adds one tie of
its own. It writes `content/W02/D3/data/C2_W02_D03_takehome_STUDENT.sql`, which loads into its own
schema, `takehome`, and leaves the warehouse the day used untouched. On 29 September 2026 the rows
loaded in the running database were compared with the file's COPY block for orders and matched
exactly.

```
python3 content/W02/D3/internal/C2_W02_D03_takehome_data_INTERNAL.py
psql -d kalpa -f content/W02/D3/data/C2_W02_D03_takehome_STUDENT.sql
```

---

## The plants, and where each is used

Every plant appears by name only in `trainer/` and here.

| Planted | Where it is used |
|---|---|
| The exact Q2 tie at fiftieth in Retail-Plus, C-0242 and C-0185 on Rs 3,350 (warehouse v4) | Round 2, where the room runs the Retail-Plus variant of section 3 of `sql/C2_W02_D03_02_protect_list_STUDENT.sql` and the empty your-turn cell of notebook 02; the escalated case, Part 1; the afternoon debrief and the released solutions, which show the count the room found without calling it planted |
| The natural tie at 48th in Retail-Plus, C-0189 and C-0206 on Rs 3,480, which nobody planted and which makes DENSE_RANK ship 52 | Round 2's boundary read, positions 44 to 54, and the day sheet's plant table |
| Three Retail-Plus members whose spend fell in each Q2 month, C-0161, C-0171 and C-0175 (warehouse v4) | Round 3, block 5 of `sql/C2_W02_D03_03_falling_spend_STUDENT.sql` and the empty your-turn cell of notebook 03; the escalated case, Part 2; the debrief, as three of the nine flagged |
| The plan line as a small table, 13 weeks from 6 July at Rs 75,69,230 | Round 3, block 7; the escalated case, Parts 3 and 4, where the plan-first join drops the week of 29 June |
| The take-home's three-way Retail-Core tie at positions 19 to 21, C-0014, C-0021 and C-0023 on Rs 5,480, added by the builder | The take-home, Part 1, and Thursday's walk-through from the day sheet |
| The take-home's falling ladder, C-0154, C-0165 and C-0170, which the generator places under the new seed | The take-home's whole-book flag counts, 23, 18 and 7 |
| The take-home's tie at fiftieth in Retail-Plus, C-0203 and C-0247 on Rs 3,780, which the generator's own tie step places under any seed and the builder's docstring does not mention | Nowhere in the brief; the day sheet names it in case a learner meets it in Part 2 |

---

## Decisions that depart from a source

1. **Q2 revenue is booked revenue in every status.** Monday's suite defines Q2 at Rs 9,84,00,000 on
   that basis, and the day starts from Monday's definition. The tie at fiftieth exists only on that
   definition, so every artifact that shows a number says which definition it uses.
2. **The day takes the faculty-day shape of the spine, which replaces the row's agenda.** The row's
   agenda runs 215 minutes as one arc (10, 40, 45, 45, 55 and 20). The spine keeps the morning's
   180 minutes as the ask and three rounds, and gives the trainer the first 60 minutes of the
   afternoon for the escalated case with its debrief (45) and the Kahoot with Thursday's ask (15),
   before the IITGN block's 120. There is no second case and no afternoon interview drill on a
   faculty day, and the interview questions live in the notebooks, the study notes and the day sheet.
3. **The traps are the spine's four and the case's one.** The whole-table ranking, LAG without a
   partition and the skipped month read as a fall were added by the spine; the tie that ships 49 or
   51 rows is the row's. The plan-first join that drops the week of 29 June is this pack's, and it is
   the case's trap.
4. **The running total's fix reads the actual at each plan week's last day.** The plan line starts
   on Monday 6 July while Q2 starts on Wednesday 1 July, so a plan-first join on date_trunc('week')
   drops the 25 orders of 1 to 5 July (Rs 15,39,820). The fix accumulates both sides and reads the
   booked-to-date at week_start + 6, which closes on Rs 9,84,00,000.
5. **"PostgreSQL Exercises, window functions category, first three" becomes three named pages.**
   The site has no separate window functions category; its window questions sit in the Aggregation
   category. The first three there are countmembers, nummembers and fachours4, and the take-home
   names them with their check dates.
6. **The take-home builds its sample by rerunning build_v4 under a new seed.** The generator has no
   seed flag, so the builder imports it and sets `SEED` before calling `build_v4`. It then adds a
   three-way tie across Retail-Core positions 19 to 21, and takes the added rupees off Q2's last
   Business order so the quarter still lands on Rs 9,84,00,000.
7. **The take-home's ask is Marketing's, on Retail-Core, with the head of Retail-Plus's tie rule.**
   `docs/07_Client_Zero.md` has no head of Retail-Core, so the brief does not invent one.
8. **No decision workbook ships today.** The standard's volume table does not require one, and the
   day's decision, the tie rule, moves on the companion page.
9. **Monday's row says v4 carries exact amount ties in the top ten for today's RANK demonstration.**
   Neither the order amounts nor the Q2 member totals in v4 tie in the top ten; the tie the row and
   `docs/07` name for today sits at fiftieth in Retail-Plus, and the pack follows today's row. The
   mechanism is shown on six invented members instead.
10. **Kahoot Q5 tests ROW_NUMBER's arbitrary cut at a tie, in place of the row's window-in-WHERE
    item.** The row's Kahoot plan lists "a window function inside WHERE; why refused and the fix".
    The requester's brief for this build says that error gets two minutes when it happens and never
    an exercise item, and the requester outranks the row, so the error stays a two-minute aside in
    Round 1 and the Kahoot slot tests a list that changes between runs because ROW_NUMBER cut a tie
    with no tiebreaker. The interview question on the error stays, since it is the row's anchor.
11. **The study notes run to about 4,400 words of prose.** The standard asks for about 4,000; the
    count is 5,272 with code, Mermaid and tables, and the twelve full interview answers carry most of
    the difference.

---

## Invented, and recorded as invented

1. The six invented members A to F of Round 2 (Rs 7,500, 7,500, 6,000, 5,200, 5,200 and 4,100),
   which show the three functions side by side, and the invented top four with a tie at fourth
   (Rs 9,100, 8,800, 8,200, 7,400, 7,400 and 6,900), which shows four rules shipping 4, 5, 5 and 3
   rows. Both sit in `sql/C2_W02_D03_02_protect_list_STUDENT.sql`, notebook 02 and the deck, labelled
   invented wherever they appear.
2. The members on the companion page, `demos/C2_W02_D03_tie_STUDENT.html`, which are invented for the
   simulator and labelled so on the page.
3. The take-home's three-way Retail-Core tie, added to the second sample by the builder.
4. Marketing's escalated-case message in `sql/C2_W02_D03_04_marketing_case_STUDENT.sql` and the
   take-home's ask, both written in the row's voice for this pack.
5. The trap values in the quizzes and exercises, which avoid the planted amounts and member ids.

---

## Sources, with the date each was checked

| Link | Role | Checked |
|---|---|---|
| https://www.postgresql.org/docs/16/tutorial-window.html | PostgreSQL 16, Tutorial 3.5, Window Functions | verified 29 Sep 2026, returned 200 |
| https://www.postgresql.org/docs/16/functions-window.html | PostgreSQL 16, 9.22 Window Functions, the list of row_number, rank, dense_rank, lag and lead | verified 29 Sep 2026 |
| https://www.postgresqltutorial.com/postgresql-window-function/ | postgresqltutorial.com, the window functions page | verified 29 Sep 2026 |
| https://www.youtube.com/watch?v=Ww71knvhQ-s | techTFQ, "SQL Window Function, How to write SQL Query using RANK, DENSE RANK, LEAD/LAG" | checked 29 Sep 2026 through YouTube's oEmbed endpoint, which returned the title and channel; the watch page refused the automated request, so the running time was not checked |
| https://pgexercises.com/ | PostgreSQL Exercises; no separate window functions category, the window questions sit in Aggregation | verified 29 Sep 2026 |
| https://pgexercises.com/questions/aggregates/countmembers.html | The first window question, a total count on every row | verified 29 Sep 2026 |
| https://pgexercises.com/questions/aggregates/nummembers.html | The second, a numbered list of members | verified 29 Sep 2026 |
| https://pgexercises.com/questions/aggregates/fachours4.html | The third, the facility with the most slots with every tied result output | verified 29 Sep 2026 |
| https://sqlbolt.com/ | SQLBolt, for anyone still shaky on joins | verified 29 Sep 2026 |
| https://www.pgtutorial.com/ | pgtutorial.com, clause syntax cross-checks | verified 29 Sep 2026 |

The row carried pgexercises.com, postgresqltutorial.com, pgtutorial.com and sqlbolt.com as verified
05 Sep 2026; each was re-checked on 29 September 2026 before it entered this pack.

---

## Tool versions

Every number and output in the pack came from PostgreSQL 16.13, Python 3.11, pandas 3.0.6,
psycopg2 2.9.13, SQLAlchemy 2.1.1 and nbclient 0.11.0, checked on 29 September 2026. The runtime
error quoted in the day sheet and the decks, `ERROR:  window functions are not allowed in WHERE`, was
produced by running the query on PostgreSQL 16.13, which prints two spaces after the colon.

The decks were built with mermaid-cli 12.0.0 in the build container. That version no longer takes
`-w`, which `scripts/build_deck.py` passes, so every diagram would fall back to monospace text. The
build put a shim first on PATH that drops `-w` and `-H` before calling mmdc, and every diagram then
rendered; the rendered slides were checked through LibreOffice with Carlito installed. The cheat
sheet's diagram renders as SVG, a path that never passes `-w`, and its PDF was checked by eye.
