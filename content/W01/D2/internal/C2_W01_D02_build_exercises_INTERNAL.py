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
        "table": """| Window | Dates | Weeks | Orders | Revenue |
|---|---|---|---|---|
| Q1, closed | 1 Apr to 30 Jun | 13 | 114 | Rs 2,10,00,000 |
| Q2, closed | 1 Jul to 30 Sep | 13 | 86 | Rs 1,87,00,000 |
| Q2 dashboard tile, cut on 15 September | 1 Jul to 15 Sep | 11 | 70 | Rs 1,55,59,950 |""",
        "picture": """flowchart LR
    A["<b>Q1</b><br/>13 weeks"] --> C{"same window?"}
    B["<b>Q2 tile</b><br/>11 weeks"] --> C
    C -->|"no"| D["match the weeks<br/>or use a rate"]
    C -->|"yes"| E["compute the change"]""",
        "items": [
            ("scenario", "Meera asks how far revenue fell between the two closed quarters. Which figure goes in the reply?",
             ["12.3 percent, the Rs 23,00,000 gap measured against Q2's total",
              "9.5 percent, from the rounded Rs 1.9 crore against Rs 2.1 crore",
              "11.0 percent, the Rs 23,00,000 gap against Q1's total",
              "25.9 percent, the figure on the dashboard tile Marketing quotes"], "c",
             "The change is measured against the starting quarter: Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent, on two closed windows of 13 weeks.",
             {"a": "Measuring against Q2 inflates the fall to 12.3 percent.", "b": "The rounded crore figures lose Rs 3,00,000 of the gap.", "d": "The tile covers 11 weeks of Q2, so its fall is a window artefact."}),
            ("scenario", "Marketing's slide reads \"Q2 Rs 1,55,59,950 against Q1 Rs 2,10,00,000: revenue fell 25.9 percent.\" What makes the slide unfit to act on?",
             ["The percentage is computed on Q2's total, which overstates the fall",
              "It compares 11 weeks of Q2 against all 13 weeks of Q1",
              "It counts booked orders, where Finance would count delivered ones",
              "It rounds both totals to the nearest lakh before dividing them"], "b",
             "The tile stopped on 15 September, so two weeks of Q2 are missing from one side only, and Rs 12 crore would move on a gap that is mostly the calendar.",
             {"a": "Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is Q1.", "c": "Both sides count booked orders, which is consistent.", "d": "The totals are exact to the rupee."}),
            ("design", "Q2 is still open on 15 September and Meera wants a number today. Which comparison is the best fit, and what would switch it?",
             ["The same 11 weeks of each quarter, switching to closed quarters at the close",
              "The tile against all of Q1, switching only once Marketing agrees the method is fair",
              "Q2 to date projected to 13 weeks, switching if the projection misses",
              "Per month, April against July only, switching when August closes"], "a",
             "The same weeks of both quarters control for length and for where in the quarter the weeks sit; the day Q2 closes, closed quarters answer the question directly.",
             {"b": "That is the unmatched comparison that produced 25.9 percent.", "c": "A projection assumes the last two weeks look like the first eleven, which Kalpa's lumpy weeks break.", "d": "One month against one month discards most of both quarters and still mixes seasons."}),
            ("design", "Four options were sized on this file: closed quarters (200 rows, minus 11.0), the same 11 weeks (167 rows, minus 17.0), per day (200 rows, minus 11.9) and last year's Q2 (0 rows, cannot run). Why is speed no reason to choose between them here?",
             ["Because the fastest option is always the least accurate one",
              "Because only last year's Q2 needs any computation at all",
              "Because the option that reads the most rows is always the most accurate one here",
              "Because every option runs in milliseconds, what each one controls for decides"], "d",
             "On 200 rows each option takes well under a millisecond or two; what separates them is what each controls for: length, position in the quarter, or the season.",
             {"a": "Speed and accuracy are unrelated here; the closed quarters are both fast and right.", "b": "Every option computes a change; last year's Q2 cannot run at all.", "c": "Rows read and accuracy are unrelated: the closed quarters and per-day options read the same 200 rows and give different answers."}),
            ("scenario", "Per day, the closed quarters run at Rs 2,30,769 and Rs 2,03,261, a fall of 11.9 percent. Why does this differ from the 11.0 percent on the totals?",
             ["A rate per day always runs higher than a rate on totals, for any windows",
              "Q2 has 92 days and Q1 has 91, so Q2's total spreads over one more day",
              "The per-day rate counts only the days on which an order was placed",
              "One of the two figures has a rounding slip, and the totals are safer"], "b",
             "Q1 runs 1 April to 30 June, 91 days; Q2 runs 1 July to 30 September, 92 days, so per day Q2's total is divided by one more day.",
             {"a": "With equal days the two agree exactly.", "c": "The rate divides by calendar days in the window.", "d": "Both figures are exact; they answer slightly different questions."}),
            ("design", "The second route added revenue by the month in `order_date` and reached the same minus 11.0 percent. What does agreement between the two routes prove?",
             ["That monthly totals are the better headline for Meera than quarters",
              "That no order in the file carries a wrong amount, a duplicate or a missing field",
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
    R["<b>revenue</b><br/>x 0.890"] --> C["<b>customers</b><br/>x 1.000"]
    R --> F["<b>orders per customer</b><br/>x 0.754"]
    R --> V["<b>revenue per order</b><br/>x 1.180"]""",
        "items": [
            ("scenario", "Marketing says the fall needs more customers. Which reading of the tree answers them?",
             ["Customers fell with orders, so acquisition is the branch to fund",
              "Customers held at 69, so the fall sits in how often they buy",
              "Revenue per order rose, so the fall must be in customers",
              "The tree cannot answer until the segments are split"], "b",
             "The count is 69 in both quarters and orders fell from 114 to 86, so orders per customer carries the fall.",
             {"a": "The count did not fall.", "c": "A rise in one leaf says nothing about customers, which are counted directly.", "d": "The tree answers the branch question on totals; segments answer the next one."}),
            ("scenario", "A colleague adds the leaf changes, minus 24.6 percent and plus 18.0 percent, and reports revenue down 6.6 percent. What is wrong?",
             ["Nothing, since percentages on leaves always add to the total change",
              "The customer leaf was left out of the sum, and it carries the missing 4.4 points",
              "Revenue per order should have been subtracted, not added",
              "The leaves multiply, and 0.754 times 1.180 is 0.890, a fall of 11.0 percent"], "d",
             "Revenue is a product of its leaves, so their ratios multiply; adding percentages ignores the part where both moved.",
             {"a": "They add only for tiny changes.", "b": "The customer ratio is 1.000 and contributes nothing.", "c": "The sign of the order-value change is right; the operation is wrong."}),
            ("design", "Meera wants rupees per branch she can follow. Which split is the best fit, and what would switch it?",
             ["A bridge in the tree's order with the order stated, and symmetric if rebuilt monthly",
              "Leaf percentages alone, with a bridge added only if Meera asks for rupees a second time",
              "A symmetric split always, since any order is a bias, and a bridge never",
              "Customer by customer for all 69, with a bridge once the list is read"], "a",
             "The bridge adds exactly to the fall and reads one step at a time; when others rebuild it every month and argue about order, the symmetric split removes the argument.",
             {"b": "Percentages give no rupees, which is what she asked for.", "c": "The symmetric split is harder to explain and the bridge's order never changes the verdict here.", "d": "Reading 69 rows first delays the answer; it is the option for who slowed."}),
            ("design", "Moving frequency first charges it Rs 51,57,895; moving it second charges Rs 60,88,372; the symmetric split says Rs 55,88,480. What does the spread of about Rs 9.3 lakh measure?",
             ["An error in one of the three computations",
              "The discount branch, which the bridge leaves out",
              "The part where frequency and order value moved together",
              "The rupees Marketing's customer branch should really carry"], "c",
             "Whichever leaf moves second is charged for the joint part; all three splits add to the same Rs 23,00,000.",
             {"a": "All three are exact and land on the fall.", "b": "Discounts sit inside revenue per order and are bounded at Rs 12,900.", "d": "The customer branch is zero in every order."}),
            ("scenario", "A hurried count reads every missing discount as zero and finds 43 of Q2's 86 orders \"without a discount\". Marketing wants the discount extended to them. Why is the premise unsafe?",
             ["The count should have used Q1, which has more orders",
              "Discounts belong to Finance, so Marketing cannot extend them without sign-off",
              "Only orders above Rs 150 can carry a discount",
              "Only 17 of the 43 record Rs 0, and the other 26 never recorded the field"], "d",
             "A blank is unknown; treating it as zero files 26 unknown orders under \"no discount\", and the extension spends margin on orders that may already carry one.",
             {"a": "The quarter is not the issue; the blanks are.", "b": "Ownership does not make the share right.", "c": "Rs 150 is the largest recorded discount, not a threshold."}),
            ("design", "The second route priced the 28 lost orders at Q1's Rs 1,84,211 and matched the bridge's frequency step to the rupee. When would this route stop matching?",
             ["When customers move as well, since lost orders then mix both branches",
              "When revenue per order changes, since the price of each order then moves as well",
              "When a discount field is missing on some orders",
              "When the quarters have different numbers of days"], "a",
             "The direct count equals the frequency step only because the customer count held; once customers move, some lost orders belong to the customer branch.",
             {"b": "Revenue per order changed here too, and the routes still agreed.", "c": "Discounts do not enter either route.", "d": "Both routes use the same closed quarters."}),
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
            ("design", "The same five numbers are needed for four segments in two quarters, then for a channel and for delivered orders later today. Which is the best fit?",
             ["Paste the loop once per group, since eight copies are quick to type",
              "One pass grouped by (quarter, segment), since it reads fewest rows",
              "A spreadsheet, since the groups are few enough to read by eye",
              "A function `tree_for(rows)`, since any later subset is one call"], "d",
             "One place holds the definitions, so a change reaches every group, and any subset asked later is a single line.",
             {"a": "Eight copies mean eight edits when the definition changes, and one gets missed.", "b": "One pass wins on a huge file; here it is shaped for these eight groups only.", "c": "It moves the work out of the pipeline the rest of the week builds on."}),
            ("design", "Which fact would switch the call from a function to one pass grouped by key?",
             ["Millions of rows with every group needed at once",
              "A definition that changes once a quarter",
              "A stakeholder who asks for one segment at a time",
              "A file of 200 orders with four segments"], "a",
             "On a large file, reading the rows once instead of once per group is what matters; that is `groupby` in Week 2.",
             {"b": "Changing definitions favour the function.", "c": "Groups asked one at a time favour the function.", "d": "That is today's file, where the function wins."}),
            ("scenario", "Anand's summary table shows a blank for Q1 orders per customer, though the helper printed 1.65 on screen. What went wrong?",
             ["The rows list was empty, so the division failed silently",
              "The function computed the wrong rate for that quarter",
              "The function printed its answer and returned nothing",
              "Python rounds a float to None when it prints it"], "c",
             "A function without `return` hands back `None`; the screen looked right and the caller got nothing.",
             {"a": "An empty list would raise a division error.", "b": "1.65 is the right Q1 figure.", "d": "Printing never changes a value."}),
            ("scenario", "Averaged over the four segments, orders per customer reads 1.94 then 1.82, a fall of 6.0 percent. A colleague says frequency is not the branch after all. What is the check?",
             ["Recompute the averages to three decimal places",
              "The roll-up must reproduce the company figures, 1.65 and 1.25",
              "Drop the smallest segment and average the other three segments again",
              "Compare the medians of the four segments instead"], "b",
             "Averaging gives a 2-customer segment the vote of a 34-customer one; total orders over total customers must give 114 over 69 and 86 over 69.",
             {"a": "More decimals of a wrong roll-up stay wrong.", "c": "Dropping groups hides the weighting problem.", "d": "Medians of rates share the same flaw."}),
            ("scenario", "Business revenue fell Rs 22,29,720. `describe` shows the median order barely moved while the range rose about 73 percent. What do you say about the typical Business order?",
             ["The typical order held, while one large order stretched the range",
              "Every Business order got smaller, which is why Business revenue fell",
              "The typical order grew sharply, so Business customers spend more",
              "Nothing can be said until the mean is computed"], "a",
             "The median moved from Rs 9,83,780 to Rs 9,52,000, while one order of Rs 29,45,460 set the range; the fall is three fewer orders.",
             {"b": "The median held.", "c": "The range grew, not the typical order.", "d": "The mean is the number one order moves most."}),
            ("design", "The second route, one pass grouped by (quarter, segment), agreed with `tree_for` on all eight groups. When would you make it the main route?",
             ["When a stakeholder asks for one segment at a time",
              "When the definition of a customer is about to change next quarter",
              "When the file holds 200 orders across four segments",
              "When every group is needed at once from millions of rows"], "d",
             "Reading the rows once instead of once per group matters on a large file when every group is wanted together.",
             {"a": "Groups asked one at a time favour the function.", "b": "A changing definition favours one function holding it.", "c": "On 200 rows the function costs nothing extra."}),
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
             ["No segment rose 18 percent, because small member orders left the blend",
              "Business rose 5.0 percent, so prices across the range can safely rise 5 percent",
              "Student rose 14.8 percent, so the young pay more",
              "Retail-Core fell, so its prices should be cut"], "a",
             "The blend rose while no segment did, because Retail-Plus's small orders fell from 44.7 to 30.2 percent of orders.",
             {"b": "Business's rise rests on one large order and says nothing about a range-wide price.", "c": "Student's figure rests on 12 orders.", "d": "A 4.9 percent dip on small orders is not a pricing finding."}),
            ("design", "Match each question to the reading that answers it: 1 how big is the rise, 2 did any segment pay more, 3 how much of the rise is mix, 4 what is a typical order; P the blended change, Q per-segment rates, R the mix-and-rate split, S medians. Which pairing holds?",
             ["1P 2R 3Q 4S", "1Q 2P 3R 4S", "1P 2Q 3R 4S", "1S 2Q 3R 4P"], "c",
             "The blend gives the size, the per-segment rates say whether any segment paid more, only the split puts rupees on mix, and medians give the typical order.",
             {"a": "Swaps the split and the per-segment rates.", "b": "Swaps the blend and the per-segment rates.", "d": "Swaps the blend and the medians."}),
            ("design", "Which fact would make the per-segment table enough without a mix split?",
             ["A rise in revenue per order larger than the 18 percent seen this quarter",
              "A segment whose rate fell while the blend rose",
              "Four segments instead of two",
              "Segments with similar order sizes, or shares that held still"], "d",
             "Mix moves a blend only when segments differ in rate and their shares move; without both, the blend tracks the segments.",
             {"a": "The size of the rise does not decide it.", "b": "That is exactly when a split is needed.", "c": "The count of segments does not decide it."}),
            ("scenario", "At Q2's mix and Q1's segment rates, revenue per order would be Rs 2,07,112. How much of the Rs 33,231 rise is mix?",
             ["Rs 10,330, the part inside segments",
              "Rs 22,902, about 69 percent",
              "Rs 33,231, all of it",
              "Rs 2,07,112, the counterfactual itself"], "b",
             "Rs 2,07,112 less Rs 1,84,211 is Rs 22,902, and the rest, Rs 10,330, is the rate inside segments.",
             {"a": "That is the rate part.", "c": "The rate part is not zero.", "d": "That is a level, not a change."}),
            ("scenario", "The rate part, Rs 10,330, splits by segment. Which segment carries most of it, and why does that matter for the price rise?",
             ["Retail-Plus, so members did pay noticeably more for each order they placed",
              "Retail-Core, so everyday shoppers carry the rise",
              "Business, since its lakh-sized orders dominate the rate part",
              "Student, whose rate rose most in percentage terms"], "c",
             "More than nine tenths of the rate part is Business, so there is no range-wide price signal to act on.",
             {"a": "Members' orders grew by about Rs 200 on 26 orders, a small share.", "b": "Retail-Core's rate fell.", "d": "Student's orders are tiny in rupees."}),
            ("design", "Moving the rate first gives mix Rs 24,028 instead of Rs 22,902. What does the second route confirm?",
             ["Both orders add to Rs 33,231, and mix stays above two thirds",
              "The first split had an arithmetic error of Rs 1,126 in its mix part",
              "The rate-first order is the correct one to report",
              "Mix and rate cannot be separated on this file"], "a",
             "The joint part moves to whichever goes second, so the parts shift slightly while the sum and the verdict hold.",
             {"b": "Both splits are exact.", "c": "Either order is honest if it is stated.", "d": "The split separated them in both orders."}),
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
    A["<b>Q1 ids</b>"] --> O["<b>overlap</b><br/>both, only Q1, only Q2"]
    B["<b>Q2 ids</b>"] --> O""",
        "items": [
            ("design", "Which test answers \"a flat count hides churn replaced by new customers\" most directly?",
             ["Compare the counts again with a different definition of customer",
              "Ask Marketing's CRM for new sign-ups by month",
              "The overlap of ids, counting both quarters, only Q1 and only Q2",
              "Average the orders per customer across segments"], "c",
             "The overlap names lost and new separately in three numbers anyone can rerun.",
             {"a": "Any count is net.", "b": "The CRM sees only new sign-ups, from a second system.", "d": "That measures frequency, and averaging it is wrong besides."}),
            ("design", "What would make you distrust the id overlap?",
             ["One person holding two ids, one from the store and one from the app",
              "A quarter holding many more orders than the other quarter in the file",
              "A segment with only two customers",
              "An export with 200 rows instead of 2,000"], "a",
             "Split identities make one customer look lost and new at once, which invents churn; the ids would need joining first.",
             {"b": "Order counts do not touch the overlap.", "c": "Segment size does not change identity.", "d": "Size does not change what an id means."}),
            ("scenario", "The overlap comes out 69 in both quarters, 0 only in Q1, 0 only in Q2. What goes back to Marketing?",
             ["Churn is hidden in the segments, so split them first and run the overlap per segment",
              "Nobody was lost and nobody was new, so acquisition has nothing to replace",
              "The flat count proves customers are loyal, so no action is needed",
              "The overlap is inconclusive until Thursday's test"], "b",
             "Every Q2 customer bought in Q1; the fall is how often the same people buy.",
             {"a": "The overlap already covers every segment's ids.", "c": "Frequency fell 24.6 percent, so action is needed on a different lever.", "d": "The overlap is a count, not a sample estimate."}),
            ("scenario", "Last quarter's script prints `summary: {'Retail-Core': -5.3, 'Business': -15.0}` because `pct_change` returns a value only when the change is 30 percent or less. Which fix to the logic keeps every segment in Meera's summary?",
             ["Raise the threshold to 50 percent, so that fewer of the changes print",
              "Print the change as well as returning it, so both appear on the screen",
              "Filter with `if ch < 0`, so that a None is compared with zero as well",
              "Return the change every time, and put the flag in a column of its own"], "d",
             "A helper that always returns the same type cannot drop a group; the flag keeps the warning without losing the number.",
             {"a": "A 49 percent fall still passes 50 only by luck, and the bug stays.", "b": "The large moves still return nothing.", "c": "Comparing None with zero raises a TypeError, and the logic is unchanged."}),
            ("scenario", "Marketing says Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall, so it does not matter. Which reply holds?",
             ["They are right: 3 percent of the fall is noise and can be left out of the note",
              "Retail-Plus is 93 percent of the consumer fall and 25 of the 28 lost orders",
              "Business should be dropped from the file as an outlier",
              "Rupees never matter, since only orders count"], "b",
             "Business orders run to lakhs, so a consumer segment is judged against the consumer business: Rs 65,250 of Rs 70,280.",
             {"a": "The comparison mixes lakh-sized and thousand-sized orders.", "c": "Business is real revenue and stays; it gets its own caveat.", "d": "Both lenses matter, each with its count."}),
            ("design", "The second route found the consumer fall by subtracting Business from the company fall. When is the bridge by segment the better route?",
             ["When the question is which consumer segment moved",
              "When the numbers involved run to crores of rupees",
              "When Business is the largest segment in rupees",
              "When the two quarters being compared are of unequal length"], "a",
             "Subtraction reaches the total fast and hides who moved; the bridge shows each segment.",
             {"b": "Size does not decide the route.", "c": "That is true here and is why the consumer view is needed at all.", "d": "Unequal windows are chapter 1's problem, fixed before either route."}),
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
    Q1["<b>Q1</b><br/>3.92 a week"] --> B["<b>before the break</b><br/>2.29 a week"]
    B --> A["<b>after the break</b><br/>1.51 a week"]""",
        "items": [
            ("design", "Four tests of the button were on the table. In which order do you run them?",
             ["The app's logs first, since they settle it and the other tests can wait for them",
              "Timing, then a comparison segment, then the channel, with the logs requested now",
              "The channel first, since the cause is an app feature",
              "All four at once, since order does not matter"], "b",
             "Timing is cheap and can rule a cause out outright; the logs settle it but are days away, so the request goes in today.",
             {"a": "Waiting for the logs leaves the cheap tests unrun.", "c": "The channel test is useful, and timing can end the question sooner.", "d": "One of the four is a data request that cannot run today."}),
            ("scenario", "The hurried memo says the button cost 25 orders and Rs 65,250. What is wrong with the figure?",
             ["It uses booked orders instead of the delivered orders the board pack reports",
              "It should be measured in customers, not orders",
              "It counts only app orders",
              "It charges the button with seven weeks of losses from before it broke"], "d",
             "Q1 against all of Q2 includes 1 July to 24 August, when the rate had already fallen to 2.29 a week.",
             {"a": "The definition is consistent across both quarters.", "b": "Orders are the right unit for a reorder button.", "c": "It counts every channel."}),
            ("scenario", "At the pre-break pace, the 37 days after the break would have carried about 12.1 orders, and the tier placed 8. What goes in the memo?",
             ["The button caused the whole fall, now proven",
              "The button had no effect at all, since most of the fall came before it broke",
              "The button explains at most about 4 orders, so the rest needs another cause",
              "The fall is too small to report"], "c",
             "About 4 orders is a ceiling, since anything else still worsening would claim part of it.",
             {"a": "Most of the fall came before the break.", "b": "The after-break rate did fall further, so an effect is possible.", "d": "The tier halved; the ceiling is small, not the fall."}),
            ("scenario", "Retail-Core kept 95 percent of its Q1 orders and Retail-Plus 51 percent. Which cause does this rule out?",
             ["A season that hit every customer alike",
              "Any change in the tier's benefits in July",
              "The reorder button",
              "A monsoon dip that hit members harder"], "a",
             "A season hitting everyone would have moved Retail-Core too; one that hit members harder still fits and needs last year's Q2 by segment.",
             {"b": "A tier change touches members only and fits the pattern.", "c": "The comparison segment says nothing about the button.", "d": "That version of the season survives the test."}),
            ("design", "The memo names two hypotheses. Which pairing of hypothesis and evidence is right?",
             ["The button with the tier's change log, and a July change with the app's reorder logs",
              "Both with this export, cut another way",
              "The button with Marketing's campaign reach, and a July change with the export",
              "The button with the reorder logs, and a July change with the tier's change log"], "d",
             "Each hypothesis is settled by data the export does not carry, and no two share their evidence.",
             {"a": "The pairs are swapped.", "b": "The export raised the question and cannot settle a cause.", "c": "Campaign reach measures acquisition, which chapter 5 ruled out."}),
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
