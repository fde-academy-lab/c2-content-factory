# Tiered extras: Day 1

Two optional tasks. Take the one that matches where you actually are, rather than the one that sounds better.

Both of them work the same thirty Kalpa Retail orders you have had open all day, and both of them stay inside what you already know. There is no function here, no file and no import, because all three of those arrive tomorrow.

---

## Recovery: if the loop never quite ran

Plenty of people finish Day 1 with a loop that will not turn. Work through these five steps in order, run each one before you write the next, and stop when you are moving again. Each step adds one line to the step before it.

**Step 1. Prove the bench is loaded.**

```
print(len(records))
```

You should see `30`.

If you see `NameError: name 'records' is not defined` instead, the setup cell has not run on this kernel. Scroll to the top, run the setup cell, then run this one again. That is the whole fix and it is worth doing once deliberately so that the error stops being frightening.

**Step 2. Prove you can hold one card.**

```
print(records[0])
print(records[0]["status"])
```

The first line prints the whole first record. The second line prints `returned`, because that is the status field of KR4200.

If the second line raises a `KeyError`, you have misspelled the field name. Copy it out of the record the first line printed rather than typing it from memory.

**Step 3. Prove the loop turns.**

```
for r in records:
    print(r["order_id"])
```

You should see thirty lines, starting at KR4200 and ending at KR4229.

If nothing prints, the `print` line is not indented under the `for` line. If exactly one line prints, the `print` is sitting outside the loop, below it. The indentation is the loop, so look at the whitespace before you look at anything else.

**Step 4. Prove the condition splits the stack.**

```
for r in records:
    if r["status"] == "cancelled":
        print(r["order_id"])
```

Ten ids should print. The `if` line is indented once so that it sits inside the loop, and the `print` line is indented twice so that it sits inside the `if`.

If all thirty ids print, the `print` is indented once instead of twice, so it is running for every card rather than only for the cards that passed.

**Step 5. Now produce the count yourself.**

Same loop as step 4. Take the `print` out from inside the `if`, put a counter above the loop, add one to it where the `print` used to be, and print the counter once at the end. Write those four lines yourself without looking back at the deck, because this is the shape the whole day rests on.

You should see `10`, and you should be able to say the answer as a sentence: ten of the thirty orders were cancelled.

If step 4 worked and step 5 did not, the difference is almost always one of two things. Either the `count = 0` line has slipped inside the loop, so the counter goes back to zero on every card and the number at the end is about the last card alone, or the `count = count + 1` line is indented once instead of twice, so every one of the thirty cards adds one and you get 30 no matter what the condition says.

---

## Stretch: if you finished the three questions with time to spare

Do not go looking for functions or files. Go deeper into what you already have. Both of these tasks are a loop, a condition and an accumulator, which is everything you learned today and nothing more.

**The three bands.**

Someone at Kalpa Retail wants the thirty orders split into three size bands rather than counted against one threshold: the orders above Rs 2,500, the orders above Rs 1,500 up to and including Rs 2,500, and the orders at or below Rs 1,500.

Write one cell that walks the records once and produces a count and a total for all three bands. One loop, one `if` and `elif` and `else` chain, six accumulators. Walking the records three times with three separate loops also works, and it is the wrong shape for a question that will grow to eight bands next month.

Then check yourself without being told the answer. Your three counts have to add up to 30, and your three totals have to add up to Rs 58,210, which is the total of every amount in the file. If either sum is short, one band's boundary is wrong and a record is falling through all three branches. If either sum is over, two branches are catching the same record, which means you wrote three separate `if` statements where the chain needed `elif`.

Then answer this in a markdown cell. The middle band is defined as above Rs 1,500 and up to Rs 2,500. Write the two comparisons you used for it, and say what happens to an order of exactly Rs 2,500 and to an order of exactly Rs 1,500 under the code you actually wrote. Both of those orders have to land in exactly one band and you have to be able to say which.

**The biggest order.**

You have counted and you have totalled. Now find the single largest amount in the file, and the order id it belongs to, with a loop.

The shape is the accumulator again with one change. Instead of adding to your variable, you compare each card against what the variable is already holding and replace it when the card is bigger. Start the variable at 0 and keep the id alongside the amount, so that at the end you have both.

Write your first attempt without any conversion, run it, and write down what happens and which record stopped it. Then fix it the way you fixed the guided build.

The amount you land on is Rs 4,500, and the order it belongs to is KR4200, which you have already met twice today.

Then answer these three in a markdown cell.

1. Your first attempt stopped. Name the record that stopped it and say in one sentence why the comparison could not be made.
2. The largest order in the file is a returned order. Write down what that means about the money.
3. Here is the hard one. Somebody asks you for "our biggest order across these thirty". You hand them Rs 4,500. What do you have to say alongside that number so that they are not misled by it, and what would you have had to check before you said anything at all?

Question 3 is the one worth sitting with. The number is correct, the code is correct, and the answer is still capable of misleading the person who asked, which is the difference between running a loop and doing the job.

## If you finished everything and want more

Open `demos/C2_W01_D01_decision_tool_STUDENT.xlsx` and work out, without changing any yellow cell,
which single change to the MissingKey tab moves the reported figure furthest with the smallest edit.
Then say in one sentence why that is the tab a reviewer should read first.

Then open the companion page's fourth experiment and run all three positions of `total = 0` in turn.
Write down the printed number for each, and say which of the three you would find hardest to catch
if somebody handed you only the number.

## If you are stuck and want a smaller step

Run `notebooks/C2_W01_D01_ex2_hands_on_STUDENT.ipynb` and stop after step 1. That step asks you for
one letter: what the broken loop prints. Get that letter right and the rest of the notebook is the
same loop with one line moved.

If step 1 is still hard, open `whiteboards/C2_W01_D01_board_diagrams_STUDENT.md` and look at diagram
4. The dotted arrow is the bug, drawn.

