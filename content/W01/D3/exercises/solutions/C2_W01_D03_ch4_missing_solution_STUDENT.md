# Solution: chapter 4 set: what is missing or malformed

Answers: 1b 2a 3d 4c

2 of 4 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | b | design | 1,800 lookups at 2 minutes each is 60 hours, more than a working week, so the flag stays and the report says how many are unknown; a lookup is worth building as an automatic feed from the courier, never as hand work before each report. | a: 60 hours of lookups before a weekly report. c: invents up to 1,800 deliveries nobody recorded. d: 3 percent of orders can move a share by up to 3 points, and dropping them hides it. |
| 2 | a | read | No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the fingerprint of a helper that turns failures into zero. | b: a free order would still carry a line and a reason. c: Kalpa's files book a cancelled order at its value. d: amounts are whole rupees, so nothing rounds to 0. |
| 3 | d | fix the logic | isdigit rejects the comma and the else branch invents a zero; trying the conversion and logging a failure keeps the value and its reason, so the order can be repaired by a stated rule instead of sold for nothing. | a: the order still reads Rs 0 in every total. b: invents an amount nobody booked. c: still turns a failure into a zero, more quietly. |
| 4 | c | design | The feed witnesses what the extract held, never whether a value is right, so its agreement repairs nothing; with no independent source the order goes to the rejects log with its reason until the ERP team supplies the value. | a: the feed copied the defect from the same extract. b: a word is not an amount, and Rs 14 sits far below any Kalpa order. d: a zero is a false value, and it hides the defect from every later check. |
