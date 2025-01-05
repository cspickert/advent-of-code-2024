from io import StringIO

import pytest

from day02 import parse_data, part1, part2


@pytest.fixture
def example_input():
    return StringIO(
        """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 2


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 4
