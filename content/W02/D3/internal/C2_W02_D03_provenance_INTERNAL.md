# Provenance: Week 2, Wednesday

INTERNAL.

## Numbers

Asserted by `--contract` and re-proved in `psql` on 13 September 2026.

| Figure | Value | Asserted |
|---|---|---|
| Retail-Plus members with a Q2 spend | 73 | Derived |
| The tie at the fiftieth position | Two members at Rs 3,350 | Yes |
| Names shipped by ROW_NUMBER at 50 | 50 | Derived, proved in psql |
| Names shipped by RANK at 50 | 51 | Derived, proved in psql |
| Names shipped by DENSE_RANK at 50 | 52 | Derived, proved in psql |
| Members falling in each of the three Q2 months | 3 | Yes |
| Their ladders | 4200/3100/1900, 3800/2600/1400, 4400/2900/1600 | Derived |
| Plan line | 13 weeks at Rs 75,69,230 | Derived |

## Something the build produced that the row did not ask for

The dataset carries a **second** tie, at positions forty-eight and forty-nine, at Rs 3,480. It was
not planted deliberately; it fell out of a book of a thousand orders with amounts in round tens.

It is kept because it improves the day. `DENSE_RANK` at fifty ships fifty-two names rather than
fifty-one precisely because of it, which gives the three functions three different answers instead
of two, and it rewards a room that looks at the whole boundary rather than one row of it.

The day sheet tells the trainer it is there and tells them not to point at it.

## The protect list by segment

| Segment | Names shipped at RANK <= 50 |
|---|---|
| Business | 35 |
| Retail-Core | 50 |
| Retail-Plus | 51 |
| Student | 20 |

Business and Student ship fewer than fifty because they have fewer than fifty members with Q2
spend. The solution file states this rather than treating it as a defect, since a segment smaller
than the cut-off is a normal thing for a top-N report to meet.

## The running total

Revenue runs ahead of the plan line from the third week and lands at Rs 9,84,00,000 against a plan
cumulative of Rs 9,83,99,990, a difference of Rs 10 from integer division across thirteen weeks.

The first week of the grouping, beginning 29 June, has no plan row because the plan line starts on
6 July, so the LEFT JOIN leaves that cell NULL. That is left in rather than smoothed away: it is a
real edge and the solution comments on it.

## Error text

```
ERROR:  window functions are not allowed in WHERE
```

Captured from Postgres 16.13 during the build, not quoted from the row.

## Links, all verified 13 September 2026

| Link | Used in |
|---|---|
| <https://pgexercises.com/> (verified 13 Sep 2026) | pre-read, study notes |
| <https://www.postgresqltutorial.com/> (verified 13 Sep 2026) | study notes |
| <https://www.youtube.com/watch?v=D2xUEYR-GIY> (verified 13 Sep 2026) | pre-read, study notes |

The video was confirmed live by title and channel through the oEmbed endpoint: "Advanced SQL Full
Course | Master Joins, Window Functions, Subqueries, CTEs in SQL", DataCamp.

## Open, for the reviewer

The take-home asks for a window query and a `GROUP BY` impostor that must return different results
on the real warehouse. That is a harder constraint than it looks, and it is deliberate. A reviewer
who finds it too hard for one evening should say so; the fallback is to allow the honest
hand-in the brief already permits, which is one sentence saying the window was decorative.
