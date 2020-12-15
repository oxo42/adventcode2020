#!/usr/bin/env python3

from typing import List
from functools import reduce


def read_file() -> List[str]:
    rec = []
    with open("day3.txt") as f:
        for line in f.readlines():
            rec.append(line.strip("\n"))
    return rec


def trees_hit(right_move: int, down_move: int) -> int:
    # memoize or pass in
    grid = read_file()
    row = 0
    col = 0
    moves_made = 0
    trees = 0
    height = len(grid)
    width = len(grid[0])
    while row < height - 1:
        moves_made += 1
        row += down_move
        col += right_move
        if col >= width:
            col = col % width
        tile = grid[row][col]
        if tile == "#":
            trees += 1
    return trees


def main():
    res = [
        trees_hit(1, 1),
        trees_hit(3, 1),
        trees_hit(5, 1),
        trees_hit(7, 1),
        trees_hit(1, 2),
    ]

    prod = reduce((lambda x, y: x * y), res)
    print(prod)


if __name__ == "__main__":
    main()