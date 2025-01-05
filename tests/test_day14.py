from io import StringIO

import pytest

from day14 import parse_data, part1


@pytest.fixture
def example_input():
    return StringIO(
        """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
    )


def test_part1(example_input):
    data = parse_data(example_input)
    data.size = (11, 7)
    assert part1(data) == 12
