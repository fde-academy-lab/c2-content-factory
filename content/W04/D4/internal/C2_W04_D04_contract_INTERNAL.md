# Week 4 Thursday: the generator's contract

Written by `C2_W04_D04_generate_INTERNAL.py`; every line must read PASS.

| Result | Line | Got | Wanted |
|---|---|---|---|
| PASS | release: every lost order came from a member who kept another September order | 3198 | 3198 |
| PASS | members: 2.6 times the January-to-July mean is August's cohort | 13000 |  |
| PASS | members: January to July move by a few hundred, none at exactly 5,000 | [4854, 5055, 5449, 4859, 4905, 4821, 5057] |  |
| PASS | members: the August cohort is the largest | 2026-08 |  |
| PASS | month one, Jan cohort, prints as 58 percent | 0.5799 | 0.58 |
| PASS | month one, Feb cohort, prints as 56 percent | 0.56 | 0.56 |
| PASS | month one, Mar cohort, prints as 55 percent | 0.55 | 0.55 |
| PASS | month one, Apr cohort, prints as 53 percent | 0.5299 | 0.53 |
| PASS | month one, May cohort, prints as 52 percent | 0.5201 | 0.52 |
| PASS | month one, Jun cohort, prints as 50 percent | 0.4999 | 0.5 |
| PASS | month one, Jul cohort, prints as 49 percent | 0.49 | 0.49 |
| PASS | month one, Aug cohort, prints as 31 percent | 0.31 | 0.31 |
| PASS | every cohort falls at every age it has reached |  |  |
| PASS | selection: organic August members keep July's month-one rate (within a point) | 0.49 | 0.49 |
| PASS | dashboard, Jun, prints as 38 percent | 0.382 | 0.38 |
| PASS | dashboard, Jul, prints as 38 percent | 0.3805 | 0.38 |
| PASS | dashboard, Aug, prints as 38 percent | 0.3794 | 0.38 |
| PASS | dashboard, Sep, prints as 38 percent | 0.3777 | 0.38 |
| PASS | dashboard: flat, within one point June to September |  |  |
| PASS | second route, Jun: the size-weighted cohort average equals the direct count |  |  |
| PASS | second route, Jul: the size-weighted cohort average equals the direct count |  |  |
| PASS | second route, Aug: the size-weighted cohort average equals the direct count |  |  |
| PASS | second route, Sep: the size-weighted cohort average equals the direct count |  |  |
| PASS | the blend over everyone who joined before September sits below the dashboard | 0.3593 | 0.3777 |
| PASS | nothing the case prints rounds to 41 (Kalpa's planted blend) |  |  |
| PASS | member_months.orders equals the order_placed sessions for every member in August and September | 0 | 0 |
| PASS | no non-member order is counted in member_months |  |  |
| PASS | no member has a session before her signup date |  |  |
| PASS | sessions fall on every day of August and September | 5300 |  |
| PASS | an evening peak: more sessions start in the evening than in any other part of the day | 0.631 |  |
| PASS | every session's stages are seconds to minutes apart, in order | (4, 320) |  |
| PASS | search to menu view, members, per session, September, prints as 118 percent | 1.18 | 1.18 |
| PASS | menu view to add-to-cart, members, per session, September, prints as 34 percent | 0.34 | 0.34 |
| PASS | menu view to add-to-cart, members, per member, September, prints as 61 percent | 0.61 | 0.61 |
| PASS | among sessions that searched, the share that opened a menu stays under 100 percent | 0.885 |  |
| PASS | add-to-cart to order, members on Android, before 14 September, prints as 58 percent | 0.58 | 0.58 |
| PASS | add-to-cart to order, members on Android, after 14 September, prints as 44 percent | 0.44 | 0.44 |
| PASS | add-to-cart to order, members on iOS, before 14 September, prints as 57 percent | 0.57 | 0.57 |
| PASS | add-to-cart to order, members on iOS, after 14 September, prints as 56 percent | 0.56 | 0.56 |
| PASS | add-to-cart to order, non-members on Android, before 14 September, prints as 52 percent | 0.52 | 0.52 |
| PASS | add-to-cart to order, non-members on Android, after 14 September, prints as 51 percent | 0.51 | 0.51 |
| PASS | the loss sits at checkout start to order placed on Android members | (0.725, 0.55) | (0.8, 0.8) |
| PASS | the weekly Android rate moves a little and never repeats a value exactly |  |  |
| PASS | every week before the release sits above every week after it |  |  |
| PASS | the fall holds with the release date moved to 7 September | (0.58, 0.475) |  |
| PASS | the fall holds with the release date moved to 21 September | (0.564, 0.433) |  |
| PASS | the lost-order estimate is close to the orders the release actually lost | 3198 | 3198 |
| PASS | orders per active Android member fell from August to September while iOS did not | {'android Aug': 1.36, 'android Sep': 1.2, 'ios Aug': 1.34, 'ios Sep': 1.4} |  |
| PASS | no zone stands out in September (every zone within three points of the city) | 0.009 |  |
| PASS | twelve rows: four May, three June and five August sale members, every one a real member |  |  |
| PASS | twelve rows: the hand counts are the designed ones | {'May m1': 3, 'May m2': 2, 'May m3': 1, 'May m4': 1, 'Jun m1': 2, 'Jun m2': 1, 'Jun m3': 1, 'Aug m1': 1} |  |
| PASS | twelve rows: the dashboard's way reads the same in August and September | (2, 7) | (2, 7) |
| PASS | twelve rows: three of the twelve ordered in September |  |  |
| PASS | twelve rows: every hand-counted rate sits at least five points from its full-data value | 0.053 |  |
| PASS | Kalpa: the 120 members are v4's 120 Retail-Plus customers |  |  |
| PASS | Kalpa: the August cohort is the largest | 32 |  |
| PASS | Kalpa: every v4 app order has exactly one checkout on its date, and no checkout lacks an order |  |  |
| PASS | Kalpa: no session before the membership started |  |  |
| PASS | Kalpa plant: blended retention (app activity), Jul, prints as 41 percent | 0.4054 | 0.41 |
| PASS | Kalpa plant: blended retention (app activity), Aug, prints as 41 percent | 0.4091 | 0.41 |
| PASS | Kalpa plant: blended retention (app activity), Sep, prints as 41 percent | 0.4083 | 0.41 |
| PASS | Kalpa plant: every cohort with two observed ages falls |  |  |
| PASS | Kalpa plant: the August cohort's month-one rate is the lowest observed | {'Jun': 0.923, 'Jul': 0.929, 'Aug': 0.812} |  |
| PASS | Kalpa plant: add-to-cart to checkout at least 15 points lower in 10 to 30 September | {'before': 0.824, 'comparison': 0.833, 'window': 0.636} |  |
| PASS | Kalpa plant: within 5 points outside the window |  |  |
| PASS | Kalpa plant: at least 20 percent of sessions skip search | 0.309 |  |
| PASS | Kalpa plant: checkout per session and per member at least 10 points apart, September | (0.078, 0.245) |  |
| PASS | Kalpa lab rows: the hand counts sit at least five points from every planted rate | (0.571, 0.75) |  |
| PASS | Kalpa lab rows: one member's week shows sessions with and without a search |  |  |
| PASS | twelve rows: no hand-counted rate within five points of a Kalpa retention plant | 0.062 |  |
| PASS | shared constants equal Monday's (the values Monday's branch writes (origin/w04-d1, commit 0f9cf0c)) |  |  |
| PASS | weekly rerun: the sale week's cohort is the largest, the highest in week one and the lowest in week two | {'2026-08-03': (1137, 0.29, 0.303), '2026-08-10': (1112, 0.376, 0.381), '2026-08-17': (9108, 0.531, 0.122), '2026-08-24': (1122, 0.325, 0.151), '2026-08-31': (1166, 0.267, 0.225), '2026-09-07': (1247, 0.338, 0.314)} |  |
| PASS | the practice set's and the quiz's blends hold flat, neither at 38 nor 41 | [[51.0, 51.0], [46.0, 46.0]] |  |
| PASS | the weekly cohorts sum to the members who joined 3 August to 13 September | 14892 |  |
| PASS | the sale week's cohort is the sale-week members and that week's organic joiners |  |  |
