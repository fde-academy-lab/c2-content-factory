# Which answers hold in the guided set on three counts over twelve carts, and why?

Answers: 1c 2b 3d

The guided set counted two pairs on twelve real Instamart carts by hand. Bread and milk read support
0.33, confidence from bread to milk 1.00 and lift 1.50, because all four bread carts held milk while
milk sat in 8 of the 12 carts anyway. Chips and cold drink read lift 2.67. Ice cream and chocolate
sauce shared a single cart, which makes a lift of 12 with nothing under it.

**Who needs the answer.** You, to check your three letters after the guided build. The category
manager acts on whichever count the team reads, so the reading has to be right before any code runs.

**The questions on the way.**

- What does the set test?
- Why is each key right, and each other letter wrong?
- Which item is worth arguing about?
- Where does the pattern live at work?

## What does the set test?

It tests whether the three counts stay separate: how often (support), how reliably from one side
(confidence), and against chance (lift). The first item is fully worked, the second half worked and
the third left to you, so the help fades as the set climbs.

## Why is each key right, and each other letter wrong?

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| Q1, bread and milk's three numbers | c | Support 4 of 12 is 0.33; confidence bread to milk 4 of 4 is 1.00; lift 4 / 2.67 is 1.50 | a gives 0.50, the confidence from milk to bread, 4 of 8; b gives milk's share, 0.67, as support and a lift of 1.00; d divides expected by seen, 2.67 / 4 = 0.67, upside down |
| Q2, chips and cold drink's lift | b | Seen 2, expected 0.75, so lift is 2.67, a statement about turning up together | a is the confidence from chips, 2 of 3; c has the right number and a causal claim no count can make; d is the support, 2 of 12 |
| Q3, a lift of 12 on one cart | d | One cart cannot tell a real pull from luck, so the call waits for the full count | a acts on a number with one cart under it; b calls a small count an error, when it is only thin; c invents a time band the twelve carts never showed |

## Which item is worth arguing about?

Q2's option c. It carries the right number, 2.67, and the wrong sentence: "chips make a shopper 2.67
times as likely to buy a cold drink". Lift says the two turn up together more than chance would put
them there. Whether promoting chips sells a single extra cold drink needs a test that changes the
strip and watches what follows, which Monday's faculty session on A/B testing (tentative) takes up.

## Where does the pattern live at work?

Every "frequently bought together" strip, every bundle a category team proposes and every
recommendation an e-commerce company ships starts from these three counts. Amazon's recommender team
wrote that counting how often buyers of A also bought B would have made a bestseller the top
suggestion beside everything, and that the fix compared what was seen with what chance predicts
(Amazon Science, checked 12 October 2026).
