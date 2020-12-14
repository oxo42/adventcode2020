#!/usr/bin/env python3

from dataclasses import dataclass

import re
from typing import List

LINE_REGEX = re.compile(r"(\d+)-(\d+) (\S): (\S+)")


@dataclass
class PasswordEntry:
    lower: int
    upper: int
    character: str
    password: str

    @property
    def valid(self) -> bool:
        count = self.password.count(self.character)
        return count >= self.lower and count <= self.upper

    @staticmethod
    def from_line(line: str) -> "PasswordEntry":
        m = LINE_REGEX.match(line)
        return PasswordEntry(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))


def get_entries() -> List[PasswordEntry]:
    res = []
    with open("day2.txt") as f:
        lines = f.readlines()
        for line in lines:
            res.append(PasswordEntry.from_line(line))

    return res


def main():
    entries = get_entries()
    print(len([e for e in entries if e.valid]))


if __name__ == "__main__":
    main()