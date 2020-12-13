#!/usr/bin/env python3

from typing import List
from itertools import permutations
from functools import reduce


def get_input() -> List[str]:
    with open("day1_input.txt") as f:
        lines = f.readlines()
        return [int(x) for x in lines]


def get_product(total: int, num_items: int) -> int:
    nums = get_input()
    for items in permutations(nums, num_items):
        if sum(items) == total:
            return reduce((lambda x, y: x * y), items)


def main():
    print(get_product(2020, 3))


if __name__ == "__main__":
    main()
