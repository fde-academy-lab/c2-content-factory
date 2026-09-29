# The second case: the director who wants to edit the source

Forty-five minutes, in pairs. One of you plays the director, the other defends the operating rule;
then you swap. The solution opens at the close of the session.

> "Retail-Plus will be back at five lakh next quarter; I have spoken to the team. Type five lakh into
> Q2 so the card stops frightening people, and fix the source later."
>
> A director, Kalpa Retail, in the room on Monday

Kavya's challenge from the morning is the brief: "Which parts belong in Excel, which must never be in
Excel, and how do you keep the two from drifting apart?"

---

## Part 1. The scene, played out, fifteen minutes

Open `notebooks/C2_W02_D05_ex2_hands_on_STUDENT.ipynb`. Four lettered `TODO` markers play the scene
on the tree: the edit, the check that catches it, the refresh that wipes it, and where the director's
assumption belongs. Each answer is the letter itself, as a string, and each step ends on checks.

## Part 2. The role play, twenty minutes

Ten minutes each way. The director pushes three times: "It is only one cell"; "Finance will never
see this deck"; "We will fix the source later." The defender says yes to the question and no to the
edit, in three lines: what they will show, why the actual stays, and the check that ties the sheet
back to the warehouse.

## Part 3. The operating rule, ten minutes

Six items, then the team's rule in three lines, one per tool, which is also tonight's recap.

Post exactly this shape, the letters in item order, no spaces: `xxxxxx`

### Q1. The director asks for five lakh in the Q2 cell. What do you say first?

a) No, since the sheet must match Finance's books exactly
b) Yes, I will type it in now and fix the source after the meeting
c) Yes: I will show five lakh as your scenario, beside the actual
d) Only if Finance signs off on the change in writing first

### Q2. Where does the director's five lakh go in the workbook?

a) Over the Q2 cell, with a comment saying who changed it
b) In the raw export, before the Tree tab reads it
c) In a separate copy of the workbook for the director
d) In a yellow input that feeds a labelled scenario line

### Q3. Which check shows the same day that a sheet has drifted from its source?

a) The sheet's Q2 total against the warehouse's Q2 total
b) The number of rows on the Tree tab against four segments
c) The card's sentence against the sentence sent last week
d) The file's saved date against the export's creation date

### Q4. Somebody typed over the Q2 cell anyway. What does Monday's refresh from a fresh export do?

a) Keeps the typed value, since Excel protects manual entries
b) Wipes it without a trace, and the reason for it with it
c) Writes the typed value back into the warehouse
d) Flags the cell in red so the owner can decide

### Q5. Which of the week's steps must never be done in Excel?

a) Removing the double-paid rows from the export
b) Slicing the tree by segment in front of the room
c) Looking up a member by id for a director
d) Showing the front-page number's trend

### Q6. Finance audits the front-page revenue number, and a director explores it in the room. Who owns it?

a) Excel, since the director uses it there
b) pandas, since an analyst rebuilds it weekly
c) The warehouse computes it; Excel presents it read-only
d) Whoever last refreshed the export on Monday morning before the review
