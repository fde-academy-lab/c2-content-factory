# Day 3 solution, E3. Classify the gaps

## The idea being tested

Four missingness cases at the top, then the row-level failures a column profile cannot see. The thread through all fifteen items is that none of these is a code decision. Every one of them is a business decision that code then carries out, and the difference between a good day and a bad one is whether the reason got written down beside the number.

## The answers

**Answers: 1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | Absence means no discount ran, which is a fact about the order. Keeping it absent and flagging it preserves that fact. | Filling with zero makes absent and zero indistinguishable for everybody downstream. Dropping 39 orders throws away most of the file to fix a field nobody required. The mean of eleven discounts says nothing about the 39 orders that had none. |
| 2 | b | An order with no amount cannot be summed, so it cannot enter a total, and the rejection carries its reason. | The segment mean invents money. Zero invents a free order. Keeping and flagging leaves an unusable value in the column somebody will sum tomorrow. |
| 3 | c | A date six weeks after its neighbours is a finding rather than a defect, and it is the second half of the duplicate pair. | Deleting and correcting both change data on a hunch. It parses perfectly, so rejecting it is wrong on the facts. |
| 4 | d | A customer places several orders, so repeats in `customer_id` are the shape you expect. | The other three treat an expected repeat as a defect, which is how real orders get deleted. |
| 5 | a | discount keeps its absence and is flagged, amount is rejected with a reason, and customer_id is expected. Escalation is left over. | The other three matchings all move one case to a treatment that changes data nobody asked to change. |
| 6 | b | A whole-record comparison finds only exact copies, and this pair differs on `order_date`. | A crashed dedupe would raise. No id is empty. A repeated header row is the companion file's problem, not this one's. |
| 7 | c | Only `order_id` alone groups the pair together, since every rule that includes `order_date` separates them. | Every field and the two multi-field rules all include something the pair differs on. |
| 8 | d | The rule is the decision and the number follows from it, which is why the rule belongs in the log. | Corrupt data would show as a parse failure. The function returns exactly what each rule asks for. The strictest rule finds nothing here, which is the worst of the four answers. |
| 9 | a | Whoever owns the order book knows whether the same order was entered twice or two orders reused an id. | You alone on a Wednesday is how a wrong deletion happens. The strictest rule is a way of avoiding the decision. The person who wrote the file may be a system. |
| 10 | b | It converts, and it has a customer, a date, a segment and a status like every other order, so it is real until somebody says otherwise. | Deleting and capping both change the business the file describes. Splitting it invents orders. |
| 11 | c | The mean is dragged far above every ordinary order, because it divides a total that one record dominates. | The mean does use every value, which is the problem rather than a defence. The median barely moves. Sorting changes nothing about the arithmetic. |
| 12 | d | The amount, its share of the total and the decision to keep it are the three facts a reader needs. | The other three either claim a change that did not happen, give a locator with no meaning, or say nothing at all. |
| 13 | a | `DictReader` takes its keys from line 1 and hands line 2 back as data, so a duplicated header arrives as a row whose every value is a field name. | Sorting, reader failure and transit corruption are all guesses that the file's own contents rule out. |
| 14 | b | A value equal to its own field's name is a one-line check that catches this and nothing else. | A row count, a parse check and an empty check all pass on this file, which is exactly why it survived. |
| 15 | c | The data plus the record of every decision taken on it. That is what makes the counts defensible. | The clean file alone and the clean file with rejects both leave the reasoning behind. The notebook is how you did it rather than what you produced. |

## The part worth arguing about

Item 1 against item 2. Both are absences and they get opposite treatment, which a room always wants a rule for. The rule is what the absence means: `discount` absent means no discount ran, and `amount` absent means the order cannot be summed. When you cannot say what an absence means, you have found the question to ask rather than the default to apply.

Item 9 is the other. Somebody always argues that escalating is slow and the answer is obvious. Ask them which of the two rows they would delete, and why, and watch the argument change shape.

## The hands-on picks

The running half is `notebooks/C2_W01_D03_ex1_hands_on_STUDENT.ipynb`, and its five markers are:

**Answers: 1b 2c 3d 4c 5c**

The executed twin is `C2_W01_D03_ex1_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

Every warehouse you will work in has a documented identity rule per table, and the documentation exists because somebody once deduped on the wrong key and deleted real orders. The rule is usually a business key rather than a technical one, which is why item 9's answer is the order book owner rather than the engineer.

The interview question is item 8's, and it arrives as "two records share an id and differ in one field, what do you do and who decides?" Say that you state the identity rule first, then say that the rule is a business decision and name who owns it.
