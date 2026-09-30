# Which answers hold in the chapter 5 set on whether the channel suite adds up, and why?

Answers: 1b 2d 3a 4c 5b

Chapter 5 tied the segment suite out the way Anand's analyst will: in each quarter the four segments
add back to the book on orders, rupees and customers, because a customer belongs to one segment. A
half-year made by adding each segment's two quarter rows counted Retail-Plus at 167 customers when the
tier has 120 members; counted from the orders it is 107, and the 60 counted twice are exactly the
members who bought in both quarters. The set asks the same questions of the channels, where a
customer can buy through more than one. Three of the five items are design items: 1, 2 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. The analyst adds
every column before she reads a query, and a channel line that fails her addition takes the whole
sheet's credibility with it.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

Orders and rupees add across any parts that split the orders; customers add only across groups no
customer can share, and a window wider than a quarter counts its customers again from the orders. The
design items choose how to produce a half-year column, switch to one pass for several windows, and
confirm a half-year by a second route. The other items read a channel tie-out that cannot close on
customers, and ask what a passing sanity check proves.

## Why is each key right, item by item?

### Q1. How should the suite produce each channel's half-year column, and what does each way assume?

Kind: a design item, the best-fit way with its size and its assumption.

The key is b, "Count the half-year from the orders the way each quarter is counted, 1,000 rows read
once more". It keeps one definition, customers who bought at least once in the window, and widens
only the window, so orders, rupees and customers all come out right: the app's half-year is 345
orders and 205 customers. On a book of 1,000 orders the extra read costs nothing anyone would notice.

- a, "Add each channel's two quarter rows, six rows read, assuming every measure adds across
  quarters": orders and rupees add, and customers do not, since a customer who bought through the app
  in both quarters sits in both rows; the app would read 257.
- c, "Report no half-year and let the analyst add the quarter rows by hand on the sheet": hands the
  same wrong addition to the analyst, who is the one person the suite is meant to satisfy.
- d, "Take the larger of each channel's two quarter counts for customers and add the rest, six rows
  read": the larger quarter, 133 for the app, misses the 72 who bought through the app only in Q2.

### Q2. Which way fits once Anand wants months, quarters and the half-year on one sheet?

Kind: a design item, the fact that switches the choice. Several windows, one pass, one result.

The key is d, "One grouped query with GROUPING SETS for month, quarter and half-year, counted from the
orders once". Each window's customers are counted from the orders, so none is added from a narrower
one, and all three windows come back in one result from one pass. Several windows at once is the fact
that makes the extra feature worth learning.

- a, "The monthly rows added into quarters and the quarters into the half-year, since the months are
  counted from the orders": the months are right, and adding them double-counts every customer who
  bought in two months.
- b, "Three separate queries, one per window, each read and tied out on its own": the numbers are
  right, in three passes and three results, where the ask was one of each.
- c, "One query grouped by channel and quarter, with the half-year added from it and the months left
  off": drops the months Anand asked for and adds customers across quarters.

### Q3. What does the Q1 tie-out of the channels' customers against the book say?

Kind: spot the plausible wrong reading. The channels' Q1 orders add to 538; their customers add to
391 against 244.

The key is a, "391 exceeds 244 because a customer who bought through two channels sits in both rows".
Of Q1's 244 customers, 126 bought through one channel, 89 through two and 29 through all three, so the
channel rows hold 126 plus 178 plus 87, which is 391. Each channel's count is right; the parts can
share a customer, so they cannot add to the whole.

- b, "The book undercounts Q1's customers by 147, since the three channel queries each count
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

The key is c, "257 may still be too high, since the check only catches a count above 340". A ceiling catches only a double count large enough to break through it. Counted from
the orders the app's half-year is 205, so the line overstates by the 52 customers who bought through
the app in both quarters, and the check never saw it.

- a, "257 holds, since it passes the one check that catches a customer counted twice": the check
  catches only the double counts large enough to exceed 340.
- b, "257 is too low, since the half-year also holds customers who bought in neither quarter": the
  half-year is the two quarters together, so a customer who bought in neither did not buy in it.
- d, "257 holds for a channel, since a channel's customers, unlike a segment's, can be added across
  quarters": a customer who comes back in Q2 sits in both of the channel's quarter rows exactly as in a
  segment's.

### Q5. What does the web's half-year come to by a second route?

Kind: a design item, the independent second route, computed. The web had 130 customers in Q1, 113 in
Q2, and 49 bought through it in both.

The key is b, "194, Q1's and Q2's customers less the 49 in both". Adding the quarters counts the 49
twice, so taking them off once leaves 130 plus 113 less 49, which is 194, the same as the count from
the orders. The route shares no code with that count, since it works from each customer's quarters.

- a, "243, the two quarters' customers added": counts the 49 who came back twice.
- c, "145, Q1's and Q2's customers less twice the 49 in both": takes the returning customers off
  twice, so they vanish from the half-year altogether.
- d, "130, the larger quarter, since the Q2 buyers bought in Q1 as well": only 49 of Q2's 113 bought
  in Q1, so 64 web customers are missing.

## Which wrong answer is worth arguing about?

Item 3, option d. Holding back a line that fails a tie-out is a sound instinct, and an analyst who
ships a failing tie-out without comment deserves the doubt she gets. Here the parts can share a
member, so the addition was never going to close. The line stays on the sheet with a note under it
saying that a customer can buy through more than one channel, and the tie-out moves to orders and
rupees, which do add.

## Where does this show up at work?

Meta's Form 10-K for 2025 reports 3.58 billion daily active people on average in December 2025, and
it defines a person as someone who visited at least one of its products that day, matching accounts to
people and counting such a group of accounts as one person. Adding Facebook's, Instagram's and
WhatsApp's daily users would count a person who opens two apps twice, which is item 3's tie-out at a
larger scale.
