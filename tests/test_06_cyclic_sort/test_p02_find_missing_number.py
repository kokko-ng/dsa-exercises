"""Tests for find_missing_number problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_missing_number():
    """Get the user's find_missing_number implementation."""
    func = get_function("find_missing_number")
    if func is None:
        pytest.skip("Function 'find_missing_number' not registered. Run check(find_missing_number) in notebook.")
    return func


class TestFindMissingNumberBasic:
    """Basic functionality tests."""

    def test_missing_middle(self, find_missing_number):
        result = find_missing_number([3, 0, 1])
        assert result == 2

    def test_missing_last(self, find_missing_number):
        result = find_missing_number([0, 1])
        assert result == 2

    def test_longer_array(self, find_missing_number):
        result = find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
        assert result == 8

    def test_missing_first(self, find_missing_number):
        result = find_missing_number([1, 2, 3])
        assert result == 0


class TestFindMissingNumberEdgeCases:
    """Edge case tests."""

    def test_single_element_missing_zero(self, find_missing_number):
        result = find_missing_number([1])
        assert result == 0

    def test_single_element_missing_one(self, find_missing_number):
        result = find_missing_number([0])
        assert result == 1

    def test_all_but_last(self, find_missing_number):
        result = find_missing_number([0, 1, 2, 3, 4])
        assert result == 5


@pytest.mark.performance
class TestFindMissingNumberPerformance:
    """Performance tests."""

    def test_large_input(self, find_missing_number):
        n = 100000
        missing = 50000
        nums = [i for i in range(n + 1) if i != missing]

        start = time.time()
        result = find_missing_number(nums)
        elapsed = time.time() - start

        assert result == missing
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
