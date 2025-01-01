import re
from dataclasses import dataclass
from functools import cache
from pathlib import Path


def part1(data):
    return sum(solution for game in data if (solution := find_min_cost(game)) < 10_000)


def part2(data):
    pass


def find_min_cost(game):
    @cache
    def find_solution(x=0, y=0, button_a=0, button_b=0):
        if button_a > 100:
            return 10_000
        if button_b > 100:
            return 10_000
        if (x, y) == game.prize:
            return 0
        press_a = 3 + find_solution(
            x + game.button_a[0], y + game.button_a[1], button_a + 1, button_b
        )
        press_b = 1 + find_solution(
            x + game.button_b[0], y + game.button_b[1], button_a, button_b + 1
        )
        return min(press_a, press_b)

    return find_solution()


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
