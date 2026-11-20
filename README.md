# News Image — 20 November 2026

[![News Image](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/tranquilnaturevista-code/news-image-20-nov/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/tranquilnaturevista-code/news-image-20-nov/reward.svg)](https://make.fun/bounty/news-image-20261120)

This entry is a single front page for Friday, 20 November 2026, built
as a classic broadsheet: one dominant story at the top, a row of
supporting headlines beneath it, and market numbers along the bottom.
The `main.py` script does the whole delivery job — it copies the
finished `entry.png` image, byte for byte, to `/output/entry.png`, so
the page that gets judged is exactly the page that was laid out, with
no re-rendering or recompression in between.

## Stories

- **A first for the three capitals:** Donald Trump, Xi Jinping and
  Vladimir Putin meet together for the first time in Shenzhen and sign
  a four-point declaration meant to bring the war in Ukraine to an end.
- **A verdict years in the making:** the International Court of Justice
  finds that Myanmar committed genocide against the Rohingya people.
- **A missile over Riyadh:** a Houthi missile strikes the PIF Tower,
  home of Saudi Arabia's sovereign wealth fund; nobody is reported hurt.
- **A split day for markets:** the S&P 500 falls 2% and the Nikkei
  drops 4.68%, while Anthropic's shares soar 17% on the first day of
  the company's record-breaking stock market debut.
- **Kyiv under fire again:** Russian missiles hit the bridges across
  the Dnipro overnight, leaving parts of the city without power
  or running water.

## How it works

Run `python3 main.py` and the script copies `entry.png` from this
folder into the output folder (the `MAKEFUN_OUTPUT_DIR` environment
variable, or `/output` when that is not set), creating the folder if
it does not exist yet.

## Verification

After copying, the script checks that the copy is exactly the same
size in bytes as the original and stops with an error if the two
sizes differ. Comparing the SHA-256 hash of the output against the
original gives the same guarantee: the two files should match
exactly.
