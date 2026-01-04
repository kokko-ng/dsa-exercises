"""Tests for missing_number problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def missing_number():
    """Get the user's missing_number implementation."""
    func = get_function("missing_number")
    if func is None:
        pytest.skip("Function 'missing_number' not registered. Run check(missing_number) in notebook.")
    return func


class TestMissingNumberBasic:
    """Basic functionality tests."""

    def test_missing_2(self, missing_number):
        result = missing_number([3, 0, 1])
        assert result == 2

    def test_missing_last(self, missing_number):
        result = missing_number([0, 1])
        assert result == 2

    def test_missing_8(self, missing_number):
        result = missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
        assert result == 8

    def test_missing_0(self, missing_number):
        result = missing_number([1, 2, 3])
        assert result == 0


class TestMissingNumberEdgeCases:
    """Edge case tests."""

    def test_single_element_missing_0(self, missing_number):
        result = missing_number([1])
        assert result == 0

    def test_single_element_missing_1(self, missing_number):
        result = missing_number([0])
        assert result == 1

    def test_missing_middle(self, missing_number):
        result = missing_number([0, 1, 3, 4, 5])
        assert result == 2

    def test_sorted_array(self, missing_number):
        result = missing_number([0, 1, 2, 3, 5])
        assert result == 4

    def test_reverse_sorted(self, missing_number):
        result = missing_number([5, 4, 2, 1, 0])
        assert result == 3


@pytest.mark.performance
class TestMissingNumberPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, missing_number):
        n = 10000
        nums = list(range(n + 1))
        nums.remove(5000)  # Remove middle element

        start = time.time()
        result = missing_number(nums)
        elapsed = time.time() - start

        assert result == 5000
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
