"""Tests for maximum_average_subarray problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def maximum_average_subarray():
    func = get_function("maximum_average_subarray")
    if func is None:
        pytest.skip("Function 'maximum_average_subarray' not registered.")
    return func


class TestMaxAverageBasic:
    def test_example_1(self, maximum_average_subarray):
        result = maximum_average_subarray([1, 12, -5, -6, 50, 3], 4)
        assert abs(result - 12.75) < 1e-5

    def test_example_2(self, maximum_average_subarray):
        result = maximum_average_subarray([5], 1)
        assert abs(result - 5.0) < 1e-5


class TestMaxAverageEdgeCases:
    def test_k_equals_n(self, maximum_average_subarray):
        result = maximum_average_subarray([1, 2, 3, 4, 5], 5)
        assert abs(result - 3.0) < 1e-5

    def test_negative_numbers(self, maximum_average_subarray):
        result = maximum_average_subarray([-1, -2, -3, -4], 2)
        assert abs(result - (-1.5)) < 1e-5

    def test_all_same(self, maximum_average_subarray):
        result = maximum_average_subarray([5, 5, 5, 5], 2)
        assert abs(result - 5.0) < 1e-5


@pytest.mark.performance
class TestMaxAveragePerformance:
    def test_large_input(self, maximum_average_subarray):
        nums = list(range(100000))
        k = 1000

        start = time.time()
        result = maximum_average_subarray(nums, k)
        elapsed = time.time() - start

        assert elapsed < 1.0
