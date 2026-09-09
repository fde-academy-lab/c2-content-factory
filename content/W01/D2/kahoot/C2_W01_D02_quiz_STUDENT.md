# Day 2 Kahoot pack

Ungraded. The score is read as a performance indicator for attention and retention, never as a marks component.

Eight items. Item 3 is the trap of the day and item 8 is Monday's return question one level up.

Run it at the close of the session. Read out the reason line after each item, since the reason is the teaching and the score is not.

---

## Q1. Functions

A function prints the id and has no return. What is in `result` after `result = fix(record)`?

1. None  <- correct
2. The record that was passed in
3. The text that appeared on the screen
4. An empty dictionary ready to be filled

**Why:** No `return` means the call hands back `None`. The printing happened for you, and the caller got nothing.

---

## Q2. Errors

In a four line traceback ending in ValueError, which line is the one you go and edit?

1. The first line, because it sits at the top
2. Line 12, the one naming your own file  <- correct
3. The last line, because it names the exception
4. Whichever line contains the word error

**Why:** The last line says what went wrong. The line naming your file says where. You edit where.

---

## Q3. Errors (trap)

You wrap `int(value)` in try with a bare except and pass. What does the printed total look like?

1. It raises and the loop stops on the first bad record
2. It prints zero because nothing was added
3. It prints a number that looks fine  <- correct
4. It prints a warning and then the number

**Why:** This is the trap of the day. The total is plausible, the label claims every record, and nothing on screen disagrees.

---

## Q4. Errors

Which exception does `int('twelve')` raise?

1. TypeError
2. SyntaxError
3. KeyError
4. ValueError  <- correct

**Why:** The type is right and the value is wrong, which is what ValueError means. TypeError would mean the wrong type entirely.

---

## Q5. Files

What does `with open(...)` guarantee that opening and closing by hand does not?

1. The file closes even if the code raises  <- correct
2. The file is read entirely into memory first
3. The file cannot be changed by another program while open
4. The file is checked for formatting errors as it opens

**Why:** The guarantee is the close, including on the failure path. Nothing about speed, locking or validation.

---

## Q6. Files

Where does `csv.DictReader` get the keys for each record?

1. From a list you pass in on every read
2. From whatever names your dictionary already uses
3. From the first row of the file  <- correct
4. From the column order in which the file was written

**Why:** The header row is the contract. Change a header spelling and every lookup in your code raises KeyError.

---

## Q7. Files

A vendor's JSON fails at line 47 column 5. What is your first move?

1. Wrap json.load in try and except and carry on
2. Rewrite the closing brackets so the file parses
3. Ask the vendor to resend before looking at the file
4. Open the file at that line and look  <- correct

**Why:** Look first. Repairing someone else's feed by hand produces a file that loads and quietly holds a fraction of the data.

---

## Q8. Return question, Monday one level up

A comparison fails mid loop on record 17 of 30. What are your first two checks?

1. Restart the kernel and run every cell again
2. The type of the value and the record it came from  <- correct
3. Whether the loop variable was renamed further up
4. The record count and whether the file was complete

**Why:** Monday you learned type before size. Today you learned the traceback names the value. Together they point at record 17 and at what it holds.

---

## Distractor audit

Run before release. Two rules: the correct answer is never the longest option, and correct positions are spread across the four slots.

| Item | Key position | Key length | Longest option | Key is longest |
|---|---|---|---|---|
| Q1 | 1 | 4 | 38 | no |
| Q2 | 2 | 37 | 45 | no |
| Q3 | 3 | 34 | 52 | no |
| Q4 | 4 | 10 | 11 | no |
| Q5 | 1 | 39 | 56 | no |
| Q6 | 3 | 30 | 51 | no |
| Q7 | 4 | 35 | 51 | no |
| Q8 | 2 | 49 | 50 | no |

Key positions used: slot 1 appears 2 times, slot 2 appears 2 times, slot 3 appears 2 times, slot 4 appears 2 times.

Longest question text: 96 characters. Longest answer text: 56 characters. Check both against the field limits in Kahoot before pasting.
