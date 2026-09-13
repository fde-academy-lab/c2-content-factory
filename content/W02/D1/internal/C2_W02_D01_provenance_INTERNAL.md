# Provenance: Week 2, Monday

INTERNAL. Not a trainer artifact and not a learner artifact.

## Constructions, marked as such

The curriculum row says the warehouse holds "the same orders and customers you cleaned last week,
one thousand orders for the two quarters". Week 1 shipped 186 distinct orders from a 200-row file,
and its quarter totals of Rs 2.10 crore and Rs 1.90 crore are computed off those. The two cannot
both be literally true.

**The construction, approved in session on 13 September 2026:** the warehouse is the full
two-quarter book, and Week 1's file was a 200-row extract the data team pulled before the room had
database access. Monday's opening move becomes reconciling the two rather than pretending they
match. This is not in `docs/07_Client_Zero.md` and is recorded here as an invention.

What it costs: Week 1's levels no longer reproduce from the warehouse. What it buys: a real
analyst moment, and the sample's *shape* does reproduce, which is the honest and teachable half.

## Numbers, and where each comes from

Every figure below is asserted by `python3 data/generate_client_zero.py --contract` and was
re-proved in `psql` against the loaded database on 13 September 2026.

| Figure | Value | Asserted |
|---|---|---|
| Orders in the warehouse | 1,000 | Yes |
| Q1 revenue | Rs 10,00,00,000 | Yes |
| Q2 revenue | Rs 9,84,00,000 | Yes |
| Retail-Plus order change | minus 34.9 percent | Derived, matches Week 1's clean minus 35.0 |
| Retail-Core order change | minus 3.0 percent | Derived |
| Customers | 340 | Yes |

The Q2 total is 1.6 percent below Q1, which is the same relationship Week 1's cleaned extract
carried. That was chosen so the sample's shape survives, not arrived at by accident.

## Error text: the row against reality

The row's WHAT THE DATA REVEALS column paraphrases the grouping error as
`ERROR: column "segment" must appear in the GROUP BY clause or be used in an aggregate function`.

Postgres 16.13 qualifies the column with its table alias. The real text, which every artifact in
this pack carries, is:

```
ERROR:  column "o.channel" must appear in the GROUP BY clause or be used in an aggregate function
```

The pack uses the real text. The row's version is a paraphrase and does not need correcting.

## Links

| Link | Used in |
|---|---|
| <https://sqlbolt.com/> (verified 13 Sep 2026) | pre-read, study notes, after-class |
| <https://www.pgtutorial.com/> (verified 13 Sep 2026) | study notes |
| <https://www.youtube.com/watch?v=qw--VYLpxG4> (verified 13 Sep 2026) | pre-read, study notes |

The video was confirmed live by title and channel through the oEmbed endpoint: "Learn PostgreSQL
Tutorial, Full Course for Beginners", freeCodeCamp.org. The row carries no video slot, and the
method asks for one per new topic, so this is an addition rather than a copy.

## Environment

The SQL days need a running Postgres, which the devcontainer did not have. Added in the same
branch: the `ghcr.io/itsmechlark/features/postgresql:1` feature, verified on containers.dev at
version 1.9.0 on 13 September 2026, plus `.devcontainer/load_warehouse.sh`, plus the official
Microsoft PostgreSQL extension `ms-ossdata.vscode-pgsql`.

Every query in this pack was executed against Postgres 16.13 during the build.

## Open, for the reviewer

Nothing is blocked. One judgment worth a second opinion: the take-home asks for two questions
"answerable from orders and customers alone", which rules out the payments table deliberately so
Tuesday opens clean. A reviewer who thinks the constraint is artificial should say so.
