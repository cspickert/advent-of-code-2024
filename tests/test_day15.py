import pytest
from day15 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 2028
