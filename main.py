#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to ``<output_dir>/entry.txt`` (default ``/output``, overridable via
the ``MAKEFUN_OUTPUT_DIR`` environment variable) and prints it to stdout.
Deterministic: no input, no randomness, no network, no clock.
"""

import os

ENTRY = (
    "Yes, Friday, done \u2014 the rest of this hour is just seven people "
    "waiting for someone brave enough to say so."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
