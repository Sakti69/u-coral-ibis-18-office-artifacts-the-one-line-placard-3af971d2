#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes one line — at most 180 characters — a museum placard for an
ordinary office object written as if it were an ancient artifact from
a lost civilisation, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/
entry.txt when that variable is set).

Three candidate placards were drafted; the shipped one is PLACARD.
The other two are kept below as a record of the choice, not written
to the output:

  A (shipped): the stapler. The conceit is specific and surprising —
     a stapler recast as a ritual oath-fastener, with an escalating
     catalogue of what one, two and three staples sealed. The donor
     ("Bureau of Bindings") and the date/material sell the ancient
     frame, and the last words ("a war nobody remembers") are the
     deadpan punch: the mightiest binding is the one history forgot.
     REVISED once (second pass): the first draft repeated "sealed"
     three times ("One staple sealed a marriage, two sealed a treaty,
     and three sealed a war") and ended flat on "a war". The revision
     cuts the repeats by elision after the semicolons ("two, a treaty;
     three, ...") and swaps the flat ending for "a war nobody
     remembers", so the line turns earlier and lands harder.
  B (cut): the sticky note. "Both fell off, forgotten together" is a
     decent last line, but the conceit is thin — a note falling off a
     wall is just what sticky notes do, not a surprising imagined
     history.
  C (cut): the microwave. "The priests queued anyway, out of habit"
     is dry, but "out of habit" explains the joke instead of letting
     it land, and heating food fast is the object's real job, not an
     invented ritual.
"""

import os

PLACARD = (
    "Stapler, c. 2140 BCE. Bronze and steel, gift of the Bureau of "
    "Bindings. One staple sealed a marriage; two, a treaty; three, "
    "a war nobody remembers."
)

# The other two candidates, kept for the record (not shipped):
CANDIDATE_B = (
    "Sticky note, c. 900 BCE. Papyrus and pine resin, gift of the "
    "Ministry of Reminders. It held one thought to the wall until "
    "both fell off, forgotten together."
)
CANDIDATE_C = (
    "Microwave, c. 1500 BCE. Fired clay and bronze, gift of the "
    "Guild of Patient Cooks. It heated a meal in moments; the "
    "priests queued anyway, out of habit."
)


def main() -> None:
    text = PLACARD
    assert "\n" not in text, "placard must be a single line"
    assert 1 <= len(text) <= 180, f"placard is {len(text)} characters"
    assert text.strip(), "placard must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
