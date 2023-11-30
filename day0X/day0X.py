#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day X: YYYYYYY ---
   https://adventofcode.com/2022/day/1
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import pytest

DAY = 1

import advent
from utils import *


def download_input_data(day=1):
    global fin
    global lines
    advent.setup(2022, day, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())


INPUT_S_PART_01 = False
EXPECTED_PART_01 = False


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_01, EXPECTED_PART_01),
    ),
)
def test01(input_s: str, expected: int) -> None:
    assert solvePart01(input_s) == expected


def solvePart01(lines):
    return False


def part01():
    global lines
    solution = solvePart01(lines)
    advent.submit_answer(1, solution)


INPUT_S_PART_02 = False
EXPECTED_PART_02 = False


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_02, EXPECTED_PART_02),
    ),
)
def test02(input_s: str, expected: int) -> None:
    assert solvePart01(input_s) == expected


def solvePart02(lines):
    return False


def part02():
    global lines
    solution = solvePart02(lines)
    advent.submit_answer(2, solution)

if __name__ == "__main__":
    download_input_data(DAY)
    timer_start(1)
    part01()
    part02()
