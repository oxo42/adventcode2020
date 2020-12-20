#!/usr/bin/env python3

from typing import List


def read_ints(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(l) for l in f.readlines()]