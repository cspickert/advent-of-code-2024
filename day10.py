from pathlib import Path


def part1(data):
    return get_result(data, get_score)


def part2(data):
    return get_result(data, get_rating)


def get_result(data, get_value):
    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 0:
                result += get_value(data, row, col)
    return result


def get_score(data, row, col):
    assert data[row][col] == 0
    unique_destinations = set(find_destinations(data, row, col))
    return len(unique_destinations)


def get_rating(data, row, col):
    assert data[row][col] == 0
    all_destinations = list(find_destinations(data, row, col))
    return len(all_destinations)


def find_destinations(data, row, col):
    if data[row][col] == 9:
        yield (row, col)
    result = 0
    for next_row, next_col in get_adj_coords(data, row, col):
        if data[next_row][next_col] == data[row][col] + 1:
            yield from find_destinations(data, next_row, next_col)
    return result


def get_adj_coords(data, row, col):
    for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < len(data) and 0 <= next_col < len(data[next_row]):
            yield (next_row, next_col)


def parse_data(input_file):
    return [[int(char) for char in line.strip()] for line in input_file.readlines()]


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day10.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
