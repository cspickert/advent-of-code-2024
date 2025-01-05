from collections import defaultdict
from itertools import combinations
from pathlib import Path


def part1(data):
    nodes, bounds = data
    antinodes = get_all_antinode_locations(nodes, bounds, repeat=False)
    return len(antinodes)


def part2(data):
    nodes, bounds = data
    antinodes = get_all_antinode_locations(nodes, bounds, repeat=True)
    return len(antinodes)


def get_all_antinode_locations(nodes, bounds, repeat):
    antinodes = set()
    for node in nodes:
        for loc1, loc2 in combinations(nodes[node], 2):
            antinodes.update(get_antinode_locations(loc1, loc2, bounds, repeat))
    return antinodes


def get_antinode_locations(loc1, loc2, bounds, repeat):
    result = set()
    r1, c1 = loc1
    r2, c2 = loc2
    dr = r2 - r1
    dc = c2 - c1
    if repeat:
        result.add(loc1)
        result.add(loc2)
    while True:
        anti_loc1 = (r1 - dr, c1 - dc)
        if not is_in_bounds(anti_loc1, bounds):
            break
        result.add(anti_loc1)
        if not repeat:
            break
        r1, c1 = anti_loc1
    while True:
        anti_loc2 = (r2 + dr, c2 + dc)
        if not is_in_bounds(anti_loc2, bounds):
            break
        result.add(anti_loc2)
        if not repeat:
            break
        r2, c2 = anti_loc2
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
