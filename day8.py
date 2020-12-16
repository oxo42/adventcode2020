#!/usr/bin/env python3
from typing import List

from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Instruction:
    line_no: int
    op: str
    arg: int


def read_program() -> List[Instruction]:
    program = []
    with open("day8.txt") as f:
        for line_no, line in enumerate(f.readlines()):
            parts = line.split()
            arg = int(parts[1])
            program.append(Instruction(line_no + 1, parts[0], arg))
    return program


class Runtime:
    def __init__(self, program: List[Instruction]) -> None:
        self.program = program
        self.accumulator = 0
        self.seen_lines = set()
        self.pointer = 0
        self.looped = False

    @property
    def instruction(self) -> Instruction:
        return self.program[self.pointer]

    @property
    def line_no(self) -> str:
        return self.instruction.line_no

    @property
    def op(self) -> str:
        return self.program[self.pointer].op

    @property
    def arg(self) -> str:
        return self.program[self.pointer].arg

    def run(self) -> None:
        while True:
            if self.pointer >= len(self.program):
                print("terminated")
                self.looped = False
                return
            # print(f"{self.pointer:03}: {self.instruction}")
            if self.line_no in self.seen_lines:
                # print(f"Loop detected on line {self.line_no}")
                self.looped = True
                return
            self.seen_lines.add(self.line_no)
            if self.op == "nop":
                self.pointer += 1
            elif self.op == "acc":
                self.accumulator += self.arg
                self.pointer += 1
            elif self.op == "jmp":
                self.pointer += self.arg


from copy import deepcopy


def main():
    program = read_program()
    for i in range(len(program)):
        copy = deepcopy(program)
        instruction = copy[i]
        if instruction.op == "acc":
            continue
        if instruction.op == "nop":
            instruction.op = "jmp"
        elif instruction.op == "jmp":
            instruction.op = "nop"

        runtime = Runtime(copy)

        runtime.run()
        if not runtime.looped:
            print(f"Complete on {i} with acc {runtime.accumulator}")
            break


if __name__ == "__main__":
    main()