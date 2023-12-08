#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day 06: Wait For It ---
   https://adventofcode.com/2023/day/8
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import functools
from math import lcm

import pytest
import advent
from support import support
from utils import *
from support import *
from collections import Counter
from enum import Enum

DAY = 8


class MapNode:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}: ({}, {})".format(self.name, self.left, self.right)

    def __str__(self):
        return "{}: ({}, {})".format(self.name, self.left, self.right)

    def next_node(self, pos):
        if pos == "L":
            return self.left
        elif pos == "R":
            return self.right
        else:
            return NotImplemented


def download_input_data(day=1):
    global instruction
    global nodes
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    instruction, nodes_list = fin.read().split("\n\n")
    nodes = parse_nodes(nodes_list.split("\n"))


def parse_nodes(nodes_list):
    nodes_list = list(map(parse_node, nodes_list))
    nodes = {}
    for node in nodes_list:
        nodes[node.name] = node
    return nodes


def parse_node(node):
    name, instructions = node.split(" = ")
    instructions = instructions[1:-1]
    left, right = instructions.split(", ")
    return MapNode(name, left, right)


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

CARD_VALUE = {'1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              'T': 10,
              'J': 11,
              'Q': 12,
              'K': 13,
              'A': 14
              }

START_NODE = "AAA"
END_NODE = "ZZZ"


def solve_part01(instruction, nodes):
    steps = 0
    instruction_pos = 0
    node = nodes[START_NODE]
    while node.name != END_NODE:
        ins = instruction[instruction_pos]
        instruction_pos += 1
        instruction_pos = instruction_pos % len(instruction)
        #print(str(steps) + " " + str(node) + " next " + ins)
        node = nodes[node.next_node(ins)]
        steps += 1
    return steps


def part01():
    global instruction
    global nodes
    solution = solve_part01(instruction, nodes)
    print(solution)
    # advent.submit_answer(1, solution)


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


def solve_part02(instruction, nodes):
    step_list = []
    actual_nodes = [nodes[key] for key in list(nodes.keys()) if key.endswith('A')]
    for node in actual_nodes:
        instruction_pos = 0
        steps = 0
        while not(node.name.endswith("Z")):
            ins = instruction[instruction_pos]
            instruction_pos += 1
            instruction_pos = instruction_pos % len(instruction)
            node = nodes[node.next_node(ins)]
            steps += 1
        step_list.append(steps)

    return lcm(*step_list)


def part02():
    global instruction
    global nodes
    solution = solve_part02(instruction, nodes)
    print(solution)
    # advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start()
    part01()
    part02()
