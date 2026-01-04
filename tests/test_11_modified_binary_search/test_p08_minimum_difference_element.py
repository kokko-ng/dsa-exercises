"""Tests for minimum_difference_element problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_difference_element():
    func = get_function("minimum_difference_element")
    if func is None:
        pytest.skip("Function 'minimum_difference_element' not registered.")
    return func


class TestMinimumDifferenceElementBasic:
    """Basic functionality tests."""

    def test_closest_is_lower(self, minimum_difference_element):
        assert minimum_difference_element([4, 6, 10], 7) == 6

    def test_exact_match(self, minimum_difference_element):
        assert minimum_difference_element([4, 6, 10], 4) == 4

    def test_equal_difference_return_smaller(self, minimum_difference_element):
        # Both 10 and 15 have difference 2 from 12
        assert minimum_difference_element([1, 3, 8, 10, 15], 12) == 10

    def test_closest_is_higher(self, minimum_difference_element):
        assert minimum_difference_element([1, 3, 8, 10, 15], 9) == 8


class TestMinimumDifferenceElementEdgeCases:
    """Edge case tests."""

    def test_target_smaller_than_all(self, minimum_difference_element):
        assert minimum_difference_element([4, 6, 10], 1) == 4

    def test_target_larger_than_all(self, minimum_difference_element):
        assert minimum_difference_element([4, 6, 10], 100) == 10

    def test_single_element(self, minimum_difference_element):
        assert minimum_difference_element([5], 3) == 5

    def test_two_elements_closer_to_first(self, minimum_difference_element):
        assert minimum_difference_element([1, 10], 2) == 1

    def test_two_elements_closer_to_second(self, minimum_difference_element):
        assert minimum_difference_element([1, 10], 9) == 10


@pytest.mark.performance
class TestMinimumDifferenceElementPerformance:
    """Performance tests."""

    def test_large_input(self, minimum_difference_element):
        n = 1000000
        nums = list(range(0, n * 2, 2))  # Even numbers

        start = time.time()
        result = minimum_difference_element(nums, 999999)
        elapsed = time.time() - start

        # 999999 is equidistant from 999998 and 1000000, return smaller
        assert result in [999998, 1000000]
        assert elapsed < 0.1
