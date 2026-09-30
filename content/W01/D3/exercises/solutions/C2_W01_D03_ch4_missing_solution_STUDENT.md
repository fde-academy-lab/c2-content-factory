# Solution: chapter 4 set: what is missing or malformed

Answers: 1c 2a 3d 4b 5d

3 of 5 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | c | design | Revenue stays whole and the order stays out of every count that needs its status. | a: removes a booked order. b and d: invent a fact nobody recorded. |
| 2 | a | read | No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the fingerprint of a coercing helper. | b: a free order would still carry a line and a reason. c: the files book cancelled orders at their value. d: zero is a claim the profile cannot support. |
| 3 | d | read | The CSV writes a missing value as an empty string, so `r["status"]` returns `""`; JSON leaves the key out, so the same line raises KeyError. | a: nothing sets a default. b: the JSON record has no key to return. c: the CSV row carries the key with an empty value. |
| 4 | b | design | A copy of the same extract repeats the defect and is no witness, so the order is rejected with its reason until an independent source supplies the value. | a: the feed copied the error. c: a word is not an amount, and Rs 14 is far below any Kalpa order. d: a zero is a false value that hides the defect. |
| 5 | d | design | 60 orders times Rs 90 is Rs 5,400, spread over 100 orders, Rs 54. | a: the blanks were ignored. b: halves the gap. c: divides by the wrong count. |
