#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update, in the voice of a lost sock, to /output/entry.txt.
The line is 112 characters, inside the 1-120 gate, with no trailing newline.
"""

import os

LINE = "Day 9 in the vacuum bag. 14 socks, 3 coins, and Gary. Gary arrived in 2019. Gary is the boss. I pay him in lint."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
