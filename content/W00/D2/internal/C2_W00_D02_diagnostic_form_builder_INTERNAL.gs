// =====================================================================
// Baseline Diagnostic, Cohort 2, Week 0: one-shot Google Form builder
// Run buildDiagnosticForm() once from the Apps Script editor.
// It creates the quiz, links a results spreadsheet, publishes the form,
// installs the on-submit trigger, and logs the two URLs you need.
// =====================================================================

// CONFIG
const CONFIG = {
  FORM_TITLE: 'Baseline Diagnostic | Cohort 2 | Week 0',
  ORG: 'IITGN CDF (CAA)',
  PROGRAMME: 'PG Diploma in AI-ML and Agentic AI Engineering',
  COHORT: 'Cohort 2',
  WEEK: 'Week 0',
  TIME_MINUTES: 90,
  RESPONDERS: 'anyone',            // 'anyone' (needs the Drive advanced service switched on), 'list' (RESPONDER_EMAILS), or 'none' (share by hand)
  RESPONDER_EMAILS: [],            // used only when RESPONDERS is 'list'
  REQUIRE_SIGN_IN: false,          // false: no Google sign-in, the candidate types the email the report goes to; true: Google sign-in, one response per account, verified email
  SEND_REPORT_EMAIL: true,         // email each candidate a full report on submission
  REPLY_TO: '',                    // optional reply-to address on the report email
  CODE_IMAGE_FOLDER_ID: '',        // optional: Drive folder holding Q1.png, Q2.png ... from the assets zip; blank means code goes in as text
  RESULTS_SPREADSHEET_NAME: 'C2 W00 Baseline Diagnostic responses',
  WORLD: 'Kalpa Retail',
};

