#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry (make.fun).

Writes a single one-line office joke to /output/entry.txt.

Pure Python standard library, no dependencies, fully deterministic:
the same joke is written on every run.
"""

import os

JOKE = "My boss says we're a family here, so I asked HR when the will reading is."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires UTF-8 text of 1 to 200 characters, not only
    # whitespace. The joke is one line, well inside that range.
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "joke out of the 1-200 character gate"
    assert "\n" not in line, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
