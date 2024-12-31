from pathlib import Path
from functools import cache
import math


def part1(data):
    return simulate(data, 25)


def part2(data):
    return simulate(data, 75)


def simulate(data, iterations):
    return sum(count_values(stone, iterations) for stone in data)


@cache
def count_values(stone, iterations):
    if iterations == 0:
        return 1

    if stone == 0:
        return count_values(1, iterations - 1)

    digits = math.floor(math.log10(stone)) + 1
    if digits % 2 == 0:
        half_digits = digits // 2
        left, right = divmod(stone, 10**half_digits)
        return count_values(left, iterations - 1) + count_values(right, iterations - 1)

    return count_values(stone * 2024, iterations - 1)


def parse_data(input_file):
    return [int(val_str) for val_str in input_file.read().strip().split()]


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day11.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
