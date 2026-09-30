# Solution: rank, compare, accumulate

Answers: P1 top four ships 4, 4, 7 and 4, top five ships 5, 7, 7 and 4; P2 G, W, G, G, W, W;
P3 RANK prints 16 vouchers for 16 members; P4 50 listed, 3 at risk, half passed in the week of
10 August.

The queries are in `C2_W02_D03_lab_solution_STUDENT.sql` in this folder and run unchanged against
the warehouse (v4). Every figure below comes from that run, checked 29 Sep 2026. Members G to N in
P1 are invented.

## P1. Three rankings on a tie

| Member (invented) | Spend | ROW_NUMBER | RANK | DENSE_RANK |
|---|---|---|---|---|
| G | Rs 6,450 | 1 | 1 | 1 |
| H | Rs 5,980 | 2 | 2 | 2 |
| J | Rs 5,980 | 3 | 2 | 2 |
| K | Rs 5,120 | 4 | 4 | 3 |
| L | Rs 4,870 | 5 | 5 | 4 |
| M | Rs 4,870 | 6 | 5 | 4 |
| N | Rs 4,870 | 7 | 5 | 4 |

| List | ROW_NUMBER ships | RANK ships | DENSE_RANK ships | Whole ties only ships |
|---|---|---|---|---|
| Top four | 4 | 4 | 7 | 4 |
| Top five | 5 | 7 | 7 | 4 |

The surprise is the top four under DENSE_RANK, which ships seven members: the tie at second saves a
number, so the three members tied at fifth carry dense number 4 and all walk onto a top-four list.
On the top five, RANK ships seven because the three-way tie at fifth ships whole, and that is the
list a segment head who asked for ties ranked the same expects, with the count said beside it.
Whole ties only ships four on the top five, one short of the ask, because the tie at the line is
dropped.

## P2. GROUP BY or window

| Ask | Answer | Why |
|---|---|---|
| 1 | G | One row per city is wanted, so GROUP BY city with a count of distinct members returns six rows, Delhi the largest at 50. |
| 2 | W | Every order has to stay, so `avg(amount) OVER (PARTITION BY channel)` keeps all 462 Q2 orders and adds the channel's average to each. |
| 3 | G | The board pack wants one line per channel, so GROUP BY channel returns three rows; ask 2 is the same average kept on every row. |
| 4 | G | GROUP BY city with `HAVING sum(amount) > 5000000` returns five cities, Delhi, Chennai, Bengaluru, Mumbai and Pune, and Hyderabad falls short. |
| 5 | W | A position inside each city is wanted, so a rank partitioned by city is computed in a CTE and filtered at three outside it; no city has a tie at third, so it returns 18 rows. |
| 6 | W | Each member's month has to sit beside the same member's previous month, so LAG partitioned by customer and ordered by month, with the previous row checked to be August. |

Asks 2 and 3 are the pair worth keeping: the same average, once collapsed to one row per channel
and once kept on every order.

## P3. Thank-you vouchers for Retail-Core

| Channel | RANK prints | ROW_NUMBER would print | DENSE_RANK would print |
|---|---|---|---|
| App | 6 | 5 | 6 |
| Store | 5 | 5 | 5 |
| Web | 5 | 5 | 7 |
| All channels | 16 | 15 | 18 |

In the app channel two orders tie at fifth on Rs 2,910, so RANK keeps both and prints six. In the
web channel two orders tie at fourth on Rs 2,900, so RANK gives them both 4 and the next order is
sixth, which keeps the web list at five; DENSE_RANK carries on at 5 and lets the two orders of
Rs 2,870 in, which is seven. The 16 vouchers go to 16 different members, so no member receives two.
Every Retail-Core order on the list is at most Rs 3,000, the largest being Rs 3,000 in the app
channel.

The sentence for the lead: "We ranked with RANK inside each channel, so equal orders share a place:
you are printing 16 vouchers for 16 members, six in the app channel because two orders tie at fifth
on Rs 2,910, and five each in store and web."

## P4. The Retail-Core at-risk list

1. The list ranked with RANK carries 50 members, because nobody ties at fiftieth, and Rs 2,78,740
   of Retail-Core's Rs 3,66,250 in Q2, which is 76.1 percent.
2. Three listed members are at risk: C-0010 at position 1 (July Rs 7,840, August Rs 4,080,
   September Rs 1,990), C-0049 at position 12 and C-0030 at position 16. They carry Rs 26,210 of
   Q2 revenue, 9.4 percent of the list's revenue. A flag without the month check names five, adding
   C-0060 at position 37 and C-0054 at position 48, each of whom skipped a month, so a month with no
   reading was read as a fall.
3. Retail-Core passed half its Q2 total, Rs 1,83,125, in the week of 10 August: it stood at
   Rs 1,76,000 at the end of the week of 3 August and at Rs 2,05,870 a week later. By the end of the
   week of 17 August it had booked Rs 2,40,360, which is 65.6 percent.
4. The running total closes at Rs 3,66,250, which is Retail-Core's Q2 total. A total that started on
   6 July would close at Rs 3,41,890 and miss Rs 24,360, the 13 Retail-Core orders placed from 1 to
   5 July, because Q2 starts on 1 July and the plan's first week starts later.
5. The three sentences: "Retail-Core's protect list, ranked with RANK, carries 50 members and 76.1
   percent of the segment's Q2 revenue. Three listed members, C-0010, C-0049 and C-0030, spent less
   in August than July and less again in September, and they carry Rs 26,210; two more members show
   falling orders across a skipped month and are not flagged, because a month without an order is
   no reading. Retail-Core passed half its Q2 total in the week of 10 August and stood at 65.6
   percent by mid-quarter, ahead of an even pace."

## The part worth arguing about

P4, step 2. Someone will argue that C-0054, whose readings run Rs 5,950, Rs 1,910 and Rs 1,090, is
the clearest faller on the list and should be flagged whatever the calendar says. The flag Marketing
asked for is two months running, and his readings come from May, July and September, so the honest
answer is a different flag with a different name, such as "spend down over the quarter", stated as
its own rule.

## Where the pattern lives in production

A voucher list, an at-risk list and a pacing line are three of the first requests a CRM or growth
team sends a new analyst, and each one fails in the way this lab stages: a tie that changes the
print run, a gap that accuses a member, and a running total that starts after the quarter did.
