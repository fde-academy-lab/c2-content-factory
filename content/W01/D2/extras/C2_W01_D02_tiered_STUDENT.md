# Tiered extras: Day 2

Two optional tasks. Take the one that matches where you actually are, not the one that sounds better.

---

## Recovery: if the lab did not come together

No shame in this. Work through these in order and stop when you are moving again.

**Step 1. Prove you can read the file.**

Open `../data/C2_W01_D02_lab_STUDENT.csv` with `csv.DictReader` and print the first record and the record count. Nothing else. If this fails, the problem is the path, and the error message contains the path it tried.

You should see 24 records.

**Step 2. Prove you can spot the bad ones.**

Loop over the records. For each one, try `int(record["amount"])` inside a `try`, and when it fails print the id and the reason. Do not build any lists yet. Just print.

You should see three ids: KR5303, KR5307 and KR5312.

**Step 3. Now build the two lists.**

Same loop. Instead of printing, append to `clean` or to `rejects`. Print the lengths at the end.

You should see 21 and 3, which add up to 24.

**Step 4. Now write them out.**

Two `with open` blocks and two `DictWriter` calls. Then reopen both and count.

If step 2 worked and step 3 did not, the difference is almost always a `continue` in the wrong place, or an append sitting inside an `if` that does not always run.

---

## Stretch: if you finished the lab with time to spare

Do not go looking for pandas. Go deeper into what you already have.

**The recovery question.**

In `../data/C2_W01_D02_orders_STUDENT.json`, record KR4214 has `"amount": null` and its original value sits inside the nested `source` block. Your morning run rejected that record on the CSV, and the value was available the whole time.

Write a function `recover_amount(record)` that takes a JSON record and returns the amount, preferring the top-level value and falling back to the nested one. Then answer these in a markdown cell:

1. How many of the 30 records could be recovered this way?
2. Your total was 53745 without recovery. What is it with recovery?
3. Here is the hard one. You now have two defensible totals for the same dataset, produced by the same person on the same afternoon. What has to be written down so that a reader knows which one they are looking at?

Question 3 is the entire reason tomorrow exists.

**The awkward record.**

`int(" 1360 ")` succeeds. `int("2 450")` raises. `int("1,240")` raises.

Write down the rule Python is actually applying, in one sentence, then test your rule on three inputs you invent yourself. If any of the three surprises you, your rule is wrong and the surprise is the interesting part.

## If you finished everything and want more

Open `demos/C2_W01_D02_decision_tool_STUDENT.xlsx` on the Format tab and find the one combination of the four yellow cells where both CSV and JSON are ruled out. Say in two sentences what you would actually do in that situation, and what you would tell the reader of the file.

Then open the companion page's fourth experiment and run all three reconciliation shapes. Write down which one loses a row without saying so, and say how you would notice it on a file of a million rows rather than five.

## If you are stuck and want a smaller step

Run `notebooks/C2_W01_D02_ex1_hands_on_STUDENT.ipynb` and stop after step 1. One letter: what is the caller holding after a function that only prints? Get that right and the rest of the notebook is the same question asked three more ways.

If step 1 is still hard, open `whiteboards/C2_W01_D02_board_diagrams_STUDENT.md` and look at diagram 1. The two arrows out of the function are the whole answer.
