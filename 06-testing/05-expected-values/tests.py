import pytest
from mergesort import *
import itertools


@pytest.mark.parametrize('ns', [
    list(range(k)) for k in range(101)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert (len(left) - len(right)) in [-1, 0, 1]


@pytest.mark.parametrize('left', [
    [],
    [1],
    [4, 10, 22],
    [4, 4, 4],
    [1, 3, 5, 7, 8]
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    [8, 9, 23],
    [3, 5, 9],
    [2, 4, 6, 9, 10]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)


@pytest.mark.parametrize('expected, ns', [
    (ns, list(permutation))
    for ns in [[], [1], [1, 2], [1, 4, 4, 6], [1, 2, 2, 4, 6, 9]]
    for permutation in itertools.permutations(ns)
])
def test_merge_sort(expected, ns):
    actual = merge_sort(ns)
    assert actual == expected
