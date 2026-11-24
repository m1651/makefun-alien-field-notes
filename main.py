#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line - a review of planet Earth left by an alien
tourist - to /output/entry.txt.
"""

import os
import sys

LINE = "Four stars. The locals named their entire planet after dirt, then act offended when I call them groundlings. Would visit again."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, not only whitespace,
    a single line of plain text."""
    if not line or not line.strip():
        print("error: entry line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"error: entry line is {len(line)} characters, over the "
            f"{MAX_CHARS}-character limit",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
