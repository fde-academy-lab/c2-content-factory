# Is a region's 5 percent drop the same story as Kalpa's, and does the members' win-back offer go to it by Friday?

> "Our region is down about 5 percent quarter on quarter. Same story as the national numbers, I
> assume: customers buying less often. We would like the Retail-Plus win-back offer extended to our
> region by Friday."
>
> The regional operations head, Kalpa Retail

> "Before I say yes to anything, tell me whether this region is the same story or a different one.
> One page. I will read the first line and the numbers, and Anand will check every number against
> the file."
>
> Meera Raghavan, CEO, Kalpa Retail

A second export has arrived from Kalpa's regional operations team, cut from their own dashboard, with
the first message above attached, and Meera has forwarded it to you with the second. The win-back
offer is a discount aimed at members of Retail-Plus, Kalpa's paid membership tier, who have started
to order less. Anand Iyer is Kalpa's finance controller. Revenue is booked revenue, every order
placed at the price charged before any cancellation or return, and Monday's revenue tree splits it
into customers x orders per customer x revenue per order. The ladder is the day's investigation,
climbed one rung at a time, each rung a question settled before the next is asked.

**Who needs the answer.** Meera Raghavan, the CEO, decides whether the win-back offer goes to the
region by Friday, and Anand Iyer, the finance controller, checks every number in your memo against
the file. A wrong call either spends the offer's margin where it cannot work or holds back an offer
the region needs, and a number Anand cannot find in a cell sends the memo back.

**The questions on the way.**

- What does the day's ladder find on a second sample nobody has explained?
- What does the one-page memo tell Meera, and in what order?
- How does your ladder compare with a published walkthrough of a sales drop?

The take-home has three parts and takes about two and a half hours in all. Part 1 is the day's
ladder on a file you have not seen. Part 2 is the memo, one page, and it is the part Meera reads.
Part 3 is reading and watching, with one change to make if the reading changes your mind. Tomorrow
opens by walking one learner's memo in front of the room.

---

## Part 1. What does the day's ladder find on a second sample nobody has explained?

This takes about ninety minutes, and at work it runs on every new export before any figure from it
is quoted.

The file sits in `data/C2_W01_D02_takehome_STUDENT.py`. It has the same fields as the class file and
none of the same numbers, so nothing from today's notebooks can be pasted across.

1. Start a new notebook beside the day's notebooks. Copy in the setup cell from chapter 3's notebook,
   `notebooks/C2_W01_D02_03_which_segment_STUDENT.ipynb`, and load the file with
   `kit.load_records("C2_W01_D02_takehome_STUDENT.py")`.
2. On the first rung, confirm the drop is real. Print the first and last order date of each quarter
   before you compute any change, and write in a markdown cell which comparison you chose and why.
3. On the second rung, build the tree for each quarter with your own `tree_for`, the function you
   wrote in chapter 3 that gives any list of orders its revenue, orders, customers and rates, and
   check it on the whole quarter before you trust it on any segment.
4. On the third rung, run `tree_for` on each of the four segments in each quarter. Count the segments
   in and the rows out. Where a branch moved, compare the sets of customer ids as well as the counts.
5. Describe the typical order and the spread of any segment you name in the memo, with its median,
   the middle order once the orders are sorted, and its range, the largest order less the smallest.
6. Count the orders that do not carry a discount field in each quarter, and write the default you
   chose for them and why, in one sentence.

Run the notebook from a fresh kernel, top to bottom, before you call it done. The self-check file,
`takehome/C2_W01_D02_selfcheck_STUDENT.md`, tells you whether each number is right.

---

## Part 2. What does the one-page memo tell Meera, and in what order?

This takes about forty minutes, and at work it comes up whenever a finding goes to a leader who reads
only the first line.

Write it as a markdown cell at the end of your notebook, or as a page beside it. It has five parts,
in this order:

1. The first line says whether this region is the same story as the national numbers, with the window
   and the definition in the same sentence. Meera reads nothing else if this line is weak.
2. The branch line says which branch of the tree moved, with the numbers from your notebook for both
   quarters on a matched comparison.
3. The segment line says which segment carries it, with its numbers, and gives one line on the
   segments that did not move.
4. The hypotheses line names two causes that could explain what you found, each stated as a
   hypothesis.
5. The evidence line gives, for each hypothesis, the data that would settle it, and says whether this
   file carries it or someone has to be asked for it.

Then write one final line: your answer to the regional operations head's request for Friday, as one
of these three, with the number from your notebook that decides it.

- Extend the win-back offer to the region, because the branch it acts on is the one that moved.
- Hold the offer and send a different recommendation, because a different branch moved.
- Hold every decision until a matched comparison exists, because the drop is not yet confirmed.

The choice must follow from your own numbers. A memo that picks one and cannot point at the number
behind it has not answered the question.

---

## Part 3. How does your ladder compare with a published walkthrough of a sales drop?

This takes about twenty minutes, and at work it comes up whenever you set your own method beside
someone else's.

Brit Institute, data analyst case study questions, including "Sales dropped last month. How would you investigate?": https://britinstitute.uk/blog/data-analyst-case-study-interview-questions (verified 29 Sep 2026)

Corey Schafer, "Python Tutorial for Beginners 8: Functions": https://www.youtube.com/watch?v=9Os0o3wzS_I (verified 29 Sep 2026)

Read the sales-drop walkthrough. Name, in one line under your memo, one step it takes that your
ladder did not, or one step your ladder took that it skipped. If the reading changes your mind,
rewrite your memo's first line and keep the old one beneath it, struck through.

Watch the functions video, and then check that every function in your notebook returns its answer.

---

## What stops a pasted answer from passing?

The memo's numbers come from a file no assistant has seen, and Anand checks each one against it. The
final line is a choice that only your own computed values can decide, and the three options are
written so that each is right for some file. Part 3 asks for a comparison between a named reading and
your own ladder, which only you ran.

---

## What do you bring tomorrow?

| Part | What to bring |
|---|---|
| 1 | Bring the notebook, run from a fresh kernel, with the dates, the trees, the segment split and the discount default. |
| 2 | Bring the memo, its five parts and the final line, with every number traceable to a cell. |
| 3 | Bring your one line on the walkthrough, and the old first line if you rewrote it. |
