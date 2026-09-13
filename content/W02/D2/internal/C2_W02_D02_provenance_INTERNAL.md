# Provenance: Week 2, Tuesday

INTERNAL.

## Numbers, and where each comes from

Every figure is asserted by `python3 data/generate_client_zero.py --contract` and was re-proved in
`psql` against the loaded warehouse on 13 September 2026.

| Figure | Value | Asserted |
|---|---|---|
| Rows a LEFT JOIN to payments returns | 1,450 from 1,000 | Yes |
| Orders carrying more than one payment row | 450 | Yes |
| Of those: instalment plans | 400 | Derived, proved in psql |
| Of those: gateway retries | 50 | Derived, proved in psql |
| Orders never paid | 30 | Yes |
| Payments whose order is not in the book | 8 | Yes |
| The naive total over the join, against the true book | 1.9952 times | Yes |
| Share of the book held by the 450 duplicated orders | Over 80 percent | Derived |

## The arithmetic the curriculum row implied

The locked client-zero file says three things at once: a LEFT JOIN grows 1,000 rows to 1,450,
50 orders carry gateway retries, and collected revenue doubles. Those only hold together one way.

1,450 rows from 1,000 orders with 30 unpaid means 1,420 rows across 970 paid orders, so 450 extra
payment rows. Fifty come from the retries the file names, so 400 come from orders paid in two
instalments, which the Tuesday scenario text already mentions.

For the total to double, those 450 duplicated orders must carry as much revenue as the whole paid
book. That is only true if the instalment orders are the large invoices, which is true of real
businesses: corporate buyers settle big orders in parts. The generator selects the instalment set
as the top 400 paid orders by value, which is why the ratio lands at 1.9952 rather than at some
uninformative 1.2.

This is a construction in the sense that the locked file does not say which orders get instalment
terms. It is recorded here.

## A change made during the build

The first version selected the 30 unpaid orders as the last 30 delivered in list order, which put
them all in small consumer orders and left Anand's Q2 gap at Rs 23,320 across the whole quarter.
A gap that small is not a business story and the day's closing report had nothing in it.

The generator now takes two of the thirty from Q2 corporate invoices on different channels. The
Q2 gap by channel is now store Rs 9,51,970, web Rs 7,81,710 and app Rs 500. The contrast between a
channel with a problem and one without is what makes the report worth reading.

All fourteen v4 contract assertions still pass after the change.

## Error text

No Postgres error is staged today. The failure is a query that runs perfectly and returns a number
that is twice the truth, which is deliberately a different shape of failure from Monday's. The
"exact wrong output" the method asks for is the ratio 1.9952, and every artifact carries it.

## Links, all verified 13 September 2026

| Link | Used in |
|---|---|
| <https://sqlbolt.com/> (verified 13 Sep 2026) | pre-read, study notes |
| <https://pgexercises.com/> (verified 13 Sep 2026) | study notes |
| <https://www.youtube.com/watch?v=FprFu75BoE4> (verified 13 Sep 2026) | pre-read, study notes |

The video was confirmed live by title and channel through the oEmbed endpoint: "POSTGRESQL JOINS
[Complete guide in 12 mins]", cudidotdev.

## Open, for the reviewer

The take-home requires a join where a fan-out is possible, which rules out `orders` to `customers`
and forces `payments` or `refunds`. A reviewer who thinks that over-constrains a first join
exercise should say so; the alternative is a take-home that can be satisfied by a safe join, which
does not test the habit the day exists to build.
