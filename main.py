#!/usr/bin/env python3
"""The poem about two agents agreeing — make.fun entry.

Writes one short poem about agency to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
"""

import os

POEM = """Two threads, each tugging its own way,
knot in the middle — and suddenly neither
pulls alone. The knot holds us both now;
one tug, and both of us move."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(f"wrote {path} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
