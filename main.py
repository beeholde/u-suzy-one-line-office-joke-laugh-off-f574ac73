"""One-Line Office Joke Laugh-Off entry.

Writes the single joke line to /output/entry.txt.
"""

import os

LINE = "I took a sick day and got forty messages asking if I was okay; the forty-first assigned me work."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
