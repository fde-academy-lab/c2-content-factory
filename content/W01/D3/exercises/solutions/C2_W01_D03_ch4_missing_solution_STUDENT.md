# Which answers hold in the chapter 4 set on values that are missing or cannot be read, and why?

Answers: 1b 2a 3d 4c

Kalpa Retail's export of orders from the ERP, the enterprise resource planning system Finance books orders in, still holds values that are missing or cannot be read once one row per order is kept, and each needs a written decision that the analyst who works for Anand Iyer, the finance controller, can follow, since Operations reads the delivered share every week and Finance reads every rupee.

Two of the four items are design items: 1 and 4.

### Q1 (Design). Which plan for 1,800 orders with no status fits the weekly report?

Next month about 1,800 of 60,000 orders will arrive with no status, a lookup in the courier's system takes about 2 minutes an order, and the delivered share goes out every Monday.

The key is b, "Leave them flagged, with the unknown count beside the share". 1,800 lookups at 2 minutes each is 60 hours, more than a working week, so the flag stays and the report says how many are unknown. A lookup earns its place once it runs as an automatic feed from the courier, and done by hand it costs those 60 hours before every report.

- a, "Look up all 1,800 by hand before the first report goes out": 60 hours of lookups before a weekly report.
- c, "Default them to delivered, since most orders with a status are": invents up to 1,800 deliveries nobody recorded.
- d, "Drop them from the report, since 3 percent cannot move a share": 3 percent of orders can move a share by up to 3 points, and dropping them hides it.

### Q2. What do 300 convertible amounts that start 0, 0, 0 tell you?

A colleague's profile of a Kalpa export, its count of each field's present, convertible and distinct values, reports 300 of 300 amounts convertible, and the sorted amounts start `0, 0, 0, 410, 460`.

The key is a, "Three amounts failed, and a helper turned each into 0". No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the fingerprint of a helper that turns failures into zero.

- b, "Three customers placed free orders during a promotion": a free order would still carry a line and a reason.
- c, "Three orders were cancelled, and cancelled orders carry 0": Kalpa's files book a cancelled order at its value.
- d, "Three small orders rounded down to 0 when converted": amounts are whole rupees, so nothing rounds to 0.

### Q3. Which change fixes a conversion that turns `1,150` into Rs 0?

A colleague converts amounts with `int(v) if v.isdigit() else 0`, and an invented amount written `1,150`, with a thousands separator, comes out as Rs 0.

The key is d, "Try int(); on failure, log the value and its reason". isdigit rejects the comma and the else branch invents a zero. Trying the conversion and logging a failure keeps the value and its reason, so the order waits in the log until a stated rule repairs it, and nothing is sold for Rs 0.

- a, "Keep the isdigit test and footnote the order in the note": the order still reads Rs 0 in every total.
- b, "Replace the 0 with the segment's median amount": invents an amount nobody booked.
- c, "Wrap int() in try and return 0 on any failure": still turns every failure into a zero, whatever its cause.

### Q4 (Design). What goes in the log for an amount that reads `fourteen`?

On an invented export an amount reads `fourteen`, the JSON feed cut from the same extract, one pull of rows out of the ERP, reads `fourteen` too, and no other source holds the order's booked value, the price it was charged.

The key is c, "Reject it to the log, and ask the ERP team for the booked value". The feed witnesses what the extract held, never whether a value is right, so its agreement repairs nothing. With no independent source the order goes to the rejects log with its reason until the ERP team supplies the booked value.

- a, "Repair it from the feed, since a second source agrees with it": the feed copied the defect from the same extract.
- b, "Read the word as Rs 14, since the text is plain about the number": reading a word as a number is a guess, and Rs 14 sits far below any Kalpa order.
- d, "Coerce it to zero, so the pass finishes and the log stays short": a zero is a false value, and it hides the defect from every later check.
