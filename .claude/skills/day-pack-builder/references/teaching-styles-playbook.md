# The teaching styles playbook

The full cards behind `teaching-styles.md`, researched on 12 October 2026 for Week 4 and kept for every
week after it (decision `teaching-approach`). Each card gives the style's moves in order, its signature
device, what a learner gains, where it fails when overused, and one move each for a deck chapter, a
notebook, an explorer scene, study notes and an interview transcript; section 5 shows the blend worked
through on Week 4's five cases. Every link carries the date it was checked.

Prepared 12 October 2026 for the Week 4 day and explorer sessions (INTERNAL). Every URL was fetched today and carries "(checked 12 October 2026)"; no YouTube watch page is used as evidence, and two video titles were confirmed through YouTube's oEmbed endpoint. Styles are described in my own words, with at most one quoted sentence per source. R1 (docs/detailing/W04_research_teaching.md) covers mysqltutorial.org, the IBM explainers, Storytelling with Data and FPP3. Section 7 lists what could not be verified.

Builders: find your artefact in section 4, follow your day in section 5, and read the section 3 cards of the styles that lead it.

## 1. The playbook in ten lines

1. Open every chapter on a question the learner answers before any teaching: a vote, a guess, a drag (Brilliant, Peer Instruction).
2. Count by hand on the case's twelve rows before any code or formula (StatQuest, Khan Academy).
3. Voice the tempting wrong answer, let the room commit, then break it with data (Veritasium; this is the house trap done properly).
4. Draw the picture before the formula; the formula arrives as a caption for the picture (3Blue1Brown).
5. Open and close each day on one numbered map of the system, today's node lit (ByteByteGo).
6. Build the number from scratch in ten lines, show the library agrees, then beat a dumb baseline (Karpathy).
7. In the explorer the learner holds the parameter: predict, move, watch, sweep, then step back down to one case (Bret Victor, Nicky Case).
8. Code along only on the three to six lines that carry the technique; the rest ships pre-filled and executed (Krish Naik, Kaggle Learn).
9. Climb from a hand count to interview grade, brute force first, with the current rung shown (takeUforward, DataLemur).
10. Close with a plain-words explanation and a transcript that sets a weak answer beside a hire-grade one (Feynman, Aced, Alex Xu).

## 2. The learner, and five findings that set the blend

The room is 0 to 3 years into work in India, often uneasy with algebra, rarely with a business role behind it, and aiming at analyst, data scientist and forward-deployed engineer jobs.

| Finding | Source | What it changes |
|---|---|---|
| Novices learn more from studying worked examples than from solving the same problems | Sweller and Cooper, 1985 https://api.crossref.org/works/10.1207/s1532690xci0201_3 (checked 12 October 2026) | L1 and L2 are fully worked |
| The advantage reverses as expertise grows | Kalyuga, Ayres, Chandler and Sweller, 2003 https://api.crossref.org/works/10.1207/S15326985EP3801_4 (checked 12 October 2026) | Steps fade from L3; L5 and L6 carry no scaffold |
| Refuting misconceptions beats clear exposition, most for weak learners | Muller and colleagues, 2008 (card 3.2) | Every trap is voiced, then refuted |
| Taking tests improves long-term retention | Roediger and Karpicke, 2006 https://api.crossref.org/works/10.1111/j.1467-9280.2006.01693.x (checked 12 October 2026) | Kahoot, notebook checks and the Saturday paper teach |
| Vote, peer argument and revote raise conceptual gains | Crouch and Mazur, 2001 (card 3.19) | One ConcepTest per deck chapter |

Indian context means companies the learners order from, cities they know and money in Rs. Written artefacts stay in English because the cohort spans many first languages.

## 3. The styles

Each card gives who and what, the moves in order, the signature device, the gain and the failure when overused, then one move per artefact.

### 3.1 3Blue1Brown (Grant Sanderson)

Grant Sanderson explains mathematics visually, animated in Manim, the Python library he wrote for his videos.

| | |
|---|---|
| Moves | 1. A puzzle with a tempting intuition (is quiet, orderly Steve a librarian or a farmer?). 2. A concrete sample replaces the abstraction (200 farmers, 10 librarians). 3. The picture moves as one quantity changes. 4. The formula last, labelling the picture. |
| Signature device | Continuous transformation over a ghost of the old state; probability as area that evidence trims. |
| Gain, and the failure | A picture weak-maths learners can redraw. Overused, watching passes for understanding. |
| Deck chapter | One diagram built over four to six slides; the formula last, colour-matched to its regions. |
| Notebook | Counts on 1,000 carts before probabilities; three frames of one diagram at three parameter values. |
| HTML scene | A slider morphs the picture over a faint "before"; the formula unlocks after the first move. |
| Study notes | A "picture you can redraw" box with numbered drawing steps. |
| Interview transcript | The strong answer sketches the square to show why lift is symmetric. |

Sources: "Never start with definitions." https://www.3blue1brown.com/about (checked 12 October 2026); https://www.3blue1brown.com/lessons/bayes-theorem (checked 12 October 2026); https://www.3blue1brown.com/lessons/linear-transformations (checked 12 October 2026).

