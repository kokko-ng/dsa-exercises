"""Tests for find_corrupt_pair problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_corrupt_pair():
    """Get the user's find_corrupt_pair implementation."""
    func = get_function("find_corrupt_pair")
    if func is None:
        pytest.skip("Function 'find_corrupt_pair' not registered. Run check(find_corrupt_pair) in notebook.")
    return func


class TestFindCorruptPairBasic:
    """Basic functionality tests."""

    def test_basic_case(self, find_corrupt_pair):
        result = find_corrupt_pair([3, 1, 2, 5, 2])
        assert result == [2, 4]

    def test_another_case(self, find_corrupt_pair):
        result = find_corrupt_pair([3, 1, 2, 3, 6, 4])
        assert result == [3, 5]

    def test_first_duplicated(self, find_corrupt_pair):
        result = find_corrupt_pair([1, 1, 3, 4, 5])
        assert result == [1, 2]

    def test_last_duplicated(self, find_corrupt_pair):
        result = find_corrupt_pair([1, 2, 3, 4, 4])
        assert result == [4, 5]


class TestFindCorruptPairEdgeCases:
    """Edge case tests."""

    def test_small_array(self, find_corrupt_pair):
        result = find_corrupt_pair([1, 1])
        assert result == [1, 2]

    def test_adjacent_corrupt(self, find_corrupt_pair):
        result = find_corrupt_pair([1, 2, 2, 4, 5])
        assert result == [2, 3]

    def test_far_apart(self, find_corrupt_pair):
        result = find_corrupt_pair([2, 2, 3, 4, 5])
        assert result == [2, 1]


@pytest.mark.performance
class TestFindCorruptPairPerformance:
    """Performance tests."""

    def test_large_input(self, find_corrupt_pair):
        n = 10000
        nums = list(range(1, n + 1))
        # Make 5000 duplicate, remove 5001
        nums[5000] = 5000

        start = time.time()
        result = find_corrupt_pair(nums)
        elapsed = time.time() - start

        assert result == [5000, 5001]
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
