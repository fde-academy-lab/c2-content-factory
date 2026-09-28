# Solution: predict before you run

Answers: 1b 2c 3a 4d 5c 6a

## The idea being tested

Python decides what an operation means from the types of its values before it looks at their size,
and a notebook decides what exists from the cells it ran. Every item is one of the day's traps, met
once on the screen and once somewhere new, so a prediction that was right by luck on the first
cell is tested again on the second.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | A dictionary matches keys exactly, so `"Amount"` is not `"amount"`: `KeyError: 'Amount'`. | a: Python never folds the case of a key. c: a missing key raises; `.get()` is the form that returns None. d: nothing in the record is blank. |
| 2 | c | Text and a number have no order between them: `TypeError: '>' not supported between instances of 'str' and 'int'`. | a and d: Python never converts text to a number on its own. b: text does not sort against numbers at all in Python 3. |
| 3 | a | `round()` returns a number, and 1.30 is the number 1.3, so the zero is dropped. An f-string with `:.2f` is how two places are shown. | b confuses the value with its display. c: round goes to the nearest, and 1.3043 is nearer 1.30. d: rounding to two places keeps two places. |
| 4 | d | `count = 0` inside the loop resets on every pass, so the last pass leaves 1. The start belongs before the loop. | a is what the code was meant to do. b: the update runs after the reset on every pass. c: a name can be assigned as often as the code likes. |
| 5 | c | 1200 plus 950 is 2150, and the third value is text, so `+=` stops with a TypeError and `total` keeps 2150. | a: nothing converts the text. b: the loop cannot skip the text silently. d: the error is about the type, and a ValueError needs a call such as `int()`. |
| 6 | a | Five values, so `len(amounts) // 2` is 2, and index 2 is the third value, 2060: the single middle of an odd count. | b and c are the values either side, the off-by-one in each direction. d averages two middles, which is the even-count rule. |

## The part worth arguing about

Item 3. Several pairs will say both a and b are fine, because 1.3 and 1.30 are the same number. They
are, and that is the point of the item: `round()` changes the value and says nothing about how it is
shown, so the zero a report needs comes from formatting, never from rounding.

## Where the pattern lives in production

Every one of these is a bug that ships. A key typed from memory raises in a nightly job; a text
amount stops a revenue script on the one row a person typed by hand; a reset inside a loop reports
one order when there were thousands; and an off-by-one median passes review because the number
looks plausible. The habit that catches all four is the one this drill trains: say what a cell will
print before it runs.
