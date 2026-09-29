# Solution: round 1 set, read the profile before any total

Answers: 1c 2c 3d 4d 5a 6b 7c

## The idea being tested

A profile is three counts per field, present, convertible and distinct, and each count answers a
different question about the file. Every item asks you to read one of them as a business fact
before any total leaves the team, and three of them stage the round's trap in a new place: a
conversion that hides its failures.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | Text compares character by character, and "9" sorts above "4" and "1", so `max` returns "950". | a: nothing converts the text. b: max takes the largest, never the middle. d: max works on text, which is why the mistake is silent. |
| 2 | c | North's two failed amounts are known, countable and can be logged. South has 19 rows beyond one per order, which inflates any total. | a: converting cleanly says nothing about copies. b: a failure you can count is not a reason to stop. d: equal row counts hide South's 19 extra rows. |
| 3 | d | No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the fingerprint of a coercing helper. | a: a free order would still carry a line and a reason. b: the files book cancelled orders at their value, as Monday counted them. c: zero is a claim the profile cannot support. |
| 4 | d | 180 rows hold 171 orders, so 9 rows repeat an order and add rupees that were never earned. | a: an optional discount does not move booked revenue. b: three channels is right for app, web and store. c: two orders can share an amount without being the same order. |
| 5 | a | The error names the line and column; reading it tells you whether the file was cut, malformed or merged. | b: skipping the feed hides the problem. c: asking for a resend before looking wastes the ERP team's time. d: a parse error on a file is not transient. |
| 6 | b | The CSV writes a missing value as an empty string, so `r["status"]` returns `""`; the JSON leaves the key out, so the same line raises KeyError. | a: nothing sets a default. c: the JSON record has no key to return. d: the CSV row carries the key with an empty value. |
| 7 | c | Rows less distinct order ids: 150 minus 141 is 9. Convertible amounts are a separate count. | a: 150 less 148 is the failed amounts. b: 9 less 2 mixes the two counts. d: 9 plus 2 adds them. |

## The part worth arguing about

Item 2. Some pairs will pick South because "every amount converts" sounds cleaner. That is the
round's trap read backwards: a clean conversion count says nothing about whether a row is a second
copy of an order, and South's copies are what would reach Anand as extra revenue.

## Where the pattern lives in production

Every warehouse load has a profile step for this reason. A nightly job that turns failures into
zero passes every row-count check and reports revenue that is wrong by the orders it zeroed; a job
that counts and logs failures raises one alert and loses nothing.
