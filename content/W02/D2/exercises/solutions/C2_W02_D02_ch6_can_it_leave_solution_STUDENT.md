# Solution: which checks must pass before the number leaves?

Answers: 1a 2b 3c 4d 5b 6c

## What does this set test?

The set tests whether a check can fail at all, which check stops each wrong report, and what leaves
the team on the day a check fails. Items 4, 5 and 6 are design items: the two checks
that cover three wrong reports, the reporting-day rule, and the source outside Kalpa's own tables.

## Why does each key hold, item by item?

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | trap | a | X is consistent with itself: collected 46,000 is at most booked 46,000, the gap of 0 is not negative, and the channels of its eight orders are all present. | b: 0 is not negative. c and d: nothing on X contradicts itself; only a check against the tables can see the two missing orders. |
| 2 | concept | b | Y repeats the multi-row orders, so its booked reads 65,000 against 50,000 in the orders table. | a: Y's gap equals the unpaid list's 4,000. c: 65,000 less 61,000 is 4,000, so it passes. d: 61,000 is at most 65,000. |
| 3 | concept | c | Z's gap of 3,000 misses the unpaid list's 4,000, and its collected 47,000 plus 1,000 posted twice is 48,000 against 47,000 in payments. | a: Z has all ten orders and a gap above zero. b: 50,000 less 47,000 is 3,000, and 47,000 is at most 50,000. d: Z's booked is right and every channel is there. |
| 4 | design | d | Booked against orders stops X (46,000) and Y (65,000); the gap against the unpaid list stops Z (3,000 against 4,000). Together they cover all three. | a: Z passes both, with ten orders and the right booked. b: all three reports pass both. c: all three reports pass both. |
| 5 | design | b | Booked ties to the orders table alone and leaves; collected, which this check guards, is held; the open line names the failed check, what it means and when it closes, and the platform lead hears that day. | a: puts an unreconciled figure on the CEO's page with a footnote nobody reads. c: withholds booked, which is reconciled. d: mixes two weeks on one page. |
| 6 | design | c | A settlement file comes from the gateway and the bank, so a difference against the payments table is evidence nobody at Kalpa wrote. | a: reads the same table again. b: compares two of Kalpa's own reports. d: recomputes Kalpa's own record. |

## Which item is worth arguing about?

Item 5's option a, the footnote, feels honest, and it is how a wrong figure reaches a leadership page
with a PASS stamp beside it. The rule separates what is reconciled from what is not, so the reader
never has to judge a footnote: booked goes out that day, collected waits, and the open line says when
it will follow.

## Where does this pattern live in production?

Wirecard's auditor, EY, refused to sign off on its 2019 accounts in June 2020, saying it was unable to
confirm that the money existed, and people with first-hand knowledge told the Financial Times that
from 2016 to 2018 the auditor had not checked directly with Singapore's OCBC Bank (BBC News, 18 June
2020; the FT, republished by the Irish Times, 26 June 2020; both checked 1 Oct 2026). A check that
reads a company's own records back to it cannot fail.
