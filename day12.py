from pathlib import Path
from copy import deepcopy


def part1(data):
    return sum(
        get_area(region) * get_perimeter(region) for region in find_regions(data)
    )


def part2(data):
    return sum(get_area(region) * get_sides(region) for region in find_regions(data))


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


def get_sides(region):
    top, left, bottom, right = set(), set(), set(), set()
    for row, col in region:
        # top
        if (row - 1, col) not in region:
            top.add((row, col))
        # left
        if (row, col - 1) not in region:
            left.add((row, col))
        # bottom
        if (row + 1, col) not in region:
            bottom.add((row, col))
        # right
        if (row, col + 1) not in region:
            right.add((row, col))

    top_count, left_count, bottom_count, right_count = 0, 0, 0, 0
    for row, col in top:
        if (row, col - 1) not in top:
            top_count += 1
    for row, col in left:
        if (row - 1, col) not in left:
            left_count += 1
    for row, col in right:
        if (row - 1, col) not in right:
            right_count += 1
    for row, col in bottom:
        if (row, col - 1) not in bottom:
            bottom_count += 1
    return top_count + left_count + bottom_count + right_count


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
