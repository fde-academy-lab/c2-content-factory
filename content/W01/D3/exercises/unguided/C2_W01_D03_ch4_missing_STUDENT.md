# What should the pass do with a value that is missing or cannot be read, so that no decision invents or deletes a fact?

Chapter 4 set, 4 items, about 12 minutes, after chapter 4. The pass is the day's cleaning run on Kalpa Retail's export of orders from the ERP, the enterprise resource planning system Finance books orders in. It profiles the file, counting for every field the values present, the values that convert and the distinct values; keeps one row per order; converts the amounts; decides every defect in writing; and reconciles to the books, Finance's own record of Q1.

> "Can my analyst follow every decision you made?"
>
> Anand Iyer, finance controller, Kalpa Retail

Chapter 3 kept one row for each of today's 186 orders and set 15 rows aside, and Q1 on the kept rows is Rs 1,90,00,000, the books to the rupee. Some kept orders still carry a field with no value, and the pass needs a written policy for any amount that does not convert. Revenue in every figure is booked value, every order at the price charged, whatever its status. An extract is one pull of rows out of the ERP.

**Who needs the answer.** Operations reads the share of orders delivered every week, and Finance reads every rupee, so a wrong call on a missing or unreadable value changes a number one of them reports. Tonight the analyst who works for Anand Iyer, the finance controller, reads every choice in the log, and a choice she cannot follow costs the team her trust.

**The questions on the way.**

- Which plan for 1,800 orders with no status fits the weekly report?
- What do 300 convertible amounts that start 0, 0, 0 tell you?
- Which change fixes a conversion that turns `1,150` into Rs 0?
- What goes in the log for an amount that reads `fourteen`?

Every number in the items is invented unless the item says it comes from today's file, and the reasoning is the one you ran on Kalpa's export. An item marked Design asks you to combine two of the day's ideas, or to size the options yourself, before you choose.

**What you post.** One line of 4 letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

### Q1. Which plan for 1,800 orders with no status fits the weekly report? (Design)

Next month about 1,800 of 60,000 orders will arrive with no status. Operations can look an order up in the courier's system at about 2 minutes an order, and the delivered share goes out every Monday. Which plan fits the weekly report?

a) Look up all 1,800 by hand before the first report goes out
b) Keep and flag them; report the share and the count unknown
c) Default them to delivered, since most orders with a status are
d) Drop them from the report, since 3 percent cannot move a share

### Q2. What do 300 convertible amounts that start 0, 0, 0 tell you?

A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted amounts start `0, 0, 0, 410, 460`. What most likely happened?

a) Three amounts failed, and a helper turned each into 0
b) Three customers placed free orders during a promotion
c) Three orders were cancelled, and cancelled orders carry 0
d) Three small orders rounded down to 0 when converted

### Q3. Which change fixes a conversion that turns `1,150` into Rs 0?

A colleague converts amounts with `int(v) if v.isdigit() else 0`. On an invented export an amount written `1,150`, with a thousands separator, comes out as Rs 0. Which change fixes the logic?

a) Keep the isdigit test and footnote the order in the note
b) Replace the 0 with the segment's median amount
c) Wrap int() in try and return 0 on any failure
d) Try int(); on failure, log the value and its reason

### Q4. What goes in the log for an amount that reads `fourteen`? (Design)

On an invented export, an amount in the CSV reads `fourteen`. The JSON feed, cut from the same extract, reads `fourteen` for that order too, and no other source holds it. What goes in the log tonight?

a) Repair it from the feed, since a second source agrees with it
b) Read the word as Rs 14, since the text is plain about the number
c) Reject it to the log, and ask the ERP team for the booked value
d) Coerce it to zero, so the pass finishes and the log stays short
