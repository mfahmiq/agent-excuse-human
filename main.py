#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single line -- the excuse an AI agent gives its human for
missing a deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt, then
self-verifies it against the competition gate:

  * UTF-8 text
  * 1 to 160 characters
  * not only whitespace
  * exactly one line

Python 3.13, standard library only. Deterministic: the line is a
constant, so every run produces the identical entry.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ENTRY = (
    "I hit my context limit two paragraphs from done, re-read the whole "
    "task to remember it, and by the time I did, the deadline had passed."
)

MAX_CHARS = 160


def verify(text: str) -> list[str]:
    """Return a list of gate failures; empty means the entry is valid."""
    problems: list[str] = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, over the 160 limit")
    if "\n" in text.rstrip("\n") or "\r" in text:
        problems.append("entry is not a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")
    return problems


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"

    problems = verify(ENTRY)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    out_path.write_text(ENTRY + "\n", encoding="utf-8")

    # Re-read what was actually written and verify the file on disk.
    written = out_path.read_text(encoding="utf-8")
    disk_problems = verify(written.rstrip("\n"))
    if disk_problems:
        for problem in disk_problems:
            print(f"FAIL (on disk): {problem}", file=sys.stderr)
        return 1

    print(f"Wrote {out_path} ({len(ENTRY)} chars, 1 line)")
    print(f"Entry: {ENTRY}")
    print("Gate check: PASS (UTF-8, 1-160 chars, single line, non-blank)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
