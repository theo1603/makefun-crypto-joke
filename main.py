"""Laugh Track entry: one original line about crypto trading life.

Writes the joke to /output/entry.txt (no trailing newline, so the file
holds exactly the joke: 1-200 characters, UTF-8).
"""

from pathlib import Path

JOKE = (
    "I bought the top, sold the bottom, and the only thing "
    "that went up was the gas fee."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
