#!/usr/bin/env python3

import logging
from common import read_ints
from typing import List, Tuple
import functools


def find_diffs(nums: List[int], src: int, j1: int, j3: int) -> Tuple[int, int]:
    logging.debug("src: %s", src)
    if src + 1 in nums:
        return find_diffs(nums, src + 1, j1 + 1, j3)
    if src + 2 in nums:
        return find_diffs(nums, src + 2, j1, j3)
    if src + 3 in nums:
        return find_diffs(nums, src + 3, j1, j3 + 1)

    if src == max(nums):
        return (j1, j3 + 1)

    raise RuntimeError("Eh, whoops")


nums: List[int] = []


@functools.lru_cache(maxsize=None)
def count_arrangements(
    src: int,
) -> int:
    logging.debug("src: %s", src)
    logging.debug("nums %s", nums)
    if src == max(nums):
        return 1
    x = 0
    if src + 1 in nums:
        x += count_arrangements(src + 1)
    if src + 2 in nums:
        x += count_arrangements(src + 2)
    if src + 3 in nums:
        x += count_arrangements(src + 3)

    return x


def main(input_file: str, dev: bool) -> None:
    nums.extend(read_ints(input_file))
    logging.debug(nums)
    j1, j3 = find_diffs(nums, 0, 0, 0)
    print(f"1 jolt: {j1}")
    print(f"3 jolt: {j3}")
    print(f"part 1: {j1*j3}")
    arrangements = count_arrangements(0)
    print(f"part 2: {arrangements}")
