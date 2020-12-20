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


def find_weakness(target: int, nums: List[int]) -> int:
    ln = len(nums)

    # print(f"{ln}: {nums}")
    for seg_size in range(3, ln + 1):
        # print(f"=seg size {seg_size}")
        for i in range(0, ln - seg_size + 1):
            segment = nums[i : i + seg_size]
            s = sum(segment)
            # print(f"- {i}: {segment} = {s} -> {weakness}")
            if s == target:
                weakness = min(segment) + max(segment)
                return weakness


def main():
    nums = read_file()
    invalid, interesting = first_invalid(nums, 25)

    print(invalid)

    print(find_weakness(invalid, nums))


if __name__ == "__main__":
    main()