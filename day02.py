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
from utils import *
import re

DAY = 2


def download_input_data(day=1):
    global games
    advent.setup(2023, day, dry_run=False)
    fin = advent.get_input()
    games = list(map(parse_games, get_lines(fin.readlines())))


def parse_games(games):  # -> dict[tuple[int, int, int], int]:
    parsed_games = []
    print(games)
    for game in games:
        game_id, game_sets = games.split(":")
        game_sets = list(map(parse_set, game_sets.split(";")))
        parsed_games.append(game_sets)
    return parsed_games


def parse_set(game_set_str):
    game_set = {"red": 0, "green": 0, "blue": 0}
    game_set_str = game_set_str.strip().split(",")
    for colors in game_set_str:
        cout, color = colors.split()
        game_set[color] = int(cout)
    return game_set


INPUT_S_PART_01 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
EXPECTED_PART_01 = 8


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_01, EXPECTED_PART_01),
    ),
)
def test01(input_s: str, expected: int) -> None:
    assert solve_part01(input_s) == expected


cubes_max = {"red": 12, "green": 13, "blue": 14}


def solve_part01(games):
    if isinstance(games, str):
        games = list(map(parse_games, games.split("\n")))
    game_sum = 0
    game_id = 0
    for game in games:
        game_id += 1
        cube_over = False
        for game_sets in game:
            for game_set in game_sets:
                if (game_set["red"] > cubes_max["red"]) or (game_set["green"] > cubes_max["green"]) or (
                        game_set["blue"] > cubes_max["blue"]):
                    cube_over = True
                    break
        if not (cube_over):
            game_sum += game_id
    return game_sum


def part01():
    global games
    solution = solve_part01(games)
    print(solution)
    # advent.submit_answer(1, solution)


INPUT_S_PART_02 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
EXPECTED_PART_02 = 2286


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S_PART_02, EXPECTED_PART_02),
    ),
)
def test02(input_s: str, expected: int) -> None:
    assert (solve_part02(input_s) == expected)


def solve_part02(games):
    if isinstance(games, str):
        games = list(map(parse_games, games.split("\n")))
    game_sum = 0
    for game in games:
        game_cubes_max = {"red": 0, "green": 0, "blue": 0}
        cube_over = False
        for game_sets in game:
            for game_set in game_sets:
                if (game_set["red"] > game_cubes_max["red"]):
                    game_cubes_max["red"] = game_set["red"]
                if (game_set["green"] > game_cubes_max["green"]):
                    game_cubes_max["green"] = game_set["green"]
                if (game_set["blue"] > game_cubes_max["blue"]):
                    game_cubes_max["blue"] = game_set["blue"]

        game_sum += game_cubes_max["red"] * game_cubes_max["green"] * game_cubes_max["blue"]
    return game_sum


def part02():
    global games
    solution = solve_part02(games)
    print(solution)
    advent.submit_answer(2, solution)


if __name__ == "__main__":
    download_input_data(DAY)
    timer_start()
    part01()
    part02()
