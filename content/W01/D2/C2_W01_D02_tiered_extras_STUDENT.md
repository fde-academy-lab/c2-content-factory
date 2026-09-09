# Tiered extras: Day 2

Two optional tasks. Take the one that matches where you actually are, not the one that sounds better.

---

## Recovery: if the lab did not come together

No shame in this. Work through these in order and stop when you are moving again.

**Step 1. Prove you can read the file.**

Open `C2_W01_D02_data_lab_STUDENT.csv` with `csv.DictReader` and print the first record and the record count. Nothing else. If this fails, the problem is the path, and the error message contains the path it tried.

You should see 24 records.

**Step 2. Prove you can spot the bad ones.**

Loop over the records. For each one, try `int(record["amount"])` inside a `try`, and when it fails print the id and the reason. Do not build any lists yet. Just print.

You should see three ids: 2004, 2008 and 2013.

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

In `C2_W01_D02_data_records_STUDENT.json`, record 1015 has `"amount": null` and its original value sits inside the nested `source` block. Your morning run rejected that record on the CSV, and the value was available the whole time.

Write a function `recover_amount(record)` that takes a JSON record and returns the amount, preferring the top-level value and falling back to the nested one. Then answer these in a markdown cell:

1. How many of the 30 records could be recovered this way?
2. Your total was 230380 without recovery. What is it with recovery?
3. Here is the hard one. You now have two defensible totals for the same dataset, produced by the same person on the same afternoon. What has to be written down so that a reader knows which one they are looking at?

Question 3 is the entire reason tomorrow exists.

**The awkward record.**

`int(" 4500 ")` succeeds. `int("24 500")` raises. `int("12,400")` raises.

Write down the rule Python is actually applying, in one sentence, then test your rule on three inputs you invent yourself. If any of the three surprises you, your rule is wrong and the surprise is the interesting part.
