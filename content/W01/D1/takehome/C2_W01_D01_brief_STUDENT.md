# Day 1 take-home: two buckets and a boundary you can defend

Due at the start of tomorrow's session, where the solution opens and is discussed.

Nothing new is introduced tonight. You take the counter you built alone this afternoon, ask it the question a stakeholder actually asks, which is how the money splits either side of a line, and then you say out loud why you drew the line where you drew it.

---

## Where the work happens

Open the notebook you built today's three unguided questions in, on the same Codespace you opened this morning. Everything tonight is added to the bottom of that notebook. Leave every cell that is already there in place, including the ones that broke on you, and start no new file.

When you are finished, save that same notebook as `takehome_d1.ipynb` in your own repository, with today's cells still in it.

Each new piece of work gets a markdown heading directly above it, carrying the exact name in the table below, in this order. Those headings are how tomorrow's discussion finds its way around your notebook.

| Cell name | What sits under it |
|---|---|
| `Take-home 1: the two buckets` | The code cell that splits the thirty orders at your boundary and prints both sides. |
| `Take-home 2: the boundary defended` | Two sentences of markdown addressed to the person who wants a different boundary. |
| `Take-home 3: the text amount` | Your own account, in markdown, of the record that stopped the loop this morning. |
| `Take-home 4: the optional field` | The code cell that totals the discount field, with the default you chose stated beside it. |
| `Take-home 5: challenges log` | One markdown cell holding every place you got stuck tonight. |

---

## 1. The two buckets

Someone on the Kalpa Retail side wants the thirty orders split in two, so that they can see how much of the money sits above a line and how much sits at or below it. You choose the line.

Pick one boundary from these four, and only these four: Rs 1,000, Rs 1,500, Rs 2,000 or Rs 2,500.

Then write one cell that walks all thirty records once and carries four accumulators, a count and a total for the bucket above your boundary and a count and a total for the bucket at or below it. Print one line that names your boundary and gives both counts and both totals, then write the sentence you would say to the person who asked, naming the group each number came from.

Two rules that decide whether your numbers mean anything. An order whose amount sits exactly on your boundary belongs in the lower bucket, so that every one of the thirty records lands in exactly one of the two buckets. And the amount of one record in this file is text, so the comparison has to be handed a number before it can be made honestly, the same way it was in the guided build.

## 2. The boundary defended

The person who asked wants to move the line. They have one of the other three boundaries in mind and they are not being unreasonable about it.

Write two sentences in markdown, and only two. The first says what your line separates, in the language of the business rather than of the code. The second says what moves if the boundary moves to one of the other three, and why you would still keep yours. A boundary you picked because it looked round is a preference, and a boundary you can hold for two sentences is a decision.

## 3. The text amount

Write your own account of the record that stopped your loop this morning, in markdown, in your own words, in at most six lines. Cover which order it was, what its amount looks like next to the other twenty-nine, the exact message your own kernel printed when the comparison reached it, what you changed to get past it, and one line on what your change quietly assumes about that amount.

Copy the message rather than remembering it. An error you can quote is an error you can search for, and an error you have paraphrased is gone.

## 4. The optional field

Two of the thirty records carry a discount and the rest do not carry the field at all. Total the discount across all thirty records in one cell, reaching the field in the way that survives a record where it is absent, and state the default you chose in the same cell.

Then one line underneath saying what your default asserts about the twenty-eight records that carry no discount. A default is a claim about the file, and you own the claim once you have typed it.

## 5. The challenges log

One markdown cell, with one entry for every place you got stuck tonight, in the order the trouble happened. Each entry carries three things: what you expected to see, the exact error text your own kernel printed, copied character for character off your own screen, and what you changed next.

Between three and six entries is the normal shape of an evening like this. An entry that describes an error in words with no error text in it is not an entry. If your run really did go straight through, restart the kernel, run every cell from the top, and write down what happened when you did.

---

## 6. Go and read the source that wrote your error

Two errors landed on your screen today and somebody wrote the words you read. Both of them live in
the source of Python itself, and tonight you go and find them. Read these two files at the v3.12.0
tag, which pins the line numbers so they stay where this brief says they are:

- `raw.githubusercontent.com/python/cpython/v3.12.0/Objects/object.c` (verified 09 September 2026)
- `raw.githubusercontent.com/python/cpython/v3.12.0/Objects/dictobject.c` (verified 09 September 2026)

Answer both in one markdown cell, and give the line number you found each answer on.

1. In `Objects/object.c`, find the line that builds the message you saw when you compared KR4200's
   amount against your boundary. Give its line number, then say what each of its three placeholders
   held at the moment your own cell failed. Read your own error text to answer that second part,
   because the file cannot tell you.
2. In `Objects/dictobject.c`, find the function behind `.get()`. Give its line number, and copy out
   the one-sentence description of what `.get()` returns that sits a few lines above it. Then say in
   one sentence what that description means for the default you chose in part 4.

A line number you did not open the file to find is usually wrong, and it is the one part of tonight
that somebody marking your work can check in ten seconds.

---

## The watch task

Corey Schafer, Dictionaries: https://www.youtube.com/watch?v=daefaLgNkw0 (verified 09 September 2026)

Watch it before tomorrow. Then add one line to your notebook naming one thing the video does with a dictionary that today's session did not, and say whether you would use it on these records.

## The setup task

There is nothing to install tonight. The Codespace you opened today is the environment for the whole programme, so tomorrow begins by reopening the same one rather than by building anything new. If it refuses to open, or opens without your notebook in it, tell the Support TA before the session starts rather than during it.

---

## What to bring tomorrow, and in what shape

1. The notebook, saved as `takehome_d1.ipynb`, open on your screen at `Take-home 1: the two buckets`, with the cell already run so the output is showing.
2. Your boundary, ready to say in one sentence, with the count and the total on both sides of it.
3. The two defence sentences, in the notebook rather than in your head.
4. The challenges log with real error text in it.
5. The two line numbers from the CPython source, with what you found on each.
6. One question you could not answer alone last night, written down. The ones people carry in their heads are the ones that go unasked.

The solution opens at the start of tomorrow's session, and tomorrow's first cell is the one this day ended on, so the notebook you bring is the notebook tomorrow starts in.

## Before tomorrow

Open `C2_W01_D01_selfcheck_STUDENT.md`. It holds checkpoints you can verify on your own screen, so that you know where you stand before the room does.

Open it after your run and before tomorrow's session, rather than while you are still building. Reading it first turns tonight into a copying exercise, and you will feel that difference tomorrow when the solution opens.
