# What does the one page a company adopts hold, and how does it settle an argument?

*Balaji Kirana and the driving school are invented for chapters 2, 5 and 6, with every number in them.*

**The example, in short.** Balaji Kirana's (invented) full page has seven lines. Numerator:
deliveries confirmed with the customer's OTP. Denominator: orders billed that week, the count printed
beside the rate. Window: the calendar week. Exclusions: orders the customer cancelled before
dispatch, each change dated. What it does not reward: a done press with no OTP, a dispatch time typed
by hand, a shrinking order count. Guardrails: complaints per 100 orders billed, and the share of
confirmed deliveries within 30 minutes of the bill. Gaming note: complaints catch an OTP asked for
by phone before the goods arrive, and the bill clock catches a dispatch time typed late. Over four weeks it read 40 of 50, 0.80. The son's
growth plan read "Deliveries, monthly, plus 20 percent".

**Who needs the answer.** Three people who must sign one page: the owner, who wants the deliveries
customers received; the son, who wants growth; and the delivery boy, who wants pay that is fair. After
the break, the Hyderabad city head signs Uber's page the same way.

**The questions on the way.** How many lines does a page with a name, a window and a wish hold?
Which line answers a delivery boy who says a quiet week punishes him? What does the page offer the
son, whose number lost?

Q1 is called aloud at the end of chapter 6, with the trainer; Q2 and Q3 are sat in the practice lab.
Every item has one right answer. Items marked **Design** ask for the best-fit approach, the fact that
would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxx
```

---

## How many lines does a page with a name, a window and a wish hold?

The seven lines run: numerator, denominator, window, exclusions, what it does not reward,
guardrails, and the gaming note.

### Q1. Chapter 2's driving school (invented) writes its growth number as "Licences, yearly, as high as possible". How many of the seven lines does it hold?

a) One: what is counted

b) Two: what is counted, and over when

c) Three, counting "as high as possible" as a line

d) Four: enough to make it computable

---

## Which line answers a delivery boy who says a quiet week punishes him?

A page settles an argument when one of its lines already answers the complaint, so the team points
at the line instead of reopening the number.

### Q2. Design. The delivery boy says the shop's number punishes him in a quiet week, when fewer orders come in. Which line of the full page already answers him?

a) The window, since a calendar week evens out the quiet days

b) The exclusions, since a quiet week's orders can be left out

c) The denominator, since a quiet week bills fewer orders too

d) The gaming note, since it names what a quiet week hides

---

## What does the page offer the son, whose number lost?

The owner chose deliveries confirmed with the customer's OTP per order billed. The son wanted total
deliveries, a number about the shop's growth.

### Q3. Design. What does the page offer the son, so that growth stays in view without becoming a second north star?

a) A growth target, orders billed up 20 percent, read beside the rate

b) A second north star for growth, read in alternate weeks

c) Nothing, since the shop's growth is not the page's job

d) The count of orders billed, printed beside the rate every week

---

## Where do you check your calls?

Notebook 06, `notebooks/C2_W04_D01_06_metric_definition_artifact_STUDENT.ipynb`, holds both pages as
dictionaries, reads them on the four weeks, and runs `missing_lines(page)`, which flags a blank line
and a guardrail that catches nothing. Then post your three letters.
