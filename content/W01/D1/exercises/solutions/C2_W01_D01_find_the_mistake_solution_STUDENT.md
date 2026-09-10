# Day 1 solution, E3. Find the mistake

## The idea being tested

A crash tells you where it happened. A wrong number tells you nothing, and this drill exists so that the room meets that difference once, in public, on a cell small enough to hold in their heads. Every item is one move in the same diagnosis: predict, locate, repair, prove, and write a check that would have caught it without anybody reading the code.

The number the broken loop prints is Rs 1,460, and the reason it is dangerous is that it is a perfectly plausible number. It has four digits, it sits inside the range of real orders, and it would survive a glance on a slide.

## The answers

**Answers: 1c 2a 3d 4b 5a 6c 7b 8d 9c 10a 11d 12b 13c 14a 15b**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The reset runs on every qualifying record, so only the last delivered order survives, and that is KR4224 at Rs 1,460. | a is the number the loop is meant to produce and never reaches; b ignores the condition entirely; d assumes an unassigned name, when the reset assigns one on the first qualifying record. |
| 2 | a | The starting value has to run once, and it is running thirteen times. | b swaps a working loop for a different one with the same bug; c changes the question rather than fixing the bug; d would add every amount regardless of status, which is a second bug rather than a fix. |
| 3 | d | KR4224 is the last delivered order the loop reaches, and its amount survives because nothing resets after it. | a names the largest amount, which is KR4200 at Rs 4,500 and returned rather than delivered; b names the first delivered order, which was wiped twelve resets ago; c names the discount record, which has nothing to do with this. |
| 4 | b | Above the loop is the only place the loop cannot reach. | a leaves the reset running per record; c produces zero every time, which is item 13; d never runs before the print. |
| 5 | a | A total that exactly equals one record's amount is the signature of a reset inside the loop. | b is true of most totals and proves nothing; c is true here and also true of many correct totals over small groups; d counts digits, which is a coincidence of this file's size. |
| 6 | c | The starting value runs first, then the loop, then the condition inside it, then the addition inside that. | a puts the reset last, so the print sees zero; b runs the reset before the loop and then the condition before the loop exists; d resets inside the loop, which is the bug being repaired. |
| 7 | b | Node D is the reset, and the drawing already resets at A. Removing D leaves the correct loop. | a stops the loop after one order, which fixes nothing and breaks the walk; c skips the addition, so every delivered order is ignored; d prints before anything is counted. |
| 8 | d | The interpreter has no opinion about a number being wrong, so the only person who can catch it is somebody who already knew roughly what to expect. | a and c invent behaviours that do not happen; b is false, since nothing raised, so there is no line number to hide. |
| 9 | c | A group's total cannot be smaller than any single member of the group, and this one is. | a is a coincidence; b would pass on the broken loop, since it does run thirty times; d bans a shape that is correct and common. |
| 10 | a | Rs 25,720 divided by Rs 1,460 is 17.6, so about seventeen times. | b, c and d are the wrong order of magnitude, and the interesting part is that the broken answer is small enough to look like a modest undercount rather than a catastrophe. |
| 11 | d | A status compared with the wrong capitalisation matches nothing, so the total comes back as zero, which is too small and runs cleanly. | a produces a count rather than a total, which is obviously wrong at a glance; b raises `TypeError` on KR4200 rather than running cleanly; c prints thirteen lines rather than one, which anybody notices. |
| 12 | b | The printed number is Rs 1,460 and one record holds exactly that. Finding it takes one search and points straight at the reset. | a works and takes longer than a minute on a real file; c is the right instinct and one step slower than the search; d tells you the number is stable, which it is, and nothing else. |
| 13 | c | The reset now runs after the addition, so the last thing that happens to `total` on every qualifying record is being set to zero. | a is the first variant's answer; b is the correct total, which needs the reset out of the loop entirely; d assumes assignment removes a name, when it replaces a value. |
| 14 | a | A group total is at least its largest member, and both variants violate that. | b passes on the first variant, which prints a positive number; c passes on every variant, since zero is an integer; d checks the file rather than the answer, so it passes while the answer is wrong. |
| 15 | b | A corrections card is three lines: the claim, the correction and the source. | a and c make it about people; d blames the data for a bug in the loop, which is the excuse the decisions log exists to prevent. |

## The part worth arguing about

Item 11. Half the room will pick the missing `int()`, because that is the failure they met an hour earlier, and it is the wrong answer here for a precise reason: it raises rather than running. Getting that wrong out loud is worth more than getting it right silently, because the distinction between a failure that stops and a failure that lies is the whole point of the day.

Item 5 also splits a room. Somebody always argues that a total smaller than the largest single order is the tell, which is item 9's answer and is a weaker signal than an exact match against one record. Both are worth having. The exact match names the bug; the smaller-than-largest catches a wider family and never names anything.

## The hands-on picks

The running half is `notebooks/C2_W01_D01_ex2_hands_on_STUDENT.ipynb`, and its four markers are:

**Answers: 1c 2d 3a 4c**

The executed twin is `C2_W01_D01_ex2_hands_on_solution_STUDENT.ipynb` in this folder, with the broken loop, the repair and the proof on a second condition all showing their outputs.

## Where this pattern lives in production

Every daily business number is an accumulator with a condition, run on a schedule. The three things that break are the three in this drill: the condition selects the wrong records, the accumulator is reset where it should not be, and a value's type changes what the comparison means.

The interview question is item 12's, and it arrives as "a reporting job comes back with a total far smaller than it should be and it does not crash, what do you check first?" Name the accumulator and say why, then name the check from item 14 that would have failed loudly. A candidate who reaches for a debugger is answering a different question from one who reaches for an invariant.
