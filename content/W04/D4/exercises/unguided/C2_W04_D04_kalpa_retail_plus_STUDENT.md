# What should Kalpa Retail's head of Retail-Plus fix first?

Kalpa Retail, the programme's client. The head of Retail-Plus, the owner of Kalpa's paid membership,
asks two questions: "Frequency fell in my tier. Is it everyone, or the members who joined during the
monsoon sale and never came back? And the app team says the reorder feature has been fixed, but our
blended retention number has not moved. Where are we actually losing people?" The data are Kalpa's
own: the 120 Retail-Plus customers of the Week 2 warehouse with the date each membership started,
their app sessions from July to September 2026, one row per event (visit, search, add to cart,
checkout), and their app orders. Kalpa counts a member as **active** in a month when she opened the
app at least once that month, and **blended retention** for a month is the share of members who
joined before that month who were active in it.

This set moves the afternoon's call to Kalpa. Item 1 can be sat at any time. Items 2 to 4 sit on
their own page and use what your lab notebook found, so sit them after the lab.

**Who needs the answer.** The head of Retail-Plus, who decides on Friday whether to chase the
monsoon-sale members or send the app team back to the checkout. Kavya Nair, the senior analyst,
reviews the page before it goes.

**The questions on the way.**

- Which first table answers "everyone, or the monsoon-sale members"?
- What is the honest headline from the lab's counts?
- How big is the app's loss, and how sure is it?
- Which call fits, and in what order?

**What you post.** Four letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

## Which table answers the first question?

This comes up at work whenever a tier owner asks whether a fall belongs to everyone or to one group:
the first table fixes the moment each member joined.

### Q1. Which first table answers the question "is it everyone, or the monsoon-sale members"?

*Level L5, a design call · asked in GCC analytics screens.*

a) Blended retention for July, August and September, one number for each month
b) The app's September funnel, each step over the step before it
c) Orders per member per month across the whole tier, July to September
d) Each joining month's active share by age, with its size

---

## After the lab: what do your findings decide?

Sit this page after the lab. It states what your lab notebook's your-turn cells found.

| What the lab found | The count |
|---|---|
| Blended retention, July, August, September | 30 of 74, 36 of 88, 49 of 120: 40.5, 40.9 and 40.8 percent |
| Each cohort's active share, July to September | Falls month by month in every cohort; May's runs 7, 6 and 5 of 13 |
| The August cohort, the largest at 32 members | 26 of 32 active in its month one, September, 81 percent, against 13 of 14 for July's cohort and 12 of 13 for June's |
| Add-to-cart to checkout, per session | 28 of 34 before 20 August, 82 percent; 10 of 12 from 20 August to 9 September, 83; 7 of 11 from 10 to 30 September, 64 |
| Sessions with no search | 145 of 469, 31 percent |
| September's checkout, two units | 12 of 153 sessions, 7.8 percent; 12 of 49 active members, 24.5 percent |

The window from 10 to 30 September is the one Monday's lab fixed, when the app's auto-reorder ran.

### Q2. What is the honest headline for the head of Retail-Plus?

*Level L5 · asked in every analytics screen.*

a) Every cohort fell, the monsoon one started lowest, and the flat 41 hides both
b) Retail-Plus is stable, since blended retention held at 41 percent all quarter
c) Everyone fell in September at once, so the app broke for the whole tier
d) The monsoon cohort is the only one falling, and the older cohorts hold

### Q3. At the earlier rate of 10 in 12, about how many checkouts are missing from the window's 11 carts, and what does that size mean for the call?

*Level L5, a design call · asked in product-company screens.*

a) About 4, the 36 percent of the 11 window carts that never reached a checkout
b) None that matters, since 7 of 11 and 10 of 12 differ by less than one session
c) About 2 in three weeks: real but thin, so confirm before rebuilding
d) About 20, the fall from 83 to 64 read as a count of checkouts

### Q4. Which call fits the lab's findings?

*Level L5, a design call · asked in GCC analytics screens.*

a) Chase the monsoon-sale members first, since their cohort is both the largest and the weakest
b) Check the window's checkout step first and confirm it; judge the monsoon cohort on its curve
c) Report the flat 41 percent, since the blend held and the reorder fix has worked
d) Rebuild the search step first, since 31 percent of sessions skip it and never search

---

## What goes on the second page?

Write the same five lines for the head of Retail-Plus that your group wrote for Zomato Gold's
membership lead: the call, the evidence with its counts, the cost with its doubt, the app team's
objection answered, and what would change it. Name the unit of every rate. Kavya Nair's review asks
for a second route: your blended retention as the weighted average of your cohort rows has to match
your direct count.
