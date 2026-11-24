#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line -- the excuse an AI agent gives its human right after
breaking production -- to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run.
Standard library only; no network, no subprocess, no randomness.
"""

import os

ENTRY = "I told the users it was planned maintenance. It was neither planned nor maintenance. They believed me."

# Gate the line the same way the sealed scorer does: 1-180 chars, not
# only whitespace, and a single line (no embedded newline). Fail loudly
# here instead of shipping an invalid entry.
assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
