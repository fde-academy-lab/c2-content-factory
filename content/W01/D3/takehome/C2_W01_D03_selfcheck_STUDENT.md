# Does your take-home reach the numbers a correct pass reaches?

The take-home runs the day's pass on a second extract, one pull of rows out of the ERP, the enterprise
resource planning system Finance books orders in. The ERP team found it from the migration, the Q1
move of the order data from one system to another, and it holds Q1 only:
`data/C2_W01_D03_takehome_STUDENT.csv`. Check your work against the tables below before you post it.
Every number in them was computed from that file by the pass the take-home brief describes, which
ends on the bridge, the walk from the file's total to the clean total one cause at a time.

## Part 1. Do your counts and totals match a correct pass?

Used at work before any number leaves the team, when a second person's figures are set beside yours.

| # | Check | You should reach | If you did not |
|---|---|---|---|
| 1 | Rows read after the header | 97 | You counted the header, or your reader skipped a line; count again with `len(raw)`. |
| 2 | Amounts that fail to convert | 1, and you read the logged row | You coerced failures or never printed the log. |
| 3 | Distinct order ids among the rows that convert | 90 | Your key is not the order_id, or it carries a field that differs on every row. |
| 4 | Rows set aside in all | 7, for two different reasons | You merged two reasons into one, or kept copies. |
| 5 | Rupees carried by the copies set aside | Rs 14,210 | You kept the wrong copy or counted a copy twice. |
| 6 | Rows reconcile | 97 = 90 + 7 | A row went missing between two steps. |
| 7 | Clean Q1 total | Rs 80,53,330 or Rs 80,50,930, depending on one decision you name | You have not made the decision the brief warns about, or you made it silently. |
| 8 | Rupees reconcile | Rupees as read less rupees set aside equals your clean total | A row left the file without its rupees leaving the bridge. |

## Part 2. Could an analyst follow your log without asking you?

Used at work when an analyst audits a log while its author is out of the room.

| # | Check | Pass when |
|---|---|---|
| 9 | Every row set aside has a line, a field and a reason | An analyst could find each one in the file without asking you |
| 10 | At least four decisions are logged | Each says drop, default, or keep and flag, and why |
| 11 | One decision names both totals | The note says what the other answer would have given |

## Part 3. Does your note carry the clean total first, both reconciliations and today's finding?

Used at work when a note reaches someone who reads its first sentence and decides from it.

| # | Check | Pass when |
|---|---|---|
| 12 | Under 120 words, numbers first | The first sentence carries the clean total |
| 13 | Both reconciliations stated | Rows and rupees, each as an equation |
| 14 | Today's finding addressed | One sentence on whether this extract changes anything said today |
