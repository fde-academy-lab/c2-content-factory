# How often do coin tosses on five members' cards make a gap of Rs 880, and what line goes to Meera on Retail-Plus?

Guided, built with the trainer during chapter 1, on paper first and then in notebook 1,
`notebooks/C2_W01_D04_01_real_or_wobble_STUDENT.ipynb`. Keep this sheet: the table you fill in is the
evidence for your first line to Meera.

> **The client asks.** "Retail-Plus is down, smaller than first reported. Real, or the wobble we see
> every quarter?" Meera Raghavan, CEO, Kalpa Retail

Retail-Plus is Kalpa Retail's paid membership tier, and the same 22 members bought in both Q1 and
Q2. Their delivered revenue per member, the money Kalpa kept once cancelled and returned orders are
left out, fell between the quarters. Every quarter's numbers wobble a little by chance, so the question
is how often chance alone would make a fall that large. The flip test answers it: for each member, a
coin decides which of their two quarters counts as Q1, the gap is worked out again, and this is
repeated many times. The share of those chance-only worlds that reach the real gap is what the line
to Meera reports. Kavya Nair, the senior analyst on the team, reviews every line before it reaches
Meera.

**Who needs the answer.** Meera decides at Monday's growth review whether the Retail-Plus fall gets a
budget of its own. A wobble read as a real fall funds a fix for nothing, and a line that reads the
share as a certainty sends her into the review sure of something the data never said.

**The questions on the way.**

- How often do ten tosses of five coins reach the real gap of Rs 880?
- What does the loop in notebook 1 do with each member's two cards?
- What does the usual wobble look like on Retail-Core, and where does Retail-Plus fall?
- Which line about Retail-Plus survives Kavya's review?

## Step 1. How often do ten tosses of five coins reach the real gap of Rs 880?

Ten index cards, **invented for the table**: five members, each with a Q1 card and a Q2 card. The
same members sit in both quarters, as Kalpa's Retail-Plus members do, so each member's two cards stay
together.

| Member | Q1 card, Rs | Q2 card, Rs | Q1 less Q2, Rs |
|---|---|---|---|
| A | 3,400 | 2,400 | 1,000 |
| B | 2,900 | 2,200 | 700 |
| C | 4,100 | 3,100 | 1,000 |
| D | 2,500 | 1,900 | 600 |
| E | 3,800 | 2,700 | 1,100 |

The real gap is the Q1 mean less the Q2 mean: Rs 3,340 less Rs 2,460, which is Rs 880.

If the quarter made no difference, each member's two cards could have come in either order. Toss a
coin for each member: heads keeps the pair as written, and tails swaps the two cards, which turns that
member's difference negative. Add the five signed differences, divide by five, and write the gap. Do
it ten times.

| Toss of five coins | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Gap, Rs | | | | | | | | | | |

How many of your ten reached Rs 880 or more? Write it on the board beside your pair's name.

## Step 2. What does the loop in notebook 1 do with each member's two cards?

In notebook 1, in the section that asks how often coin tosses on five members' cards make a gap of
Rs 880, the trainer reads `flip_gaps` from the setup cell with you line by line. Say what each line
does in card words: `diffs` is each member's Q1 less Q2, the coin is `random.random() < 0.5`, a tails
turns a member's difference negative, and the mean of the five is the number you wrote in step 1. A
thousand tosses with seed 2026 put 35 gaps at Rs 880 or more, and 64 at Rs 880 or more in either
direction. Five coins can land 32 ways, and only the way that keeps every pair as recorded reaches
Rs 880, so the exact share is 1 in 32. Ten tosses are far too few to measure a share that small, which
is why the loop runs thousands.

## Step 3. What does the usual wobble look like on Retail-Core, and where does Retail-Plus fall?

The trainer runs Retail-Core, Kalpa's other consumer tier, in notebook 1's section on the usual
wobble: a fall of Rs 110 per member that about a third of 5,000 flips match, and about seven in ten
match counting a move that large either way. You run Retail-Plus in the next section, which asks how
often chance alone makes a fall as large as Retail-Plus's, and fill in:

| Retail-Plus | Your number |
|---|---|
| Delivered revenue per member, Q1 | |
| Delivered revenue per member, Q2 | |
| The real gap per member | |
| Flips with a fall at least as large, out of 5,000 | |
| Flips with a move that large either way, out of 5,000 | |
| The two shares | |

## Step 4. Which line about Retail-Plus survives Kavya's review?

Write it in the form that survives Kavya's review: both shares, the world they were counted in, and
what they let you conclude. Meera's question came after the fall was seen, so neither direction was
chosen in advance and both go in the line.

"If nothing had changed between the quarters, a fall of Rs ______ per member or more would turn up in
about ______ of every 100 flips, and a move that large either way in about ______, so
___________________________."

Read it to your partner. If your sentence contains the words "chance we are wrong" or "percent
certain", rewrite it before chapter 1 closes.
