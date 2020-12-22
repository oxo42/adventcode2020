#!/usr/bin/env python3

import logging
from copy import deepcopy
from typing import Callable, List, Tuple

import common


def read_grid(fn: str) -> List[str]:
    with open(fn) as f:
        return [list(l.strip("\n")) for l in f.readlines()]


class Grid:
    grid: List[List[str]]

    def __init__(self, grid: List[List[str]]) -> None:
        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.TOLERANCE = 4

    def occupied(self, row: int, col: int) -> int:
        # before first row or column
        if row < 0 or col < 0:
            return 0
        # after last row or column
        if row >= self.height or col >= self.width:
            return 0
        return 1 if self.grid[row][col] == "#" else 0

    def adjacent(self, row: int, col: int) -> int:
        adjacents = [
            # previous row
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            # this row
            (row, col - 1),
            (row, col + 1),
            # next row
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ]
        return sum([self.occupied(r, c) for r, c in adjacents])

    def total_occupied(self) -> int:
        count = 0
        for row, _ in enumerate(self.grid):
            for col, _ in enumerate(self.grid[row]):
                count += self.occupied(row, col)
        return count

    def clone_grid(self) -> List[List[str]]:
        return deepcopy(self.grid)

    def run_to_stable(self) -> int:
        # returns total occupied seats
        previous_occupied = self.total_occupied()
        current_occupied = -1
        while previous_occupied != current_occupied:
            previous_occupied = current_occupied
            new_grid: List[List[str]] = self.clone_grid()
            for row, _ in enumerate(self.grid):
                for col, _ in enumerate(self.grid[row]):
                    if self.grid[row][col] == ".":
                        continue
                    if self.occupied(row, col) == 0 and self.adjacent(row, col) == 0:
                        new_grid[row][col] = "#"
                    if (
                        self.occupied(row, col) == 1
                        and self.adjacent(row, col) >= self.TOLERANCE
                    ):
                        new_grid[row][col] = "L"
            self.grid = new_grid
            current_occupied = self.total_occupied()

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.grid])


class Grid2(Grid):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.TOLERANCE = 5

    def is_direction_occupied(
        self, rowcol: Tuple[int, int], delta: Callable[[int, int], Tuple[int, int]]
    ) -> True:
        row, col = rowcol
        in_bounds = row >= 0 and row < self.height and col >= 0 and col < self.width
        if not in_bounds:
            return 0
        seat = self.grid[row][col]
        if seat == "#":
            return 1
        if seat == "L":
            return 0
        return self.is_direction_occupied(delta(row, col), delta)

    def adjacent(self, row: int, col: int) -> int:
        permutations = [
            lambda row, col: (row - 1, col),  # Up
            lambda row, col: (row + 1, col),  # Down
            lambda row, col: (row, col - 1),  # Left
            lambda row, col: (row, col + 1),  # Right
            lambda row, col: (row - 1, col - 1),  # Up-Left
            lambda row, col: (row - 1, col + 1),  # Up-Right
            lambda row, col: (row + 1, col - 1),  # Down-Left
            lambda row, col: (row + 1, col + 1),  # Down-Right
        ]
        count = 0

        for delta in permutations:
            c = self.is_direction_occupied(delta(row, col), delta)
            count += c

        return count


def main(input_file: str, dev: bool) -> None:
    grid = Grid(read_grid(input_file))
    grid.run_to_stable()
    print("\n\nGrid 1")
    print(grid)
    print(f"Occupied {grid.total_occupied()}")

    print("=" * 80)

    grid2 = Grid2(read_grid(input_file))
    grid2.run_to_stable()
    print("\n\nGrid 2")
    print(grid2)
    print(f"Occupied {grid2.total_occupied()}")
