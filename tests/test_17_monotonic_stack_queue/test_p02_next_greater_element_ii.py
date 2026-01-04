"""Tests for next_greater_element_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def next_greater_element_ii():
    """Get the user's next_greater_element_ii implementation."""
    func = get_function("next_greater_element_ii")
    if func is None:
        pytest.skip("Function 'next_greater_element_ii' not registered. Run check(next_greater_element_ii) in notebook.")
    return func


class TestNextGreaterElementIIBasic:
    """Basic functionality tests."""

    def test_simple_circular(self, next_greater_element_ii):
        result = next_greater_element_ii([1, 2, 1])
        assert result == [2, -1, 2]

    def test_increasing_with_wrap(self, next_greater_element_ii):
        result = next_greater_element_ii([1, 2, 3, 4, 3])
        assert result == [2, 3, 4, -1, 4]

    def test_all_same(self, next_greater_element_ii):
        result = next_greater_element_ii([5, 5, 5])
        assert result == [-1, -1, -1]

    def test_increasing(self, next_greater_element_ii):
        result = next_greater_element_ii([1, 2, 3, 4])
        assert result == [2, 3, 4, -1]

    def test_decreasing(self, next_greater_element_ii):
        result = next_greater_element_ii([4, 3, 2, 1])
        assert result == [-1, 4, 4, 4]


class TestNextGreaterElementIIEdgeCases:
    """Edge case tests."""

    def test_single_element(self, next_greater_element_ii):
        result = next_greater_element_ii([42])
        assert result == [-1]

    def test_two_elements(self, next_greater_element_ii):
        result = next_greater_element_ii([1, 2])
        assert result == [2, -1]

    def test_wrap_around_needed(self, next_greater_element_ii):
        result = next_greater_element_ii([3, 1, 2])
        assert result == [-1, 2, 3]

    def test_max_at_end(self, next_greater_element_ii):
        result = next_greater_element_ii([1, 3, 2, 4])
        assert result == [3, 4, 4, -1]


@pytest.mark.performance
class TestNextGreaterElementIIPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, next_greater_element_ii):
        n = 100000
        nums = [1] * n
        nums[0] = 2  # Only first element is larger

        start = time.time()
        result = next_greater_element_ii(nums)
        elapsed = time.time() - start

        assert result[0] == -1
        assert all(r == 2 for r in result[1:])
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
