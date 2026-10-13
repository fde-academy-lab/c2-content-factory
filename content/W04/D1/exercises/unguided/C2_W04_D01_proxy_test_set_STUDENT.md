# Which numbers pass the proxy test, and which drift once somebody is paid on them?

*The canteen and the school bus are invented for chapter 1, with every number in them. Uber's case is illustrative: the company is real, the situation and the data are synthetic, built for this class.*

**The example, in short.** A school canteen (invented) serves 200 plates a day. From day 6 its
servers are paid per token handed out, and tokens go from 200 a day to 400 while plates stay at 200,
so the owner, who cooks tomorrow's rice from today's tokens, throws away Rs 1,500 of rice a day. The
same school pays its bus driver per kilometre logged from day 6, and the kilometres go from 40 a day
to 55 while 30 children are dropped home every day.

**Who needs the answer.** Anyone about to pay a team on a number: the canteen's owner, the school
that runs the bus, and Uber's Hyderabad city head, whose scheme pays drivers on peak online hours. A
number that fails the proxy test pays for the drift.

**The questions on the way.** Which canteen count could the servers not raise without serving a
plate? Which number should the school pay the bus driver on? Which of Uber's numbers passes the test
for riders served?

Q1 is called aloud at the end of chapter 1, with the trainer; Q2 and Q3 are sat in the practice lab.
Every item has one right answer. Items marked **Design** ask for the best-fit approach, the fact that
would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxx
```

---

## Which canteen count could the servers not raise without serving a plate?

The proxy test asks whether a team could hit a number while the thing it stands for got worse or
stayed the same. Once pay follows a count, the people paid find the cheapest way to raise it.

### Q1. Once the servers are paid per token, which count could they not raise without serving one more plate?

a) Tokens handed out at the counter, as the owner reads them each evening

b) Plates collected at the washing station at the end of the day

c) Kilograms of rice cooked from the evening's count of tokens

d) Tokens written into the tally book by the server on duty

---

## Which number should the school pay the bus driver on?

A pay rule is a design choice: the number chosen decides what the driver works to raise.

### Q2. Design. Which number should the school pay the bus driver on, so that it passes the proxy test for children taken home?

a) Kilometres logged, since a longer route means more work done

b) Hours on duty, since the hours cover the traffic and the wait at the gate

c) Litres of fuel bought, since the fuel bill moves with the distance

d) Children handed to a parent at the stop, each one signed for

---

## Which of Uber's numbers passes the test for riders served?

At Uber's Hyderabad scheme (illustrative) the city team wants riders picked up faster at peak, and
asks which number it could pay drivers on.

### Q3. Design. Which number could the city pay drivers on without paying for an hour that serves no rider?

a) Peak online hours, since drivers must be online to pick riders up

b) Offers shown per driver, since more offers mean more riders reached

c) Completed peak trips, since each one needs a rider who asked for it

d) Enrolled drivers, since each new enrolment adds supply at peak

---

## Where do you check your calls?

Notebook 01, `notebooks/C2_W04_D01_01_proxy_test_STUDENT.ipynb`, runs the proxy test as the function
`drifted(paid, wanted)` on the canteen, and its your-turn cell runs it on the bus. Notebook 07,
`notebooks/C2_W04_D01_07_proxy_test_on_twelve_rows_STUDENT.ipynb`, runs the same test on six Uber
drivers. Then post your three letters.
