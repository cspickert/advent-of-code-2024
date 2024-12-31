from pathlib import Path


def part1(data):
    return simulate(data, 25)


def part2(data):
    pass


def simulate(data, iterations):
    for _ in range(iterations):
        data = step(data)
    return len(data)


def step(data):
    return [changed for stone in data for changed in change(stone)]


def change(stone):
    stone_str = str(stone)
    digits = len(stone_str)
    if stone == 0:
        yield 1
    elif digits % 2 == 0:
        yield int(stone_str[: digits // 2])
        yield int(stone_str[digits // 2 :])
    else:
        yield stone * 2024


def parse_data(input_file):
    return [int(val_str) for val_str in input_file.read().strip().split()]


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day11.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