### 3.2 Veritasium (Derek Muller)

Derek Muller's science channel of experiments and street interviews; his University of Sydney PhD (2008) tested which physics videos teach.

| | |
|---|---|
| Moves | 1. A question with a tempting wrong answer, often put to passers-by. 2. The wrong answer said confidently. 3. The demonstration that breaks it. 4. The right model set against the wrong one. 5. Back to the question. |
| Signature device | The refutation: a believable voice states the misconception, then it is dismantled. |
| Gain, and the failure | With 364 first-year physics students, refutation and dialogue versions beat a concise lecture, and low prior knowledge students gained most. Overused, every chapter feels like a trick. |
| Deck chapter | The trap slot: predict, "what most people say", the reveal, wrong model against right. |
| Notebook | The tempting number in a titled cell, a CHECK that breaks it, then the fix. |
| HTML scene | A guess marker first; the reveal shows guess, truth and the common guess. |
| Study notes | A "tempting answer" box with its counter-example in numbers. |
| Interview transcript | A dialogue: the weak candidate voices the misconception, the strong one refutes it. |

Sources: "Results show the Refutation and Dialogue produced the greatest learning gains, with effect sizes of 0.79 and 0.83, respectively, compared with the Exposition." (Muller, Bewes, Sharma and Reimann, 2008; Wiley refused automated access, so the abstract was read on Crossref https://api.crossref.org/works/10.1111/j.1365-2729.2007.00248.x (checked 12 October 2026)); the dialogue study https://api.crossref.org/works/10.1002/sce.20244 (checked 12 October 2026); https://en.wikipedia.org/wiki/Derek_Muller (checked 12 October 2026); https://www.veritasium.com/ (checked 12 October 2026); "Khan Academy and the Effectiveness of Science Videos" https://www.youtube.com/watch?v=eVtCO84MDj8 (checked 12 October 2026, title via oEmbed).

### 3.3 Krish Naik

A Bengaluru data science educator with English and Hindi channels, step-by-step tutorials on real problems, end-to-end projects and live cohorts.

| | |
|---|---|
| Moves | 1. The problem and the dataset. 2. Code typed live, each line explained. 3. Errors fixed on screen. 4. An end-to-end project, published as a repository. |
| Signature device | The code-along: the learner's screen mirrors the trainer's. |
| Gain, and the failure | "I made it run" confidence in a format the cohort knows. Overused, typing passes for understanding and live errors eat the clock. |
| Deck chapter | The trainer types only the lines that carry the technique. |
| Notebook | Three to six type-along cells with saved output to compare; the rest pre-filled and executed. |
| HTML scene | A "show the code" toggle with the pandas equivalent. |
| Study notes | "The code in five lines", glossed line by line. |
| Interview transcript | The live SQL round: talk while writing, test on a tiny table. |

Sources: https://www.krishnaik.in/ (checked 12 October 2026); https://github.com/krishnaik06/The-Grand-Complete-Data-Science-Materials (checked 12 October 2026); https://analyticsindiamag.com/ai-features/top-10-programmers-to-follow-on-youtube (checked 12 October 2026).

### 3.4 ByteByteGo (Alex Xu)

Alex Xu's system-design guides and interview books, made to "Explain complex systems using visuals and simple terms."

| | |
|---|---|
| Moves | 1. One question. 2. One diagram of the whole flow, steps numbered. 3. Prose walking the numbers. In interviews: scope and assumptions, a high-level design with rough numbers, a deep dive, a wrap-up. |
| Signature device | The numbered flow: one canvas, numbers on the arrows, text keyed to them. |
| Gain, and the failure | Every part placed on one map, the cure for "not connected". Overused, boxes carry no quantities. |
| Deck chapter | A map slide opens and closes each chapter, today's step lit. |
| Notebook | A numbered mermaid flow first; each section header names its step. |
| HTML scene | The home screen: the week's map lighting day by day. |
| Study notes | One flow page with a "where it breaks" mark on each step. |
| Interview transcript | The four steps retimed for an analytics case. |

Sources: https://github.com/ByteByteGoHq/system-design-101 (checked 12 October 2026); https://bytebytego.com/guides/how-does-chatgpt-work/ (checked 12 October 2026); "Never say your design is perfect and nothing can be improved." https://bytebytego.com/courses/system-design-interview/a-framework-for-system-design-interviews (checked 12 October 2026).

### 3.5 StatQuest (Josh Starmer)

Josh Starmer's statistics and ML videos, pictures drawn by hand, begun as tutorials for colleagues whose data he analysed.

| | |
|---|---|
| Moves | 1. A tiny dataset in view. 2. The calculation by hand, a picture per step. 3. The name after it. 4. One complication at a time. 5. "BAM!" and a pointer to the prerequisite. |
| Signature device | Tiny numbers: a handful of points, dots beside the table, every step shown. |
| Gain, and the failure | Formula-shy learners check every number. Overused, toys feel unreal and hide rare events. |
| Deck chapter | The twelve-row case table, one arithmetic step per build; the term after the count. |
| Notebook | Plain Python reproduces the hand count; pandas agrees on twelve rows, then runs on all. |
| HTML scene | Every dot is a row; click to read it. |
| Study notes | A "worked by hand" box, one step per line. |
| Interview transcript | The strong candidate tests reasoning on a tiny example aloud. |

Sources: "Because I didn't want my analysis to be like 'magic', I created little tutorials on basic statistics for them." https://towardsdatascience.com/interviewing-statquests-founder-and-ceo-josh-starmer-6f96fe71ec25 (checked 12 October 2026); https://statquest.org/ (checked 12 October 2026); "Conditional Probabilities, Clearly Explained!!!" https://www.youtube.com/watch?v=_IgyaD7vOOA (checked 12 October 2026, title via oEmbed).

### 3.6 takeUforward (Striver) and the A2Z sheet

An Indian interview-preparation platform whose A2Z DSA sheet, under Striver's name, orders about 450 items in about twenty sections, basics to advanced.

| | |
|---|---|
| Moves | 1. One section at a time, in a fixed order. 2. Easy pattern problems, then variants, then interview grade. 3. Per problem: brute force, better, optimal, proof, complexity. 4. The solution only after a real attempt. |
| Signature device | The ladder sheet: difficulty-ordered problems, each climbed from brute force to optimal. |
| Gain, and the failure | A visible route to interview grade. Overused, ticking boxes becomes the goal. |
| Deck chapter | The chapter closes on the L1 to L6 ladder, current rung lit. |
| Notebook | The exercise twin as a ladder, each item solved by hand, then groupby, then window function. |
| HTML scene | A ladder sidebar; scenes unlock after each prediction. |
| Study notes | Ten to fifteen items, easy to interview grade, tagged by pattern. |
| Interview transcript | Brute force, then better, said aloud. |

Sources: "The goal is not to memorize solutions." https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2 (checked 12 October 2026); https://takeuforward.org/ (checked 12 October 2026).

### 3.7 Brilliant

An interactive course app whose about page says "We don't teach how to do something before asking questions."

| | |
|---|---|
| Moves | 1. A problem tried on intuition (a pretest). 2. Feedback on the answer given. 3. A short explanation naming what was done. 4. A harder variant. 5. Practice without hints. |
| Signature device | Problem first, feedback written for each wrong answer. |
| Gain, and the failure | Active from the first minute. Overused, fragments with no big picture. |
| Deck chapter | One question slide before any definition; the next answers each option. |
| Notebook | A "try first" cell whose check answers each common mistake. |
| HTML scene | The explanation unlocks after an attempt, starting from the option chosen. |
| Study notes | "Try this before reading on", answer at the foot. |
| Interview transcript | "Pause and write your answer" before the model answer. |

Sources: https://brilliant.org/about/ (checked 12 October 2026).

### 3.8 Explorable explanations (Bret Victor, Nicky Case)

Bret Victor's 2011 essay asked for reactive documents; Nicky Case's playables (Parable of the Polygons with Vi Hart, The Evolution of Trust) built them.

| | |
|---|---|
| Moves | Case: 1. A question posed as a story or game. 2. Start on the ground (drag an unhappy shape). 3. Climb by BUT and THEREFORE. 4. Reveals follow the reader's actions (a mild one-third preference segregates the town). 5. A sandbox. Victor: one instance, then over time, then a parameter sweep, stepping back down. |
| Signature device | The reader holds a model's parameter and finds the counter-intuitive result. |
| Gain, and the failure | Discovery the learner owns. Overused, fiddling without a question. |
| Deck chapter | Three screenshots told as a BUT and THEREFORE story, then the live explorer. |
| Notebook | The notebook's slider: ten settings as one curve, two printed row by row. |
| HTML scene | Question, action, reveal, sandbox; one slider, a reset, clickable marks; drawn static first, then inputs that move outputs (Red Blob Games). |
| Study notes | The day's chain in prose, with the slider setting to try. |
| Interview transcript | What-if reasoning aloud about a changed threshold. |

Sources: https://worrydream.com/ExplorableExplanations/ (checked 12 October 2026); https://worrydream.com/LadderOfAbstraction/ (checked 12 October 2026); "But the goal shouldn't be to dumb the ideas down, it should be to smart the people up." https://blog.ncase.me/how-i-make-an-explorable-explanation/ (checked 12 October 2026); https://ncase.me/polygons/ (checked 12 October 2026); https://www.redblobgames.com/making-of/line-drawing/ (checked 12 October 2026); Bartosz Ciechanowski's Moon essay, which starts on two made-up bodies https://ciechanow.ski/ (checked 12 October 2026).

### 3.9 distill.pub

A machine learning journal, on hiatus since July 2021, built on interactive, carefully drawn explanation.

| | |
|---|---|
| Moves | 1. A hero figure previewing the idea. 2. Prose and figures interleaved, labels on the marks. 3. Figures the reader varies. 4. An equation beside its geometry. 5. Depth in footnotes. |
| Signature device | The annotated figure that carries the argument; notation as the idea's interface. |
| Gain, and the failure | Precision with intuition. Overused, dense and costly; interactivity can distract. |
| Deck chapter | Direct labels, no legends; one notation box all week. |
| Notebook | Annotate the point that matters; colour the formula to match the plot. |
| HTML scene | Hover a formula term to light its region. |
| Study notes | A notation card for the week. |
| Interview transcript | Terms defined before use. |

Sources: "Research distillation is the opposite of research debt." https://distill.pub/2017/research-debt/ (checked 12 October 2026); https://distill.pub/2020/communicating-with-interactive-articles/ (checked 12 October 2026); https://distill.pub/2021/distill-hiatus/ (checked 12 October 2026).

### 3.10 The Pudding

A visual-essay publication: "The Pudding explains ideas debated in culture with visual essays."

| | |
|---|---|
| Moves | 1. Open near the reader (their own city). 2. Study the data, then choose the story's shape. 3. Narrow step by step (about 7,000 bands at small venues down to 11 at the largest). 4. Sparse text, each step landing a hard conclusion. |
| Signature device | The scroll-driven reveal with a shape (a V, an inverted V) taken from the data. |
| Gain, and the failure | A conclusion earned step by step. Overused, style over substance. |
| Deck chapter | One chart revealed in steps, a sentence per slide. |
| Notebook | The chart re-plotted with one more filter per cell. |
| HTML scene | Steps beside a sticky chart; a trainer-paced Next control suits the projector, though The Pudding warns phone readers off steppers. |
| Study notes | The story as a strip of captioned charts. |
| Interview transcript | User, then segment, then conclusion. |

Sources: https://pudding.cool/about/ (checked 12 October 2026); "Visual stories really need clear, hard, underlying conclusions in order to be interesting to people." https://www.storybench.org/pudding-structures-stories-visual-essays/ (checked 12 October 2026); https://pudding.cool/process/responsive-scrollytelling/ (checked 12 October 2026).

### 3.11 Khan Academy: mastery and worked examples

Sal Khan's platform, begun in 2004 tutoring a cousin: digital-blackboard videos that work a problem by hand, then practice at the learner's own pace.

| | |
|---|---|
| Moves | 1. One worked example, narrated. 2. Same-type practice at once. 3. Move on after mastery; a gap sends the learner back. 4. Mixed review later. |
| Signature device | The narrated worked example, then an item that differs in one way. |
| Gain, and the failure | No silent gaps. Overused, procedure without meaning, and full steps hinder stronger learners. |
| Deck chapter | Worked, then one change, then faded with two steps blank. |
| Notebook | Worked cell, faded cell, full problem, a check after each. |
| HTML scene | A "next step" button writes the next line onto the diagram. |
| Study notes | One worked example per concept, practice answers overleaf. |
| Interview transcript | Each number derived on its own line, then a faded copy. |

Sources: "Would you choose to build a house on top of an unfinished foundation?" https://www.ted.com/talks/sal_khan_let_s_teach_for_mastery_not_test_scores (checked 12 October 2026); https://en.wikipedia.org/wiki/Khan_Academy (checked 12 October 2026).

### 3.12 CS50 (David Malan)

Harvard's introduction to computer science, free as CS50x; Week 0 teaches algorithms by searching a phone book.

| | |
|---|---|
| Moves | 1. An everyday object and a task. 2. Naive (a page at a time), faster (two at a time), clever (halve and repeat). 3. All three on one cost chart (n, n/2, log n). 4. Pseudocode, then code. |
| Signature device | The everyday-object demonstration ending on a chart of the methods' costs. |
| Gain, and the failure | The idea before the syntax, methods sized. Overused, theatre for trivial points. |
| Deck chapter | A props beat with receipts or chits, then the costs slide. |
| Notebook | Three methods timed on growing data and plotted together. |
| HTML scene | A race with step counters. |
| Study notes | A "three ways, sized" table at 1,000 and 100,000 rows. |
| Interview transcript | The naive way offered, priced, then improved. |

Sources: https://cs50.harvard.edu/x/ (checked 12 October 2026); "Then, repeat this process, cutting the problem in half and half and half." https://cs50.harvard.edu/x/notes/0/ (checked 12 October 2026).

### 3.13 Andrej Karpathy, with fast.ai as the counterweight

Karpathy's Zero to Hero course builds from backpropagation to GPT in code, starting with micrograd (about 100 lines); his training recipe opens with "become one with the data".

| | |
|---|---|
| Moves | 1. Raw rows first. 2. The simplest version from scratch on a tiny example. 3. Checked against the library. 4. One piece at a time, each effect predicted. 5. A dumb baseline beaten first. |
| Signature device | The from-scratch twin that reproduces the library's number. |
| Gain, and the failure | No black boxes, and the baseline reflex. Overused, tools get reinvented; fast.ai's "whole game" (a working pipeline first, then its layers) balances it. |
| Deck chapter | Plain-Python lines beside the one-line pandas call, one number under both. |
| Notebook | The whole game in cell one; from scratch on twelve rows; the library on all, asserted equal; the baseline first. |
| HTML scene | A panel showing the scene's own short function. |
| Study notes | The from-scratch function, glossed. |
| Interview transcript | "Compute retention without a library; which baseline would you beat?" |

Sources: "We start with the basics of backpropagation and build up to modern deep neural networks, like GPT." https://karpathy.ai/zero-to-hero.html (checked 12 October 2026); https://github.com/karpathy/micrograd (checked 12 October 2026); https://karpathy.github.io/2019/04/25/recipe/ (checked 12 October 2026); https://www.fast.ai/posts/2016-10-08-teaching-philosophy.html (checked 12 October 2026).

### 3.14 The Feynman technique

A self-test under Feynman's name: explain an idea plainly to find where understanding breaks; the earliest version found is Scott Young's 2011 handout.

| | |
|---|---|
| Moves | 1. The concept's name atop a blank page. 2. Explain it to a new student. 3. Where you stall, back to the source. 4. Simplify, find an analogy, teach someone. |
| Signature device | The plain explanation as a probe: "You haven't grasped it fully if you can't explain it simply." |
| Gain, and the failure | Self-diagnosis and interview fluency. Overused, the simple version drops the condition that matters. |
| Deck chapter | A two-sentence turn-and-talk that must use the slide's words. |
| Notebook | An "in plain words" cell paired with a pick-the-best-explanation item. |
| HTML scene | Three explanations to choose from, one oversimplified. |
| Study notes | The plain version, an analogy, and where the analogy breaks. |
| Interview transcript | "Explain lift to a category manager who hates maths." |

Sources: https://fs.blog/feynman-technique/ (checked 12 October 2026); https://www.scotthyoung.com/learnonsteroids/grab/TranscriptFeynman.pdf (checked 12 October 2026).

### 3.15 Seeing Theory, with Setosa

Seeing Theory, built by Daniel Kunin as a Brown undergraduate and now archived, teaches probability through D3 visualisations; Setosa's Explained Visually series does likewise.

| | |
|---|---|
| Moves | 1. A definition beside a live visual. 2. The reader runs the experiment and frequencies settle. 3. Conditioning as a click to a smaller universe. 4. The formula. |
| Signature device | "Mathematically, computing a conditional probability amounts to shrinking our sample space to a particular event." |
| Gain, and the failure | Probability as frequency, kind to weak maths. Overused, random results confuse the room. |
| Deck chapter | "Run it 1,000 times", the spread read in one sentence. |
| Notebook | Seeded independent carts showing how widely lift spreads at tiny support. |
| HTML scene | Universe tabs and a "simulate 1,000 carts" button. |
| Study notes | A "what chance alone does" histogram. |
| Interview transcript | "How far would chance alone move this lift?" |

Sources: https://seeing-theory.brown.edu/ (checked 12 October 2026); https://seeing-theory.brown.edu/compound-probability/index.html (checked 12 October 2026); Setosa's balls on two shelves https://setosa.io/conditional/ (checked 12 October 2026); the series https://setosa.io/ev/ (checked 12 October 2026).

### 3.16 Kaggle Learn

Kaggle's free short courses: each tutorial notebook pairs with an exercise notebook checked by the open-source learntools package.

| | |
|---|---|
| Moves | 1. A short tutorial on real data. 2. The exercise at once, check() called. 3. Numbered hints, then a logged solution. 4. The next lesson builds on it. |
| Signature device | check(), hint(n) and solution() inside the notebook. |
| Gain, and the failure | Instant feedback in the work tool. Overused, checks test values and never judgement. |
| Deck chapter | A slide naming the exercise item and its check. |
| Notebook | The TODO twin with small check, hint and solution functions; design items answered as letters. |
| HTML scene | A "check my guess" control. |
| Study notes | The exercise path. |
| Interview transcript | A checked drill bank of short SQL tasks. |

Sources: https://github.com/Kaggle/learntools (checked 12 October 2026); https://raw.githubusercontent.com/Kaggle/learntools/master/learntools/core/problem_view.py (checked 12 October 2026); tutorial and exercise pairs https://github.com/Kaggle/learntools/tree/master/notebooks/python/raw (checked 12 October 2026).

### 3.17 Indian YouTube educators of data and DSA

codebasics (Dhaval Patel, with a Hindi sister channel), CampusX (Nitish Singh), CodeWithHarry (Hindi, from the basics), Namaste SQL (Ankit Bansal, over a decade at Amazon) and Apna College, beside 3.3 and 3.6.

| | |
|---|---|
| Moves | 1. A known setting: codebasics casts learners as analysts ("Help AtliQ Media to Decode the 2026 Tamil Nadu Election"). 2. A numbered path (CampusX's day folders). 3. Hard questions split and solved more than one way (Namaste SQL). 4. The placement frame. |
| Signature device | A relatable Indian scenario in an interview frame, solved two ways. |
| Gain, and the failure | Belonging and job relevance. Overused, placement hype, shortcuts and language that excludes. |
| Deck chapter | Uber Hyderabad or Instamart Pune in Rs; R2's company-tagged questions. |
| Notebook | Indian-looking data (cities, Rs, UPI, festival dates); key queries written two ways. |
| HTML scene | Indian places and prices. |
| Study notes | A "two ways to write it" box. |
| Interview transcript | Set at a GCC, Swiggy or Flipkart screen, question types from R2. |

Sources: https://analyticsindiamag.com/ai-features/top-10-programmers-to-follow-on-youtube (checked 12 October 2026); https://codebasics.io/event/codebasics-resume-project-challenge (checked 12 October 2026); https://github.com/campusx-official/100-days-of-machine-learning (checked 12 October 2026); https://www.namastesql.com/ (checked 12 October 2026); https://www.apnacollege.in/ (checked 12 October 2026).

### 3.18 Hans Rosling and Gapminder (added)

Rosling's 2006 TED talk used world data with a sportscaster's urgency to overturn myths about the "developing world"; Gapminder quizzes the public and offers animated-data tools.

| | |
|---|---|
| Moves | 1. A three-option fact question first. 2. Answers set against the truth. 3. The data animated with commentary. 4. The misleading instinct named (gap, straight line, size). |
| Signature device | The misconception quiz, then the narrated moving chart. |
| Gain, and the failure | Every number arrives with a comparison. Overused, performance replaces analysis. |
| Deck chapter | Headline numbers always shown with comparison and denominator. |
| Notebook | Each headline number printed beside its comparison. |
| HTML scene | A time slider the trainer narrates over. |
| Study notes | "Per what, against what" under each number. |
| Interview transcript | The strong answer compares before concluding. |

Sources: "You've never seen data presented like this." https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen (checked 12 October 2026); https://www.gapminder.org/ (checked 12 October 2026); https://www.gapminder.org/factfulness/ (checked 12 October 2026).

### 3.19 Peer Instruction (Eric Mazur) (added)

Eric Mazur's method from early-1990s Harvard physics, built on conceptual questions called ConcepTests.

| | |
|---|---|
| Moves | 1. A ConcepTest from known difficulties. 2. Answer alone. 3. Argue with neighbours. 4. Answer again. 5. "The instructor again reviews responses and decides whether more explanation is needed before moving on to the next concept." |
| Signature device | Vote, argue, revote. |
| Gain, and the failure | A decade of classes showed gains in conceptual reasoning and quantitative problem solving; it fits nine groups. Overused on recall, it wastes the block. |
| Deck chapter | One ConcepTest per chapter, distractors from the day's misconceptions. |
| Notebook | A "commit first" cell stores the learner's letter for comparison. |
| HTML scene | The vote comes before the scene plays. |
| Study notes | Each option's reasoning, right or wrong. |
| Interview transcript | Pairs swap roles and score with the transcript's notes. |

Sources: https://en.wikipedia.org/wiki/Peer_instruction (checked 12 October 2026); Crouch and Mazur, 2001 https://api.crossref.org/works/10.1119/1.1374249 (checked 12 October 2026).

### 3.20 Interview rehearsal through annotated expert answers (added)

Aced (formerly Exponent) shows expert video answers; DataLemur tags questions by company and as Easy, Medium or Hard; CaseInterview.com (Victor Cheng) teaches structured cases.

| | |
|---|---|
| Moves | 1. The question as asked. 2. Clarify and state assumptions. 3. A structure aloud before any number. 4. Rounded, checked numbers. 5. A recommendation with risks. 6. The interviewer's notes. |
| Signature device | The annotated transcript, a weak answer beside a hire-grade one. |
| Gain, and the failure | Learners hear what good sounds like. Overused, scripts get recited. |
| Deck chapter | The L6 slide: the question, three listening points, the common wrong answer. |
| Notebook | The interview's SQL round last, with its added edge case. |
| HTML scene | Not used. |
| Study notes | Tagged questions, answers overleaf. |
| Interview transcript | Two voices, notes keyed to Alex Xu's four steps, the AI variant last. |

Sources: "Discover the interview questions companies actually ask and watch how experts answer them in over 100+ live video answers." https://www.aced.io/ (checked 12 October 2026); https://datalemur.com/ (checked 12 October 2026); https://www.caseinterview.com/ (checked 12 October 2026).

## 4. Which styles lead in each artefact

| Artefact | Lead styles | Never |
|---|---|---|
| Deck chapter | Brilliant or Peer Instruction to open; StatQuest's hand count; 3Blue1Brown's picture; Veritasium at the trap; Rosling on headline numbers; ByteByteGo's map first and last | Code before the question; a formula before its picture |
| Notebook | fast.ai's whole game first; Karpathy's raw rows, from-scratch twin and baseline; StatQuest's twelve rows; Krish Naik's type-along lines; Kaggle's checks; CS50's methods timed | A cell that teaches only syntax |
| HTML scene | Explorables (the viewer holds the parameter, sandbox last); 3Blue1Brown (continuous change); Veritasium and Brilliant (predict, then reveal); distill (details on demand); Seeing Theory (simulate) | A control that changes nothing visible; any Kalpa plant |
| Study notes | Khan Academy (worked, then faded); StatQuest (by hand); Feynman (plain words, where the analogy breaks); ByteByteGo (flow page); takeUforward (practice ladder) | A definition as the first line |
| Interview transcript | Annotated rehearsal; Alex Xu's four steps; Veritasium's dialogue; Karpathy's "without a library"; takeUforward and DataLemur's difficulty ladder | A framework recited by name |

## 5. Blend recipes for Week 4

Beats follow the revision brief's ladder (L1 to L6), lead style first and support in brackets. Numbers are the brief's targets, which the case file and each day's generator fix; the explorer and learner files carry only case and toy numbers, never a Kalpa plant.

### 5.1 Monday: metric design and gaming (Uber, Hyderabad, a peak-hour earnings guarantee)

| Beat | Lead (support) | The move |
|---|---|---|
| Ticket | Brilliant (Peer Instruction) | Peak online hours up 24 percent, completed peak trips up 3 percent, trips per peak online hour 1.9 to 1.6; vote on "is it working?", argue, revote. |
| L1 | StatQuest (ByteByteGo) | Trips per online hour by hand on twelve driver-weeks; then a numbered flow from scheme rule to driver choice (drive, idle, decline, two apps) to logs, payout and rider wait. |
| Scene | Explorables (3Blue1Brown) | Drivers as dots drift from driving to idle online as the threshold slider rises; predict the ratio, sweep it into a curve, click a point for its dots. |
| L2 | Krish Naik (Karpathy) | Type the five lines (group, sum, divide, sort, flag); a plain loop on twelve rows matches pandas. |
| L3 | Veritasium (Rosling) | The confident "supply rose 24 percent" slide, broken by the per-hour and completed-trip view. |
| L4 | distill (Feynman) | The definition line by line (unit, numerator, denominator, window, exclusions), each with its gaming route and guardrail. |
| L5 | Rosling | Pay per completed peak trip with an acceptance guardrail, costed in Rs; driver operations objects; the test passes to the IITGN experiments block (tentative). |
| L6 | Interview rehearsal (takeUforward) | "How would you know a driver incentive works?"; AI variant: a coding assistant whose accepted suggestions are later deleted. |

### 5.2 Tuesday: stakeholder communication and the first guesstimate

| Beat | Lead (support) | The move |
|---|---|---|
| Ticket | Rosling (Peer Instruction) | A nine-number status slide against one claim with its comparison; vote on which the Hyderabad city head acts on. |
| Say it | Feynman (Pudding) | Three minutes aloud, then one sentence; the slide runs from the head's own falling number (gross bookings per online hour) to the cause to the ask. |
| Structure | ByteByteGo | Claim, one piece of evidence with its denominator, a caveat, the ask with its cost, numbered. |
| Objections | Veritasium dialogue | Role cards for driver operations, marketing and finance; each objection in its owner's words, then the reply. |
| Guesstimate | StatQuest (CS50, ByteByteGo) | Drivers online in Hyderabad at the weekday evening peak, by a demand route and a supply route; clarify, structure, round, sanity-check against R2's anchor. |
| Scene | Brilliant (Seeing Theory) | A slider per assumption, the answer as a range, a bar for each input's pull; predict the biggest first. |
| L3 | Veritasium | False precision and a per-day against per-hour slip, shown, then fixed. |
| Written case | Khan Academy | A fully worked one-page case, a faded template, then the AI-free case. |
| L6 | Interview rehearsal | The guesstimate transcript; AI variant (proposed here): the GPUs an AI startup needs at its evening peak. |

### 5.3 Wednesday: market basket on a quick-commerce cart (Swiggy Instamart, Pune)

| Beat | Lead (support) | The move |
|---|---|---|
| Ticket | Brilliant (Peer Instruction) | Toned milk sits beside nearly everything in "frequently bought together" and click-through fell; vote on what belongs beside chips. |
| L1 | StatQuest | Twelve receipts: carts with A, with B, with both; support, confidence, the count expected if unrelated. |
| Picture | 3Blue1Brown (Seeing Theory) | Confidence as the universe shrinking to carts with A; P(A) times P(B) as an area beside the observed overlap, so lift is a ratio of areas and symmetric. |
| Scene | Explorables | A slider raises milk's share of carts; confidence toward milk climbs while lift stays near 1; predict lift at 90 percent first. |
| L2 | Karpathy (CS50) | Pair counts with a dictionary on twelve carts, then the SQL self-join, same numbers; three methods timed. |
| L3 | Veritasium | "High confidence means a strong pair", refuted by the popular partner. |
| L4 | Seeing Theory | Simulated independent carts show lift wandering at tiny support (the support floor); the strip itself manufactures co-occurrence. |
| L5 | ByteByteGo (Rosling) | Impression, click, add, incremental margin: one strip slot's worth in Rs against a holdout. |
| L6 | Interview rehearsal (DataLemur) | Rank "frequently bought together"; the pair-count SQL; AI variant: an LLM assistant's add-ons judged by incremental add-ons against a control. |

### 5.4 Thursday: cohorts, retention and funnels (a food-delivery membership, Chennai)

| Beat | Lead (support) | The move |
|---|---|---|
| Ticket | Veritasium (Peer Instruction) | Reported month-two retention has held flat for months; vote on whether membership is healthy. |
| L1 | StatQuest (Khan Academy) | Twelve members in three signup cohorts; retention per cohort and blended, by hand; the triangle worked once in full. |
| Scene | 3Blue1Brown (Explorables) | The cohort triangle fills while the blended line stays flat; a slider sizes the festive-sale cohort; click a row for its falling curve. |
| L2 | Krish Naik (Indian educators) | The cohort table in pandas and in SQL, two ways, a check after each. |
| L3 | Veritasium (Rosling) | Blended flat while every cohort declines, Week 1's reversal returning; compare same-age cohorts. |
| Funnel | ByteByteGo (Brilliant) | Denominators written on every arrow; "which stage leaks?" asked first; the stage whose drop is a change of unit. |
| L4 | distill (Feynman) | Censored young cohorts, signup seasonality, what "retained" means, the release date as a before and after. |
| L5 | Rosling | The stage to fix after the checkout release, priced in orders and Rs, against the app team's objection. |
| L6 | Interview rehearsal | "Retention dropped, walk me through it", hypotheses with tests before data; AI variant: novelty against habit in an AI app's cohorts. |

### 5.5 Friday: forecasting with seasonal baselines and a Diwali date shift (Flipkart or Amazon India, a Lucknow fulfilment centre)

| Beat | Lead (support) | The move |
|---|---|---|
| Ticket | fast.ai (Veritasium) | Three lines give the seasonal naive and its hold-out error beside the vendor's +22 percent and finance's +4; vote on whether the best fit forecasts best. |
| L1 | StatQuest (Karpathy) | Eight weeks by hand (naive, seasonal naive, mean absolute error); then all 104 weeks plotted, Diwali marked, before any model. |
| Scene | 3Blue1Brown (Explorables) | Trend, season and noise sliders build the series; the festival marker slides into November; the calendar-week baseline keeps the old peak while the festival-aligned one follows. |
| L2 | Krish Naik | Shift by 52 weeks, align by weeks to Diwali, hold-out MAE in shipments. |
| L3 | Veritasium | Copying last year's week after the festival moved, and a near-perfect fit that extrapolates last Diwali's spike. |
| L4 | Brilliant (distill) | A cost slider for an idle packer against a missed shipment; predict the best staffing level; error in shipments and in Rs. |
| L5 | Rosling (Pudding) | The good-enough call to finance: forecast, range, the cost of each error; +22 against +4 settled on held-out weeks. |
| L6 | Interview rehearsal (CS50) | "Forecast festive staffing": three methods sized, then the call; AI variant: inference demand when launches move like festivals. |

## 6. Where blends go wrong

| Overused | What the room shows | Repair |
|---|---|---|
| 3Blue1Brown with no learner action | Nods in class, wrong Kahoot answers | A prediction before every animation |
| Veritasium in every chapter | "Is this another trick?" | One refutation per chapter, at the trap |
| Krish Naik before the question | The code becomes the lesson | Question and hand count first |
| StatQuest never scaled | "Real data is different" | The same code on twelve rows and the full table |
| ByteByteGo without numbers | A map nobody can use | A count or rate on each arrow |
| takeUforward's ladder alone | Ticked boxes, no judgement | A third of items are design items (house rule) |
| Explorables without a task | Slider fiddling | Each scene opens on a question and closes on a sentence to complete |
| Rosling or Pudding as performance | A story the data cannot carry | Each step lands a conclusion the notebook proves |

## 7. What could not be verified today

- Muller's thesis PDF (old University of Sydney address) returns 404 and its catalogue records returned 503; Wiley refused automated access, so the findings come from Crossref abstracts and the thesis title from Wikipedia.
- Khan Academy's own about and help pages refused automated reading, so mastery-level thresholds found by search are not verified.
- Kaggle Learn's course pages render only in a browser; course lengths are not verified.
- CampusX's own site returned nothing readable; its teaching language is not verified.
- Love Babbar's 450 sheet (450dsa.com shows only a title) and Aditya Verma's dynamic programming series (no own site found): not verified, so not used.
- takeUforward's pages name only "Striver"; the full name Raj Vikramaditya, from third-party write-ups, is not verified.
- R2D3's A Visual Introduction to Machine Learning returned server errors twice: not verified, so not used.
- The Caltech Feynman Lectures site refused automated access; whether Feynman set out these steps himself is not verified.
- Victor Cheng's Look Over My Shoulder programme: its format is not described on the page read, so not verified.
- No YouTube watch page was read; two titles were confirmed through oEmbed only.
