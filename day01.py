#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day 01: Trebuchet?! ---
   https://adventofcode.com/2023/day/1
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import pytest
import advent
from utils import *
import re

DAY = 1



def download_input_data(day=1):
    global fin
    global lines
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())


INPUT_S_PART_01 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
EXPECTED_PART_01 = 142


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_01, EXPECTED_PART_01),
    ),
)
def test01(input_s: str, expected: int) -> None:
    assert solve_part01(input_s) == expected


def only_numbers_simple(line):
    return re.findall(r'\d', line)


def solve_part01(lines):
    if isinstance(lines, str):
        lines = lines.split()
    numbers_sum = 0
    for line in lines:
        numbers = only_numbers_simple(line)
        numbers_sum += int("" + numbers[0] + numbers[-1])
    return numbers_sum


def part01():
    global lines
    solution = solve_part01(lines)
    advent.submit_answer(1, solution)


INPUT_S_PART_02 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
EXPECTED_PART_02 = 281


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_02, EXPECTED_PART_02),
    ),
)
def test02(input_s: str, expected: int) -> None:
    assert (solve_part02(input_s) == expected)


numberdict = {"one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9}


def only_numbers_extended(line):
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    for key in numberdict.keys():
        if key in numbers:
            numbers = list(map(lambda x: x.replace(key, str(numberdict[key])), numbers))
    return numbers


def solve_part02(lines):
    if isinstance(lines, str):
        lines = lines.split()
    numbers_sum = 0
    for line in lines:
        numbers = only_numbers_extended(line)
        number = int("" + numbers[0] + numbers[-1])
        numbers_sum += number
    return numbers_sum


def part02():
    global lines
    solution = solve_part02(lines)
    advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start(1)
    part01()
    part02()
