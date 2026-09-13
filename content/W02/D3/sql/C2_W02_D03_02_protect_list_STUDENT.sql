-- The protect list, the falling flag and the plan line. No hints.
--
-- Marketing will act on this, so the note at the bottom matters as much as the queries. One of
-- the decisions below is a business decision and no amount of SQL will make it for you.

-- ---------------------------------------------------------------- 1. the protect list
-- The question: the top fifty customers by Q2 revenue in each segment.
-- The head of Retail-Plus said: "If two members spent the same, I want them ranked the same, and
-- I want to know how many made the top fifty, not forty-nine because of a tie."
-- Put that sentence in your comment. The next person will not have heard him say it.
-- __TODO1__


-- ---------------------------------------------------------------- 2. how many names shipped
-- The question: how many rows does your list actually contain, per segment?
-- If any segment is not exactly fifty, say why in the comment rather than fixing it.
-- __TODO2__


-- ---------------------------------------------------------------- 3. falling two months running
-- The question: which Retail-Plus members spent less in August than July, and less again in
-- September than August?
-- Decide before you write it what a member with only one month of data should do to the flag.
-- __TODO3__


-- ---------------------------------------------------------------- 4. the running total
-- The question: how does Q2 revenue accumulate week by week against the plan line?
-- Give the window an order that cannot tie, or the cumulative column can differ between runs.
-- __TODO4__


-- ---------------------------------------------------------------- 5. the note
-- Four sentences in a comment block:
--   which tie rule you chose
--   the sentence from the head of Retail-Plus that decided it
--   how many names the Retail-Plus list contains
--   what you say to a flagged member who was on holiday in August
-- __TODO5__
