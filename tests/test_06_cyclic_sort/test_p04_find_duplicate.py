"""Tests for find_duplicate problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_duplicate():
    """Get the user's find_duplicate implementation."""
    func = get_function("find_duplicate")
    if func is None:
        pytest.skip("Function 'find_duplicate' not registered. Run check(find_duplicate) in notebook.")
    return func


class TestFindDuplicateBasic:
    """Basic functionality tests."""

    def test_duplicate_at_end(self, find_duplicate):
        result = find_duplicate([1, 3, 4, 2, 2])
        assert result == 2

    def test_duplicate_at_start(self, find_duplicate):
        result = find_duplicate([3, 1, 3, 4, 2])
        assert result == 3

    def test_all_same(self, find_duplicate):
        result = find_duplicate([2, 2, 2, 2, 2])
        assert result == 2

    def test_duplicate_one(self, find_duplicate):
        result = find_duplicate([1, 1])
        assert result == 1


class TestFindDuplicateEdgeCases:
    """Edge case tests."""

    def test_small_array(self, find_duplicate):
        result = find_duplicate([1, 2, 1])
        assert result == 1

    def test_larger_duplicate(self, find_duplicate):
        result = find_duplicate([1, 2, 3, 4, 5, 5])
        assert result == 5

    def test_first_and_last(self, find_duplicate):
        result = find_duplicate([4, 1, 2, 3, 4])
        assert result == 4


@pytest.mark.performance
class TestFindDuplicatePerformance:
    """Performance tests."""

    def test_large_input(self, find_duplicate):
        n = 100000
        duplicate = 50000
        nums = list(range(1, n + 1)) + [duplicate]

        start = time.time()
        result = find_duplicate(nums)
        elapsed = time.time() - start

        assert result == duplicate
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
