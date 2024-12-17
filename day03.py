from pathlib import Path
import re


def part1(data):
    return sum(a * b for a, b in data)


def part2(data):
    pass


def parse_data(input_file):
    matches = re.findall(r"mul\(((\d{1,3}),(\d{1,3}))\)", input_file.read())
    data = []
    for _, lhs, rhs in matches:
        data.append((int(lhs), int(rhs)))
    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day03.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
