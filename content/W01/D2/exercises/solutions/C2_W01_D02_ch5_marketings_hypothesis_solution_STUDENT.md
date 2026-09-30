# Solution: Marketing says the flat count hides customers lost and replaced: were any lost, who slowed instead, and which segment fell most?

Answers: 1c 2a 3b 4d 5b 6d

The marketing lead pushed back three ways: a flat count of 69 customers can hide churn, customers who stop buying, replaced by new ones; Retail-Plus, the paid membership tier, is only Rs 65,250 of a Rs 23 lakh fall; and last quarter's summary script says Business fell most. Meera Raghavan, Kalpa Retail's CEO, decides on the Rs 12 crore acquisition budget from the answers.

Three of the six items are design items: 1, 2 and 6.

### Q1. Which test can see churn behind a flat count, and when would it mislead? (Design)

Marketing claims a flat count hides churn replaced by new customers, and four tests are offered, each with a reason to distrust it.

The key is c, "Compare the ids in both quarters, only in Q1 and only in Q2; one person with two ids". Only a comparison of ids names the lost and the new separately, since any count is net. If the store and the app gave one person two ids, the comparison would invent churn until the ids were joined.

- a, "Count each quarter's customers by segment; a segment whose definition changed": a count per segment is still net inside each segment.
- b, "Ask Marketing's CRM for sign-ups by month; a campaign that ran in both quarters": sign-ups see new customers only, and from a second system.
- d, "Compare the counts under a new definition of customer; a customer who changed segment": another count is still net.

### Q2. When does a table of all 69 customers become the better fit? (Design)

With Marketing's churn claim answered by the id overlap's three counts, the item asks when a table of all 69 customers, one row each, becomes the better fit.

The key is a, "When the next question is who slowed, which three counts cannot name". The three counts of the id overlap settle lost and new. The next question, who is buying less, needs each customer's orders side by side.

- b, "When the export holds more than a few hundred customers in a quarter": a larger file makes the table longer to read and changes nothing about which question it answers.
- c, "When Marketing wants the result in rupees rather than in customers": rupees need order values, which neither test reads.
- d, "When the ids come from two systems that each number customers apart": split ids break both tests, and they need joining through the CRM first.

### Q3. Which reply answers Marketing on the 23 customers who ordered less?

Marketing concedes that nobody left, then calls the 23 customers who ordered less churn in all but name.

The key is b, "Buying less is frequency: all 23 bought in Q2, so the lever is keeping them buying". Churn is a customer who stops buying, and all 23 bought in both quarters. Buying less is the frequency branch, which retention work moves and new customers do not.

- a, "They are right: a customer who orders less is halfway gone, so acquisition gets funded": a customer who still buys has not churned, and acquisition adds new people while the 23 stay at their slower pace.
- c, "Split the 23 by segment first, since churn hides inside segments until they are split": splitting by segment says where the slowing sits and leaves it slowing, which is still frequency.
- d, "Leave the 23 out of the customer count, since customers who slow down distort it": the 23 are customers in both quarters, so dropping them changes the count and hides the fall.

### Q4. Which fix keeps every segment in Meera's summary?

Last quarter's script prints `summary: {'Retail-Core': -5.3, 'Business': -15.0}` because its helper `pct_change` returns a value only when the change is 30 percent or less.

The key is d, "Always hand back a number, and mark large changes in a separate column". A function that always returns its number keeps every segment, and the flag no longer depends on whether a value came back.

- a, "Raise the threshold to 50 percent, so that fewer of the changes print": a larger change would still vanish.
- b, "Print the change as well as returning it, so both appear on the screen": it still returns None past the threshold.
- c, "Filter with `if ch < 0`, so that a None is compared with zero as well": comparing None with a number raises an error in Python 3.

### Q5. Does the tier's Rs 65,250 matter in a Rs 23 lakh fall?

Marketing says Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall, so it does not matter, while consumer revenue fell from Rs 2,28,820 to Rs 1,58,540.

The key is b, "Retail-Plus is 93 percent of the consumer business's Rs 70,280 fall". Business orders run to lakhs, so a consumer segment is judged against the consumer business: Rs 65,250 of the Rs 70,280 fall, 93 percent.

- a, "They are right in rupees, so the memo leads with Business and footnotes the tier": the Business rupees rest on three orders, and the behaviour sits in the tier.
- c, "The tier is 49 percent of the fall, since its orders per member fell 49 percent": a fall in a rate is not a share of the rupee fall.
- d, "The tier is 3 percent of the fall, so the reorder complaint can wait a quarter": judged against the whole company, a consumer segment always looks small.

### Q6. What does each customer's first and last order date add, and where does it stop? (Design)

The second route took each customer's first and last order date in the export and counted who first ordered in Q2 or last ordered in Q1: 0 and 0.

The key is d, "The same 0 and 0 from dates alone, though new still means new since 1 April". It reaches the overlap's answer without the quarter field or any set arithmetic, so it could have disagreed. A first order in this export is only the first since 1 April.

- a, "Nothing new, since it reads the same 69 ids the first route already compared": it reads the dates and never the quarter field, so a mislabelled quarter would split the two routes.
- b, "It proves that no customer has left Kalpa since the business opened": the export covers two quarters.
- c, "It shows which customers slowed, which the overlap cannot see": who slowed needs each customer's order counts, the table of all 69 customers.
