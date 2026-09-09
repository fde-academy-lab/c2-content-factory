# Tiered extras: Week 1, Day 4

Two tasks, prepared in advance. Take the one that matches where you are, not the one that sounds more impressive.

---

## STRETCH: for anyone who finished the segment summary early

### The trimmed mean, and why nobody trusts it by default

You now know that the mean breaks on a tail and the median does not. There is a third option people reach for, and it is worth understanding well enough to argue against.

A **trimmed mean** throws away the largest and smallest few values and averages what is left. On Kalpa's 44 orders, dropping the single highest and single lowest and averaging the middle 42 gives you something between the mean and the median.

Do this:

1. Compute the mean, the median, and the mean of the 42 orders left after dropping the single highest and single lowest amount. Print all three.
2. Now drop the highest and lowest **three** instead of one. Print it again.
3. Answer in a markdown cell: which of the two trims would you report, and what rule did you use to choose? If your rule is "whichever looks more reasonable", say so honestly, and then say why that is a problem.
4. Answer this too: the trimmed mean removed a real order from a calculation. Yesterday you were told not to delete real orders. Are these in conflict? Take a position in three sentences.

The fourth question is the actual exercise. There is a defensible answer in both directions and the defence is what is being asked for.

### A second run, if you want it

Compute the median amount per segment **among returned orders only**, and compare it to the median across all orders in that segment.

One segment moves more than the others. Say which, say by how much, and give one plausible business reason. You will not be able to confirm the reason from this file, and saying that you cannot is part of the answer.

Watch your denominators here. Business has one returned order, so its "median among returned orders" is that single order's amount. Say what that number is worth.

---

## RECOVERY: for anyone whose segment summary is not running

The summary has four moving parts and it is worth finding which one is stuck. Do these in order and stop at the first one that fails.

### Step 1: does the file load?

```python
import csv
with open("../data/C2_W01_D04_profiled_STUDENT.csv") as f:
    orders = list(csv.DictReader(f))
print(len(orders))
```

You should see `44`.

If you see `FileNotFoundError`, the notebook is not in the same folder as the CSV. Check the file name character by character, since the name is long and one wrong character reads the same to a human.

If you see `50`, you opened yesterday's raw orders file rather than today's profiled one.

### Step 2: are the amounts numbers yet?

```python
print(orders[0]["amount"], type(orders[0]["amount"]))
```

If it says `<class 'str'>`, you skipped Tuesday's conversion. Everything read from a CSV is text, and every comparison and every sum below this line will misbehave until you fix it.

```python
for r in orders:
    r["amount"] = int(r["amount"])
```

Run that once. Running it twice is harmless. Running it never is why your medians look strange.

### Step 3: does one bucket build?

Forget all four segments. Build one.

```python
business_amounts = []
for r in orders:
    if r["segment"] == "Business":
        business_amounts.append(r["amount"])
print(len(business_amounts))
```

You should see `9`.

If you see `0`, your comparison is not matching. Print `orders[0]["segment"]` and look at it closely, since a stray space or a lowercase letter reads the same to you and differently to Python. The segment names carry a hyphen in two cases: `Retail-Core` and `Retail-Plus`.

### Step 4: now do it for every segment

The only change from step 3 is that the destination is chosen by the order instead of being fixed:

```python
buckets = {}
for r in orders:
    key = r["segment"]
    if key not in buckets:
        buckets[key] = []
    buckets[key].append(r["amount"])

for key in sorted(buckets):
    print(key, len(buckets[key]))
```

You should see Business 9, Retail-Core 14, Retail-Plus 11 and Student 10, which sum to 44.

If the total is not 44, you are dropping orders, and the cause is almost always an `if` that should not be there.

### Step 5: add the statistic

Once the counts are right, the median is one line per bucket:

```python
import statistics
for key in sorted(buckets):
    print(key, len(buckets[key]), statistics.median(buckets[key]))
```

You now have two thirds of the session's deliverable. The return rate is the same loop with one more counter, testing `r["status"] == "returned"`, and you should try it before looking at the solution.

**If you got here, you are not behind.** Steps 1 and 2 are where most people are actually stuck, and both are Tuesday's material rather than today's.
