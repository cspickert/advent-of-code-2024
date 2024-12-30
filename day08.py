from pathlib import Path
from collections import defaultdict
from itertools import combinations


def part1(data):
    nodes, bounds = data
    antinodes = set()
    for node in nodes:
        for loc1, loc2 in combinations(nodes[node], 2):
            for antinode_loc in get_antinode_locations(loc1, loc2):
                if is_in_bounds(antinode_loc, bounds):
                    antinodes.add(antinode_loc)
    return len(antinodes)


def part2(data):
    pass


def get_antinode_locations(loc1, loc2):
    result = []
    r1, c1 = loc1
    r2, c2 = loc2
    dr = r2 - r1
    dc = c2 - c1
    result.append((r1 - dr, c1 - dc))
    result.append((r2 + dr, c2 + dc))
    return result


def is_in_bounds(location, bounds):
    row, col = location
    height, width = bounds
    return 0 <= row < height and 0 <= col < width


def parse_data(input_file):
    data = defaultdict(list)
    lines = [line.strip() for line in input_file.readlines()]
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != ".":
                data[char].append((row, col))
    return data, (len(lines), len(lines[0]))


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day08.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
