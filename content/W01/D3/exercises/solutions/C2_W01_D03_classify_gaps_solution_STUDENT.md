# Day 3 solution, E3. Classifying four gaps

| # | Answer | Reason |
|---|---|---|
| 1 | Drop the record, into rejects | `amount` is required and the value exists nowhere else, so the order cannot be computed on. It goes to the rejects file with its reason, never to the bin |
| 2 | Keep absent as absent | Absence carries meaning here, so filling it destroys information and gains nothing |
| 3 | Escalate before deciding | A known failed job means the values are recoverable from the source. Defaulting or dropping throws away six orders that somebody can simply re-run |
| 4 | Escalate before deciding | The largest order in the file with no status is a question for the order book owner, and any default you pick moves the biggest number in the dataset |

### The two that could be argued the other way

**Number 2.** Filling `discount` with zero is defensible if every downstream consumer treats zero and absent identically. Settle it by asking one question: does anything downstream distinguish an order with no discount from an order with a zero discount? If nothing does, the default is harmless. If anything does, it is not.

**Number 3.** Keep and flag is defensible if the re-run will take weeks and the analysis cannot wait. Settle it by asking when the job can be re-run. Anything inside your own deadline makes escalate the better answer.

Numbers 1 and 4 are not really arguable. A required field with no recoverable value is a rejection, and the largest record in the file is never a place to apply a silent default.
