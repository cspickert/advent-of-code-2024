from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path


def part1(data):
    data = deepcopy(data)
    defrag_blocks(data)
    return get_checksum(data)


def part2(data):
    data = deepcopy(data)
    defrag_files(data)
    return get_checksum(data)


def defrag_blocks(data):
    left_ptr = 0
    right_ptr = len(data) - 1

    while left_ptr < right_ptr:
        left = data[left_ptr]
        right = data[right_ptr]

        if not left.space:
            left_ptr += 1
            continue

        if left.id != right.id:
            space = left.space
            left.space = 0

            left_ptr += 1
            left = Chunk(id=right.id, size=0, space=space)
            data.insert(left_ptr, left)
            right_ptr += 1

        moved = min(left.space, right.size)

        left.size += moved
        left.space -= moved
        right.size -= moved

        if not right.size:
            data.pop(right_ptr)
            right_ptr -= 1


def defrag_files(data):
    right_ptr = len(data) - 1
    while right_ptr > 0:
        right = data[right_ptr]
        moved = False
        for left_ptr in range(right_ptr):
            left = data[left_ptr]
            space = left.space
            if right.size and space >= right.size:
                data[right_ptr] = Chunk(id=None, size=0, space=right.size + right.space)
                data.insert(left_ptr + 1, right)
                left.space = 0
                right.space = space - right.size
                moved = True
                break
        if not moved:
            right_ptr -= 1


def get_checksum(data):
    pos = 0
    result = 0
    for left in data:
        for _ in range(left.size):
            result += left.id * pos
            pos += 1
        pos += left.space
    return result


def print_data(data):
    output = ""
    for chunk in data:
        output += str(chunk.id) * chunk.size
        output += "." * chunk.space
    print(output)


@dataclass
class Chunk:
    id: int
    size: int
    space: int


def parse_data(input_file):
    data = []
    input_str = input_file.read().strip()
    for i in range(0, len(input_str), 2):
        id = data[-1].id + 1 if data else 0
        vals_str = input_str[i : i + 2]
        if len(vals_str) < 2:
            size = int(vals_str)
            space = 0
        else:
            size_str, space_str = vals_str
            size = int(size_str)
            space = int(space_str)
        data.append(Chunk(id=id, size=size, space=space))
    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day09.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
