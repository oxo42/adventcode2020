#!/usr/bin/env python3

import logging
from common import read_ints
from typing import List, Tuple


def find_diffs(nums: List[int], src: int, j1: int, j3: int) -> Tuple[int, int]:
    logging.info("src: %s", src)
    if src + 1 in nums:
        return find_diffs(nums, src + 1, j1 + 1, j3)
    if src + 2 in nums:
        return find_diffs(nums, src + 2, j1, j3)
    if src + 3 in nums:
        return find_diffs(nums, src + 3, j1, j3 + 1)

    if src == max(nums):
        return (j1, j3 + 1)

    raise RuntimeError("Eh, whoops")


def main(input_file: str, dev: bool) -> None:
    nums = read_ints(input_file)
    logging.info(nums)
    j1, j3 = find_diffs(nums, 0, 0, 0)
    print(f"1 jolt: {j1}")
    print(f"3 jolt: {j3}")
    print(f"part 1: {j1*j3}")