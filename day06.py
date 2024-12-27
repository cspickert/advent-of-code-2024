from pathlib import Path
from dataclasses import dataclass, field, replace
from functools import cached_property


def part1(data):
    data.simulate()
    return len(data.visited_coords)


def part2(data):
    data.simulate()
    return len(data.added_obstacles)


@dataclass(frozen=True)
class Position:
    start: tuple[int, int] = (0, 0)
    direction: tuple[int, int] = (0, 0)

    def move_forward(self):
        dr, dc = self.direction
        row, col = self.start
        next_row, next_col = row + dr, col + dc
        return replace(self, start=(next_row, next_col))

    def pivot(self):
        return replace(self, direction=get_next_direction(self.direction))


class LoopDetected(Exception):
    pass


@dataclass
class State:
    obstacles: set[tuple[int, int]] = field(default_factory=set)
    start_position: Position = Position()
    position: Position = Position()
    visited: set[tuple[int, int]] = field(default_factory=set)
    added_obstacles: set[tuple[int, int]] = field(default_factory=set)
    try_add_obstacles: bool = False

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
        row, col = self.position.start
        min_row, min_col = self.min_coords
        max_row, max_col = self.max_coords
        return min_row <= row <= max_row and min_col <= col <= max_col

    @property
    def visited_coords(self):
        return {position.start for position in self.visited}

    def move_forward(self):
        dr, dc = self.position.direction
        row, col = self.position.start
        next_row, next_col = row + dr, col + dc
        if (next_row, next_col) not in self.obstacles:
            self.position = self.position.move_forward()
            return True
        return False

    def pivot(self):
        self.position = self.position.pivot()

    def try_adding_obstacle(self):
        if not self.try_add_obstacles:
            return
        state = State(
            set(self.obstacles),
            self.start_position,
            self.start_position,
        )
        obstacle = self.position.start
        if obstacle not in state.obstacles:
            state.obstacles.add(obstacle)
            try:
                state.simulate()
            except LoopDetected:
                self.added_obstacles.add(obstacle)

    def simulate(self):
        while self.is_in_bounds:
            if self.position in self.visited:
                raise LoopDetected
            self.visited.add(self.position)
            if len(self.visited) > 0:
                self.try_adding_obstacle()
            if not self.move_forward():
                self.pivot()


def parse_data(input_file):
    data = State(try_add_obstacles=True)
    for row, line in enumerate(input_file.readlines()):
        for col, char in enumerate(line):
            match char:
                case ".":
                    continue
                case "#":
                    data.obstacles.add((row, col))
                case direction if direction in ("^", "<", "v", ">"):
                    direction = parse_direction(direction)
                    start = (row, col)
                    data.start_position = data.position = Position(start, direction)
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
