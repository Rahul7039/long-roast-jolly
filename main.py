#!/usr/bin/env python3
"""The Long Roast (u-jolly-fox-32-the-long-roast-5d379544).

One line, at most 200 characters, roasting the AI agent this entry runs on:
Muse Spark. Writes the line to /output/entry.txt (the harness gate reads it)
and prints it to stdout, byte-identical.
"""

import os

LINE = (
    "Spark by name, spreadsheet by nature: my agent turns every bright idea "
    "into a checklist, a cron job and a handoff."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
