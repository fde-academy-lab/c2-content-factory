# How many customers could a new Kalpa store sign up to Retail-Plus, and how would you know the estimate is sane?

Kalpa Retail, the programme's client, sells through its app, its website and its stores. Anand Iyer,
Kalpa Retail's finance controller, is deciding whether to fund a new store, and he wants a rough
number before the data exists: how many customers it could sign up to Retail-Plus, Kalpa's paid
membership tier, in its first year, in fifteen minutes, from stated assumptions. A sign-up is a new
paying member whose home store is the new one.

**Who needs the answer.** Anand Iyer, who funds or does not fund the store, and who will ask how you
know your number is not wildly off.

**The questions on the way.**

- What is the closest published number to check a store's year against?
- What does the check say when an estimate lands above it?

The closest published number is DMart's, a large grocery chain whose filings give revenue and store
counts:

| Item | Value |
|---|---|
| FY26 standalone total revenue | Rs 66,968 crore |
| Stores at 31 March 2026 | 500 |
| Stores added in FY26 | 85 |
| Stores at 31 March 2025 | 415 (500 less the 85 added) |

Source: Avenue Supermarts' press release of 2 May 2026 (checked 12 October 2026). The table is also
in `data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv`.

Post one line, two letters in item order, no spaces:

```
Post exactly this shape: xx
```

---

## What does DMart sell per store in a year?

This comes up at work whenever a company's total has to be turned into a per-store figure: the
denominator decides the answer.

### Q1. What was DMart's FY26 revenue per store on the average of its opening and closing store counts?

*Level L5 · asked in retail and consulting screens.*

a) About Rs 134 crore
b) About Rs 161 crore
c) About Rs 146 crore
d) About Rs 788 crore

---

## What does the check say about an estimate that lands above it?

This comes up the moment an estimate is laid beside a published figure: the check passes only when the
two count the same thing.

A classmate's chain for Anand implies the new Kalpa store would sell Rs 150 crore in its first year
(an invented result, for this item).

### Q2. Design. What does the validate step say about the classmate's Rs 150 crore?

*Level L5, a design call · asked in retail and product-company screens.*

a) It passes, since it sits within a few percent of DMart's average of about Rs 146 crore a store
b) It is too high: a new store sells below DMart's average, so recheck footfall or spend
c) It cannot be checked at all, since Kalpa sells different products from DMart
d) It is too low, since DMart's two-year-old stores grew 10.8 percent in FY26's last quarter

---

**What does the lab add?** The TA lab sizes Anand's question itself: clarify, map, calculate,
validate, with the catch that a store in its first year sells less than a store that has had years to
build its customers.

**In the interview.** [S] A guesstimate: how many customers could a new store sign up to a loyalty
tier in its first year?