// ---------------------------------------------------------------------
// Item bank (generated from the locked paper; do not edit by hand)
// ---------------------------------------------------------------------
const BANK = {
 "SECTIONS": {
  "A": {
   "title": "Python for data and GenAI",
   "minutes": 30,
   "claimed": "Python"
  },
  "B": {
   "title": "SQL for data and GenAI",
   "minutes": 20,
   "claimed": "SQL"
  },
  "C": {
   "title": "Numbers and reasoning",
   "minutes": 14,
   "claimed": "Numbers and reasoning"
  },
  "D": {
   "title": "Case and scenarios",
   "minutes": 10,
   "claimed": "Working an unfamiliar business problem"
  },
  "E": {
   "title": "Judgment calls",
   "minutes": 5,
   "claimed": null
  }
 },
 "CLAIMED_AREAS": [
  [
   "Python",
   "A"
  ],
  [
   "SQL",
   "B"
  ],
  [
   "Numbers and reasoning (percentages, averages, chance)",
   "C"
  ],
  [
   "Working an unfamiliar business problem",
   "D"
  ],
  [
   "Using LLM tools for work",
   "G"
  ]
 ],
 "CLAIMED_SCALE": [
  "1 = I have not used this",
  "2 = I can follow it when someone shows me",
  "3 = I can do it alone on a small problem",
  "4 = I can find and fix mistakes in someone else's version"
 ],
 "SELF_REPORT": [
  "When code fails, I read the full error message before changing anything.",
  "I ask for help within thirty minutes of getting stuck.",
  "I want to know why something works before I use it.",
  "I check a number a second way before I send it to anyone.",
  "I am comfortable being wrong in front of a group.",
  "I usually finish work before the deadline rather than at it.",
  "In the last month I have used an AI assistant to write or fix code.",
  "I regularly explain technical ideas to people who are not technical.",
  "I keep a written note of mistakes I have made and what I changed.",
  "I would rather be told directly when my work is weak than have it softened."
 ],
 "GENAI_IDS": [
  "Q4",
  "Q5",
  "Q11",
  "Q19",
  "Q20",
  "Q28",
  "Q33",
  "Q34"
 ],
 "ITEMS": [
  {
   "id": "Q1",
   "section": "A",
   "fmt": "Predict the output",
   "genai": false,
   "stem": [
    "What does this code print?"
   ],
   "lang": "python",
   "code": [
    "orders = [\"120\", \"80\", \"200\"]",
    "total = 0",
    "for o in orders:",
    "    total = total + o",
    "print(total)"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "400, since the strings are converted to numbers first",
     "code": false
    },
    {
     "letter": "B",
     "text": "12080200, since + joins the strings together",
     "code": false
    },
    {
     "letter": "C",
     "text": "TypeError, since int and str cannot be added",
     "code": false
    },
    {
     "letter": "D",
     "text": "0, since the loop body never runs at all",
     "code": false
    }
   ],
   "explain": "total starts as the integer 0 and each o is a string, so the first + raises TypeError. Convert with int(o) before adding.",
   "correct": "C"
  },
  {
   "id": "Q2",
   "section": "A",
   "fmt": "Spot the bug, if there is one",
   "genai": false,
   "stem": [
    "Kavya expected q1 to stay as [4, 9, 7]. The code prints 4 9. Which statement is right?"
   ],
   "lang": "python",
   "code": [
    "q1 = [4, 9, 7]",
    "q2 = q1",
    "q2.append(3)",
    "print(len(q1), sorted(q1)[-1])"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "There is a bug: q2 = q1 should have copied the list and Python failed to, so the change leaked into q1",
     "code": false
    },
    {
     "letter": "B",
     "text": "The code is right: q2 = q1 makes both names refer to one list; q2 = q1.copy() would give a separate one",
     "code": false
    },
    {
     "letter": "C",
     "text": "append() cannot affect q1 because it was called on q2, so the printed 4 must come from somewhere else in the program",
     "code": false
    },
    {
     "letter": "D",
     "text": "sorted() changed q1 in place, and that in-place sort is what added the fourth element to the list",
     "code": false
    }
   ],
   "explain": "Assignment never copies a list. q1 and q2 are two names for one object, so an append through either name shows through both. q1.copy() or list(q1) makes a separate list.",
   "correct": "B"
  },
  {
   "id": "Q3",
   "section": "A",
   "fmt": "Trace the flow (pseudocode)",
   "genai": false,
   "stem": [
    "This is pseudocode, not Python. What does it print?"
   ],
   "lang": "pseudo",
   "code": [
    "SET running_total TO 0",
    "SET best_day TO none",
    "FOR EACH (day, revenue) IN [(Mon, 40), (Tue, 25), (Wed, 55), (Thu, 55)]",
    "    running_total <- running_total + revenue",
    "    IF best_day IS none OR revenue > best_revenue THEN",
    "        best_day <- day",
    "        best_revenue <- revenue",
    "    END IF",
    "END FOR",
    "PRINT best_day, running_total"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Thu 175",
     "code": false
    },
    {
     "letter": "B",
     "text": "Wed 120",
     "code": false
    },
    {
     "letter": "C",
     "text": "Thu 55",
     "code": false
    },
    {
     "letter": "D",
     "text": "Wed 175",
     "code": false
    }
   ],
   "explain": "The comparison is strict (>), so Thursday's 55 does not replace Wednesday's 55. The running total is 40 + 25 + 55 + 55 = 175.",
   "correct": "D"
  },
  {
   "id": "Q4",
   "section": "A",
   "fmt": "Predict the output",
   "genai": true,
   "stem": [
    "An LLM has labelled six support tickets. What does the code print?"
   ],
   "lang": "python",
   "code": [
    "labels = [\"refund\", \"delivery\", \"refund\", \"refund\", \"delivery\", \"other\"]",
    "count = {}",
    "for lab in labels:",
    "    count[lab] = count.get(lab, 0) + 1",
    "print(count[\"refund\"], len(count))"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "3 3",
     "code": false
    },
    {
     "letter": "B",
     "text": "3 6",
     "code": false
    },
    {
     "letter": "C",
     "text": "6 3",
     "code": false
    },
    {
     "letter": "D",
     "text": "KeyError: 'refund'",
     "code": false
    }
   ],
   "explain": "count.get(lab, 0) returns 0 for a key it has not seen, so there is no KeyError. Three tickets are labelled refund and there are three distinct keys.",
   "correct": "A"
  },
  {
   "id": "Q5",
   "section": "A",
   "fmt": "Fix the code",
   "genai": true,
   "stem": [
    "The last line raises TypeError: list indices must be integers or slices, not str. Which replacement for the last line returns the text 'Refund approved'?"
   ],
   "lang": "python",
   "code": [
    "resp = {\"choices\": [{\"message\": {\"role\": \"assistant\", \"content\": \"Refund approved\"}}],",
    "        \"usage\": {\"prompt_tokens\": 412, \"completion_tokens\": 9}}",
    "text = resp[\"choices\"][\"message\"][\"content\"]"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "text = resp[\"choices\"][\"message\"][0][\"content\"]",
     "code": true
    },
    {
     "letter": "B",
     "text": "text = resp[\"choices\"][0][\"message\"][\"content\"]",
     "code": true
    },
    {
     "letter": "C",
     "text": "text = resp.choices.message.content",
     "code": true
    },
    {
     "letter": "D",
     "text": "text = resp[\"choices\"][\"message\"][\"content\"][0]",
     "code": true
    }
   ],
   "explain": "resp['choices'] is a list, so it needs an integer index first; the message dict sits inside its first element.",
   "correct": "B"
  },
  {
   "id": "Q6",
   "section": "A",
   "fmt": "Predict the output",
   "genai": false,
   "stem": [
    "What does this code print?"
   ],
   "lang": "python",
   "code": [
    "sales = [1200, 0, 900, None, 300]",
    "clean = [s for s in sales if s]",
    "print(sum(clean) / len(clean), len(sales) - len(clean))"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "600.0 1",
     "code": false
    },
    {
     "letter": "B",
     "text": "800 2",
     "code": false
    },
    {
     "letter": "C",
     "text": "TypeError, because None cannot be summed",
     "code": false
    },
    {
     "letter": "D",
     "text": "800.0 2",
     "code": false
    }
   ],
   "explain": "In an if test, 0 and None are both false, so the comprehension drops two values. sum(clean) / len(clean) is 2400 / 3, and / always gives a float: 800.0.",
   "correct": "D"
  },
  {
   "id": "Q7",
   "section": "A",
   "fmt": "Which line",
   "genai": false,
   "stem": [
    "Kavya's calculator gives 833.33 as the Plus average for the same rows, but the function returns 833. Which line causes the difference?"
   ],
   "lang": "python",
   "code": [
    "def average_by_tier(rows):",
    "    totals = {}",
    "    counts = {}",
    "    for tier, amount in rows:",
    "        totals[tier] = totals.get(tier, 0) + amount",
    "        counts[tier] = counts.get(tier, 0) + 1",
    "    result = {}",
    "    for tier in totals:",
    "        result[tier] = totals[tier] // counts[tier]",
    "    return result"
   ],
   "numbered": true,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Line 9: the // operator discards the fraction",
     "code": false
    },
    {
     "letter": "B",
     "text": "Line 5: totals should be written with += amount",
     "code": false
    },
    {
     "letter": "C",
     "text": "Line 6: counts should start from 1, not 0",
     "code": false
    },
    {
     "letter": "D",
     "text": "No line: the calculator is showing extra decimals",
     "code": false
    }
   ],
   "explain": "// is floor division and discards the fraction. totals[tier] / counts[tier] keeps it.",
   "correct": "A"
  },
  {
   "id": "Q8",
   "section": "A",
   "fmt": "Predict the output",
   "genai": false,
   "stem": [
    "What does this code print?"
   ],
   "lang": "python",
   "code": [
    "def tag_order(order_id, tags=[]):",
    "    tags.append(order_id)",
    "    return tags",
    "",
    "a = tag_order(\"K-101\")",
    "b = tag_order(\"K-102\")",
    "print(a, b)"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "['K-101'] ['K-102']",
     "code": false
    },
    {
     "letter": "B",
     "text": "['K-101'] ['K-101', 'K-102']",
     "code": false
    },
    {
     "letter": "C",
     "text": "['K-101', 'K-102'] ['K-101', 'K-102']",
     "code": false
    },
    {
     "letter": "D",
     "text": "The output depends on the Python version",
     "code": false
    }
   ],
   "explain": "A default argument is created once, when the function is defined. Both calls append to that same list, so a and b are the same object. Use tags=None and create the list inside the function.",
   "correct": "C"
  },
  {
   "id": "Q9",
   "section": "A",
   "fmt": "Fix the code",
   "genai": false,
   "stem": [
    "The comprehension crashes with ValueError on 'n/a'. Anand wants every bad value skipped and counted, whatever it looks like. Which rewrite does that?"
   ],
   "lang": "python",
   "code": [
    "def to_amount(text):",
    "    return float(text.replace(\",\", \"\"))",
    "",
    "rows = [\"1,200\", \"950\", \"n/a\", \"300\"]",
    "amounts = [to_amount(r) for r in rows]"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "amounts, rejected = [], []\nfor r in rows:\n    try:\n        amounts.append(to_amount(r))\n    except ValueError:\n        rejected.append(r)",
     "code": true
    },
    {
     "letter": "B",
     "text": "amounts = []\nfor r in rows:\n    if r not in (\"n/a\", \"NA\", \"\"):\n        amounts.append(to_amount(r))",
     "code": true
    },
    {
     "letter": "C",
     "text": "amounts = []\ntry:\n    for r in rows:\n        amounts.append(to_amount(r))\nexcept ValueError:\n    print(\"bad row found\")",
     "code": true
    },
    {
     "letter": "D",
     "text": "amounts = [float(r.replace(\",\", \"\")) for r in rows if r.strip()]",
     "code": true
    }
   ],
   "explain": "Only a try/except inside the loop catches every failing value and keeps a record of it. Skipping named strings misses the next bad value; a try around the whole loop drops every row after the first failure.",
   "correct": "A"
  },
  {
   "id": "Q10",
   "section": "A",
   "fmt": "Spot the bug",
   "genai": false,
   "stem": [
    "The code should print the customer with the highest spend, but it prints ('Zara', 700). Why?"
   ],
   "lang": "python",
   "code": [
    "customers = [(\"Asha\", 4200), (\"Ravi\", 9100), (\"Zara\", 700)]",
    "top = sorted(customers)[-1]",
    "print(top)"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "sorted() returns ascending order, so [-1] picks the smallest value rather than the largest",
     "code": false
    },
    {
     "letter": "B",
     "text": "Tuples cannot be compared with each other, so the data must be a list of lists first",
     "code": false
    },
    {
     "letter": "C",
     "text": "700 is compared as text, and the string '7' sorts after '4' and '9'",
     "code": false
    },
    {
     "letter": "D",
     "text": "sorted() orders tuples by their first element, the name, unless a key is given",
     "code": false
    }
   ],
   "explain": "Tuples compare element by element from the first, so sorted() orders by name. sorted(customers, key=lambda c: c[1])[-1] gives the highest spend.",
   "correct": "D"
  },
  {
   "id": "Q11",
   "section": "A",
   "fmt": "Predict the output",
   "genai": true,
   "stem": [
    "Kavya builds a classification prompt from a template. What happens on the second line?"
   ],
   "lang": "python",
   "code": [
    "template = ('Classify the ticket as one of {labels}. '",
    "            'Reply as JSON: {\"label\": ...}. Ticket: {ticket}')",
    "prompt = template.format(labels=\"refund, delivery, other\", ticket=\"My parcel never came\")"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "The prompt is built with both placeholders filled and the JSON kept as written",
     "code": false
    },
    {
     "letter": "B",
     "text": "KeyError, since the braces around \"label\" read as a third placeholder",
     "code": false
    },
    {
     "letter": "C",
     "text": "SyntaxError, since double quotes cannot sit inside a single-quoted string",
     "code": false
    },
    {
     "letter": "D",
     "text": "The prompt is built but {ticket} is left unfilled because it comes last",
     "code": false
    }
   ],
   "explain": "str.format() treats every {...} as a placeholder, so {\"label\": ...} is read as a field named \"label\" and raises KeyError. Double the braces ({{ }}) or build the JSON part separately.",
   "correct": "B"
  },
  {
   "id": "Q12",
   "section": "A",
   "fmt": "Fix the code",
   "genai": false,
   "stem": [
    "grid should be two independent rows of three zeros. After grid[0][1] = 7 it prints [[0, 7, 0], [0, 7, 0]]. Which first line gives [[0, 7, 0], [0, 0, 0]]?"
   ],
   "lang": "python",
   "code": [
    "grid = [[0] * 3] * 2",
    "grid[0][1] = 7",
    "print(grid)"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "grid = [[0, 0, 0]] * 2",
     "code": true
    },
    {
     "letter": "B",
     "text": "grid = list([[0] * 3] * 2)",
     "code": true
    },
    {
     "letter": "C",
     "text": "grid = [[0] * 3 for _ in range(2)]",
     "code": true
    },
    {
     "letter": "D",
     "text": "grid = [[0] * 3] * 2 and then grid = grid.copy()",
     "code": true
    }
   ],
   "explain": "[[0] * 3] * 2 repeats one inner list twice, so both rows are the same object; list() and copy() copy only the outer list. A comprehension builds a fresh inner list for each row.",
   "correct": "C"
  },
  {
   "id": "Q13",
   "section": "B",
   "fmt": "Predict the result",
   "genai": false,
   "stem": [
    "The orders table below is used for Q13 to Q16 and Q18. What does this query return?"
   ],
   "lang": "sql",
   "code": [
    "SELECT COUNT(*), COUNT(amount), SUM(amount)",
    "FROM orders",
    "WHERE status <> 'cancelled';"
   ],
   "numbered": false,
   "table": {
    "headers": [
     "order_id",
     "customer_id",
     "tier",
     "order_date",
     "amount",
     "status"
    ],
    "rows": [
     [
      "1",
      "C1",
      "Plus",
      "2026-04-02",
      "1200",
      "paid"
     ],
     [
      "2",
      "C2",
      "Basic",
      "2026-04-03",
      "NULL",
      "paid"
     ],
     [
      "3",
      "C1",
      "Plus",
      "2026-04-05",
      "800",
      "cancelled"
     ],
     [
      "4",
      "C3",
      "Student",
      "2026-04-06",
      "300",
      "paid"
     ],
     [
      "5",
      "C2",
      "Basic",
      "2026-04-09",
      "500",
      "paid"
     ]
    ],
    "widths": [
     1200,
     1500,
     1300,
     1700,
     1300,
     1400
    ]
   },
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "4, 4, 2000",
     "code": false
    },
    {
     "letter": "B",
     "text": "4, 3, 2000",
     "code": false
    },
    {
     "letter": "C",
     "text": "5, 4, 2800",
     "code": false
    },
    {
     "letter": "D",
     "text": "4, 3, NULL",
     "code": false
    }
   ],
   "explain": "COUNT(*) counts rows, COUNT(amount) counts non-NULL amounts, and SUM ignores NULL. After the WHERE removes the cancelled order, four rows remain, three with an amount, summing to 2000.",
   "correct": "B"
  },
  {
   "id": "Q14",
   "section": "B",
   "fmt": "Fix the query",
   "genai": false,
   "stem": [
    "On Postgres this query returns 0 for the orders table, where one order in five is cancelled. Which version returns 0.2?"
   ],
   "lang": "sql",
   "code": [
    "SELECT SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*) AS cancel_rate",
    "FROM orders;"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) * 1.0 / COUNT(*)",
     "code": true
    },
    {
     "letter": "B",
     "text": "ROUND(SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2)",
     "code": true
    },
    {
     "letter": "C",
     "text": "COUNT(status = 'cancelled') / COUNT(*)",
     "code": true
    },
    {
     "letter": "D",
     "text": "AVG(status = 'cancelled')",
     "code": true
    }
   ],
   "explain": "Both operands are integers, so Postgres does integer division and 1 / 5 becomes 0. Multiplying by 1.0 (or casting) makes the division decimal.",
   "correct": "A"
  },
  {
   "id": "Q15",
   "section": "B",
   "fmt": "Predict the result",
   "genai": false,
   "stem": [
    "Against the orders table, what does this query return?"
   ],
   "lang": "sql",
   "code": [
    "SELECT tier, COUNT(*) AS n",
    "FROM orders",
    "WHERE status = 'paid'",
    "GROUP BY tier",
    "HAVING COUNT(*) > 1;"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Plus 2 and Basic 2",
     "code": false
    },
    {
     "letter": "B",
     "text": "Basic 2, Plus 1 and Student 1",
     "code": false
    },
    {
     "letter": "C",
     "text": "No rows, because HAVING must refer to the alias n",
     "code": false
    },
    {
     "letter": "D",
     "text": "Basic 2 only",
     "code": false
    }
   ],
   "explain": "WHERE removes the cancelled order before grouping, so Plus has one paid order. HAVING then keeps only groups with more than one row: Basic with 2.",
   "correct": "D"
  },
  {
   "id": "Q16",
   "section": "B",
   "fmt": "Spot the bug",
   "genai": false,
   "stem": [
    "Kavya expects 4 (five orders minus the one at 800) but gets 3. Why?"
   ],
   "lang": "sql",
   "code": [
    "SELECT COUNT(*) FROM orders WHERE amount <> 800;"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "<> is not valid in Postgres, so != must be used for the comparison to run",
     "code": false
    },
    {
     "letter": "B",
     "text": "COUNT(*) skips any row that has a NULL in any of its columns",
     "code": false
    },
    {
     "letter": "C",
     "text": "NULL compared with 800 is neither true nor false, so that row is dropped",
     "code": false
    },
    {
     "letter": "D",
     "text": "The cancelled row is left out automatically because its status is not paid",
     "code": false
    }
   ],
   "explain": "A comparison with NULL yields unknown, and WHERE keeps only rows that are true, so the NULL-amount order is dropped along with the 800. Use amount <> 800 OR amount IS NULL if NULL rows should count.",
   "correct": "C"
  },
  {
   "id": "Q17",
   "section": "B",
   "fmt": "Spot the bug and fix it",
   "genai": false,
   "stem": [
    "Anand wants one row per customer with the count of orders placed in 2026, including customers with none. The tables and the query are below. The query returns only C1 2 and C3 1. Which one-line change returns C1 2, C2 0, C3 1, C4 0?"
   ],
   "lang": "sql",
   "code": [
    "SELECT c.customer_id, COUNT(o.order_id) AS orders_2026",
    "FROM customers c",
    "LEFT JOIN orders o ON o.customer_id = c.customer_id",
    "WHERE o.order_date >= '2026-01-01'",
    "GROUP BY c.customer_id;"
   ],
   "numbered": false,
   "table": null,
   "tables": [
    {
     "caption": "customers",
     "headers": [
      "customer_id"
     ],
     "rows": [
      [
       "C1"
      ],
      [
       "C2"
      ],
      [
       "C3"
      ],
      [
       "C4"
      ]
     ],
     "widths": [
      1800
     ]
    },
    {
     "caption": "orders",
     "headers": [
      "order_id",
      "customer_id",
      "order_date"
     ],
     "rows": [
      [
       "1",
       "C1",
       "2026-01-15"
      ],
      [
       "2",
       "C2",
       "2025-11-03"
      ],
      [
       "3",
       "C1",
       "2026-03-02"
      ],
      [
       "4",
       "C3",
       "2026-02-20"
      ]
     ],
     "widths": [
      1400,
      1600,
      1900
     ]
    }
   ],
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Move the date condition from WHERE into the ON clause",
     "code": false
    },
    {
     "letter": "B",
     "text": "Change COUNT(o.order_id) to COUNT(*) so that the empty rows are counted",
     "code": false
    },
    {
     "letter": "C",
     "text": "Change LEFT JOIN to RIGHT JOIN so that the customers side is kept",
     "code": false
    },
    {
     "letter": "D",
     "text": "Add HAVING COUNT(o.order_id) >= 0 after GROUP BY",
     "code": false
    }
   ],
   "explain": "The LEFT JOIN keeps C2 and C4 with NULL order columns, but the WHERE on o.order_date then throws those rows away. A condition in ON filters the right side before the join, so every customer survives.",
   "correct": "A"
  },
  {
   "id": "Q18",
   "section": "B",
   "fmt": "Predict the result",
   "genai": false,
   "stem": [
    "Against the orders table, what happens when this runs on Postgres?"
   ],
   "lang": "sql",
   "code": [
    "SELECT customer_id, SUM(amount) AS total",
    "FROM orders",
    "WHERE SUM(amount) > 1000",
    "GROUP BY customer_id;"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "It returns the customers whose total is above 1000, in the order they appear",
     "code": false
    },
    {
     "letter": "B",
     "text": "It fails: an aggregate is not allowed in WHERE; the condition belongs in HAVING",
     "code": false
    },
    {
     "letter": "C",
     "text": "It returns every customer, since WHERE runs before SUM exists and is quietly skipped",
     "code": false
    },
    {
     "letter": "D",
     "text": "It returns no rows, since SUM is NULL at the moment WHERE is evaluated",
     "code": false
    }
   ],
   "explain": "WHERE runs row by row before any grouping, so no aggregate exists yet and Postgres refuses the query. HAVING SUM(amount) > 1000 after GROUP BY is the right place.",
   "correct": "B"
  },
  {
   "id": "Q19",
   "section": "B",
   "fmt": "Predict the result",
   "genai": true,
   "stem": [
    "Farhan's team logs every LLM call made on a support ticket. The llm_calls table below is used for Q19 and Q20. What does this query return?"
   ],
   "lang": "sql",
   "code": [
    "SELECT ticket_id, call_id",
    "FROM (",
    "  SELECT ticket_id, call_id,",
    "         ROW_NUMBER() OVER (PARTITION BY ticket_id ORDER BY call_id DESC) AS rn",
    "  FROM llm_calls",
    ") t",
    "WHERE rn = 1",
    "ORDER BY ticket_id;"
   ],
   "numbered": false,
   "table": {
    "headers": [
     "call_id",
     "ticket_id",
     "model",
     "prompt_tokens",
     "completion_tokens",
     "cost"
    ],
    "rows": [
     [
      "1",
      "T1",
      "small",
      "400",
      "100",
      "0.02"
     ],
     [
      "2",
      "T1",
      "large",
      "1200",
      "300",
      "0.30"
     ],
     [
      "3",
      "T2",
      "small",
      "800",
      "50",
      "0.03"
     ],
     [
      "4",
      "T3",
      "large",
      "600",
      "200",
      "0.30"
     ],
     [
      "5",
      "T2",
      "small",
      "200",
      "20",
      "0.01"
     ]
    ],
    "widths": [
     1100,
     1300,
     1200,
     1900,
     2300,
     1100
    ]
   },
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "(T1, 1), (T2, 3), (T3, 4)",
     "code": false
    },
    {
     "letter": "B",
     "text": "Five rows, because ROW_NUMBER never removes rows",
     "code": false
    },
    {
     "letter": "C",
     "text": "An error, because a window function cannot be used to filter rows",
     "code": false
    },
    {
     "letter": "D",
     "text": "(T1, 2), (T2, 5), (T3, 4)",
     "code": false
    }
   ],
   "explain": "ROW_NUMBER() numbers each ticket's calls from the highest call_id down, and rn = 1 in the outer query keeps the latest call per ticket. The window function sits in a subquery, which is why filtering on it works.",
   "correct": "D"
  },
  {
   "id": "Q20",
   "section": "B",
   "fmt": "Fix the query",
   "genai": true,
   "stem": [
    "tickets holds one row per ticket with its category: T1 refund, T2 delivery, T3 refund. ticket_tags holds (T1, urgent), (T1, vip), (T2, urgent), (T3, vip). Anand asks for LLM spend by ticket category.",
    "The query returns refund 0.94 and delivery 0.04, which adds to 0.98, while the cost column of llm_calls sums to 0.66. Which change gives the right totals?"
   ],
   "lang": "sql",
   "code": [
    "SELECT t.category, SUM(c.cost) AS spend",
    "FROM llm_calls c",
    "JOIN tickets t ON t.ticket_id = c.ticket_id",
    "JOIN ticket_tags g ON g.ticket_id = t.ticket_id",
    "GROUP BY t.category;"
   ],
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Change SUM(c.cost) to SUM(DISTINCT c.cost), so each cost value is added only once",
     "code": false
    },
    {
     "letter": "B",
     "text": "Add DISTINCT after SELECT, so repeated rows are removed before summing",
     "code": false
    },
    {
     "letter": "C",
     "text": "Drop the ticket_tags join; the question never uses tags and it repeats T1's calls",
     "code": false
    },
    {
     "letter": "D",
     "text": "Change JOIN tickets to LEFT JOIN tickets, so no ticket is lost from the totals",
     "code": false
    }
   ],
   "explain": "A ticket can carry several tags, so joining ticket_tags repeats every llm_calls row once per tag; T1's two tags double its spend. Drop the join. SUM(DISTINCT) would also merge the two genuine 0.30 costs into one.",
   "correct": "C"
  },
  {
   "id": "Q21",
   "section": "C",
   "fmt": "Reason with numbers",
   "genai": false,
   "stem": [
    "Kalpa Retail revenue fell 12 percent from Q1 to Q2 while the order count rose 5 percent. Which statement about the average order value must be true?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "It fell by about 7 percent",
     "code": false
    },
    {
     "letter": "B",
     "text": "It fell by about 12 percent",
     "code": false
    },
    {
     "letter": "C",
     "text": "It cannot be determined without the number of customers",
     "code": false
    },
    {
     "letter": "D",
     "text": "It fell by about 16 percent",
     "code": false
    }
   ],
   "explain": "Average order value is revenue divided by orders: 0.88 / 1.05 is about 0.84, a fall of roughly 16 percent. Percentage changes divide; they do not subtract.",
   "correct": "D"
  },
  {
   "id": "Q22",
   "section": "C",
   "fmt": "Reason with numbers",
   "genai": false,
   "stem": [
    "Five Plus customers spent Rs 300, 350, 400, 450 and 9,000 this quarter. Meera wants one number on her slide for 'what a typical Plus customer spends'. Which number, and why?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "400, the median, since one bulk buyer drags the mean above the other four",
     "code": false
    },
    {
     "letter": "B",
     "text": "2,100, the mean, since it is the only number that uses every value",
     "code": false
    },
    {
     "letter": "C",
     "text": "300 to 9,000, the range, since any single number would mislead the board",
     "code": false
    },
    {
     "letter": "D",
     "text": "1,250, the midpoint between the mean and the median, as a compromise",
     "code": false
    }
   ],
   "explain": "Four of the five customers spent 300 to 450; the mean of 2,100 describes none of them. The median, 400, is what 'typical' means here.",
   "correct": "A"
  },
  {
   "id": "Q23",
   "section": "C",
   "fmt": "Reason with numbers",
   "genai": false,
   "stem": [
    "A monsoon discount email went to 20,000 customers and produced 400 orders. A plain email went to 5,000 customers and produced 150 orders. Which group responded better?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "The discount group, since 400 orders is more than double 150",
     "code": false
    },
    {
     "letter": "B",
     "text": "The plain-email group, since 3 percent beats 2 percent",
     "code": false
    },
    {
     "letter": "C",
     "text": "They are level once the group sizes are allowed for",
     "code": false
    },
    {
     "letter": "D",
     "text": "It cannot be judged without the revenue per order",
     "code": false
    }
   ],
   "explain": "Compare rates, not counts: 150 / 5,000 is 3 percent and 400 / 20,000 is 2 percent. The plain email did better per person reached.",
   "correct": "B"
  },
  {
   "id": "Q24",
   "section": "C",
   "fmt": "Two statements",
   "genai": false,
   "stem": [
    "Statement I: A number that rises 10 percent and then falls 10 percent is back where it started.",
    "Statement II: A number that falls 50 percent needs a rise of 100 percent to recover."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Only I is true",
     "code": false
    },
    {
     "letter": "B",
     "text": "Both are true",
     "code": false
    },
    {
     "letter": "C",
     "text": "Only II is true",
     "code": false
    },
    {
     "letter": "D",
     "text": "Neither is true",
     "code": false
    }
   ],
   "explain": "1.10 x 0.90 = 0.99, so Statement I is false. Halving needs a doubling to recover, so Statement II is true.",
   "correct": "C"
  },
  {
   "id": "Q25",
   "section": "C",
   "fmt": "Reason with numbers",
   "genai": false,
   "stem": [
    "A clinic with 50 bookings a week saw its no-show rate go from 10 percent to 14 percent this week. What is the fairest reading?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Two extra no-shows out of 50 sits inside normal week-to-week noise; watch a few more weeks",
     "code": false
    },
    {
     "letter": "B",
     "text": "A rise from 10 to 14 percent is a 40 percent jump in the rate, which needs action this week",
     "code": false
    },
    {
     "letter": "C",
     "text": "The rate has been miscalculated, since 7 out of 50 is 12 percent and not 14",
     "code": false
    },
    {
     "letter": "D",
     "text": "Nothing can be said either way until a proper significance test has been run",
     "code": false
    }
   ],
   "explain": "The rate moved from 5 no-shows to 7 out of 50. A change of two events sits well inside week-to-week noise for a count that small; several more weeks are needed before it means anything.",
   "correct": "A"
  },
  {
   "id": "Q26",
   "section": "C",
   "fmt": "Reason with numbers",
   "genai": false,
   "stem": [
    "A fraud model flags 5 percent of all transactions. It catches 90 percent of the transactions that are actually fraudulent, and fraud is 1 percent of all transactions. Of the flagged transactions, roughly what share are actually fraud?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "About 90 percent",
     "code": false
    },
    {
     "letter": "B",
     "text": "About 5 percent",
     "code": false
    },
    {
     "letter": "C",
     "text": "About 1 percent",
     "code": false
    },
    {
     "letter": "D",
     "text": "About 18 percent",
     "code": false
    }
   ],
   "explain": "Of 1,000 transactions, 10 are fraud and the model catches 9 of them, while it flags 50 in total. So 9 of 50 flagged transactions, about 18 percent, are fraud. Catching 90 percent of fraud (recall) is not the same as 90 percent of flags being fraud (precision).",
   "correct": "D"
  },
  {
   "id": "Q27",
   "section": "C",
   "fmt": "Reason with numbers",
   "genai": false,
   "stem": [
    "Overall conversion fell from 5 percent to 4 percent, yet conversion rose in every single city. How can both be true?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "They cannot both be true, since the total is just the cities added up; one figure must be wrong",
     "code": false
    },
    {
     "letter": "B",
     "text": "The mix shifted toward cities with lower conversion, so the total fell as each city rose",
     "code": false
    },
    {
     "letter": "C",
     "text": "Rounding in the city figures hides small falls that only show up in the total",
     "code": false
    },
    {
     "letter": "D",
     "text": "Seasonality moves the total without moving any single city's own figure",
     "code": false
    }
   ],
   "explain": "The overall rate is a weighted average of the city rates. If more customers now come from low-conversion cities, the total can fall while every city improves. This is a mix shift.",
   "correct": "B"
  },
  {
   "id": "Q28",
   "section": "C",
   "fmt": "Estimate",
   "genai": true,
   "stem": [
    "Farhan plans one LLM call per support ticket. Suppose the model bills Rs 40 per million input tokens and Rs 160 per million output tokens, and a call uses about 1,200 input tokens and 200 output tokens. At 1,000 tickets a day for 30 days, the monthly bill is closest to"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Rs 1,440",
     "code": false
    },
    {
     "letter": "B",
     "text": "Rs 6,720",
     "code": false
    },
    {
     "letter": "C",
     "text": "Rs 2,400",
     "code": false
    },
    {
     "letter": "D",
     "text": "Rs 24,000",
     "code": false
    }
   ],
   "explain": "Input: 1,000 x 1,200 x 30 = 36 million tokens, Rs 1,440 at Rs 40 per million. Output: 6 million tokens, Rs 960 at Rs 160 per million. Total Rs 2,400 a month.",
   "correct": "C"
  },
  {
   "id": "Q29",
   "section": "D",
   "fmt": "Case: Kalpa Retail, Q1 against Q2",
   "genai": false,
   "stem": [
    "Which line best explains most of the fall?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": {
    "headers": [
     "Tier",
     "Q1 customers",
     "Q1 orders",
     "Q1 revenue",
     "Q2 customers",
     "Q2 orders",
     "Q2 revenue"
    ],
    "rows": [
     [
      "Plus",
      "10,000",
      "30,000",
      "360",
      "10,000",
      "27,000",
      "324"
     ],
     [
      "Basic",
      "40,000",
      "60,000",
      "420",
      "44,000",
      "64,000",
      "400"
     ],
     [
      "Student",
      "5,000",
      "6,000",
      "24",
      "8,000",
      "9,000",
      "36"
     ],
     [
      "Total",
      "55,000",
      "96,000",
      "804",
      "62,000",
      "100,000",
      "760"
     ]
    ]
   },
   "tables": null,
   "case_intro": [
    "Meera Raghavan, CEO of Kalpa Retail, has one question for the analytics team: revenue fell from Q1 to Q2, where did it go? Kavya Nair pulled the table below. Use it for Q29 to Q32. Revenue is in Rs lakh."
   ],
   "options": [
    {
     "letter": "A",
     "text": "Plus customers ordered less often at the same order value; that tier carries most of the fall",
     "code": false
    },
    {
     "letter": "B",
     "text": "Basic customers paid less per order than in Q1; that tier carries most of the fall",
     "code": false
    },
    {
     "letter": "C",
     "text": "Student growth pulled spending away from the Plus tier, which is why Plus orders fell by a tenth",
     "code": false
    },
    {
     "letter": "D",
     "text": "Fewer customers overall placed orders in Q2, which lowered revenue across every tier",
     "code": false
    }
   ],
   "explain": "Plus revenue fell 36 lakh (orders down 10 percent at an unchanged Rs 1,200 per order), Basic fell 20 lakh, Student rose 12 lakh. Plus alone explains most of the net 44 lakh fall.",
   "correct": "A"
  },
  {
   "id": "Q30",
   "section": "D",
   "fmt": "Case: Kalpa Retail, Q1 against Q2",
   "genai": false,
   "stem": [
    "Kavya's first hypothesis is that Plus customers are downgrading to Basic. What does the table say about it?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "It supports it, since Basic gained 4,000 customers",
     "code": false
    },
    {
     "letter": "B",
     "text": "It supports it, since the Basic order value fell",
     "code": false
    },
    {
     "letter": "C",
     "text": "It weakens it, since the Plus customer count did not fall",
     "code": false
    },
    {
     "letter": "D",
     "text": "It cannot be judged without customer-level churn data from both quarters",
     "code": false
    }
   ],
   "explain": "Plus customers were 10,000 in both quarters. If Plus customers had moved to Basic, the Plus count would have dropped. The table weakens the hypothesis.",
   "correct": "C"
  },
  {
   "id": "Q31",
   "section": "D",
   "fmt": "Case: Kalpa Retail, Q1 against Q2",
   "genai": false,
   "stem": [
    "A monsoon discount was given to some Basic customers in Q2. Meera asks whether it caused the rise in Basic orders. Which comparison is the fairest one available?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Basic Q2 orders against Basic Q1 orders, since the before-and-after is the change in question",
     "code": false
    },
    {
     "letter": "B",
     "text": "Discounted Basic customers against non-discounted Basic customers, same weeks",
     "code": false
    },
    {
     "letter": "C",
     "text": "Basic Q2 orders against Plus Q2 orders, since Plus had no discount",
     "code": false
    },
    {
     "letter": "D",
     "text": "Basic Q2 revenue against the plan line, since the plan assumed no discount",
     "code": false
    }
   ],
   "explain": "The fair comparison holds everything else constant: same tier, same weeks, the discount as the only difference. Before-and-after and cross-tier comparisons mix the discount with every other change.",
   "correct": "B"
  },
  {
   "id": "Q32",
   "section": "D",
   "fmt": "Case: Kalpa Retail, Q1 against Q2",
   "genai": false,
   "stem": [
    "Before you put the Plus finding in front of Meera, which check protects the finding most?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Ask for the Plus tier's marketing budget for Q2 and compare it with Q1's",
     "code": false
    },
    {
     "letter": "B",
     "text": "Re-add the six revenue figures in a spreadsheet to confirm that the totals match the table exactly",
     "code": false
    },
    {
     "letter": "C",
     "text": "Compute the Plus tier's share of total revenue in each quarter and compare",
     "code": false
    },
    {
     "letter": "D",
     "text": "Check that Q1 and Q2 have the same trading days and that no festival sat in one quarter only",
     "code": false
    }
   ],
   "explain": "A quarter with fewer trading days, or a festival that sat in Q1 only, can create the whole fall on its own. Checking the window protects the finding; the other options describe or re-add the same numbers.",
   "correct": "D"
  },
  {
   "id": "Q33",
   "section": "D",
   "fmt": "Scenario: LLM intuition",
   "genai": true,
   "stem": [
    "Farhan's team uses an LLM to label each support ticket as refund, delivery or other. The prompt says only 'Label this ticket'. Sending the same ticket twice gives refund once and delivery the second time. Which explanation and first fix fit best?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Sampling above zero temperature varies the reply, and the prompt never names the labels; lower it and list the three labels with an example each",
     "code": false
    },
    {
     "letter": "B",
     "text": "The model remembers the first call and changed its mind on the second; clear its conversation history before every call so each starts fresh",
     "code": false
    },
    {
     "letter": "C",
     "text": "The ticket text must contain a typo or odd formatting that confuses the model; clean the data before calling again and re-check",
     "code": false
    },
    {
     "letter": "D",
     "text": "The model is too small for a three-way classification; switch to the largest model available and re-run the whole batch",
     "code": false
    }
   ],
   "explain": "Sampling with a temperature above zero makes replies vary, and a prompt that never lists the allowed labels leaves the model to invent them. Lower the temperature and give the label set with an example each. API calls carry no memory of each other unless the history is sent.",
   "correct": "A"
  },
  {
   "id": "Q34",
   "section": "D",
   "fmt": "Scenario: LLM intuition",
   "genai": true,
   "stem": [
    "Kavya's prompt asks a model to rate the sentiment of each customer review from 1 to 5. On 200 reviews the ratings look plausible. Which check tells her fastest whether the ratings can be trusted?"
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Ask the model to add a confidence score to each rating and keep the high ones",
     "code": false
    },
    {
     "letter": "B",
     "text": "Hand-rate a random 30 reviews herself and compare with the model's ratings",
     "code": false
    },
    {
     "letter": "C",
     "text": "Run the prompt through a second model and average the two ratings for each review",
     "code": false
    },
    {
     "letter": "D",
     "text": "Add 'be accurate and careful' to the prompt and re-run the whole batch",
     "code": false
    }
   ],
   "explain": "Ratings that look plausible are not evidence. Hand-rating a random sample and comparing gives a measured agreement rate within an hour; confidence scores and a second model only add more unverified output.",
   "correct": "B"
  },
  {
   "id": "Q35",
   "section": "E",
   "fmt": "Best and worst",
   "genai": false,
   "stem": [
    "You sent Anand Iyer, the Finance Controller, the quarterly revenue figure yesterday. This morning you find your query counted returned orders as sales, so the figure is about 4 percent too high, and it is already in a board deck. Mark the best action and the worst action."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Fix the query so next month's figure is right and say nothing about this one, since 4 percent sits inside normal variance",
     "code": false
    },
    {
     "letter": "B",
     "text": "Ask a peer to re-run your query and send a correction only once they confirm the error is real",
     "code": false
    },
    {
     "letter": "C",
     "text": "Send Anand the corrected figure now, with the cause and size of the error",
     "code": false
    },
    {
     "letter": "D",
     "text": "Tell your reporting manager and let them decide whether Finance needs to hear about it",
     "code": false
    }
   ],
   "explain": {
    "best": "Sending the correction yourself, now, with the cause and the size, is the only option that protects the board figure and your credibility at once.",
    "worst": "Saying nothing about a known error in a board figure is the one action that destroys trust when it surfaces later, and it always surfaces."
   },
   "best": "C",
   "worst": "A"
  },
  {
   "id": "Q36",
   "section": "E",
   "fmt": "Best and worst",
   "genai": true,
   "stem": [
    "During an ungraded exercise you got the answer from an AI assistant and submitted it without understanding it. The trainer asks you to explain your approach to the room. Mark the best action and the worst action."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Ask the trainer to come back to you once you have had time to study the answer properly",
     "code": false
    },
    {
     "letter": "B",
     "text": "Say you used an AI assistant, then walk through what you do and do not yet understand",
     "code": false
    },
    {
     "letter": "C",
     "text": "Ask the person next to you, who solved it without help, to explain the approach instead",
     "code": false
    },
    {
     "letter": "D",
     "text": "Present the answer as your own reasoning and improvise wherever the logic is unclear to you",
     "code": false
    }
   ],
   "explain": {
    "best": "Naming the tool and what you do not yet understand is the honest answer and the one that gets you help on the spot.",
    "worst": "Presenting borrowed reasoning as your own compounds the gap and is found out within minutes of the first question."
   },
   "best": "B",
   "worst": "D"
  },
  {
   "id": "Q37",
   "section": "E",
   "fmt": "Best and worst",
   "genai": false,
   "stem": [
    "During your group's presentation a group-mate says, in front of the panel, that your chart is misleading. Mark the best action and the worst action."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Say nothing now, since the panel is watching, and fix the chart after the presentation",
     "code": false
    },
    {
     "letter": "B",
     "text": "Point out that their own section had errors too, so the panel hears both sides",
     "code": false
    },
    {
     "letter": "C",
     "text": "Defend the chart, since you checked the numbers twice before the presentation",
     "code": false
    },
    {
     "letter": "D",
     "text": "Ask what specifically misleads and offer to fix it before the presentation moves on",
     "code": false
    }
   ],
   "explain": {
    "best": "Asking what specifically misleads, in front of the panel, turns criticism into a fix and shows the panel how you work.",
    "worst": "Retaliating in front of the panel damages both of you and answers nothing about the chart."
   },
   "best": "D",
   "worst": "B"
  },
  {
   "id": "Q38",
   "section": "E",
   "fmt": "Best and worst",
   "genai": false,
   "stem": [
    "A take-home is due tonight. Your notebook runs, but the answer to the last question is wrong and you know why; the fix needs two more hours. Mark the best action and the worst action."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Submit on time with a note saying which part is wrong, why, and when the fix follows",
     "code": false
    },
    {
     "letter": "B",
     "text": "Message the TA that you will submit tomorrow with the fix included, since correctness matters more",
     "code": false
    },
    {
     "letter": "C",
     "text": "Submit as it is and say nothing, since the notebook runs and the deadline is what counts",
     "code": false
    },
    {
     "letter": "D",
     "text": "Submit only the parts that are right and quietly drop the last question from the notebook",
     "code": false
    }
   ],
   "explain": {
    "best": "Submitting on time with a note that names the wrong part, the cause and the fix date keeps both the deadline and your credibility.",
    "worst": "Knowingly submitting a wrong answer as right is exactly the failure the note would have prevented."
   },
   "best": "A",
   "worst": "C"
  },
  {
   "id": "Q39",
   "section": "E",
   "fmt": "Best and worst",
   "genai": false,
   "stem": [
    "You have spent 90 minutes stuck on an environment error while the session moves on without you. Mark the best action and the worst action."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Ask the person next to you to do the setup on your machine so you can catch up with the session",
     "code": false
    },
    {
     "letter": "B",
     "text": "Wait until the end of the day and email a screenshot of the error to the TA",
     "code": false
    },
    {
     "letter": "C",
     "text": "Post the exact error text in the Discussions thread and continue with the parts that need no setup",
     "code": false
    },
    {
     "letter": "D",
     "text": "Keep trying alone, since asking now would show the room you cannot handle the basics",
     "code": false
    }
   ],
   "explain": {
    "best": "Posting the exact error text is the fastest route to a fix, and working on the parts that need no environment keeps the day productive.",
    "worst": "Ninety minutes alone is already too long; asking early is the habit the programme depends on."
   },
   "best": "C",
   "worst": "D"
  },
  {
   "id": "Q40",
   "section": "E",
   "fmt": "Best and worst",
   "genai": false,
   "stem": [
    "Anand says your analysis 'cannot be right' because it contradicts his experience, and asks you to change the conclusion before the meeting. Mark the best action and the worst action."
   ],
   "lang": null,
   "code": null,
   "numbered": false,
   "table": null,
   "tables": null,
   "case_intro": null,
   "options": [
    {
     "letter": "A",
     "text": "Change the conclusion; he has run Finance for years and knows the business better than the data",
     "code": false
    },
    {
     "letter": "B",
     "text": "Walk him through the path from raw table to final number and ask which step he doubts",
     "code": false
    },
    {
     "letter": "C",
     "text": "Tell him the numbers do not lie and keep the conclusion exactly as it is",
     "code": false
    },
    {
     "letter": "D",
     "text": "Escalate to Meera at once so she can decide between his experience and your analysis",
     "code": false
    }
   ],
   "explain": {
    "best": "Walking through the path from raw table to number lets him point at the step he doubts, which is either a real error or the end of the disagreement.",
    "worst": "Changing a conclusion because of pushback abandons the evidence and makes the analysis worthless to everyone, including him."
   },
   "best": "B",
   "worst": "A"
  }
 ]
};

