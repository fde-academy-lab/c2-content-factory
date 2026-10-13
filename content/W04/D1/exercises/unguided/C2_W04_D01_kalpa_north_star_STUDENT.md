# Which number should Kalpa's growth plan chase, and which lines stop the app from gaming it?

*Kalpa Retail is the programme's fictional client: Kalpa and its people are invented, and the data are synthetic.*

**The ask.** Meera Raghavan, Kalpa Retail's CEO, has asked for a growth plan built on how often
customers buy. Three departments have each proposed the company's target: Marketing wants orders
per month, Operations wants app sessions, and the head of Retail-Plus, Kalpa's paid membership tier,
wants reorders per member, which the app can raise by placing reorders on its own. Meera: "One number
the whole company chases, and the numbers that stop us gaming it. If the target moves and the business
does not, I want to know before the board does."

The growth plan's proposed north star is **delivered orders per active customer per month**. The
lab's table, `kalpa_app_reorders`, holds one row per reorder placement: `reorder_id`, `customer_id`,
`placed_ts`, `value_rs` (the placement's booked value, whatever happened to it), `auto` (True when the
app placed it on its own), `status`, which is one of delivered, returned, cancelled, merged into a
basket the member already had open, or pending, and `order_id`, the order in Kalpa's warehouse that
the placement became, blank if none. The lab's per-member figures divide both windows by the same 107
members, the ones already in the tier when the comparison window opened on 20 August, because a
member who joined later had fewer of its days to reorder in: one who joined on 25 August had 16 of its
21.

**Who needs the answer.** Meera, who takes one number to the board, and the three department heads,
each of whom loses their own target under it. A north star the app can raise by itself would show
the board growth while customers received nothing more.

**The questions on the way.** What should the numerator count? Which customers belong in the
denominator? Which guardrail catches frequency bought with low-value orders? Which numbers move
first? Which comparison window keeps a sale out of the reading?

You sit this set after the lab's notebook, `notebooks/C2_W04_D01_04_kalpa_lab_STUDENT.ipynb`, using
the morning's template: the north star's name, its seven lines (numerator, denominator, window,
exclusions, what it does not reward, guardrails, gaming note) and its leading inputs. Items marked **Design** ask for the best-fit approach, the fact
that would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxxxx
```

---

## What should the numerator count?

Every retailer that pays teams on orders decides here whether a placement or a delivery is the order,
and the answer decides what the app is rewarded for.

### Q1. Design. Which numerator should delivered orders per active customer per month count?

a) Every reorder placement in the month, whether the app or the member placed it

b) Orders delivered to the customer in the month, one per order the customer received

c) Every placement a member tapped in the month, whatever its status turned out to be

d) The booked value in rupees of every placement in the month, in place of a count

---

## Which customers belong in the denominator?

A denominator that is defined by the outcome hides the customers who stop buying, which is the
mistake a review of how many customers keep buying is built to catch.

### Q2. Design. Which denominator still counts a customer who stopped ordering this month, without counting one who left years ago?

a) Customers with a delivered order in that same month, count printed beside it

b) Every customer who has ever ordered from Kalpa Retail, years ago included

c) App sessions in the month, counted across every member of Retail-Plus

d) Customers with a delivered order in the three months before, count printed

---

## Which guardrail catches frequency bought with low-value orders?

Marketing teams that run coupons are judged against a guardrail like this one, so a cheaper basket is
seen the week it starts.

### Q3. Design. Marketing plans small-basket coupons to lift order frequency. Which guardrail catches frequency bought with low-value orders?

a) Revenue per active customer, read beside the north star every month

b) App sessions per member, since more sessions lead to more orders

c) The number of coupon campaigns sent, since each one lifts frequency

d) Orders per member per month, read weekly against the plan's target

---

## Which numbers move first?

A growth plan names the inputs a team can move this month, so the board sees early whether the north
star is on its way.

### Q4. Which pair are leading inputs for delivered orders per active customer per month?

a) Last quarter's audited revenue, and the return rate for the whole quarter

b) Revenue per active customer, and the discount share of booked revenue

c) Add-to-cart events per active app member, and new Retail-Plus sign-ups

d) Delivered orders in the last month, and the quarter's gross revenue

---

## Which comparison window keeps a sale out of the reading?

Every before-and-after comparison at a retailer is checked for a sale or a festival inside one window
and not the other, because a sale moves orders by itself.

The lab compared reorders in 10 to 30 September 2026 with the three weeks before, 20 August to 9
September 2026. The monsoon sale ran from 5 to 19 August 2026.

### Q5. Design. Why does the comparison window start on 20 August rather than three weeks earlier, on 30 July?

a) Those three weeks hold more reorders, so the comparison would come out too large

b) Both windows then sit after the sale, so the sale's extra orders are in neither

c) A comparison window has to sit in the same calendar month as the one it is set against

d) Every one of the 120 members was then in the tier for the whole of both windows

---

## What does your definition look like on the template?

Write the growth plan's definition on the template below, the seven lines between the north star's
name and its leading inputs, using your five answers, the three guardrails Meera's team has proposed
(revenue per active customer, discount share of booked revenue, and the return rate) and one gaming
note per guardrail. Then post your five letters.

| Line | Kalpa's growth plan |
|---|---|
| North star | Delivered orders per active customer per month |
| Numerator | |
| Denominator | |
| Window | |
| Exclusions | |
| What it does not reward | |
| Guardrails | |
| Gaming note, one line per guardrail | |
| Leading inputs | |
