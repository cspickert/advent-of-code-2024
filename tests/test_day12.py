import pytest
from day12 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 1930


def test_part2(example_input):
    data = parse_data(example_input)
    # assert part2(data) == 4
