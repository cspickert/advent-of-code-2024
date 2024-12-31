import pytest
from day11 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
125 17
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 55312


def test_part2(example_input):
    data = parse_data(example_input)
    # assert part2(data) == 4
