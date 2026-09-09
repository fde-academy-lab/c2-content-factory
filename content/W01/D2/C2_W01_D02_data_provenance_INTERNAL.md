# Data provenance: Week 1, Day 2

Internal working file. Never given to a learner.

## Where this pack's data comes from

Every data file in this folder is generated, not hand-written. One command rebuilds all of them:

```
python3 data/generate_client_zero.py --version v0            --out content/W01/D2 --stem C2_W01_D02
python3 data/generate_client_zero.py --version w1d2-lab      --out content/W01/D2 --stem C2_W01_D02
python3 data/generate_client_zero.py --version w1d2-takehome --out content/W01/D2 --stem C2_W01_D02
```

The generator is seeded, so those commands produce byte-identical files on every machine and all
sixty learners hold the same data. Editing a data file by hand breaks that guarantee. Change the
generator instead, rerun the commands, then rerun the verification gate and both notebooks.

## What this pack was rebuilt from, and when

This pack was first built against placeholder field names, because client zero was frame locked and
no schema existed. `docs/07_Client_Zero.md` was locked at v1.0 on 09 September 2026, and the pack was
regenerated against the real schema the same day.

| Was | Is now | Source |
|---|---|---|
| `id` | `order_id` | Section 3 entity model, ORDERS |
| `date` | `order_date` | Section 3 entity model, ORDERS |
| `outcome` with values accepted, declined, pending | `status` with values delivered, returned, cancelled | Section 3 entity model, ORDERS |
| `segment_a` to `segment_d` | Retail-Core, Retail-Plus, Business, Student | Section 3, "Segments are four" |
| `feed_01` | `kalpa_retail_orders` | Section 2, Kalpa Retail is the spine vertical |
| Amounts from Rs 880 to Rs 23,600 | Amounts inside Rs 800 to Rs 3,000 | Section 3, "a typical order sits between Rs 800 and Rs 3,000" |
| No customer id, no discount column | `customer_id` and the optional `discount` | Section 3 entity model, and section 4 v0 |

The amount band moved, so every total in this pack moved with it. These are the current figures and
each one is computed from the generated files rather than typed.

| Figure | Value | Where it appears |
|---|---|---|
| Main file | 30 orders in, 28 clean, 2 rejected, total 53745 | deck half one, deck half two, both notebooks, activity, solutions, study notes, day sheet, tiered extras |
| Rejected orders, main file | KR4210 with `twelve`, KR4214 with an empty amount | the same files |
| Lab file | 24 in, 21 clean, 3 rejected, total 34515 | solutions holds all four; tiered extras holds the three counts |
| Take-home file | 30 in, and either 27 clean at 47645 or 26 clean at 49495 | take-home self-check |
| Truncated feed | `Expecting ',' delimiter: line 48 column 1 (char 1027)` | notebook 2 at runtime, exercises, day sheet |

## The witnesses this pack depends on

Each planted defect serves exactly one teaching point. `python3 data/generate_client_zero.py --list`
prints the full table. The ones Tuesday turns on:

- `KR4200` carries its amount as the text `4500`, which is Monday's type break arriving in a file.
- `KR4210` carries the word `twelve`, which is the `ValueError` the day is built around.
- `KR4214` has no amount in the CSV, and the JSON's nested `source.amount_raw` still holds `2840`.
  That contrast is the flattening-cost lesson, and removing it removes section 5 of notebook 2.
- The first six orders carry no discount, which is Monday's `.get()` with a default.
- The vendor feed stops mid-record at line 47, so the parser names a position that does not exist.

## Conflicts, now closed

Section 9 of `docs/07_Client_Zero.md` recorded four conflicts between that file and the curriculum
export. All four were ruled on at v1.1 on 09 September 2026, in the curriculum's favour, and the
client-zero file was edited to match rather than the other way round.

Two of them touched this pack and both are now settled in this pack's favour, so nothing here
changes: v0 at 30 orders is the Monday and Tuesday dataset, and `discount` is an optional field on
the order rather than on the customer.
