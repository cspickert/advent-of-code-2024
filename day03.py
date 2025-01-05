import re
from pathlib import Path


def part1(data):
    result = 0
    for item in data:
        match item:
            case ("mul", a, b):
                result += a * b
    return result


def part2(data):
    do = True
    result = 0
    for item in data:
        match item:
            case ("do",):
                do = True
            case ("don't",):
                do = False
            case ("mul", a, b):
                if do:
                    result += a * b
    return result


def parse_data(input_file):
    matches = re.findall(
        r"(mul|do|don't)\((?:((\d{1,3}),(\d{1,3}))?)\)", input_file.read()
    )
    data = []
    for ins, _, lhs, rhs in matches:
        if ins == "mul":
            data.append((ins, int(lhs), int(rhs)))
        else:
            data.append((ins,))
    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day03.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
