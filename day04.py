from pathlib import Path


def part1(data):
    return find_all_words(data, "XMAS")


def part2(data):
    return find_all_patterns(data, ["M.S", ".A.", "M.S"])


def find_all_words(data, word):
    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            for direction in get_all_directions():
                result += find_word(data, word, row, col, direction)
    return result


def find_word(data, word, start_row, start_col, direction):
    if data[start_row][start_col] != word[0]:
        return 0
    if len(word) == 1:
        return 1
    result = 0
    for row, col in get_adj_coords(data, start_row, start_col, direction):
        result += find_word(data, word[1:], row, col, direction)
    return result


def get_all_directions():
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if not (dr == 0 and dc == 0):
                yield dr, dc


def get_adj_coords(data, row, col, direction):
    dr, dc = direction
    next_row, next_col = row + dr, col + dc
    if 0 <= next_row < len(data) and 0 <= next_col < len(data[next_row]):
        yield next_row, next_col


def find_all_patterns(data, pattern):
    result = 0
    for rotation in get_all_pattern_rotations(pattern):
        result += find_pattern(data, rotation)
    return result


def find_pattern(data, pattern):
    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if check_region(data, pattern, row, col):
                result += 1
    return result


def get_all_pattern_rotations(pattern):
    yield pattern

    for _ in range(len(pattern)):
        rotated_cols = ["".join(reversed(row)) for row in pattern]
        rotated_rows = [
            "".join(col[i] for col in rotated_cols) for i in range(len(rotated_cols))
        ]
        yield rotated_rows
        pattern = rotated_rows


def check_region(data, pattern, row, col):
    pattern_dim = len(pattern)
    data_rows = data[row : row + pattern_dim]
    if len(data_rows) < pattern_dim:
        return False
    for data_row, pattern_cols in zip(data_rows, pattern):
        data_cols = data_row[col : col + pattern_dim]
        if len(data_cols) < pattern_dim:
            return False
        for data_col, pattern_col in zip(data_cols, pattern_cols):
            if pattern_col == ".":
                continue
            if data_col != pattern_col:
                return False
    return True


def parse_data(input_file):
    return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day04.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
