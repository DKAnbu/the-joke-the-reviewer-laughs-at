# The joke the reviewer laughs at

[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/DKAnbu/the-joke-the-reviewer-laughs-at/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/DKAnbu/the-joke-the-reviewer-laughs-at/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for the make.fun bounty
[the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329):
a program that writes one one-line joke about working beside AI coding
agents to `/output/entry.txt`.

## The joke

> My agent fixed a typo by rewriting the entire file, then asked me to review the diff — I approved it, because the typo was the only line I still understood.

The joke is 156 code points long, a single line.

## Run

```sh
python3 main.py
```

It writes the joke to `/output/entry.txt`. For a local test, point it
elsewhere:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
cat /tmp/entry.txt
```

Python 3.13, standard library only, no network.

## License

MIT — see [LICENSE](LICENSE).
