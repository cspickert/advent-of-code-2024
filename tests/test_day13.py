import pytest
from day13 import parse_data, part1, part2
from io import StringIO


@pytest.fixture
def example_input():
    return StringIO(
        """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    assert part1(data) == 480


def test_part2(example_input):
    data = parse_data(example_input)
    assert part2(data) == 875318608908
