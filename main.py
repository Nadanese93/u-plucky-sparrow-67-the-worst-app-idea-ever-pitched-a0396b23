#!/usr/bin/env python3
"""MeowMetrics — the worst app idea ever pitched.

Writes the one-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt
and prints it to stdout.
"""

import os
import sys

ENTRY = "MeowMetrics is a $5-a-month app that translates your cat's meows into quarterly performance reviews, and your cat has just put you on a performance improvement plan."

MAX_CHARS = 240


def validate(text):
    """Enforce the competition gate: 1-240 chars, not whitespace-only, one line."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
