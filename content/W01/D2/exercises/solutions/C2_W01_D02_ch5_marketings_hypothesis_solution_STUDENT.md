# Solution: chapter 5 scenario set: Marketing's hypothesis

Answers: 1c 2a 3b 4d 5b 6d

3 of the 6 items are design items.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | design | c | Only a comparison of ids names lost and new separately, since any count is net; and if the store and the app gave one person two ids, the comparison would invent churn until the ids were joined. | a: A count per segment is still net inside each segment. b: Sign-ups see new customers only, from a second system. d: Another count is still net. |
| 2 | design | a | The three numbers settle lost and new; the next question, who is buying less, needs each customer's orders side by side. | b: A larger file makes the table longer to read and changes nothing about which question it answers. c: Rupees need order values, which neither test reads. d: Split ids break both tests; they need joining through the CRM first. |
| 3 | scenario | b | Churn is a customer who stops buying, and all 23 bought in both quarters; buying less is the frequency branch, which retention work moves and new customers do not. | a: A customer who still buys has not churned, and acquisition adds new people rather than bringing the 23 back to their old pace. c: Splitting by segment says where the slowing sits and leaves it slowing, which is still frequency. d: The 23 are customers in both quarters; dropping them changes the count and hides the fall. |
| 4 | scenario | d | A function that always returns its number keeps every segment, and the flag stops depending on whether a value came back. | a: A larger change would still vanish. b: It still returns None past the threshold. c: Comparing None with a number raises an error in Python 3. |
| 5 | scenario | b | Business orders run to lakhs, so a consumer segment is judged against the consumer business: Rs 65,250 of the Rs 70,280 fall, 93 percent. | a: The Business rupees rest on three orders, and the behaviour sits in the tier. c: A fall in a rate is not a share of the rupee fall. d: Judged against the whole company, a consumer segment always looks small. |
| 6 | design | d | It reaches the overlap's answer without the quarter field or set arithmetic, so it could have disagreed; a first order in the export is only the first since 1 April. | a: It reads the dates and never the quarter field, so a mislabelled quarter would split the two routes. b: The export covers two quarters. c: Who slowed needs order counts per customer, option C. |
