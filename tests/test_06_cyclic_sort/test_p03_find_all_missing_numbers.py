"""Tests for find_all_missing_numbers problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_all_missing_numbers():
    """Get the user's find_all_missing_numbers implementation."""
    func = get_function("find_all_missing_numbers")
    if func is None:
        pytest.skip("Function 'find_all_missing_numbers' not registered. Run check(find_all_missing_numbers) in notebook.")
    return func


class TestFindAllMissingNumbersBasic:
    """Basic functionality tests."""

    def test_two_missing(self, find_all_missing_numbers):
        result = find_all_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1])
        assert sorted(result) == [5, 6]

    def test_one_missing(self, find_all_missing_numbers):
        result = find_all_missing_numbers([1, 1])
        assert result == [2]

    def test_none_missing(self, find_all_missing_numbers):
        result = find_all_missing_numbers([1, 2, 3, 4, 5])
        assert result == []

    def test_all_duplicates(self, find_all_missing_numbers):
        result = find_all_missing_numbers([1, 1, 1, 1])
        assert sorted(result) == [2, 3, 4]


class TestFindAllMissingNumbersEdgeCases:
    """Edge case tests."""

    def test_single_element_correct(self, find_all_missing_numbers):
        result = find_all_missing_numbers([1])
        assert result == []

    def test_single_element_wrong(self, find_all_missing_numbers):
        # Array [2] but range is [1, 1] - this is invalid input per constraints
        # Testing with valid input
        result = find_all_missing_numbers([2, 2])
        assert result == [1]

    def test_alternating_duplicates(self, find_all_missing_numbers):
        result = find_all_missing_numbers([1, 1, 3, 3, 5, 5])
        assert sorted(result) == [2, 4, 6]


@pytest.mark.performance
class TestFindAllMissingNumbersPerformance:
    """Performance tests."""

    def test_large_input(self, find_all_missing_numbers):
        n = 100000
        # Create array with some duplicates
        nums = list(range(1, n + 1))
        for i in range(0, n, 100):
            nums[i] = nums[(i + 50) % n]

        start = time.time()
        result = find_all_missing_numbers(nums)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
