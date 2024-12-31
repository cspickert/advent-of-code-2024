import pytest
from day09 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
2333133121414131402
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 1928


def test_part2(example_input):
    pass
