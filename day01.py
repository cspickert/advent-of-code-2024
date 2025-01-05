from collections import Counter
from pathlib import Path


def part1(data):
    left, right = data
    left = sorted(left)
    right = sorted(right)
    return sum(abs(a - b) for a, b in zip(left, right))


def part2(data):
    left, right = data
    right_count = Counter(right)
    return sum(a * right_count[a] for a in left)


def parse_data(input_file):
    left, right = [], []
    for line in input_file.readlines():
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    return (left, right)


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day01.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
