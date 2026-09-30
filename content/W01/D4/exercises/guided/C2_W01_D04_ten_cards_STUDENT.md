# Guided: ten cards, the first coded shuffle, and the Retail-Plus line

Built with the trainer during chapter 1, on paper first and then in notebook 1. Keep this sheet; the
table you fill in is the evidence for your first line to Meera.

> **The client asks.** "Retail-Plus is down, smaller than first reported. Real, or the wobble we see
> every quarter?" Meera Raghavan, CEO, Kalpa Retail

## Step 1. The cards, by hand

Ten index cards, **invented for the table**: five members' Q1 spend and five members' Q2 spend.

| Q1 card | Rs | Q2 card | Rs |
|---|---|---|---|
| A | 3,400 | F | 2,200 |
| B | 2,900 | G | 3,100 |
| C | 4,100 | H | 1,900 |
| D | 2,500 | I | 2,700 |
| E | 3,800 | J | 2,400 |

The real gap is the Q1 mean less the Q2 mean: Rs 3,340 less Rs 2,460, which is Rs 880.

Shuffle the ten cards face down, deal five to a "Q1" pile and five to a "Q2" pile, and write the new
gap. Do it ten times.

| Shuffle | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Gap, Rs | | | | | | | | | | |

How many of your ten reached Rs 880 or more? Write it on the board beside your pair's name.

## Step 2. The same deal, as a loop

In notebook 1, section 1, the trainer types `shuffle_gaps` with you line by line. Say what each line
does in card words: `pool` is the ten cards face down, `random.shuffle` is the deal, the two slices are
the two piles, and the gap is the number you wrote in step 1. A thousand shuffles with seed 2026 put
21 gaps at Rs 880 or more.

## Step 3. The usual wobble, then Retail-Plus

The trainer runs Retail-Core in notebook 1, section 3: a gap of Rs 110 per member that about a third
of 5,000 shuffles match. You run Retail-Plus in section 4 and fill in:

| Retail-Plus | Your number |
|---|---|
| Delivered revenue per member, Q1 | |
| Delivered revenue per member, Q2 | |
| The real gap per member | |
| Shuffles at least as large, out of 5,000 | |
| The share | |

## Step 4. The line to Meera

Write it in the form that survives Kavya's review: the share, the world it was counted in, and what it
lets you conclude.

"If nothing had changed between the quarters, a fall of Rs ______ per member or more would turn up in
about ______ of every 100 shuffles, so ___________________________."

Read it to your partner. If your sentence contains the words "chance we are wrong" or "percent
certain", rewrite it before chapter 1 closes.
