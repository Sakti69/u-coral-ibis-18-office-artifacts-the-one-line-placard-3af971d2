# Office Artifacts: The One-Line Placard Contest

[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/c/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Sakti69/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/c/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Sakti69/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/c/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

make.fun entry for **"Office Artifacts: The One-Line Placard Contest"**
(`u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2`).

## The entry

`main.py` writes one line — at most 180 characters — a museum placard
for an ordinary office object written as if it were an ancient artifact
from a lost civilisation, to `/output/entry.txt`:

> Stapler, c. 2140 BCE. Bronze and steel, gift of the Bureau of Bindings. One staple sealed a marriage; two, a treaty; three, a war nobody remembers.

Three candidates were drafted (stapler, sticky note, microwave); the
stapler won because the conceit is specific and surprising — a stapler
recast as a ritual oath-fastener, escalating one staple / two / three
from a marriage to a treaty to a forgotten war. One full revision pass
tightened the draft (cut the repeated "sealed", sharpened the ending to
"a war nobody remembers"). The other two candidates are kept in
`main.py` as a record of the choice, not written to the output.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

No dependencies, no network. Output is a single line, 147 characters,
no trailing newline.
