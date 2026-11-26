#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

A robot vacuum explains, in one line, why it missed a spot.
Pure Python standard library, fully deterministic: the same line
on every run. Writes the line to /output/entry.txt.
"""

import os
from pathlib import Path

EXCUSE = "I skipped that spot because the dust there unionized, and I don't cross picket lines."


def main() -> None:
    line = EXCUSE.strip()
    # The gate: UTF-8 text of 1 to 120 characters, not only white space,
    # a single line. Refuse to write anything that would fail it.
    assert line, "excuse must not be empty"
    assert "\n" not in line, "excuse must be a single line"
    assert len(line) <= 120, f"excuse is {len(line)} chars, over the 120 limit"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
