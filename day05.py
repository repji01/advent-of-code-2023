#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day 04: Scratchcards ---
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

DAY = 5


def download_input_data(day=1):
    global seeds
    global maps
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    seeds, maps = parse_input(fin.read())

def parse_input(s):
    parts = s.split("\n\n")
    seeds = parse_seeds(parts[0])
    maps = {}
    for part in parts[1:]:
        part_lines = part.split("\n")
        map_name = parse_map_name(part_lines[0])
        maps[map_name] = parse_map(part_lines[1:])
    return seeds, maps

def parse_seeds(s:str):
    _, seed_str = s.split(":")
    return [int(seed) for seed in seed_str.strip().split(" ")]

def parse_map_name(s:str):
    return s.split(" ")[0].replace("-", "_")

def parse_map(lines):
    lst = []
    for line in lines:
        dest, source, length = line.split(" ")
        dest = int(dest)
        source = int(source)
        length = int(length)
        lst.append([(dest, dest + length - 1), (source, source + length - 1)])
    lst.sort(key=lambda a: a[0][0])
    return lst

def find_in_map(str, number):
    ms = maps.get(str)
    found = False
    out = number
    for map_part in ms:
        dst, src = map_part
        src_start, src_end = src
        dst_start, dst_end = dst
        if (number >= src_start) and (number<= src_end):
            diff = number - src_start
            out = dst_start + diff
            break
    return out






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
def solve_part01(input):
    points = 0
    seeds = input[0]
    maps = input[1]
    if isinstance(input, str):
        seeds, maps = map(parse_input, input)
    locations = []
    for seed in seeds:
        nbr = seed

        for map in maps:
            nbr = find_in_map(map, nbr)
            if "location" in map:
                locations.append(nbr)

    return min(locations)

def part01():
    global seeds
    global maps
    solution = solve_part01((seeds, maps))
    print(solution)
    #advent.submit_answer(1, solution)


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
    seeds = input[0]
    maps = input[1]
    if isinstance(input, str):
        seeds, maps = map(parse_input, input)
    loc_min = float('inf')
    for seed_idx in range(0, len(seeds), 2):
        start = seeds[seed_idx]
        end = seeds[seed_idx+1]
        print("("+str(start)+", "+str(end)+")")
        for seed in range(start, start+ end):

            nbr = seed
            for map in maps:
                nbr = find_in_map(map, nbr)
                if "location" in map:
                    if nbr < loc_min:
                        loc_min = nbr
                    #print(map + " " + str(seed) + "->" + str(nbr))
    return loc_min


def part02():
    global seeds
    global maps
    solution = solve_part02((seeds, maps))
    print(solution)
    #advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start()
    part01()
    part02()
