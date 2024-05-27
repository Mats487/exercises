import pytest
from mystatistics import average

@pytest.mark.parametrize('ns, expected', [
    ([1, 2, 3], 2),
    ([3, 33, 333], 123),
    ([0.1, 0.1, 0.1], 0.1)
])
def test_average(ns, expected):
    actual = average(ns)
    assert actual == pytest.approx(expected), f"Average is incorrect!"