# Data provenance: Week 1, Day 1

Internal working file. Never given to a learner.

## Where this pack's data comes from

The thirty Kalpa Retail orders this day runs on are generated, never typed. One command rebuilds
them:

```
python3 data/generate_client_zero.py --version w1d1 --out content/W01/D1 --stem C2_W01_D01
```

That writes `content/W01/D1/C2_W01_D01_data_orders_STUDENT.py`, which holds `records = [ ... ]`.
The generator is seeded, so the command produces a byte-identical file on every machine and all
sixty learners hold the same thirty orders in the same order. Editing a data file by hand breaks
that guarantee. Change the generator instead, rerun the command, then rerun the verification gate
and both notebooks.

## Why Monday's records are a Python literal and not a file

Monday's curriculum row stops before files and before any import statement, so the day cannot open a
data file at all. The same list therefore sits inline in the setup cell of each notebook and again in
the handout copy, and every one of those copies is written from the same generator function, so they
cannot drift apart. When an amount changes it changes in the generator, and every copy is rewritten
from there. Nobody retypes a record and nobody shortens the list to make it fit a slide.

## Monday's records and Tuesday's files

This is a build decision and it is worth stating plainly. Monday holds the thirty orders as the
Kalpa team keyed them into the system, so they are clean apart from the one planted text amount and
the day has exactly one type break in the way. Tuesday's CSV and JSON are the vendor export of those
same thirty orders, and the export is where the two further defects enter.

Two records carry the join between the two days, and neither amount may be changed on one side
alone.

| Record | On Monday | In Tuesday's export |
|---|---|---|
| `KR4214` | The amount reads Rs 2,840 on an ordinary delivered Student order. | The CSV amount cell is empty and the JSON's nested `source.amount_raw` still holds `2840`. Monday's amount is set to Rs 2,840 so that it agrees with the value Tuesday recovers from that nested field. |
| `KR4210` | The amount reads Rs 1,625 on an ordinary delivered Business order. | The amount arrives as the word `twelve`, which is the `ValueError` Tuesday is built around. |

## The witnesses this pack depends on

Each planted defect serves exactly one teaching point.
`python3 data/generate_client_zero.py --list` prints the full table. The three the `w1d1` version
turns on:

- The amount is stored as the text `4500` on `KR4200`, which is Monday's type break.
- The `discount` key is absent on 28 of the 30 records, which is Monday's `KeyError` and the
  `.get()` with a stated default.
- Every other amount is typed as an integer, so exactly one comparison fails and the break is one
  record and not the whole column.

Removing any one of them removes a block. `KR4200` carries the `TypeError` in block one and the
conversion at the point of use that the day ends on. The absent `discount` carries the whole
optional-field idea in block two. The single failing comparison is what lets the room see that a
column can look uniform on screen and still hold one value of another type.

## Every figure this pack states, and where it appears

Every number below is computed from the generated file rather than typed. A figure that is not in
this table does not belong in an artifact.

| Figure | Value | Where it appears |
|---|---|---|
| Records in the file | 30 | Every artifact in the pack states it |
| Total of all amounts | Rs 58,210 | notebook 1, take-home self-check, tiered extras |
| Smallest and largest amount | Rs 840 and Rs 4,500 | The largest amount reaches both teaching decks, both cheat sheets, exercises, the Kahoot pack, solutions, study notes, tiered extras, both notebooks, the activity and the day sheet, because it is also the planted text amount. The smallest amount is stated nowhere and sits only in the data file. |
| delivered | 13 orders, Rs 25,720 | introduction deck, deck half one, deck half two, both cheat sheets, exercises, solutions, study notes, take-home self-check, notebook 1, day sheet |
| returned | 7 orders, Rs 13,670 | solutions, study notes |
| cancelled | 10 orders, Rs 18,820 | Approved and stated nowhere in the pack |
| Retail-Core | 8 orders, Rs 18,955 | Approved and stated nowhere in the pack |
| Retail-Plus | 8 orders, Rs 14,050 | notebook 2 |
| Student | 7 orders, Rs 12,945 | solutions, study notes |
| Business | 7 orders, Rs 12,260 | Approved and stated nowhere in the pack |
| Above Rs 2,000 | 13 orders, Rs 35,020 | both cheat sheets, deck half two, exercises, solutions, study notes, take-home self-check, notebook 2, activity, day sheet |
| At or below Rs 2,000 | 17 orders, Rs 23,190 | take-home self-check |
| Above Rs 1,500 | 17 orders, Rs 42,070 | take-home self-check |
| At or below Rs 1,500 | 13 orders, Rs 16,140 | take-home self-check |
| Above Rs 2,500 | 8 orders, Rs 23,865 | take-home self-check |
| At or below Rs 2,500 | 22 orders, Rs 34,345 | take-home self-check |
| Above Rs 1,000 | 28 orders, Rs 56,450 | take-home self-check |
| At or below Rs 1,000 | 2 orders, Rs 1,760 | take-home self-check |
| Above Rs 3,000 | 1 order, Rs 4,500 | take-home self-check |
| At or below Rs 3,000 | 29 orders, Rs 53,710 | take-home self-check |
| delivered and above Rs 2,000 | 6 orders, Rs 15,520 | solutions and study notes carry the count and the total, and the day sheet names the count on its own |
| Discount present on | KR4215 at Rs 75 and KR4223 at Rs 175, and nowhere else | Both notebooks name the two order ids, and notebook 2 states the two amounts |
| `r.get("discount", 0)` summed over 30 records | Rs 250 | both cheat sheets, deck half two, solutions, study notes, take-home self-check, notebook 2, day sheet |
| `r.get("discount", 100)` summed over 30 records | Rs 3,050, which is the wrong-default demonstration | The same files as the line above |
| Distinct order dates | 11, from 2026-08-03 to 2026-08-17 | The date range reaches deck half two, study notes and both notebooks, and deck half one and the activity name the first date on its own. The count of 11 is stated nowhere. |
| Returned order ids | KR4200, KR4203, KR4218, KR4221, KR4225, KR4226, KR4228 | solutions, study notes, both notebooks |
| The misplaced accumulator result | Rs 1,460, which is the amount of KR4224, the last delivered order in the file, and not a sum of anything | deck half one, solutions, study notes, notebook 1, day sheet |

