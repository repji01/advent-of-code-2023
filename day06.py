#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day 06: Wait For It ---
   https://adventofcode.com/2023/day/4
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import pytest
import advent
from support import support
from utils import *
from support import *
from collections import Counter

DAY = 6


def download_input_data(day=1):
    global race_input
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    race_input = fin.read().split("\n")




def parse_input_part1(split):
    race_input = []
    for line in split:
        while "  " in line:
            line = line.replace("  ", " ")
        race_input.append([ int(part) for part in line.split(" ")[1:]])
    return race_input

def parse_input_part2(split):
    race_input = []
    for line in split:
        while "  " in line:
            line = line.replace("  ", " ")
        race_input.append(int("".join(line.split(" ")[1:]).replace(" ", "")))
    return race_input

INPUT_S_PART_01 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
EXPECTED_PART_01 = 8

"""
@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_01, EXPECTED_PART_01),
    ),
)
def test01(input_s: str, expected: int) -> None:
    assert solve_part01(input_s) == expected
"""

def boat_race(time, record_dst):
    win = 0
    boat_speed = -1
    for x in range(time + 1):
        boat_speed += 1
        final_dst = boat_speed * (time - x)
        #print("time {}: boat speed: {} {}".format(x, boat_speed, final_dst))
        if final_dst > record_dst:
            win += 1
    return win
def solve_part01(input):
    race_input = parse_input_part1(input)
    race_input = list(zip(race_input[0], race_input[1]))
    out = 1
    for race in race_input:
        win = boat_race(race[0], race[1])
            #print("time {}: boat speed: {} {}".format(x, boat_speed, final_dst))
        if win>1:
            out *= win
        #print(time, record_dst)
    return out

def part01():
    global race_input
    solution = solve_part01((race_input))
    #print(solution)
    advent.submit_answer(1, solution)


INPUT_S_PART_02 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
EXPECTED_PART_02 = 2286

"""
@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_02, EXPECTED_PART_02),
    ),
)
def test02(input_s: str, expected: int) -> None:
    assert (solve_part02(input_s) == expected)
"""




def solve_part02(input):
    out = 1
    race_input = parse_input_part2(input)
    win = boat_race(race_input[0], race_input[1])
    if win > 1:
        out *= win
    return out


def part02():
    global race_input
    solution = solve_part02(race_input)
    advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start()
    part01()
    part02()
