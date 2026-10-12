# Week 4 Monday: the generator's contract

Written by `C2_W04_D01_generate_INTERNAL.py`; every line must read PASS.

| Result | Line | Got | Wanted |
|---|---|---|---|
| PASS | peak online hours, before | 118000 | 118000 |
| PASS | peak online hours, after | 146300 | 146300 |
| PASS | hours up 24 percent |  |  |
| PASS | completed peak trips, before | 224200 | 224200 |
| PASS | completed peak trips, after | 230900 | 230900 |
| PASS | trips up 3 percent |  |  |
| PASS | trips per peak online hour 1.90 before |  |  |
| PASS | trips per peak online hour 1.58 after |  |  |
| PASS | acceptance 0.863 before | 0.863 | 0.863 |
| PASS | acceptance 0.730 after | 0.73 | 0.73 |
| PASS | driver cancels share 0.037 before |  |  |
| PASS | driver cancels share 0.090 after |  |  |
| PASS | accepted = trips + driver cancels in every row |  |  |
| PASS | share of peak online hours with no trip 0.22 before |  |  |
| PASS | share of peak online hours with no trip 0.38 after |  |  |
| PASS | hours with no trip never exceed hours, never fall below hours less trips |  |  |
| PASS | median rider wait 4.8 before | 4.8 | 4.8 |
| PASS | median rider wait 4.6 after | 4.6 | 4.6 |
| PASS | unfulfilled share 0.11 before |  |  |
| PASS | unfulfilled share 0.10 after |  |  |
| PASS | rider requests rise slightly, 251,910 to 256,556 |  |  |
| PASS | zone fulfilled equals driver trips, week by week |  |  |
| PASS | requests crest in the first after weeks and ease by the last |  |  |
| PASS | bookings Rs 3,69,93,000 before and Rs 3,80,98,500 after |  |  |
| PASS | Rs 314 and Rs 260 per peak online hour |  |  |
| PASS | top-up Rs 0 before and Rs 1.9 crore after |  |  |
| PASS | 61 percent of the top-up to driver-weeks under 0.5 acceptance | (11590000, 7410000) | (11590000, 7410000) |
| PASS | no top-up above the floor times the hours |  |  |
| PASS | no driver-week above 42 peak hours | 42 | 42 |
| PASS | driver-weeks 6,360 before and 6,500 after |  |  |
| PASS | drivers online at peak vary week to week | [1046, 1042, 1048, 1044, 1043, 1047, 1058, 1067, 1071, 1073, 1080, 1085] |  |
| PASS | 1,200 drivers, 140 joined after the launch |  |  |
| PASS | idle tail: 180 drivers under 1.0 trips per peak online hour after the launch | 180 | 180 |
| PASS | idle tail: hours 2.1 times |  |  |
| PASS | idle tail: trips 0.88 times |  |  |
| PASS | idle tail: 72 percent of new hours in the outer zones | 0.72 | 0.72 |
| PASS | idle tail driver-weeks after the launch all under 0.5 acceptance |  |  |
| PASS | every other driver-week after the launch with an hour online at 0.5 or above |  |  |
| PASS | the fall survives without the 140 new drivers |  |  |
| PASS | in the three crest weeks the fall is already there |  |  |
| PASS | twelve rows: hours 60 to 74, trips 114 to 88 |  |  |
| PASS | twelve rows: 1.90 to 1.19 trips per hour |  |  |
| PASS | twelve-row hand count at least 0.05 from the city's 1.58 |  |  |
| PASS | Kalpa: 120 Retail-Plus members |  |  |
| PASS | Kalpa plant: reorders placed per member 1.22 times | 1.22 | 1.22 |
| PASS | Kalpa plant: booked value per member 0.96 times | 0.96 | 0.96 |
| PASS | Kalpa plant: no reorder in the window delivered, each cancelled, merged or pending |  |  |
| PASS | Kalpa lab twelve rows: seven members, both ratios at least 0.05 from the plants | (1.35, 0.88) |  |
| PASS | shared constants: the two Kalpa windows |  |  |
