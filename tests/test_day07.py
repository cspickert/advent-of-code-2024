from io import StringIO

import pytest

from day07 import parse_data, part1, part2


@pytest.fixture
def example_input():
    return StringIO("""\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""")


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 3749


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 11387
