# R1: Teaching patterns to borrow for Week 4

Prepared 12 October 2026 for the Week 4 planning council (INTERNAL). Every URL below was fetched today and carries "(checked 12 October 2026)". Section 7 lists what would not load and what has moved. We borrow structure and ideas only; no text or image from any source goes into a pack.

## 1. What to steal, in ten lines

1. One running database, introduced once with a printed map and reused on every page (mysqltutorial.org). Kalpa is that database already; it lacks the printed map and the table card shown at the moment a table enters.
2. A picture that grows by one box per page: mysqltutorial's clause-order strip goes from two boxes on SELECT FROM to seven on GROUP BY. Week 4 can grow one diagram across its five days.
3. Toy table first, real table second: mysqltutorial builds two tiny tables before any join touches the real database; StatQuest and Setosa teach conditional probability on countable dots.
4. A hub page that previews its spokes with one example each, then a page per spoke (mysqltutorial's WHERE page).
5. Edge cases and "X against Y" comparisons come last, and two to four summary bullets close every page.
6. Three numbered questions boxed on the board as the explainer's agenda (IBM Technology's Monte Carlo and supervised-learning boards; the time series video's description opens on three questions).
7. An everyday object or scene carries the idea: a smartwatch for time series, a phone and a coffee cup for customer data, an ice-cream shop's opening banner for feature flags (IBM Technology).
8. Hypotheses listed and ordered before the data opens, with the answer key on a separate page (the Yammer cases, now hosted by ThoughtSpot).
9. Every baseline drawn on the same series with the same axes, one method per panel, then a scoreboard (Forecasting: Principles and Practice).
10. Compression as a ladder: a three-minute story, then a one-sentence Big Idea, then the slide (Storytelling with Data).

## 2. mysqltutorial.org: how it layers and why it feels connected

### 2.1 What was read

https://www.mysqltutorial.org/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/ (checked 12 October 2026)
https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/mysql-select-from/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/mysql-order-by/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/mysql-where/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/mysql-group-by/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/mysql-join/ (checked 12 October 2026)
https://www.mysqltutorial.org/mysql-basics/mysql-inner-join/ (checked 12 October 2026)
https://www.mysqltutorial.org/tryit/ (checked 12 October 2026)

### 2.2 One sample database, printed and reused

The whole site runs on classicmodels, a retailer of scale-model classic cars with eight tables (customers, products, productlines, orders, orderdetails, payments, employees, offices). The sample database page shows the ER diagram, offers it as an A4 PDF and tells the reader to print it and keep it on the desk. Each topic page then names the table it uses and shows that table's schema card just before the first example, never earlier: ORDER BY shows customers first, orderdetails at its third example and orders when the custom sort needs it. The same rows recur from page to page, so outputs become predictable. The TryIt page loads all eight tables into an in-browser editor, and every numbered example on the pages read links to its own runnable query.

### 2.3 Page anatomy, measured

Every topic page runs in one order: a one-line objective, the syntax with placeholders, a numbered reading of the syntax ("First, ... Second, ..."), a small diagram of where the clause runs, numbered examples titled "1) Using X to do Y example", then edge cases and comparisons, then two to four summary bullets. Each example is a goal sentence, the query, the runnable link, the printed result (often marked partial) and one sentence reading it.

| Page | Words, code included | Numbered examples | What closes the page |
|---|---|---|---|
| SELECT FROM | about 640 | 3: one column, several, all | 2 summary bullets |
| ORDER BY | about 1,470 | 3, then a custom sort order and NULL ordering | 4 summary bullets |
| WHERE | about 1,460 | 8, one operator each | 2 summary bullets |
| GROUP BY | about 1,150 | 5: plain grouping up to two columns | MySQL against the SQL standard; GROUP BY against DISTINCT |
| Joins overview | about 1,790 | one per join type, on a two-table toy | inner, left and right joins each drawn as a Venn diagram |
| INNER JOIN | about 900 | two tables, then with GROUP BY, then three, then four | joins on operators other than equality |

Pages take three to eight minutes to read, carry one idea each, and let the examples teach: WHERE holds 26 code blocks (queries and printed results) against about 830 words of prose.

### 2.4 How the sequence layers topics

The Basics index teaches querying, sorting, filtering, joining, grouping, subqueries and set operators before managing tables or modifying data: reading before writing. Inside a section the clause comes before its operators (WHERE, then DISTINCT, AND, OR, IN, BETWEEN, LIKE, LIMIT, IS NULL). The home page splits the site into tracks (getting started, developers, programming interfaces, administrators, functions).

Three devices make it feel connected. The clause-order strip grows, verified from the diagrams themselves: two boxes on SELECT FROM, three on ORDER BY, four on WHERE and seven on GROUP BY, so each page adds its clause to a picture the reader already holds. The hub previews its spokes: WHERE gives one example each of AND, OR, BETWEEN, LIKE, IN and IS NULL, each later a page of its own. And toys come first: ORDER BY computes FIELD('A', 'A', 'B', 'C') = 1 before sorting real orders, and the Joins overview builds two tiny tables (members and committees, overlapping on purpose) before INNER JOIN climbs from two real tables to four.

### 2.5 Patterns to copy into Week 4

| Pattern | What we do with it | Where it lands |
|---|---|---|
| One database, one printed map | An A4 Kalpa v5 map on every desk from Monday | Cheat sheet |
| Table card at entry | order_items at Wednesday's first basket, events on Thursday, revenue on Friday | Deck, notebook first cell |
| Template read in order | The metric definition, the lift formula and the forecast note shown with placeholders, then read line by line | Deck, cheat sheet |
| Growing strip | One week diagram gaining a box a day (section 6) | Each deck's first slide |
| Numbered examples, one change each | Three to eight mini examples per chapter on one table, output shown and read in a line | Notebooks, study notes |
| Toy before real | Ten dots before twelve baskets before order_items; two batches before the event log | Chapter 1 |
| Hub previews spokes | Chapter 1 gives one tiny example of every sub-concept; later chapters deepen each | Deck chapter 1 |
| Comparisons last | Confidence against lift, blended against cohort, fit against forecast | Last chapter, Kahoot |
| Two to four summary bullets | Saturday's crux lines from memory | Every chapter |
| Runnable example | Each example names the notebook cell or companion state that runs it | Decks, study notes |
| Tracks by reader | Interview prep split by the BA, DS and FDE roles the Saturday paper tags | Interview sheet |

## 3. IBM: the topic pages and the lightboard explainers

### 3.1 The Think topic pages

IBM Think pages share one skeleton: "What is X?" with a two-sentence definition, "How X works" as numbered steps, key concepts as subheadings, a taxonomy from simplest to most complex, an "X against Y" section, benefits and limitations, and use cases by industry, in about 2,000 to 3,300 words with few worked numbers. We found no Think page for A/B testing, KPIs, data storytelling, market basket, cohort or funnel analysis, or time series forecasting; the obvious slugs redirect to the topics index and a site search turned up none (checked 12 October 2026). The closest pages:

| Week 4 topic | Best IBM page | What to borrow |
|---|---|---|
| Metrics and north-star | What Are Objectives and Key Results (OKRs)? https://www.ibm.com/think/topics/okrs (checked 12 October 2026) | Its key-result checklist (quantifiable, results over activities, time-bound, two to four per objective) and its OKRs-against-KPIs section |
| A/B testing (faculty block) | Causal Inference https://www.ibm.com/think/topics/causal-inference (checked 12 October 2026) | Its order: potential outcomes, confounders, colliders, the causal graph |
| Data storytelling | What Is Data Visualization? https://www.ibm.com/think/topics/data-visualization (checked 12 October 2026); Bridge the data literacy skills gap with data storytelling https://www.ibm.com/think/insights/bridge-the-data-literacy-skills-gap-with-data-storytelling (checked 12 October 2026) | The four purposes of a visual it takes from Harvard Business Review (idea generation, idea illustration, visual discovery, everyday dataviz); set the context, know the audience, keep it simple |
| Market basket | What is the Apriori algorithm? https://www.ibm.com/think/topics/apriori-algorithm (checked 12 October 2026) | One running example through support, confidence and lift, and use cases across retail, healthcare, web clickstreams and finance. Read 3.2 first |
| Cohorts, funnels, retention | What Is Customer Retention? https://www.ibm.com/think/topics/customer-retention (checked 12 October 2026); What is a Sales Funnel? https://www.ibm.com/think/topics/sales-funnel (checked 12 October 2026) | A retention rate that removes customers acquired in the period before dividing by the starting count, the one-line reason a blend must take new members out; six named funnel stages |
| Forecasting | What Is Forecasting? https://www.ibm.com/think/topics/forecasting (checked 12 October 2026); What is a Time Series Model? https://www.ibm.com/think/topics/time-series-model (checked 12 October 2026) | Six steps (define, gather, select, generate, verify, present) and a method list that opens on the naive forecast as the simplest benchmark |

### 3.2 One caution: the Apriori page's lift arithmetic

The Apriori page runs one example (2,000 transactions; apples in 250, bananas in 500, both in 150) and then divides confidence by the antecedent's support, printing lift 4.8 for apples to bananas and 1.2 for the reverse. Lift divides by the consequent's support and is symmetric: 0.075 / (0.125 x 0.25) = 2.4 both ways. Wednesday's trainer and the association-rules faculty should know this before pointing anyone at the page; it also makes a trainer-side "audit a published explanation" item, re-checked on the day since IBM may correct it. Practical Business Python states lift correctly, as observed support over the support expected under independence: https://pbpython.com/market-basket-analysis.html (checked 12 October 2026).

### 3.3 The IBM Technology explainers

Titles and channel were confirmed through YouTube's oEmbed endpoint, lengths through the channel's search listing. youtube-transcript-api 1.2.4 (in a scratch virtualenv) was refused for every video (IpBlocked) and the watch pages redirected to a captcha, so beat timings were not measurable. The last column reads the finished board in each thumbnail.

| Use | Video | Length | Finished board |
|---|---|---|---|
| Friday | What is Time Series Analysis? https://www.youtube.com/watch?v=GE3JOFwTWVM (checked 12 October 2026) | 7:29 | The presenter points at his smartwatch; mini-charts labelled cycle and variation; "3. Implement" pointing to ARIMA and exponential smoothing; a Python, pandas, matplotlib chain. The description opens on three questions: what a time series is, what analysis it allows, what the results are for |
| Tuesday | Data Visualization Made Simple: Do's & Don'ts for Clear Insights https://www.youtube.com/watch?v=QGDhKyZiPAo (checked 12 October 2026) | 5:38 | Two bar charts with labelled axes, stick-figure pictograms, a numbered "Do" list (simple, know your audience, clear) and a "Don't" list |
| Wednesday | What is an AI Recommendation Engine? https://www.youtube.com/watch?v=gEdePRsDACc (checked 12 October 2026) | 10:53 | Everyday icons (a video player, a music note, a box), a "Benefits" column, numbered approaches (content-based filtering and hybrid are legible), two items flagged with exclamation marks |
| Thursday | Understanding Data Structures: Time Series, Cross-Sectional, and Panel Data Explained https://www.youtube.com/watch?v=LoMgvSfKp6Y (checked 12 October 2026) | 11:39 | Stick figures for many entities, clock faces for time, boxed grids for both together |
| Thursday | What is Root Cause Analysis (RCA)? https://www.youtube.com/watch?v=7t3lTYEd_PM (checked 12 October 2026) | 8:32 | "Ask why?" beside a sequence: identify, collect data, communicate, implement, monitor and log |
| Monday | Goodbye Tokenmaxxing: From AI Usage to Agentic AI Outcomes https://www.youtube.com/watch?v=FheRqx7DjbU (checked 12 October 2026) | 8:26, two weeks old | Questions about tokens, deploys and development time; a token with an up arrow; a first-place medal. The description says teams measured AI success through adoption and token consumption, and the title moves the measure to outcomes: a current proxy test |
| Monday (faculty) | What are Feature Flags? https://www.youtube.com/watch?v=AJa2B-twtG4 (checked 12 October 2026) | 6:40 | An ice-cream shop's "Grand Opening!" banner switched on by one line of code, a segment defined by email ID, numbered benefit lists |
| Week map | The 4 Pillars of Core Analytics https://www.youtube.com/watch?v=m9emhDSDKcs (checked 12 October 2026) | 4:39 | One chevron strip (descriptive, diagnostic, predictive, prescriptive) with question words such as "What?" and "Why?" above it |
| Tuesday stretch | What is Monte Carlo Simulation? https://www.youtube.com/watch?v=7TqhmX92P6U (checked 12 October 2026) | 4:35 | Dice, and three boxed questions: how do they work, who uses them, how to run one |

Three more show the same habits: Supervised vs. Unsupervised Learning https://www.youtube.com/watch?v=W01tIRP_Rqs (checked 12 October 2026) draws a numbered agenda and a bracket tree; Customer Experience Acronym Guide https://www.youtube.com/watch?v=opIuk5fCXNw (checked 12 October 2026) draws a phone and a coffee cup and sets acronyms in a row of boxes, icon above and meaning below; Lightboard Videos: How We Make Them https://www.youtube.com/watch?v=Uoz_osFtw68 (checked 12 October 2026) shows how the board is filmed.

### 3.4 How the explainers are built, and what we copy

What the finished boards show (the order in which things are drawn is inferred, since the videos could not be transcribed here): an everyday object or scene anchors the idea; a numbered agenda of two or three questions sits on the board; each sub-concept gets its own small sketch in its own region, so the finished board is a map a viewer could photograph; steps are numbered, pitfalls carry an exclamation mark, tools sit at the end of a short chain, and siblings are taught side by side. One idea runs four to twelve minutes.

For Week 4: open each chapter on the three questions it answers, drawn as numbered boxes and ticked as they close (the house question ladder made visible); build the chapter's diagram across slides so the last slide is the finished board; put the trap in the same corner of every slide under the same exclamation mark; end on the tool chain (SQL, pandas, the chart) so code arrives last. A six-minute explainer could run a hook of under a minute and about ninety seconds per question; that proportion is our proposal, since IBM's beat timings were not measurable.

## 4. Other sources worth stealing from

| Source | What to take | Day |
|---|---|---|
| Forecasting: Principles and Practice, chapter 5 https://otexts.com/fpp3/toolbox.html (checked 12 October 2026) and chapter 2 https://otexts.com/fpp3/graphics.html (checked 12 October 2026) | Four benchmarks (mean, naive, seasonal naive, drift), one formula and one figure each on the same series (Australian clay brick production); a seasonal series where only the seasonal naive tracks the actuals, and a stock price where the naive wins; a test set of about a fifth of the sample, at least as long as the horizon; a scoreboard of RMSE, MAE, MAPE and MASE; the warning that a close fit need not forecast well; a rolling-origin diagram, a four-pattern figure and the seasonal plot | Friday |
| SQL Analytics Training, the Yammer cases (formerly Mode) https://www.thoughtspot.com/sql-tutorial/sql-business-analytics-training (checked 12 October 2026), https://www.thoughtspot.com/sql-tutorial/a-drop-in-user-engagement (checked 12 October 2026), https://www.thoughtspot.com/sql-tutorial/validating-ab-test-results (checked 12 October 2026) | A dated morning, a product head at your desk, one chart with a dip; "getting oriented" asks for causes listed and ordered, with criteria and a test each, before any data opens, and for what the chart does not show; table cards, questions ending in a recommendation, the answer key on its own page. The A/B case opens on a 50 percent lift that looks too good to be true. Its analysts trade precision for time and judge product decisions against core engagement, retention and growth metrics | Thursday, Monday |
| Storytelling with Data: the 3-minute story https://www.storytellingwithdata.com/blog/2014/02/the-3-minute-story (checked 12 October 2026), the Big Idea https://www.storytellingwithdata.com/blog/2014/02/whats-big-idea (checked 12 October 2026), makeovers https://www.storytellingwithdata.com/makeovers (checked 12 October 2026) | Say it in three minutes without slides; cut it to one complete sentence with a point of view and what is at stake; then storyboard. Makeovers pair each before and after under a heading that names the lesson | Tuesday |
| Mixpanel: north-star https://mixpanel.com/blog/north-star-metric/ (checked 12 October 2026), guardrails https://mixpanel.com/blog/guardrail-metrics/ (checked 12 October 2026), cohorts https://mixpanel.com/blog/cohort-analysis/ (checked 12 October 2026) | The metric tree (north star, a focus metric, L1 to L3 inputs); a focus metric as a value moment plus its natural frequency; north star against the One Metric That Matters; two or three guardrails per experiment, citing Airbnb's experiment guardrails and Spotify; the triangular cohort table read across a row and down a column, its plateau, and retention, churn and latency versions | Monday, Thursday |
| Amplitude: North Star Playbook https://amplitude.com/books/north-star (checked 12 October 2026), funnel analysis https://amplitude.com/blog/funnel-analysis (checked 12 October 2026) | The playbook opens on one person's frustration and the "three languages" (customer, product, business) a north star ties together; its chapters include a statement exercise and a troubleshooting chapter on traps. Four funnel lenses: conversion, conversion over time by entry date, time to convert, frequency | Monday, Thursday |
| StatQuest, Conditional Probabilities, Clearly Explained!!! https://www.youtube.com/watch?v=_IgyaD7vOOA (checked 12 October 2026) | A Venn diagram of countable coloured dots beside the matching table, joined by a double arrow | Wednesday |
| Setosa, Conditional probability explained visually https://setosa.io/conditional/ (checked 12 October 2026) | Balls falling onto two shelves; counts for A only, B only, both and neither, with "actual" and "expected" readouts: lift without the word | Wednesday |
| Seeing Theory, Compound Probability https://seeing-theory.brown.edu/compound-probability/index.html (checked 12 October 2026) | Conditional probability as shrinking the sample space (the site is archived) | Wednesday |
| Financial Times Visual Vocabulary https://ft-interactive.github.io/visual-vocabulary/ (checked 12 October 2026) | Charts chosen by relationship (deviation, correlation, change over time, ranking, distribution, part to whole, magnitude, spatial, flow); the fan chart for a projection's uncertainty; magnitude bars start at zero | Tuesday, Friday |
| Think Insights, Guesstimates https://thinkinsights.net/strategy/guesstimates (checked 12 October 2026) | Four imperative headings: clarify, map, calculate, validate | Tuesday |
| Goodhart's law https://en.wikipedia.org/wiki/Goodhart%27s_law (checked 12 October 2026); Experiment Guide https://experimentguide.com/ (checked 12 October 2026) | The principle behind the proxy test; the companion site of Kohavi, Tang and Xu's Trustworthy Online Controlled Experiments (2020) for the faculty handover | Monday |

## 5. Concept ladders by day

Rung 1 is a two-minute toy a learner with no business background checks by hand; each rung adds one idea; the top rung is interview depth. Toy numbers stay away from Kalpa's planted values, so the room still finds those in the data.

### Monday: the number the plan chases

| Rung | One new idea | Tiny example | Borrowed from |
|---|---|---|---|
| 1 | A number can rise while what it stands for does not | A canteen pays servers per token; tokens go from 200 to 400 a day while plates stay at 200, because each plate now gets two tokens | Goodhart's law; IBM Tokenmaxxing |
| 2 | The proxy test | Could a department hit this while the business got worse? One line for each of the three Kalpa proposals | mysqltutorial hub |
| 3 | The denominator is a choice | 1,000 orders over 400 members is 2.5; add 100 dormant members and it reads 2.0, behaviour unchanged | mysqltutorial template |
| 4 | The window | 2.5 orders a month or 0.6 a week; match how often a customer naturally buys | Mixpanel focus metric |
| 5 | Exclusions | Auto-generated, staff and test orders struck out | IBM OKR page |
| 6 | Guardrails | The north star on one side of a seesaw, two guardrails on the other | Mixpanel guardrails |
| 7 | Leading against lagging | On the tree, inputs move before the north star | Mixpanel tree; IBM four pillars |
| 8 | Interview depth | "How would you measure a feature's success?" and "three departments want their own target": goal, north star, inputs, guardrails, definition line by line, gaming note, then the experiment (faculty block); Wells Fargo, the row's case, as the cost of a gamed target | Yammer philosophy; Amplitude's three languages |

### Tuesday: one slide, then the first guesstimate

| Rung | One new idea | Tiny example | Borrowed from |
|---|---|---|---|
| 1 | The title is the claim | "Breakfast survey results" rewritten as a sentence a hostel warden could act on | SWD Big Idea; Pyramid Principle https://managementconsulted.com/pyramid-principle/ (checked 12 October 2026) |
| 2 | Say it before you slide it | Three minutes aloud, then one sentence | The 3-minute story |
| 3 | One piece of evidence, with its denominator | One number or chart, picked by relationship: change over time is a line, a ranking a sorted bar | FT Visual Vocabulary |
| 4 | The caveat | One line on what the evidence does not show | Yammer case |
| 5 | The action with its cost | The ask in rupees and weeks | Pyramid Principle |
| 6 | Cutting | A nine-number slide rebuilt, before and after side by side | SWD makeovers; IBM do's and don'ts |
| 7 | Defence | Restate, answer from evidence, concede, say what would change your mind; in threes with role cards | The row |
| G1 to G4 | Clarify, map, calculate, validate | Cups of tea the campus canteen sells on a weekday: people times share who buy times cups each, round numbers aloud, checked against the canteen's till | Think Insights |
| G5 | Interview depth | Anand's loyalty-tier question in fifteen minutes, ending on the sanity check; the stretch gives a range | The row; IBM Monte Carlo |

### Wednesday: which pairs beat chance

| Rung | One new idea | Tiny example | Borrowed from |
|---|---|---|---|
| 1 | Support is counting | Ten tea-stall orders as dots: chai in 6, biscuit in 4, both in 3, neither in 3; support 3/10 | StatQuest Venn; mysqltutorial toys |
| 2 | Confidence shrinks the world | Of the six chai orders, 3 have biscuits: 0.5 | Seeing Theory |
| 3 | Expected under independence, and lift | 10 x 0.6 x 0.4 = 2.4 expected, 3 seen, lift 1.25 | Setosa; pbpython |
| 4 | Lift is symmetric | Biscuit to chai: 0.75 over 0.6 is 1.25 again | IBM Apriori page as counter-example (trainer side) |
| 5 | The popular partner | A carry bag in 9 of 10 orders: biscuit to bag has confidence 0.75, lift 0.3/(0.4 x 0.9) = 0.83 | The row's confidence trap, on a toy so Kalpa's case is still found |
| 6 | The support floor | Lift 6 in 3 of 2,000 baskets goes on a watch list | IBM minimum support |
| 7 | Rupees | 120 extra orders a month x Rs 80 margin, less Rs 6,000 promotion cost: Rs 3,600 a month | The row; FT waterfall |
| 8 | Interview depth | Which measure popularity cannot fool; lift 4 at 0.3 percent support; changing merchandising's mind | IBM use cases, reused Saturday |

### Thursday: who leaves, and where

| Rung | One new idea | Tiny example | Borrowed from |
|---|---|---|---|
| 1 | Fix the entry moment | A coaching centre's June and July batches of 10; 6 and 4 return in month two | IBM panel data; Mixpanel |
| 2 | The triangle | Rows are joining months, columns months since; younger rows are shorter; read across, then down | Mixpanel |
| 3 | Shape and floor | Where a row's curve flattens is the share that stayed for good | Mixpanel plateau |
| 4 | Blended against cohort | Last month batch A (100) stood at 50 percent; now A is at 40 and new batch B (400) at 52.5: 250 of 500 is still 50 percent while each batch falls with age, and next month the blend drops | Week 1 Simpson reversal; IBM retention formula |
| 5 | Stages and their denominators | 100 visits, 40 searches, 20 add-to-cart, 10 checkouts: steps of 40, 50, 50 percent, overall 10 | Amplitude lenses; IBM stages |
| 6 | The denominator artefact | Checkout per session 10 of 50 (20 percent), per member 10 of 20 (50 percent): a change of unit | FPP3's January jump, put down to when sales are registered |
| 7 | Hypotheses before data | Causes ordered with a test each, then stage and cohort named with evidence | Yammer; IBM RCA |
| 8 | Interview depth | "Retention dropped, walk me through it"; "the app team says your stage is fine". Censoring stays with the faculty | The row |

### Friday: a baseline that is hard to beat

| Rung | One new idea | Tiny example | Borrowed from |
|---|---|---|---|
| 1 | Naive | 50, 52, 49, 51 cups on four days; tomorrow's forecast is 51 | IBM forecasting page; FPP3 |
| 2 | Read the shape first | Four panels: trend, seasonality, cycle, noise | FPP3; IBM's one sketch per component |
| 3 | Seasonal naive | Sundays sell 80, so next Sunday's forecast is 80; then month of year with Diwali | FPP3 |
| 4 | Drift | Last value plus the average change | FPP3 |
| 5 | Hold out | Hide six months and forecast them; the test spans the horizon | FPP3 |
| 6 | MAE in rupees | Mean absolute error in the business's unit; a scoreboard | FPP3 |
| 7 | A perfect fit is not a forecast | A curve through every past point fails on the hidden months | FPP3 |
| 8 | Interview depth | A fan around the chosen forecast, its typical error in rupees, what would make it wrong; "two forecasts eighteen points apart" | FT fan chart; FPP3 rolling origin |

### Saturday: transfer

One grid per brief: the technique in the first column, then what changed (the metric, the constraint, the cost of an error), the Apriori page's habit of replaying one method across industries. The crux lines from memory are each chapter's closing bullets.

## 6. Visual devices by topic

Concept diagrams are mermaid fences, per the house rule; data pictures come from code cells on Kalpa data; an animated GIF is a new artifact type and needs the council's yes and a deck-builder check. The less common mermaid types below (quadrantChart, sankey-beta, block-beta) passed the Mermaid Chart validator today with section 5's toy values.

| Device | Day | What it makes visible | Build as | Idea from |
|---|---|---|---|---|
| Week strip gaining a box a day (define, communicate, find the lever, locate the loss, forecast) | All | Where today sits | Mermaid flowchart LR | mysqltutorial strip; IBM four pillars |
| Metric tree with guardrails hanging off it | Mon | North star, inputs, what must not fall | Mermaid flowchart TD | Mixpanel |
| Guardrail seesaw | Mon | A target rising while a guardrail falls | Matplotlib twin lines (trainer side until found); a toy for learners | Mixpanel guardrails |
| Leading against lagging | Mon | One series moving weeks before another | Matplotlib, or a GIF drawing both lines week by week | Mixpanel tree |
| One-slide anatomy (claim, evidence, caveat, action) | Tue | What stays, what goes | Mermaid block or the deck layout | SWD; Pyramid Principle |
| Before and after makeover | Tue | Same data, cluttered then clear | Matplotlib, two versions | SWD; IBM do's and don'ts |
| Guesstimate tree | Tue | The estimate as multiplied factors | Mermaid flowchart TD, values on nodes | Think Insights |
| Countable Venn beside its 2 x 2 table | Wed | Support, confidence and lift as counts | Matplotlib dots in circles, plus a table | StatQuest |
| Shrinking universe | Wed | Confidence as a smaller denominator | GIF from the twelve baskets: all, only A, A with B | Seeing Theory |
| Actual against expected bars | Wed | Lift as a ratio of two bars | Matplotlib | Setosa |
| Lift and support action map (promote, watch, ignore, trap) | Wed | Why thin support waits | Mermaid quadrantChart for the toy; matplotlib for all pairs | IBM support threshold |
| Rupee waterfall | Wed | Margin gained less promotion cost | Matplotlib | FT waterfall |
| Panel grid (members across, months along) | Thu | What a cohort fixes | Mermaid block or matplotlib grid | IBM panel-data explainer |
| Cohort triangle heatmap | Thu | Retention by joining month and age | Matplotlib; a GIF filling one diagonal per month shows why it is a triangle | Mixpanel |
| Retention curves with their floor | Thu | Shape, plateau, worst cohort | Matplotlib | Mixpanel |
| Blend decomposition | Thu | A flat average over falling cohorts | Stacked cohort sizes under a flat blended line; a GIF adding one cohort at a time | Week 1 Simpson reversal |
| Funnel with step and overall rates | Thu | Where the loss sits, on which denominator | Mermaid sankey-beta; matplotlib bars | Amplitude |
| Hypothesis ladder | Thu | Causes ordered with their tests | Mermaid flowchart TD | Yammer case |
| Four-pattern panel | Fri | Trend, seasonality, cycle, noise | Matplotlib small multiples on toy series | FPP3 |
| Seasonal plot, years overlaid | Fri | The Diwali month standing out each year | Matplotlib on the 24 months | FPP3 |
| One baseline per panel, then the scoreboard | Fri | What each baseline assumes and how it scores | Matplotlib small multiples, then a table | FPP3 |
| Hold-out split and rolling origin | Fri | Which months are hidden, and why | Matplotlib shading; dot rows | FPP3 |
| The reveal | Fri | Vendor curve against seasonal naive as hidden months appear | GIF from our own series | FPP3 |
| Fan chart | Fri | The error bar on the board number | Matplotlib | FT Visual Vocabulary |

## 7. Not verified today, and links that moved

- YouTube transcripts: refused for every request (IpBlocked); two third-party caption services were themselves blocked by YouTube. No beat timing in section 3 is measured.
- IGotAnOffer market sizing guide (a Tuesday resource in the row): Cloudflare challenge; not verified.
- Kaggle Learn time series course: reCAPTCHA; not verified, not cited.
- Khan Academy (a Friday resource in the row): client challenge page; not verified.
- A Medium post by an IBM lightboard presenter on technical storytelling: Cloudflare 403; not verified, not used.
- Amplitude North Star Playbook chapters: only the landing page and chapter titles load; chapter content not verified.
- Forecasting: Principles and Practice has been restructured: simple-methods.html redirects to toolbox.html#sec-simple-methods and accuracy.html to toolbox.html#sec-accuracy (checked 12 October 2026). The row's links still resolve; packs should cite the new addresses. From this environment otexts.com refused a browser-like request with 403 and loaded with a plain one.
- mode.com/sql-tutorial now redirects to thoughtspot.com/sql-tutorial (checked 12 October 2026).
