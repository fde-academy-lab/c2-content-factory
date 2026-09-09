# Link register: Week 1, Day 4

Internal working file. Never given to a learner and never merged into a student artifact.

## What is verified and shipped

| Reference | URL | Checked | Where it is used |
|---|---|---|---|
| CPython `statistics` module source, tag v3.12.0 | `raw.githubusercontent.com/python/cpython/v3.12.0/Lib/statistics.py` | 09 Sep 2026, HTTP 200 in the build session | Take-home exploration section; pre-read optional reading |

This link carries the take-home's fifth shortcut-resistance pattern. The learner has to open the file, find `def median(data):` and cite two specific things: that the first act is `data = sorted(data)`, and that an even-length input returns the average of the two middle values.

That second point is load-bearing for this pack rather than decorative. Kalpa's profiled file holds 44 orders, which is even, so today's median of Rs 1,910.00 is the average of Rs 1,865 and Rs 1,955 and **is not the amount of any Kalpa order**. A learner who reads the source discovers that the number they quoted all day does not exist in the data. The self-check names it as checkpoint 8.

## What is still blocked

The egress proxy answered 403 to CONNECT on these, tested in the build session on 09 Sep 2026:

| Domain | Result | What it was wanted for |
|---|---|---|
| `www.khanacademy.org` | 403 at the proxy, policy denial | The row's three trainer references on mean, median and mode |
| `seeing-theory.brown.edu` | 403 at the proxy, policy denial | The row's student reference, the frequentist inference chapter, previewing Monday |
| `en.wikipedia.org` | 403 at the proxy, policy denial | Anscombe's quartet, as a slide citation |
| `docs.python.org` | 403 at the proxy, policy denial | The `statistics` module documentation |

`raw.githubusercontent.com` is reachable and is the only reference domain that is. That is why this pack cites CPython source rather than documentation.

## The slots waiting

| File | Where | Blocking? |
|---|---|---|
| `C2_W01_D04_preread_STUDENT.md` | Optional exploration, the Seeing Theory chapter | No. The pre-read tells the learner to skip it if it has not appeared, and Monday does not depend on it. |

Deck half one's Anscombe slide (S23) states the 1973 result in prose with no URL, which is correct under the standing rule. If `en.wikipedia.org` or a primary source becomes reachable, add a dated citation to that slide.

## What to do when the proxy opens

Check each blocked URL above, then paste it into its slot with the date it was checked, **on the same line as the URL**. The verification script warns about any URL on a line without a date, so keep them together.

The row's own dates (03 and 05 Sep 2026) belong to the curriculum row and never to this pack. Recheck rather than copying them.
