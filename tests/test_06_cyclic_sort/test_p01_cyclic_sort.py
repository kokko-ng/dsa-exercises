"""Tests for cyclic_sort problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def cyclic_sort():
    """Get the user's cyclic_sort implementation."""
    func = get_function("cyclic_sort")
    if func is None:
        pytest.skip("Function 'cyclic_sort' not registered. Run check(cyclic_sort) in notebook.")
    return func


class TestCyclicSortBasic:
    """Basic functionality tests."""

    def test_unsorted_array(self, cyclic_sort):
        result = cyclic_sort([3, 1, 5, 4, 2])
        assert result == [1, 2, 3, 4, 5]

    def test_longer_array(self, cyclic_sort):
        result = cyclic_sort([2, 6, 4, 3, 1, 5])
        assert result == [1, 2, 3, 4, 5, 6]

    def test_already_sorted(self, cyclic_sort):
        result = cyclic_sort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self, cyclic_sort):
        result = cyclic_sort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5]


class TestCyclicSortEdgeCases:
    """Edge case tests."""

    def test_single_element(self, cyclic_sort):
        result = cyclic_sort([1])
        assert result == [1]

    def test_two_elements(self, cyclic_sort):
        result = cyclic_sort([2, 1])
        assert result == [1, 2]

    def test_alternating(self, cyclic_sort):
        result = cyclic_sort([1, 3, 5, 2, 4])
        assert result == [1, 2, 3, 4, 5]


@pytest.mark.performance
class TestCyclicSortPerformance:
    """Performance tests."""

    def test_large_input(self, cyclic_sort):
        import random
        n = 100000
        nums = list(range(1, n + 1))
        random.shuffle(nums)

        start = time.time()
        result = cyclic_sort(nums)
        elapsed = time.time() - start

        assert result == list(range(1, n + 1))
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
