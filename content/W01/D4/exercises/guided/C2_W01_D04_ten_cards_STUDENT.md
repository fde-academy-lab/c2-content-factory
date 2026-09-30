# Guided: ten cards, the first coded flip, and the Retail-Plus line

Built with the trainer during chapter 1, on paper first and then in notebook 1. Keep this sheet; the
table you fill in is the evidence for your first line to Meera.

> **The client asks.** "Retail-Plus is down, smaller than first reported. Real, or the wobble we see
> every quarter?" Meera Raghavan, CEO, Kalpa Retail

## Step 1. Five members, two cards each, by hand

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
coin for each member: heads keeps the pair as written, tails swaps the two cards, which turns that
member's difference negative. Add the five signed differences, divide by five, and write the gap. Do
it ten times.

| Toss of five coins | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Gap, Rs | | | | | | | | | | |

How many of your ten reached Rs 880 or more? Write it on the board beside your pair's name.

## Step 2. The same toss, as a loop

In notebook 1, section 1, the trainer reads `flip_gaps` from the setup cell with you line by line. Say
what each line does in card words: `diffs` is each member's Q1 less Q2, the coin is
`random.random() < 0.5`, a tails turns a member's difference negative, and the mean of the five is
the number you wrote in step 1. A thousand tosses with seed 2026 put 35 gaps at Rs 880 or more, and
64 at Rs 880 or more in either direction. Five coins can land 32 ways, and only the way that keeps
every pair as recorded reaches Rs 880, so the exact share is 1 in 32.

## Step 3. The usual wobble, then Retail-Plus

The trainer runs Retail-Core in notebook 1, section 2: a fall of Rs 110 per member that about a third
of 5,000 flips match, and about seven in ten match counting a move that large either way. You run
Retail-Plus in section 3 and fill in:

| Retail-Plus | Your number |
|---|---|
| Delivered revenue per member, Q1 | |
| Delivered revenue per member, Q2 | |
| The real gap per member | |
| Flips with a fall at least as large, out of 5,000 | |
| Flips with a move that large either way, out of 5,000 | |
| The two shares | |

## Step 4. The line to Meera

Write it in the form that survives Kavya's review: both shares, the world they were counted in, and
what they let you conclude. Meera's question came after the fall was seen, so neither direction was
chosen in advance and both go in the line.

"If nothing had changed between the quarters, a fall of Rs ______ per member or more would turn up in
about ______ of every 100 flips, and a move that large either way in about ______, so
___________________________."

Read it to your partner. If your sentence contains the words "chance we are wrong" or "percent
certain", rewrite it before chapter 1 closes.
