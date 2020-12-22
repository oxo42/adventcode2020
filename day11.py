#!/usr/bin/env python3

import logging
from copy import deepcopy
from typing import List

import common


def read_grid(fn: str) -> List[str]:
    with open(fn) as f:
        return [list(l.strip("\n")) for l in f.readlines()]


class Grid:
    grid: List[List[str]]

    def __init__(self, grid: List[List[str]]) -> None:
        self.grid = grid

    def occupied(self, row: int, col: int) -> int:
        # before first row or column
        if row < 0 or col < 0:
            return 0
        # after last row or column
        if row >= len(self.grid) or col >= len(self.grid[0]):
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
            logging.debug(
                "previous: %s, current: %s", previous_occupied, current_occupied
            )
            new_grid: List[List[str]] = self.clone_grid()
            for row, _ in enumerate(self.grid):
                for col, _ in enumerate(self.grid[row]):
                    if self.grid[row][col] == ".":
                        continue
                    if self.occupied(row, col) == 0 and self.adjacent(row, col) == 0:
                        new_grid[row][col] = "#"
                    if self.occupied(row, col) == 1 and self.adjacent(row, col) >= 4:
                        new_grid[row][col] = "L"
            self.grid = new_grid
            current_occupied = self.total_occupied()

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.grid])


def main(input_file: str, dev: bool) -> None:
    grid = Grid(read_grid(input_file))
    grid.run_to_stable()
    print(grid)
    print(f"Occupied {grid.total_occupied()}")
