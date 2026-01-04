"""Tests for find_all_duplicates problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_all_duplicates():
    """Get the user's find_all_duplicates implementation."""
    func = get_function("find_all_duplicates")
    if func is None:
        pytest.skip("Function 'find_all_duplicates' not registered. Run check(find_all_duplicates) in notebook.")
    return func


class TestFindAllDuplicatesBasic:
    """Basic functionality tests."""

    def test_two_duplicates(self, find_all_duplicates):
        result = find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1])
        assert sorted(result) == [2, 3]

    def test_one_duplicate(self, find_all_duplicates):
        result = find_all_duplicates([1, 1, 2])
        assert result == [1]

    def test_no_duplicates(self, find_all_duplicates):
        result = find_all_duplicates([1])
        assert result == []

    def test_all_duplicates(self, find_all_duplicates):
        result = find_all_duplicates([1, 1, 2, 2, 3, 3])
        assert sorted(result) == [1, 2, 3]


class TestFindAllDuplicatesEdgeCases:
    """Edge case tests."""

    def test_single_element(self, find_all_duplicates):
        result = find_all_duplicates([1])
        assert result == []

    def test_two_same(self, find_all_duplicates):
        result = find_all_duplicates([1, 1])
        assert result == [1]

    def test_consecutive_duplicates(self, find_all_duplicates):
        result = find_all_duplicates([1, 2, 2, 3, 3, 4])
        assert sorted(result) == [2, 3]


@pytest.mark.performance
class TestFindAllDuplicatesPerformance:
    """Performance tests."""

    def test_large_input(self, find_all_duplicates):
        n = 100000
        # Half are duplicates
        nums = list(range(1, n // 2 + 1)) * 2

        start = time.time()
        result = find_all_duplicates(nums)
        elapsed = time.time() - start

        assert len(result) == n // 2
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
