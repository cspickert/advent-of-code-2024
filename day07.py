from functools import partial
from pathlib import Path


def part1(data):
    is_valid = partial(find_solution, ["+", "*"])
    return sum(item[0] for item in data if is_valid(item))


def part2(data):
    is_valid = partial(find_solution, ["+", "*", "||"])
    return sum(item[0] for item in data if is_valid(item))


def find_solution(ops, item):
    result, args = item
    return find_solution_helper(ops, result, args[0], args[1:])


def find_solution_helper(ops, result, accum, args):
    if accum == result:
        return True
    if accum > result or not args:
        return False
    for op in ops:
        match op:
            case "+":
                next_accum = accum + args[0]
            case "*":
                next_accum = accum * args[0]
            case "||":
                next_accum = int(str(accum) + str(args[0]))
        if find_solution_helper(ops, result, next_accum, args[1:]):
            return True
    return False


def parse_data(input_file):
    data = []
    for line in input_file.readlines():
        result_str, args_str = line.split(": ")
        result = int(result_str)
        args = tuple(int(arg_str) for arg_str in args_str.split())
        data.append((result, args))
    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day07.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
