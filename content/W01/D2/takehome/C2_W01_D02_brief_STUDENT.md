# Take-home: the investigation memo

Three parts, about two and a half hours in all. Part 1 is the day's ladder on a file you have not
seen. Part 2 is the memo, one page, and it is the part Meera reads. Part 3 is reading and watching,
with one change to make if the reading changes your mind.

Tomorrow opens by walking one learner's memo in front of the room.

---

## The ask

A second export has arrived from Kalpa's regional operations team, cut from their own dashboard,
with a message attached:

> "Our region is down about 5 percent quarter on quarter. Same story as the national numbers, I
> assume: customers buying less often. We would like the Retail-Plus win-back offer extended to our
> region by Friday." (the regional operations head)

Meera forwards it to you with one line:

> "Before I say yes to anything, tell me whether this region is the same story or a different one.
> One page. I will read the first line and the numbers, and Anand will check every number against
> the file." (Meera Raghavan)

---

## Part 1. The ladder on a second sample, about ninety minutes

The file sits in `data/C2_W01_D02_takehome_STUDENT.py`. It has the same fields as the class file and
none of the same numbers, so nothing from today's notebooks can be pasted across.

1. Start a new notebook beside the day's notebooks. Copy in the setup cell from notebook 3 and load
   the file with `kit.load_records("C2_W01_D02_takehome_STUDENT.py")`.
2. Rung 1: confirm the drop is real. Print the first and last order date of each quarter before you
   compute any change, and write in a markdown cell which comparison you chose and why.
3. Rung 2: build the tree for each quarter with your own `tree_for`, and check it on the whole
   quarter before you trust it on any segment.
4. Rung 3: run `tree_for` on each of the four segments in each quarter. Count the segments in and the
   rows out. Where a branch moved, compare the sets of customer ids as well as the counts.
5. Describe the typical order and the spread of any segment you name in the memo.
6. Count the orders that do not carry a discount field in each quarter, and write the default you
   chose for them and why, in one sentence.

Run the notebook from a fresh kernel, top to bottom, before you call it done. The self-check file
tells you whether each number is right.

---

## Part 2. The memo, one page, about forty minutes

Write it as a markdown cell at the end of your notebook, or as a page beside it. It has five parts,
in this order:

1. **The first line.** Whether this region is the same story as the national numbers, with the
   window and the definition in the same sentence. Meera reads nothing else if this line is weak.
2. **The branch.** Which branch of the tree moved, with the numbers from your notebook for both
   quarters on a matched comparison.
3. **The segment.** Which segment carries it, with its numbers, and one line on the segments that
   did not move.
4. **Two hypotheses.** Two causes that could explain what you found, each stated as a hypothesis.
5. **The evidence.** For each hypothesis, the data that would settle it, and whether this file
   carries it or someone has to be asked for it.

Then one final line: your answer to the regional operations head's request for Friday, as one of
these three, with the number from your notebook that decides it:

- extend the win-back offer to the region, because the branch it acts on is the one that moved;
- hold the offer and send a different recommendation, because a different branch moved;
- hold every decision until a matched comparison exists, because the drop is not yet confirmed.

The choice must follow from your own numbers. A memo that picks one and cannot point at the number
behind it has not answered the question.

---

## Part 3. Read and watch, about twenty minutes

Brit Institute, data analyst case study questions, including "Sales dropped last month. How would you investigate?": https://britinstitute.uk/blog/data-analyst-case-study-interview-questions (verified 29 Sep 2026)

Corey Schafer, "Python Tutorial for Beginners 8: Functions": https://www.youtube.com/watch?v=9Os0o3wzS_I (verified 29 Sep 2026)

Read the sales-drop walkthrough. Name, in one line under your memo, one step it takes that your
ladder did not, or one step your ladder took that it skipped. If the reading changes your mind,
rewrite your memo's first line and keep the old one beneath it, struck through.

Watch the functions video, and then check that every function in your notebook returns its answer.

---

## What makes this hard to shortcut

The memo's numbers come from a file no assistant has seen, and Anand checks each one against it. The
final line is a choice that only your own computed values can decide, and the three options are
written so that each is right for some file. Part 3 asks for a comparison between a named reading and
your own ladder, which only you ran.

---

## What to bring tomorrow

| Part | What to bring |
|---|---|
| 1 | The notebook, run from a fresh kernel, with the dates, the trees, the segment split and the discount default |
| 2 | The memo: five parts and the final line, each number traceable to a cell |
| 3 | Your one line on the walkthrough, and the old first line if you rewrote it |
