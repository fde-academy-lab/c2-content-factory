# Day 3, E3. Mid-session: classify four gaps

Drop point: the break in the second half. About 15 minutes. No computer.

Four fields are missing values in a Kalpa Retail extract. For each, choose **drop the record**, **use a stated default**, **keep and flag**, or **escalate before deciding**, and write the one-line reason a reviewer would read.

| # | The gap |
|---|---|
| 1 | `amount` is empty on 2 orders out of 50. The order book has no other copy of the value. |
| 2 | `discount` is empty on 39 orders out of 50. Absence means no discount was applied. |
| 3 | `segment` is empty on 6 orders. Segment is assigned by a nightly job that failed once last month. |
| 4 | `status` is empty on 1 order, which is also the largest order in the file at Rs 480,000. |

Then answer this: two of your four choices could be argued the other way. Say which two, and what fact you would need to settle each.
