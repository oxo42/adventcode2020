#!/usr/bin/env python3

from typing import List, Tuple, Set, Dict
from dataclasses import dataclass
import re


@dataclass
class BagRule:
    color: str
    contains: List[Tuple[int, str]]

    @property
    def contains_colors(self) -> List[str]:
        return [color for _count, color in self.contains]

    @property
    def contains_len(self) -> int:
        return len(self.contains)


RULE1 = re.compile(r"^([a-z ]+) bags contain (.*)")
ITEMS_RULE = re.compile(r"(\d+) ([a-z ]+) bag")


def parse_rule(line: str) -> BagRule:
    m1 = RULE1.match(line)
    color = m1.group(1)
    items = m1.group(2)
    contains = ITEMS_RULE.findall(items)
    return BagRule(color, contains)


def get_rules() -> Dict[str, BagRule]:
    rules = {}
    with open("day7.txt") as f:
        for line in f.readlines():
            bag = parse_rule(line)
            rules[bag.color] = bag
    return rules


def find_colors(rules: List[BagRule], accumulator: Set[str], color: str) -> None:
    possible_containing_colors = [r.color for r in rules if color in r.contains_colors]
    for p in possible_containing_colors:
        if p not in accumulator:
            accumulator.add(p)
            find_colors(rules, accumulator, p)

    return accumulator


def bags_required(rules: Dict[str, BagRule], color: str) -> int:
    rule = rules[color]
    if rule.contains_len == 0:  # The last bag counts as 1
        return 1

    accum = []
    for sub_count, sub_color in rule.contains:
        sub_count = int(sub_count)
        req = bags_required(rules, sub_color)
        accum.append(sub_count * req)

    return sum(accum) + 1


def main():
    rules = get_rules()
    colors = set()
    find_colors(rules.values(), colors, "shiny gold")
    print(len(colors))

    print(bags_required(rules, "shiny gold") - 1)


if __name__ == "__main__":
    main()