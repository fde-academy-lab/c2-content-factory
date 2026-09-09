# Day 1 Kahoot pack

Ungraded. The score is read as a signal of attention and retention, and it counts towards nothing at all.

Seven items, one for each line of the day's quiz plan. Item 1 and item 7 are the traps of the day, and there is no return question, because Day 1 has nothing behind it to return to. Today's two traps are what tomorrow's return question comes back to.

Run it at the close of the session. Read out the reason line after each item, since the reason is the teaching and the score is not.

---

## Q1. Types (trap)

You run `'10' > 9` in a cell. Is the result True, an error, or does it depend?

1. True, because Python reads the digits inside the quotes and compares ten with nine
2. False, because a piece of text always sorts below a number
3. It raises a TypeError, since one side of the comparison is text  <- correct
4. It depends on how many digits the text side holds

**Why:** Python refuses the comparison rather than guessing what you meant by it. Text and a number have no shared order, and the interpreter says so instead of inventing one.

**Pull of each wrong option:**

- Option 1 attracts you because your eye reads `'10'` as the number ten, and the quotes are the easiest character on the line to skip.
- Option 2 attracts you because sorting text against text is a real thing you have seen, and this looks like more of it.
- Option 4 attracts you because "it depends" is the safe answer in a room where nobody wants to be wrong out loud.

**Trap:** The question is dressed as arithmetic and it is really about what the two sides are. Type is decided before size is even considered, which is the same discipline the Mars Climate Orbiter needed at its system boundary.

---

## Q2. The kernel

You wrote three cells and ran them in the order 3, 1, 2. Which error appears, and why?

1. A NameError, because cell 3 used a name nothing had defined yet  <- correct
2. A SyntaxError, because the cells ran out of their written order
3. A KeyError, because the lookup ran before the record was built
4. No error at all, since a notebook sorts its cells before it runs them

**Why:** The kernel knows the order you ran things in and nothing about the order they sit in on screen. Cell 3 asked for a name, and at that moment the workbench was empty, so you got `NameError: name 'records' is not defined`.

**Pull of each wrong option:**

- Option 2 attracts you because running things out of order feels like a rule you broke, and a broken rule sounds like a syntax problem.
- Option 3 attracts you because a KeyError is also a lookup that found nothing, and the two failures feel similar until you read them.
- Option 4 attracts you because the cells are numbered on screen, and numbering implies somebody is enforcing the sequence.

**Trap:** The layout on screen and the history in the kernel are two different things, and only one of them decides what your code sees.

---

## Q3. Loops and accumulators

Your accumulator adds the amount when the status is delivered. KR4201 delivered Rs 2,395, KR4202 delivered Rs 1,360, KR4203 returned Rs 1,440. What does `total` hold?

1. Rs 5,195, because every amount that went past was added
2. Rs 3,755, because the returned order never reached the addition  <- correct
3. Rs 1,360, because the total starts again each pass
4. Rs 2,395, because the total stops updating after the first match

**Why:** Rs 2,395 plus Rs 1,360 is Rs 3,755, and KR4203 never reaches the addition because its status is returned. The condition decides what enters, and the accumulator decides what survives across passes.

**Pull of each wrong option:**

- Option 1 attracts you because Rs 5,195 is the total of all three amounts, which is what you get the moment you stop reading the `if`.
- Option 3 attracts you because it is exactly what happens when `total = 0` sits inside the loop, and that is the mistake you hunted in the mid-session drill.
- Option 4 attracts you because an accumulator that updates once and then holds still is a plausible story if you have never watched one run.

**Trap:** Two lines do two different jobs here, and losing either one still produces a number that looks like an answer. That is the whole reason you check an accumulator against a small case you can add up by hand.

---

## Q4. Types

What do `type('4500')` and `type(4500)` report?

1. Both report int, because the digits in the quotes are what count
2. Both report str, because everything in a cell arrives as text
3. The first reports str and the second reports float, since a bare number is a float
4. The first reports str, because of the quotes, and the second reports int  <- correct

**Why:** The quotes are the whole difference. `'4500'` is four characters that happen to be digits, and `4500` is a number, and `type()` is how you settle the question in one second instead of arguing about it.

**Pull of each wrong option:**

- Option 1 attracts you because the characters are digits and your eye grants them number status without asking.
- Option 2 attracts you because you have met a system where every field arrives as text, which is true of files and not true of a literal you typed.
- Option 3 attracts you because a spreadsheet does turn plain numbers into decimals, and that habit follows you into Python.

