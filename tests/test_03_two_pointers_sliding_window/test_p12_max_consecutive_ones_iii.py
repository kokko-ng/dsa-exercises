"""Tests for max_consecutive_ones_iii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def max_consecutive_ones_iii():
    func = get_function("max_consecutive_ones_iii")
    if func is None:
        pytest.skip("Function 'max_consecutive_ones_iii' not registered.")
    return func


class TestMaxConsecutiveBasic:
    def test_example_1(self, max_consecutive_ones_iii):
        assert max_consecutive_ones_iii([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6

    def test_example_2(self, max_consecutive_ones_iii):
        assert max_consecutive_ones_iii([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10


class TestMaxConsecutiveEdgeCases:
    def test_all_ones(self, max_consecutive_ones_iii):
        assert max_consecutive_ones_iii([1, 1, 1, 1], 2) == 4

    def test_all_zeros(self, max_consecutive_ones_iii):
        assert max_consecutive_ones_iii([0, 0, 0, 0], 2) == 2

    def test_k_zero(self, max_consecutive_ones_iii):
        assert max_consecutive_ones_iii([1, 0, 1, 1, 0], 0) == 2

    def test_k_greater_than_zeros(self, max_consecutive_ones_iii):
        assert max_consecutive_ones_iii([1, 0, 1, 0, 1], 5) == 5


@pytest.mark.performance
class TestMaxConsecutivePerformance:
    def test_large_input(self, max_consecutive_ones_iii):
        nums = [1, 0] * 50000

        start = time.time()
        result = max_consecutive_ones_iii(nums, 25000)
        elapsed = time.time() - start

        assert result == 75000
        assert elapsed < 1.0
