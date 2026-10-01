# Which answers hold in the chapter 5 set on whether the channel suite adds up, and why?

Answers: 1c 2a 3b 4d 5c

Chapter 5 tied the segment suite out the way Anand's analyst will: in each quarter the four segments
add back to the book on orders, rupees and customers, because a customer belongs to one segment. A
half-year made by adding each segment's two quarter rows counted Retail-Plus at 167 customers when the
tier has 120 members; counted from the orders it is 107, and the 60 counted twice are exactly the
members who bought in both quarters. The set asks the same questions of the channels, where a customer
can buy through more than one. Three of the five items are design items: 1, 2 and 5.

**Who needs the answer.** You do, when you check your five letters after the lab or tonight. The
analyst adds every column before she reads a query, and a channel line that fails her addition takes
the whole sheet's credibility with it.

**The questions on the way.**

- Which idea does the chapter 5 set test: which columns add, and how a wider window is counted?
- Why does each of the five keys hold, from the web's 194 to the store's 204?
- Why is option d in item 3, holding the channel lines back, worth arguing about?
- Where does Meta count a person once across four apps?

## Which idea does the chapter 5 set test: which columns add, and how a wider window is counted?

Orders and rupees add across quarters and across channels; customers add only across groups a customer
cannot share. The design items judge the ways to a half-year by what each prints for the web, size
the ways to six months, two quarters and a half-year in one sheet, and confirm the store's half-year
from each customer's history. The other two items read a channel tie-out that cannot close and judge
what a ceiling check proves.

## Why does each of the five keys hold, from the web's 194 to the store's 204?

### Q1. Which way should produce each channel's half-year customers, judged by what each prints for the web?

Kind: a design item, the best-fit way sized by what each prints, which the learner works out from the
table: the web had 130 customers in Q1 and 113 in Q2, and 49 bought through it in both.

The key is c, "Count the web's customers from April to September in its orders: 194, with 1,000 rows
read". A count over the six months counts each customer once, and the table shows what that gives
before anyone runs it: 130 plus 113 counts the 49 twice, so the half-year holds 130 plus 113 less 49,
which is 194. It reads the 1,000 orders once more, which costs no noticeable time on this book.

- a, "Add the web's two quarter rows: 243 customers, with six rows read for the three channels": reads
  the fewest rows and counts the 49 who came back twice.
- b, "Take the larger quarter for customers, 130, and add the two quarters' orders and rupees": only
  49 of Q2's 113 bought in Q1, so 64 web customers are missing from it.
- d, "Count every web order of the half-year with count(*): 331 customers, with all 1,000 rows read":
  counts the web's 181 and 150 orders under the name customers, chapter 1's mistake on a wider
  window.

### Q2. Which way fits once Anand wants months, quarters and the half-year on one sheet, sized in statements and reads?

Kind: a design item, the fact that switches the choice, sized: three channels times six months, two
quarters and one half-year is 27 lines.

The key is a, "GROUPING SETS: 1 statement, 1 read of the 1,000 orders and 27 rows, each window
counted from them". One statement returns every window, each counted from the orders with the same
definition, so the analyst reruns one query and ties the sheet out in one result. With one window,
a plain count from the orders was enough; several windows at once are what make the extra feature
worth reading.

- b, "Three queries, one per window: 3 statements and 3 reads of the 1,000 orders for the same 27
  rows": every number is right, at three times the statements and reads, and the analyst ties out
  three results where one would do.
- c, "Months added into quarters and the half-year: 1 read and 27 rows, the customers added across
  months": orders and rupees survive the adding, and a customer who bought in two months is counted
  twice in the quarter.
- d, "One query by month: 1 read and 18 rows, with the quarters and the half-year left to the sheet's
  formulas": the sheet's formulas would add the months' customers, the same double count moved out of
  the warehouse.

### Q3. What does the Q1 tie-out of the channels' customers against the book say?

Kind: spot the plausible wrong reading. The channels' Q1 orders add to 538; their customers add to
391 against 244.

The key is b, "391 exceeds 244 because a customer who bought through two channels sits in both of those
channels' rows".
Of Q1's 244 customers, 126 bought through one channel, 89 through two and 29 through all three, so the
channel rows hold 126 plus 178 plus 87, which is 391. Each channel's count is right; the parts can
share a customer, so they cannot add to the whole.

- a, "The book undercounts Q1's customers by 147, since the three channel queries each count
  customers once": each query counts a customer once within its channel, and the book counts each
  customer once across all three, which is why the book is smaller.
- c, "One of the channel queries counts order rows as customers, since only a wrong count could exceed
  the book": the channels' order counts are 192, 181 and 165, and their customer counts are well
  below them, so no query is counting rows.
- d, "The tie-out fails on customers, so the channel lines stay off the sheet until they add to 244":
  the customer lines are right and can never add to 244; the sheet says why and ties out orders and
  rupees instead.

### Q4. What should the analyst conclude from a half-year line that passes the members check?

Kind: judge what a check proves. The added line reads 257 app customers, under the book's 340.

The key is d, "257 may still be too high, since the check only catches a count above the 340
customers". A ceiling catches only a double count large enough to break through it. Counted from the
orders the app's half-year is 205, so the line overstates by the 52 customers who bought through
the app in both quarters, and the check never saw it.

- a, "257 holds, since it passes the one check that catches a customer counted twice": the check
  catches only the double counts large enough to exceed 340.
- b, "257 is too low, since the half-year also holds customers who bought in neither quarter": the
  half-year is the two quarters together, so a customer who bought in neither did not buy in it.
- c, "257 holds for a channel, since a channel's customers, unlike a segment's, can be added across
  quarters": a customer who comes back in Q2 sits in both of the channel's quarter rows exactly as in a
  segment's.

### Q5. Which tie-out of the store's customer histories confirms its half-year count?

Kind: a design item, the independent second route, computed. Three filters over one row per store
customer gave 83 in Q1 only, 76 in Q2 only and 45 in both; the table gives the store's quarters, 128
and 121.

The key is c, "83 plus 76 plus 45 is 204, and 83 plus 45 and 76 plus 45 give back Q1's 128 and Q2's
121". The three groups never overlap, so their sum is the half-year, and it matches the 204 the
half-year query printed. The same groups rebuild each quarter, so a wrong count anywhere would break a
tie-out.

- a, "128 plus 121 is 249, so the half-year query undercounts the store's customers by 45": adding the
  quarters counts the 45 who bought in both twice, so 249 is the overcount, not the query.
- b, "83 plus 76 is 159, since the 45 in both quarters were already counted in Q1's 83": the 83 are
  the customers who bought in Q1 only, so the 45 sit in none of the two numbers added.
- d, "128 plus 121 less twice the 45 is 159, since the 45 sit in both of the two quarter counts": the
  45 are counted twice in 249 and belong once in the half-year, so they come off once, not twice.

## Why is option d in item 3, holding the channel lines back, worth arguing about?

Holding back a line that fails a tie-out is a sound instinct, and an analyst who ships a failing
tie-out without comment deserves the doubt she gets. Here the parts can share a customer, so the
addition was never going to close. The line stays on the sheet with a note under it saying that a
customer can buy through more than one channel, and the tie-out moves to orders and rupees, which do
add.

## Where does Meta count a person once across four apps?

Meta's Form 10-K for 2025 reports 3.58 billion daily active people on average in December 2025, and it
defines a person as a logged-in user of Facebook, Instagram, Messenger or WhatsApp who visited at least
one of them that day, matching accounts to people and counting such a group of accounts as one person.
Adding each app's daily users would count a person who opens two apps twice, which is item 3's
tie-out at a larger scale.
