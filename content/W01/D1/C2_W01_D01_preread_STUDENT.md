# Pre-read for tomorrow, and tonight's setup

Ships tonight. About fifteen minutes of work. Do the gap sheet before you sleep and tomorrow's first
hour will feel like ground you have already walked.

---

## Tomorrow in one sentence

Today you wrote the same four lines over and over in loose cells, on records that were sitting in the
kernel where you could read them. Tomorrow those lines get a name you can call again, the failures
get caught by name instead of stopping the notebook, and the records leave the cell and become a file
that has forgotten every type it ever knew.

---

## The vocabulary, as a gap sheet

Twelve words you will hear tomorrow. Write the meaning yourself in one line, in your own words, and
guess when you are unsure, because a wrong guess tonight is free and it is what makes the right
answer stick when you hear it. The answers are at the bottom of this file.

**1. `def`**
Write what the word `def` puts on the bench that a loose cell of code does not.
Your line: ______________________________________________________________

**2. A parameter**
Write what the names inside the brackets of a `def` line promise to whoever calls it.
Your line: ______________________________________________________________

**3. `return` against `print`**
Write who each of those two is talking to, and what the caller receives from each.
Your line: ______________________________________________________________

**4. Scope**
Write which values a function can see while it runs.
Your line: ______________________________________________________________

**5. A traceback**
Write what those several lines of red text are a record of, and which end you read first.
Your line: ______________________________________________________________

**6. `try` and `except`**
Write what those two words let a program do when a line fails.
Your line: ______________________________________________________________

**7. `raise`**
Write why you would stop your own program on purpose when nothing has crashed yet.
Your line: ______________________________________________________________

**8. The rejects log**
Write what you do with a record you cannot use, so that somebody who was not in the room can follow
it later.
Your line: ______________________________________________________________

**9. `with open(...)`**
Write what the `with` guarantees about a file you have opened.
Your line: ______________________________________________________________

**10. `csv.DictReader`**
Write what it hands you for each row of a CSV, and where the field names come from.
Your line: ______________________________________________________________

**11. `json.load`**
Write what it turns a JSON file into, and what happens when the file is damaged half way down.
Your line: ______________________________________________________________

**12. A file format as an agreement**
Write what a file format actually promises the person who reads the file.
Your line: ______________________________________________________________

---

## Tonight's setup

There is nothing to install. The Codespace you opened today is the environment for the whole
programme, so tomorrow begins by reopening the same one rather than by building anything new.

Three checks tonight, so that tomorrow does not begin with a broken environment.

1. Close the Codespace and reopen it from the repository, and wait for the editor to finish loading
   with your notebook still in the explorer on the left. A Codespace that refuses to reopen is a
   problem the Support TA can fix tonight and cannot fix in the middle of a session.
2. Restart the kernel and run every cell from the top of your notebook, in order, without touching
   anything in between. It has to run cold from top to bottom on a clean bench. Anything that fails
   now will fail in front of the room tomorrow, and the deliberate breaks you kept from today should
   be the only messages you see.
3. Save the notebook with your take-home cells in it, all five headings present, and the output of
   each code cell showing under the cell that produced it. Reopen the saved file once and read it, so
   you know what is actually on disk rather than what was on your screen.

---

## The watch task

Corey Schafer, Dictionaries, video: link to be found.

Watch it before tomorrow. Then write one line naming something the video does with a dictionary that
today's session did not, and say whether you would use it on these thirty orders.

---

## Answers to the gap sheet

Read these only after you have written something on every line above.

1. `def` gives a block of code a name and a home, so you can run it again later by saying that name.
2. The names inside the brackets are the values the function is promising to work with, and the
   caller supplies them at the moment of the call.
3. `print` shows something to the human at the screen, and `return` hands a value back to the line of
   code that made the call, so a function that only prints hands its caller nothing.
4. A function sees the values that were handed to it, which is as far as scope needs to go this week.
5. A traceback is the record of where the interpreter stopped and how it got there, and you read it
   from the bottom, because the bottom line names the failure and the value behind it.
6. They let you attempt a line, name the failure you expected, and decide what happens next instead
   of letting the whole run stop.
7. You raise when a value has converted cleanly and is still unacceptable to the business, so you
   stop the run yourself and say why in the message.
8. You set the record aside with the reason it was rejected, so the count of what you kept and the
   count of what you dropped both have an explanation attached.
9. The `with` guarantees the file is closed when the block ends, including when your own code fails
   inside it.
10. It hands you one dictionary per row, and the field names come from the header row of the file.
11. It turns the whole file into Python lists and dictionaries in one go, and a file that is damaged
    anywhere fails to load at all rather than loading the good part.
12. A file format promises the reader a structure and nothing else, so a CSV promises rows, commas
    and a header row, and it promises nothing whatsoever about types.
