"""Tests for ceiling_of_number problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def ceiling_of_number():
    func = get_function("ceiling_of_number")
    if func is None:
        pytest.skip("Function 'ceiling_of_number' not registered.")
    return func


class TestCeilingOfNumberBasic:
    """Basic functionality tests."""

    def test_exact_match(self, ceiling_of_number):
        assert ceiling_of_number([4, 6, 10], 6) == 1

    def test_ceiling_exists(self, ceiling_of_number):
        assert ceiling_of_number([1, 3, 8, 10, 15], 12) == 4

    def test_no_ceiling(self, ceiling_of_number):
        assert ceiling_of_number([4, 6, 10], 17) == -1

    def test_ceiling_first_element(self, ceiling_of_number):
        assert ceiling_of_number([1, 3, 8, 10, 15], 0) == 0

    def test_ceiling_last_element(self, ceiling_of_number):
        assert ceiling_of_number([1, 3, 8, 10, 15], 14) == 4


class TestCeilingOfNumberEdgeCases:
    """Edge case tests."""

    def test_single_element_exact(self, ceiling_of_number):
        assert ceiling_of_number([5], 5) == 0

    def test_single_element_smaller(self, ceiling_of_number):
        assert ceiling_of_number([5], 3) == 0

    def test_single_element_larger(self, ceiling_of_number):
        assert ceiling_of_number([5], 7) == -1

    def test_target_between_elements(self, ceiling_of_number):
        assert ceiling_of_number([1, 2, 4, 5], 3) == 2

    def test_negative_numbers(self, ceiling_of_number):
        assert ceiling_of_number([-10, -5, 0, 5, 10], -7) == 1


@pytest.mark.performance
class TestCeilingOfNumberPerformance:
    """Performance tests."""

    def test_large_input(self, ceiling_of_number):
        n = 1000000
        nums = list(range(0, n * 2, 2))  # Even numbers

        start = time.time()
        result = ceiling_of_number(nums, 999999)  # Odd number
        elapsed = time.time() - start

        assert result == 500000  # Index of 1000000
        assert elapsed < 0.1
