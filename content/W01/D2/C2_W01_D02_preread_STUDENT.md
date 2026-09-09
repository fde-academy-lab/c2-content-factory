# Pre-read for tomorrow, and tonight's setup

Ships tonight. Fifteen minutes of reading. Do the gap sheet before you sleep and tomorrow's first hour will feel like revision.

---

## Tonight's setup

Nothing to install. The Codespace you opened on Monday stays the environment for the whole programme.

Three things to have ready before tomorrow starts:

1. Your `output` folder from today, holding your clean file and your rejects file. Tomorrow starts from it.
2. Your two functions, `normalise_amount` and `clean_records`, in a cell you can find quickly. You will be asked for them by name and you will call them without editing them.
3. Your take-home notebook, finished. Tomorrow opens by walking one.

If your notebook does not run cold from top to bottom, fix that tonight rather than tomorrow. Restart the kernel and run all. Anything that fails now will fail in front of the room later.

---

## Tomorrow in one sentence

Today you cleaned one record at a time and you knew which records were bad because somebody planted them. Tomorrow you get a dataset nobody prepared, and the first question is how many usable records it actually has.

---

## The vocabulary, as a gap sheet

Fill these in from the words below. Guessing is the exercise. Being wrong tonight is free.

**Word bank:** profiling, identity rule, decisions log, keep and flag, convertibility, outlier, reconcile, distinct count

1. Looking at a dataset field by field before changing anything, counting what is present, what converts and how many different values there are, is called ______________.

2. The count of how many values in a field can actually become the type you need is that field's ______________.

3. The number of different values a field holds, which tells you whether a field is a category or a free text box, is its ______________.

4. When a value is missing you have three choices: drop the record, use a stated default, or ____________________ so the gap travels with the data.

5. Two records share an id and disagree on one field. Deciding which of them counts as the same record is an ____________________, and it has to be written down.

6. A value far outside the range of everything else is an ______________, and it is a finding to investigate before it is a row to delete.

7. The written record of every cleaning decision and its reason, so a reviewer can follow what you did, is the ____________________.

8. Checking that input equals clean plus rejected is how you ______________ your counts, and you did the first version of this today.

---

## Two questions to arrive with

Bring an answer to each. They are the first two things tomorrow asks.

1. Your run today reported zero rejects on a file you know is dirty. Name the two most likely causes.

2. Two records share an id and disagree on one field. What do you do, and who decides?

The second one has no correct answer from your side of the table. That is what makes it worth asking.

---

## Optional reading

The chapter on reading and writing files from the book on today's reference list, if you did not get to it for the take-home.

Link status: to be found. The reference is `Automate the Boring Stuff with Python`, 3rd edition, chapter 10. The verified link goes on this line before this pack is released.
