from pathlib import Path
from copy import deepcopy


def part1(data):
    return sum(get_cost(region) for region in find_regions(data))


def part2(data):
    pass


def get_cost(region):
    return get_area(region) * get_perimeter(region)


def get_area(region):
    return len(region)


def get_perimeter(region):
    result = 0
    for row, col in region:
        perimeter = 4
        for next_row, next_col in get_adj_coords(None, row, col):
            if (next_row, next_col) in region:
                perimeter -= 1
        result += perimeter
    return result


def find_regions(data):
    data = deepcopy(data)
    result = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            region = find_region(data, row, col)
            if region:
                result.append(region)
    return result


def find_region(data, row, col):
    if not data[row][col]:
        return None

    plant = data[row][col]
    data[row][col] = ""

    result = set()
    result.add((row, col))
    for next_row, next_col in get_adj_coords(data, row, col):
        if data[next_row][next_col] == plant:
            result.update(find_region(data, next_row, next_col))
    return result


def get_adj_coords(data, row, col):
    for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        next_row, next_col = row + dr, col + dc
        if data is None or (
            0 <= next_row < len(data) and 0 <= next_col < len(data[next_row])
        ):
            yield (next_row, next_col)


def parse_data(input_file):
    return [list(line.strip()) for line in input_file.readlines()]


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day12.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
