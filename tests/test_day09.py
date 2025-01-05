from io import StringIO

import pytest

from day09 import parse_data, part1, part2


@pytest.fixture
def example_input():
    return StringIO(
        """\
2333133121414131402
"""
    )


@pytest.fixture
def example_input2():
    return StringIO(
        """\
1313165
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 1928


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 2858


def test_part2_alt(example_input2):
    data = parse_data(example_input2)
    assert part2(data) == 169
