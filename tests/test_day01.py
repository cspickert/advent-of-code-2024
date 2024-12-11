import pytest
from day01 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 11


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 31
