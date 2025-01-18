from io import StringIO

import pytest

from day16 import parse_data, part1, part2


@pytest.fixture
def example_input():
    return StringIO(
        """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 7036


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 45
