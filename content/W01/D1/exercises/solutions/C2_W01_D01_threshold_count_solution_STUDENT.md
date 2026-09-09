# Day 1 solution, E1. The threshold count and total

### What the build was teaching

Three pieces answer this question and you already had all three: a loop that walks the records one at a time, a condition that asks one thing of each record, and two accumulators that remember what the condition found.

The reason it was built one line at a time is that the failure sits in the middle of it. A cell handed to you whole would have run, given you a number, and taught you nothing about the record that was going to stop it.

### The break you passed through

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

KR4200 stores its amount as the text `"4500"` rather than the number `4500`, and it is the first record in the file, so the loop stopped on card one. `count` was still 0 when it stopped, because nothing had been counted yet.

Python was asked whether a piece of text is greater than a number, and it refused and named both types it was holding. A spreadsheet would have placed that value somewhere in the sort order and shown you a number with no warning attached. You lost ten seconds and you kept the truth.

### The answer

```
count = 0
total = 0
for r in records:
    if int(r["amount"]) > 2000:
        count = count + 1
        total = total + int(r["amount"])

print(count, total)
```

```
13 35020
```

13 of the thirty orders are above Rs 2,000, and those orders total Rs 35,020.

### Line by line

`count = 0` and `total = 0` sit above the loop and inside the same cell. Rerunning the cell puts them back to zero before the loop starts again, which is what stops a second run from adding a second copy of everything onto the first run's answer.

`for r in records:` deals you one card at a time, and `r` is the card in your hand for that turn through the indented lines.

`int(r["amount"])` converts at the point of use. The record on the bench still holds text, and the comparison still gets a number. Today `int()` is a converter and nothing more. What it does when a value will not convert is tomorrow's business.

The two accumulator lines sit inside the `if`, so a card that fails the condition adds nothing to either name. That is the whole mechanism.

`print(count, total)` sits outside the loop with no indent, so it runs once at the end instead of thirty times.

### The two thirteens

The opening demo gave you 13 delivered orders totalling Rs 25,720. This build gave you 13 orders above Rs 2,000 totalling Rs 35,020. They are two different groups of orders that happen to share a count, and the totals are different because the groups are different. If you report one of those thirteens without naming its group, the person reading it will assume you meant the other one.

### Where this pattern lives in production

Every reporting pipeline has a filter, a count and a total somewhere near its output, and the first question a reviewer asks is which records were excluded and why. A money column arriving as text is the ordinary case in this work, which is why the conversion sits at the point of use rather than in your assumptions about the file.