**Trap:** This is KR4200 in miniature. Its amount is the text `"4500"`, and one pair of quotes is all that stands between a working comparison and a TypeError.

---

## Q5. Dictionaries

A record has no `discount` key at all. What does `rec.get('discount', 0)` give you?

1. It raises a KeyError, the same way a square bracket lookup would
2. It returns 0, which is the default you stated in the call  <- correct
3. It returns None, because the field is absent
4. It quietly adds a discount field set to 0 and then returns it

**Why:** You stated the default yourself, so the absent field comes back as the value you chose. That choice is yours to defend, and choosing 100 instead of 0 would give you a number that is just as confident and completely wrong.

**Pull of each wrong option:**

- Option 1 attracts you because you met the KeyError first today, and the first failure is the one that sticks to the whole topic.
- Option 3 attracts you because `.get()` does return None when you name no default, so the option is right about a call you did not make.
- Option 4 attracts you because filling in a gap sounds helpful, and a tool that edits your data behind your back is what you would expect from a spreadsheet.

**Trap:** An optional field is absent rather than empty, and the default you supply is a decision you are on the hook for later.

---

## Q6. The kernel

You restart the kernel. What is gone, and what is still there?

1. It erases the notebook file, so you reopen it from the repository
2. It erases the code in the cells, and running all brings the code back
3. It erases nothing, because the values are saved into the notebook whenever you save it
4. It erases every value in memory, and the cell text stays in the file  <- correct

**Why:** A restart clears the workbench and leaves the instructions for rebuilding it. Your code is on disk and your values are not, which is why run all is the recovery move and why a notebook that only works in your kernel is not finished.

**Pull of each wrong option:**

- Option 1 attracts you because restart sounds destructive, and a beginner reasonably fears losing the file itself.
- Option 2 attracts you because run all does put you back where you were, so it is easy to believe it restored the code as well as the values.
- Option 3 attracts you because you saved the file a moment ago, and saving feels like it should have covered everything you could see.

**Trap:** Values live in memory and code lives on disk, and the reason to know which is which is that only one of them survives a restart, a crash or a new machine.

---

## Q7. Lists (trap)

You run `a = [1, 2, 3]`, then `b = a`, then `b.append(9)`. What is `len(a)` now?

1. It is 3, since only b was appended
2. It is 0, because the assignment handed the items over to b
3. It is 4, because a and b are two names for one list  <- correct
4. It is 3 until you print b, and then both catch up to 4

**Why:** `b = a` hands the same list a second name. There is one list on the workbench with two labels on it, so appending through either label changes what both labels show you.

**Pull of each wrong option:**

- Option 1 attracts you because you appended through b and never typed the name a, so a feels untouched.
- Option 2 attracts you because assignment moves a value in plenty of languages you might have used before Python.
- Option 4 attracts you because printing is when you see the change, which makes it easy to believe that printing is when the change happened.

**Trap:** Copying a name is not the same act as copying a list, and the two look identical on the line you typed. This is the one from today that will cost somebody a whole afternoon in Week 2 if it does not land now.

---

## Distractor audit

Run before release. Three rules: the correct answer is never the longest option, correct positions are spread across the four slots, and no option can be dropped on grammar or length alone.

| Item | Key position | Key length | Longest option | Shortest option | Key is longest | Key is shortest |
|---|---|---|---|---|---|---|
| Q1 | 3 | 63 | 82 | 49 | no | no |
| Q2 | 1 | 63 | 69 | 62 | no | no |
| Q3 | 2 | 63 | 64 | 50 | no | no |
| Q4 | 4 | 72 | 82 | 61 | no | no |
| Q5 | 2 | 57 | 64 | 44 | no | no |
| Q6 | 4 | 68 | 86 | 65 | no | no |
| Q7 | 3 | 51 | 58 | 34 | no | no |

Key positions used: slot 1 appears 1 time, slot 2 appears 2 times, slot 3 appears 2 times, slot 4 appears 2 times. No slot carries more than two keys and no slot is skipped.

In every item the key sits second or third longest of the four, so a learner who always picks the longest option and a learner who always picks the shortest one both finish with nothing. Every option in every item is a clause that answers the question and then states a reason for it, so no option gives itself away by being the only one shaped like a real answer, and every one of them is grammatical against its own stem.

Longest question text: 166 characters in Q3. Longest answer text: 86 characters. Check both against the field limits in Kahoot before pasting.
