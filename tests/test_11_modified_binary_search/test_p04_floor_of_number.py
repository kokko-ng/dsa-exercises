"""Tests for floor_of_number problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def floor_of_number():
    func = get_function("floor_of_number")
    if func is None:
        pytest.skip("Function 'floor_of_number' not registered.")
    return func


class TestFloorOfNumberBasic:
    """Basic functionality tests."""

    def test_exact_match(self, floor_of_number):
        assert floor_of_number([4, 6, 10], 6) == 1

    def test_floor_exists(self, floor_of_number):
        assert floor_of_number([1, 3, 8, 10, 15], 12) == 3

    def test_no_floor(self, floor_of_number):
        assert floor_of_number([4, 6, 10], 2) == -1

    def test_floor_first_element(self, floor_of_number):
        assert floor_of_number([1, 3, 8, 10, 15], 1) == 0

    def test_floor_last_element(self, floor_of_number):
        assert floor_of_number([1, 3, 8, 10, 15], 20) == 4


class TestFloorOfNumberEdgeCases:
    """Edge case tests."""

    def test_single_element_exact(self, floor_of_number):
        assert floor_of_number([5], 5) == 0

    def test_single_element_larger(self, floor_of_number):
        assert floor_of_number([5], 7) == 0

    def test_single_element_smaller(self, floor_of_number):
        assert floor_of_number([5], 3) == -1

    def test_target_between_elements(self, floor_of_number):
        assert floor_of_number([1, 2, 4, 5], 3) == 1

    def test_negative_numbers(self, floor_of_number):
        assert floor_of_number([-10, -5, 0, 5, 10], -3) == 1


@pytest.mark.performance
class TestFloorOfNumberPerformance:
    """Performance tests."""

    def test_large_input(self, floor_of_number):
        n = 1000000
        nums = list(range(0, n * 2, 2))  # Even numbers

        start = time.time()
        result = floor_of_number(nums, 999999)  # Odd number
        elapsed = time.time() - start

        assert result == 499999  # Index of 999998
        assert elapsed < 0.1
