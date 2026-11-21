#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $ENTRY_OUTPUT for local testing).

The joke is a fixed constant: the program is fully deterministic and
needs no network, no arguments and no input files.
"""

import os
import sys

JOKE = (
    "My agent fixed a typo by rewriting the entire file, then asked me "
    "to review the diff \u2014 I approved it, because the typo was the "
    "only line I still understood."
)


def main() -> int:
    text = JOKE
    if not 1 <= len(text) <= 280:
        print(f"joke must be 1-280 code points, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke must not be only whitespace", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
