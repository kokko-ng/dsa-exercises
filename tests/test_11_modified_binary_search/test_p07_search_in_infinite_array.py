"""Tests for search_in_infinite_array problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def search_in_infinite_array():
    func = get_function("search_in_infinite_array")
    if func is None:
        pytest.skip("Function 'search_in_infinite_array' not registered.")
    return func


class TestSearchInInfiniteArrayBasic:
    """Basic functionality tests."""

    def test_found_middle(self, search_in_infinite_array):
        assert search_in_infinite_array(
            [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 16
        ) == 6

    def test_not_found(self, search_in_infinite_array):
        assert search_in_infinite_array(
            [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 11
        ) == -1

    def test_found_first(self, search_in_infinite_array):
        assert search_in_infinite_array([1, 2, 3, 4, 5], 1) == 0

    def test_found_last(self, search_in_infinite_array):
        assert search_in_infinite_array([1, 2, 3, 4, 5], 5) == 4


class TestSearchInInfiniteArrayEdgeCases:
    """Edge case tests."""

    def test_single_element_found(self, search_in_infinite_array):
        assert search_in_infinite_array([5], 5) == 0

    def test_single_element_not_found(self, search_in_infinite_array):
        assert search_in_infinite_array([5], 3) == -1

    def test_two_elements(self, search_in_infinite_array):
        assert search_in_infinite_array([1, 100], 100) == 1

    def test_target_smaller_than_all(self, search_in_infinite_array):
        assert search_in_infinite_array([10, 20, 30], 5) == -1

    def test_target_larger_than_all(self, search_in_infinite_array):
        assert search_in_infinite_array([10, 20, 30], 100) == -1


@pytest.mark.performance
class TestSearchInInfiniteArrayPerformance:
    """Performance tests."""

    def test_large_input(self, search_in_infinite_array):
        n = 1000000
        nums = list(range(n))

        start = time.time()
        result = search_in_infinite_array(nums, n - 1)
        elapsed = time.time() - start

        assert result == n - 1
        assert elapsed < 0.1
