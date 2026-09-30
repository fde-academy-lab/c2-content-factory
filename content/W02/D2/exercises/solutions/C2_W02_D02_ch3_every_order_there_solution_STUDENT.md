# Solution: is every booked order still in the report?

Answers: 1b 2a 3c 4b 5a 6d

## What does this set test?

The count that catches a dropped order, the bridge that separates two causes netted into one gap, and
a second route whose blind spot differs from the first. Items 2, 5 and 6 are design items: the proof
to run first under time pressure, where two independent methods part company, and what changes the
form of the proof at the quarter's close.

## Why does each key hold, item by item?

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | trap | b | The plain JOIN keeps U-1, U-2, U-4 and U-5: booked 7,700 against posted 8,700, so booked less posted is minus 1,000. U-3 and U-6, never paid, are gone. | a: 300 is the six orders' booked less posted, which only a LEFT JOIN keeps. c: forgets U-2's repeat inside posted. d: keeps six orders, which a plain JOIN cannot. |
| 2 | design | a | Orders in the report against the table, 4 against 6, needs no rupee, runs in a moment and fails the moment one order goes missing. | b: compares two totals that can both be wrong. c: catches it only if someone reads every line in ten minutes. d: a positive gap says nothing about a missing order. |
| 3 | arithmetic | c | 2,000 plus U-2's 1,500 once, plus U-4's 1,800 and 1,200, plus U-5's 700: 7,200. | a: 8,700 is posted, with U-2's repeat inside. b: 9,000 is booked. d: 7,700 is the plain JOIN's booked. |
| 4 | trap | b | Booked 9,000 less collected 7,200 is 1,800: U-3 and U-6 never paid, 900 and 400, and U-5 paid 500 short. | a: booked less posted nets the repeat against the gap, which is the one-number trap. c: leaves out U-5's 500. d: posted twice sits above collected, outside the gap. |
| 5 | design | a | The instalment route would count a retry written under a new instalment number as a second instalment, while the cap stops at booked, so only there do they part. | b: both routes count two genuine instalments in full. c: both give an unpaid order nothing. d: both give U-1 its 2,000. |
| 6 | design | d | Ticking every order needs every order on a page, so the statement travels as an appendix while the report itself keeps its count and bridge. | a: one number hides both causes. b: the count cannot say which order is short. c: a bar without its list cannot be ticked. |

## Which item is worth arguing about?

Item 1, option c. A pair who spots the dropped orders sometimes expects the gap to vanish to zero.
It comes out negative because U-2's repeated posting sits inside posted, which is the other error in
the same draft: two faults, one of which drops rupees and one of which adds them.

## Where does this pattern live in production?

Public Health England left 15,841 positive COVID-19 cases out of the daily figures reported between
25 September and 2 October 2020 (GOV.UK, 4 October 2020); the BBC reported that the files were loaded
into old XLS templates that held about 65,000 rows (BBC News, 5 October 2020), both checked 30 Sep
2026. No row that arrived was wrong, and a count of rows sent against rows loaded would have caught it.
