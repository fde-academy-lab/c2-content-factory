# Which letters say which numbers pass the proxy test, and which drift once somebody is paid on them?

Answers: 1b 2d 3c

*The canteen and the school bus are invented for chapter 1, with every number in them. Uber's case is illustrative: the company is real, the situation and the data are synthetic, built for this class.*

A school canteen (invented) pays its servers per token from day 6, and tokens go from 200 to 400 a
day while plates stay at 200. The same school pays its bus driver per kilometre logged, and the
kilometres go from 40 to 55 a day while 30 children are dropped home. At Uber's Hyderabad scheme the
city team pays drivers on peak online hours. The set asks which number in each place passes the
proxy test.

## What does the set test about the proxy test?

The proxy test asks whether a team could hit a number while the thing it stands for got worse or
stayed the same. A count passes when raising it needs the thing itself: a plate used, a child handed
over, a trip a rider asked for. A count fails when the people paid control it, as servers control
tokens, a driver controls kilometres, and a driver controls when the app is open.

## Why is each key right, and why does each other option fail?

| Item | Key | The question in one line | Why the key holds | Why each other option fails |
|---|---|---|---|---|
| 1 | b | Which canteen count could the servers not raise without serving a plate? | A plate reaches the washing station only after a diner has eaten from it, so the count rises only with plates served. | a: tokens are what the servers hand out, and two tokens a plate doubled them. c: rice cooked follows the token count, so it doubles with the tokens. d: the tally book is written by the server who is paid on it. |
| 2 | d | Which number should the school pay the bus driver on? | A child handed to a parent and signed for is the thing the bus exists to do, confirmed by the person served, so the driver cannot raise it without taking a child home. | a: kilometres rose from 40 to 55 a day while 30 children got home, the same drift as the canteen's tokens. b: hours on duty rise with a slower route. c: fuel moves with the kilometres, so it drifts with them. |
| 3 | c | Which number could the city pay on without paying for an empty hour? | A completed trip needs a rider's request, so a driver cannot raise it by keeping the app open in a zone with no riders. | a: an hour counts whenever the app is open, the drift chapter 7 counts on six drivers. b: offers rise when drivers decline, since a declined request is offered again. d: a driver can enrol for the floor and never drive. |

## Which item is worth arguing about?

Item 2, option d against option a. Kilometres feel like work, and on most routes they move with the
children taken home, which is why a school would pay on them. The test is what happens once pay
follows the number: from day 6 the kilometres went from 40 a day to 55 and not one more child got home. The
signature turns the count into one the person served confirms, the line chapter 5 adds to every
definition that resists gaming.

## Where does a number that fails the proxy test show up at work?

Wells Fargo paid staff on a cross-sell number, accounts and products per household, that counted
accounts nobody used. In September 2016 the bank paid USD 185 million in penalties, USD 100 million
of it to the Consumer Financial Protection Bureau, and in 2020 it agreed a combined USD 3 billion
settlement with the SEC and the Department of Justice (CFPB press release, 8 September 2016, and SEC
press release 2020-38, both checked 13 October 2026).

## What does notebook 01 confirm?

Notebook 01 prints tokens per plate at 1.0 for days 1 to 5 and 2.0 for days 6 to 10, draws the Rs
7,500 thrown away over the five paid days, and runs `drifted(days["tokens"], days["plates"])` to
True. Its your-turn cell runs the same function on the bus, and the check under it confirms 1.83
kilometres a child on day 10 and a drift.
