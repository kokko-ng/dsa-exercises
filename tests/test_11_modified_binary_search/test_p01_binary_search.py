"""Tests for binary_search problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def binary_search():
    """Get the user's binary_search implementation."""
    func = get_function("binary_search")
    if func is None:
        pytest.skip("Function 'binary_search' not registered. Run check(binary_search) in notebook.")
    return func


class TestBinarySearchBasic:
    """Basic functionality tests."""

    def test_found_middle(self, binary_search):
        assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

    def test_found_first(self, binary_search):
        assert binary_search([-1, 0, 3, 5, 9, 12], -1) == 0

    def test_found_last(self, binary_search):
        assert binary_search([-1, 0, 3, 5, 9, 12], 12) == 5

    def test_not_found(self, binary_search):
        assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

    def test_single_element_found(self, binary_search):
        assert binary_search([5], 5) == 0

    def test_single_element_not_found(self, binary_search):
        assert binary_search([5], 3) == -1


class TestBinarySearchEdgeCases:
    """Edge case tests."""

    def test_two_elements_first(self, binary_search):
        assert binary_search([1, 3], 1) == 0

    def test_two_elements_second(self, binary_search):
        assert binary_search([1, 3], 3) == 1

    def test_negative_numbers(self, binary_search):
        assert binary_search([-10, -5, -3, -1], -5) == 1

    def test_target_smaller_than_all(self, binary_search):
        assert binary_search([2, 4, 6, 8], 1) == -1

    def test_target_larger_than_all(self, binary_search):
        assert binary_search([2, 4, 6, 8], 10) == -1


@pytest.mark.performance
class TestBinarySearchPerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_input(self, binary_search):
        n = 1000000
        nums = list(range(0, n * 2, 2))  # Even numbers
        target = n - 2

        start = time.time()
        result = binary_search(nums, target)
        elapsed = time.time() - start

        assert result == (n - 2) // 2
        assert elapsed < 0.1, f"Solution too slow: {elapsed:.3f}s (should be < 0.1s)"
