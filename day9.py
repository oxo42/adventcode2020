#!/usr/bin/env python3
from typing import List, Tuple
from itertools import permutations


def read_file() -> List[int]:
    with open("day9.txt") as f:
        return [int(l) for l in f.readlines()]


def first_invalid(nums: List[int], spread: int) -> Tuple[int, List[int]]:
    for i in range(spread, len(nums)):
        interesting = nums[i - spread : i]
        sums = [sum(p) for p in permutations(interesting, 2)]
        if nums[i] not in sums:
            return (nums[i], interesting)


def main():
    nums = read_file()
    invalid, interesting = first_invalid(nums, 5)
    
    print(invalid)


if __name__ == "__main__":
    main()