"""Tests for squares_of_sorted_array problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def squares_of_sorted_array():
    func = get_function("squares_of_sorted_array")
    if func is None:
        pytest.skip("Function 'squares_of_sorted_array' not registered.")
    return func


class TestSquaresBasic:
    def test_example_1(self, squares_of_sorted_array):
        assert squares_of_sorted_array([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

    def test_example_2(self, squares_of_sorted_array):
        assert squares_of_sorted_array([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

    def test_all_positive(self, squares_of_sorted_array):
        assert squares_of_sorted_array([1, 2, 3, 4]) == [1, 4, 9, 16]


class TestSquaresEdgeCases:
    def test_all_negative(self, squares_of_sorted_array):
        assert squares_of_sorted_array([-5, -4, -3, -2, -1]) == [1, 4, 9, 16, 25]

    def test_single_element(self, squares_of_sorted_array):
        assert squares_of_sorted_array([5]) == [25]
        assert squares_of_sorted_array([-5]) == [25]

    def test_zeros(self, squares_of_sorted_array):
        assert squares_of_sorted_array([-2, 0, 2]) == [0, 4, 4]


@pytest.mark.performance
class TestSquaresPerformance:
    def test_large_input(self, squares_of_sorted_array):
        nums = list(range(-5000, 5001))

        start = time.time()
        result = squares_of_sorted_array(nums)
        elapsed = time.time() - start

        assert result == sorted([x * x for x in nums])
        assert elapsed < 1.0
