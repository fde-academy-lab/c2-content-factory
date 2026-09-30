# Which answers hold in the chapter 1 set on what the ERP actually sent, and why?

Answers: 1c 2b 3a 4d

Anand Iyer, Kalpa Retail's finance controller, will not act on the dashboard's Rs 2.1 crore for Q1 until the team shows what the ERP, the enterprise resource planning system Finance books orders in, actually sent, since the books, Finance's own record of Q1, say Rs 1.9 crore and his analyst ties out every figure, matching it to the books line by line.

Two of the four items are design items: 2 and 4.

### Q1. Should the note on the largest Q2 order go to Anand?

A colleague's note names Rs 980 as the largest Q2 order in a new export, found by `max()` on the amounts as the CSV gave them, while the same export holds 21 Business orders, Kalpa's sales to companies, from Rs 2,10,000 up.

The key is c, "Hold it: no largest order sits below every Business order". A Q2 order at Rs 980 cannot be the largest when 21 Business orders start at Rs 2,10,000. `max()` compared the amounts as text, where 9 beats 2, so the note names a small order and the analyst's audit skips the money.

- a, "Send it, since max() looked at every Q2 amount the file holds": max() ranked the amounts by spelling, so reading every one did not help.
- b, "Send it, adding that Business orders are counted apart": the Business orders are Q2 orders in the same file, so the note still names the wrong one.
- d, "Hold it until the ERP team confirms Rs 980 is the true value": the ERP holds the right value, and the fault is in how the colleague compared it.

### Q2 (Design). Which plan fits the 45 minutes before the analyst starts?

A new export of 1.2 crore rows and 12 fields lands, the analyst starts in 45 minutes, and the team's profile, three counts for every field, reads about 20 lakh values a minute.

The key is b, "Profile order_id and amount, then read the rows they flag". All 12 fields are 14.4 crore values, 72 minutes at 20 lakh a minute, past the deadline. order_id and amount are 2.4 crore values, 12 minutes, which leaves half an hour to read what they flag, and those two fields are where a repeated order or an unreadable amount would move Anand's figure.

- a, "Profile all 12 fields, then read the rows the profile flags": 72 minutes, so the analyst starts before the profile has finished.
- c, "Tie out a random sample of 10,000 rows against the books": reads under a tenth of a percent of the rows and says nothing about the rest.
- d, "Total every amount, then set the total beside the books": a total cannot say why it differs from the books.

### Q3. How many rows are copies, and how many amounts cannot be read?

An invented export holds 250 rows, 238 distinct order ids and 247 amounts that convert.

The key is a, "12 copies and 3 unreadable amounts". 250 rows less 238 ids is 12 rows beyond one per order, and 250 less 247 is 3 amounts that do not convert.

- b, "3 copies and 12 unreadable amounts": swaps the two counts.
- c, "15 copies and no unreadable amounts": adds the two counts into one.
- d, "9 copies and 3 unreadable amounts": takes the 3 failures out of the 12, as if every failure were a copy.

### Q4 (Design). Which route counts the distinct ids of 4 crore rows with 2 GB free?

Next quarter's export will hold 4 crore rows, a Python set takes about 100 bytes an id, and the laptop left running overnight has 2 GB free.

The key is d, "Sort the ids on disk, then count each change from the last". 4 crore ids at 100 bytes each is about 4 GB, twice the memory free, so any route that holds every id at once stops part way. A sort can run on disk and has to remember only the id before.

- a, "A set of every id, then its length, as chapter 1 did": needs about 4 GB.
- b, "A Counter over every id, which also keeps how often each appears": needs at least as much as a set, since it keeps a count beside every id.
- c, "A set of the first crore ids, with the answer times four": scales a count that does not scale, since repeated ids can sit anywhere in the file.
