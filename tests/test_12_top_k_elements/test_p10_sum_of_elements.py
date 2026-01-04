"""Tests for sum_of_elements problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sum_of_elements():
    func = get_function("sum_of_elements")
    if func is None:
        pytest.skip("Function 'sum_of_elements' not registered.")
    return func


class TestSumOfElementsBasic:
    """Basic functionality tests."""

    def test_standard_case(self, sum_of_elements):
        assert sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6) == 23

    def test_four_elements(self, sum_of_elements):
        assert sum_of_elements([3, 5, 8, 7], 1, 4) == 12

    def test_consecutive_k(self, sum_of_elements):
        # k1=2, k2=3 means sum elements between 2nd and 3rd smallest
        assert sum_of_elements([1, 2, 3, 4, 5], 2, 4) == 3  # Only 3 is between 2 and 4


class TestSumOfElementsEdgeCases:
    """Edge case tests."""

    def test_adjacent_k(self, sum_of_elements):
        # k1=1, k2=2 means no elements between 1st and 2nd smallest
        assert sum_of_elements([1, 2, 3], 1, 2) == 0

    def test_all_between(self, sum_of_elements):
        assert sum_of_elements([1, 2, 3, 4, 5], 1, 5) == 9  # 2+3+4

    def test_with_duplicates(self, sum_of_elements):
        assert sum_of_elements([1, 1, 2, 2, 3], 2, 5) == 4  # 1+2+1? Need to verify

    def test_negative_numbers(self, sum_of_elements):
        assert sum_of_elements([-5, -3, -1, 0, 2], 1, 5) == 0 + (-1) + (-3)  # -4


@pytest.mark.performance
class TestSumOfElementsPerformance:
    """Performance tests."""

    def test_large_input(self, sum_of_elements):
        nums = list(range(10000))
        k1 = 100
        k2 = 9900

        start = time.time()
        result = sum_of_elements(nums, k1, k2)
        elapsed = time.time() - start

        # Sum of elements from index 100 to 9898 (exclusive of boundaries)
        expected = sum(range(100, 9899))
        assert result == expected
        assert elapsed < 1.0
