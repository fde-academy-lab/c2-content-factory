"""Write the six chapter scenario sets and their solutions from one table, so a key never drifts.

    python3 content/W01/D2/internal/C2_W01_D02_build_exercises_INTERNAL.py

Each item is (kind, stem, options a to d, key, why the key holds, why each other letter fails).
kind is "design" for the best-fit approach, a sizing, the fact that would switch it or the second
route, and "scenario" for every other business item.
"""
import pathlib

DAY = pathlib.Path(__file__).resolve().parents[1]
UNG = DAY / "exercises" / "unguided"
SOL = DAY / "exercises" / "solutions"

SETS = {
    1: {
        "slug": "ch1_is_the_drop_real",
        "title": "Chapter 1 scenario set: is the drop real",
        "ask": "\"Q2 was Rs 1.9 crore, Q1 was 2.1. Marketing says more customers. Prove it or disprove it.\" (Meera Raghavan)",
        "table": """| Window | Dates | Orders | Revenue |
|---|---|---|---|
| Q1, closed | 1 Apr to 30 Jun | 114 | Rs 2,10,00,000 |
| Q2, closed | 1 Jul to 30 Sep | 86 | Rs 1,87,00,000 |
| Q2 dashboard tile, cut on 15 September | 1 Jul to 15 Sep | 70 | Rs 1,55,59,950 |""",
        "picture": """flowchart LR
    A["<b>1 Apr</b><br/>Q1 opens"] --> B["<b>1 Jul</b><br/>Q2 opens"]
    B --> C["<b>15 Sep</b><br/>the tile is cut"]
    C --> D["<b>30 Sep</b><br/>Q2 closes"]""",
        "items": [
            ("scenario", "Meera asks how far revenue fell between the two closed quarters. Which figure goes in the reply?",
             ["12.3 percent, the Rs 23,00,000 gap measured against Q2's total",
              "9.5 percent, from the rounded Rs 1.9 crore against Rs 2.1 crore",
              "11.0 percent, the Rs 23,00,000 gap measured against Q1's total",
              "25.9 percent, the figure on the dashboard tile Marketing quotes"], "c",
             "The change is measured against the starting quarter: Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent, on two closed quarters.",
             {"a": "Measuring against Q2 inflates the fall to 12.3 percent.", "b": "The rounded crore figures lose Rs 3,00,000 of the gap.", "d": "The tile stops on 15 September, so its fall is partly a window artefact."}),
            ("scenario", "Marketing's slide reads \"Q2 Rs 1,55,59,950 against Q1 Rs 2,10,00,000: revenue fell 25.9 percent.\" What makes the slide unfit to act on?",
             ["The percentage is computed on Q2's total, which overstates the fall",
              "It sets about 11 weeks of Q2 against all 13 weeks of the closed Q1",
              "It counts booked orders, where Finance would count delivered ones",
              "It rounds both totals to the nearest lakh before dividing them"], "b",
             "The tile runs 1 July to 15 September, about 11 weeks, against Q1's 13, so two weeks are missing from one side only and Rs 12 crore would move on a gap that is mostly the calendar.",
             {"a": "Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is Q1.", "c": "Both sides count booked orders, which is consistent.", "d": "The totals are exact to the rupee."}),
            ("design", "On 15 September, with Q2 still open, a colleague turns both sides of Marketing's slide into revenue per week, each side divided by the weeks its dates cover. What does the rate give, and what does it still miss?",
             ["Minus 12.4 percent, and it still compares Q2's early weeks with the whole of Q1",
              "Minus 25.9 percent, since dividing both sides by weeks leaves their ratio alone",
              "Minus 11.0 percent, since a rate per week removes every difference in the windows",
              "Minus 17.0 percent, the answer that matched weeks of each quarter would give"], "a",
             "Rs 16,15,385 a week against Rs 14,14,541 is minus 12.4 percent. A rate fixes the length and not the position: Q2's first eleven weeks stand against all of Q1, so while Q2 is open the same 11 weeks of each quarter are the better fit, and the two disagree here (minus 17.0) because a few lakh-sized orders make weeks lumpy.",
             {"b": "Dividing by 13 and by 11 changes the ratio by 13 over 11.", "c": "11.0 is the closed quarters, which needs Q2 closed.", "d": "The same weeks give minus 17.0 because Kalpa's weeks are lumpy, so the two methods disagree on this file."}),
            ("design", "Both quarters have closed. Meera now asks: \"Is Q2 always weaker than Q1, because of the monsoon?\" Which option answers her, and what does it need?",
             ["Closed quarters again, since both are complete and compare like with like",
              "A rate per day, since it removes the one-day gap between 91 and 92 days",
              "The same 11 weeks of each quarter, since it also matches position",
              "The same quarter last year, which needs last year's export to run"], "d",
             "Only a comparison with the same season a year earlier takes the season out, and the file holds April to September of one year, so it needs a data request.",
             {"a": "Closed quarters fix the length, and the two quarters are still different seasons.", "b": "A rate per day fixes a day, not a season.", "c": "Matched weeks fix the position inside a quarter; Q1 and Q2 are still different seasons."}),
            ("scenario", "Four moves answer \"is the drop real\": p) compute the change, q) find the first and last order date of each window, r) state the definition and the window in the sentence to Meera, s) choose closed quarters or matched weeks. Which order is right?",
             ["s, q, p, r",
              "q, s, p, r",
              "q, p, s, r",
              "q, s, r, p"], "b",
             "Read the windows, choose a fair pair, compute, then say the definition and the window in the sentence.",
             {"a": "Chooses a pair before anyone has read the dates.", "c": "Computes before choosing the fair pair, which is how the tile's number reached a slide.", "d": "Writes the sentence before the number it states exists."}),
            ("design", "The second route added revenue by the month in `order_date` and reached the same fall as the closed quarters. What does agreement between the two routes prove?",
             ["That monthly totals are a better headline for Meera than the quarters",
              "That no order in the file carries a wrong amount or a missing field",
              "That the quarter field and the dates give each quarter the same total",
              "That the fall is real and needs no comparison with last year"], "c",
             "The first route trusted the `quarter` field and the second only the dates, and both give each quarter the same total, which is agreement in aggregate; two mislabelled orders of equal value could still cancel out, so an order-by-order check is the stronger proof.",
             {"a": "The quarter key stays the headline; months are for questions inside a quarter.", "b": "Both routes read the same amounts, so a wrong amount would fool both.", "d": "The season is still in the comparison; only last year's Q2 removes it."}),
        ],
    },
    2: {
        "slug": "ch2_which_branch",
        "title": "Chapter 2 scenario set: which branch moved",
        "ask": "\"Are we losing customers, or are the ones we have buying less? Marketing says more customers.\" (Meera Raghavan)",
        "table": """| Branch | Q1 | Q2 | Ratio |
|---|---|---|---|
| Customers | 69 | 69 | 1.000 |
| Orders per customer | 1.65 | 1.25 | 0.754 |
| Revenue per order | Rs 1,84,211 | Rs 2,17,442 | 1.180 |
| Revenue | Rs 2,10,00,000 | Rs 1,87,00,000 | 0.890 |""",
        "picture": """flowchart LR
    R["<b>revenue</b><br/>Rs 2.10 cr to Rs 1.87 cr"] --> C["<b>customers</b><br/>69 to 69"]
    R --> F["<b>orders per customer</b><br/>1.65 to 1.25"]
    R --> V["<b>revenue per order</b><br/>Rs 1,84,211 to Rs 2,17,442"]""",
        "items": [
            ("scenario", "Marketing says the fall needs more customers. Which reading of the tree answers them?",
             ["Customers fell with orders, 114 to 86, so acquisition is the branch to fund",
              "Customers held at 69, so the fall sits in how often they buy",
              "Revenue per order rose 18.0 percent, so the fall must sit with customers",
              "The tree cannot answer until the four segments are split"], "b",
             "Customers held at 69 in both quarters, while orders per customer fell from 1.65 to 1.25, so the branch Marketing wants to fund did not move.",
             {"a": "114 and 86 are orders: rows counted as customers, Monday's trap.", "c": "Customers held, so a rise in order value cannot put the fall there.", "d": "The tree answers Marketing's claim now; segments come in chapter 3."}),
            ("scenario", "A colleague adds the leaf changes, minus 24.6 percent and plus 18.0 percent, and reports revenue down 6.6 percent. What is wrong?",
             ["Nothing: the customer leaf adds zero, so minus 24.6 and plus 18.0 net to minus 6.6",
              "The customer leaf was left out of the sum, and it carries the missing 4.4 points",
              "The two leaves should be averaged, which puts the fall at 3.3 percent",
              "The leaves multiply: 0.754 times 1.180 is 0.890, a fall of 11.0 percent"], "d",
             "Revenue is customers times frequency times order value, so the ratios multiply; adding percentages drops the part where two leaves moved together, as Monday's two lifts called 20 percent did.",
             {"a": "Percentage changes on leaves do not add.", "b": "The customer leaf is 1.000 and carries nothing.", "c": "An average of two changes is no quantity in the tree."}),
            ("design", "Meera wants rupees per branch on one slide she can follow, and Finance will rebuild the same split every month while two branches keep moving together. Which split fits which reader?",
             ["The symmetric split for both, since any order of steps is a bias someone will argue",
              "Leaf percentages for Meera, since she reads percentages, and the bridge for Finance",
              "The bridge in tree order for Meera, order stated; the symmetric split for Finance",
              "Customer by customer for both, since it names who moved before anyone adds them up"], "c",
             "A CEO follows one leaf at a time, so she gets the bridge with its order written beside it; a split rebuilt monthly while two branches move together goes symmetric, so nobody argues about order.",
             {"a": "Meera loses the one-step reading, and on this quarter every order gives the same verdict.", "b": "Percentages do not add, so Meera gets no rupees.", "d": "69 rows before any total answer who moved, not which branch."}),
            ("design", "Customers held at 69, orders per customer fell from 1.652 to 1.246, and Q1's revenue per order was Rs 1,84,211. In the tree's order, what does the bridge's frequency step come to?",
             ["Minus Rs 51,57,895: 69 customers times 0.406 fewer orders at Rs 1,84,211",
              "Minus Rs 60,88,372: the same fall in frequency priced at Q2's Rs 2,17,442",
              "Minus Rs 23,00,000, since frequency is the only branch of the three that fell",
              "Minus Rs 28,57,895, since the order value step takes away the rest of it"], "a",
             "In the tree's order frequency moves second, with customers at Q2 and order value still at Q1: 69 times minus 0.406 times Rs 1,84,211, which is 28 fewer orders at Q1's value.",
             {"b": "Pricing at Q2's value moves frequency after order value, which is the reversed bridge.", "c": "The fall is net of the order value step, which gave back Rs 28,57,895.", "d": "That is the order value step, and it gave rupees back rather than taking them."}),
            ("scenario", "A hurried count reads every missing discount as zero and finds 43 of Q2's 86 orders \"without a discount\". Marketing wants the discount extended to them. Why is the premise unsafe?",
             ["Q1 had 32 blanks as well, so the offer has to reach both quarters' blank orders",
              "The 43 hold, but they should be counted by revenue, since orders differ in size",
              "Blank and Rs 0 both mean no discount, so the 43 hold and only the offer's size is open",
              "Only 17 of the 43 record Rs 0, and the other 26 never recorded the field"], "d",
             "A blank is unknown; reading it as zero files 26 unknown orders under \"no discount\", and the extension spends margin on orders that may already carry one.",
             {"a": "It keeps reading the blanks as zeros, on more orders.", "b": "Changing the weights leaves the blanks read as zeros.", "c": "That is the misreading itself: 26 of the 43 are blanks, which are unknown."}),
            ("design", "The second route split the fall symmetrically, choosing no order at all, and charged frequency minus Rs 55,88,480. Set beside the bridge, what does it show?",
             ["The bridge understated frequency, so its figure has to be corrected upwards",
              "Frequency carries the fall either way; the rupees per branch depend on the method",
              "The two agree to the rupee once the customers step is added back into the bridge",
              "The gap between them is the customers branch, which only the symmetric split sees"], "b",
             "An independent split that chooses no order puts the largest fall on the same branch; the Rs 4,30,585 between them is the part where frequency and order value moved together, which each method shares out differently.",
             {"a": "Neither figure is wrong; the bridge charges the joint part, Rs 4,30,585, to the leaf that moves second.", "c": "The customers step is zero in both routes.", "d": "Customers held at 69; the gap is the joint part of frequency and order value."}),
        ],
    },
    3: {
        "slug": "ch3_which_segment",
        "title": "Chapter 3 scenario set: which segment",
        "ask": "\"One of my members says the app's reorder button has been broken for six weeks. Is my tier the one slipping?\" (the head of Retail-Plus)",
        "table": """| Shown on the projector | Customers | Orders Q1, Q2 | Orders per customer Q1, Q2 |
|---|---|---|---|
| Retail-Core | 34 | 38, 36 | 1.12, 1.06 |
| Business | 11 | 20, 17 | 1.82, 1.55 |
| All customers | 69 | 114, 86 | 1.65, 1.25 |""",
        "picture": """flowchart LR
    T["<b>orders per customer</b><br/>1.65 to 1.25"] --> A["<b>Retail-Core</b><br/>-5.3%"]
    T --> B["<b>Business</b><br/>-15.0%"]
    T --> C["<b>the rest</b><br/>your run"]""",
        "items": [
            ("design", "Copying the loop takes 72 lines and 8 places to edit, a function 21 lines and 1 place, and one pass by key 14 lines and 1 place, shaped for these eight groups. A channel, a month and delivered orders are asked for later today. Which is the best fit?",
             ["Copy the loop per group, since each copy can be checked on its own",
              "One pass by key, since it is the shortest code and reads the rows once",
              "A spreadsheet, since eight groups are few enough to total by hand",
              "A function, tree_for(rows), since each later subset is one more call"], "d",
             "The later asks are new subsets, and a function answers any list of orders with one call; one pass by key would need a new loop for each new key.",
             {"a": "Eight places to edit when the definition changes, and one gets forgotten.", "b": "Shortest today, and a channel or a month needs a new loop.", "c": "A hand total cannot be rerun on delivered orders this afternoon."}),
            ("design", "Next quarter's export holds 40 lakh orders, and Anand wants all 40 segment-and-month groups every Monday. Filtering the export once per group and totalling each group reads how many rows, against one pass by key?",
             ["16 crore rows against 40 lakh, so one pass by key takes over",
              "40 lakh either way, since each group's total reads only its own rows",
              "16 crore against 40 lakh, and filtering stays, since each group is easy to check",
              "1,600 rows against 200, the same gap as on today's file"], "a",
             "Each filter reads the whole export, 40 times over, where one pass reads it once and fills every group: the fact the chapter named for switching.",
             {"b": "True only once something has split the rows by group, which is itself a pass by key.", "c": "One pass by key checks just as well group by group, and it reads the export once.", "d": "That is today's 200-row file, where speed decides nothing."}),
            ("scenario", "Anand's summary table shows a blank for Q1 orders per customer, although calling the helper on its own in a cell shows 1.65 under it. What went wrong?",
             ["The table was filled before the helper ran, so it still holds an old blank",
              "The helper rounds 1.652 to 1.65, and the table will not take a rounded value",
              "The helper printed its answer and returned nothing, so the table got None",
              "The helper returned from inside its loop, before the last order was counted"], "c",
             "print shows the value and hands back None, and a table built from the call holds None, which shows as a blank.",
             {"a": "Rerunning the table would fix that, and the blank stays.", "b": "A table holds any number, rounded or not.", "d": "An early return hands back a wrong number, never a blank."}),
            ("scenario", "Averaged over the four segments, orders per customer reads 1.94 then 1.82, a fall of 6.0 percent. The four segments hold 69 customers, who placed 114 orders in Q1 and 86 in Q2. What does the roll-up with weights give?",
             ["1.94 to 1.82, since the weights cancel out once all four segments are counted",
              "1.65 to 1.25, a fall of 24.6 percent, so frequency is the branch after all",
              "1.65 to 1.25, a fall of 32.0 percent, measured against the Q2 figure",
              "0.61 to 0.80, total customers over total orders in each quarter"], "b",
             "Total orders over total customers weights each segment by its customers: 114 over 69 and 86 over 69, minus 24.6 percent, which reproduces chapter 2.",
             {"a": "Weights cancel only when every segment is the same size.", "c": "32.0 is the change measured against Q2.", "d": "That is the reciprocal, customers per order."}),
            ("scenario", "Business revenue fell Rs 22,29,720 on three fewer orders. `describe` shows the median Business order barely moved while the range rose about 73 percent. What do you say about the typical Business order?",
             ["It held: one very large order stretched the range; the fall is three fewer orders",
              "It grew, since a range up 73 percent means the middle of the orders moved up too",
              "It shrank, since revenue fell by Rs 22 lakh while the count moved by only three",
              "It is the mean here, since a median ignores the lakh-sized orders that matter most"], "a",
             "The median is the typical order and barely moved; the range is set by the two extreme orders, and one very large order widened it; the rupee fall is three orders worth lakhs each.",
             {"b": "It reads a spread as a level.", "c": "Three orders at about Rs 10 lakh each are about Rs 30 lakh, so the count carries the fall.", "d": "The mean is what one large order pulls; the median is the typical order."}),
            ("scenario", "Anand asks for the company's orders per customer rolled up from the four segments. Order the steps: p) divide total orders by total customers, q) compute each segment's orders and customers in each quarter, r) check the result against chapter 2's 1.65 and 1.25, s) add the segments' orders and their customers. Which order is right?",
             ["q, p, s, r",
              "s, q, p, r",
              "q, s, r, p",
              "q, s, p, r"], "d",
             "Compute each segment's counts, add them, divide the totals, then check the roll-up reproduces the company figure.",
             {"a": "Divides before there are totals to divide.", "b": "Adds counts that have not been computed yet.", "c": "Checks a result before it exists."}),
        ],
    },
    4: {
        "slug": "ch4_mix_or_rate",
        "title": "Chapter 4 scenario set: mix or rate",
        "ask": "\"Revenue per order is up 18 percent. Our customers are happy to pay more. Put a price rise into the plan.\" (the marketing lead)",
        "table": """| Segment | Share of orders Q1, Q2 | Revenue per order Q1 | Revenue per order Q2 |
|---|---|---|---|
| Retail-Core | 33.3%, 41.9% | Rs 2,117 | Rs 2,014 |
| Retail-Plus | 44.7%, 30.2% | Rs 2,815 | Rs 3,012 |
| Business | 17.5%, 19.8% | Rs 10,38,559 | Rs 10,90,674 |
| Student | 4.4%, 8.1% | Rs 962 | Rs 1,104 |
| All orders | 114, 86 orders | Rs 1,84,211 | Rs 2,17,442 |""",
        "picture": """flowchart LR
    A["<b>Q1</b><br/>Rs 1,84,211"] --> M["<b>mix</b><br/>?"]
    M --> R["<b>rate</b><br/>?"]
    R --> D["<b>Q2</b><br/>Rs 2,17,442"]""",
        "items": [
            ("scenario", "Which reading of the table answers Marketing's price claim?",
             ["Business rose 5.0 percent, so prices across the range can safely rise 5 percent",
              "No segment rose 18 percent, so small member orders leaving the blend explain it",
              "Student rose 14.8 percent, so the students' higher prices explain the blended rise",
              "Retail-Core fell 4.9 percent, so its prices should be cut to win the orders back"], "b",
             "The blend rose 18.0 percent while no segment rose that far, because Retail-Plus's small orders fell from 44.7 to 30.2 percent of orders and Business's lakh-sized ones rose to 19.8 percent.",
             {"a": "Business's own rise is 5 percent on its own orders and says nothing for consumer prices.", "c": "Student is 8 percent of orders at about a thousand rupees each; it cannot move a blend of lakhs.", "d": "A fall inside Retail-Core says nothing about the blend's rise."}),
            ("design", "Match each question to the reading that answers it: 1 how big is the rise, 2 did any segment pay more, 3 how much of the rise is mix, 4 what is a typical order; P the per-segment rates, Q the medians, R the blended change, S the mix-and-rate split. Which pairing holds?",
             ["1R 2S 3P 4Q",
              "1S 2P 3R 4Q",
              "1R 2P 3S 4Q",
              "1R 2P 3Q 4S"], "c",
             "The blend gives the size, the per-segment rates say whether anyone paid more, the split puts rupees on the mix, and the median is the typical order.",
             {"a": "The split cannot say whether a given segment paid more, and the rates cannot size the mix.", "b": "The size of the rise is the blend itself, not the split.", "d": "A median cannot size the mix, and the split says nothing of a typical order."}),
            ("design", "Which fact would make the per-segment table enough without a mix split?",
             ["A rise in revenue per order larger than the 18 percent seen this quarter",
              "Segments whose own rates all moved by less than the blend did",
              "Four segments instead of two",
              "Segments with similar order sizes, or shares that held still"], "d",
             "Mix moves the blend only when segments differ in size and their shares move; without either, the per-segment rates are the whole story.",
             {"a": "A bigger rise still needs splitting.", "b": "That is this quarter, where the split was needed to put rupees on the gap.", "c": "The number of segments does not decide whether mix matters."}),
            ("design", "Price Q2's order mix at each segment's Q1 revenue per order, using the table. What does revenue per order come to, and how much of the Rs 33,231 rise is mix?",
             ["Rs 2,07,112, so the mix is Rs 22,902 of the rise, about 69 percent",
              "Rs 2,07,112, so the mix is Rs 10,330 of the rise, about 31 percent",
              "Rs 1,93,414, so the mix is Rs 9,203 of the rise, about 28 percent",
              "Rs 2,17,442, so the mix is all Rs 33,231 of the rise, every rupee"], "a",
             "Business's share rose from 17.5 to 19.8 percent at about Rs 10.4 lakh an order, which lifts the blend to Rs 2,07,112 with no segment's rate moving: Rs 22,902 of the Rs 33,231 rise.",
             {"b": "Rs 10,330 is the rest, the rate part.", "c": "That prices Q1's mix at Q2's rates, which isolates the rate part.", "d": "Rs 2,17,442 is Q2's actual figure, mix and rate together."}),
            ("scenario", "The rate part of the rise, what is left once the mix is priced, splits by segment. Which segment carries most of it, and why does that matter for the price rise?",
             ["Retail-Plus, so members did pay noticeably more for each order they placed",
              "Business, since its lakh-sized orders dominate the rate part",
              "Retail-Core, so everyday shoppers carry the rise",
              "Student, whose rate rose most in percentage terms"], "b",
             "Business's 17 orders each grew about Rs 52,000 on average, so almost all of the rate part is Business, and the consumer segments moved by a few hundred rupees at most.",
             {"a": "Retail-Plus's rise is about Rs 200 an order on 30 percent of orders, about Rs 60 of the rate part.", "c": "Retail-Core's rate fell.", "d": "The largest percentage sits on the smallest orders, about Rs 11 of the rate part."}),
            ("design", "The envelope route treats Kalpa as two groups: Business's share of orders rose from 17.5 to 19.8 percent, and a Q1 Business order was worth Rs 10,36,125 more than a consumer order. What does it put on the mix, and what does that show?",
             ["About Rs 23,000, within 1 percent of the split, so the call holds however it is cut",
              "About Rs 23,000, so the four-segment split was out by Rs 137 and needs correcting",
              "About Rs 2,300, since a 2.2-point move in share moves the blend 2.2 percent at most",
              "All Rs 33,231, since only Business's share moved while the consumer prices held"], "a",
             "0.022 times Rs 10,36,125 is about Rs 23,000, against Rs 22,902 from four segments: an independent route that could have disagreed lands within one percent.",
             {"b": "The routes differ by what the consumer segments' own mix does, so a small gap is expected and is no error.", "c": "The share change multiplies a gap of lakhs per order, not the blend.", "d": "The rate part, Rs 10,330, is Business's own orders growing, which the envelope leaves out."}),
        ],
    },
    5: {
        "slug": "ch5_marketings_hypothesis",
        "title": "Chapter 5 scenario set: Marketing's hypothesis",
        "ask": "\"A flat count can hide churn replaced by new customers. And Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall.\" (the marketing lead)",
        "table": """| Measure | Value |
|---|---|
| Customer ids in Q1, in Q2 | 69, 69 |
| Customers who placed fewer orders in Q2 | 23 |
| Consumer revenue, Q1 to Q2 | Rs 2,28,820 to Rs 1,58,540 |
| Business revenue fall | Rs 22,29,720 on 3 fewer orders |""",
        "picture": """flowchart LR
    A["<b>Marketing's claim</b><br/>a flat count hides churn"] --> B["<b>Marketing's ask</b><br/>Rs 12 crore for acquisition"]""",
        "items": [
            ("design", "Which test answers \"a flat count hides churn replaced by new customers\" most directly, and what would make you distrust it?",
             ["Count each quarter's customers by segment; a segment whose definition changed",
              "Ask Marketing's CRM for sign-ups by month; a campaign that ran in both quarters",
              "Compare the ids in both quarters, only in Q1 and only in Q2; one person with two ids",
              "Compare the counts under a new definition of customer; a customer who changed segment"], "c",
             "Only a comparison of ids names lost and new separately, since any count is net; and if the store and the app gave one person two ids, the comparison would invent churn until the ids were joined.",
             {"a": "A count per segment is still net inside each segment.", "b": "Sign-ups see new customers only, from a second system.", "d": "Another count is still net."}),
            ("design", "Three numbers already answer Marketing's churn claim. When does a table of all 69 customers, one row each, become the better fit?",
             ["When the next question is who slowed, which three counts cannot name",
              "When the export holds more than a few hundred customers in a quarter",
              "When Marketing wants the result in rupees rather than in customers",
              "When the ids come from two systems that each number customers apart"], "a",
             "The three numbers settle lost and new; the next question, who is buying less, needs each customer's orders side by side.",
             {"b": "A larger file makes the table longer to read and changes nothing about which question it answers.", "c": "Rupees need order values, which neither test reads.", "d": "Split ids break both tests; they need joining through the CRM first."}),
            ("scenario", "Marketing concedes that nobody left, then adds: \"23 customers ordered less, and that is churn in all but name.\" Which reply holds?",
             ["They are right: a customer who orders less is halfway gone, so acquisition gets funded",
              "Buying less is frequency: all 23 bought in Q2, so the lever is keeping them buying",
              "Split the 23 by segment first, since churn hides inside segments until they are split",
              "Leave the 23 out of the customer count, since customers who slow down distort it"], "b",
             "Churn is a customer who stops buying, and all 23 bought in both quarters; buying less is the frequency branch, which retention work moves and new customers do not.",
             {"a": "A customer who still buys has not churned, and acquisition adds new people rather than bringing the 23 back to their old pace.", "c": "Splitting by segment says where the slowing sits and leaves it slowing, which is still frequency.", "d": "The 23 are customers in both quarters; dropping them changes the count and hides the fall."}),
            ("scenario", "Last quarter's script prints `summary: {'Retail-Core': -5.3, 'Business': -15.0}` because `pct_change` returns a value only when the change is 30 percent or less. Which fix to the logic keeps every segment in Meera's summary?",
             ["Raise the threshold to 50 percent, so that fewer of the changes print",
              "Print the change as well as returning it, so both appear on the screen",
              "Filter with `if ch < 0`, so that a None is compared with zero as well",
              "Always hand back a number, and mark large changes in a separate column"], "d",
             "A function that always returns its number keeps every segment, and the flag stops depending on whether a value came back.",
             {"a": "A larger change would still vanish.", "b": "It still returns None past the threshold.", "c": "Comparing None with a number raises an error in Python 3."}),
            ("scenario", "Marketing says Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall, so it does not matter. Using the table, which reply holds?",
             ["They are right in rupees, so the memo leads with Business and footnotes the tier",
              "Retail-Plus is 93 percent of the consumer business's Rs 70,280 fall",
              "The tier is 49 percent of the fall, since its orders per member fell 49 percent",
              "The tier is 3 percent of the fall, so the reorder complaint can wait a quarter"], "b",
             "Business orders run to lakhs, so a consumer segment is judged against the consumer business: Rs 65,250 of the Rs 70,280 fall, 93 percent.",
             {"a": "The Business rupees rest on three orders, and the behaviour sits in the tier.", "c": "A fall in a rate is not a share of the rupee fall.", "d": "Judged against the whole company, a consumer segment always looks small."}),
            ("design", "The second route took each customer's first and last order date in the export and counted who first ordered in Q2 or last ordered in Q1: 0 and 0. What does it add, and where does it stop?",
             ["Nothing new, since it reads the same 69 ids the first route already compared",
              "It proves that no customer has left Kalpa since the business opened",
              "It shows which customers slowed, which the overlap cannot see",
              "The same 0 and 0 from dates alone; new still means new since 1 April"], "d",
             "It reaches the overlap's answer without the quarter field or set arithmetic, so it could have disagreed; a first order in the export is only the first since 1 April.",
             {"a": "It reads dates, not the quarter field, so a mislabelled quarter would split the two routes.", "b": "The export covers two quarters.", "c": "Who slowed needs order counts per customer, option C."}),
        ],
    },
    6: {
        "slug": "ch6_the_memo",
        "title": "Chapter 6 scenario set: the memo and its evidence",
        "ask": "\"It is the broken reorder button. One of my members says it has been broken for six weeks.\" (the head of Retail-Plus)",
        "table": """| Retail-Plus window | Days | Orders | Orders per week |
|---|---|---|---|
| Q1, 1 Apr to 30 Jun | 91 | 51 | 3.92 |
| Q2, 1 Jul to 24 Aug | 55 | 18 | 2.29 |
| Q2, 25 Aug to 30 Sep | 37 | 8 | 1.51 |""",
        "picture": """flowchart LR
    A["<b>1 Apr</b><br/>Q1 opens"] --> B["<b>1 Jul</b><br/>Q2 opens"]
    B --> C["<b>25 Aug</b><br/>the button breaks"]
    C --> D["<b>30 Sep</b><br/>Q2 closes"]""",
        "items": [
            ("design", "The memo is due tonight. Four tests are on the table: A, before and after the break (the tier's 77 orders, minutes); B, Retail-Core as a comparison (151 orders, minutes); C, the tier by channel (77 orders, minutes); D, the app's reorder logs (a request, days away). Which plan fits?",
             ["D first, since it settles the question, then A to C if the logs run late",
              "A alone, since timing already shows the fall began before the break",
              "A, B and C tonight in that order, and the request for D sent today",
              "B, C and D, since the complaint already dates the break for us"], "c",
             "Each cheap test can rule a cause in or out tonight from the export already open, timing first since a cause cannot come after its effect; only the logs settle it, so they are requested now rather than waited for.",
             {"a": "The memo waits days while three tests sit unrun.", "b": "Timing caps the button and says nothing of the season or the channel.", "d": "The complaint gives a date; testing it against the fall's timing is the first test."}),
            ("scenario", "The hurried memo says the button cost 25 orders and Rs 65,250. What is wrong with the figure?",
             ["It uses booked orders instead of the delivered orders the board pack counts",
              "It should be measured in members, 22 in both quarters, and not in orders",
              "It counts only the 13 and 8 app orders, leaving out the web and the store",
              "It charges the button with about eight weeks of losses from before it broke"], "d",
             "Q1 against all of Q2 includes 1 July to 24 August, when the rate had already fallen to 2.29 a week.",
             {"a": "The definition is consistent across both quarters.", "b": "Orders are the right unit for a reorder button, and the members did not change.", "c": "It counts every channel."}),
            ("design", "The tier placed 18 orders in the 55 days before the break and 8 in the 37 days after it. At most how many orders can the button explain?",
             ["About 10, since 18 orders came before the break and 8 came after it",
              "About 4: the pre-break pace gives about 12.1 in 37 days, and 8 came",
              "About 25, the tier's whole fall from Q1's 51 orders to Q2's 26",
              "About 12, the 12.1 orders the pre-break pace predicts after the break"], "b",
             "18 in 55 days is 0.327 a day, about 12.1 in the 37 days after the break; the tier placed 8, so about 4.1 is the most the button can explain, and it is a ceiling since anything else still worsening would claim part of it.",
             {"a": "It compares windows of 55 and 37 days, chapter 1's trap.", "c": "It charges the button with the fall that came before it broke.", "d": "12.1 is what was expected, and 8 of those came."}),
            ("scenario", "Retail-Core kept 95 percent of its Q1 orders and Retail-Plus 51 percent. Which cause does this rule out?",
             ["A season that hit every customer alike",
              "Any change in the tier's benefits in July",
              "The reorder button",
              "A monsoon dip that hit members harder"], "a",
             "A season hitting everyone would have moved Retail-Core too; one that hit members harder still fits and needs last year's Q2 by segment.",
             {"b": "A tier change touches members only and fits the pattern.", "c": "The comparison segment says nothing about the button.", "d": "That version of the season survives the test."}),
            ("design", "The memo names two hypotheses. Which pairing of hypothesis and evidence is right?",
             ["The button with the tier's change log, and a July change with the app's reorder logs",
              "The button with Retail-Core's orders by week, and a July change with the tier's channels",
              "The button with the tier's renewals, and a July change with the app's release date",
              "The button with the reorder logs, and a July change with the tier's change log"], "d",
             "Each hypothesis is settled by data the export does not carry, and no two share their evidence.",
             {"a": "The pairs are swapped.", "b": "Both are cuts of this export, which can cap a cause and cannot settle it.", "c": "Renewals and a release date each belong to the other hypothesis."}),
            ("design", "The second route scales the tier's pre-break pace by Retail-Core's own change in pace across the break, 0.946, before comparing with what the tier placed after it. What does it show?",
             ["About 3.5 orders, inside the ceiling, as part of the dip hit Retail-Core too",
              "About 11.5 orders, the button's full cost once the season is taken out",
              "The ceiling was wrong, since the two routes differ by about 0.6 orders",
              "The button explains nothing at all, since Retail-Core also slowed after 25 August"], "a",
             "11.45 expected against 8 placed is about 3.5: an independent correction that lands under the ceiling of about 4, which is what a ceiling predicts.",
             {"b": "11.5 is the corrected expectation, of which 8 came.", "c": "A lower figure from a stricter route is what a ceiling predicts, not an error.", "d": "Retail-Core slowed about 5 percent, far less than the tier."}),
        ],
    },
}