const SECTION_ORDER = ['A', 'B', 'C', 'D', 'E'];
const SECTION_BLURB = {
  A: 'Every question shows real code. Read it line by line; the answer is in what the code does, never in what it was meant to do.',
  B: 'The small tables are shown once and reused where a question says so. NULL means the value is missing. Assume PostgreSQL.',
  C: 'Rough arithmetic is enough; every answer is far from its neighbours.',
  D: 'Q29 to Q32 use one case. Read the table once, then answer all four before moving on. Q33 and Q34 are stand-alone scenarios.',
  E: 'Each situation has two questions: the best action and the worst action. There is no neutral choice; every option has consequences.',
};

// ---------------------------------------------------------------------
// 1. Build
// ---------------------------------------------------------------------
function buildDiagnosticForm() {
  const form = FormApp.create(CONFIG.FORM_TITLE);
  form.setIsQuiz(true);
  form.setDescription(formDescription_());
  if (CONFIG.REQUIRE_SIGN_IN) { form.setCollectEmail(true); form.setLimitOneResponsePerUser(true); } else { form.setLimitOneResponsePerUser(false); }
  form.setProgressBar(true);
  form.setShuffleQuestions(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setPublishingSummary(false);
  form.setConfirmationMessage(
    'Submitted. Your score and the correct answers are behind the View score link, and a full report with an explanation for every question is on its way to the email address you typed. ' +
    'Nothing in this paper carries marks; it shapes this week\'s Python and SQL sessions and is discussed with you individually.');

  // Page 1: email, identity and the five self-ratings, filled before any question is seen
  form.addTextItem().setTitle('Email address')
    .setHelpText('Your full report, with every answer explained, is sent here the moment you submit. Type it carefully; it cannot be resent.')
    .setRequired(true)
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().setHelpText('That does not look like an email address.').build());
  form.addTextItem().setTitle('Student ID').setHelpText('As printed on your admission letter.').setRequired(true);
  form.addTextItem().setTitle('Full name').setRequired(true);
  form.addSectionHeaderItem().setTitle('Step one: rate yourself before you read any question')
    .setHelpText('Rate yourself from 1 to 4 on the five areas below, as you are today. The comparison between your rating and your score is the most useful thing this paper produces.\n\n' +
      BANK.CLAIMED_SCALE.join('\n'));
  BANK.CLAIMED_AREAS.forEach(a => {
    form.addScaleItem().setTitle('Self-rating: ' + a[0]).setBounds(1, 4)
      .setLabels('I have not used this', 'I can fix someone else\'s version').setRequired(true);
  });

  // Sections A to E
  const bySection = {};
  BANK.ITEMS.forEach(it => { (bySection[it.section] = bySection[it.section] || []).push(it); });
  SECTION_ORDER.forEach(sec => {
    const meta = BANK.SECTIONS[sec];
    const its = bySection[sec];
    form.addPageBreakItem().setTitle('Section ' + sec + '. ' + meta.title)
      .setHelpText(its.length + ' questions, ' + its[0].id + ' to ' + its[its.length - 1].id + ', about ' + meta.minutes + ' minutes. ' + SECTION_BLURB[sec]);
    let caseShown = false;
    its.forEach(it => {
      if (it.case_intro && !caseShown) {
        form.addSectionHeaderItem().setTitle('The case: ' + CONFIG.WORLD + ', Q1 against Q2').setHelpText(it.case_intro.join('\n'));
        if (!addImageIfAvailable_(form, it.id, CONFIG.WORLD + ' table, revenue in Rs lakh')) {
          form.addSectionHeaderItem().setTitle('Revenue in Rs lakh').setHelpText(tableText_(it.table));
        }
        caseShown = true;
      }
      if (sec === 'E') addJudgmentPair_(form, it); else addSingleKeyItem_(form, it);
    });
  });

  // Final page: the ten statements
  form.addPageBreakItem().setTitle('Ten statements about how you work')
    .setHelpText('These have no right answers and no marks. For each statement choose 1 to 5: 1 = not like me at all, 3 = sometimes like me, 5 = exactly like me.');
  form.addGridItem().setTitle('How you work').setRows(BANK.SELF_REPORT.map((s, i) => 'R' + (i + 1) + '. ' + s))
    .setColumns(['1', '2', '3', '4', '5']).setRequired(true);

  // Results spreadsheet with a Profiles tab mirroring the INTERNAL workbook's Entry columns
  const ss = SpreadsheetApp.create(CONFIG.RESULTS_SPREADSHEET_NAME);
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  ensureProfilesSheet_(ss);

  // Publish and open to responders
  if (form.supportsAdvancedResponderPermissions()) form.setPublished(true); else form.setAcceptingResponses(true);
  openToResponders_(form);

  PropertiesService.getScriptProperties().setProperties({ FORM_ID: form.getId(), SHEET_ID: ss.getId() });
  installSubmitTrigger();

  Logger.log('Form editor: ' + form.getEditUrl());
  Logger.log('Respond link: ' + form.getPublishedUrl());
  Logger.log('Results sheet: ' + ss.getUrl());
  Logger.log(manualChecklist_());
}

