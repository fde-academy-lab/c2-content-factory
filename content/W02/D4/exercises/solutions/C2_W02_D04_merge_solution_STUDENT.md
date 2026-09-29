# Solution: round 2 set

Answers: 1c 2a 3d 4b 5a 6c 7b

## The idea being tested

A merge is a join: it multiplies rows when a key repeats, it keeps whatever `how` says, and a
duplicate in a feed is a business question before it is a pandas one. `validate=` turns the
row-count check into an error, and groupby's default quietly drops what has no key.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | 500 accounts, of which 230 appear once in the feed, 10 appear twice and 260 not at all: 230 + 20 + 260 = 510. The 10 repeated accounts each gain a row. | a is what the merge should return, and returns only when the feed is unique. b stacks, which is concat. d is an inner or right merge's idea of the feed. |
| 2 | a | `validate="one_to_one"` raises `MergeError` before the table exists when either side repeats a key. | b changes which rows survive and multiplies as much as before. c labels rows and never stops anything. d sorts the fan-out neatly. |
| 3 | d | The customer table has one row per customer, so extra rows can only come from repeated feed keys, and every repeat copies that customer's whole spend. | a: the feed carries exposures, never orders. b: sums of rupee amounts in the warehouse have no float drift at this size, and the row count rose. c: a left merge never adds customers from the right. |
| 4 | b | A duplicate is information about the source. Look, find the cause, state the rule, keep validate on. | a disables the guard to make the error go away. c ships this week's wrong table. d throws away customers who were reached, which understates reach. |
| 5 | a | "Did the sale reach them" is answered by the first exposure; a later one adds nothing to reach. | b answers the question too, with a different date, and hides when the sale first landed. c invents a spend split. d drops customers who were reached twice, the most-reached of all. |
| 6 | c | When the table was built from order rows, reached customers who never ordered have no segment, and `groupby` drops a missing key by default. | a: every customer in the feed is in the warehouse, which `indicator=True` confirms. b: 130 is already a distinct count. d confuses how that table was built with what groupby does. |
| 7 | b | `indicator=True` labels each row `both`, `left_only` or `right_only`; `left_only` on the customer table is the unreached. | a keeps only the reached. c starts from the feed, so the unreached are not in it. d: "both" is the reached, again. |

## The part worth arguing about

Item 5, option b. Some teams do keep the last touch, and for a question like "which message did
they see most recently" it is right. The rule follows the question: reach is first touch.

## Where the pattern lives in production

Campaign platforms, payment gateways and CRMs all re-send rows on retry. Every merge onto a
customer table in a scheduled job carries `validate=` for that reason, and teams that skip it
find out from Finance.
