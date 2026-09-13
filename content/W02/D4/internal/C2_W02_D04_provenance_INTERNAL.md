# Provenance: Week 2, Thursday

INTERNAL.

## Versions, verified during the build on 13 September 2026

| Thing | Version |
|---|---|
| pandas | 3.0.5, the current release on PyPI |
| SQLAlchemy | 2.0.52 |
| Postgres | 16.13 |

The curriculum row notes that current pandas docs cover pandas 3.0. Confirmed: the environment
runs 3.0.5 and `pip index versions pandas` lists it as the newest.

## Error text, captured rather than quoted

```
pandas.errors.MergeError: Merge keys are not unique in right dataset; not a one-to-one merge
Duplicates in right:
 customer_id
     C-0001
     C-0002
     C-0003
     C-0006
     C-0007 ...
```

The row paraphrases this as "Merge keys are not unique in right dataset". The real message
continues with the clause "not a one-to-one merge" and then lists the offending keys, which is
more useful in a classroom because it names what to look at next. Every artifact carries the full
text.

## Numbers

| Figure | Value | Asserted |
|---|---|---|
| Duplicate customer keys in the exposure feed | 6 | Yes, by `--contract` |
| Customer table rows before the exposure merge | 301, the customers who ordered | Derived |
| Rows after an unvalidated merge | 307 | Derived |
| Columns in the finished table | 9 | Checked in the notebook |
| Cells filled by the wrong-index pivot | under 40 percent | Checked in the notebook |

A correction made during the build: the demo notebook first asserted 8 columns and the table has
9, since `first_seen` comes across with `exposed`. The check now names every expected column
rather than counting them, which fails more usefully.

## A change to the shared kit

`scripts/c2kit.py` gains `engine()`, returning a SQLAlchemy engine. `pandas.read_sql` warns on a
raw psycopg2 connection, and a warning printed beside every table in a teaching notebook trains
people to ignore warnings. SQLAlchemy 2.0.52 was added to the environment for this.

## Links, all verified 13 September 2026

| Link | Used in |
|---|---|
| <https://pandas.pydata.org/docs/user_guide/10min.html> (verified 13 Sep 2026) | pre-read, study notes |
| <https://pandas.pydata.org/docs/user_guide/index.html> (verified 13 Sep 2026) | study notes |
| <https://www.youtube.com/watch?v=txMdrV1Ut64> (verified 13 Sep 2026) | pre-read, study notes |

The video was confirmed live by title and channel through the oEmbed endpoint: "Python Pandas
Tutorial (Part 8): Grouping and Aggregating - Analyzing and Exploring Your Data", Corey Schafer.

## Open, for the reviewer

The pivot round-trip point, that melting a pivot returns more rows than you started with because
every gap became a cell, is in the solutions and the study notes but not on a slide. It is a real
gotcha and it is also the fifth idea in a block that already carries four, so it was cut from the
deck deliberately. A reviewer who wants it on a slide should say which of the four it replaces.
