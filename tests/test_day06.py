import pytest
from io import StringIO
from day06 import parse_data, part1, part2


@pytest.fixture
def example_input():
    return StringIO("""\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""")


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 41


def test_part2(example_input):
    pass