function formDescription_() {
  return CONFIG.ORG + ' | ' + CONFIG.PROGRAMME + ' | ' + CONFIG.COHORT + ' | ' + CONFIG.WEEK + '\n\n' +
    'This paper carries no marks and goes on no transcript. It shows you, and the people running your first week, where each of us should start. ' +
    'A blank answer tells us less than a wrong one, so answer every question.\n\n' +
    'Time: ' + CONFIG.TIME_MINUTES + ' minutes in one sitting; the section time guides are suggestions.\n' +
    'Tools: your own head only. No second tab, no notes, no AI assistant; rough working on paper is fine.\n' +
    'Answers: every question has four options and one best answer, except Section E, where each situation asks for the best action and the worst action.\n' +
    'Code: read it as written. Assume Python 3 and PostgreSQL unless the question says pseudocode.\n\n' +
    'Sections: A Python for data and GenAI (Q1 to Q12, 30 min) | B SQL for data and GenAI (Q13 to Q20, 20 min) | C Numbers and reasoning (Q21 to Q28, 14 min) | ' +
    'D Case and scenarios (Q29 to Q34, 10 min) | E Judgment calls (Q35 to Q40, 5 min).\n\n' +
    'Some questions are set inside ' + CONFIG.WORLD + ', a fictional company you will meet again from Week 1. Meera Raghavan is its CEO, Anand Iyer its Finance Controller, ' +
    'Kavya Nair its senior analyst and Farhan Sheikh its Head of Support. Nothing about it needs to be known in advance.';
}

