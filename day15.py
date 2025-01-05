from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path


def part1(data):
    data = deepcopy(data)
    data.do_all_moves()
    return data.get_gps_sum()


def part2(data):
    data = deepcopy(data)
    data.do_all_moves()
    return data.get_gps_sum()


@dataclass
class Mapping:
    thing_to_coords: dict[str, list[tuple[int, int]]] = field(default_factory=dict)
    coords_to_thing: dict[tuple[int, int], str] = field(default_factory=dict)

    def __contains__(self, coords):
        return coords in self.coords_to_thing

    def add(self, thing_id, all_coords):
        self.thing_to_coords[thing_id] = all_coords
        for coords in all_coords:
            assert coords not in self.coords_to_thing
            self.coords_to_thing[coords] = thing_id

    def overlaps(self, other):
        return bool(set(self.coords_to_thing) & set(other.coords_to_thing))

    def move(self, from_coords, to_coords, moved=None):
        if moved is None:
            moved = set()

        dr, dc = to_coords[0] - from_coords[0], to_coords[1] - from_coords[1]

        thing = self.coords_to_thing[from_coords]
        moved.add(thing)

        src_coords = self.thing_to_coords.pop(thing)
        for src in src_coords:
            del self.coords_to_thing[src]

        dst_coords = [(src[0] + dr, src[1] + dc) for src in src_coords]
        for dst in dst_coords:
            push_thing = self.coords_to_thing.get(dst)
            if push_thing and push_thing not in moved:
                moved.add(push_thing)
                self.move(dst, (dst[0] + dr, dst[1] + dc), moved)

        self.thing_to_coords[thing] = dst_coords
        for dst in dst_coords:
            self.coords_to_thing[dst] = thing


@dataclass
class Data:
    robot: tuple[int, int]
    boxes: Mapping
    walls: Mapping
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
        new_boxes = deepcopy(self.boxes)

        dr, dc = self.get_delta(box_pos)
        new_boxes.move(box_pos, (box_pos[0] + dr, box_pos[1] + dc))

        if not new_boxes.overlaps(self.walls):
            self.boxes = new_boxes
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
        return sum(
            all_coords[0][0] * 100 + all_coords[0][1]
            for _, all_coords in self.boxes.thing_to_coords.items()
        )

    def display(self):
        max_row = max(row for row, _ in self.walls.coords_to_thing)
        max_col = max(col for _, col in self.walls.coords_to_thing)
        for row in range(max_row + 1):
            line = ""
            for col in range(max_col + 1):
                if (row, col) in self.walls:
                    line += "#"
                elif (row, col) in self.boxes:
                    line += self.boxes.coords_to_thing[(row, col)]
                elif (row, col) == self.robot:
                    line += "@"
                else:
                    line += "."
            print(line)


def parse_data(input_file, part_2=False):
    data = Data(
        robot=(0, 0),
        boxes=Mapping(),
        walls=Mapping(),
        moves=[],
    )

    map_str, moves_str = input_file.read().strip().split("\n\n")

    wall_id = 0
    box_id = 0

    for row, line in enumerate(map_str.splitlines()):
        for col, char in enumerate(line):
            if part_2:
                col *= 2
            match char:
                case "@":
                    data.robot = (row, col)
                case "#":
                    wall_id += 1
                    wall_coords = [(row, col)]
                    if part_2:
                        wall_coords += [(row, col + 1)]
                    data.walls.add(str(wall_id), wall_coords)
                case "O":
                    box_id += 1
                    box_coords = [(row, col)]
                    if part_2:
                        box_coords += [(row, col + 1)]
                    data.boxes.add(str(box_id), box_coords)

    for char in moves_str:
        if char in "<>^v":
            data.moves.append(char)

    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day15.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    input_file.seek(0)
    data = parse_data(input_file, part_2=True)
    print(part2(data))
