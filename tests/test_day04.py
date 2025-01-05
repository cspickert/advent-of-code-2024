from io import StringIO

import pytest

from day04 import parse_data, part1, part2


@pytest.fixture
def example_input():
    return StringIO("""\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""")


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 18


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 9
