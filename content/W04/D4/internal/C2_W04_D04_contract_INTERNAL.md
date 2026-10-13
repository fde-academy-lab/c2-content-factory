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
| PASS | twelve rows: the hand counts are the designed ones | {'May m1': 3, 'May m2': 2, 'May m3': 1, 'May m4': 1, 'Jun m1': 2, 'Jun m2': 1, 'Jun m3': 1, 'Aug m1': 0} |  |
| PASS | twelve rows: the dashboard's way reads the same in August and September | (2, 7) | (2, 7) |
| PASS | twelve rows: two of the twelve ordered in September |  |  |
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
| PASS | shared constants equal Monday's (content/W04/D1/internal/C2_W04_D01_facts_INTERNAL.yaml) |  |  |
| PASS | weekly rerun: the sale week's cohort is the largest, the highest in week one and the lowest in week two | {'2026-08-03': (1137, 0.29, 0.303), '2026-08-10': (1112, 0.376, 0.381), '2026-08-17': (9108, 0.531, 0.122), '2026-08-24': (1122, 0.325, 0.151), '2026-08-31': (1166, 0.267, 0.225), '2026-09-07': (1247, 0.338, 0.314)} |  |
| PASS | counted over everyone, the series falls every month from June to September |  |  |
| PASS | held fixed, iOS completion moves by under a point while Android's falls by more than 15 |  |  |
| PASS | every Android session from 14 September runs v2, and every other session v1 | 1.0 | 1.0 |
| PASS | joined before July, the share who ordered moves under a point on each platform while orders per ordering member fall only on Android |  |  |
| PASS | the practice set's and the quiz's blends hold flat, neither at 38 nor 41 | [[51.0, 51.0], [46.0, 46.0]] |  |
| PASS | the gym: thirty joiners, ten a month, counted by age as designed | {'2026-01': [8, 6, 5, 5, 5], '2026-02': [7, 5, 3, 3], '2026-03': [6, 4, 3]} |  |
| PASS | the gym's April column reads 5, 5 and 6 of 10, 16 of 30, so March looks best by calendar month |  |  |
| PASS | the gym: at the same age March is the weakest batch (age one 80, 70, 60; age two 60, 50, 40) |  |  |
| PASS | the gym's floors: January 5 of 10, February 3 of 10, March none yet | {'2026-01': 5, '2026-02': 3, '2026-03': None} |  |
| PASS | every gym row falls or holds with age, never rises |  |  |
| PASS | the gym's dashboard holds at 50 percent (50 of 100, then 250 of 500) while the older members fall 50 to 40 |  |  |
| PASS | the plain mean of February's two rates is 46.25, not the 50 percent counted |  |  |
| PASS | the second gym's blend reads 48.0 then 47.8 percent while X and Y fall |  |  |
| PASS | the college's step rates: 80, 50, 75, 80 this cycle against 80, 50, 90, 80 last cycle |  |  |
| PASS | the step rates multiply to the overall conversion, 24 percent against 28.8 |  |  |
| PASS | the test is sat by 80 percent of applications in each of three cycles, so its no-show never moved |  |  |
| PASS | per applicant reads higher than per application at every step, and 26.7 against 24 from the top |  |  |
| PASS | the sister programme's test to shortlist reads 107 percent, an artefact; 77 among test-takers |  |  |
| PASS | the groups add up to the programme's shortlist and acceptances in every cycle |  |  |
| PASS | acceptance: in-state 92 to 90, other states 87 to 50; 60 fewer acceptances, 55 of them from other states |  |  |
| PASS | the loss in joiners two ways: 288 less 240 = 48 = 60 fewer acceptances x the 80 percent who join |  |  |
| PASS | the cost on joiners: Rs 48 to 72 lakh of first-year fees, Rs 57.6 lakh at Rs 1.2 lakh | [48.0, 57.6, 72.0] |  |
| PASS | every printed toy blend sits five points from 41, 38, 36 and 33 | [53.3, 50.0, 50.0, 46.2, 48.0, 47.8] |  |
| PASS | the toy artefact and its fix sit five points from the case's 118 and 89 |  |  |
| PASS | the toy skip shares (20 and 70 percent) sit five points from Kalpa's 31 percent with no search |  |  |
| PASS | no toy blend echoes the Saturday bank or the Kahoot, and no toy funnel count echoes the bank's funnel |  |  |
| PASS | the weekly cohorts sum to the members who joined 3 August to 13 September | 14892 |  |
| PASS | the sale week's cohort is the sale-week members and that week's organic joiners |  |  |
