#!/usr/bin/env python3

import click
import logging
from importlib import import_module


def input_file(day: str, dev: bool) -> str:
    if dev:
        return f"day{day}_sample.txt"
    return f"day{day}.txt"


@click.command()
@click.argument("day")
@click.option("-d", "--dev", is_flag=True, default=False)
def run(day: str, dev: bool) -> None:
    log_level = logging.INFO if dev else logging.WARNING
    logging.basicConfig(level=log_level)
    logging.info("Day %s, dev mode %s", day, dev)
    mod = import_module(f"day{day}")
    mod.main(input_file(day, dev), dev)


if __name__ == "__main__":
    run()
