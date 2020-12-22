#!/usr/bin/env python3

import click
import time
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
    log_level = logging.DEBUG if dev else logging.INFO
    logging.basicConfig(level=log_level)
    logging.info("Day %s, dev mode %s", day, dev)
    mod = import_module(f"day{day}")
    start = time.perf_counter()
    mod.main(input_file(day, dev), dev)
    end = time.perf_counter()
    logging.info("Elapsed: %s", (start - end))


if __name__ == "__main__":
    run()
