from io import StringIO

import pytest

from day03 import parse_data, part1, part2


@pytest.fixture
def example_input1():
    return StringIO(
        """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    )


@pytest.fixture
def example_input2():
    return StringIO(
        """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
    )


def test_part1(example_input1):
    data = parse_data(example_input1)
    assert part1(data) == 161


def test_part2(example_input2):
    data = parse_data(example_input2)
    assert part2(data) == 48
