#!/usr/bin/env python3

from typing import List
from operator import attrgetter


class Seat:
    def __init__(self, line: str) -> None:
        self.line = line

    @property
    def row(self) -> int:
        b = self.line[0:7].replace("F", "0").replace("B", "1")
        return int(b, 2)

    @property
    def col(self) -> int:
        b = self.line[7:10].replace("L", "0").replace("R", "1")
        return int(b, 2)

    @property
    def seat(self) -> int:
        return self.row * 8 + self.col

    def __str__(self):
        return f"row {self.row} col {self.col} seat {self.seat}"


def get_seats() -> List[Seat]:
    seats = []
    with open("day5.txt") as f:
        for line in f.readlines():
            seats.append(Seat(line))
    return seats


def main():
    seats = get_seats()
    high_seat = max(seats, key=attrgetter("seat"))
    print(high_seat)

    seat_ids = sorted([s.seat for s in seats])
    for index, seat_id in enumerate(seat_ids):
        if seat_ids[index + 1] != seat_id + 1:
            print(f"My seat is {seat_id + 1}")
            break


if __name__ == "__main__":
    main()