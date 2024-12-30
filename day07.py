from pathlib import Path


def part1(data):
    return sum(item[0] for item in data if find_solution(item))


def part2(data):
    pass


def find_solution(item):
    result, args = item
    return find_solution_helper(result, args[0], args[1:])


def find_solution_helper(result, accum, args):
    if accum == result:
        return True
    if accum > result or not args:
        return False
    if find_solution_helper(result, accum + args[0], args[1:]):
        return True
    if find_solution_helper(result, accum * args[0], args[1:]):
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
