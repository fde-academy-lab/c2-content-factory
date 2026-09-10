# Day 2 solution, E3. The truncated feed

## The idea being tested

A CSV loses one row when it truncates. A JSON file loses everything, because the format has no record boundary a parser can stop at safely. Fifteen items on that difference, on reading the message the parser gives you, and on what you say back to whoever sent the file.

The message this file produces is `Expecting ',' delimiter: line 48 column 1 (char 1027)`, and the file itself is 47 lines. That gap is the whole diagnosis: the parser is telling you it ran out of file while it was still inside a record.

## The answers

**Answers: 1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | `json.load` refuses the document and names where it gave up. | The 46 complete records describe how a CSV behaves. `FileNotFoundError` names a path problem, and the path was fine. An empty list is what a silent failure would give, and JSON never fails silently. |
| 2 | b | Line 48 does not exist, which is the parser saying it wanted more and the file ended. | Calling the message wrong is the reflex worth breaking; the message is precise. A blank line 48 would be present in the file, and it is not. The column is the least useful of the three numbers here. |
| 3 | c | The document parses wholly or not at all, so nothing is available. | 46 assumes a row-by-row format. 3 counts the records the fragment opened, which is a different question and a useful one. Saying it depends on the parser suggests a tolerant parser exists that would be safe to use, and one that guesses at a truncated record is worse than one that refuses. |
| 4 | d | A newline ends a CSV row, so every complete row above the break is still a complete row. | File size has nothing to do with it. No CSV parser repairs a row. Saying there is no difference is the belief the item exists to correct. |
| 5 | a | Everything else you might do depends on knowing what is actually at that line. | Asking the vendor first means you never learn what they got wrong. A tolerant parser treats a truthful error as a tool problem. Rewriting by hand puts your guess into their data. |
| 6 | b | The last line is a field inside a nested object, with no closing brace, no closing bracket and no comma. | A valid record with a missing bracket would end on a closing brace. The date is fine. Blaming a different system is a guess with nothing behind it. |
| 7 | c | Run it, read it, open the named line, count what the fragment held, then send the vendor the exact message. | Every other ordering either sends the message before you know what it means, or opens the file before you know which line to open. |
| 8 | d | Three `"order_id"` keys in the raw text, counted without parsing anything. | Dividing lines by a lines-per-record figure assumes every record is the same height, and the truncated one is not. No parser offers a partial result. A spreadsheet cannot open JSON. |
| 9 | a | Record 3 stops mid-object and the closing bracket never arrives, which is exactly the file you have. | Removing the opening bracket would fail at line 1. Removing record 2 leaves a valid document. Swapping braces for brackets is a different malformation entirely. |
| 10 | b | The file, the parser's own wording, and the fact that nothing in it was usable. That is the row a reviewer needs. | Nothing at all loses the fact that a delivery arrived and failed. A line per record invents records you never read. The last line alone is evidence with no claim attached. |
| 11 | c | It names the line, the failure and what it costs, and it is short enough to act on. | Broken and please fix it gives them nothing to look at. Could not open reads as your problem rather than theirs. Asking for a different format changes the contract to avoid the bug. |
| 12 | d | Catching the exception stops your notebook falling over. It does not hand you any records, because none were produced. | Both True options assume a partial result exists. The other False option is right about the outcome and wrong about the mechanism, since a caught exception does not raise again. |
| 13 | a | 483 lines across 30 records is about 16 lines each, and the truncated fragment's 47 lines match three records. | 6, 30 and 48 are all inconsistent with a fragment that opened three records in 47 lines. |
| 14 | b | The CSV pass is unchanged at 30 in, 28 clean and 2 rejected. The feed contributed nothing, so it changes no count. | Saying both files are fine ignores the failure. 33 in counts records that were never read. 47 in counts lines as records. |
| 15 | c | A byte count or a checksum agreed in advance is the only one of these that fires before your code runs. | Scrolling an editor is what you do after it fails. A longer timeout addresses a cause you have not established. Reading twice catches a flaky download and not a file the vendor truncated at source. |

## The part worth arguing about

Item 3 against item 8. Nothing in the file is usable, and yet you can say it opened three records. A room usually feels those two facts contradict each other, and they do not: counting `"order_id"` in the raw text is reading the file as text, and parsing it is reading it as JSON. Knowing which one you are doing is the skill.

Item 15 is the other. Somebody will argue for the tolerant parser again. The reply is that a parser which guesses at a truncated record produces data nobody can distinguish from real data, which is the failure mode this whole week is built to prevent.

## The hands-on picks

The running half is `notebooks/C2_W01_D02_ex2_hands_on_STUDENT.ipynb`, and its four markers are:

**Answers: 1b 2c 3a 4d**

The executed twin is `C2_W01_D02_ex2_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

Public Health England, October 2020, dropped 15,841 COVID cases because a CSV-to-XLS conversion hit an old row limit and nothing checked the count on the far side. That failure is item 14's: a pass that reported a clean number while the input had quietly shrunk.

The interview question is item 5's, and it arrives as "the vendor's JSON fails at line 47 column 5, what is your first move?" Say you open the file at that line, and say why: the message is a fact about their file rather than a complaint about your parser.