Five approved figures reach no artifact: the smallest amount, the cancelled group, the Retail-Core
group, the Business group, and the count of distinct order dates. They stay in this table because a
trainer who is asked one of them in the room can read the checked value here rather than guess at
it, and because a later edit that needs one already has it.

## The two thirteens

Two different thirteens live in this day and they are unrelated. Thirteen orders were delivered and
they total Rs 25,720, and thirteen orders sit above Rs 2,000 and they total Rs 35,020. The overlap
between the two sets is the 6 orders totalling Rs 15,520 that answer the third unguided question. No
sentence in any artifact may imply that the two thirteens describe the same set of orders, and any
edit that puts both numbers on one screen has to name the condition beside each of them.

## Open conflicts

### New, and raised by this day's build

| # | The locked file says | The curriculum row says | Resolved as, for now |
|---|---|---|---|
| 5 | Section 4 describes v0 as about 30 flat order records with a nested customer sub-record on some of them. | The Monday row calls for about 30 flat client-zero records loaded by a setup cell, with an id, a segment, an amount, an outcome and a date. | Resolved in the curriculum's favour, since the curriculum outranks the client-zero file. Monday's thirty records are flat, and the nested customer sub-record first appears in Tuesday's JSON, where the cost of flattening it is the lesson. |
| 6 | Section 4 lists v0's witnesses as one set, so the word `twelve`, the record missing a required amount, the nested sub-record and the truncated line all sit inside the version first used on Monday. | The Monday row names one planted text amount and the optional field reached through `.get()`, and no other defect. | Resolved in the curriculum's favour. The `w1d1` build takes the same thirty orders and holds back the two defects that belong to Tuesday, so Tuesday's opening `ValueError` still lands on a room that has never seen it. |

### Carried forward from section 9 of docs/07_Client_Zero.md

These four are already recorded there and none of them is new. They are repeated in one line each so
that this pack can be read on its own.

| # | The conflict | Resolved as, for now |
|---|---|---|
| 1 | Section 4 puts v1 at 50 records from Week 1 Tuesday to Thursday, while the curriculum rows put 50 records at Wednesday and about 30 at Tuesday. | v0 at 30 records carries Monday and Tuesday, and v1 at 50 records starts on Wednesday. |
| 2 | Section 4 plants the near-duplicate pair with one differing timestamp, while the Wednesday row says the pair shares an id and differs on one field. | The pair differs on `order_date`, since the section 3 entity model gives ORDERS a date and no timestamp. |
| 3 | Section 4 names `discount` as v0's optional field, while the section 3 entity model gives CUSTOMERS an optional `loyalty_tier` and no `discount` anywhere. | Both fields exist. `discount` sits on the order and is the optional field Monday reads through `.get()`, and `loyalty_tier` sits on the customer and stays untouched until it is needed. |
| 4 | Section 3 says a typical order sits between Rs 800 and Rs 3,000, while no curriculum row states an amount range. | The generator draws typical orders inside that band, and KR4200 at Rs 4,500 sits outside it on purpose as the planted largest amount. |
