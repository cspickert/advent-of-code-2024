from pathlib import Path
from dataclasses import dataclass
from copy import deepcopy


def part1(data):
    data = deepcopy(data)
    data.do_all_moves()
    return data.get_gps_sum()


def part2(data):
    pass


@dataclass
class Data:
    robot: tuple[int, int]
    boxes: set[tuple[int, int]]
    walls: set[tuple[int, int]]
    moves: list[str]

    def do_all_moves(self):
        for move in self.moves:
            self.do_move(move)

    def do_move(self, move):
        next_pos = self.get_move_pos(move)
        if next_pos in self.walls:
            pass
        elif next_pos in self.boxes:
            self.push_box(next_pos)
        else:
            self.robot = next_pos

    def push_box(self, box_pos):
        # can we push the box(es)?
        dr, dc = self.get_delta(box_pos)
        pos = box_pos
        while pos in self.boxes:
            pos = pos[0] + dr, pos[1] + dc
        if pos in self.walls:
            return
        # found empty spot
        while pos != self.robot:
            to_move = pos[0] - dr, pos[1] - dc
            if to_move in self.boxes:
                self.boxes.remove(to_move)
                self.boxes.add(pos)
            else:
                assert to_move == self.robot
                break
            pos = to_move
        self.robot = box_pos

    def get_move_pos(self, move):
        dr, dc = self.get_move_delta(move)
        return self.robot[0] + dr, self.robot[1] + dc

    def get_move_delta(self, move):
        match move:
            case "^":
                return (-1, 0)
            case "v":
                return (1, 0)
            case "<":
                return (0, -1)
            case ">":
                return (0, 1)
        raise ValueError(move)

    def get_delta(self, pos):
        return pos[0] - self.robot[0], pos[1] - self.robot[1]

    def get_gps_sum(self):
        return sum(box[0] * 100 + box[1] for box in self.boxes)


def parse_data(input_file):
    data = Data(
        robot=(0, 0),
        boxes=set(),
        walls=set(),
        moves=[],
    )

    map_str, moves_str = input_file.read().strip().split("\n\n")

    for row, line in enumerate(map_str.splitlines()):
        for col, char in enumerate(line):
            match char:
                case "@":
                    data.robot = (row, col)
                case "#":
                    data.walls.add((row, col))
                case "O":
                    data.boxes.add((row, col))

    for char in moves_str:
        if char in "<>^v":
            data.moves.append(char)

    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day15.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