// One graded multiple-choice question with an optional code or table image above it
function addSingleKeyItem_(form, it) {
  const hasImage = addImageIfAvailable_(form, it.id, it.id + ' code');
  const multiline = it.options.some(o => o.text.indexOf('\n') >= 0);
  const optionsAsImage = multiline && addImageIfAvailable_(form, it.id + '_options', it.id + ' options');
  const q = form.addMultipleChoiceItem();
  q.setTitle(it.id + ' \u00b7 ' + it.fmt);
  q.setHelpText(questionHelpText_(it, hasImage, multiline && !optionsAsImage));
  q.setChoices(it.options.map(o => q.createChoice(choiceLabel_(o, multiline), o.letter === it.correct)));
  q.setPoints(1).setRequired(true);
  const key = it.options.filter(o => o.letter === it.correct)[0];
  q.setFeedbackForCorrect(FormApp.createFeedback().setText('Right. ' + it.explain).build());
  q.setFeedbackForIncorrect(FormApp.createFeedback().setText('The answer is ' + key.letter + '. ' + it.explain).build());
}

// Section E: two graded questions per situation, best and worst
function addJudgmentPair_(form, it) {
  const scenario = it.stem.join('\n').replace(' Mark the best action and the worst action.', '');
  [['best', 'Best action', it.best, it.explain.best], ['worst', 'Worst action', it.worst, it.explain.worst]].forEach(([kind, label, key, explain], idx) => {
    const q = form.addMultipleChoiceItem();
    q.setTitle(it.id + ' \u00b7 ' + label);
    q.setHelpText(idx === 0 ? scenario + '\n\nWhich action is the best one?' : 'Same situation as above. Which action is the worst one?');
    q.setChoices(it.options.map(o => q.createChoice(choiceLabel_(o, false), o.letter === key)));
    q.setPoints(1).setRequired(true);
    q.setFeedbackForCorrect(FormApp.createFeedback().setText('Right. ' + explain).build());
    q.setFeedbackForIncorrect(FormApp.createFeedback().setText('The ' + kind + ' action is ' + key + '. ' + explain).build());
  });
}