def write_set(n, s):
    letters = "abcd"
    lines = [f"# {s['title']}", "",
             "Ten minutes, alone, then compare with the person beside you before Kavya's review. Every item has",
             "one right answer. Decide first, then record the letter. Items marked design ask for the best-fit",
             "approach, a sizing, the fact that would switch it, or the second route.", "",
             f"Post one line, {len(s['items'])} letters in item order, no spaces:", "", "```",
             "Post exactly this shape: " + "x" * len(s["items"]), "```", "",
             "The ask behind every item:", "", f"> {s['ask']}", "", "The numbers every item refers to, booked orders, the export as it stands:", "",
             s["table"], "", "```mermaid", s["picture"], "```", "", "---", ""]
    for i, (kind, stem, opts, key, why, others) in enumerate(s["items"], 1):
        tag = " (design)" if kind == "design" else ""
        lines += [f"### Q{i}.{tag} {stem}", ""]
        lines += [f"{letters[j]}) {o}" for j, o in enumerate(opts)]
        lines += [""]
    (UNG / f"C2_W01_D02_{s['slug']}_STUDENT.md").write_text("\n".join(lines).rstrip() + "\n")

    answers = " ".join(f"{i}{it[3]}" for i, it in enumerate(s["items"], 1))
    design = sum(1 for it in s["items"] if it[0] == "design")
    sol = [f"# Solution: {s['title'][0].lower() + s['title'][1:]}", "", f"Answers: {answers}", "",
           f"{design} of the {len(s['items'])} items are design items.", "", "## Item by item", "",
           "| Item | Kind | Key | Why it holds | Why the others fail |", "|---|---|---|---|---|"]
    for i, (kind, stem, opts, key, why, others) in enumerate(s["items"], 1):
        rest = " ".join(f"{k}: {v}" for k, v in sorted(others.items()))
        sol.append(f"| {i} | {kind} | {key} | {why} | {rest} |")
    (SOL / f"C2_W01_D02_{s['slug']}_solution_STUDENT.md").write_text("\n".join(sol) + "\n")
    return len(s["items"]), design


if __name__ == "__main__":
    total = designs = 0
    for n, s in SETS.items():
        a, b = write_set(n, s)
        total += a
        designs += b
    print(f"{total} items across six chapter sets, {designs} of them design items")
