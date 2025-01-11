from io import StringIO

import pytest

from day16 import parse_data, part1


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
