# W04 D3 cold reads: a fresh graduate and a hiring interviewer

INTERNAL. Two reads by separately spawned agents on the latest Opus model, each told to write findings
only and never edit; both ran on 12 October 2026 after the pack was built and before the fix pass.
Their findings are copied below as each reader returned them, with what each became. The second
read changed a method other files repeat, so a narrow re-check of the interview material followed
the fix pass, and a confirmation read followed the re-check's fixes (the last two sections).

| Read | Who | What it read | Findings |
|---|---|---|---|
| One | A fresh graduate, 23, no company experience, weak in maths | Every STUDENT file, in learner order | 72 |
| Two | A hiring interviewer for Uber, Swiggy, Google and AI-startup screens | The transcripts, the AI variant, the guesstimate, the interview slides and the sources | 25, one blocker |
| Re-check | A second hiring interviewer, after the fix pass | The same interview material, against the first interviewer's findings | 7, two blockers |
| Confirmation | A third hiring interviewer, after the re-check's fixes | The same interview material, against the re-check's findings | 8, three blockers |

## What did the fresh graduate find?

1. slides/C2_W04_D03_half1_STUDENT.md | S1, "The metric" row | Click-through is "clicks over impressions", but the slide never says what an impression is (only the trainer's notes do). "Slot" is used in the ask and in strip_log but never tied to "one of the strip's three places". | One line on S1: an impression is one time a slot was shown, and a slot is one of the strip's three places.
2. slides/C2_W04_D03_half1_STUDENT.md | S1 "Company, city, surface" row and the title slide's "Who" line (also S27 "Friday's review", notebook 03 c10 "Growth keeps the margin") | I have never worked in a company. I don't know what a ticket is, what "surface" means, what a growth lead or a category manager does, what Friday's review is, or who "Growth" is. | A short who's-who line: a ticket is a work request, a surface is a part of the app, the growth lead owns clicks and orders, the category manager decides which products are promoted, and Friday's review is the weekly meeting where the numbers are defended.
3. slides/C2_W04_D03_half1_STUDENT.md | S1 data row, strip_log columns (also S27 and S37 "milk anchors the cart", board_work "Anchor") | anchor_item and adds are never explained. Later "anchor" means three different things: the item a suggestion is ranked from; "milk anchors the cart", which is only explained at half two S40; and the concept board's Anchor. | Define anchor item and add the first time they appear (the cart item the suggestion is paired with; the shopper puts the suggested item in the cart), and explain "anchors the cart" where it first appears.
4. slides/C2_W04_D03_half1_STUDENT.md | S1 Caveats row | It took three reads to get "the strip causes some of the co-occurrence it counts". "Co-occurrence" is new to me and the loop is never spelled out. | One plain example: the strip shows milk beside bread, some shoppers add it, so the bread-and-milk count grows because of the strip.
5. slides/C2_W04_D03_half1_STUDENT.md | S1 data row vs S30 and S32 (also notebook 03 c06) | 40,000 carts in 28 days is about 1,430 a day, yet S32 uses 60,000 cart-page views a day, and only S30 calls the carts "this sample". I could not tell whether the 40,000 are all of Pune's carts or a sample. | Say on S1 that the carts are a sample of Pune's carts.
6. slides/C2_W04_D03_half1_STUDENT.md | S2 week map, centre node | In "One number, five tickets" I could not tell which one number is meant. | Name it the way the study notes do: each day asks what one number is compared with.
7. slides/C2_W04_D03_half1_STUDENT.md | S3 Promote card | "Three pairs above a 1 percent floor" uses "floor" before it is defined (S29, notebook 03), and the numbers 3.39, 3.00 and 2.21 are not labelled as lifts. | Write "lift 3.39" and add a few words on what a floor is.
8. slides/C2_W04_D03_half1_STUDENT.md | S6 and S7 (also S20 "Lift divides milk's popularity out", notebook 01 c03 to c05) | S6 says "from biscuit's side it is 0.75 / 0.60", but the first sum was already from biscuit's side. S7 says "lift is 0.75 / 0.90". The reason a confidence over the partner's share gives lift only arrives at S22, so until then I took it on trust. | State the rule the first time it is used and show both sides: chai to biscuit 0.50 / 0.40 = 1.25, biscuit to chai 0.75 / 0.60 = 1.25.
9. slides/C2_W04_D03_half1_STUDENT.md | S8 title (also the cart cards intro, notebook 01 c06, the study notes and the three_counts solution) | It says "twelve real carts" while S1 says the data are synthetic. I wondered whether these twelve came from a different, real source. | "Twelve carts taken from the 40,000".
10. slides/C2_W04_D03_half1_STUDENT.md | S11 text and its picture (shrink_still_last) | "The fix: read lift, 1.50, on too few carts to trust" took three reads. The picture's title "Of those, carts that also hold milk: 4" points to a "those" from a frame I cannot see. | "The fix: read lift instead, 1.50, though twelve carts are too few to trust it", and the title "Of the 4 bread carts, 4 also hold milk".
11. slides/C2_W04_D03_half1_STUDENT.md | S13 (also half two S46, the study notes week map and the board_work week map) | "A cohort against the blend", "beyond the blend" and "beyond the baseline" are never explained, so the lines about Thursday and Friday meant nothing to me. | A one-line plain meaning for each word, or leave the words for those days.
12. slides/C2_W04_D03_half1_STUDENT.md | S17 last code line and caption (also notebook 01 c11, notebook 02 c07, cheat sheet panel 1) | Lift is written as both x n / (A x B), "times all carts, over the two items' own counts". I could not see how this equals seen over expected (12 x 4/12 x 8/12), because the cancelling step is never shown. | One worked line on the twelve carts: 4 / (12 x 4/12 x 8/12) = 4 x 12 / (4 x 8) = 1.50.
13. slides/C2_W04_D03_half1_STUDENT.md | S18 text and the areas picture's title | 0.252 / 0.241 gives 1.046 on my calculator, which rounds to 1.05, not the 1.04 printed. | Use the counts, 10,064 / 9,656 = 1.04, as the study notes do, or show four decimals.
14. slides/C2_W04_D03_half1_STUDENT.md | S18 picture (whiteboards/C2_W04_D03_areas_STUDENT.png), right panel | The red dashes sit at 0.71 on the axis but are labelled "the expected 0.241", and this panel's y-axis has no label. It took me a long time to see that the area, not the height, is 0.241. | Label the heights 0.71 and 0.74 and add "area = width x height = share of carts holding both".
15. slides/C2_W04_D03_half1_STUDENT.md | S20 picture (milk_everywhere) | The caption says "the twelve most common items", but the chart shows nine and the text talks about 50. "Milk's own share 71 percent" runs into the title, and the dashed lines cut through 0.74 and 1.04. | Match the caption to the bars and move the labels off the lines.
16. slides/C2_W04_D03_half1_STUDENT.md | S21 "measured the base rate per purchase" (also notebook 02 c19 to c20, half two S41, the interview and cheat sheet panel 7) | "Base rate" is used as if I already knew it. Its meaning only appears in the study notes glossary, at the end of the day. | Define it at S21: how common the partner item is across all carts (milk, 71 percent).
17. slides/C2_W04_D03_half1_STUDENT.md | S22 second-route line (also study notes "The second route") | For "milk to bread 0.35 / 0.34 = 1.04" I get 1.03. | Show 0.354 / 0.34 = 1.04, or say the inputs are rounded.
18. slides/C2_W04_D03_half1_STUDENT.md | S22 table vs notebook 02 c07 | The deck lists "ice cream, chocolate sauce" with confidence A to B 0.06 and B to A 0.18. The notebook lists "chocolate sauce, ice cream" with conf_a_to_b 0.1838 and conf_b_to_a 0.0625, so the two look swapped. | Use the same pair order in both, or name the direction ("ice cream to sauce 0.06").
19. slides/C2_W04_D03_half1_STUDENT.md | S22 table (also S18) | In the same row, support is a percent (25.2%) and confidence is a decimal (0.74), while S18 wrote the same support as 0.252. Switching formats slowed me down. | One format per measure, or show both formats side by side.
20. slides/C2_W04_D03_half1_STUDENT.md | S24 "up from 6.2" (also notebook 02 c18, the study notes, cheat sheet panel 3, fallback S11) | 6.2 is never computed anywhere. Notebook 02 splits only the rows after the change. | One line or cell that splits the before rows the same way (milk 2 percent of impressions, everything else at 6.2).
21. slides/C2_W04_D03_half1_STUDENT.md | S29 text and picture (also half two S38, the pair cards regions, cheat sheet panel 4) | "Four beat chance clearly" and "lift well above one" come with no number. The green band starts near 1.5 with no tick, and 1.5 only appears in a notebook 03 check and the exercise rules, so I could not place namkeen and poha (1.29) on the pair cards. | Write the rule "lift at least 1.5" on S29 and mark that line on the picture.
22. slides/C2_W04_D03_half1_STUDENT.md | S29 vs S3, S37 and S46 | Four pairs qualify, but the answer promotes three, and onions and tomatoes (1.70) disappears without a word. Only notebook 03 c04 says "the first three fill the strip". | One sentence on S29: there are three slots, so the fourth pair waits.
23. slides/C2_W04_D03_half1_STUDENT.md | S29 picture (action_map), x-axis | "Log scale" is never explained. The stretch from 0.1 to 1 percent is as wide as the one from 1 to 10 percent, which misled me. | One line under the picture saying each tick to the right means ten times more carts.
24. slides/C2_W04_D03_half1_STUDENT.md | S30 (also notebook 03 c06 to c07) | In "the strongest pair between 0.2 and 1 percent support" I don't know where 0.2 comes from, since the map starts at 0.1. | Say why pairs under 0.2 percent are left out.
25. slides/C2_W04_D03_half1_STUDENT.md | S30 (also half two S42, quiz Q4, the interview) | "A slot is shown on every cart page, so a pair that thin cannot repay it" and "beats the slot's own record" took three reads. I did not know what repaying a slot means or which record is meant. | Spell it out: the slot appears on every cart page, but this pair fits only about 100 carts, so it earns little; the record is that slot's usual click-through (fallback S2 says this).
26. slides/C2_W04_D03_half1_STUDENT.md | S32 cascade (also notebook 03 c08) | The slide cites "60,000 views a day (strip_log)", but the log holds impressions, which add up to about 180,000 a day; only notebook 02 c13 and the afternoon set say each view shows all three slots. The slide gives no source for 0.5 adds per click or Rs 9, and no working for the Rs 3.9 to 9.3 lakh range. | Say views are impressions per slot, give each factor's source, and show the low (0.4 x Rs 7) and high (0.6 x Rs 11) products.
27. slides/C2_W04_D03_half1_STUDENT.md | S32 and S33 (also notebook 03 c08 and kalpa_charger Q1) | "Margin" is never defined in the decks or the notebooks. Only the study notes glossary told me it is what the business keeps after the item's cost, and kalpa_charger Q1 depends on it. | Define margin at S32 with one item from cart_items (bread sells for Rs 45 with a margin of Rs 6.70).
28. slides/C2_W04_D03_half1_STUDENT.md | S32 picture and S3 card (also notebook 03 c09) | Rs 17,280 is labelled "a slot showing a pair that beats chance", but 6.4 percent is the click-through of everything except milk after the change. I could not tell whether the new pairs are assumed to click at that rate. | Say it is an assumption that the promoted pairs will click at the 6.4 percent the other suggestions drew.
29. slides/C2_W04_D03_half1_STUDENT.md | S33 (also notebook 03 c10 to c11, study notes WATCH OUT) | The slide says "1,920 adds a day, each selling for about Rs 42, so Rs 80,197", but 1,920 x 42 is Rs 80,640. | Show the price as Rs 41.77, or print Rs 80,640.
30. slides/C2_W04_D03_half1_STUDENT.md | S33 (also notebook 03 c10, the interview, the strip solution) | "Swiggy's own letter", "Maxxsaver" and "(W4, checked ...)": I did not know which letter or what Maxxsaver is, and W4 (with W1 and W2 in the interview) read to me as week numbers. | Write "Swiggy's shareholder letter for April to June 2025", add one line on Maxxsaver (the study notes have it), and use a source name in place of W1, W2 and W4.
31. slides/C2_W04_D03_half1_STUDENT.md | S34 first row (also notebook 03 c12, half two S43, cheat sheet panel 6) | "A holdout that changes the strip" uses holdout, which is not explained until the interview transcript (the assistant on half the carts, the baseline on the other half). | Define holdout the first time it is used.
32. slides/C2_W04_D03_half1_STUDENT.md | S34 first row (also notebook 03 c12, the three_counts solution, the study notes) | "Monday's faculty session on A/B testing (tentative)": today is Wednesday, so I could not tell whether it already happened or is still to come, and notebook 03 says it "takes up" in the present tense. | Say "held this Monday" or "planned for next Monday".
33. slides/C2_W04_D03_half1_STUDENT.md | S34 table (also notebook 03 c12) | The slide promises six doubts, but row six ("Answered above") repeats row two. Notebook 03's "which the first check answers" doesn't say which check, and no row clearly answers S1's caveat that the strip creates some of the pairs it counts. | Merge rows two and six, and name the row that answers the S1 caveat.
34. slides/C2_W04_D03_half1_STUDENT.md | S35 text and picture title (also notebook 03 c13, the study notes) | The slide never says how "counted with every customer once" works; the weighting appears only in the trainer notes, the notebook code and the afternoon table. "73 percent of the carts holding both" is not computed in any file. | A tiny example (a shopper with 4 carts counts each cart as 0.25), plus a cell that prints the 73.
35. slides/C2_W04_D03_half1_STUDENT.md | S36 | In "Curd is in 12 of 2,583 carts. Set those aside", "those" could mean the 12 or the 2,583. Only the 27.8 told me it was the 2,583. | "Set those 2,583 carts aside".
36. whiteboards/C2_W04_D03_cart_cards_STUDENT.md | "Which grid does your group fill in for each pair?" | I first read "lift is the top-left cell over what chance gives, 12 times the A total over 12 times the B total over 12" as (12 x A) / (12 x B) / 12. | Write it as 12 x (A / 12) x (B / 12) and fill it in once for bread and milk.
37. notebooks/C2_W04_D03_01_receipts_STUDENT.ipynb | Cell c05 picture | The bars run from 0 to 1 with no x-axis label, so I had to guess the scale is a share of orders (the deck's version has the label). | Add the label "share of orders".
38. exercises/C2_W04_D03_index_STUDENT.md | Last paragraph (also interview "What does the scorer listen for?") | I don't know what "a sizing" (and later "sized it with a unit") means. | One line saying that sizing means putting a number with its unit on an option (carts, minutes or rupees).
39. exercises/unguided/C2_W04_D03_ch1_one_pair_STUDENT.md | Q1 to Q4 level tags (also the other sets and the interview intro) | "Asked in GCC analytics screens", "product-company screens" and "stakeholder round": I don't know what GCC stands for, or that a screen is an interview round. | Spell out GCC once (global capability centre, a foreign company's India office) and say a screen is an interview round.
40. notebooks/C2_W04_D03_02_pairs_table_STUDENT.ipynb | Cell c05 | Counter(p for basket in baskets for p in combinations(sorted(basket), 2)) has no comment here. combinations, two fors in one line and the reason for sorted are all new to me, and only the deck's copy has comments. | The deck's comments above the cell, and one cart worked by hand: {bread, eggs, milk} gives three pairs.
41. notebooks/C2_W04_D03_02_pairs_table_STUDENT.ipynb | Cell c09 picture | Two rectangles with 0 to 1 on both axes and no axis labels. I could not tell what the width and the height stand for. | Label x "share of carts with bread" and y "share of those with milk", as the deck's picture does.
42. notebooks/C2_W04_D03_02_pairs_table_STUDENT.ipynb | Cell c13 | In "The strip shows packs, and toned milk comes in more than one pack, so one view can show milk in two slots", I did not know what a pack means. | "Each pack size is its own suggestion, so milk can fill two slots on one view".
43. notebooks/C2_W04_D03_02_pairs_table_STUDENT.ipynb | Cell c15, your turn | I could not start "check that the two rates, weighted by their shares, give back the blended rate". Weighting and "blended rate" have not been shown with numbers before this cell; S24's half-and-half line comes after it. | Put the "half of 1.2 plus half of 6.4" example in the cell's text first.
44. whiteboards/C2_W04_D03_pair_cards_STUDENT.md | Intro | It says every number here was already computed in notebook 02, but notebook 02 never printed bread and butter, onions and tomatoes, butter and tomatoes, or namkeen and poha. | Say where these come from (notebook 03, deck S29).
45. whiteboards/C2_W04_D03_pair_cards_STUDENT.md | "Which four regions does the wall carry?" vs half one S29 picture and cheat sheet panel 4 | The cards have four regions and put milk's pairs (lift near one, above the floor) in Trap. The deck's map has three regions and calls the same area Ignore, and the cheat sheet repeats Ignore. | Use the same regions and names everywhere.
46. notebooks/C2_W04_D03_03_action_map_STUDENT.ipynb | Cell c04 (also fallback S4) | "Margin" also means a gap here ("beat chance by a clear margin"), and fallback S4 puts "by a margin fixed in advance" next to "adds x margin", so I mixed it up with the rupee margin. | Use "gap" or "by enough" when it is not rupees.
47. notebooks/C2_W04_D03_03_action_map_STUDENT.ipynb | Cell c05 picture (also the notebook 04 c09 scatter) | The axes read 10^-3, 10^-2 and 10^-1 (and 10^3 to 10^7 rupees in notebook 04), which I cannot turn into percents or rupees. The point at lift 4.6 has no label. | Tick labels of 0.1%, 1% and 10%, and Rs 1,000 up to Rs 1 crore, as the deck's picture does, and label the top point.
48. notebooks/C2_W04_D03_03_action_map_STUDENT.ipynb | Cell c12 | I read "a party shopper buys chips and cold drink together, and promoting chips sells no cold drink to anyone else" three times and am still unsure what it proves. | "Lift says the two are bought together; it does not show that suggesting cold drink beside chips makes anyone buy a cold drink they would not have bought."
49. notebooks/C2_W04_D03_03_action_map_STUDENT.ipynb | Cell c17 interview line (also half two S43, quiz Q5, the interview) | "Incremental adds", "cost line" and quiz Q5's "expected value" are new, and until now "expected" meant "expected by chance". | Explain them: incremental adds are adds that would not have happened without the strip; the cost line is what gets subtracted, here the discount.
50. slides/C2_W04_D03_half2_STUDENT.md | S38 and S39 vs the strip set in exercises/unguided | S38 and S39 say each group hands in a one-page strip with four fields in 35 minutes. The afternoon set in exercises/unguided is five letter items for the same 35 minutes in groups. I could not tell which one we hand in, or where the one-page template is. | Say whether both are due, and where the template is.
51. slides/C2_W04_D03_half2_STUDENT.md | S43 (also strip set Q5, the interview, the study notes) | "Lift of its suggestions over a popularity baseline", "offline", "online" and "held-out carts": lift here compares an assistant with a baseline rather than two items in a cart, and the other words are new to me. | One line each: held-out carts are carts the assistant never saw; offline means scored on past carts; this lift is the assistant's hit rate over the baseline's.
52. slides/C2_W04_D03_half2_STUDENT.md | S44 handoff (also study notes "What was left out" and ORIGIN) | "A lift near one is independence made visible", "lets an algorithm skip counting every combination" and "association rules": I don't know independence in this sense, which algorithm is meant, or what a rule is. | One line saying independent means knowing one item tells you nothing about the other, and a rule is "bread, so milk", plus a note that the faculty session names the algorithm.
53. extras/C2_W04_D03_interview_STUDENT.md | Follow-ups and pain-points table (also the study notes) | "Q1 FY26 letter", "MTUs", "Uber's 10-K", "gross bookings" and "Osco Drug" are all new to me, and I could not see what the check "Ask who chose to use both" means. | Explain each once (MTU = monthly transacting user, 10-K = a US annual report, Q1 FY26 = April to June 2025) and expand the check: heavy users pick both products, so using both is not what caused the bookings.
54. kahoot/C2_W04_D03_quiz_STUDENT.md | Every item | My copy shows the "<- correct" marks, so I was not sure whether to read it before the live quiz or only afterwards. | Say at the top that this is the answer sheet for after the quiz.
55. kahoot/C2_W04_D03_quiz_STUDENT.md | Q2 | Working out 1,800 x 40,000 / (13,600 x 2,400) in twenty seconds is beyond me without a calculator. | Round the counts or give the shares (0.34 and 0.06), or allow more time.
56. notebooks/C2_W04_D03_04_kalpa_lab_STUDENT.ipynb | Cell c00 (also the kalpa_charger intro and the lab set) | "Merchandising team", "head of merchandising", "merchandiser" and "Retail-Plus members": I don't know what merchandising does or what Retail-Plus is. | One line on what merchandising decides and what Retail-Plus is.
57. notebooks/C2_W04_D03_04_kalpa_lab_STUDENT.ipynb | Cells c00 and c06 | The floor is 5 percent of baskets here but 1 percent at Instamart, and nothing says why. | One line: 812 baskets is a small set, so 1 percent would be about 8 baskets, which is too thin.
58. notebooks/C2_W04_D03_04_kalpa_lab_STUDENT.ipynb | Cells c02 to c03 | It says "The cell below confirms your count", but the cell only prints the baskets and the item counts. It does not show the screen protector's confidence and lift or the earphones' lift I counted (I got 0.67, 0.89 and 2.67 and cannot check them). "Lift toward the charger" also clashes with "lift is the same from either side". | Print those three numbers in the cell and say "lift with the charger".
59. notebooks/C2_W04_D03_04_kalpa_lab_STUDENT.ipynb | Cells c05 and c07, your turn | Two empty cells with a one-line hint and no check or expected numbers, so I cannot tell whether my code is right, and kalpa_charger Q2 and Q3 depend on them. | A check cell with the expected charger share, or a half-written cell.
60. notebooks/C2_W04_D03_04_kalpa_lab_STUDENT.ipynb | Cell c06 | "Check which segment its baskets come from by joining orders": the notebook never lists the segments (only Business) or says why the segment matters, and I did not know how to join a Series of baskets to orders. | Print orders.segment.value_counts(), show the join line, and say what it would mean if a pair came mostly from one segment.
61. notebooks/C2_W04_D03_04_kalpa_lab_STUDENT.ipynb | Cell c09 histogram | "Baskets hold one to eight lines": I did not see what this tells me about whether the data can carry the answer, and the tall bar at eight is not explained. | One sentence on what the chart checks and why eight lines is the most common size.
62. exercises/unguided/C2_W04_D03_kalpa_charger_STUDENT.md | Q3 option b (also lab set Q6 option c) | "A stated uplift range" and "an uplift assumption": is uplift the same as lift? It is never defined. | Define uplift (the extra sales a bundle causes) or use a different word.
63. exercises/practice/C2_W04_D03_lab_set_STUDENT.md | Q5 | Line 1 uses both, n, a and b, which none of the four lines define, so I thought no order could run "without an error". The solution only notes that 2, 4, 3, 1 also works. | Write line 1 as lift = pair_count[(a, b)] * len(baskets) / (single[a] * single[b]), or say that a, b, both and n are already set.
64. study-notes/C2_W04_D03_notes_STUDENT.md | "Where does Wednesday sit in the week?" | It says "Upsell was named and left for later", but I never saw upsell in class or in any file. | Drop it, or define it where it was named.
65. study-notes/C2_W04_D03_notes_STUDENT.md | "Two ways to count every pair" | "About 433,000, since a cart holds 4.7 items on average": 4.7 items give 4.7 x 3.7 / 2 = about 8.7 pairs a cart, which is about 348,000 for 40,000 carts. | Show the average number of pairs per cart (about 10.8) that gives 433,000.
66. study-notes/C2_W04_D03_notes_STUDENT.md | "Four ways to rank, and the call" | "A cheaper slot would change it by letting a lower floor admit thinner pairs": I don't know what makes a slot cheaper. | "If a slot were worth less, a lower floor would be acceptable".
67. study-notes/C2_W04_D03_notes_STUDENT.md | "The guesstimate" | "Dark store", "catchment" and "per active store-day" are new. The 430 to 2,860 range comes with no input ranges, "Swiggy reported 1,089 across 1,171 stores" doesn't say 1,089 of what, and none of this was covered in class. | Define the words, give the low and high inputs, and write "1,089 orders a store a day".
68. cheatsheets/C2_W04_D03_beyond_chance_STUDENT.md | Panel 6, stock-out row (the same in the PDF) | The trap "A stock-out hides a pair" has the check "curd's lift with milk stays 1.01", which shows nothing was hidden, and deck S36 says a stock-out "cuts the count, never the pull". | "A stock-out lowers a count".
69. preread/C2_W04_D03_preread_STUDENT.md | "What does Thursday's ticket say?" | The ticket says "month-two retention flat at 38 percent", then "each new month keeps fewer in its first month: 58, 49, 31". I could not tell whether month two and first month are the same measure, so I could not connect these numbers to the 38. "Add-to-cart to order rate" is also new. | Use one name for one measure, and add one line showing how 38 can be a mix of groups.
70. slides/C2_W04_D03_fallback_STUDENT.md | S2 cards | One card says "one shown the pair and one left as it is", but "Against what" says "the click-through that slot drew in the same zones before the trial". I could not tell whether the pair is compared with the other zone or with its own past. | Pick one comparison and say it.
71. slides/C2_W04_D03_fallback_STUDENT.md | S7 "Thin ground" vs the take-home self-check, Hinjewadi night | The fallback says three pairs on 7 to 10 carts slip above bread with butter. The self-check says two (coriander and ghee, pav and potatoes). | Note that one counts the top five pairs and the other the top four.
72. slides/C2_W04_D03_fallback_STUDENT.md | S9 "Friday's method" | It took three reads to get "Compare each week with the same distance from the event, never the same calendar week". | A small example using two Diwali dates.

**What worked, in the reader's words.** With the twelve cart cards and the 2 by 2 grid the reader could do every hand count, and bread and milk (1.50), chips and cold drink (2.67) and ice cream and chocolate sauce (12) came out exactly as the slides say. The ten dots and the carry bag made the difference between confidence and lift click before any formula appeared. "Half of 1.2 plus half of 6.4 is 3.8" with the daily chart explained the fall in one breath, and the slot cascade came out right at every step. Every exercise could be answered from the files, the reader's letters matched every key, and every count and lift in the take-home self-check came out exactly on the data files.

## What became of each graduate finding?

| Finding | Outcome |
|---|---|
| 1 | S1 defines an impression and a slot; notebook 01's first cell too |
| 2 | S1 gains a Who asks row and the ticket's meaning; notebook 01's first cell names the roles and Friday's review |
| 3 | S1 defines anchor_item and adds; "anchors the cart" is gone from S27, S37, S40, the strip set, its solution and the notes; the concept board's region is The example |
| 4 | S1's caveat carries the milk-add example |
| 5 | S1 says a sample of 40,000 carts, every September cart of 12,000 customers |
| 6 | S2's centre node reads one question, five tickets: compared with what? |
| 7 | S3 labels each lift and defines the floor |
| 8 | S6 and S7 state the second route with both sides; notebook 01 too |
| 9 | "Carts from the case" in S8, section 1, the cart cards, notebook 01, the notes and the index |
| 10 | S11 reworded; the still's title reads Of the 4 bread carts, 4 also hold milk |
| 11 | Plain words for Thursday and Friday in S13, S46, the notes and the board work |
| 12 | S17 shows the rearranged form on the twelve carts; notebook 01 and notebook 02 comment it |
| 13 | S18 and the areas picture use 10,064 / 9,656 = 1.04 |
| 14 | The areas picture labels both heights and the area rule |
| 15 | S20's caption reads nine items; the picture's labels sit off the lines |
| 16 | S21 and notebook 02 define the base rate where it first appears |
| 17 | S22 and the notes show 0.354 / 0.34 |
| 18 | S22 lists chocolate sauce, ice cream in the notebook's order |
| 19 | S22 states each format; S18 uses counts |
| 20 | Notebook 02 splits the before rows too and checks 6.2 percent; S24 says so |
| 21 | S29, the action map's dotted line, the pair cards and cheat sheet panel 4 state lift 1.5 or more |
| 22 | S29 and notebook 03 say three slots, so onions and tomatoes waits |
| 23 | S29 and both action maps say each step right is ten times more carts; notebook 03 prints percent ticks |
| 24 | S30 and notebook 03 give the 0.2 percent band as 80 carts, too few even to trial |
| 25 | S30, S42, the quiz, the notes and the transcript give the anchor-based reason (the interviewer's finding 3 sharpened it) |
| 26 | S32 and notebook 03 give each factor's source, 180,000 impressions a day and the low and high products |
| 27 | S32 and notebook 03 define margin with bread's Rs 45 and Rs 6.70 |
| 28 | S32 and notebook 03 state the 6.4 percent assumption |
| 29 | S33, notebook 03 and the notes print Rs 41.77 |
| 30 | S33, notebook 03, the notes, the transcript and the strip solution name the letter and Maxxsaver; the W codes left every learner file |
| 31 | S34 and notebook 03 define a holdout |
| 32 | Every learner file says this week's Monday faculty session (tentative) |
| 33 | S34, notebook 03 and the notes carry six distinct doubts, the last answering S1's caveat |
| 34 | S35 and notebook 03 explain the weights with a four-cart shopper; notebook 03 prints and checks the 73 percent |
| 35 | S36 reads those 2,583 carts |
| 36 | The cart cards write 12 x (A total / 12) x (B total / 12), worked on the tea stall, so the bread reveal stays for S10 |
| 37 | Notebook 01's bag chart labels its axis |
| 38 | The index defines a sizing; the transcript glosses sized it with a unit |
| 39 | Level tags read interviews; the index and the transcript define a GCC |
| 40 | Notebook 02 comments the counting cell and works one cart by hand |
| 41 | Notebook 02's areas picture labels both axes |
| 42 | Notebook 02 explains pack sizes |
| 43 | Notebook 02's your-turn cell opens on an invented blend |
| 44 | The pair cards say notebooks 02 and 03, and go out after notebook 03's first cells; the run sheet follows |
| 45 | Four regions everywhere: the action map, the pair cards, the board work and cheat sheet panel 4 |
| 46 | Gap replaces margin where no rupees are meant, in notebook 03 and the fallback |
| 47 | Notebook 03 prints percent ticks and labels the top thin pair; notebook 04 prints rupee ticks |
| 48 | Notebook 03's cause sentence rewritten as suggested |
| 49 | Notebook 03, S43 and the quiz define incremental adds and the cost line |
| 50 | S38 and the strip set say the one-page strip is handed in and the five items ride along |
| 51 | S43 and the strip set define held-out carts, offline and online |
| 52 | S44 glosses independence and a rule |
| 53 | The transcript defines MTU, 10-K, the letter's quarter and Osco Drug stores, and expands the Uber check |
| 54 | The quiz says it is the answer sheet, read after the live quiz |
| 55 | Q2 gets sixty seconds; the counts stay, since the sum is the skill tested |
| 56 | Notebook 04, the Kalpa set and the lab set define merchandising, Retail-Plus and a merchandiser |
| 57 | Notebook 04 gives the 5 percent floor's reason, about 8 against about 41 baskets |
| 58 | Notebook 04 prints the twelve baskets' three numbers and says lift with the charger |
| 59 | Partly: notebook 04 adds sanity checks a learner can run; the expected values stay out (reason below) |
| 60 | Notebook 04 shows the segment join and why a segment matters |
| 61 | Notebook 04 explains the eight-line cap and why one-line baskets matter |
| 62 | The Kalpa set and the lab set define uplift |
| 63 | The lab set's line 1 is rewritten and a and b are set |
| 64 | S37 names upsell; the notes define it |
| 65 | The notes give 10.8 pairs for an average cart |
| 66 | The notes reword the cheaper-slot line |
| 67 | The notes define a dark store, a catchment and active days, and give every input range |
| 68 | Cheat sheet panel 6 reads a stock-out lowers a count |
| 69 | Partly: the pre-read quotes the case file's blended definition and flags month one and month two as different measures (reason below) |
| 70 | Fallback S2 and S4 compare with the shoppers not shown the pair |
| 71 | The self-check names the third pair on 7 carts |
| 72 | Fallback S9 works the two Diwali dates |

## What did the hiring interviewer find?

Findings: 25

Scale: mine is 0 absent, 1 present but incomplete or fails the obvious follow-up, 2 complete and survives it. The TRAINER file's is 0 absent, 1 named, 2 named with the day's number.

**[S] hire-grade answer, with its three follow-up lines**

| Criterion | Mine | TRAINER | Reason |
|---|---|---|---|
| Clarified the scope | 2 | 2 | Three clarifiers that change the answer: what a basket is, choosing versus measuring, how many carts the rarest pair sits in |
| Named the denominator and the window | 1 | 2 | Names milk's 71 percent as the base rate but never picks a window; the question's "year of carts" silently becomes four weeks of September |
| Saw the paradox | 2 | 2 | 0.74 is milk's own 0.71, while 0.42 hides 3.39; only "1.04: chance" is loose (finding 6) |
| Sized it with a unit | 1 | 2 | Carts and rupees appear, but Rs 17,280 and Rs 80,197 have no range, and the add rate and margin are never called assumptions |
| Said what would change their mind | 1 | 2 | Names a holdout and a trial, never the result that would flip the ranking |
| Tied it to a decision and its cost | 1 | 2 | The ranking rule and the watch list are decisions; the cost given is gross margin on every strip add, never incremental margin or what milk's slots cost |
| Gave the structure before the number | 2 | 2 | The pick and its reason come first; same score, but TRAINER's reason ("three questions apart") is not in the answer |
| Total | 10 | 14 | |

**[D] hire-grade answer**

| Criterion | Mine | TRAINER | Reason |
|---|---|---|---|
| Clarified the scope | 2 | 2 | Asks for both windows, what else shipped on 7 September, and whether the redesign replaces the fix or runs beside it |
| Named the denominator and the window | 1 | 2 | Never states the windows or the impression mix (milk went from 2 to 50 percent of impressions), which is what turns 1.2 and 6.4 into 3.8 |
| Saw the paradox | 2 | 2 | Sees the blend fall while every other suggestion rose from 6.2 to 6.4 |
| Sized it with a unit | 1 | 2 | Rates only; the fall is never sized in clicks or rupees |
| Said what would change their mind | 2 | 2 | A real falsifier (the other slots falling too), though worded as if milk's own rate fell |
| Tied it to a decision and its cost | 1 | 1 | Re-rank, and test the layout separately, with no rupees attached |
| Gave the structure before the number | 2 | 2 | Restates before any number and runs the four moves in order |
| Total | 11 | 13 | |

**AI-company variant (the TRAINER file does not score it)**

| Criterion | Mine | TRAINER | Reason |
|---|---|---|---|
| Clarified the scope | 0 | none | No question on what "accept" means (a tap, an add, an item paid for) or what it is compared with |
| Named the denominator and the window | 1 | none | "Per cart" is named; there is no window or test length, and carts are randomised rather than customers |
| Saw the paradox | 1 | none | Says acceptance is flattered by items bought anyway, then scores offline hits, which are those same items |
| Sized it with a unit | 0 | none | No number anywhere |
| Said what would change their mind | 1 | none | An offline gate (beat popularity), and no online result that would stop a launch |
| Tied it to a decision and its cost | 1 | none | Incremental adds times margin, less cost, but no ship rule and no guardrail |
| Gave the structure before the number | 2 | none | The trap first, then the offline step and the online step |
| Total | 6 | none | |

- **Acceptance line 14 fails as the files stand.** Both transcripts score 1 on criterion 2, and finding 1 is a blocker.
- **Arithmetic is clean.** Every number in the material traces to its facts-file id and recomputes within rounding. For example, 60,000 x 0.064 x 0.5 x 9 = 17,280; 0.5018 x 1.2 + 0.4982 x 6.4 = 3.79; 2,000 x 40,000 / (4,800 x 4,920) = 3.39; and 40,000 x 0.15 x 1.5 / 7 = 1,286, which is 18 percent above 1,089. The number problems are about labels and meaning (findings 11, 13 and 25).
- **Public facts, re-fetched today:** W1: Amazon Science. W2: The Register. W4: the Swiggy Q1 FY26 letter (page 13) and the Uber 10-K for 2025. T3: the Swiggy Q1 FY27 letter (page 6 table and footnote); the fetch tool got HTTP 503, so the reader downloaded it directly. Every figure matches its source. The wording claims more than the source says in findings 2, 19, 21, 22 and 24. Findings 14 and 23 make claims no source supports.
- **The files changed while the reader read them.** The Osco hedge and S43's "accepted suggestions" wording were fixed mid-read, and the findings quote the latest text.
- **Nothing was written in the repository.** The only files the reader created are the two Swiggy letters and their text extracts, in the session scratchpad.

1. [blocker] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 3, "a slot at 6.4 percent earns Rs 17,280 a day against Rs 80,197 of sales" | Counts every strip add as caused by the slot, which reads correlation as cause. Never calls the 0.5 add rate or the Rs 9 margin an assumption, though both are assumptions with ranges in the facts file. Gives no range, quotes Rs 80,197 to the rupee from assumed inputs, and makes no recommendation. Fails the spine's own L5 listening line ("incremental adds times margin, less the cost line, with the assumption named"). S42 and the notes each answer the same follow-up differently | "The line people forget is incrementality: some strip adds would have come through search or habit anyway. Assuming 0.5 adds per click and Rs 9 margin, re-ranking milk's half of the slots recovers about Rs 6.3 lakh a month, Rs 3.9 to 9.3 lakh across the ranges, before that share comes off, and only a holdout measures it. Any bundle discount is also paid on carts that would have bought anyway, and sales of about Rs 80,000 a day are no part of the gain." Use this one version in S42 and the notes as well.
2. [improve] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 3, "which is how Swiggy's shareholder letter for April to June 2025 describes Maxxsaver" | Claims more than the source. The letter (question 9, page 13) says the value comes "by funneling back some part of the margins from the larger basket back to the user" and that Maxxsaver "sometimes results in cart-consolidation". It never says the discount is paid on adds that would have happened anyway | "Swiggy's letter describes Maxxsaver as returning part of the larger basket's margin to the user, and says it consolidates carts into fewer orders; that consolidation is discount paid on purchases that would have happened anyway."
3. [improve] extras/C2_W04_D03_interview_STUDENT.md [S] follow-up 1; slides/C2_W04_D03_half2_STUDENT.md S42 row 1; study-notes interview table row 2; trainer/C2_W04_D03_interview_TRAINER.md reply to "why not 0.5?" | "cannot repay a slot shown on every cart page" | The strip depends on what is already in the cart (strip_log has an anchor_item column, and the ticket ranks by the items already in it). An ice-cream rule therefore fills a slot only on ice-cream carts, and it displaces only the next-best suggestion there. 100 carts against 22 expected is not luck either (chi-square near 300 by the reader's arithmetic), so the main answer's "a lift on a few carts can be luck" fails for this pair too | "The pair is real: 100 carts against 22 expected. It fires only on ice-cream carts, 1,600 in four weeks, so it is worth little in rupees. It takes the slot on those carts if it beats the next-best suggestion there, which a test on ice-cream carts settles. My floor guards against noise; what holds this pair back is money."
4. [improve] extras/C2_W04_D03_interview_STUDENT.md [S] follow-up 2; S42 row 2; study-notes row 3 | "They inflate the pairs they repeat ... Amazon's team measured the base rate ... per purchase for the same reason" | The interviewer's premise is breadth: heavy buyers' bigger baskets hold any pair by chance, which is Amazon's W1 mechanism. The answer switches to repetition. Amazon's fix is also different from "count each customer once": the source says the likelihood of buying B "with any given purchase", discounting heavy buyers "according to the heaviness of their buying". The answer never says which lift should rank a strip that is served per cart | "Two effects. Heavy buyers repeat the party pair, with 73 percent of its carts from the top tenth, so I weight each customer once and 3.39 falls to 2.56. Bigger baskets hold any pair by chance, so the expected count should come from each cart's size, which is the cart-level version of Amazon's per-purchase baseline. I rank on 2.56, because heavy buyers add the pair without any prompt."
5. [improve] extras/C2_W04_D03_interview_STUDENT.md | The question ("You have a year of shopping carts") against the hire-grade numbers ("100 carts in four weeks", September's 40,000 carts) | The window is never chosen or squared with the year the interviewer gave, so the 71 percent and the 1 percent floor have no fixed base. A year mixes seasons (ice cream), and a floor counted in carts depends on the window. This is the criterion 2 miss | Add a fourth clarifier and one line: "Which window? I rank on the last four weeks and refresh weekly, because a year mixes seasons; on September's 40,000 Pune carts, milk is in 71 percent."
6. [improve] extras/C2_W04_D03_interview_STUDENT.md hire-grade "The number"; TRAINER [S] "Saw the paradox" cell | "lift is 0.74 over 0.71, 1.04: chance" | At 40,000 carts, 10,064 against 9,656 expected gives a chi-square near 90 (the reader's arithmetic from the facts file's counts). A data-science interviewer will say 1.04 is not chance; the point is that the effect is small | "1.04: bread buyers take milk 4 percent more often than everyone else. At this size that may be real, and it is far too small to spend a slot on."
7. [improve] extras/C2_W04_D03_interview_STUDENT.md hire-grade rows; S41 title "Lift is the count popularity cannot fool" | The question names three measures and the answer explains two | Never says why support fails, and "cannot be fooled" overclaims. Lift's ceiling is one over the partner's share (1 / 0.71, about 1.41 for milk). It rises when carts holding neither item are added. It is symmetric, so it says nothing about direction. After 7 September it is partly counted on carts the strip itself filled | "Support crowns milk as well: bread and milk share 25.2 percent of carts because milk is everywhere. Lift divides that popularity out, but it has blind spots: it is silent on direction (ice cream to sauce 0.06, sauce to ice cream 0.18), it moves with what counts as a cart, and after 7 September it partly measures the strip's own suggestions, so I would check it on a holdout's carts that never saw the strip."
8. [improve] slides/C2_W04_D03_half2_STUDENT.md | S41 weak card against its speaker notes | The card's weak line, "Confidence is the probability they go together", defines support, not confidence. The notes say the weak answer "is not wrong about confidence's meaning", and the transcript's weak line correctly says "the probability of B given A" | Put the transcript's weak line on the card: "Confidence, because it is the probability of B given A, so the highest-confidence pair goes in the strip."
9. [improve] trainer/C2_W04_D03_interview_TRAINER.md | [S] scorecard, column "What earned the hire-grade 2" | Gives credit for lines the answer does not contain. "400 carts": the answer says only "1 percent of carts". "Three questions apart": the hire-grade lines never separate support, confidence and lift. A holdout and a trial as what would change the mind: those are tests, not results that flip the call. Scored on its own lines, the answer makes 10 of 14 | Rescore against the lines as written, or add the missing lines to the answer, for example: "If chips and cold drink fell near one per customer, or the trial left the pair below the slot's own click-through, I would drop it."
10. [improve] trainer/C2_W04_D03_interview_TRAINER.md [D] "Answer" row and follow-up 1; slides/C2_W04_D03_fallback_STUDENT.md S11 Answer and What-would-change cards, S12 caption and chart | How the fall happened | Never names the mix: milk's share of impressions went from 2 to 50 percent. "The fall sits in milk's slots" and "had the non-milk slots fallen with milk's" imply milk's rate fell, but milk clicked 1.2 percent before the change too. "6.4 against 6.2" compares a set pushed into lower slots, while slot by slot the rest rose 7.5 to 8.2, 6.1 to 6.7 and 4.9 to 5.4. S11's "every other slot 6.4" means every other suggestion. S12's "would have stopped clicking everything" is a straw man, and its chart shows rates with no impression shares, so it cannot show the mix that made the blend | "No rate fell; the mix moved. Milk went from 2 to 50 percent of impressions and clicked 1.2 percent before and after. The other suggestions rose in every slot, 7.5 to 8.2 in slot 1, and half at 1.2 with half at 6.4 is 3.8. Every day before the switch sat between 5.8 and 6.4 percent, every day after between 3.6 and 4.0. I cannot prove the monsoon did nothing, and the fall does not need it."
11. [improve] trainer/C2_W04_D03_interview_TRAINER.md [D] "Concede" row; fallback S11 Concede card; S12 chart title "Slot 1 draws the most clicks"; notes six-doubts row | "slot 1 draws 8.2 percent against 5.4 for slot 3" | True only of suggestions other than milk. Counting milk, slot 1 now draws about 3.4 percent and slot 3 about 4.0 (the reader's arithmetic from the facts file's slot shares and rates), so a manager with the dashboard will contradict it. Slot 1 also holds the top-ranked suggestion, so the gap mixes position with relevance | "Among suggestions other than milk, slot 1 draws 8.2 percent against 5.4 for slot 3. Part of that is position and part is that slot 1 holds the strongest suggestion; a test that shuffles the order separates the two."
12. [improve] trainer/C2_W04_D03_interview_TRAINER.md [D] "Next step" row and follow-up 2; fallback S2 and S4 (the trial zone against "the zone left as it is"); [S] follow-up 1 "two-zone trial" | How the tests are designed | The re-rank ships untested, though [S] says cause needs a holdout. A two-zone test is one treated zone against one control zone, so any zone shock reads as the effect (the curd stock-out hit two zones). Two changes can run in the same weeks as a 2 by 2 randomised by customer, so "then neither can be credited" holds only for a blind launch | "Neither ships blind. Ranking (count or lift) and layout (old or two-row) run as a 2 by 2 randomised by customer across Pune, so each effect and their interaction are measured in the same weeks, and the re-rank arm doubles as the holdout that shows the ranking caused the fall."
13. [improve] trainer/C2_W04_D03_interview_TRAINER.md | [D] scorecard ("Sized it with a unit" 2, "Named the denominator and the window" 2) and the closing cost note | The [D] answer quotes rates only, never sizes the fall, and never states the windows or the impression mix. The note's "Rs 6.3 lakh a month recovered" for a 2 has no range. It also uses a flat 6.4 against 1.2, though the same answer cites slot 1 at 8.2 and milk holds 70 percent of slot 1. Weighting by slot gives about Rs 7.3 lakh if replacements click at each slot's current rate (the reader's arithmetic) | Score sizing 1 and denominator 1 (11 of 14), and write the line for a 2 as "about Rs 6.3 lakh a month, Rs 3.9 to 9.3 lakh across the add-rate and margin ranges, and more once milk's 70 percent of slot 1 is weighted".
14. [improve] slides/C2_W04_D03_fallback_STUDENT.md | S11 Restate card, "The monsoon ended inside the window" | Asserts a real weather event over Pune between 17 August and 27 September 2026, with no source in the sources file. Wednesday's ticket does not carry it, and the case file has only the manager believe it | Restate it as the manager's view: "You think shoppers changed when the monsoon ended." Or source the IMD withdrawal date with its check date.
15. [improve] extras/C2_W04_D03_interview_STUDENT.md AI variant; half2 S43 | The offline step ("count how often each suggestion lands in the held-out cart ... which is lift over the base rate"; S43 "its lift is how often its suggestions land in those carts, over how often the most popular items would") | A hit in a held-out cart is an item the shopper bought with no suggestion at all, which is exactly the bought-anyway behaviour the variant warns about. Beating popularity offline can therefore reward an assistant that predicts habits and adds nothing, and gating on it can reject one that suggests new items. A ratio of hit rates is also not association lift | "Offline is only a sanity gate: hide one item in each held-out cart, check that the assistant recovers it more often than a popularity list does, and leave out items the shopper buys every week. The online test decides whether it earns its place."
16. [improve] extras/C2_W04_D03_interview_STUDENT.md AI variant; half2 S43 | Baseline and split ("a popularity baseline that always suggests the most common items"; "past carts it never saw while it was built") | A global popularity list is the floor, and the bar is the current strip. Carts held out at random let the model see the future. W1 is the sourced case: a bestseller list beat Prime Video's autoencoder until the test was made chronological | "I compare it with the current strip and with a popularity list, on carts placed after a cutoff date. Amazon's Prime Video team learned this when a bestseller list first beat their autoencoder (Amazon Science, W1)."
17. [improve] extras/C2_W04_D03_interview_STUDENT.md AI variant; half2 S43 node C and prose | The online step ("assistant on half the carts and the baseline on the other half ... incremental adds per cart times margin"; "the ones that would not have happened without it") | Randomises carts, though one customer places many (the top tenth place 38 percent), so one shopper sits in both arms. A popularity arm cannot count adds that "would not have happened without it"; that needs an arm with no suggestions. Adds are not purchases. There is no guardrail (checkout conversion, latency, out-of-stock or off-catalogue suggestions), and no test length fixed in advance despite the novelty effect | "Customers are randomised into three arms, no suggestions, the current strip and the assistant, for a length fixed before launch. The metric is incremental margin per customer on items kept at payment, less inference cost. The guardrails are checkout conversion, latency and the share of suggestions out of stock in that dark store."
18. [improve] extras/C2_W04_D03_interview_STUDENT.md AI variant; trainer/C2_W04_D03_interview_TRAINER.md | The variant as a whole | No clarifying question, no number anywhere, and no TRAINER score. On the day's seven criteria it makes 6 of 14, so it reads as a model answer without being hire-grade | Open with "Accepted how: tapped, added or paid for? And how many of those carts held the item anyway?", size one quantity with a range (incremental margin per customer a week), and score the variant in the TRAINER file.
19. [improve] trainer/C2_W04_D03_guesstimate_TRAINER.md "Validate" and "The catch"; study-notes guesstimate paragraph | "1,089 orders per dark store per day across 1,171 stores" | Claims more than T3 says. 1,171 is "Active Dark Stores (Exit)", the stores with an order on the quarter's last day, while 1,089 is averaged over active store-days. The letter counts completed orders, but the clarify step estimates orders placed. The catch "a new store does not pull the average down before it opens" states the obvious and never draws the consequence: a mature metro store should sit above an all-store average that includes stores still ramping up | "Swiggy reported 1,089 completed orders per active store-day in the quarter to June 2026, a quarter it ended with 1,171 stores. That average includes young stores still ramping up and small-city stores, so a mature Pune store 18 percent above it is what I would expect."
20. [improve] trainer/C2_W04_D03_guesstimate_TRAINER.md | The "Map" and "Assume" steps | The 40,000 households are asserted, not built from a delivery radius and a density. The 15 percent weekly share folds two things into one number: quick-commerce adoption, and this app's share against Blinkit and Zepto. The 430 to 2,860 range multiplies every extreme together. No input is named as the one that moves the answer most, and the estimate is never re-solved against the anchor | "The catchment is the delivery radius times households per square km. The weekly share is the households using quick commerce times Instamart's share of them. My least certain input is that share, and landing on 1,089 needs about 13 percent, which I find believable." The 13 percent is the reader's arithmetic and would need a facts entry.
21. [improve] extras/C2_W04_D03_interview_STUDENT.md | Pain-point row 4 (Uber): the check "Heavy users are the ones who try both, so using both did not by itself cause the bookings", and "for 2025" | The check swaps one unproven causal claim for another; the 10-K says nothing about who tries both. The figure covers only the three months ended 31 December 2025, in countries offering both services, which "for 2025" hides | Check: "Ask who chose to use both, and compare the same consumers before and after they added a second product." Case: "...in the fourth quarter of 2025, where both were offered."
22. [improve] extras/C2_W04_D03_interview_STUDENT.md pain-point rows 1 and 2; study-notes chapter 1 IN THE FIELD | "Amazon's team wrote" and "Amazon's recommendation team wrote" | The source is an Amazon Science article (Larry Hardesty, 2019, per R2) that tells the team's story; the words are the article's, not the team's | "Amazon Science's history of the algorithm says counting co-purchases would make bestsellers like Harry Potter books and trash bags the top recommendation for every customer."
23. [improve] slides/C2_W04_D03_half2_STUDENT.md | SECTION 4 subtitle, "as Uber, Swiggy, Google or an AI startup would ask it" | Claims to reproduce company screens. The case file says company interview reports were not verified and that no transcript may claim to reproduce a company's screen | "How does a strong candidate answer the day's question in a product-analytics screen?"
24. [improve] internal/C2_W04_D03_sources_INTERNAL.md | W2 row, "no shelf moved ... All four points" | The Register hedges: Osco "does not appear to have exploited the information by moving the products around". The learner files now carry the hedge, but this row still records the unhedged claim as confirmed | "Osco does not appear to have moved any products (hedged in the source)."
25. [improve] whiteboards/C2_W04_D03_ctr_by_slot_STUDENT.png (fallback S12) | Bar labels and legend | Slot 2's after bar prints 6.8, where its facts entry (ctr_after_other_slot2, 0.0675) prints 6.7. The legend "before, every suggestion" labels slot 3's 4.9, which the facts file records as suggestions other than milk | Print 6.7 from the facts entry's shown form, and label the before bars "before, everything else".

## What became of each interviewer finding?

| Finding | Outcome |
|---|---|
| 1 | The transcript's third follow-up, S42, the notes and the day sheet carry one incrementality line with its range and its holdout |
| 2 | The transcript keeps the letter's words and states the discount on bought-anyway purchases as the analyst's reading; the sources list says so |
| 3 | The anchor-based reason, 100 carts against 22 and 1,600 ice-cream carts, in S30, S42, notebook 03, the notes, the transcript, the quiz, the four-pairs solution, the pair cards, the run sheet and the day sheet |
| 4 | The transcript, S42 and the notes name both effects; Amazon's per-purchase baseline is quoted from the source. The re-check (its finding 5) found the size effect named and never applied, so the answer now applies both |
| 5 | A fourth clarifier fixes the window; the hire-grade line names September's 40,000 carts |
| 6 | 1.04 reads as a 4 percent pull, possibly real and too small for a slot |
| 7 | The hire-grade answer says why support fails and names lift's limits; S41's title changed |
| 8 | S41's weak card uses the transcript's line |
| 9 | The answer gained the missing lines (three questions, 400 carts, the result that flips it) and the TRAINER file was rescored against them |
| 10 | The [D] answer, follow-up 1, fallback S11 and S12 say the mix moved, with the windows and the daily band; the re-check (its finding 3) replaced "no rate fell" with milk's slot-3 slip |
| 11 | The non-milk qualifier and position against relevance in [D], S11, S34, the notes and the chart's title |
| 12 | Partly: [D] runs a two-by-two randomised by customer; the watch-list trial stays in two zones as the spine sets it, with shoppers randomised inside them |
| 13 | [D] sizes the gain with its range and is rescored against its lines; the slot-1 weighting was cut after the re-check (its finding 2) |
| 14 | S11's restate card gives the manager's view |
| 15 | The offline step is a gate that hides one item and leaves out weekly staples, in the transcript and S43 |
| 16 | The current strip and a popularity list on carts after a cutoff date; the Prime Video case is quoted from the source |
| 17 | Customers randomised to three arms for a fixed length, margin per customer on items kept at payment, three guardrails |
| 18 | The variant opens on clarifiers and the TRAINER file scores it; after the re-check (its finding 6) it sizes its own serving cost |
| 19 | Completed orders per active store-day, a quarter ending on 1,171 active stores across 131 cities, in the guesstimate and the notes |
| 20 | The map builds the catchment and the share; the least certain input is named with its reason, and the 13 percent back-solve sits in Validate after the re-check (its finding 7) |
| 21 | The Uber check compares the same consumers before and after; the case says the last quarter of 2025, where both were offered |
| 22 | Amazon Science's history, never the team's words, in S21, the notes, the transcript and the three-counts solution |
| 23 | Section 4's subtitle names a product-analytics interview |
| 24 | The sources list's W2 row carries the hedge |
| 25 | The chart prints the facts file's shown forms and labels the before bars everything else |

## Which findings were not fixed in full, and why?

- Graduate 59: the lab's your-turn cells carry sanity checks but no expected values, because the plants must be found in an empty cell (decision `w4-finding-once-found`, acceptance line 13); the TA lab note holds the numbers.
- Graduate 69: the pre-read stays terms only, as the spine sets it; the line showing how 38 percent can be a mix is Thursday's lesson.
- Graduate 55: the quiz keeps the counts and gives item 2 sixty seconds, because computing lift from three counts is the skill the item tests.
- Interviewer 12, in part: the watch-list trial stays in two zones, as the spine's fallback protocol sets it, with shoppers randomised inside those zones.

## Did the fixes hold under a second, narrow read?

A third agent, told to read as a second hiring interviewer and to write findings only, read the
interview material after the fix pass on 12 October 2026. Its report is copied as it returned it.

Findings: 7

Spine section 12, line 8 passes. The pack has both transcripts in the required shape, the AI variant, the TRAINER scorecards, the guesstimate with its anchor and catch, and five anchored pain points. Line 14 passes its first half, since all three hire-grade answers score 2 on criteria 1 to 3. It fails its second half until findings 1 and 2 are fixed.

**[S] hire-grade answer, with its follow-ups**

| Criterion | Score | Reason |
|---|---|---|
| Clarified the scope | 2 | Four clarifiers (what a basket is, the window, choosing versus measuring, how many carts the rarest pair sits in), each tied to what it decides |
| Named the denominator and the window | 2 | Milk is in 71 percent of September's 40,000 carts, ranked on the last four weeks and refreshed weekly; follow-up 2 adds the per-customer count |
| Saw the paradox | 2 | The 0.74 confidence is just milk's own 0.71 (lift 1.04), while the weak-looking 0.42 hides a lift of 3.39 |
| Sized it with a unit | 2 | A 400-cart floor, 100 carts against 22, and Rs 6.3 lakh with its range; only the thin pair's "worth little" has no number |
| Said what would change their mind | 1 | The per-customer test is sound. The causal test compares clicks with shoppers who were never shown the pair, so it can never trigger |
| Tied it to a decision and its cost | 2 | The ranking rule, the watch list, incrementality and the bundle discount are named as cost lines, and sales are kept out of the gain |
| Gave the structure before the number | 2 | Support, confidence and lift are kept apart, and the base rate is named before any figure |
| Total | 13 of 14 | |

**[D] hire-grade answer**

| Criterion | Score | Reason |
|---|---|---|
| Clarified the scope | 2 | Asks which windows and how each slot's mix changed, what else shipped on 7 September, and whether the redesign replaces the fix or runs beside it |
| Named the denominator and the window | 2 | Uses share of impressions, 2 against 50 percent, with dated windows |
| Saw the paradox | 2 | The blended rate fell from 6.1 to 3.8 while milk held 1.2 and the other suggestions rose in every slot; "no rate fell" goes too far at slot level (finding 3) |
| Sized it with a unit | 2 | Rs 6.3 lakh a month with its range; daily bands of 5.8 to 6.4 before against 3.6 to 4.0 after |
| Said what would change their mind | 2 | If the other suggestions had fallen with the blend, the habits story would lead; the monsoon is left unproven either way |
| Tied it to a decision and its cost | 1 | The two-by-two test with customers randomised is right, but no metric is named for it and its worth is the uncut ceiling plus "and more" |
| Gave the structure before the number | 2 | Restate, answer, concede, what would change it, next step, in that order |
| Total | 13 of 14 | |

**AI-company variant**

| Criterion | Score | Reason |
|---|---|---|
| Clarified the scope | 2 | Asks whether "accepted" means tapped, added or paid for; how many carts held the item anyway; and whether the comparison is the strip or no suggestions |
| Named the denominator and the window | 2 | Online: customers, over two full weeks fixed before launch. Offline: carts after a cutoff date, though still averaged per cart |
| Saw the paradox | 2 | Acceptance flatters the assistant the way confidence flattered milk; weekly staples are left out of the offline gate |
| Sized it with a unit | 1 | Its only rupee figure is the strip re-rank's uncut ceiling; the assistant's serving cost and the gain it must clear are not sized |
| Said what would change their mind | 2 | It does not ship if its arm fails to beat the strip's arm or a guardrail moves |
| Tied it to a decision and its cost | 2 | Incremental margin per customer on items kept at payment, less serving cost, with three guardrails |
| Gave the structure before the number | 2 | Clarifiers, the trap, the offline gate, the online test, then the number |
| Total | 13 of 14 | |

**First-read points: fixed or not**

1. [S] window: fixed. Clarifier 2 ranks on the last four weeks, refreshed weekly, and the answer reads milk's 71 percent on September's carts. It no longer says the 40,000 carts are a sample.
2. Rupee follow-up counting every strip add as caused: fixed in [S] and S42, which now call Rs 6.3 lakh a ceiling that a holdout measures. Not fixed in [D] (finding 2) or in the AI variant's "for scale" figure (finding 6).
3. Thin pair's reason: fixed. "Real, 100 against 22" and "only beside ice cream" replace the every-cart-page reason. Its 1,600 carts is the sample's count, set against rupees computed on city-wide views (finding 4).
4. Heavy buyers' two effects: half fixed. Both effects are named, but only repetition is applied ("I rank on 2.56", finding 5).
5. [D] impression mix and windows: fixed. The clarifier and the answer give 2 and 50 percent with dated windows, plus the daily bands.
6. Slot 1's 8.2 percent applies only to suggestions other than milk: fixed in the [D] Concede row, S11 and S25, and position is now separated from suggestion strength.
7. Zone-level tests: fixed. [D], S12, S43 and the AI variant randomise customers, and the watch-list trial splits shoppers at random inside two zones.
8. AI variant: mostly fixed. It now has clarifiers, excludes weekly staples, splits on a cutoff date, randomises customers, and has three guardrails, a ship rule and a TRAINER score. Still open: its number is the borrowed, uncut strip ceiling (finding 6), and the offline gate still averages per cart.
9. Guesstimate: the anchor is fixed (completed orders per active store-day, 1,171 stores at the quarter's end). The least certain input is named, but the reason given rests on a back-solve made before the anchor is revealed (finding 7).

**Numbers check**

Every figure in [S], [D], the AI variant and the guesstimate matches the facts file at its printed rounding, and recomputing from strip_log reproduces the strip figures. There are three exceptions:
- "131 cities" has no facts-file id; it appears only in the sources file's T3 row.
- "Milk 1.2 percent in both windows" pairs ctr_before_milk_slot3 (slot 3 only) with milk_slot_ctr_after (all slots blended); see finding 3.
- "The Rs 80,197 of daily sales" in [S] follow-up 3 is gross_sales_day, one slot's gross sales a day at 6.4 percent, and the transcript never says so. "No part of the gain" is also loose, because the Rs 17,280 margin sits inside that figure.

**Findings**

1. [blocker] extras/C2_W04_D03_interview_STUDENT.md | [S] hire-grade, "What would change the call" (the same line is in the TRAINER scorecard's criterion 5; fallback S4's pass rule has the same flaw) | "Shoppers shown the pair clicked it no more than shoppers who were not" cannot work: shoppers never shown the pair have no strip click to make, so the test can never trigger and says nothing about cause. S4 likewise promotes on slot click-through and strip adds | "...or if chips buyers shown cold drink in the strip buy it no more often than chips buyers in a holdout who never see the strip, I would drop it"; and for S4: "promote only if ice-cream carts in the shown half carry more margin than the other half's, by a gap set before the trial."
2. [blocker] trainer/C2_W04_D03_interview_TRAINER.md | [D] hire-grade, "Next step, and its worth" | "Re-ranking alone is worth about Rs 6.3 lakh a month ... and more once milk's 70 percent of slot 1 is weighted" counts every strip add as caused, which is the first read's blocker back in [D]. It also adds unpriced upside from a slot-1 rate that the Concede row just said is partly the strongest suggestion, and it never says what the two-by-two test is measured on | "Re-ranking is worth up to Rs 6.3 lakh a month, Rs 3.9 lakh to Rs 9.3 lakh, before the adds that would have come anyway; every arm is read on margin per customer from items kept at payment, over two weeks fixed in advance, with checkout conversion as the guardrail, so the count-ranking arms measure that share."
3. [improve] trainer/C2_W04_D03_interview_TRAINER.md | [D] Answer row, "No rate fell ... clicking 1.2 percent in both windows" (also fallback S11 and S12) | The "before" 1.2 is milk in slot 3 only; the "after" 1.2 blends 1.4, 1.1 and 0.9. Milk in slot 3 fell from 1.2 to 0.9, and strip_log shows the identical cell (atta to milk, slot 3) also falling from 1.2 to 0.9. The answer splits the other suggestions by slot but blends milk, which is the day's own trap | "The mix moved: milk went from 2 to 50 percent of impressions at about 1 percent while the others rose in every slot; milk's old cell, slot 3, slipped from 1.2 to 0.9, too little to move the blend."
4. [improve] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 1 (also half1 S30 and half2 S42) | "1,600 carts over four weeks" is the count in the 40,000-cart sample (S1: every cart of 12,000 customers), yet the slot's rupees are computed on 60,000 city views a day. "Worth little" has no figure. On 1,600 carts, the two-zone, half-split, two-week trial gets about 100 ice-cream carts per arm. And "the floor guards against noise" does not fit a floor that excludes a pair at 100 against 22 | "Ice cream is in 4 percent of carts, about 2,400 of the strip's 60,000 daily views, so even in place of milk the rule earns at most about Rs 17,000 a month, 4 percent of a slot's Rs 4.2 lakh; the 1 percent floor is doing a money job here, and the trial runs on city traffic" (add 2,400 and Rs 17,000 to the facts file).
5. [improve] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 2 (also half2 S42) | The answer names the basket-size effect, then says "I rank on 2.56", which corrects only repetition. I recounted from cart_items with expected counts stratified by cart size: chips and cold drink 2.48, coriander and chillies 2.25, bread and butter 1.74, onions and tomatoes 1.38. So the named effect moves three of the four lifts more than the per-customer fix does, and it drops the first replacement below the 1.5 bar | "Sized by each cart's item count, chips and cold drink still read about 2.5 and onions and tomatoes fall below 1.5, so I rank on the size-adjusted lift and the first replacement changes" (add the four values to the facts file).
6. [improve] extras/C2_W04_D03_interview_STUDENT.md | AI-company variant, the "For scale" line and the Prime Video sentence | The only rupee figure is the strip re-rank's uncut ceiling, so the assistant's own bar is never sized. Separately, "scored on the fortnight that followed" is not in the sources file's checked W1 row | "At the strip's 60,000 cart views a day, every 10 paise of serving cost is Rs 1.8 lakh a month, so at 35 paise the assistant spends all Rs 6.3 lakh a re-rank could recover; it ships only if its incremental margin over the strip clears that cost"; and either add the fortnight clause to the W1 row with its check date, or cut it.
7. [improve] trainer/C2_W04_D03_guesstimate_TRAINER.md | Calculate row and the catch | "Landing on 1,089 needs about 13 percent" quotes the anchor before the Validate row reveals it. The share and orders-per-week each swing the answer from about 860 to 1,710, so the range does not single out the share. "A mature Pune store" is scoped only after the reveal. "131 cities" has no facts-file id | Calculate: "About 1,290 a day; my least certain input is the share, since it stacks two guesses, adoption and Instamart's slice, and on its own it moves me from about 860 to 1,710"; Clarify scopes "a mature store in a large city"; the 13 percent back-solve moves to Validate; 131 gets a facts-file id.

### What became of each re-check finding?

| Finding | Outcome |
|---|---|
| 1, blocker | [S]'s "what would change the call" compares chips buyers shown cold drink with chips buyers in a holdout who never see the strip; the TRAINER criterion 5 line matches; fallback S2, S3 and S4 promote only if shoppers in the shown half earn more margin on their ice-cream carts than the other half, by a gap set before the trial, and S3's data request is each shopper's half; S30, notebook 03, the notes and the day sheet carry the same margin rule |
| 2, blocker | [D]'s next step says up to Rs 6.3 lakh, Rs 3.9 lakh to Rs 9.3 lakh, before the adds that would have come anyway, reads every arm on margin per customer from items kept at payment over two weeks fixed in advance, with checkout conversion as the guardrail, and takes the lift arms against the count arms as the re-rank's worth; the slot-1 weighting is gone; criteria 4 and 6 are rescored against these lines |
| 3 | [D]'s answer, fallback S11 and S12: milk held 2 percent of impressions, all in slot 3, then 50 at 0.9 to 1.4 percent, and its old cell slipped from 1.2 to 0.9, too little to move the blend; checked against `strip_log` (slot 3, beside atta, 888 clicks on 73,985 impressions before; 3,416 on 378,988 after) |
| 4 | [S] follow-up 1, S30, S32's notes, S42, notebook 03, the notes and the day sheet: ice cream is in 4 percent of carts, about 2,400 of 60,000 views a day, so in place of milk the rule earns about Rs 17,000 a month, 4 percent of a full slot's Rs 4.2 lakh, and the floor does a money job there; new facts `ice_cream_views_day` and `thin_rule_month` |
| 5 | [S] follow-up 2 and S42 apply both effects: sized by cart, chips and cold drink 2.48 and onions and tomatoes 1.38; corrected for both, 1.95 and 1.38, so chips and cold drink keeps its slot and onions and tomatoes no longer earns one; the generator recounts all six values and checks them (`*_lift_size`, `*_lift_both`); the notes' self-check item 5 now asks for the per-customer lift and why it falls, so it no longer calls 2.56 the number to quote |
| 6 | The AI variant sizes its own bar: every 10 paise of serving cost a view is Rs 1.8 lakh a month, so at 35 paise it spends the whole Rs 6.3 lakh a re-rank could recover, and it ships only if its margin over the strip's arm clears that cost; the offline gate counts each customer once; the Prime Video sentence now follows the article (a list of the past two weeks' most popular rentals; trained before a cutoff, scored on the two weeks after it), refetched and added to the sources list's W1 row |
| 7 | The guesstimate's Clarify row scopes a mature store in a large city; Calculate names the share as least certain because it stacks two guesses, moving the answer from about 860 to about 1,710 on its own, as orders a week do; the 13 percent back-solve moved to Validate; `instamart_cities` is a fact, checked against the letter's own text |
| Numbers check, third point | [S] follow-up 3 now says the gain is margin: a slot's adds ring up Rs 80,197 of sales a day, of which only the Rs 17,280 margin counts |

**Scores after the fixes.** The re-check scored each hire-grade answer 13 of 14 before these fixes,
with criterion 5 of [S], criterion 6 of [D] and criterion 4 of the AI variant at 1. The confirmation
read below scored the result.

## Did a third read confirm the fixes, and what did it still find?

A fourth agent, told to read as a hiring interviewer and to write findings only, read the interview
material after the re-check's fixes on 12 October 2026, recomputing every number from the data. Its
report is copied as it returned it.

Findings: 8

| Re-check finding | Holds? | Evidence |
|---|---|---|
| 1 Falsifier, S4 rule | Yes | [S] and TRAINER criterion 5 compare chips buyers shown cold drink with a holdout that never sees the strip. That is a yes-or-no read that can fire. S4 compares the two halves on margin per shopper. The metric S4 uses is a new problem (blocker 2) |
| 2 [D] next step | Yes | "Up to Rs 6.3 lakh ... before the adds that would have come anyway"; every arm is read on margin per customer from items kept at payment; the slot-1 upside is gone |
| 3 Milk's slot 3 | Yes | [D], S11 and S12 say 1.2 to 0.9. strip_log: 888/73,985 = 1.20 percent before, atta to milk 201/22,213 = 0.90 after |
| 4 Thin pair on city views | Yes | 60,000 x 4 percent = 2,400 views a day; Rs 16,848 a month. The margin it uses is wrong (blocker 1) |
| 5 Both heavy-buyer effects | Yes | Recomputed from the CSVs: by cart size 2.48 and 1.38, both effects 1.95 and 1.38, per customer 2.56, top tenth 73 percent |
| 6 AI sizing, Prime Video | Yes | Rs 1.8 lakh and 35 paise both recompute. The sentence matches the W1 row, and the article refetched today reads "the two-week period after the cutoff time". The arm it is compared against is a new problem (blocker 3) |
| 7 Guesstimate | Partly | The store is scoped in Clarify, the back-solve sits in Validate and a reason is given, but the ranges contradict that reason (improve 8) |

**[S] with follow-ups**

| Criterion | Score | Reason |
|---|---|---|
| Clarified the scope | 2 | Four clarifiers, each tied to what it decides |
| Named the denominator and the window | 2 | Milk's 71 percent over the last four weeks, refreshed weekly |
| Saw the paradox | 2 | 0.74 is milk's own 0.71, and 0.42 hides a lift of 3.39 |
| Sized it with a unit | 1 | The 400 carts and Rs 6.3 lakh with its range hold; the thin pair's Rs 17,000 is about five times too low |
| Said what would change their mind | 2 | Per-customer lift near one, or no gain over the holdout |
| Tied it to a decision and its cost | 1 | The watch list rests on a trial that cannot detect its own effect |
| Gave the structure before the number | 2 | The three questions kept apart, base rate first |
| Total | 12 of 14 | TRAINER claims 14 |

**[D]**

| Criterion | Score | Reason |
|---|---|---|
| Clarified the scope | 2 | Both windows and each slot's mix, what else shipped, replace or run beside |
| Named the denominator and the window | 2 | 2 and 50 percent of impressions, with dates |
| Saw the paradox | 2 | The blend fell while the other suggestions rose in every slot |
| Sized it with a unit | 2 | Rs 6.3 lakh as a ceiling with its range, plus the daily bands |
| Said what would change their mind | 2 | The other suggestions falling with the blend |
| Tied it to a decision and its cost | 2 | Two-by-two read on margin per customer; lift arms against count arms |
| Gave the structure before the number | 2 | The four moves in order |
| Total | 14 of 14 | |

**AI variant**

| Criterion | Score | Reason |
|---|---|---|
| Clarified the scope | 2 | Tapped, added or paid; carts that held the item anyway; compared with what |
| Named the denominator and the window | 2 | Per customer, a cutoff date, two full weeks |
| Saw the paradox | 2 | Acceptance flatters the assistant as confidence flattered milk; staples left out |
| Sized it with a unit | 2 | Rs 1.8 lakh a month per 10 paise, 35 paise to break even |
| Said what would change their mind | 2 | A ship rule with three guardrails |
| Tied it to a decision and its cost | 1 | Measured against the count-ranked strip, it gets credit for the re-rank's Rs 6.3 lakh |
| Gave the structure before the number | 2 | Trap, offline gate, online test, then the number |
| Total | 13 of 14 | TRAINER claims 14 |

**Findings**

1. [blocker] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 1 (also half2 S42 row 1 and facts `thin_rule_month`) | Rs 17,000 prices every sauce add and every lost milk add at the Rs 9 basket average. cart_items gives chocolate sauce a margin of Rs 37.40 a unit and milk Rs 2.00. On the answer's own click assumption the pair earns about Rs 85,000 a month, 20 percent of a slot's Rs 4.2 lakh, so "4 percent" and "the floor is doing a money job" do not follow | Price each add at its own item's margin and restate what the pair is worth and what the floor is for (the same shortcut makes Rs 6.3 lakh cautious: it is Rs 7.5 lakh with milk at Rs 2).

2. [blocker] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 1 (also half2 S42 row 1, fallback S2 to S4 and S4's notes) | The pass rule reads whole-cart margin, which has a standard deviation of Rs 28 across the sample's 1,600 ice-cream carts. At the answer's own Rs 0.23 a cart, 80 percent power needs about 227,000 ice-cream carts an arm. That is about two years at the roughly 300 a day each arm gets in two zones. Even at sauce's own margin it needs about 8,800 an arm, or 35,000 if half the adds would have come anyway | Read the trial on whether each ice-cream cart buys sauce (about 1,100 carts an arm at the full effect and 4,000 at half, which is 4 to 14 days), keep margin per shopper as the guardrail, and fix the length from that count before day one.

3. [blocker] extras/C2_W04_D03_interview_STUDENT.md | AI variant (also half2 S43, the TRAINER AI scorecard, the notes and the day sheet) | The assistant ships if its margin beats "the current strip", the count-ranked strip that shows milk on half its impressions. That credits it with the Rs 6.3 lakh a free re-rank recovers. An assistant that only matches the re-rank ships at 20 paise a view and loses Rs 3.6 lakh a month against the re-ranked strip | Add the lift-ranked strip as an arm and ship only if the assistant's margin over that arm clears its serving cost.

4. [improve] extras/C2_W04_D03_interview_STUDENT.md | [S] "The window and the number" | "September's 40,000 Pune carts" reads as the city's total next to the later "60,000 views a day", but the 40,000 are every September cart of 12,000 sampled customers | Say "a sample of 40,000 carts from 12,000 customers".

5. [improve] extras/C2_W04_D03_interview_STUDENT.md | [S] follow-up 2, "the 1.5 I set for a slot" | The answer only ever sets the 1 percent floor, never a 1.5 bar | Add "and a lift of at least 1.5" to the floor line.

6. [improve] trainer/C2_W04_D03_interview_TRAINER.md | [D] Answer row and follow-up 1 | "Rose in every slot" mostly compares different suggestions, since only four cells other than milk run in both windows. "Whatever the monsoon did, it did not lower clicks on them" claims a cause from a before-and-after count | Cite those four cells, which rose 8 to 12 percent, and say "net of whatever the monsoon did".

7. [improve] trainer/C2_W04_D03_interview_TRAINER.md | [D] next step (also the AI variant's two weeks) | If each cart sees the strip once, re-ranking is worth about Rs 0.59 a customer a fortnight at the ceiling. The sample's fortnightly margin per customer has a standard deviation of Rs 87, so the ranking comparison needs about 340,000 customers a side, and four times that at half the effect | State the count the test needs, or read margin on the suggested items with each customer's earlier margin as a covariate.

8. [improve] trainer/C2_W04_D03_guesstimate_TRAINER.md | Map, Assume and Calculate rows | The share is called least certain because it "stacks two guesses", yet its 10 to 20 percent range is no wider than the 1 to 2 range for orders a week. The map's radius and density never get values | Give adoption and Instamart's slice their own ranges so the share's range comes out wider, and show the radius and density behind the 40,000 households.

Method: read only, no repository file was changed. Every number was recomputed with pandas from content/W04/D3/data/, and the Amazon Science article was refetched for the Prime Video and heavy-buyer passages.

### What became of each confirmation finding?

| Finding | Outcome |
|---|---|
| 1, blocker | Checked against `cart_items`: sauce keeps Rs 37.40 an add and milk Rs 2. The thin pair is priced at its own margins, about Rs 85,000 a month (`thin_rule_month`, `sauce_margin`), and the claim that the floor does a money job is gone; [S] follow-up 1, S30, S32's notes, S42, notebook 03, the notes, the day sheet and the TRAINER scorecard say so. The third follow-up adds that milk at its own Rs 2 makes the re-rank about Rs 7.5 lakh, so Rs 6.3 lakh is the cautious figure (`recoverable_month_milk_own`) |
| 2, blocker | Checked: a whole ice-cream cart's margin has a standard deviation of Rs 28.12 on 1,600 carts. The watch-list trial now reads whether ice-cream carts buy sauce, shown half against the other half, with margin per shopper as the guardrail and the length fixed from the count before day one, in [S] follow-up 1, S30, S42, notebook 03, the notes, the day sheet, fallback S2 to S4 with S4's notes, and the fallback note; the TRAINER file gives the counts, about 1,100 ice-cream carts an arm for the full effect and about 4,000 for half (`trial_n_full`, `trial_n_half`), and leaves the method to the faculty session (tentative) |
| 3, blocker | The AI variant's arms are no suggestions, the strip re-ranked by lift, and the assistant; the offline gate beats a popularity list and the re-ranked strip; it ships only if its margin over the re-ranked strip's arm clears its serving cost; the clarifier asks for the best strip shippable without it. Changed in the transcript, S43 and its notes, the TRAINER scorecard, the notes and the day sheet |
| 4 | The window line says "September's sample of 40,000 Pune carts, every cart of 12,000 customers" |
| 5 | The floor line sets the 1.5 bar beside the 1 percent floor |
| 6 | Checked: four anchor, suggestion and slot cells other than milk run in both windows, and each rose 8 to 12 percent (`same_cells`, `same_cells_rise_low`, `same_cells_rise_high`, with a generator check). The [D] answer cites them, and follow-up 1 now says the fall cannot come from shoppers clicking less on the same suggestions, with no claim about the monsoon |
| 7 | [D] reads margin per customer adjusted for each customer's margin in the weeks before, with the length fixed from the count before launch; the AI variant runs at least two full weeks and as long as its count needs |
| 8 | The guesstimate builds the catchment from a 2.5 km radius at about 2,000 households a square km, and the share from two guesses with their own ranges (30 percent using quick commerce, 20 to 40; half of them Instamart's, 35 to 65 percent), so the share runs 7 to 26 percent and alone moves the answer from about 600 to about 2,230 against about 860 to about 1,710 for orders a week; the full range is about 300 to about 3,710, and the notes carry the same ranges |

**Scores after these fixes.** The confirmation read scored [S] 12, [D] 14 and the AI variant 13 of
14, and every point it withheld traces to blockers 1 to 3, now fixed, so the TRAINER file scores all
three at 14. That rescoring is the builder's own, made against the read's stated reasons; no fifth
read ran.
