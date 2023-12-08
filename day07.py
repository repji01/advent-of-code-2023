#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2023 --- Day 06: Wait For It ---
   https://adventofcode.com/2023/day/7
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import functools

import pytest
import advent
from support import support
from utils import *
from support import *
from collections import Counter
from enum import Enum

DAY = 7


def download_input_data(day=1):
    global games
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    games = list(map(parse_games, get_lines(fin.readlines())))



def parse_games(game):
    hand, bit = game.split(" ")
    return hand, parse_hand(hand), int(bit)


class HandTypes(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

def parse_hand(hand):
    hand_combination = []
    for card in set(hand):
        card_count = hand.count(card)
        if (card_count == 5):
            hand_combination.append(HandTypes.FIVE_OF_A_KIND)
            break
        elif (card_count == 4):
            hand_combination.append(HandTypes.FOUR_OF_A_KIND)
            break
        elif (card_count == 3):
            hand_combination.append(HandTypes.THREE_OF_A_KIND)
        elif (card_count == 2):
            hand_combination.append(HandTypes.ONE_PAIR)
        else:
            hand_combination.append(HandTypes.HIGH_CARD)
    if len(hand_combination) > 0:
        if HandTypes.THREE_OF_A_KIND in hand_combination and HandTypes.ONE_PAIR in hand_combination:
            hand_combination = HandTypes.FULL_HOUSE
        elif HandTypes.THREE_OF_A_KIND in hand_combination and not (HandTypes.ONE_PAIR in hand_combination):
            hand_combination = HandTypes.THREE_OF_A_KIND
        elif hand_combination.count(HandTypes.ONE_PAIR)>1:
            hand_combination = HandTypes.TWO_PAIR
        elif HandTypes.ONE_PAIR in hand_combination:
            hand_combination = HandTypes.ONE_PAIR
        else:
            hand_combination = HandTypes.HIGH_CARD
    else:
        hand_combination = hand_combination[0]
    return hand_combination



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

CARD_VALUE = {'1':1,
              '2':2,
              '3':3,
              '4':4,
              '5':5,
              '6':6,
              '7':7,
              '8':8,
              '9':9,
              'T':10,
              'J':11,
              'Q':12,
              'K':13,
              'A':14
              }

def card_compare(cards, other_cards):
    for x in range(5):
        card =cards[x]
        other_card = other_cards[x]
        if CARD_VALUE[card] < CARD_VALUE[other_card]:
            return -1
        elif CARD_VALUE[card] > CARD_VALUE[other_card]:
            return 1
    return 0

def game_compare(game, other_game):
    hand, combination, _ = game
    other_hand, other_combination, _ = other_game
    if combination < other_combination:
        return -1
    elif combination > other_combination:
        return 1
    else:
        return card_compare(hand, other_hand)

def solve_part01(games):
    out = 0
    games = sorted(games, key=functools.cmp_to_key(game_compare))
    for idx,game in enumerate(games):
        _, _, bit = game
        out+= bit*(idx+1)
    return out


def part01():
    global games
    solution = solve_part01(games)
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
    # part02()
