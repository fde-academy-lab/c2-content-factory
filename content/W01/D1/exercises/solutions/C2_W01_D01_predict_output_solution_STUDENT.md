# Day 1 solution, E2. Predict the output

## The idea being tested

Every item on this sheet turns on one question: what are the two values on either side of the operator, and what does the operator mean for those two types? A learner who asks that question first gets fourteen of the fifteen without running anything, and the fifteenth is arithmetic.

The reason this runs before the find-the-mistake drill is that prediction is cheap and diagnosis is expensive. A room that has already been wrong about a printed number in public is a room that reads the next number properly.

## The answers

**Answers: 1d 2a 3b 4c 5a 6c 7b 8d 9a 10b 11a 12d 13c 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | d | Quotes make text, so `type('4500')` is `str` whatever the characters inside look like. | a reads the digits rather than the quotes; b prints the value, which `type()` never does; c invents an error, since quoted digits are perfectly ordinary text. |
| 2 | a | The two calls return two different type objects, and different objects compare as unequal. | b treats the printed digits as the thing being compared; c names the type of the result rather than the result; d assumes types cannot be compared, when they compare fine and simply disagree. |
| 3 | b | Two of the three are delivered, at Rs 2,395 and Rs 1,360, which is Rs 3,755. | a totals all three, ignoring the condition; c keeps only the returned order, which the condition excludes; d keeps only the first delivered order, which is the reset bug from the next drill. |
| 4 | c | With the condition gone, all three amounts land in the accumulator, giving Rs 5,195. | a is the answer with the condition still in place; b is one record; d would need the accumulator reset inside the loop after the addition. |
| 5 | a | Text compares character by character, and `"9"` sorts after `"2"`, so the shorter, larger-looking number wins. | b applies numeric reasoning to text; c assumes text has no ordering, when it has a strict one; d confuses a comparison with a lookup that found nothing. |
| 6 | c | Nine hundred is smaller than two thousand, so the comparison is `False`. | a inverts it; b confuses a printed `False` with nothing being printed; d assumes a refusal, which only happens across two different types. |
| 7 | b | Item 6 compares two numbers, so its answer is about size. Item 5 compares two strings, so its answer is about spelling. | a treats strictness as a property of text; c writes off item 6, which is honest; d treats the operator as the thing that decides, when the operands decide. |
| 8 | d | The types are the whole story, and they are invisible in the printed output. | a and b name facts that would not change either line; c names a fact about the room rather than the data. |
| 9 | a | The counter runs once per record, three times, and once more on the returned order, so four. | b counts records and misses the second increment; c is one record; d doubles every record rather than the returned one. |
| 10 | b | Adding two strings joins them, so `"1460" + "0"` is `"14600"`, printed without its quotes. | a reads the zero as a number; c gets the digits right and the type wrong, which is the near miss worth arguing about; d assumes text refuses addition, when text defines it as joining. |
| 11 | a | A number and a piece of text have no shared meaning for `+`, so Python refuses and names both types. | b assumes the number is converted to text; c assumes the text is converted to a number; d dresses up b with quotes. |
| 12 | d | Rs 25,720 across thirteen orders is Rs 1,978.46, which rounds to Rs 1,978. | a is one order's amount; b divides by ten; c is a plausible round number with nothing behind it. |
| 13 | c | Rs 58,210 minus Rs 25,720 is Rs 32,490, which is 55.8 percent of the file. | a and b undercount badly; d overcounts and would leave delivered orders at a fifth of the money. |
| 14 | b | A number that runs cleanly has proved only that no operator refused it. The find-the-mistake drill in the next fifteen minutes prints Rs 1,460 without a murmur. | a is the belief the whole day is built to break. |
| 15 | c | Every comparison hands back a `bool`, whatever the operands were. | a confuses `True` printing as `1` in arithmetic with the type itself; b guesses text; d names the value rather than the type. |

## The part worth arguing about

Item 10 against item 11. The same `+` sign either joins or refuses, depending on nothing more than what sits on each side of it. Ask the room which of those two behaviours they would rather Python had chosen for a mixed pair, and let them argue. The answer that matters is that a silent conversion in either direction produces a number nobody can trace, and the refusal costs ten seconds.

Item 5 is the other one. A room usually splits on whether string comparison is a bug or a feature. It is a feature, and it is exactly the feature that sorts a list of names, which is why nobody can remove it to protect you from item 5.

## The hands-on picks

The running half is `notebooks/C2_W01_D01_ex1_hands_on_STUDENT.ipynb`, and its five markers are:

**Answers: 1b 2a 3a 4c 5b**

The executed twin, with every placeholder filled and every check passing, is `C2_W01_D01_ex1_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

Every data pipeline has a boundary where a value arrives as text and must become a number, and the only question is whether the conversion is written down or left to chance. Systems that convert silently produce numbers nobody can trace back to a record. Systems that refuse produce an error somebody fixes in ten seconds.

The interview version of item 7 is the one that separates candidates: given two conflicting outputs from the same operator, what do you look at first? The answer is the types, and the follow-up is where you would put the conversion. Say at the point of use, and say why the record keeps what it was sent.
