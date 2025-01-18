import math
from collections import defaultdict
from dataclasses import dataclass
from functools import cache
from pathlib import Path

DIRECTIONS_CW = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(data):
    return find_min_path(data)


def part2(data):
    min_costs = find_min_costs(data)
    return count_min_positions(data, min_costs)


def find_min_path(data):
    min_costs = find_min_costs(data)
    return min_costs[data.start, (0, 1)]


def count_min_positions(data, min_costs):
    positions = {data.end}

    stack = []
    for direction in DIRECTIONS_CW:
        stack.append((data.end, direction, []))

    while stack:
        pos, direction, path = stack.pop()
        cost = min_costs[pos, direction]

        if pos == data.start:
            positions.update(path)
            continue

        # Try moving forward
        next_pos = pos[0] + direction[0], pos[1] + direction[1]
        if next_pos not in data.walls:
            move_forward_state = (next_pos, direction)
            move_forward_cost = 1 + cost
            if move_forward_cost == min_costs[move_forward_state]:
                stack.append((*move_forward_state, [*path, next_pos]))

        # Try turning clockwise or counterclockwise
        for next_direction in (
            get_next_direction_clockwise(direction),
            get_next_direction_counterclockwise(direction),
        ):
            next_pos = pos[0] + next_direction[0], pos[1] + next_direction[1]
            if next_pos not in data.walls:
                next_direction_state = (pos, next_direction)
                next_direction_cost = cost + 1000
                if next_direction_cost == min_costs[next_direction_state]:
                    stack.append((*next_direction_state, [*path, next_pos]))

    return len(positions)


def find_min_costs(data):
    min_costs = defaultdict(lambda: math.inf)

    for direction in DIRECTIONS_CW:
        min_costs[data.end, direction] = 0

    # populate min costs
    stack = list(min_costs)

    while stack:
        state = stack.pop()
        pos, direction = state
        cost = min_costs[state]

        # Try moving forward
        next_pos = pos[0] + direction[0], pos[1] + direction[1]
        if next_pos not in data.walls:
            move_forward_state = (next_pos, direction)
            move_forward_cost = 1 + cost
            if move_forward_cost < min_costs[move_forward_state]:
                min_costs[move_forward_state] = move_forward_cost
                stack.append(move_forward_state)

        # Try turning clockwise or counterclockwise
        for next_direction in (
            get_next_direction_clockwise(direction),
            get_next_direction_counterclockwise(direction),
        ):
            next_pos = pos[0] + next_direction[0], pos[1] + next_direction[1]
            if next_pos not in data.walls:
                next_direction_state = (pos, next_direction)
                next_direction_cost = cost + 1000
                if next_direction_cost < min_costs[next_direction_state]:
                    min_costs[next_direction_state] = next_direction_cost
                    stack.append(next_direction_state)

    return min_costs


def get_next_direction_clockwise(direction):
    match direction:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
        case _:
            raise ValueError(f"Invalid direction: {direction}")


def get_next_direction_counterclockwise(direction):
    match direction:
        case (-1, 0):
            return (0, -1)
        case (0, -1):
            return (1, 0)
        case (1, 0):
            return (0, 1)
        case (0, 1):
            return (-1, 0)
        case _:
            raise ValueError(f"Invalid direction: {direction}")


@dataclass
class Maze:
    walls: set[tuple[int, int]]
    start: tuple[int, int]
    end: tuple[int, int]


def parse_data(input_file):
    data = Maze(walls=set(), start=(0, 0), end=(0, 0))
    for row, line in enumerate(input_file.readlines()):
        for col, char in enumerate(line.strip()):
            match char:
                case "S":
                    data.start = (row, col)
                case "E":
                    data.end = (row, col)
                case "#":
                    data.walls.add((row, col))
    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day16.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
