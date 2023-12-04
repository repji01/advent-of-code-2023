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

DAY = 4


def download_input_data(day=1):
    global tickets
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    tickets = list(map(parse_tickets, get_lines(fin.readlines())))

def parse_tickets(tickets):  # -> dict[tuple[int, int, int], int]:
    ticket_id, ticket = tickets.split(":")
    winning_numbers, ticket_numbers = ticket.split(" | ")
    winning_numbers = [int(number.strip()) for number in winning_numbers.strip().replace("  ", " ").split(" ")]
    ticket_numbers = [int(number.strip()) for number in ticket_numbers.strip().replace("  ", " ").split(" ")]
    return (ticket_id,winning_numbers, ticket_numbers, 0)



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
def solve_part01(tickets):
    points = 0
    if isinstance(tickets, str):
        tickets = map(parse_tickets, tickets.split("\n"))
    for ticket in tickets:

        _, winning_numbers, ticket_numbers, _ = ticket
        winning_numbers = Counter(winning_numbers)
        ticket_numbers = Counter(ticket_numbers)
        win_power = len(winning_numbers & ticket_numbers)
        if (win_power>0):
            points += pow(2, win_power-1)
    return points

def part01():
    global tickets
    solution = solve_part01(tickets)
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




def solve_part02(tickets):


    if isinstance(tickets, str):
        tickets = list(map(parse_tickets, tickets.split("\n")))
    points = 0
    for idx in range(len(tickets)):
        ticket = tickets[idx]
        _, winning_numbers, ticket_numbers, orig_counter = ticket
        winning_numbers = Counter(winning_numbers)
        ticket_numbers = Counter(ticket_numbers)
        win_power = len(winning_numbers & ticket_numbers)
        if win_power>0:
            for duplicate in range(1, win_power+1):
                ticket = tickets[idx+duplicate]
                id, winning_numbers, ticket_numbers, counter = ticket
                counter += orig_counter+1
                tickets[idx + duplicate] = (id, winning_numbers, ticket_numbers, counter)
    for ticket in tickets:
        _, _, _, counter = ticket
        points += counter
    points += len(tickets)
    return points

def part02():
    global tickets
    solution = solve_part02(tickets)
    advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start()
    part01()
    part02()
