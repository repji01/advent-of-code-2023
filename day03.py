#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day 02: Cube Conundrum ---
   https://adventofcode.com/2023/day/2
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
import re

DAY = 3


def download_input_data(day=1):
    global matrix
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    matrix = get_char_matrix(fin.readlines())




INPUT_S_PART_01 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
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

cubes_max = {"red": 12, "green": 13, "blue": 14}

def expand_matrix(matrix):
    expanded_matrix = list()
    for x in range(len(matrix[0])+2):
        expanded_matrix.append(["."] * (len(matrix)+2))

    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            expanded_matrix[y+1][x+1] = matrix[y][x]
    return expanded_matrix

def solve_part01(matrix):
    matrix = expand_matrix(matrix)
    part_of_number = False
    safe_number = False
    number = ""
    sum = 0
    for y, row in enumerate(matrix):
        safe_number = False
        for x, char in enumerate(row):
            if char.isalnum():
                part_of_number = True
                number+=char
                for yy,xx in support.adjacent_8(y,x):
                        if not(matrix[yy][xx].isalnum()) and matrix[yy][xx] != ".":
                            safe_number = True
            elif part_of_number:
                part_of_number = False
                if safe_number:
                    sum += int(number)
                number = ""
                safe_number = False
    return sum



def part01():
    global matrix
    #dump_char_matrix(matrix)

    solution = solve_part01(matrix)
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

def read_matrix_number(matrix, y, x):
    matrix_line = matrix[y]
    x_start=x
    number = ""
    while(matrix_line[x_start].isalnum()):
        x_start += -1
    x_start+=1
    while (matrix_line[x_start].isalnum()):
        number +=  matrix_line[x_start]
        x_start += 1
    return int(number)


def solve_part02(matrix):
    #matrix = get_char_matrix(INPUT_S_PART_02.split("\n"))
    matrix = expand_matrix(matrix)
    sum = 0
    for y, row in enumerate(matrix):
        safe_number = False
        for x, char in enumerate(row):
            if char == "*":
                numbers = set()
                for yy,xx in support.adjacent_8(y,x):
                        if matrix[yy][xx].isalnum():
                            numbers.add(read_matrix_number(matrix, yy, xx))
                if len(numbers) == 2:
                    numbers = list(numbers)
                    sum += numbers[0]*numbers[1]
    return sum

def part02():
    global matrix
    solution = solve_part02(matrix)
    advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start()
    part01()
    part02()