function choiceLabel_(o, multiline) {
  if (multiline) return 'Option ' + o.letter;
  return o.letter + '. ' + o.text.replace(/\n/g, ' ');
}

// Stem, then tables and code as text when no image is available. Indentation survives as non-breaking spaces.
function questionHelpText_(it, hasImage, optionsAsText) {
  const parts = [it.stem.join('\n')];
  if (!hasImage) {
    if (it.tables) it.tables.forEach(t => parts.push(t.caption + '\n' + tableText_(t)));
    else if (it.table && !it.case_intro) parts.push(tableText_(it.table));
    if (it.code) {
      const lines = it.code.map((ln, i) => (it.numbered ? String(i + 1).padStart(2, ' ') + '  ' : '') + ln);
      parts.push(lines.map(nb_).join('\n'));
    }
  }
  if (optionsAsText) it.options.forEach(o => parts.push('Option ' + o.letter + '\n' + o.text.split('\n').map(nb_).join('\n')));
  return parts.join('\n\n');
}

function tableText_(t) {
  const rows = [t.headers].concat(t.rows);
  const widths = t.headers.map((_, c) => Math.max.apply(null, rows.map(r => String(r[c]).length)));
  const fmt = r => r.map((v, c) => String(v).padEnd(widths[c], ' ')).join('  ');
  return [fmt(t.headers), widths.map(w => '-'.repeat(w)).join('  ')].concat(t.rows.map(fmt)).map(nb_).join('\n');
}

