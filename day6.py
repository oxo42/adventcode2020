#!/usr/bin/env python3

from typing import List, Dict
from collections import defaultdict


def groups() -> List[str]:
    with open("day6.txt") as f:
        text = f.read()
        groups = text.split("\n\n")
        return groups


def num_questions(group: str) -> int:
    res = set()
    for c in group.replace("\n", ""):
        res.add(c)
    return len(res)


def num_all_yes(group: str) -> int:
    lines = len(group.split())
    res = defaultdict(int)
    for c in group.replace("\n", ""):
        res[c] += 1

    return len([k for k, v in res.items() if v == lines])


def main():
    total = sum(num_questions(g) for g in groups())
    print(f"Any yes {total}")

    allyes = sum(num_all_yes(g) for g in groups())
    print(f"all yes {allyes}")


if __name__ == "__main__":
    main()