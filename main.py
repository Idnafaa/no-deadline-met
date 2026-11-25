#!/usr/bin/env python3
"""One Line, No Deadline Met — deadline-excuse writer.

Prints one original single-line joke excusing a missed deadline and
saves it to /output/entry.txt for the make.fun judge.
"""

import os

LINE = "I didn't miss the deadline, I just kept hitting remind me later until it stopped asking."

OUT_PATH = "/output/entry.txt"


def build_line():
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    return line


def main():
    line = build_line()
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote %d characters to %s" % (len(line), OUT_PATH))


if __name__ == "__main__":
    main()