function nb_(s) { return s.replace(/ /g, '\u00a0'); }

// Looks for <name>.png in CODE_IMAGE_FOLDER_ID; adds it as an image item and returns true, else false
function addImageIfAvailable_(form, name, alt) {
  if (!CONFIG.CODE_IMAGE_FOLDER_ID) return false;
  try {
    const files = DriveApp.getFolderById(CONFIG.CODE_IMAGE_FOLDER_ID).getFilesByName(name + '.png');
    if (!files.hasNext()) return false;
    form.addImageItem().setImage(files.next().getBlob()).setTitle(alt).setAlignment(FormApp.Alignment.LEFT).setWidth(720);
    return true;
  } catch (err) {
    Logger.log('Image ' + name + ' skipped: ' + err);
    return false;
  }
}

function openToResponders_(form) {
  if (CONFIG.RESPONDERS === 'list' && CONFIG.RESPONDER_EMAILS.length) {
    form.addPublishedReaders(CONFIG.RESPONDER_EMAILS);
    return;
  }
  if (CONFIG.RESPONDERS === 'anyone') {
    try {
      Drive.Permissions.create({ type: 'anyone', view: 'published', role: 'reader' }, form.getId());
    } catch (err) {
      Logger.log('Could not set "anyone with the link can respond" automatically (' + err + '). Switch on the Drive advanced service (Services > Drive API) and run setAnyoneWithLinkResponder(), or open the form, click Publish, and set Responders to anyone with the link.');
    }
  }
}

function setAnyoneWithLinkResponder() {
  const id = PropertiesService.getScriptProperties().getProperty('FORM_ID');
  Drive.Permissions.create({ type: 'anyone', view: 'published', role: 'reader' }, id);
  Logger.log('Anyone with the link can now respond.');
}

function manualChecklist_() {
  return 'Two settings the Forms service cannot set by script; check them once in the form\'s Settings tab: ' +
    '(1) Release grade: immediately after each submission. (2) Respondent can see: missed questions, correct answers, point values, all on. ' +
    'Both are the quiz defaults, so this is a ten-second confirmation. ' +
    'Then open the respond link in a private browser window: it must load without asking for a Google sign-in.';
}

