# Extras: one to stretch, one to recover

---

## Stretch: how small a difference could you have caught?

You finished early and the shuffle felt straightforward. Then this, and it is the question a good
interviewer asks next.

**The situation.** You told Meera that Retail-Plus is real and Student is not. She asks the obvious
follow-up:

> "Fine. If Student had actually moved, how big would the move have had to be before your method
> would have noticed?"

**What to build.** Take the Student data, twelve orders. For each possible split from 6 and 6 up to
0 and 12, compute the rise and run the same chance test. Build one table:

| Q1 orders | Q2 orders | The rise | p-value | Would you report it? |
|---|---|---|---|---|

Then answer three questions in writing.

1. At what split does the p-value first drop below 0.05, and what rise does that correspond to?
2. What does that tell you about what twelve observations can and cannot detect?
3. If Meera insists on a Student answer this quarter, what is the smallest honest thing you can tell
   her?

**The hard part, and the point.** The answer to question one is a surprisingly large rise. That
number is the **smallest effect your method could have caught**, and knowing it turns "not
significant" from an excuse into a measurement. Any interviewer who asks "how would you know if you
were wrong" is asking for this.

---

## Recovery: ten cards, on your own table

The shuffle went past you and the code made it worse. Then do it with cards tonight, alone, and skip
the code entirely.

**You need ten playing cards and ten minutes.**

1. Write `A` on six cards and `B` on four. These are two groups.
2. Write a number on the back of each card: any ten numbers between 1 and 20. Do not think about it.
3. Deal by the letters. Compute the average of the `A` backs and the average of the `B` backs.
   Write the difference down and circle it. **That is your real gap.**
4. Now turn every card face down, shuffle the whole pack, and deal six and four **ignoring the
   letters**. Compute the two averages and the difference. Write it in a list.
5. Do step 4 nine more times, so you have ten differences.
6. Count how many of your ten are at least as big as the circled one, ignoring the sign.

```
that count, over ten
```

That is a p-value. You have now computed one by hand.

**What you should end up believing.** The shuffle does not know anything about your data. It builds
worlds where the labels mean nothing and asks how often those worlds look like yours. If they often
do, your labels might mean nothing either.

**Then do one thing more.** Go back to step 2 and, instead of any ten numbers, write 15 to 20 on the
`A` cards and 1 to 6 on the `B` cards. Repeat the whole exercise. Your count out of ten will be zero
or one, and you will have felt the difference between a real effect and noise without a formula
anywhere near it.
