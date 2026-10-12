# Does the morning's story survive a cohort table built by week?

Zomato Gold, Chennai. In class, the cohort table on all 53,089 members, built by signup month, showed
every cohort falling with age, the dashboard's flat 38 percent as a weighted average of cohorts on a
slow slide, and the August cohort's 8,027 sale-week members keeping 20 percent in month one against
49 for the organic August members. In the order flow, members' add-to-cart to order on Android fell
from 58 to 44 percent from the release week of 14 September. Illustrative case: the company is real,
the situation and the data are synthetic, built for this class.

Tonight you rebuild the cohort table by signup week instead of signup month, from the event log, and
say which parts of the story survive. About 60 minutes of work.

**Who needs the answer.** The membership lead, who will be asked on Friday whether the story holds at
a finer grain or only on the monthly table. A finding that changes with the grain is a finding to
state with its grain.

**The questions on the way.**

- How many members joined from 3 August to 13 September, and how do they split into weekly cohorts?
- What share of each weekly cohort ordered in each full week after joining?
- Does the Android fall hold week by week?
- Can one cell be reached a second way?
- Which sentences of the morning survive, and which need new words?

## What do you build, and what do you hand in?

Use `members` and `events` in `content/W04/D4/data/` (the log is `C2_W04_D04_events_STUDENT.csv.gz`;
pandas reads it as it is). In `events`, `user_id` is the same id as `member_id` in `members` for every
member, so a member's orders join to her signup date on it. A week starts on Monday. A member's signup
week is the week holding her signup date, and her **week k** is the k-th full week after it. She is
**active** in week k when the log holds an `order_placed` event of hers in that week. The week of 28
September is three days long, so the table stops at the week of 21 September.

**How to get a week from two dates.** `dates.dt.to_period("W-SUN").dt.start_time` gives the Monday
that starts each date's week: `W-SUN` names the Sunday a week ends on, so each week runs Monday to
Sunday. Two Mondays are `(later - earlier).dt.days // 7` weeks apart. For example, a member who joined
on Wednesday 19 August has the signup week of Monday 17 August; an order on Tuesday 25 August falls in
the week of Monday 24 August, 7 days later, so it is her week 1.

If the faculty session (tentative) slipped today and the fallback block ran, you built part 2 in class
in pairs: rebuild it on your own tonight, then add the rest.

Hand in one notebook that runs top to bottom, with these five things, each under a heading that is a
question:

1. The number of members who joined from 3 August to 13 September, from `members`, and the six
   weekly cohorts' sizes, asserted to sum to it.
2. The weekly cohort table: for each signup week, the share who ordered in weeks 1, 2, 3 and on, up
   to the week of 21 September, built with one `pivot_table` as notebook 02 builds the monthly one.
3. Members on Android, add-to-cart to order per session, week by week from the week of 27 July to
   the week of 28 September, with the release week marked: sessions that placed an order over
   sessions that added to a cart.
4. One check by a second route: the sale week's week-1 share recomputed from a filtered log (the
   members who joined from 17 to 23 August, and their `order_placed` events from 24 to 30 August),
   asserted equal to the table's cell.
5. A paragraph of four to six sentences for the membership lead, plain words first: which sentences
   of the morning survive on the weekly table, which need new words, and what the weekly view shows
   that the monthly one hid.

## What makes the paragraph strong?

It names numbers from your weekly table, never the monthly one. It says what changed with the grain
and why. It says whether the Android fall still starts in one week and no earlier. And it ends on one
sentence the membership lead can repeat.

The self-check (`takehome/C2_W04_D04_selfcheck_STUDENT.md`) lists the numbers your table should give.
Open it after your notebook runs, never before.
