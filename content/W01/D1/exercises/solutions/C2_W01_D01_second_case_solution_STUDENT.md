# Solution: does one channel change the recommendation?

Answers: 11c 12a 13d 14b 15a 16b

The executed notebook beside this file,
`exercises/solutions/C2_W01_D01_ex2_second_case_solution_STUDENT.ipynb`, computes every number here
from the 30 orders.

## The idea being tested

"Store brings 91.6 percent of revenue" is true on booked rupees and misleading as a basis for a
plan, because one order carries it: the order your round 3 sort put at the top is a store order.
The check is the count of orders behind each share, then the share recomputed on the other 29
orders, then each channel split by status. On those 29 orders, Rs 64,810 in all, store holds
Rs 18,920, 29 percent, and 4 of its 9 orders were cancelled. Web leads on booked rupees with
Rs 27,290, and half its orders came back: 5 returned, Rs 14,970. App is clean, 10 of 10 delivered,
Rs 18,600. The branch recommendation, frequency first, stands, and the channel view adds two leaks
to name in the note: web returns and store cancellations.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 11 | c | Store's 91.6 percent is mostly one order, so its share describes that order and says little about store's customers. | a moves the share the wrong way for the wrong reason; delivered orders make it about 94 percent, which is the same order again. b swaps rupees for orders without saying so. d accepts a total the morning taught you to question. |
| 12 | a | Store's other 9 orders total Rs 18,920, and Rs 18,920 over Rs 64,810 is 29 percent. | b keeps the order the question set aside. c divides delivered rupees by booked rupees, two definitions in one ratio. d is a share of orders, and the question asked for revenue. |
| 13 | d | Web's 10 orders split 5 delivered, Rs 12,320, and 5 returned, Rs 14,970, so more than half of its booked rupees came back. | a: web delivered only Rs 12,320, less than app's Rs 18,600. b: web had no cancelled orders. c: half of web's orders were returned. |
| 14 | b | Store's 9 orders on this base split 4 cancelled, Rs 9,050, and 5 delivered, Rs 9,870. | a: 4 were cancelled. c: store had no returns; the returns sit on web. d: 5 of the 9 were delivered. |
| 15 | a | The branch question was answered by customers and frequency, and no channel number changes those; the channel view adds two leaks the note should name. | b is the trap, a share carried by one order. c reads web's booked lead without its returns. d throws away two findings Meera can act on. |
| 16 | b | The 10 Retail-Plus orders carry 8 distinct ids, and one of those customers also bought as Retail-Core, since segment is recorded on the order. | a counts orders as customers, round 2's trap on a new split. c is every customer in the file. d divides revenue by a typical order, which estimates orders, and then calls them customers. |

## The part worth arguing about

Item 15. Pairs who found the web returns will want the note to lead with them, because they are
the most striking number in the split. They belong in the note, second. Meera asked which branch to
open, and the returns are a leak inside revenue per order on one channel, which does not change the
branch. A note that leads with the most striking finding over the asked-for one reads as a changed
subject.

**Kavya's review.** "Every share has a count behind it. Say how many orders make the share before
anyone plans around it."

## Where the pattern lives in production

Channel mix reviews in retail, marketplace seller rankings and regional revenue splits all carry
the same risk: one large account or one large order sets a share, and a plan follows the share.
Sales operations teams report shares with and without their top accounts for exactly this reason,
and a returns rate by channel is a standard line in any e-commerce operating review.

## Hands-on

The seven TODO picks in `notebooks/C2_W01_D01_ex2_second_case_STUDENT.ipynb`, in order, are
c b d a b c a. The executed solution notebook named above carries the filled line for each, and its
checks all print PASS.

## The afternoon in one line

For the debrief, both cases together:

Answer key: 3b 4d 6a 7c 8b 9d 10a 11c 12a 13d 14b 15a 16b
