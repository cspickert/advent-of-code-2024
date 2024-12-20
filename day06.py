from pathlib import Path
from dataclasses import dataclass, field
from functools import cached_property


def part1(data):
    return data.simulate()


def part2(data):
    pass


@dataclass
class State:
    obstacles: set[tuple[int, int]] = field(default_factory=set)
    start: tuple[int, int] = (0, 0)
    direction: tuple[int, int] = (0, 0)
    visited: set[tuple[int, int]] = field(default_factory=set)

    @cached_property
    def min_coords(self):
        min_row = min(row for row, _ in self.obstacles)
        min_col = min(col for _, col in self.obstacles)
        return (min_row, min_col)

    @cached_property
    def max_coords(self):
        max_row = max(row for row, _ in self.obstacles)
        max_col = max(col for _, col in self.obstacles)
        return (max_row, max_col)

    @property
    def is_in_bounds(self):
        row, col = self.start
        min_row, min_col = self.min_coords
        max_row, max_col = self.max_coords
        return min_row <= row <= max_row and min_col <= col <= max_col

    def simulate(self):
        while self.is_in_bounds:
            self.visited.add(self.start)
            dr, dc = self.direction
            row, col = self.start
            next_row, next_col = row + dr, col + dc
            if (next_row, next_col) in self.obstacles:
                self.direction = get_next_direction(self.direction)
            else:
                self.start = (next_row, next_col)
        return len(self.visited)


def parse_data(input_file):
    data = State()
    for row, line in enumerate(input_file.readlines()):
        for col, char in enumerate(line):
            match char:
                case ".":
                    continue
                case "#":
                    data.obstacles.add((row, col))
                case direction if direction in ("^", "<", "v", ">"):
                    data.direction = parse_direction(direction)
                    data.start = (row, col)
                    data.visited.add(data.start)
    return data


def parse_direction(direction_str):
    match direction_str:
        case "^":
            return (-1, 0)
        case "<":
            return (0, -1)
        case "v":
            return (1, 0)
        case ">":
            return (0, 1)


def get_next_direction(direction):
    match direction:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day06.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
