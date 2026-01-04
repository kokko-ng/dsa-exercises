"""Tests for kth_largest_element problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def kth_largest_element():
    func = get_function("kth_largest_element")
    if func is None:
        pytest.skip("Function 'kth_largest_element' not registered.")
    return func


class TestKthLargestElementBasic:
    """Basic functionality tests."""

    def test_standard_case(self, kth_largest_element):
        assert kth_largest_element([3, 2, 1, 5, 6, 4], 2) == 5

    def test_with_duplicates(self, kth_largest_element):
        assert kth_largest_element([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    def test_k_equals_1(self, kth_largest_element):
        assert kth_largest_element([3, 2, 1, 5, 6, 4], 1) == 6

    def test_k_equals_length(self, kth_largest_element):
        assert kth_largest_element([3, 2, 1, 5, 6, 4], 6) == 1


class TestKthLargestElementEdgeCases:
    """Edge case tests."""

    def test_single_element(self, kth_largest_element):
        assert kth_largest_element([5], 1) == 5

    def test_two_elements(self, kth_largest_element):
        assert kth_largest_element([2, 1], 1) == 2
        assert kth_largest_element([2, 1], 2) == 1

    def test_all_same(self, kth_largest_element):
        assert kth_largest_element([5, 5, 5, 5], 3) == 5

    def test_negative_numbers(self, kth_largest_element):
        assert kth_largest_element([-1, -2, -3, -4], 2) == -2


@pytest.mark.performance
class TestKthLargestElementPerformance:
    """Performance tests."""

    def test_large_input(self, kth_largest_element):
        import random
        nums = list(range(100000))
        random.shuffle(nums)
        k = 500

        start = time.time()
        result = kth_largest_element(nums, k)
        elapsed = time.time() - start

        assert result == 100000 - k
        assert elapsed < 1.0
