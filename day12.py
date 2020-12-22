#!/usr/bin/env python3

import logging
from typing import List
from dataclasses import dataclass


@dataclass
class Move:
    action: str
    value: int


def get_moves(fn: str) -> List[Move]:
    moves = []
    with open(fn) as f:
        for line in f.readlines():
            moves.append(Move(action=line[0], value=int(line[1:])))
    return moves


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 90  # east

    def normalised_direction(self, value: int) -> str:
        d = value % 360
        if d < 0:
            d = 360 - d
        return d

    def forward(self, value: int) -> None:
        compass = {0: "N", 90: "E", 180: "S", 270: "W"}[
            self.normalised_direction(self.direction)
        ]
        self.move(Move(compass, value))

    def move(self, m: Move) -> None:
        if m.action == "N":
            self.y -= m.value
        if m.action == "S":
            self.y += m.value
        if m.action == "E":
            self.x += m.value
        if m.action == "W":
            self.x -= m.value
        if m.action == "F":
            self.forward(m.value)
        if m.action == "R":
            self.direction += m.value
        if m.action == "L":
            self.direction -= m.value

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return f"At ({self.x}, {self.y}) facing {self.direction}, manhattan distance {self.manhattan_distance}"


class Ship2(Ship):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wp_x = 10
        self.wp_y = -1

    def rotate(self, value: int) -> None:
        d = self.normalised_direction(value)
        if d == 180:
            self.wp_x = -self.wp_x
            self.wp_y = -self.wp_y
        if d == 90:
            y = self.wp_x
            x = -self.wp_y
            self.wp_x = x
            self.wp_y = y
        if d == 270:
            y = -self.wp_x
            x = self.wp_y
            self.wp_x = x
            self.wp_y = y

    def forward(self, value: int) -> None:
        for _ in range(value):
            self.x += self.wp_x
            self.y += self.wp_y

    def move(self, m: Move) -> None:
        if m.action == "N":
            self.wp_y -= m.value
        if m.action == "S":
            self.wp_y += m.value
        if m.action == "E":
            self.wp_x += m.value
        if m.action == "W":
            self.wp_x -= m.value
        if m.action == "F":
            self.forward(m.value)
        if m.action == "R":
            self.rotate(m.value)
        if m.action == "L":
            self.rotate(-m.value)

    def __str__(self):
        return f"At ({self.x}, {self.y}) wp ({self.wp_x}, {self.wp_y}) manhattan distance {self.manhattan_distance}"


def main(input_file: str, dev: bool) -> None:
    ship = Ship()
    moves = get_moves(input_file)
    for m in moves:
        ship.move(m)

    print(ship)

    print("=" * 80)
    ship2 = Ship2()
    for m in moves:
        ship2.move(m)
        logging.debug("%s: %s", m, ship2)

    print(ship2)