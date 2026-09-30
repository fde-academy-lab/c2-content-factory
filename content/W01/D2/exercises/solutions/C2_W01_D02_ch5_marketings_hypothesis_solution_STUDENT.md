# Solution: chapter 5 scenario set: Marketing's hypothesis

Answers: 1c 2a 3b 4d 5b 6d

3 of the 6 items are design items.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | design | c | Only a comparison of ids names lost and new separately; any count is net, so 20 lost and 20 new also give 69 and 69. | a: A count per segment is still net inside each segment. b: It sees new customers only, from a second system. d: Another count is still net. |
| 2 | design | a | Split identities make one person look lost and new at once, which invents churn; the ids would need joining first. | b: The id stays the same when the segment changes, so the overlap counts the person once. c: Each order sits in its own quarter, so the customer is correctly in both. d: Order counts do not change whether an id appears in a quarter. |
| 3 | scenario | b | Every Q2 customer bought in Q1 and every Q1 customer bought in Q2, so there is no churn for acquisition to replace. | a: The overlap on the whole file already covers every segment. c: Loyal buyers can still buy less, and 23 did. d: Buying less is frequency, not churn: all 23 still bought. |
| 4 | scenario | d | A function that always returns its number keeps every segment, and the flag stops depending on whether a value came back. | a: A larger change would still vanish. b: It still returns None past the threshold. c: Comparing None with a number raises an error in Python 3. |
| 5 | scenario | b | Business orders run to lakhs, so a consumer segment is judged against the consumer business: Rs 65,250 of the Rs 70,280 fall, 93 percent. | a: The Business rupees rest on three orders, and the behaviour sits in the tier. c: A fall in a rate is not a share of the rupee fall. d: Judged against the whole company, a consumer segment always looks small. |
| 6 | design | d | It reaches the overlap's answer without the quarter field or set arithmetic, so it could have disagreed; a first order in the export is only the first since 1 April. | a: It reads dates, not the quarter field, so a mislabelled quarter would split the two routes. b: The export covers two quarters. c: Who slowed needs order counts per customer, option C. |
