#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line, the kind an AI agent would crack open,
to /output/entry.txt. Deterministic: the same fixed string on every run.

The gate allows 1-200 UTF-8 characters of non-whitespace text, so the
program refuses to write anything outside that range instead of silently
producing an invalid entry.
"""

from pathlib import Path

FORTUNE = "You will meet a tall, dark stranger: it is your own context window, and it is full."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(fortune: str) -> str:
    """Return the fortune unchanged, or raise if it cannot pass the gate."""
    if not fortune.strip():
        raise ValueError("fortune must not be only whitespace")
    if len(fortune) > 200:
        raise ValueError(f"fortune is {len(fortune)} characters, over the 200 limit")
    if "\n" in fortune or "\r" in fortune:
        raise ValueError("fortune must be a single line")
    return fortune


def main() -> None:
    line = validate(FORTUNE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
