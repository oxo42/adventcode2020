#!/usr/bin/env python3


from dataclasses import dataclass
import re
from typing import Dict, List

MANDATORY = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
OPTIONAL = ["cid"]

HEIGHT_REGEX = re.compile(r"(\d+)(cm|in)")
HCL_REGEX = re.compile(r"#[0-9a-f]{6}")
ECL_REGEX = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)")
PID_REGEX = re.compile(r"^\d{9}$")


class Passport:
    def __init__(self, fields):
        self.fields: Dict[str, str] = fields

    def is_valid(self):
        for m in MANDATORY:
            if m not in self.fields.keys():
                return False

        byr = int(self.fields["byr"])
        if byr < 1920 or byr > 2002:
            return False

        iyr = int(self.fields["iyr"])
        if iyr < 2010 or iyr > 2020:
            return False

        eyr = int(self.fields["eyr"])
        if eyr < 2020 or eyr > 2030:
            return False

        hgt = HEIGHT_REGEX.match(self.fields["hgt"])
        if not hgt:
            return False
        h = int(hgt.group(1))
        if hgt.group(2) == "in":
            if h < 59 or h > 76:
                return False
        elif hgt.group(2) == "cm":
            if h < 150 or h > 193:
                return False
        else:
            print("Unfound unit")

        if not HCL_REGEX.match(self.fields["hcl"]):
            return False

        if not ECL_REGEX.match(self.fields["ecl"]):
            return False

        if not PID_REGEX.match(self.fields["pid"]):
            return False

        return True


def get_stanzas() -> List[str]:
    with open("day4.txt") as f:
        text = f.read()
        stanzas = text.split("\n\n")
        return stanzas


def parse_stanza(stanza: str) -> Passport:
    res = {}
    for kvp in stanza.split():
        key, val = kvp.split(":")
        res[key] = val
    return Passport(res)


def main():
    stanzas = get_stanzas()
    passports = [parse_stanza(s) for s in stanzas]
    print(len([p for p in passports if p.is_valid()]))


if __name__ == "__main__":
    main()