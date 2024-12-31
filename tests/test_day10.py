import pytest
from day10 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 36


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 81
