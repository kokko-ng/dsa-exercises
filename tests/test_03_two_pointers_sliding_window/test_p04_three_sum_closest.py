"""Tests for three_sum_closest problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def three_sum_closest():
    func = get_function("three_sum_closest")
    if func is None:
        pytest.skip("Function 'three_sum_closest' not registered.")
    return func


class TestThreeSumClosestBasic:
    def test_example_1(self, three_sum_closest):
        assert three_sum_closest([-1, 2, 1, -4], 1) == 2

    def test_example_2(self, three_sum_closest):
        assert three_sum_closest([0, 0, 0], 1) == 0

    def test_exact_match(self, three_sum_closest):
        assert three_sum_closest([1, 2, 3, 4], 6) == 6


class TestThreeSumClosestEdgeCases:
    def test_min_array(self, three_sum_closest):
        assert three_sum_closest([1, 1, 1], 3) == 3

    def test_negative_target(self, three_sum_closest):
        assert three_sum_closest([-1, 0, 1, 2], -1) == 0

    def test_large_target(self, three_sum_closest):
        assert three_sum_closest([1, 2, 3], 100) == 6

    def test_negative_numbers(self, three_sum_closest):
        assert three_sum_closest([-3, -2, -1], -6) == -6
