# Self-check before you hand in Thursday's take-home

Ten checks.

## The note

1. Count your sentences. Five. If you have seven, two of them are saying the same thing and you
   have not decided which.

2. Read sentence four. Is it about audit, ownership or readership? If the words "faster",
   "slower", "can handle" or "scales" appear, it is the wrong kind of objection.

3. Read sentence five. Does it name a concrete situation, or does it hedge? "Unless the situation
   requires it" is a hedge. "Unless the number is a one-off nobody will re-run" is a case.

4. Would sentences one to three survive somebody asking "why not the other two" for each? Try it
   out loud on sentence two.

5. Is there a tool you named twice for different jobs? That is a good sign, and worth saying
   explicitly rather than leaving the reader to notice.

## The column

6. Read your "what it is" line to somebody who has not seen the table. Do they understand what the
   number means without seeing the code? If not, the column name is doing work the line should.

7. Your "why they want it" line names a decision. Which decision, made by whom? If the answer is
   "it would be interesting", the column has not earned its place.

8. The cost line: every derived column assumes something or hides something. If yours genuinely
   does neither, you have probably renamed an existing column.

9. Refresh safety. Rebuild the table with `AS_OF` moved forward by one week and diff your column.
   Did it change for customers whose orders did not? If yes, say so in the line rather than fixing
   it silently, because that may be the correct behaviour.

10. Run every merge in your build with `validate=` set. All of them, not the ones you think are
    safe. If any raises, you have found something about the data worth reporting, which is a
    better hand-in than a column that merged quietly.
