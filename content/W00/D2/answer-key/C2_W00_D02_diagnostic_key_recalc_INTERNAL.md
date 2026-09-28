# Recalculation manifest: the diagnostic's key and profile workbook

INTERNAL. This drives `scripts/xlsx_recalc.py`, which makes LibreOffice recompute the requester's
workbook and then enters one answer sheet to prove the profile and the brush-up call follow it.

The workbook ships empty, so as shipped every profile reads Pending and the dashboard counts no one.
The first flip types one complete answer sheet into the Entry tab for S01: self-ratings of 3, 3, 2,
2 and 1, five of the twelve Python items right, every other item right and every statement at 3. The
profile then reads 42 percent on Python, which is below the Dashboard's Python cut of 50 percent, so
the call is a full brush-up, and the learner under-claims on average. The second flip enters the same
sheet with the Python cut moved to 40 percent, and the call turns light.

```yaml
workbook: C2_W00_D02_diagnostic_key_INTERNAL.xlsx
verdicts:
  - {sheet: Dashboard, cell: B6, expect: "0"}
  - {sheet: Dashboard, cell: C15, expect: "0.5"}
  - {sheet: Profile, cell: D7, expect: "Pending"}
flips:
  - name: one answer sheet is entered, with five of twelve on Python
    set:
      - {sheet: Entry, cell: C7, value: "3"}
      - {sheet: Entry, cell: D7, value: "3"}
      - {sheet: Entry, cell: E7, value: "2"}
      - {sheet: Entry, cell: F7, value: "2"}
      - {sheet: Entry, cell: G7, value: "1"}
      - {sheet: Entry, cell: H7, value: "C"}
      - {sheet: Entry, cell: I7, value: "B"}
      - {sheet: Entry, cell: J7, value: "D"}
      - {sheet: Entry, cell: K7, value: "A"}
      - {sheet: Entry, cell: L7, value: "B"}
      - {sheet: Entry, cell: M7, value: "A"}
      - {sheet: Entry, cell: N7, value: "B"}
      - {sheet: Entry, cell: O7, value: "A"}
      - {sheet: Entry, cell: P7, value: "B"}
      - {sheet: Entry, cell: Q7, value: "A"}
      - {sheet: Entry, cell: R7, value: "A"}
      - {sheet: Entry, cell: S7, value: "A"}
      - {sheet: Entry, cell: T7, value: "B"}
      - {sheet: Entry, cell: U7, value: "A"}
      - {sheet: Entry, cell: V7, value: "D"}
      - {sheet: Entry, cell: W7, value: "C"}
      - {sheet: Entry, cell: X7, value: "A"}
      - {sheet: Entry, cell: Y7, value: "B"}
      - {sheet: Entry, cell: Z7, value: "D"}
      - {sheet: Entry, cell: AA7, value: "C"}
      - {sheet: Entry, cell: AB7, value: "D"}
      - {sheet: Entry, cell: AC7, value: "A"}
      - {sheet: Entry, cell: AD7, value: "B"}
      - {sheet: Entry, cell: AE7, value: "C"}
      - {sheet: Entry, cell: AF7, value: "A"}
      - {sheet: Entry, cell: AG7, value: "D"}
      - {sheet: Entry, cell: AH7, value: "B"}
      - {sheet: Entry, cell: AI7, value: "C"}
      - {sheet: Entry, cell: AJ7, value: "A"}
      - {sheet: Entry, cell: AK7, value: "C"}
      - {sheet: Entry, cell: AL7, value: "B"}
      - {sheet: Entry, cell: AM7, value: "D"}
      - {sheet: Entry, cell: AN7, value: "A"}
      - {sheet: Entry, cell: AO7, value: "B"}
      - {sheet: Entry, cell: AP7, value: "C"}
      - {sheet: Entry, cell: AQ7, value: "A"}
      - {sheet: Entry, cell: AR7, value: "B"}
      - {sheet: Entry, cell: AS7, value: "D"}
      - {sheet: Entry, cell: AT7, value: "D"}
      - {sheet: Entry, cell: AU7, value: "B"}
      - {sheet: Entry, cell: AV7, value: "A"}
      - {sheet: Entry, cell: AW7, value: "C"}
      - {sheet: Entry, cell: AX7, value: "C"}
      - {sheet: Entry, cell: AY7, value: "D"}
      - {sheet: Entry, cell: AZ7, value: "B"}
      - {sheet: Entry, cell: BA7, value: "A"}
      - {sheet: Entry, cell: BB7, value: "3"}
      - {sheet: Entry, cell: BC7, value: "3"}
      - {sheet: Entry, cell: BD7, value: "3"}
      - {sheet: Entry, cell: BE7, value: "3"}
      - {sheet: Entry, cell: BF7, value: "3"}
      - {sheet: Entry, cell: BG7, value: "3"}
      - {sheet: Entry, cell: BH7, value: "3"}
      - {sheet: Entry, cell: BI7, value: "3"}
      - {sheet: Entry, cell: BJ7, value: "3"}
      - {sheet: Entry, cell: BK7, value: "3"}
    verdicts:
      - {sheet: Entry, cell: BL7, expect: "Yes"}
      - {sheet: Profile, cell: Y7, expect: "Full"}
      - {sheet: Profile, cell: Z7, expect: "Light"}
      - {sheet: Profile, cell: AA7, expect: "Under-claims"}
      - {sheet: Dashboard, cell: B6, expect: "1"}
      - {sheet: Dashboard, cell: F6, expect: "1"}
  - name: the same sheet with the Python cut lowered to 40 percent
    set:
      - {sheet: Entry, cell: C7, value: "3"}
      - {sheet: Entry, cell: D7, value: "3"}
      - {sheet: Entry, cell: E7, value: "2"}
      - {sheet: Entry, cell: F7, value: "2"}
      - {sheet: Entry, cell: G7, value: "1"}
      - {sheet: Entry, cell: H7, value: "C"}
      - {sheet: Entry, cell: I7, value: "B"}
      - {sheet: Entry, cell: J7, value: "D"}
      - {sheet: Entry, cell: K7, value: "A"}
      - {sheet: Entry, cell: L7, value: "B"}
      - {sheet: Entry, cell: M7, value: "A"}
      - {sheet: Entry, cell: N7, value: "B"}
      - {sheet: Entry, cell: O7, value: "A"}
      - {sheet: Entry, cell: P7, value: "B"}
      - {sheet: Entry, cell: Q7, value: "A"}
      - {sheet: Entry, cell: R7, value: "A"}
      - {sheet: Entry, cell: S7, value: "A"}
      - {sheet: Entry, cell: T7, value: "B"}
      - {sheet: Entry, cell: U7, value: "A"}
      - {sheet: Entry, cell: V7, value: "D"}
      - {sheet: Entry, cell: W7, value: "C"}
      - {sheet: Entry, cell: X7, value: "A"}
      - {sheet: Entry, cell: Y7, value: "B"}
      - {sheet: Entry, cell: Z7, value: "D"}
      - {sheet: Entry, cell: AA7, value: "C"}
      - {sheet: Entry, cell: AB7, value: "D"}
      - {sheet: Entry, cell: AC7, value: "A"}
      - {sheet: Entry, cell: AD7, value: "B"}
      - {sheet: Entry, cell: AE7, value: "C"}
      - {sheet: Entry, cell: AF7, value: "A"}
      - {sheet: Entry, cell: AG7, value: "D"}
      - {sheet: Entry, cell: AH7, value: "B"}
      - {sheet: Entry, cell: AI7, value: "C"}
      - {sheet: Entry, cell: AJ7, value: "A"}
      - {sheet: Entry, cell: AK7, value: "C"}
      - {sheet: Entry, cell: AL7, value: "B"}
      - {sheet: Entry, cell: AM7, value: "D"}
      - {sheet: Entry, cell: AN7, value: "A"}
      - {sheet: Entry, cell: AO7, value: "B"}
      - {sheet: Entry, cell: AP7, value: "C"}
      - {sheet: Entry, cell: AQ7, value: "A"}
      - {sheet: Entry, cell: AR7, value: "B"}
      - {sheet: Entry, cell: AS7, value: "D"}
      - {sheet: Entry, cell: AT7, value: "D"}
      - {sheet: Entry, cell: AU7, value: "B"}
      - {sheet: Entry, cell: AV7, value: "A"}
      - {sheet: Entry, cell: AW7, value: "C"}
      - {sheet: Entry, cell: AX7, value: "C"}
      - {sheet: Entry, cell: AY7, value: "D"}
      - {sheet: Entry, cell: AZ7, value: "B"}
      - {sheet: Entry, cell: BA7, value: "A"}
      - {sheet: Entry, cell: BB7, value: "3"}
      - {sheet: Entry, cell: BC7, value: "3"}
      - {sheet: Entry, cell: BD7, value: "3"}
      - {sheet: Entry, cell: BE7, value: "3"}
      - {sheet: Entry, cell: BF7, value: "3"}
      - {sheet: Entry, cell: BG7, value: "3"}
      - {sheet: Entry, cell: BH7, value: "3"}
      - {sheet: Entry, cell: BI7, value: "3"}
      - {sheet: Entry, cell: BJ7, value: "3"}
      - {sheet: Entry, cell: BK7, value: "3"}
      - {sheet: Dashboard, cell: C15, value: 0.4}
    verdicts:
      - {sheet: Profile, cell: Y7, expect: "Light"}
      - {sheet: Dashboard, cell: F6, expect: "0"}
```
