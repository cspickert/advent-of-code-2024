import re
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path


def part1(data):
    data = deepcopy(data)
    return sum(find_min_cost(game) for game in data)


def part2(data):
    data = deepcopy(data)
    adjust_games(data)
    return sum(find_min_cost(game) for game in data)


def adjust_games(data):
    adjustment = 10000000000000
    for game in data:
        game.prize = (game.prize[0] + adjustment, game.prize[1] + adjustment)


def find_min_cost(game):
    # Had to look up some very stong hints for this implementation 😬 (it's been
    # too long since I studied linear algebra)
    b_presses, b_remainder = divmod(
        game.button_a[1] * game.prize[0] - game.button_a[0] * game.prize[1],
        game.button_a[1] * game.button_b[0] - game.button_a[0] * game.button_b[1],
    )
    a_presses, a_remainder = divmod(
        game.prize[0] - b_presses * game.button_b[0], game.button_a[0]
    )
    if a_remainder or b_remainder:
        return 0
    return a_presses * 3 + b_presses


@dataclass
class Game:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_data(input_file):
    return [parse_game(chunk) for chunk in input_file.read().split("\n\n")]


def parse_game(chunk):
    match = re.match(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
        chunk,
    )
    return Game(
        button_a=(int(match.group(1)), int(match.group(2))),
        button_b=(int(match.group(3)), int(match.group(4))),
        prize=(int(match.group(5)), int(match.group(6))),
    )


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day13.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
