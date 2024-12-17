import pytest
from day03 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 161


def test_part2(example_input):
    # data = parse_data(example_input)
    # assert part2(data) == 4
    pass
