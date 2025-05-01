import pytest

from simple_math import SimpleMath


@pytest.fixture
def simple_math():
    return SimpleMath()

@pytest.mark.parametrize('num, result', [
    (2, 4),
    (-3, 9),
    (0, 0),
])
def test_square(simple_math, num, result):
    exp_result = simple_math.square(num)
    assert exp_result  == result


@pytest.mark.parametrize('num, result', [
    (2, 8),
    (-3, -27),
    (0, 0),
])
def test_cube(simple_math, num, result):
    exp_result = simple_math.cube(num)
    assert exp_result  == result
