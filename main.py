"""One-Line Office Joke Laugh-Off entry.

Writes the single joke line to /output/entry.txt.
"""

import os

LINE = (
    "I won the office raffle: a free lunch with the CEO, "
    "redeemable during my unpaid break."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