// ---------------------------------------------------------------------
// 2. Trigger
// ---------------------------------------------------------------------
function installSubmitTrigger() {
  const id = PropertiesService.getScriptProperties().getProperty('FORM_ID');
  ScriptApp.getProjectTriggers().forEach(t => { if (t.getHandlerFunction() === 'onDiagnosticSubmit') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('onDiagnosticSubmit').forForm(FormApp.openById(id)).onFormSubmit().create();
  Logger.log('Submit trigger installed on form ' + id);
}

// ---------------------------------------------------------------------
// 3. On submit: score by section, write the profile row, email the report
// ---------------------------------------------------------------------
function onDiagnosticSubmit(e) {
  if (!e || !e.response) return;
  const lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    const result = scoreResponse_(e.response);
    appendProfileRow_(result);
    if (CONFIG.SEND_REPORT_EMAIL && result.email) sendReport_(result);
  } finally {
    lock.releaseLock();
  }
}

function scoreResponse_(formResponse) {
  const answers = {};   // title -> response string
  formResponse.getItemResponses().forEach(ir => { answers[ir.getItem().getTitle()] = ir.getResponse(); });
  const result = {
    timestamp: formResponse.getTimestamp(),
    email: String(answers['Email address'] || formResponse.getRespondentEmail() || '').trim().toLowerCase(),
    studentId: String(answers['Student ID'] || '').trim(), name: String(answers['Full name'] || '').trim(),
    claimed: BANK.CLAIMED_AREAS.map(a => answers['Self-rating: ' + a[0]] || ''),
    selfReport: [], sections: {}, rows: [], genai: { score: 0, max: BANK.GENAI_IDS.length }, total: 0, max: 0,
  };
  SECTION_ORDER.forEach(s => { result.sections[s] = { score: 0, max: 0, title: BANK.SECTIONS[s].title }; });
  BANK.ITEMS.forEach(it => {
    if (it.section === 'E') {
      [['Best action', it.best, it.explain.best], ['Worst action', it.worst, it.explain.worst]].forEach(([label, key, explain]) => {
        const given = letterOf_(answers[it.id + ' \u00b7 ' + label]);
        const ok = given === key;
        tally_(result, it, ok);
        result.rows.push({ id: it.id, label: label, given: given, key: key, ok: ok, explain: explain, options: it.options });
      });
    } else {
      const given = letterOf_(answers[it.id + ' \u00b7 ' + it.fmt]);
      const ok = given === it.correct;
      tally_(result, it, ok);
      if (it.genai && ok) result.genai.score += 1;
      result.rows.push({ id: it.id, label: it.fmt, given: given, key: it.correct, ok: ok, explain: it.explain, options: it.options });
    }
  });
  const grid = answers['How you work'];
  result.selfReport = Array.isArray(grid) ? grid : BANK.SELF_REPORT.map(() => '');
  return result;
}

function tally_(result, it, ok) {
  result.sections[it.section].max += 1; result.max += 1;
  if (ok) { result.sections[it.section].score += 1; result.total += 1; }
}

function letterOf_(text) {
  if (!text) return '-';
  const m = String(text).match(/^(?:Option\s+)?([A-D])\b/);
  return m ? m[1] : '-';
}

// Profiles tab: same column order as the INTERNAL workbook's Entry tab from column C onward
function ensureProfilesSheet_(ss) {
  let sh = ss.getSheetByName('Profiles');
  if (sh) return sh;
  sh = ss.insertSheet('Profiles');
  const header = ['Timestamp', 'Email', 'Student ID', 'Name'].concat(BANK.CLAIMED_AREAS.map(a => 'Claimed: ' + a[0].split(' (')[0]));
  BANK.ITEMS.forEach(it => { if (it.section === 'E') header.push(it.id + ' best', it.id + ' worst'); else header.push(it.id); });
  BANK.SELF_REPORT.forEach((_, i) => header.push('R' + (i + 1)));
  header.push('A %', 'B %', 'C %', 'D %', 'E %', 'GenAI %', 'Total %', 'Attempt');
  sh.getRange(1, 1, 1, header.length).setValues([header]).setFontWeight('bold').setBackground('#EFE3CF');
  sh.setFrozenRows(1); sh.setFrozenColumns(4);
  return sh;
}

function appendProfileRow_(r) {
  const sheetId = PropertiesService.getScriptProperties().getProperty('SHEET_ID');
  const ss = SpreadsheetApp.openById(sheetId);
  const sh = ensureProfilesSheet_(ss);
  const row = [r.timestamp, r.email, r.studentId, r.name].concat(r.claimed);
  r.rows.forEach(x => row.push(x.given));
  r.selfReport.forEach(v => row.push(v));
  SECTION_ORDER.forEach(s => row.push(r.sections[s].max ? r.sections[s].score / r.sections[s].max : ''));
  row.push(r.genai.max ? r.genai.score / r.genai.max : '', r.max ? r.total / r.max : '');
  row.push(attemptLabel_(sh, r));
  sh.appendRow(row);
  const last = sh.getLastRow();
  sh.getRange(last, row.length - 7, 1, 7).setNumberFormat('0%');
}

// "First" for a new email or Student ID; "Repeat of row N" when either has been seen before, so the one-to-one uses the first sitting
function attemptLabel_(sh, r) {
  const last = sh.getLastRow();
  if (last < 2) return 'First';
  const seen = sh.getRange(2, 2, last - 1, 2).getValues();   // Email, Student ID
  for (let i = 0; i < seen.length; i++) {
    const em = String(seen[i][0]).trim().toLowerCase(), sid = String(seen[i][1]).trim().toLowerCase();
    if ((r.email && em === r.email) || (r.studentId && sid === r.studentId.toLowerCase())) return 'Repeat of row ' + (i + 2);
  }
  return 'First';
}

// ---------------------------------------------------------------------
// 4. Report email
// ---------------------------------------------------------------------
function sendReport_(r) {
  const pct = (a, b) => b ? Math.round(100 * a / b) + '%' : '';
  const bronze = '#B37A33', ink = '#1C1B16', hair = '#D5D0C4', ivory = '#F9F8F3', grey = '#6B675E';
  const td = 'padding:6px 8px;border-bottom:1px solid ' + hair + ';vertical-align:top;font-size:13px;';
  const th = td + 'background:#EFE3CF;font-weight:bold;';
  let h = '<div style="font-family:Arial,Helvetica,sans-serif;color:' + ink + ';max-width:760px;margin:0 auto;background:' + ivory + ';padding:24px">';
  h += '<div style="height:6px;background:' + bronze + '"></div>';
  h += '<h1 style="font-family:Georgia,serif;color:' + bronze + ';font-weight:normal;margin:16px 0 4px">Baseline Diagnostic: your report</h1>';
  h += '<p style="color:' + grey + ';margin:0 0 16px;font-size:13px">' + CONFIG.ORG + ' | ' + CONFIG.COHORT + ' | ' + CONFIG.WEEK + (r.studentId ? ' | ' + esc_(r.studentId) : '') + '</p>';
  h += '<p style="font-size:14px">This paper carries no marks. Your score is ' + r.total + ' of ' + r.max + ' (' + pct(r.total, r.max) + '). ' +
       'Read the section table against your own ratings first; that gap is what your one-to-one this week is about.</p>';

  h += '<table style="border-collapse:collapse;width:100%;margin:12px 0"><tr><th style="' + th + '">Area</th><th style="' + th + '">Your rating (1 to 4)</th><th style="' + th + '">Your score</th></tr>';
  const areaRows = [['Python', r.claimed[0], r.sections.A], ['SQL', r.claimed[1], r.sections.B], ['Numbers and reasoning', r.claimed[2], r.sections.C],
    ['Working an unfamiliar business problem', r.claimed[3], r.sections.D], ['Using LLM tools for work', r.claimed[4], r.genai], ['Judgment calls', '', r.sections.E]];
  areaRows.forEach(([lab, cl, sc]) => {
    h += '<tr><td style="' + td + '">' + lab + '</td><td style="' + td + '">' + esc_(String(cl)) + '</td><td style="' + td + '">' + sc.score + ' of ' + sc.max + ' (' + pct(sc.score, sc.max) + ')</td></tr>';
  });
  h += '</table>';

  h += '<h2 style="font-family:Georgia,serif;color:' + bronze + ';font-weight:normal;margin:20px 0 6px;font-size:18px">Every question, your answer, the right answer, and why</h2>';
  h += '<table style="border-collapse:collapse;width:100%"><tr><th style="' + th + '">Q</th><th style="' + th + '">Yours</th><th style="' + th + '">Answer</th><th style="' + th + '">Why</th></tr>';
  r.rows.forEach(x => {
    const mark = x.ok ? '<span style="color:#2E6B2E">&#10003;</span>' : '<span style="color:#9C2B1F">&#10007;</span>';
    const keyText = x.options.filter(o => o.letter === x.key)[0];
    h += '<tr><td style="' + td + 'white-space:nowrap">' + x.id + (x.label === 'Best action' || x.label === 'Worst action' ? ' ' + x.label.split(' ')[0].toLowerCase() : '') + '</td>' +
         '<td style="' + td + '">' + mark + ' ' + x.given + '</td>' +
         '<td style="' + td + '"><b>' + x.key + '</b>. ' + esc_(keyText ? keyText.text.replace(/\n/g, ' ') : '') + '</td>' +
         '<td style="' + td + '">' + esc_(x.explain) + '</td></tr>';
  });
  h += '</table>';
  h += '<p style="color:' + grey + ';font-size:12px;margin-top:18px">Your results plan this week\'s Python and SQL sessions and are discussed with you individually. Keep this email; the one-to-one starts from it.</p>';
  h += '</div>';

  const mail = { to: r.email, subject: 'Baseline Diagnostic: your report (' + r.total + ' of ' + r.max + ')', htmlBody: h, name: CONFIG.ORG };
  if (CONFIG.REPLY_TO) mail.replyTo = CONFIG.REPLY_TO;
  MailApp.sendEmail(mail);
}

function esc_(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

// ---------------------------------------------------------------------
// 5. Utilities
// ---------------------------------------------------------------------
// Emails the script owner a report built from the first stored response, to check the email design before the sitting
function sendSampleReportToMe() {
  const id = PropertiesService.getScriptProperties().getProperty('FORM_ID');
  const responses = FormApp.openById(id).getResponses();
  if (!responses.length) { Logger.log('No responses yet; submit one test response first.'); return; }
  const r = scoreResponse_(responses[responses.length - 1]);
  r.email = Session.getEffectiveUser().getEmail();
  sendReport_(r);
  Logger.log('Sample report sent to ' + r.email);
}

// Closes the form to new responses without unpublishing it
function closeDiagnostic() {
  const id = PropertiesService.getScriptProperties().getProperty('FORM_ID');
  FormApp.openById(id).setAcceptingResponses(false);
  Logger.log('Form closed.');
}

// Sanity check of the embedded bank: counts and key positions
function auditBank() {
  const single = BANK.ITEMS.filter(it => it.section !== 'E');
  const pos = { A: 0, B: 0, C: 0, D: 0 };
  single.forEach(it => { pos[it.correct] += 1; });
  Logger.log('Items: ' + BANK.ITEMS.length + ' (' + single.length + ' single-key, ' + (BANK.ITEMS.length - single.length) + ' best/worst). Key positions: ' + JSON.stringify(pos) + '. Max marks: ' + (single.length + 2 * (BANK.ITEMS.length - single.length)));
}
