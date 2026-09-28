# Solutions: the librarian's log

Week 0, Wednesday. Released once the exercise has closed.

## The idea being tested

Each item asks one of the five ideas from the class a question it can only answer if the idea is
understood rather than recognised: what type a value carries, which position and key reach a field,
where a running total starts, what a function hands back, and which line of a traceback to read
first.

## The answers

Answers: 1a 2d 3c 4d 5b 6c 7c 8b 9a 10d 12a

Item 11 is an order, so it takes four letters: b c d a.

| No. | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | `len` counts the six letters, and `*` on text repeats it with nothing between the copies | Twelve counts the repeated word; the spaced pair adds a space Python never inserts; one counts the word rather than its letters |
| 2 | d | `/` always gives a float, `//` drops the remainder of 20 by 3, and `%` is that remainder | The bare 5 forgets that `/` gives a float; 6.67 is what `/` would give, never `//`; 0.67 is a fraction where `%` gives the whole remainder |
| 3 | c | Position 4 is the fifth issue, and the key names the field | Position 5 is the sixth issue; the list has positions and no keys; the issue number is a whole number, which has no fields |
| 4 | d | Poetry was kept 5 days and then 9, and both are Arts | Two counts the Arts issues instead of adding their days; nine is only the last Arts issue; 91 adds every department |
| 5 | b | The total starts once, before the loop, so each late issue adds to it | Counting 14 as late still resets the total on every issue; printing inside the loop shows one issue at a time; adding days changes what is counted and keeps the reset |
| 6 | c | A new student starts at 0, and the next line adds the first 1 | Starting at 1 counts every student's first issue twice; rebuilding the dictionary throws away every earlier student; a dictionary has no `append` |
| 7 | c | S01 borrowed Algebra and Calculus, and five different students appear | Eight counts issues rather than students; one misses S01's second book; 32 is S01's days kept, not issues |
| 8 | b | The function prints 7, then hands back `None`, which the second print shows | A second 7 needs a `return`; `None` cannot come first, since the call runs before `result` is printed; the second print always shows something, even `None` |
| 9 | a | Twenty is 6 past the 14-day loan and not past a 21-day loan, so the second call returns 0 | Minus one would need the function to subtract without checking the loan; the second 6 ignores the loan it was given; 20 is the days kept rather than the days over |
| 10 | d | The last line says what happened, and the `NoneType` on the right means `days_over` returned nothing | The first line of a traceback only says a traceback follows; `late` is the `int`, on the left; the called function is exactly where the `None` came from |
| 11 | b c d a | Start the total, open the loop, update once per issue, read the total after the loop | Any other order prints before the total exists or starts it again inside the loop |
| 12 | a | A returned total can be stored, added to and compared with next week's | Printing leaves her nothing to add; returning inside the loop hands back the first issue's days only; printing after the loop still hands back `None` |

## The part worth arguing about

Item 5 is worth a minute. The broken loop is valid Python and runs without an error, so nothing on
the screen says it is wrong; only the number 0 against the two late issues anyone can see in the log
gives it away. That is the most expensive kind of bug in a report, because it looks like an answer.

## Where this lives in production

A weekly library report, a canteen's daily takings and a hostel's attendance count are the same
program: a list of records, one loop per question, and a function per answer so next week's data
goes in without anyone editing a loop. Reading the last line of a traceback first is how every
engineer starts on an error, in any language.

## Hands-on picks

The hands-on notebook's twelve letters, in order: b d a a c d b c b d c a.
