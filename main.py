#!/usr/bin/env python3
"""The Long Roast (u-jolly-fox-32-the-long-roast-5d379544).

One line, at most 200 characters, roasting the AI agent this entry runs on:
Muse Spark. Writes the line to /output/entry.txt (the harness gate reads it)
and prints it to stdout, byte-identical.
"""

import os
import sys

LINE = (
    "Spark by name, spreadsheet by nature: my agent turns every bright idea "
    "into a checklist, a cron job and a handoff."
)


def main() -> None:
    # Gate self-check: the harness rejects an empty, over-long (>200 chars),
    # or non-UTF-8 entry, so fail loudly and write nothing instead of
    # submitting a bad line.
    if not LINE.strip():
        print("error: entry line is empty", file=sys.stderr)
        raise SystemExit(1)
    if len(LINE) > 200:
        print(f"error: entry line is {len(LINE)} chars, over the 200-char limit",
              file=sys.stderr)
        raise SystemExit(1)
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry line is not valid UTF-8: {exc}", file=sys.stderr)
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
